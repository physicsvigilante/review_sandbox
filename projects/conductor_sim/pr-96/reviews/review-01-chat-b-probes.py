"""Independent Chat B review probes for conductor_sim M39a PR 96.

Deliberately new six-cavity topology. Decimal reference written by this reviewer;
does NOT call the production reference to calculate expected totals.
Run on literal production SHA; never on floating production branch.
"""
import copy
from dataclasses import replace
from decimal import Decimal, localcontext
import json
import math
from pathlib import Path
import sys
import traceback

from conductor_sim.cavity_gauss import (
    CavityCharge, SealedCavity, GaussCavityAssembly, solve_cavity_gauss,
    validate_cavity_gauss_ledger,
)
from conductor_sim.model import FixedNetCharge, Grounded
from conductor_sim.solver import UnsupportedProblem
from tools.m39a_gauss_reference import check_gauss_record

E = Decimal("8.8541878128e-12")
DATA = (
    ("North", (("n_pos", "7e-9"), ("n_neg", "-2e-9"))),
    ("West", (("w_neg", "-4e-9"), ("w_pos", "1e-9"))),
    ("Neutral", (("neutral_pos", "6e-9"), ("neutral_neg", "-6e-9"))),
    ("Empty", ()),
    ("South", (("s_neg", "-8e-9"), ("s_pos", "1.5e-9"))),
    ("East", (("e_pos", "2e-9"), ("e_small", "0.5e-9"))),
)
RESULTS = []
FAILED = []

def check(label, fn):
    try:
        detail = fn()
        RESULTS.append({"name": label, "status": "PASS", "detail": str(detail or "")})
        print("PASS", label, detail or "", flush=True)
    except Exception as ex:
        detail = f"{type(ex).__name__}: {ex}"
        RESULTS.append({"name": label, "status": "FAIL", "detail": detail})
        FAILED.append(label)
        print("FAIL", label, detail, flush=True)
        traceback.print_exc()

def close(a, b, name, *, abs_tol=1e-25):
    if not math.isclose(float(a), float(b), rel_tol=3e-13, abs_tol=abs_tol):
        raise AssertionError(f"{name}: got {a!r}, expected {b!r}")

def decimal_sum(x):
    # Explicitly wide enough for even an IEEE double 1e308 / 1e-19 cancellation.
    with localcontext() as ctx:
        ctx.prec = 400
        return sum((Decimal(item) for item in x), Decimal(0))

def model_for(data, constraint):
    return GaussCavityAssembly(
        "ReviewerMetal",
        tuple(SealedCavity(cid, tuple(CavityCharge(sid,float(q)) for sid,q in sources))
              for cid,sources in data),
        constraint,
    )

def expected_map(data):
    return {cid: decimal_sum([q for sid,q in sources]) for cid,sources in data}

def verify(record, data, metal, grounded):
    expect = expected_map(data)
    total = decimal_sum([str(v) for v in expect.values()])
    qouter = Decimal(0) if grounded else Decimal(metal) + total
    qmetal = -total if grounded else Decimal(metal)
    assert [c["cavity_id"] for c in record["cavities"]] == [x[0] for x in data]
    for row, (cid,sources) in zip(record["cavities"],data):
        assert [(s["source_id"],Decimal(str(s["charge_c"]))) for s in row["authored_sources"]] == (
            [(sid,Decimal(str(float(q)))) for sid,q in sources])
        close(row["source_charge_sum_c"],expect[cid],cid+" q")
        close(row["induced_inner_face_total_charge_c"],-expect[cid],cid+" inner")
    close(record["total_interior_source_charge_c"],total,"S")
    close(record["outer_face_total_charge_c"],qouter,"outer face")
    close(record["conductor"]["equilibrium_net_metal_charge_c"],qmetal,"metal total")
    close(record["exterior_electric_flux_v_m"],qouter/E,"exterior phi",abs_tol=1e-17)
    assert record["exterior_electric_field_zero_theorem"] is grounded
    assert record["original_workbook_items_newly_solved"] == 0
    assert record["source_role"] == "teacher_hypothetical_topology_gauss_only"
    assert record["geometry_verified"] is False
    assert record["source_position_defined"] is False
    assert record["time_evolution_defined"] is False
    assert "surface charge density" in " ".join(record["unsupported"])
    return f"S={total} C, metal={qmetal} C, outer={qouter} C, phi={qouter/E} V*m"

def must_refuse(fn, reason):
    try:
        fn()
    except (ValueError, TypeError, UnsupportedProblem) as ex:
        assert str(ex), "refusal must explain failure"
        return type(ex).__name__ + " / " + str(ex)
    raise AssertionError("forged or unsupported request accepted: "+reason)

def edit(path, value, base):
    bad=copy.deepcopy(base)
    target=bad
    for k in path[:-1]:
        target=target[k]
    target[path[-1]]=value
    return bad

def main():
    out=Path(sys.argv[1] if len(sys.argv)>1 else "../evidence")
    out.mkdir(parents=True,exist_ok=True)
    parent=model_for(DATA,FixedNetCharge(1.25e-9))
    child=model_for(DATA,Grounded()) # genuinely separate authored static assembly
    initial=solve_cavity_gauss(parent)
    grounded=solve_cavity_gauss(child)
    initial_record=initial.as_dict()
    grounded_record=grounded.as_dict()
    for name,doc in [("review-six-isolated.json",initial_record),("review-six-grounded.json",grounded_record)]:
        (out/name).write_text(json.dumps(doc,indent=2,allow_nan=False)+"\n")
    check("UNFAMILIAR_6C_ISOLATED_GAUSS_INDEPENDENT_ARITHMETIC",
          lambda: verify(initial_record,DATA,"1.25e-9",False))
    check("SEPARATE_6C_GROUNDED_GAUSS_AND_EXTERIOR_UNIQUENESS",
          lambda: verify(grounded_record,DATA,"0",True))
    check("STANDALONE_DECIMAL_CHECKER_ACCEPTS_NEW_ISOLATED",
          lambda: check_gauss_record(initial_record))
    check("STANDALONE_DECIMAL_CHECKER_ACCEPTS_NEW_GROUNDED",
          lambda: check_gauss_record(grounded_record))

    def order_independent():
        permuted=replace(parent,cavities=tuple(reversed(tuple(
            replace(c,sources=tuple(reversed(c.sources))) for c in parent.cavities))))
        got=solve_cavity_gauss(permuted).as_dict()
        rev_data=tuple((cid,tuple(reversed(src))) for cid,src in reversed(DATA))
        verify(got,rev_data,"1.25e-9",False)
        check_gauss_record(got)
        close(got["outer_face_total_charge_c"],initial_record["outer_face_total_charge_c"],"permutation outer")
        return "both cavity/source order permutations preserve exact integrated charge"
    check("REORDER_SOURCES_AND_CAVITIES",order_independent)

    def revised_membership():
        old_first=parent.cavities[0]
        neutral=parent.cavities[2]
        moved=neutral.sources[0]
        new_cav=(
          replace(old_first,sources=old_first.sources+(moved,)),
          parent.cavities[1],
          replace(neutral,sources=(neutral.sources[1],)),
        )+parent.cavities[3:]
        newer=replace(parent,cavities=new_cav)
        got=solve_cavity_gauss(newer).as_dict()
        new_data=list(DATA)
        new_data[0]=(DATA[0][0],DATA[0][1]+(DATA[2][1][0],))
        new_data[2]=(DATA[2][0],(DATA[2][1][1],))
        verify(got,tuple(new_data),"1.25e-9",False)
        check_gauss_record(got)
        assert initial.as_dict()==initial_record, "parent ledger mutated"
        assert solve_cavity_gauss(parent).as_dict()==initial_record, "parent assembly mutated"
        return "move neutral_pos Neutral -> North; separate model; no time/current claim"
    check("REASSIGN_SOURCE_AND_PARENT_IMMUTABILITY",revised_membership)

    def zero_cases():
        e={c["cavity_id"]:c for c in initial_record["cavities"]}
        for name in ("Neutral","Empty"):
            assert e[name]["source_charge_sum_c"]==0
            assert e[name]["induced_inner_face_total_charge_c"]==0
        assert len(e["Neutral"]["authored_sources"])==2
        assert not e["Empty"]["authored_sources"]
        return "local sigma not inferred from whole-face cancellation"
    check("NEUTRAL_NONEMPTY_VS_EMPTY_CAVITY",zero_cases)

    for method,args in [
        ("potential_at",((0,0,0),)),
        ("electric_field_at",((0,0,0),)),
        ("surface_charge_density_at",("North",(0,0,0))),
        ("force_on_source",("n_pos",)),
        ("ground_wire_current",(1.0,)),
    ]:
        check("REFUSE_LOCAL_OR_DYNAMIC_"+method,lambda method=method,args=args:
              must_refuse(lambda:getattr(initial,method)(*args),method))
    for path, fake, name in [
        (("total_interior_source_charge_c",),False,"BOOL_TOTAL"),
        (("cavities",0,"authored_sources",0,"charge_c"),False,"BOOL_SOURCE"),
        (("conductor","equilibrium_net_metal_charge_c"),True,"BOOL_METAL"),
        (("exterior_electric_flux_v_m",),False,"BOOL_FLUX"),
        (("source_role",),"original_jee","SOURCE_PROVENANCE"),
        (("original_workbook_items_newly_solved",),1,"JEE_COUNT"),
        (("assumptions",),[],"FALSE_ASSUMPTIONS"),
        (("conductor","constraint"),"grounded_zero_potential","FALSE_GROUNDING"),
        (("cavities",0,"sealed"),False,"OPEN_CAVITY"),
        (("cavities",1,"cavity_id"),"North","DUPLICATE_CAVITY_ID"),
        (("cavities",1,"induced_inner_face_total_charge_c"),False,"FORGED_FACE_SIGN"),
        (("outer_face_total_charge_c",),0.0,"FORGED_OUTER"),
        (("geometry_verified",),True,"FALSE_GEOMETRY"),
        (("time_evolution_defined",),True,"FALSE_CHRONOLOGY"),
        (("units","exterior_electric_flux"),"C","FALSE_UNITS"),
    ]:
        check("JSON_REJECT_"+name,lambda path=path,fake=fake,name=name:
              must_refuse(lambda:check_gauss_record(edit(path,fake,initial_record)),name))
    def fake_extra():
        bad=copy.deepcopy(initial_record)
        bad["ground_current_a"]=0.1
        return must_refuse(lambda:check_gauss_record(bad),"invented current")
    check("JSON_REJECT_FAKE_DYNAMIC_FIELD",fake_extra)
    def identity_attack():
        bad=copy.deepcopy(initial_record)
        # Change only a stored source ID, preserving all algebra.
        bad["cavities"][0]["authored_sources"][0]["source_id"]="n_neg"
        return must_refuse(lambda:check_gauss_record(bad),"duplicate source identity")
    check("JSON_REJECT_DUPLICATE_IDENTITY",identity_attack)
    def native_face_attack():
        forged=replace(initial,faces=(initial.faces[0],
            replace(initial.faces[1],cavity_id="North"))+initial.faces[2:])
        return must_refuse(lambda:validate_cavity_gauss_ledger(forged),"wrong native face ID")
    check("NATIVE_REJECT_FACE_ID_WITH_SAME_Q",native_face_attack)
    def native_bool_attack():
        forged=replace(initial,total_source_charge_c=False)
        return must_refuse(lambda:forged.as_dict(),"forged Boolean native total")
    check("NATIVE_REJECT_BOOLEAN_ZERO_OR_CHARGE",native_bool_attack)
    def overflow():
        huge=model_for((("Stress",(("plus","1e308"),("more","1e308"))),), Grounded())
        return must_refuse(lambda:solve_cavity_gauss(huge),"finite inputs with sum overflow")
    check("NATIVE_REJECT_FINITE_INPUT_OVERFLOW",overflow)
    def flux_overflow():
        huge=GaussCavityAssembly("Metal",(
            SealedCavity("Stress",(CavityCharge("plus",1e308),)),),
            FixedNetCharge(0.),1e-320)
        return must_refuse(lambda:solve_cavity_gauss(huge),"flux overflows")
    check("NATIVE_REJECT_EXTERIOR_FLUX_OVERFLOW",flux_overflow)

    def large_cancel_valid():
        # fsum genuinely retains small residual; default Decimal sum (28 digits)
        # loses the 1e-9 between 1e150 and -1e150. This accepted native model
        # must NOT be rejected merely because the checker uses less precision.
        m=model_for((("Stress",(("large","1e150"),("residual","1e-9"),
                              ("negative","-1e150"))),),Grounded())
        ledger=solve_cavity_gauss(m)
        doc=ledger.as_dict()
        close(doc["total_interior_source_charge_c"],Decimal("1e-9"),"cancel net")
        close(doc["cavities"][0]["induced_inner_face_total_charge_c"],Decimal("-1e-9"),"cancel inner")
        (out/"review-near-overflow-cancellation.json").write_text(
            json.dumps(doc,indent=2,allow_nan=False)+"\n")
        return check_gauss_record(doc)
    check("HIGH_DYNAMIC_RANGE_VALID_NATIVE_CHECKER_CONSISTENCY",large_cancel_valid)

    def permuted_high_dynamic_range():
        m=model_for((("Stress",(("large","1e150"),("negative","-1e150"),
                              ("residual","1e-9"))),),Grounded())
        doc=solve_cavity_gauss(m).as_dict()
        close(doc["total_interior_source_charge_c"],Decimal("1e-9"),"cancel reordered")
        return check_gauss_record(doc)
    check("HIGH_DYNAMIC_RANGE_REORDERED_CHECKER",permuted_high_dynamic_range)

    def self_consistent_identity_swap():
        changed=copy.deepcopy(initial_record)
        a=changed["cavities"][0]["authored_sources"][0]
        b=changed["cavities"][1]["authored_sources"][0]
        a["source_id"],b["source_id"]=b["source_id"],a["source_id"]
        # Record and native ledger are NOT authenticated to an external manifest.
        # If this passes, note as expected untrusted self-consistent JSON limit,
        # independently compare to the reviewer's immutable DATA IDs.
        check_gauss_record(changed)
        assert [s["source_id"] for s in changed["cavities"][0]["authored_sources"]] != (
            [sid for sid,q in DATA[0][1]])
        return "unanchored self-consistent JSON permits identity re-authoring; cannot attest originals"
    check("DOCUMENT_UNANCHORED_IDENTITY_SWAP_TRUST_LIMIT",self_consistent_identity_swap)

    payload={
        "production_head_expected":"1a11bd03d51645bcc7994ab0ec50a553dd47dc7a",
        "production_tree_expected":"1295380ec4b4c97cb3a8c99aeea1bdb3c8102122",
        "novel_topology":DATA,
        "test_results":RESULTS,
        "failures":FAILED,
    }
    (out/"review-probe-results.json").write_text(json.dumps(payload,indent=2,allow_nan=False)+"\n")
    print("REVIEW_NATIVE_PROBES",len(RESULTS),"FAILURES",FAILED,flush=True)
    return 1 if FAILED else 0

if __name__=="__main__":
    sys.exit(main())
