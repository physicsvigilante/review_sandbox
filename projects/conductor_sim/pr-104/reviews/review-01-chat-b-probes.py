"""Chat B reproducibility probe for conductor_sim PR 104.

Reviewer-authored, not a production test. Run on each extracted pinned source:
    PYTHONPATH=<source>/src:<source> python review-01-chat-b-probes.py <source>
The full first-attempt/second-attempt stdout and original larger harness are
preserved separately in the conversation's reviewer evidence ZIP.
"""
import copy
import fnmatch
import json
import math
import pathlib
import re
import sys
from dataclasses import replace
from decimal import Decimal, getcontext

root = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root))
sys.path.insert(0, str(root / "src"))
candidate = (root / "src/conductor_sim/_directions.py").exists()

from conductor_sim.model import (ConductingPlane, ElectrostaticProblem, Grounded,
    FixedNetCharge, PointCharge, SphericalShell, EPSILON_0)
from conductor_sim.grounded_plane import GroundedPlaneBackend
from conductor_sim.nested_shells import NestedShellBackend
from conductor_sim.motion_1d import Motion1DSpec, integrate_motion_1d
from conductor_sim.motion_2d import _unit as plane_unit
from conductor_sim.visualization import SliceSpec, unit as visual_unit
from conductor_sim.cavity_gauss import CavityCharge, SealedCavity, GaussCavityAssembly
from conductor_sim.spherical_multicavity import (
    NamedSourcePosition, SphericalVoid, SphericalMetalGeometry,
    SphericalSigmaModel, solve_spherical_sigma)
from conductor_sim.spherical_sigma_atlas import surface_atlas_manifest
from tools.m40b_spherical_atlas_reference import check_manifest

T = math.ulp(0.0)
raw = (-7*T, 5*T, -2*T)  # New signed/oblique input, not developer's rays
getcontext().prec = 90
den = float(sum(Decimal(i)**2 for i in (-7, 5, -2)).sqrt())
n = tuple(i/den for i in (-7, 5, -2))
def norm(v): return math.hypot(*v)
def unit(v): return tuple(a/norm(v) for a in v)
def plus(*vs): return tuple(sum(v[i] for v in vs) for i in range(3))
def minus(a,b): return tuple(a[i]-b[i] for i in range(3))
def mul(x,s): return tuple(s*a for a in x)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def near(x,y,atol=2e-19): return abs(x-y) <= atol + 7e-13*max(abs(x),abs(y))
def near3(a,b,atol=2e-19): return all(near(x,y,atol) for x,y in zip(a,b))
def accept(doc):
    try: return {"accepted": True, "summary":check_manifest(doc)}
    except ValueError as e: return {"accepted":False, "error":str(e)}

t1 = unit((n[1], -n[0], 0.))
t2 = unit(cross(n,t1))
p0 = (.42, -.73, .21)
a = plus(p0, mul(n,.87), mul(t1,.31), mul(t2,-.16))
b = plus(p0, mul(n,1.41), mul(t1,-.24), mul(t2,.19))
observation = plus(p0, mul(n,.72), mul(t1,.52), mul(t2,.34))
surface = plus(p0, mul(t1,.21), mul(t2,-.26))
sites = ((1.7e-9,a),(-.63e-9,b))
mirror = lambda p: minus(p, mul(n,2*dot(minus(p,p0),n)))
K=1/(4*math.pi*EPSILON_0)
V=0.; E=[0.]*3; sigma=0.
for q,p in sites:
    v=minus(observation,p); w=minus(observation,mirror(p))
    d=norm(v); di=norm(w)
    V += K*q*(1/d-1/di)
    for j in range(3): E[j]+=K*q*(v[j]/d**3-w[j]/di**3)
    sigma -= q*dot(minus(p,p0),n)/(2*math.pi*norm(minus(surface,p))**3)
F=[0.]*3
for idx,(q,p) in enumerate(sites):
    v=minus(a,mirror(p));d=norm(v)
    for j in range(3): F[j]-=K*sites[0][0]*q*v[j]/d**3
    if idx:
        v=minus(a,p);d=norm(v)
        for j in range(3):F[j]+=K*sites[0][0]*q*v[j]/d**3

plane=ConductingPlane(point_m=p0,normal=raw)
problem=ElectrostaticProblem(charges=tuple(PointCharge(q,p) for q,p in sites),conductors=(plane,))
sol=GroundedPlaneBackend().solve(problem)
# Native source order is position-canonicalized, not author-list order.
idx=next(i for i,s in enumerate(sol.sources) if s.position_m==a)
actual={"normal":plane.normal,
    "V":sol.potential_at(observation),
    "E":sol.electric_field_at(observation),
    "F":sol.force_on_charge_n(idx),
    "sigma":sol.surface_charge_density_at("outer",surface)}
expected={"normal":n,"V":V,"E":E,"F":F,"sigma":sigma}
equal_physics=(near(actual["V"],V) and near3(actual["E"],E) and
    near3(actual["F"],F,1e-25) and near(actual["sigma"],sigma,1e-25))
assert equal_physics == candidate, (expected, actual)

# Real native symmetry-certified 1D integration, not a synthetic axis adapter.
cp=ElectrostaticProblem(charges=(PointCharge(7e-10),),
   conductors=(SphericalShell(.9,1.2,Grounded()),))
def run_motion(v):
    spec=Motion1DSpec(cp,0,.002,v,.16,.018,.006)
    return integrate_motion_1d(spec,NestedShellBackend())
ordinary=run_motion((-7,5,-2))
try: tiny=run_motion(raw); tiny_motion={"completed":True, "samples":len(tiny.samples),
    "displacement_m":tiny.samples[-1].displacement_m,
    "position_m":tiny.samples[-1].position_m}
except Exception as e: tiny_motion={"completed":False,"exception":str(e)}
assert tiny_motion["completed"] == candidate
if candidate:
    assert tiny_motion["samples"]==4
    assert near3(tiny_motion["position_m"],ordinary.samples[-1].position_m,1e-15)

s=SliceSpec(origin_m=p0,u=raw,v=t2)
p=s.world((.29,-.18))
slice_evidence={"distance_m":norm(minus(p,p0)), "xy":s.project(p)[:2],
    "normal_length":norm(s.normal)}
if candidate:
    assert near(slice_evidence["distance_m"],math.hypot(.29,.18),1e-14)
    assert near3((slice_evidence["xy"][0],slice_evidence["xy"][1],0.),(.29,-.18,0.),1e-14)

# Fresh source inventories, not the packaged teacher example.
def atlas(order):
    cavities={
      "A":SealedCavity("A",(CavityCharge("a_plus",2.4e-9),CavityCharge("a_minus",-1.1e-9))),
      "E":SealedCavity("E"),
      "B":SealedCavity("B",(CavityCharge("b_neg",-.7e-9),))}
    voids={
      "A":SphericalVoid("A",(-1.16,.37,.24),.65,(
         NamedSourcePosition("a_plus",(-1.02,.46,.31)),
         NamedSourcePosition("a_minus",(-1.37,.29,.08)))),
      "E":SphericalVoid("E",(.25,-1.78,-.25),.5),
      "B":SphericalVoid("B",(1.38,.85,.48),.7,(
         NamedSourcePosition("b_neg",(1.42,.78,.43)),))}
    g=GaussCavityAssembly("ReviewMetal",tuple(cavities[z] for z in order),
                         FixedNetCharge(.39e-9),EPSILON_0)
    geom=SphericalMetalGeometry((.19,-.13,.05),4.6,tuple(voids[z] for z in order))
    m=SphericalSigmaModel(g,geom)
    grd=replace(m,gauss_assembly=replace(g,constraint=Grounded()))
    return surface_atlas_manifest(solve_spherical_sigma(m),solve_spherical_sigma(grd),
                                  directions=((0.,1.,0.),(.6,.8,0.),(-1.,0.,0.)))
cavity_evidence={}
for name,order in (("empty_last",("A","B","E")),
                   ("charged_last",("A","E","B")),
                   ("one",("A",)),("two",("A","B"))):
    full=atlas(order)
    report={"complete":accept(full)}
    assert report["complete"]["accepted"]
    if len(order)==3:
        omitted=copy.deepcopy(full)
        omitted["cavities"].pop()
        for state in ("isolated","grounded"):
            omitted["native_m40a_v2_witness_records"][state].pop(-2)
        report["omission"]=accept(omitted)
        assert report["omission"]["accepted"] != candidate
        for label,edit in (
            ("duplicate",lambda d:d["cavities"].__setitem__(1,copy.deepcopy(d["cavities"][0]))),
            ("order",lambda d:d["cavities"].reverse()),
            ("bool_flag",lambda d:d.__setitem__("geometry_qualified_spherical_only",1)),
            ("bool_charge",lambda d:d["cavities"][0].__setitem__("source_total_charge_c",True))):
            changed=copy.deepcopy(full);edit(changed)
            report[label]=accept(changed);assert not report[label]["accepted"]
    cavity_evidence[name]=report

# Independently selected path-set probes; live candidate has 7 additive globs.
tests={
 "m37b-source-current.yml":("src/conductor_sim/_directions.py","tools/check_m37b_nojs_hostility.py"),
 "m38a-prescribed-line.yml":("src/conductor_sim/model.py","tools/m37a_ground_wire_reference.py"),
 "m38b-line-viewer.yml":("src/conductor_sim/grounded_plane.py","tools/m38a_line_reference.py"),
 "m39a-gauss-cavities.yml":("src/conductor_sim/cavity_gauss.py","pyproject.toml"),
 "m39b-topology-viewer.yml":("src/conductor_sim/cavity_gauss.py","tools/m39a_gauss_reference.py"),
 "m40a-spherical-multicavity.yml":("src/conductor_sim/spherical_multicavity.py","tools/m39a_gauss_reference.py"),
 "m40b-spherical-atlas.yml":("src/conductor_sim/spherical_multicavity.py","tools/m40a_spherical_reference.py"),
}
ci={}
for name,paths in tests.items():
    yml=(root/".github/workflows"/name).read_text()
    block=yml.split("  pull_request:",1)[1].split("  push:",1)[0]
    patterns=re.findall(r"^\s+- ['\"]([^'\"]+)['\"]\s*$",block,re.M)
    ci[name]={p:any(fnmatch.fnmatchcase(p,glob) for glob in patterns) for p in paths}
assert all(x for cases in ci.values() for x in cases.values()) if candidate else True

print(json.dumps({"baseline":not candidate,"expected":expected,"actual":actual,
     "motion":tiny_motion,"slice":slice_evidence,"atlas":cavity_evidence,
     "ci":ci},indent=2))
