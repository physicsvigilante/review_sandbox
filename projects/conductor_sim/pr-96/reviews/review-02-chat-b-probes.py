"""Independent correction-review #02 probes for pinned conductor_sim PR96 M39a.

Only the expected mathematical answers are derived here from Python's Fraction
and a reviewer-authored source inventory. Production is imported only as the
system under test. The externally provided standalone CLI is executed for both
authentic and forged JSON records. All first-attempt results are preserved.
"""
import copy
from dataclasses import replace
from fractions import Fraction
import json
import math
from pathlib import Path
import subprocess
import sys
import traceback

from conductor_sim.cavity_gauss import (
    CavityCharge, SealedCavity, GaussCavityAssembly, CavityFaceTotal,
    solve_cavity_gauss, validate_cavity_gauss_ledger,
)
from conductor_sim.model import FixedNetCharge, Grounded
from conductor_sim.solver import UnsupportedProblem
from tools.m39a_gauss_reference import check_gauss_record

EXPECTED_HEAD = "8d235eab5bf14bebf191e15771d296878a151a23"
EXPECTED_TREE = "820ab1e35aee40a30eb45e9b32157416dfd59642"
RESULTS = []
FAILED = []
OUT = None

def run_check(name, test):
    try:
        message = test()
        RESULTS.append({"probe": name, "status": "PASS", "detail": str(message or "")})
        print("PASS", name, message or "", flush=True)
    except Exception as exc:
        FAILED.append(name)
        RESULTS.append({"probe": name, "status": "FAIL",
                        "detail": f"{type(exc).__name__}: {exc}"})
        print("FAIL", name, type(exc).__name__, str(exc), flush=True)
        traceback.print_exc()

def refuses(fn, exc_type=Exception, keyword=None):
    try:
        fn()
    except exc_type as exc:
        if keyword and keyword not in str(exc).lower():
            raise AssertionError(f"wrong refusal reason {exc!r}; expected {keyword}")
        return f"{type(exc).__name__}: {exc}"
    raise AssertionError("incorrectly accepted invalid case")

def fraction_total(values):
    return sum((Fraction.from_float(float(v)) for v in values), Fraction(0))

def equal_float(got, expected):
    desired = float(expected)
    if not math.isfinite(desired):
        raise AssertionError("bad review expectation")
    assert got == desired, (got, desired, expected)

def save(name, doc):
    path = OUT / (name + ".json")
    path.write_text(json.dumps(doc, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    return path

def actual_cli(name, doc, should_pass):
    path = save(name, doc)
    p = subprocess.run(
        [sys.executable, "-m", "tools.m39a_gauss_reference",
         "--input", str(path)],
        text=True, capture_output=True,
    )
    (OUT / (name + "-cli.txt")).write_text(
        f"exit={p.returncode}\nstdout:\n{p.stdout}\nstderr:\n{p.stderr}",
        encoding="utf-8",
    )
    if should_pass:
        assert p.returncode == 0, (name, p.stdout, p.stderr)
    else:
        assert p.returncode != 0, (name, p.stdout)
    return p.stderr.strip().splitlines()[-1] if p.stderr.strip() else f"exit {p.returncode}"

def large_order(order):
    values = [("large", 1e150), ("residual", 1e-9), ("negative", -1e150)]
    ordered = tuple(CavityCharge(*values[i]) for i in order)
    m = GaussCavityAssembly("Metal", (SealedCavity("Stress", ordered),), Grounded())
    result = solve_cavity_gauss(m)
    expected = fraction_total(v for _, v in values)
    equal_float(result.faces[0].enclosed_source_charge_c, expected)
    equal_float(result.faces[0].induced_inner_face_charge_c, -expected)
    equal_float(result.total_source_charge_c, expected)
    assert result.outer_face_charge_c == 0 and result.exterior_electric_flux_v_m == 0
    doc = result.as_dict()
    assert [s["source_id"] for s in doc["cavities"][0]["authored_sources"]] == [
        values[i][0] for i in order]
    assert check_gauss_record(doc)["point_source_identities_checked"] == 3
    actual_cli("f01-order-" + "".join(str(i) for i in order), doc, True)
    return f"exact source sum {float(expected):.17g} C; inner {-float(expected):.17g} C"

def cross_cavity(order, net):
    qs = {"P": 1e150, "R": 1e-9, "N": -1e150}
    cavities = tuple(SealedCavity(k, (CavityCharge("src_"+k, qs[k]),)) for k in order)
    result = solve_cavity_gauss(GaussCavityAssembly("Metal", cavities, FixedNetCharge(net), 1.0))
    expected = fraction_total(qs.values())
    equal_float(result.total_source_charge_c, expected)
    equal_float(result.outer_face_charge_c, expected + Fraction.from_float(net))
    equal_float(result.exterior_electric_flux_v_m, expected + Fraction.from_float(net))
    doc = result.as_dict()
    assert [c["cavity_id"] for c in doc["cavities"]] == list(order)
    assert [c["authored_sources"][0]["source_id"] for c in doc["cavities"]] == [
        "src_"+k for k in order]
    check_gauss_record(doc)
    actual_cli("f01-cross-"+"".join(order)+"-"+str(net).replace(".","_"),doc,True)
    return f"qtotal={result.total_source_charge_c:.17g}; outer={result.outer_face_charge_c:.17g}"

def true_cancel():
    charges = (CavityCharge("pos", 1e150), CavityCharge("neg", -1e150))
    for mode in (FixedNetCharge(0.0), Grounded()):
        result=solve_cavity_gauss(GaussCavityAssembly("Metal", (SealedCavity("Void", charges),),mode,1.0))
        assert result.total_source_charge_c == 0.0
        assert result.outer_face_charge_c == 0.0
        assert result.exterior_electric_flux_v_m == 0.0
        check_gauss_record(result.as_dict())
    return "true exact 0 C remains zero in both electrical constraints"

def tiny_flux_underflow(sign):
    q=sign*1e-300
    model=GaussCavityAssembly("TinyMetal", (SealedCavity("Void"),),FixedNetCharge(q),1e100)
    exact=Fraction.from_float(q)/Fraction.from_float(1e100)
    assert exact != 0 and float(exact)==0, "review's rational flux must be unrepresentable"
    return refuses(lambda:solve_cavity_gauss(model), UnsupportedProblem, "underflow")

def forged_underflow():
    model=GaussCavityAssembly("TinyMetal", (SealedCavity("Void"),),FixedNetCharge(1e-300),1.0)
    doc=solve_cavity_gauss(model).as_dict()
    doc["permittivity_f_per_m"]=1e100
    doc["exterior_electric_flux_v_m"]=0.0
    detail=refuses(lambda:check_gauss_record(doc), ValueError, "underflow")
    actual_cli("f02-forged-underflow",doc,False)
    return detail

def grounded_no_flux():
    cavities=(SealedCavity("C", (CavityCharge("p", 1e150),CavityCharge("n", -1e150),CavityCharge("r",1e-9))),)
    doc=solve_cavity_gauss(GaussCavityAssembly("Metal",cavities,Grounded(),1e100)).as_dict()
    assert doc["total_interior_source_charge_c"]==1e-9
    assert doc["conductor"]["equilibrium_net_metal_charge_c"]==-1e-9
    assert doc["exterior_electric_flux_v_m"]==0
    assert doc["exterior_electric_field_zero_theorem"] is True
    check_gauss_record(doc)
    actual_cli("f02-grounded-authentic-zero",doc,True)
    return "grounded external flux exactly 0 despite nonzero signed sources"

def representable_flux():
    doc=solve_cavity_gauss(GaussCavityAssembly("M", (SealedCavity("Void"),),
         FixedNetCharge(1e-300),1e-100)).as_dict()
    expected=Fraction.from_float(1e-300)/Fraction.from_float(1e-100)
    equal_float(doc["exterior_electric_flux_v_m"],expected)
    assert doc["exterior_electric_flux_v_m"]>0
    check_gauss_record(doc)
    actual_cli("f02-representable-flux",doc,True)
    return f"{doc['exterior_electric_flux_v_m']:.17g} V*m"

def high_flux_overflow():
    m=GaussCavityAssembly("Metal", (SealedCavity("Void"),),
                         FixedNetCharge(1e300),1e-300)
    return refuses(lambda:solve_cavity_gauss(m),UnsupportedProblem,"overflow")

def subnormal_sign(sign):
    smallest=float.fromhex("0x0.0000000000001p-1022")
    m=GaussCavityAssembly("Tiny", (SealedCavity("Empty"),),
                         FixedNetCharge(sign*smallest),1.0)
    doc=solve_cavity_gauss(m).as_dict()
    equal_float(doc["outer_face_total_charge_c"], Fraction.from_float(sign*smallest))
    equal_float(doc["exterior_electric_flux_v_m"], Fraction.from_float(sign*smallest))
    check_gauss_record(doc)
    actual_cli(f"f03-authentic-sign-{sign}",doc,True)
    for field in ("outer_face_total_charge_c","exterior_electric_flux_v_m"):
        forged=copy.deepcopy(doc)
        forged[field]=0.0
        detail=refuses(lambda:check_gauss_record(forged),ValueError,"forged zero")
        actual_cli(f"f03-forged-zero-{field}-sign-{sign}",forged,False)
    for field in ("outer_face_total_charge_c","exterior_electric_flux_v_m"):
        reversed_sign=copy.deepcopy(doc)
        reversed_sign[field]=-(reversed_sign[field])
        refuses(lambda:check_gauss_record(reversed_sign),ValueError,"reversed")
        actual_cli(f"f03-reversed-{field}-sign-{sign}",reversed_sign,False)
    return f"authentic {sign*smallest} C and V*m; both forged zeros and signs refused"

def normal_ulp():
    model=GaussCavityAssembly("Normal", (SealedCavity("C", (
        CavityCharge("p",0.1), CavityCharge("n",-0.01))),),
        FixedNetCharge(0.13),1.0)
    doc=solve_cavity_gauss(model).as_dict()
    check_gauss_record(doc)
    adjacent=copy.deepcopy(doc)
    adjacent["outer_face_total_charge_c"]=math.nextafter(doc["outer_face_total_charge_c"],math.inf)
    check_gauss_record(adjacent)
    actual_cli("f03-normal-one-ulp",adjacent,True)
    return f"1 ULP variation admitted around {doc['outer_face_total_charge_c']} C"

SIX=(
    ("North", (("n_pos",7e-9),("n_neg",-2e-9))),
    ("West", (("w_neg",-4e-9),("w_pos",1e-9))),
    ("Neutral", (("neutral_pos",6e-9),("neutral_neg",-6e-9))),
    ("Empty", ()),
    ("South", (("s_neg",-8e-9),("s_pos",1.5e-9))),
    ("East", (("e_pos",2e-9),("e_small",0.5e-9))),
)

def six_cavity(mode):
    cavities=tuple(SealedCavity(cid,tuple(CavityCharge(s,q) for s,q in sources))
                   for cid,sources in SIX)
    eps=8.8541878128e-12
    model=GaussCavityAssembly("Metal",cavities,
         Grounded() if mode=="grounded" else FixedNetCharge(1.25e-9),eps)
    ledger=solve_cavity_gauss(model)
    doc=ledger.as_dict()
    qtot=sum((fraction_total(q for _,q in src) for _,src in SIX),Fraction())
    assert len(doc["cavities"])==6
    for (cid,sources),record in zip(SIX,doc["cavities"]):
        assert cid==record["cavity_id"]
        assert tuple((s["source_id"],s["charge_c"]) for s in record["authored_sources"])==sources
        charge=fraction_total(q for _,q in sources)
        equal_float(record["source_charge_sum_c"],charge)
        equal_float(record["induced_inner_face_total_charge_c"],-charge)
    equal_float(doc["total_interior_source_charge_c"],qtot)
    net=-qtot if mode=="grounded" else Fraction.from_float(1.25e-9)
    qouter=Fraction() if mode=="grounded" else net+qtot
    equal_float(doc["conductor"]["equilibrium_net_metal_charge_c"],net)
    equal_float(doc["outer_face_total_charge_c"],qouter)
    equal_float(doc["exterior_electric_flux_v_m"],qouter/Fraction.from_float(eps))
    assert check_gauss_record(doc)["point_source_identities_checked"]==10
    actual_cli("six-"+mode,doc,True)
    return f"qtot={float(qtot):.17g} C; outer={float(qouter):.17g} C"

def malformed_bool_and_id():
    m=GaussCavityAssembly("Metal",(SealedCavity("Void",(CavityCharge("charge",1.0),)),),
                          FixedNetCharge(0.0),1.0)
    doc=solve_cavity_gauss(m).as_dict()
    for path in (("total_interior_source_charge_c",),("outer_face_total_charge_c",),
                 ("exterior_electric_flux_v_m",),("permittivity_f_per_m",)):
        x=copy.deepcopy(doc)
        x[path[0]]=True
        refuses(lambda:check_gauss_record(x),ValueError)
    bad=copy.deepcopy(doc)
    bad["cavities"][0]["authored_sources"][0]["source_id"]="Void"
    refuses(lambda:check_gauss_record(bad),ValueError,"identity")
    invalid=copy.deepcopy(doc)
    invalid["cavities"][0]["authored_sources"].append(
        copy.deepcopy(invalid["cavities"][0]["authored_sources"][0]))
    refuses(lambda:check_gauss_record(invalid),ValueError,"identity")
    refuses(lambda:GaussCavityAssembly("Metal",(SealedCavity("Void",(
        CavityCharge("a",1),CavityCharge("a",-1))),),Grounded()),ValueError)
    return "Boolean SI values and duplicate/multiply-assigned source identities refused"

def native_identity_tamper():
    ledger=solve_cavity_gauss(GaussCavityAssembly("Metal",(
        SealedCavity("A",(CavityCharge("a",1),)),
        SealedCavity("B",(CavityCharge("b",2),))),Grounded(),1.0))
    swapped=replace(ledger,faces=(replace(ledger.faces[0],cavity_id="B"),ledger.faces[1]))
    return refuses(lambda:validate_cavity_gauss_ledger(swapped),ValueError,"identit")

def manifest_anchor():
    m=GaussCavityAssembly("Metal",(
        SealedCavity("A",(CavityCharge("id1",1.0),)),
        SealedCavity("B",(CavityCharge("id2",-1.0),))),Grounded(),1.0)
    doc=solve_cavity_gauss(m).as_dict()
    anchor=tuple(tuple(s["source_id"] for s in cav["authored_sources"]) for cav in doc["cavities"])
    rewritten=copy.deepcopy(doc)
    rewritten["cavities"][0]["authored_sources"][0]["source_id"]="id2"
    rewritten["cavities"][1]["authored_sources"][0]["source_id"]="id1"
    check_gauss_record(rewritten)  # Without external ID manifest this is consistent.
    changed=tuple(tuple(s["source_id"] for s in cav["authored_sources"]) for cav in rewritten["cavities"])
    assert changed!=anchor, "independent trusted anchor did not detect identity substitution"
    return "unanchored identity rewrite accepted consistently, external ID anchor rejects"

def refused_local_requests():
    ledger=solve_cavity_gauss(GaussCavityAssembly("Metal",(SealedCavity("C"),),Grounded()))
    for method in ("electric_field_at","potential_at","surface_charge_density_at",
                   "force_on_source","ground_wire_current"):
        refuses(lambda:getattr(ledger,method)(0),UnsupportedProblem)
    for flag in ("geometry_verified","source_position_defined","time_evolution_defined"):
        assert ledger.as_dict()[flag] is False
    return "E(x), V(x), sigma(x), force and current fail closed; geometry/time provenance false"

def main():
    global OUT
    OUT=Path(sys.argv[1]).resolve()
    OUT.mkdir(parents=True,exist_ok=True)
    checks=[
      ("F01_ORDER_012",lambda:large_order((0,1,2))),
      ("F01_ORDER_021",lambda:large_order((0,2,1))),
      ("F01_ORDER_210",lambda:large_order((2,1,0))),
      ("F01_CROSS_CAVITIES_PRN",lambda:cross_cavity(("P","R","N"),0.0)),
      ("F01_CROSS_CAVITIES_NPR_ISOLATED",lambda:cross_cavity(("N","P","R"),0.25)),
      ("F01_TRUE_CANCELLATION_ZERO",true_cancel),
      ("F02_NATIVE_POSITIVE_UNDERFLOW",lambda:tiny_flux_underflow(1)),
      ("F02_NATIVE_NEGATIVE_UNDERFLOW",lambda:tiny_flux_underflow(-1)),
      ("F02_FORGED_UNDERFLOW_CLI",forged_underflow),
      ("F02_GROUNDED_ZERO",grounded_no_flux),
      ("F02_REPRESENTABLE_TINY_FLUX",representable_flux),
      ("F02_HIGH_FLUX_OVERFLOW",high_flux_overflow),
      ("F03_SMALLEST_POSITIVE_SUBNORMAL",lambda:subnormal_sign(1)),
      ("F03_SMALLEST_NEGATIVE_SUBNORMAL",lambda:subnormal_sign(-1)),
      ("F03_NORMAL_ONE_ULP",normal_ulp),
      ("SIX_CAVITY_ISOLATED",lambda:six_cavity("isolated")),
      ("SIX_CAVITY_GROUNDED",lambda:six_cavity("grounded")),
      ("BOOLEAN_AND_SOURCE_ID_REFUSAL",malformed_bool_and_id),
      ("NATIVE_SAVED_FACE_ID_REFUSAL",native_identity_tamper),
      ("EXTERNAL_ID_ANCHOR_BOUNDARY",manifest_anchor),
      ("UNSUPPORTED_LOCAL_FIELDS_REFUSAL",refused_local_requests),
    ]
    for name,fn in checks:
        run_check(name,fn)
    payload={"production_head_expected":EXPECTED_HEAD,"production_tree_expected":EXPECTED_TREE,
             "probes":RESULTS,"pass":len(RESULTS)-len(FAILED),
             "fail":len(FAILED),"failed_names":FAILED}
    (OUT/"review-02-probe-results.json").write_text(json.dumps(payload,indent=2)+"\n")
    print(f"REVIEW_02_TOTAL={len(RESULTS)} PASS={len(RESULTS)-len(FAILED)} FAIL={len(FAILED)}",flush=True)
    return int(bool(FAILED))

if __name__=="__main__":
    sys.exit(main())
