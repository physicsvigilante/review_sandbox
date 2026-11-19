"""Independent PR100 #02: reviewer-owned, raw-direction Kelvin field B1 probes.

No production source or oracle is used to calculate mathematical expectations.
Every wall direction is normalized in 105-digit Decimal *from the supplied
binary64 tuple*, not after a rounded binary64 normalization. This catches
loss of tangential precision near the 1.2e-8 source-wall clearance.
"""
from __future__ import annotations

from copy import deepcopy
from decimal import Decimal, localcontext
from math import hypot, isfinite, pi
import json
from pathlib import Path
import sys

from conductor_sim.cavity_gauss import CavityCharge, GaussCavityAssembly, SealedCavity
from conductor_sim.model import Grounded, FixedNetCharge
from conductor_sim.solver import UnsupportedProblem
from conductor_sim.spherical_multicavity import (
    NamedSourcePosition, SphericalVoid, SphericalMetalGeometry,
    SphericalSigmaModel, solve_spherical_sigma,
)
from tools.m40a_spherical_reference import check_record

HEAD = "e4a64a580cf1a3eca93d4b7315ed1f4aa4ab585e"
TREE = "03eee7d1f4b97d627eb8ccf1a2ff41e837e94ea6"
LIMIT = 2e-10
REVIEW = {"head": HEAD, "tree": TREE, "reviewer_owned": True,
          "raw_real_kelvin_image_field": True, "cases": [], "refusals": [],
          "failures": []}

def log(case, **details):
    item = {"case": case, **details}
    REVIEW["cases"].append(item)
    print("SCIENCE", json.dumps(item, sort_keys=True), flush=True)

def flag(condition, message):
    if not condition:
        REVIEW["failures"].append(message)
        print("FINDING", message, flush=True)

def relative(a, b):
    return abs(a-b)/abs(b) if b else abs(a-b)

def normalize_binary(v):
    L = hypot(*v)
    return tuple(x/L for x in v)

def kelvin_normal_field_sigma(q, radius, source, raw_normal):
    """Independent real+image E_n on the *physical spherical surface*.

    Raw floating components specify a direction. Normalize with Decimal,
    then compute real charge E and Kelvin-image E (not Poisson sigma).
    """
    with localcontext() as c:
        c.prec = 105
        D = Decimal.from_float
        A, Q = D(radius), D(q)
        U = tuple(D(x) for x in source)
        V = tuple(D(x) for x in raw_normal)
        norm2 = sum((x*x for x in V), Decimal(0))
        assert norm2 > 0
        N = tuple(x/norm2.sqrt() for x in V)
        X = tuple(A*x for x in N)
        d2 = sum((x*x for x in U), Decimal(0))
        if d2 == 0:
            return float(-Q/(Decimal(4)*D(pi)*A*A))
        d = d2.sqrt()
        image_position = tuple(A*A*x/d2 for x in U)
        image_q = -Q*A/d

        def projected_field(pos, charge):
            delta = tuple(X[i]-pos[i] for i in range(3))
            r2 = sum((x*x for x in delta), Decimal(0))
            dot = sum((N[i]*delta[i] for i in range(3)), Decimal(0))
            return charge*dot/(r2*r2.sqrt())

        answer = -(projected_field(U,Q)+
                   projected_field(image_position,image_q))/(Decimal(4)*D(pi))
        return float(answer)

def one_source(q, radius, displacement, constraint):
    gauss = GaussCavityAssembly("M",(
        SealedCavity("V",(CavityCharge("q",q),)),
    ),constraint)
    geometry = SphericalMetalGeometry((0.,0.,0.),3.,(
        SphericalVoid("V",(0.,0.,0.),radius,(
            NamedSourcePosition("q", displacement),
        )),
    ))
    return solve_spherical_sigma(SphericalSigmaModel(gauss,geometry))

def refuse(title, operation, errors=(ValueError, UnsupportedProblem, TypeError)):
    try:
        operation()
    except errors as exc:
        REVIEW["refusals"].append({"case":title,"refused":True,
                                   "error":type(exc).__name__})
    else:
        REVIEW["refusals"].append({"case":title,"refused":False})
        flag(False,"expected refusal: "+title)

def pole_and_forgery():
    a, q = .85, 3.1e-9
    d = a*(1-1.2e-8)
    sol = one_source(q,a,(d,0.,0.),Grounded())
    exactly=(1.,0.,0.)
    almost=(1.+9e-13,0.,0.)
    expected = -q*(a+d)/(4*pi*a*(a-d)**2)
    native_exact=sol.inner_surface_charge_density("V",exactly)
    native_almost=sol.inner_surface_charge_density("V",almost)
    expected_field=kelvin_normal_field_sigma(q,a,(d,0.,0.),almost)
    flag(relative(native_exact,expected)<1e-12,"radial exact-unit pole theorem")
    flag(native_almost==native_exact,"radial admitted near-unit must hit same wall")
    flag(relative(native_almost,expected_field)<LIMIT,"radial Kelvin-field witness")
    saved=sol.as_dict((("V",almost),("outer",almost)))
    flag(saved["samples"][0]["unit_normal"]==[1.,0.,0.],
         "radial export unit-normal canonicality")
    flag(saved["samples"][0]["sigma_c_per_m2"]==native_exact,
         "radial export signed SI C/m2")
    flag(saved["samples"][1]["sigma_c_per_m2"]==0.,
         "grounded exterior zero uniform sigma")
    flag(check_record(saved)["sampled_local_surface_densities_checked"]==2,
         "independent JSON accepted true pole/grounded exterior")
    log("original-B1-pole", analytic=expected, real_image=expected_field,
        native_unit=native_exact, native_near=native_almost,
        exported_normal=saved["samples"][0]["unit_normal"])

    bad=deepcopy(saved)
    bad["samples"][0]["unit_normal"]=list(almost)
    old=-q*(a*a-d*d)/(4*pi*a*(a*almost[0]-d)**3)
    bad["samples"][0]["sigma_c_per_m2"]=old
    flag(relative(old,expected_field)>2e-4,
         "original B1 forged off-sphere value must differ materially")
    refuse("forged old off-surface sigma",lambda:check_record(bad),(ValueError,))
    bad["samples"][0]["sigma_c_per_m2"]=native_exact
    flag(check_record(bad)["sampled_local_surface_densities_checked"]==2,
         "accepted alternative near-unit representation with correct wall sigma")
    return sol,saved

def adversarial_oblique():
    radius=.85
    bases=((.6,.8,0.),(.48,-.64,.6))
    for b in bases:
        source=tuple(x*radius*(1-1.2e-8) for x in b)
        # Probe an angle ~5e-9 radians off the pole: within 1e-8 near-wall
        # angular length scale, so near-unit rounding must not shift sigma.
        offset=5e-9
        perturbed=(b[0]+offset,b[1]-offset*.5,b[2]+offset*.2)
        exact_unit=normalize_binary(perturbed)
        near=tuple(x*(1.+9e-13) for x in exact_unit)
        assert abs(hypot(*near)-1.)<=1e-12
        for q, mode, constraint in (
            (3.1e-9,"grounded",Grounded()),
            (-2.4e-9,"isolated",FixedNetCharge(1.1e-9)),
        ):
            sol=one_source(q,radius,source,constraint)
            expected_at_raw=kelvin_normal_field_sigma(q,radius,source,near)
            expected_at_unit=kelvin_normal_field_sigma(q,radius,source,exact_unit)
            actual=sol.inner_surface_charge_density("V",near)
            actual_unit=sol.inner_surface_charge_density("V",exact_unit)
            # Diagnostic: compare with native's double-normalized direction.
            # This is NOT a mathematical expectation for the raw direction.
            canonical = near if hypot(*near)==1. else normalize_binary(near)
            expected_canonical=kelvin_normal_field_sigma(q,radius,source,canonical)
            err_raw=relative(actual,expected_at_raw)
            err_canonical=relative(actual,expected_canonical)
            exported=sol.as_dict((("V",near),("outer",near)))
            witness=check_record(exported)
            assert witness["sampled_local_surface_densities_checked"]==2
            outer=(q+1.1e-9)/(4*pi*3.**2) if mode=="isolated" else 0.
            flag(relative(sol.outer_surface_charge_density(near),outer)<1e-13,
                 "outer uniform charge "+mode)
            flag((actual<0)==(q>0),"inner sigma correct polarity "+mode)
            flag(err_canonical<=LIMIT,"canonical normal image field "+mode)
            log("oblique-physical-raw", direction=b, mode=mode, q_c=q,
                native_sigma=actual, actual_unit=actual_unit,
                raw_real_image_sigma=expected_at_raw,
                canonical_real_image_sigma=expected_canonical,
                raw_relative_error=err_raw, canonical_relative_error=err_canonical,
                raw_normal=list(near),
                saved_normal=exported["samples"][0]["unit_normal"],
                source=list(source), outer_sigma=outer)
            flag(err_raw<=LIMIT,
                 "admitted near-unit oblique wall direction relative error "+
                 repr(b)+" "+mode+" = "+format(err_raw,".4g"))
            # The saved-evidence checker must not reject an otherwise
            # correct physically-normalized raw-direction result as forged.
            raw_saved=deepcopy(exported)
            raw_saved["samples"][0]["unit_normal"]=list(near)
            raw_saved["samples"][0]["sigma_c_per_m2"]=expected_at_raw
            try:
                check_record(raw_saved)
                accepted=True
            except ValueError as exc:
                accepted=False
                log("valid-raw-direction-witness-refused",
                    direction=b, mode=mode, reason=str(exc))
            flag(accepted,
                 "correct physical raw-direction sigma rejected by witness "+
                 repr(b)+" "+mode)

def refusals_and_controls(radial,saved):
    for name,n in (
        ("arbitrary norm 1+2e-12",(1+2e-12,0.,0.)),
        ("zero direction",(0.,0.,0.)),
        ("nonfinite nan",(float("nan"),0.,0.)),
        ("nonfinite infinity",(float("inf"),0.,0.)),
        ("Boolean direction",(True,0.,0.)),
    ):
        refuse(name,lambda n=n:radial.inner_surface_charge_density("V",n),
               (ValueError,))
    for frac in (1.,1.-5e-9):
        refuse("source on/inside clearance "+str(frac),lambda frac=frac:
               one_source(3.1e-9,.85,(.85*frac,0.,0.),Grounded()),
               (UnsupportedProblem,))
    for title,key,evil in (
        ("reversed sigma","sigma_c_per_m2",-
         saved["samples"][0]["sigma_c_per_m2"]),
        ("zero sigma","sigma_c_per_m2",0.),
        ("wrong sigma units","units",None),
        ("fake source provenance","source_role","genuine_original_jee"),
    ):
        fake=deepcopy(saved)
        if key=="units":
            fake["units"]["surface_density"]="C/m"
        elif key=="source_role":
            fake["source_role"]=evil
        else:
            fake["samples"][0][key]=evil
        refuse(title,lambda fake=fake:check_record(fake),(ValueError,))
    refuse("subqualifying signed charge",lambda:
           one_source(1e-241,.85,(0.,0.,0.),Grounded()),
           (UnsupportedProblem,))
    refuse("overqualifying charge",lambda:
           one_source(1e181,.85,(0.,0.,0.),Grounded()),
           (UnsupportedProblem,))

    for displacement in (1e-250,.17):
        sol=one_source(2e-9,.85,(displacement,0.,0.),Grounded())
        n=(.48,-.64,.6)
        actual=sol.inner_surface_charge_density("V",n)
        expected=kelvin_normal_field_sigma(2e-9,.85,(displacement,0.,0.),n)
        err=relative(actual,expected)
        flag(err<=LIMIT,"near-center/far-wall positive field "+str(displacement))
        flag(check_record(sol.as_dict((("V",n),)))["sampled_local_surface_densities_checked"]==1,
             "positive evidence verification "+str(displacement))
        log("near-center-or-ordinary", displacement_m=displacement,
            native_sigma=actual, independent_image_sigma=expected,
            relative_error=err)
    gauss=GaussCavityAssembly("M",(SealedCavity("V",(
        CavityCharge("p",3.1e-9),CavityCharge("n",-3.1e-9*(1-1e-13)),
    )),),Grounded())
    geo=SphericalMetalGeometry((0.,0.,0.),3.,(
        SphericalVoid("V",(0.,0.,0.),.85,(
            NamedSourcePosition("p",(.2,0.,0.)),
            NamedSourcePosition("n",(.2,0.,0.)),
        )),
    ))
    mixed=solve_spherical_sigma(SphericalSigmaModel(gauss,geo))
    refuse("near-cancelled false theorem zero",lambda:
           mixed.inner_surface_charge_density("V",(1.,0.,0.)),
           (UnsupportedProblem,))

def main():
    output=Path(sys.argv[1]) if len(sys.argv)>1 else Path("review100-02-results.json")
    try:
        radial,saved=pole_and_forgery()
        adversarial_oblique()
        refusals_and_controls(radial,saved)
    except Exception as exc:
        flag(False,"unexpected first-attempt execution error: "+repr(exc))
        raise
    finally:
        output.write_text(json.dumps(REVIEW,indent=2,sort_keys=True,allow_nan=False)+"\n")
        print("TOTAL",len(REVIEW["cases"]),"science cases;",
              len(REVIEW["refusals"]),"refusals;",
              len(REVIEW["failures"]),"scientific failures",flush=True)
    if REVIEW["failures"]:
        raise SystemExit("INDEPENDENT SCIENCE CHANGES REQUESTED: "+
                         "; ".join(REVIEW["failures"]))
    print("INDEPENDENT TARGETED B1 SCIENCE PASSED",flush=True)

if __name__=="__main__":
    main()
