"""Fresh reviewer-owned PR100 #03: raw-direction Kelvin physics and v2 hostility.

Scientific expectations are computed from the field of the REAL point source
and its Kelvin IMAGE, using 110-digit arithmetic on original binary64 inputs.
No candidate density function, candidate verifier, or copied expected-output
array is used to calculate mathematical expectations.
"""
from __future__ import annotations

import json
import math
import sys
from copy import deepcopy
from decimal import Decimal, localcontext
from pathlib import Path

HEAD = "b2303a5bd424b2dff6f088c15691aa2ce2c5f3e2"
TREE = "ab41e066ca6d53809b27b142ae35105eaebbf032"
REL_BOUND = 5e-11  # Independent acceptance; stricter than advertised 2e-10.
LOG = {"source_head": HEAD, "source_tree": TREE,
       "oracle": "110-digit REAL-plus-KELVIN-IMAGE normal E; raw binary64 rays",
       "numerical_cases": [], "record_checks": [], "refusals": [], "failures": []}


def emit(kind, **data):
    LOG[kind].append(data)
    print(kind.upper(), json.dumps(data, sort_keys=True, allow_nan=False), flush=True)


def assert_science(condition, explanation):
    if not condition:
        LOG["failures"].append(explanation)
        print("SCIENCE_FAILURE", explanation, flush=True)


def relerr(x, y):
    return abs(x-y)/abs(y) if y != 0 else abs(x-y)


def raw_to_display(v):
    with localcontext() as ctx:
        ctx.prec = 110
        D = Decimal.from_float
        w = [D(x) for x in v]
        length = sum((t*t for t in w), Decimal(0)).sqrt()
        return tuple(float(t / length) for t in w)


def n64(v):
    return tuple(t / math.hypot(*v) for t in v)


def kelvin_image_field_sigma(radius, sources, original_raw_ray, center=(0., 0., 0.)):
    """Sigma = -epsilon0 E_cavity.normal from physical source and image.

    All source and center coordinates are *separately* converted from their
    original binary64 values before subtraction, preserving near-wall gaps.
    The image is located at a^2*u/|u|^2 and has charge -q*a/|u|.
    """
    with localcontext() as ctx:
        ctx.prec = 110
        D = Decimal.from_float
        A = D(radius)
        v = tuple(D(x) for x in original_raw_ray)
        norm2 = sum((x*x for x in v), Decimal(0))
        if norm2 == 0:
            raise ValueError("zero ray")
        n = tuple(x / norm2.sqrt() for x in v)
        wall = tuple(A*n[i] for i in range(3))
        field = Decimal(0)
        for q, absolute in sources:
            if q == 0.:
                continue
            Q = D(q)
            u = tuple(D(absolute[i])-D(center[i]) for i in range(3))
            d2 = sum((x*x for x in u), Decimal(0))
            if d2 == 0:
                field += -Q / (Decimal(4)*D(math.pi)*A*A)
                continue
            distance = d2.sqrt()
            image = tuple(A*A*u[i]/d2 for i in range(3))
            image_q = -Q*A/distance
            def normal_flux(charge, origin):
                delta = tuple(wall[i]-origin[i] for i in range(3))
                r2 = sum((x*x for x in delta), Decimal(0))
                radial_component = sum((n[i]*delta[i] for i in range(3)), Decimal(0))
                return charge*radial_component/(r2*r2.sqrt())
            field += -(normal_flux(Q, u) + normal_flux(image_q, image))/(Decimal(4)*D(math.pi))
        return float(field)


def make_model(q, radius, absolute, constraint, center=(0.,0.,0.),
               outer_radius=3., outer_center=(0.,0.,0.)):
    from conductor_sim.cavity_gauss import CavityCharge, SealedCavity, GaussCavityAssembly
    from conductor_sim.spherical_multicavity import (
        NamedSourcePosition, SphericalVoid, SphericalMetalGeometry,
        SphericalSigmaModel, solve_spherical_sigma)
    topology = GaussCavityAssembly("TeacherMetal", (
        SealedCavity("V", (CavityCharge("charge", q),)),
    ), constraint)
    geometry = SphericalMetalGeometry(outer_center, outer_radius, (
        SphericalVoid("V", center, radius, (NamedSourcePosition("charge", absolute),)),
    ))
    return solve_spherical_sigma(SphericalSigmaModel(topology, geometry))


def check_numbers(tag, native, expected, meta=None, bound=REL_BOUND):
    error = relerr(native, expected)
    emit("numerical_cases", label=tag, native_sigma_c_per_m2=native,
         independent_sigma_c_per_m2=expected, relative_error=error,
         acceptance_relative_bound=bound, **(meta or {}))
    assert_science(math.isfinite(native) and math.isfinite(expected) and
                   (native == 0 or ((native>0) == (expected>0))) and error <= bound,
                   f"{tag}: native does not reproduce raw-ray independent image field (error {error:.5g})")


def expect_refusal(tag, callback, allowed=(ValueError, TypeError)):
    try:
        callback()
    except allowed as e:
        emit("refusals", label=tag, refused=True, exception=type(e).__name__, message=str(e)[:130])
    except Exception as e:
        emit("refusals", label=tag, refused=False, unexpected=repr(e))
        assert_science(False, f"{tag}: unexpected exception {type(e).__name__}")
    else:
        emit("refusals", label=tag, refused=False)
        assert_science(False, f"{tag}: unqualified or forged input was accepted")


def check_native_record(tag, record):
    from tools.m40a_spherical_reference import check_record
    witness = check_record(record)
    assert_science(witness.get("sampled_local_surface_densities_checked") == len(record["samples"]),
                   f"{tag}: witness sample count mismatch")
    assert_science(record["schema"].endswith(".v2"), f"{tag}: not v2 evidence")
    emit("record_checks", label=tag, accepted=True, witness=witness)


def radial_and_original_oblique():
    from conductor_sim.model import Grounded, FixedNetCharge
    a = 0.85
    q = 3.1e-9
    d = a*(1.-1.2e-8)
    pole = make_model(q, a, (d,0.,0.), Grounded())
    raw_pole = (1.+9e-13,0.,0.)
    exact = pole.inner_surface_charge_density("V", (1.,0.,0.))
    near = pole.inner_surface_charge_density("V", raw_pole)
    analytic = -q*(a+d)/(4*math.pi*a*(a-d)**2)
    independent = kelvin_image_field_sigma(a, [(q,(d,0.,0.))], raw_pole)
    check_numbers("B1 radial analytic pole", near, analytic, bound=1e-12)
    check_numbers("B1 radial independent Kelvin", near, independent)
    assert_science(exact == near, "B1 radial same-direction near-unit differs from exact")
    radial_doc = pole.as_dict((("V",raw_pole),("outer",raw_pole)))
    assert_science(radial_doc["samples"][0]["input_direction"] == list(raw_pole),
                   "radial raw input not preserved")
    assert_science(radial_doc["samples"][0]["unit_normal"] == [1.,0.,0.],
                   "radial display normal unexpected")
    assert_science(radial_doc["samples"][1]["sigma_c_per_m2"] == 0.,
                   "grounded exterior must have zero sigma")
    check_native_record("B1 pole genuine v2",radial_doc)

    expected_02 = [(-3532142.26790142, -3532142.2752839886),
                   (+2734561.7557946476, +2734561.761510185),
                   (-4242770.360599676, -4242770.356589729),
                   (+3284725.440464265, +3284725.43735979)]
    i=0
    all_records=[]
    for b in ((.6,.8,0.), (.48,-.64,.6)):
        position = tuple(v*a*(1.-1.2e-8) for v in b)
        off = tuple(b[k]+(5e-9,-2.5e-9,1e-9)[k] for k in range(3))
        w = n64(off)
        raw = tuple(v*(1.+9e-13) for v in w)
        assert_science(abs(math.hypot(*raw)-1) <= 1e-12,
                       "provided oblique direction rejected before running test")
        for mode,q,constraint in (("grounded",+3.1e-9,Grounded()),
                                  ("isolated",-2.4e-9,FixedNetCharge(+1.1e-9))):
            sol = make_model(q,a,position,constraint)
            reference = kelvin_image_field_sigma(a, [(q,position)], raw)
            actual = sol.inner_surface_charge_density("V",raw)
            prior_reference, stale_sigma = expected_02[i]
            tag = f"review02-{i+1}-{mode}"
            check_numbers(tag,actual,reference,meta={"raw_direction":list(raw),
                "source_m":list(position),"mode":mode,"q_c":q,
                "previous_review_expected":prior_reference,
                "previous_bug_sigma":stale_sigma})
            assert_science(relerr(reference,prior_reference)<1e-11,
                           f"{tag}: separately derived reference differs from previous reviewer expectation")
            assert_science(relerr(stale_sigma,reference)>2e-10,
                           f"{tag}: stale sigma would not be distinguishable at 2e-10")
            doc = sol.as_dict((("V",raw),("outer",raw)))
            assert_science(doc["samples"][0]["input_direction"]==list(raw),
                           f"{tag}: export altered raw ray")
            assert_science(doc["samples"][0]["unit_normal"]==list(raw_to_display(raw)),
                           f"{tag}: display-only vector not reproducible")
            assert_science(doc["samples"][0]["sigma_c_per_m2"]==actual,
                           f"{tag}: export not genuine native density")
            expected_outer=(q+1.1e-9)/(4*math.pi*3.**2) if mode=="isolated" else 0.
            assert_science(relerr(doc["samples"][1]["sigma_c_per_m2"],expected_outer)<1e-13,
                           f"{tag}: outer Gauss/grounding error")
            check_native_record(tag+" native v2",doc)
            all_records.append((tag,doc,raw,stale_sigma))
            i+=1
    return pole,radial_doc,all_records


def attack_v2(tag, genuine, raw, stale):
    from tools.m40a_spherical_reference import check_record
    samples=genuine["samples"]
    def mutated(name, callback):
        fake=deepcopy(genuine)
        callback(fake)
        expect_refusal(f"{tag}: {name}",lambda:check_record(fake))
    mutated("stale prematurely-rounded sigma",
            lambda r:r["samples"][0].__setitem__("sigma_c_per_m2",stale))
    mutated("signed density reversed",
            lambda r:r["samples"][0].__setitem__("sigma_c_per_m2",-samples[0]["sigma_c_per_m2"]))
    mutated("false physical zero",
            lambda r:r["samples"][0].__setitem__("sigma_c_per_m2",0.))
    mutated("forged display unit normal",
            lambda r:r["samples"][0].__setitem__("unit_normal",[1.,0.,0.]))
    def shift_input(r):
        pert=n64((raw[0]+7e-9,raw[1]-4e-9,raw[2]+2e-9))
        pert=tuple(x*(1.+9e-13) for x in pert)
        r["samples"][0]["input_direction"]=list(pert)
        r["samples"][0]["unit_normal"]=list(raw_to_display(pert))
    mutated("altered raw input with matching display but old sigma",shift_input)
    def swap_components(r):
        changed=(raw[1],raw[0],raw[2])
        r["samples"][0]["input_direction"]=list(changed)
        r["samples"][0]["unit_normal"]=list(raw_to_display(changed))
    mutated("swapped raw coordinates",swap_components)
    mutated("boolean raw coordinate",
            lambda r:r["samples"][0].__setitem__("input_direction",[True,raw[1],raw[2]]))
    mutated("source ID mismatch",lambda r:r["voids"][0]["source_positions"][0].__setitem__("source_id","faked"))
    mutated("surface ID mismatch",lambda r:r["samples"][0].__setitem__("surface_id","not-a-void"))
    mutated("wrong surface units",lambda r:r["units"].__setitem__("surface_density","V/m"))
    mutated("wrong source role",lambda r:r.__setitem__("source_role","authentic_workbook_solutions"))
    mutated("fake original JEE solved item",lambda r:r.__setitem__("original_workbook_items_newly_solved",1))
    mutated("fake 3D electric field evidence",lambda r:r["samples"][0].__setitem__("E_v_per_m",[0,0,0]))
    mutated("fake source force",lambda r:r.__setitem__("force_newtons",[0,0,0]))
    mutated("fake potential",lambda r:r.__setitem__("potential_volts",1.))
    mutated("fake current",lambda r:r.__setitem__("ground_current_a",1.))
    mutated("fake time evolution",lambda r:r.__setitem__("time_evolution_defined",True))
    mutated("pretend schema v1",lambda r:r.__setitem__("schema",r["schema"].replace(".v2",".v1")))


def novel_near_wall_and_controls():
    from conductor_sim.cavity_gauss import CavityCharge, SealedCavity, GaussCavityAssembly
    from conductor_sim.model import Grounded
    from conductor_sim.spherical_multicavity import (
        NamedSourcePosition, SphericalVoid, SphericalMetalGeometry,
        SphericalSigmaModel, solve_spherical_sigma)
    a=.85
    center=(.231,-.417,.119)
    direction=n64((.227,-.517,.826))  # novel 3D direction, not either review02 basis
    local=tuple(x*a*(1.-1.6e-8) for x in direction)
    physical=tuple(center[k]+local[k] for k in range(3))
    biased=n64(tuple(direction[k]+(-3.8e-9,4.2e-9,2.7e-9)[k] for k in range(3)))
    raw=tuple(x*(1.+7e-13) for x in biased)
    sol=make_model(-1.9e-9,a,physical,Grounded(),center=center,outer_radius=5.)
    actual=sol.inner_surface_charge_density("V",raw)
    independent=kelvin_image_field_sigma(a,[(-1.9e-9,physical)],raw,center=center)
    check_numbers("NOVEL translated 3D near-wall source",actual,independent,
                  meta={"center_m":list(center),"source_m":list(physical),
                        "raw_direction":list(raw),"charge_c":-1.9e-9})
    check_native_record("NOVEL genuine translated v2",sol.as_dict((("V",raw),)))

    for name, source, n in (
        ("exact center",(0.,0.,0.),(.21,-.38,.9)),
        ("very-near center",(1e-250,0.,0.),(.48,-.64,.6)),
        ("non-near-wall",(.17,.08,-.03),(.48,-.64,.6)),
    ):
        q=2e-9
        n=n64(n)
        sol=make_model(q,a,source,Grounded())
        expected=kelvin_image_field_sigma(a,[(q,source)],n)
        check_numbers(name,sol.inner_surface_charge_density("V",n),expected,
                      meta={"source_m":list(source)})
        check_native_record(name+" actual record",sol.as_dict((("V",n),)))

    # Signed neutral at the global level does not imply local density=0.
    q1,q2=3.1e-9,-3.1e-9
    pos1=(.23,.05,-.06); pos2=(-.13,.18,.21)
    gauss=GaussCavityAssembly("NeutralMetal",(
        SealedCavity("V",(CavityCharge("positive",q1),CavityCharge("negative",q2))),
    ),Grounded())
    geometry=SphericalMetalGeometry((0.,0.,0.),3.,(
        SphericalVoid("V",(0.,0.,0.),a,(
            NamedSourcePosition("positive",pos1),NamedSourcePosition("negative",pos2))),
    ))
    sol=solve_spherical_sigma(SphericalSigmaModel(gauss,geometry))
    n=n64((.3,.4,.82))
    actual=sol.inner_surface_charge_density("V",n)
    expected=kelvin_image_field_sigma(a,[(q1,pos1),(q2,pos2)],n)
    check_numbers("signed-neutral but nonuniform inner face",actual,expected)
    assert_science(actual != 0.,"signed-neutral interior falsely forced to zero local density")
    check_native_record("signed-neutral valid evidence",sol.as_dict((("V",n),)))


def refusals(pole):
    from conductor_sim.model import Grounded
    from conductor_sim.solver import UnsupportedProblem
    bad_rays=[("arbitrary nonunit >1e-12",(1.+2e-12,0.,0.)),
        ("zero ray",(0.,0.,0.)),("bool ray",(True,0.,0.)),
        ("nonfinite NaN",(float("nan"),0.,0.)),
        ("nonfinite infinite",(float("inf"),0.,0.))]
    for name,ray in bad_rays:
        expect_refusal(name,lambda ray=ray:pole.inner_surface_charge_density("V",ray))
    for frac in (1.,1.-5e-9,1.-1e-8):
        expect_refusal(f"source gap at/under required 1e-8: factor {frac}",
                       lambda frac=frac:make_model(3.1e-9,.85,(.85*frac,0.,0.),Grounded()),
                       (UnsupportedProblem,ValueError))
    expect_refusal("subqualified nonzero q cannot be treated zero",
                   lambda:make_model(1e-241,.85,(0.,0.,0.),Grounded()),
                   (UnsupportedProblem,ValueError))
    expect_refusal("unqualified huge q",lambda:make_model(1e181,.85,(0.,0.,0.),Grounded()),
                   (UnsupportedProblem,ValueError))
    # Near-exact signed cancellation must be refused; not called exact zero.
    from conductor_sim.cavity_gauss import CavityCharge, SealedCavity, GaussCavityAssembly
    from conductor_sim.spherical_multicavity import (
        NamedSourcePosition, SphericalVoid, SphericalMetalGeometry,
        SphericalSigmaModel, solve_spherical_sigma)
    topology=GaussCavityAssembly("M",(
        SealedCavity("V",(CavityCharge("plus",3.1e-9),
                         CavityCharge("minus",-3.1e-9*(1-1e-13)))),
    ),Grounded())
    geo=SphericalMetalGeometry((0.,0.,0.),3.,(
        SphericalVoid("V",(0.,0.,0.),.85,(
            NamedSourcePosition("plus",(.2,0.,0.)),
            NamedSourcePosition("minus",(.2,0.,0.)))),
    ))
    mixed=solve_spherical_sigma(SphericalSigmaModel(topology,geo))
    expect_refusal("high-cancellation cannot claim theorem zero",
                   lambda:mixed.inner_surface_charge_density("V",(1.,0.,0.)),
                   (UnsupportedProblem,))
    for name,call in (
        ("fake local E",lambda:pole.electric_field_at((0.,0.,0.))),
        ("fake local V",lambda:pole.potential_at((0.,0.,0.))),
        ("fake source force",lambda:pole.force_on_source("charge")),
        ("fake wire current",lambda:pole.ground_wire_current()),
    ):
        expect_refusal(name,call,(UnsupportedProblem,))


def main():
    path = Path(sys.argv[1]) if len(sys.argv)>1 else Path("review100-03-numerical.json")
    try:
        pole,radial_doc,records=radial_and_original_oblique()
        for tag,genuine,raw,stale in records:
            attack_v2(tag,genuine,raw,stale)
        novel_near_wall_and_controls()
        refusals(pole)
    except BaseException as exc:
        LOG["failures"].append("uncaught error: "+repr(exc))
        print("UNCAUGHT",repr(exc),flush=True)
        raise
    finally:
        path.write_text(json.dumps(LOG,indent=2,sort_keys=True,allow_nan=False)+"\n",encoding="utf-8")
        print("SUMMARY",len(LOG["numerical_cases"]),"numerical",
              len(LOG["record_checks"]),"accepted records",
              len(LOG["refusals"]),"refusals",
              len(LOG["failures"]),"failures",flush=True)
    if LOG["failures"]:
        raise SystemExit("CHANGES REQUESTED: "+"; ".join(LOG["failures"]))
    print("INDEPENDENT SCIENTIFIC REVIEW #03: PASS",flush=True)


if __name__ == "__main__":
    main()
