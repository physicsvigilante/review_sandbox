"""Fresh-context M40a PR100 reviewer-owned source-pinned native and independent probes.

Mathematical expectations are computed here, not by the candidate helper or
its bundled oracle. CI retains FIRST attempt logs and a structured evidence JSON.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import replace
import json
from math import cos, hypot, isfinite, pi, sin, sqrt
from pathlib import Path
import sys

from conductor_sim.cavity_gauss import CavityCharge, GaussCavityAssembly, SealedCavity
from conductor_sim.model import FixedNetCharge, Grounded
from conductor_sim.solver import UnsupportedProblem
from conductor_sim.spherical_multicavity import (
    NamedSourcePosition, SphericalVoid, SphericalMetalGeometry, SphericalSigmaModel,
    solve_spherical_sigma,
)
from tools.m40a_spherical_reference import check_record

EXPECTED_HEAD = "f38fb82f27312f9ea1526c1a65bb93657937a0cb"
EXPECTED_TREE = "0495115a3ad0d38c71f704ae14a8842d466afe55"
OUT = {"expected_candidate_commit": EXPECTED_HEAD, "expected_candidate_tree": EXPECTED_TREE,
       "reviewer_authored": True, "new_original_jee_solved": 0,
       "cases": [], "mathematical_samples": [], "integrals": [], "refusals": []}

# Six arbitrary nonconcentric genuinely 3D voids, 12 identified charges,
# one EMPTY void, and one NET-NEUTRAL NONEMPTY void at distinct source sites.
SPECS = (
 ("A_Neutral", (-4.25,1.38,.72), .85,
     (("A_plus",3.1e-9,(.22,-.17,.11)),("A_minus",-3.1e-9,(-.19,.23,-.14)))),
 ("B_Mixed", (2.7,-3.35,1.6), 1.15,
     (("B_1",4.2e-9,(.25,.13,-.2)),("B_2",-1.3e-9,(-.31,.22,.19)),
      ("B_3",.9e-9,(.02,-.44,.05)))),
 ("C_Empty", (4.6,3.6,-2.25), .65, ()),
 ("D_Mixed", (-2.45,-3.75,-2.7), .92,
     (("D_1",-2.4e-9,(-.14,.21,.27)),("D_2",1.1e-9,(.3,-.13,.1)))),
 ("E_Mixed", (.15,4.8,3.12), 1.2,
     (("E_1",3.8e-9,(.55,.2,-.15)),("E_2",-.7e-9,(-.23,-.12,.38)),
      ("E_3",-1.6e-9,(-.4,.15,-.2)))),
 ("F_Mixed", (5.2,-.45,3.85), .7,
     (("F_1",-1.7e-9,(-.11,.31,.04)),("F_2",.5e-9,(.17,-.16,.11)))),
)
CENTER = (.35,-.21,.4)
OUTER_R = 12.0

def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(s,x): return tuple(s*a for a in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def length(x): return hypot(*x)
def unit(x): return scale(1/length(x), x)
def close(got,expected,label,rtol=3e-10,atol=5e-22):
    assert isfinite(got) and isfinite(expected), label
    err=abs(got-expected)
    assert err<=max(atol,rtol*max(abs(got),abs(expected))), f"{label}: {got:.18g} != {expected:.18g}; error {err:.6g}"

def note(name, payload=None):
    print("REVIEW:",name,("" if payload is None else json.dumps(payload,sort_keys=True)),flush=True)

def model():
    cavities=[]; voids=[]
    for cid,c,r,charges in SPECS:
        cavities.append(SealedCavity(cid,tuple(CavityCharge(sid,q) for sid,q,_ in charges)))
        voids.append(SphericalVoid(cid,c,r,tuple(NamedSourcePosition(sid,add(c,rel))
                                                for sid,_,rel in charges)))
    gauss=GaussCavityAssembly("ReviewMetal",tuple(cavities),FixedNetCharge(2.8e-9))
    geom=SphericalMetalGeometry(CENTER,OUTER_R,tuple(voids))
    return SphericalSigmaModel(gauss,geom)

def independently_verify_geometry(m):
    geo=m.geometry
    outer_gaps=[geo.outer_radius_m-length(sub(v.center_m,geo.outer_center_m))-v.radius_m
                for v in geo.voids]
    pair_gaps=[length(sub(v.center_m,w.center_m))-v.radius_m-w.radius_m
               for i,v in enumerate(geo.voids) for w in geo.voids[i+1:]]
    source_gaps=[v.radius_m-length(sub(s.position_m,v.center_m))
                 for v in geo.voids for s in v.positions]
    assert len(geo.voids)==6 and sum(len(v.positions) for v in geo.voids)==12
    assert min(outer_gaps)>0 and min(pair_gaps)>0 and min(source_gaps)>0
    for v in geo.voids:
        assert v.cavity_id!="outer"
        assert len({p.source_id for p in v.positions})==len(v.positions)
    result={"voids":len(geo.voids),"sources":sum(len(v.positions) for v in geo.voids),
            "minimum_outer_metal_gap_m":min(outer_gaps),
            "minimum_intervoid_metal_gap_m":min(pair_gaps),
            "minimum_source_wall_gap_m":min(source_gaps),
            "source_ids":[s.source_id for v in geo.voids for s in v.positions]}
    note("independent_geometry",result)
    OUT["geometry"]=result

# Direct real-charge plus external Kelvin-image NORMAL ELECTRIC FIELD.
# Dirichlet spherical boundary derivation: image at a^2 u/|u|^2,
# image strength -q a/|u|, and sigma_metal=-epsilon*(E_cavity dot n).
# This code never calls the candidate density or its bundled reference.
def image_field_sigma(radius, named, n):
    wall=scale(radius,n)
    total=0.
    for q,u in named:
        if not q: continue
        d=length(u)
        if d==0:
            total-=q/(4*pi*radius**2)
            continue
        ui=scale(radius*radius/(d*d),u)
        qi=-q*radius/d
        dr=sub(wall,u); di=sub(wall,ui)
        total-=(q*dot(n,dr)/length(dr)**3 + qi*dot(n,di)/length(di)**3)/(4*pi)
    return total

# Second, independent one-sided finite difference of the DIRICHLET
# real+Kelvin-image potential, not a copy of the surface-density kernel.
def dirichlet_fd_sigma(radius,named,n,h_fraction=1e-6):
    def potential_charge_numerator(r):
        p=scale(r,n)
        total=0.
        for q,u in named:
            if not q: continue
            d=length(u)
            if d==0:
                total += q/length(p)-q/radius
            else:
                im=scale(radius*radius/d**2,u)
                qim=-q*radius/d
                total += q/length(sub(p,u))+qim/length(sub(p,im))
        return total
    h=h_fraction*radius
    # V(a)=0 by the image boundary condition.
    return -potential_charge_numerator(radius-h)/(4*pi*h)

def named_sources(m,cid):
    cav=next(c for c in m.gauss_assembly.cavities if c.cavity_id==cid)
    void=next(v for v in m.geometry.voids if v.cavity_id==cid)
    byid={p.source_id:p.position_m for p in void.positions}
    return [(s.charge_c,sub(byid[s.source_id],void.center_m)) for s in cav.sources]

def quadrature(m,cid,Nmu,Nphi,use_native):
    void=next(v for v in m.geometry.voids if v.cavity_id==cid)
    sol=solve_spherical_sigma(m) if use_native else None
    named=named_sources(m,cid)
    total=0.
    for i in range(Nmu):
        mu=-1+(i+.5)*2/Nmu
        transverse=sqrt(1-mu*mu)
        for j in range(Nphi):
            phi=2*pi*(j+.5)/Nphi
            n=(transverse*cos(phi),transverse*sin(phi),mu)
            sigma=(sol.inner_surface_charge_density(cid,n)
                   if use_native else image_field_sigma(void.radius_m,named,n))
            total += sigma
    return total*void.radius_m**2*(2/Nmu)*(2*pi/Nphi)

def rejects(name,fn):
    try:
        fn()
    except (ValueError,TypeError,UnsupportedProblem) as exc:
        record={"case":name,"error":type(exc).__name__,"detail":str(exc)[:160]}
        OUT["refusals"].append(record)
        note("expected_refusal",record)
        return
    raise AssertionError("INVALID PHYSICAL/PROVENANCE INPUT ACCEPTED: "+name)

def main():
    m=model()
    independently_verify_geometry(m)
    s=solve_spherical_sigma(m)
    assert len(s.gauss_ledger.faces)==6
    assert [f.cavity_id for f in s.gauss_ledger.faces]==[x[0] for x in SPECS]
    assert s.gauss_ledger.faces[0].induced_inner_face_charge_c==0.
    assert s.gauss_ledger.faces[2].induced_inner_face_charge_c==0.
    mode={}
    normals=[unit((.3,.4,.866025403784)),unit((-.47,.25,.85)),unit((.39,-.81,.44))]
    probes=[(cid,n) for cid in ("A_Neutral","B_Mixed","D_Mixed","E_Mixed","F_Mixed")
            for n in normals] + [("C_Empty",normals[0]),("outer",normals[1]),("outer",normals[2])]
    for label,constraint in (("isolated",m.gauss_assembly.constraint),("grounded",Grounded())):
        mm=replace(m,gauss_assembly=replace(m.gauss_assembly,constraint=constraint))
        sol=solve_spherical_sigma(mm)
        doc=sol.as_dict(probes)
        witness=check_record(doc)
        assert witness["point_sources_checked"]==12 and witness["cavities_checked"]==6
        inner={}
        for cid in ("A_Neutral","B_Mixed","D_Mixed","E_Mixed","F_Mixed"):
            R=next(v.radius_m for v in mm.geometry.voids if v.cavity_id==cid)
            for k,n in enumerate(normals):
                got=sol.inner_surface_charge_density(cid,n)
                reference=image_field_sigma(R,named_sources(mm,cid),n)
                close(got,reference,cid+" Kelvin image normal field")
                fd=dirichlet_fd_sigma(R,named_sources(mm,cid),n)
                close(got,fd,cid+" finite difference potential",rtol=5e-5,atol=5e-17)
                inner[cid+":"+str(k)]=got
                OUT["mathematical_samples"].append({"state":label,"cavity":cid,"normal":n,
                    "production_sigma_c_per_m2":got,"independent_kelvin_field":reference,
                    "independent_dirichlet_finite_difference":fd})
        assert abs(inner["A_Neutral:0"])>1e-13
        assert abs(inner["A_Neutral:1"])>1e-13
        assert sol.inner_surface_charge_density("C_Empty",normals[0])==0.
        Q=sol.gauss_ledger.outer_face_charge_c
        outer_ref=Q/(4*pi*OUTER_R**2)
        close(sol.outer_surface_charge_density(normals[1]),outer_ref,label+" outer density")
        assert sol.outer_surface_charge_density(normals[1])==sol.outer_surface_charge_density(normals[2])
        mode[label]={"Qmetal":sol.gauss_ledger.net_metal_charge_c,
                     "Qouter":Q,"flux":sol.gauss_ledger.exterior_electric_flux_v_m,
                     "outer_sigma":outer_ref,"inner":inner,"witness":witness}
        note(label+"_global_charge_flux", {k:v for k,v in mode[label].items() if k!="inner"})
    assert mode["isolated"]["Qmetal"]==2.8e-9
    close(mode["isolated"]["Qouter"],
          2.8e-9+sum(q for _,_,_,ss in SPECS for _,q,_ in ss),
          "isolated total source charge")
    assert mode["grounded"]["Qouter"]==0. and mode["grounded"]["outer_sigma"]==0.
    close(mode["grounded"]["Qmetal"],-sum(q for _,_,_,ss in SPECS for _,q,_ in ss),
          "grounded induced metal net charge")
    for k in mode["isolated"]["inner"]:
        assert mode["isolated"]["inner"][k]==mode["grounded"]["inner"][k]
    OUT["modes"]={label:{k:v for k,v in data.items() if k!="inner"} for label,data in mode.items()}
    note("grounding_invariant_inner",len(mode["isolated"]["inner"]))

    # Two independent 2D quadrature resolutions and native sampled quadrature.
    for cid in ("B_Mixed","E_Mixed","A_Neutral"):
        face=next(f for f in s.gauss_ledger.faces if f.cavity_id==cid)
        target=face.induced_inner_face_charge_c
        independent_lo=quadrature(m,cid,64,128,False)
        independent_hi=quadrature(m,cid,128,256,False)
        native_lo=quadrature(m,cid,24,48,True)
        native_hi=quadrature(m,cid,48,96,True)
        err=abs(independent_hi-target)
        assert err<max(1e-13,abs(target)*3e-4), (cid,independent_hi,target)
        assert abs(native_hi-target)<max(2e-13,abs(target)*9e-4), (cid,native_hi,target)
        assert abs(independent_hi-target)<=abs(independent_lo-target)+2e-14
        data={"cavity":cid,"Gauss_integrated_charge_c":target,
              "independent_2D_64x128":independent_lo,
              "independent_2D_128x256":independent_hi,
              "native_2D_24x48":native_lo,
              "native_2D_48x96":native_hi,
              "independent_absolute_error_c":err}
        OUT["integrals"].append(data);note("full_2D_spherical_integral",data)

    # Uniform centered-source and off-center pole limits are reviewer-authored.
    q=2.2e-9; r=.7; d=.3
    uniform=-(q/(4*pi*r*r))
    close(image_field_sigma(r,[(q,(0,0,0))],(1.,0.,0.)),uniform,"centered")
    near=image_field_sigma(r,[(q,(d,0,0))],(1.,0.,0.))
    far=image_field_sigma(r,[(q,(d,0,0))],(-1.,0.,0.))
    close(near,-q*(r+d)/(4*pi*r*(r-d)**2),"near pole",rtol=2e-12)
    close(far,-q*(r-d)/(4*pi*r*(r+d)**2),"far pole",rtol=2e-12)
    note("analytic_centered_and_poles",{"uniform":uniform,"near":near,"far":far})

    old=s.inner_surface_charge_density("A_Neutral",normals[0])
    void=m.geometry.voids[0]; p=void.positions[0]
    shifted=replace(p,position_m=add(p.position_m,(.09,-.06,.02)))
    newer=replace(m,geometry=replace(m.geometry,voids=(
        replace(void,positions=(shifted,)+void.positions[1:]),)+m.geometry.voids[1:]))
    sn=solve_spherical_sigma(newer)
    new=sn.inner_surface_charge_density("A_Neutral",normals[0])
    assert abs(new-old)>1e-12 and sn.gauss_ledger.faces[0].induced_inner_face_charge_c==0.
    assert solve_spherical_sigma(m).inner_surface_charge_density("A_Neutral",normals[0])==old
    note("immutable_source_repositioning",{"old_sigma":old,"new_sigma":new})

    revsrc=replace(m.gauss_assembly,cavities=tuple(replace(c,sources=tuple(reversed(c.sources)))
                                                  for c in m.gauss_assembly.cavities))
    revgeo=replace(m.geometry,voids=tuple(replace(v,positions=tuple(reversed(v.positions)))
                                            for v in m.geometry.voids))
    reordered=solve_spherical_sigma(replace(m,gauss_assembly=revsrc,geometry=revgeo))
    close(reordered.inner_surface_charge_density("B_Mixed",normals[0]),
          s.inner_surface_charge_density("B_Mixed",normals[0]),"source order")
    perm=(5,3,1,4,0,2)
    mp=replace(m,gauss_assembly=replace(m.gauss_assembly,
                       cavities=tuple(m.gauss_assembly.cavities[i] for i in perm)),
               geometry=replace(m.geometry,voids=tuple(m.geometry.voids[i] for i in perm)))
    close(solve_spherical_sigma(mp).inner_surface_charge_density("E_Mixed",normals[1]),
          s.inner_surface_charge_density("E_Mixed",normals[1]),"cavity permutation")
    def rot(p): return (-p[1],p[0],p[2])
    def trans(p): return add(p,(.37,-.42,.23))
    def transform(fn):
        gg=m.geometry
        return replace(m,geometry=SphericalMetalGeometry(fn(gg.outer_center_m),gg.outer_radius_m,
           tuple(SphericalVoid(v.cavity_id,fn(v.center_m),v.radius_m,
                 tuple(NamedSourcePosition(p.source_id,fn(p.position_m))
                       for p in v.positions)) for v in gg.voids)))
    close(solve_spherical_sigma(transform(rot)).inner_surface_charge_density("D_Mixed",rot(normals[0])),
          s.inner_surface_charge_density("D_Mixed",normals[0]),"rotated geometry and normal",rtol=8e-13)
    close(solve_spherical_sigma(transform(trans)).inner_surface_charge_density("D_Mixed",normals[0]),
          s.inner_surface_charge_density("D_Mixed",normals[0]),"translated world",rtol=8e-13)
    note("source_order_cavity_order_rotation_translation",{"passed":True})

    rejects("Boolean surface normal",lambda:s.inner_surface_charge_density("B_Mixed",(True,0.,0.)))
    rejects("nonunit surface normal",lambda:s.outer_surface_charge_density((.2,0.,0.)))
    rejects("nonfinite surface normal",lambda:s.outer_surface_charge_density((float('nan'),0,0)))
    rejects("Boolean charge",lambda:CavityCharge("bad",True))
    rejects("Boolean radius",lambda:SphericalVoid("bad",(0,0,0),True))
    rejects("Boolean position",lambda:NamedSourcePosition("bad",(True,0,0)))
    rejects("fake surface ID",lambda:s.inner_surface_charge_density("outer",normals[0]))
    rejects("fake original charge placement",lambda:SphericalSigmaModel(m.gauss_assembly,
        replace(m.geometry,voids=(replace(void,positions=(
          NamedSourcePosition("B_1",p.position_m),)+void.positions[1:]),)+m.geometry.voids[1:])))
    rejects("duplicate source placement",lambda:replace(void,positions=(
        void.positions[0],void.positions[0])))
    rejects("source on wall",lambda:SphericalSigmaModel(m.gauss_assembly,
        replace(m.geometry,voids=(replace(void,positions=(
           replace(p,position_m=add(void.center_m,(void.radius_m,0,0))),)+void.positions[1:]),)+m.geometry.voids[1:])))
    rejects("source below clearance",lambda:SphericalSigmaModel(m.gauss_assembly,
        replace(m.geometry,voids=(replace(void,positions=(
           replace(p,position_m=add(void.center_m,(void.radius_m*(1-5e-9),0,0))),)+void.positions[1:]),)+m.geometry.voids[1:])))
    rejects("cavities touch/overlap",lambda:SphericalSigmaModel(m.gauss_assembly,
        replace(m.geometry,voids=(void,replace(m.geometry.voids[1],center_m=void.center_m))+m.geometry.voids[2:])))
    rejects("void exits exterior sphere",lambda:SphericalSigmaModel(m.gauss_assembly,
        replace(m.geometry,voids=(replace(void,center_m=(11.7,0.,0.)),)+m.geometry.voids[1:])))
    rejects("missing cavity geometry",lambda:SphericalSigmaModel(m.gauss_assembly,
        replace(m.geometry,voids=m.geometry.voids[:-1])))
    rejects("Boolean outer radius",lambda:SphericalMetalGeometry(CENTER,True,m.geometry.voids))
    rejects("extra 3D E",lambda:s.electric_field_at((1,0,0)))
    rejects("invented source force",lambda:s.force_on_source("A_plus"))
    rejects("invented wire time",lambda:s.ground_wire_current(1.))
    rejects("point potential",lambda:s.potential_at((0,0,0)))

    # Qualified just-above-cutoff wall position should remain finite, no sign/zero fiction.
    very_near=replace(p,position_m=add(void.center_m,(void.radius_m*(1-1.2e-8),0,0)))
    near_model=replace(m,geometry=replace(m.geometry,voids=(
       replace(void,positions=(very_near,)+void.positions[1:]),)+m.geometry.voids[1:]))
    near_sigma=solve_spherical_sigma(near_model).inner_surface_charge_density("A_Neutral",(1.,0.,0.))
    assert isfinite(near_sigma) and near_sigma!=0.
    note("admitted_near_wall",{"sigma":near_sigma})

    # Small centered displacement, and very small/large *admitted* charge regimes.
    for tiny in (5e-324,1e-250,1e-160,1e-50,1e-12):
        one=GaussCavityAssembly("m",(SealedCavity("V",(CavityCharge("q",2e-9),)),),Grounded())
        g=SphericalMetalGeometry((0.,0.,0.),3.,(
           SphericalVoid("V",(0.,0.,0.),.5,(NamedSourcePosition("q",(tiny,0,0)),)),))
        a=solve_spherical_sigma(SphericalSigmaModel(one,g)).as_dict((("V",(1.,0.,0.)),))
        assert check_record(a)["sampled_local_surface_densities_checked"]==1
    tiny_q=GaussCavityAssembly("m",(SealedCavity("V",(CavityCharge("q",1e-240),)),),Grounded())
    tiny_g=SphericalMetalGeometry((0.,0.,0.),1e6,(
        SphericalVoid("V",(0.,0.,0.),2e5,(NamedSourcePosition("q",(0.,0.,0.)),)),))
    t=solve_spherical_sigma(SphericalSigmaModel(tiny_q,tiny_g))
    assert 0<abs(t.inner_surface_charge_density("V",(1.,0.,0.)))<1e-240
    assert check_record(t.as_dict((("V",(1.,0.,0.)),)))["sampled_local_surface_densities_checked"]==1
    large_q=GaussCavityAssembly("m",(SealedCavity("V",(CavityCharge("q",1e180),)),),Grounded())
    large_g=SphericalMetalGeometry((0.,0.,0.),1e-4,(
        SphericalVoid("V",(0.,0.,0.),1e-6,(NamedSourcePosition("q",(0.,0.,0.)),)),))
    huge=solve_spherical_sigma(SphericalSigmaModel(large_q,large_g))
    assert isfinite(huge.inner_surface_charge_density("V",(1.,0.,0.)))
    rejects("charge below qualified range",lambda:SphericalSigmaModel(
        replace(one,cavities=(SealedCavity("V",(CavityCharge("q",1e-250),)),)),g))
    rejects("charge above qualified range",lambda:SphericalSigmaModel(
        replace(one,cavities=(SealedCavity("V",(CavityCharge("q",2e180),)),)),g))
    note("extreme_finite_and_near_center",{"tiny_sigma":t.inner_surface_charge_density("V",(1.,0.,0.)),
                                         "huge_sigma":huge.inner_surface_charge_density("V",(1.,0.,0.))})

    doc=s.as_dict(probes)
    for label,mutator in (
        ("fake original JEE solved",lambda d:d.__setitem__("original_workbook_items_newly_solved",1)),
        ("fake local map claim",lambda d:d.__setitem__("irregular_3d_fields_qualified",True)),
        ("fake time evolution",lambda d:d.__setitem__("time_evolution_defined",True)),
        ("false SI units",lambda d:d["units"].__setitem__("surface_density","nC/m2")),
        ("false grounded flag",lambda d:d["gauss"]["conductor"].__setitem__("constraint","grounded_zero_potential")),
        ("injected local E field",lambda d:d.__setitem__("electric_field_at",(1,2,3))),
        ("forged local sigma",lambda d:d["samples"][0].__setitem__("sigma_c_per_m2",0)),
        ("false face flux",lambda d:d["gauss"].__setitem__("outer_face_total_charge_c",0)),
        ("swapped placement ID",lambda d:d["voids"][0]["source_positions"][0].__setitem__("source_id","B_1")),
        ("boolean JSON position",lambda d:d["voids"][0]["source_positions"][0]["position_m"].__setitem__(0,True)),
    ):
        forged=deepcopy(doc)
        mutator(forged)
        rejects("standalone JSON "+label,lambda x=forged:check_record(x))
    forged_native=solve_spherical_sigma(m)
    object.__setattr__(forged_native.gauss_ledger,"outer_face_charge_c",0.0)
    rejects("native Gauss ledger low-level tampering",lambda:forged_native.as_dict(probes))
    note("unfamiliar_native_and_independent_review_COMPLETE")
    OUT["status"]="PASS_FIRST_ATTEMPT"
    output=Path(sys.argv[1] if len(sys.argv)>1 else "../review100-chatb.json")
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(OUT,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    note("evidence_written",{"file":str(output),"refusals":len(OUT["refusals"]),
                             "local_probe_comparisons":len(OUT["mathematical_samples"])})

if __name__=="__main__":
    main()
