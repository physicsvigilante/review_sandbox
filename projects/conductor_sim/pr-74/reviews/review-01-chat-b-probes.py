"""Chat B / PR #74 independently authored R2 native adversarial and SI probes.

Source pin: f299478224d3247e439a08425b4ad23712b20c17
This script deliberately does not import developer m32b examples or tests for its
new held-source, oblique x-z plane, gravity and event-root reference.
Only separate specialist refusal fixtures are reused where labelled.
"""
from __future__ import annotations
from dataclasses import replace
from math import fsum, sqrt, isfinite
import json
import sys

from conductor_sim import (
    CoupledPropertyEdit, PhysicalWorldNode, SourceWorldAncestry,
    StructuralWorldNode, UniformElectricField, UnifiedObservationPlan,
    UnifiedObservationRun, PointCharge, PrescribedField, TestChargeMotionSpec,
    UniformGravity, run_unified_observation_graph,
)
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.motion_events import PlaneEvent, EventPolicy
from conductor_sim.structural_family import StructuralCase
from conductor_sim.structural_scenarios import NamedSource, SourceReplacement
from examples.m29b_structural_events import make_plan

RESULTS = {}
def check(condition, text):
    if not condition:
        raise AssertionError(text)

def refuses(label, fn):
    try:
        fn()
    except (TypeError, ValueError):
        RESULTS[label] = "refused"
        return
    raise AssertionError("Hostile mutation unexpectedly accepted: "+label)

def physical(ident, parent, edits, mode="events"):
    return PhysicalWorldNode(
        ident, parent, "R2 reviewer separate SI physical hypothesis",
        tuple(CoupledPropertyEdit(*e) for e in edits), mode)

def novel_plan():
    spec = TestChargeMotionSpec(
        PrescribedField((UniformElectricField((380., 0., -140.)),)),
        PointCharge(1.7e-9, (0., 0., .05)),
        1.4e-6, (.11, 0., .28), .65, .013,
        plane_normal=(0., 1., 0.),
        gravity=UniformGravity((0., 0., -.33)),
    )
    root = PrescribedScenario(
        "review74-original", spec, (("field:base", "Inclined base field"),),
        "Independent oblique x-z motion, explicit gravity, stationary E.")
    seen = "field:fleeting"
    temp = NamedSource(seen, "Temporary oblique field",
                       UniformElectricField((120., 0., 60.)))
    kept = NamedSource("field:kept", "Replaced in-plane field",
                       UniformElectricField((-80., 0., 240.)))
    new = NamedSource("field:fresh", "Unrelated newly held E",
                      UniformElectricField((60., 0., -40.)))
    nodes = (
        StructuralWorldNode("birth", "baseline", StructuralCase(
            "birth", "Introduce transient held source.", add_sources=(temp,)), "events"),
        StructuralWorldNode("retire", "birth", StructuralCase(
            "retire", "Retire transient ID, insert persistent new source.",
            replace_sources=(SourceReplacement(seen, kept),)), "events"),
        physical("edit", "retire", (
            ("field:base", "field_v_m", (480., 0., -240.)),
            ("test-particle", "mass_kg", 1.1e-6),
        )),
        StructuralWorldNode("reuseadd", "edit", StructuralCase(
            "reuseadd", "Hostile re-add of historically retired source.",
            add_sources=(temp,)), "events"),
        StructuralWorldNode("reuseswap", "edit", StructuralCase(
            "reuseswap", "Hostile replacement with historically retired source.",
            replace_sources=(SourceReplacement("field:kept", temp),)), "events"),
        StructuralWorldNode("fresh", "edit", StructuralCase(
            "fresh", "Legitimate independent newly held field.",
            add_sources=(new,)), "events"),
        StructuralWorldNode("siblingA", "baseline", StructuralCase(
            "siblingA", "First unrelated teacher hypothesis.",
            add_sources=(temp,)), "events"),
        StructuralWorldNode("siblingB", "baseline", StructuralCase(
            "siblingB", "Second unrelated teacher hypothesis with same new ID.",
            add_sources=(temp,)), "events"),
    )
    qs = (PlaneEvent("x:review", (.075, 0., 0.), (1., 0., 0.),
                     "Passive detector at x=0.075 m", direction=1),)
    policy = EventPolicy(.008, 1e-9, 1e-8, 1e-7)
    return UnifiedObservationPlan(
        "review74:novel", root, nodes, "events", qs, policy,
        retain_source_ancestry=True)

def direct_si_check(world, event, label):
    """Separate exact constant-E plus gravity Newton reference, no field/ODE callback."""
    spec = world.spec
    check(all(type(s) is UniformElectricField for s in spec.field.sources),
          label+" no longer all uniform fields")
    q = spec.particle.charge_c
    m = spec.mass_kg
    E = tuple(fsum(s.field_v_m[k] for s in spec.field.sources)
              for k in range(3))
    g = spec.gravity.acceleration_m_s2 if spec.gravity is not None else (0.,0.,0.)
    F = tuple(q*E[k]+m*g[k] for k in range(3))
    a = tuple(F[k]/m for k in range(3))
    r0, v0 = spec.particle.position_m, spec.initial_velocity_m_s
    check(event.trajectory.termination == "duration", label+" must complete")
    maxpos, maxvel, maxforce = 0.,0.,0.
    samples = event.trajectory.samples
    check(len(samples)>=4, label+" insufficient genuine SI samples")
    for sample in samples:
        t=sample.time_s
        check(type(t) is float and isfinite(t) and 0<=t<=spec.duration_s,
              label+" invalid native time")
        for k in range(3):
            rx = r0[k] + v0[k]*t + .5*a[k]*t*t
            vx = v0[k] + a[k]*t
            maxpos=max(maxpos,abs(rx-sample.position_m[k]))
            maxvel=max(maxvel,abs(vx-sample.velocity_m_s[k]))
            maxforce=max(maxforce,abs(F[k]-sample.force_n[k]))
    check(maxpos<3e-7 and maxvel<3e-6 and maxforce<1e-12,
          f"{label} standalone SI qE+mg error: {maxpos}, {maxvel}, {maxforce}")
    roots=[ev for ev in event.events if ev.event_id=="x:review"]
    check(len(roots)==1 and roots[0].direction==1,
          label+" expected one positive native x-plane root")
    d=.075-r0[0]
    check(v0[0]>0 and a[0]>0, label+" expected monotonic +x dynamics")
    true=2*d/(v0[0]+sqrt(v0[0]**2+2*a[0]*d))
    root=roots[0]
    native=root.sample.time_s
    check(type(native) is float and root.time_bracket_s[0]<=native<=root.time_bracket_s[1],
          label+" actual event outside root bracket")
    check(abs(native-true)<3e-6, label+" signed SI event discrepancy")
    check(abs(root.sample.position_m[0]-.075)<2e-6, label+" event state off detector")
    check(abs(event.trajectory.samples[-1].time_s-spec.duration_s)<2e-10,
          label+" incomplete actual SI duration")
    return dict(max_position_error_m=maxpos, max_velocity_error_m_s=maxvel,
                max_force_error_n=maxforce, native_root_s=native,
                independent_root_s=true, root_error_s=native-true,
                signed_direction=root.direction, saved_samples=len(samples),
                total_E_v_m=E, gravity_m_s2=g, total_force_n=F)

def test_novel_mixed_graph():
    plan=novel_plan()
    original_snapshot=plan.original.as_dict()
    out=run_unified_observation_graph(plan)
    statuses=[r.status for r in out.entries]
    check(statuses==["complete","complete","complete",
                     "rejected-structural-model","rejected-structural-model",
                     "complete","complete","complete"],
          "unexpected authentic qualification/refusal stages "+str(statuses))
    birth,retire,edit,bad_add,bad_swap,fresh,left,right=out.entries
    check(edit.scenario.parent_revision_id==retire.scenario.revision_id,
          "M20b real direct source parent broken")
    check(retire.assembly.parent is birth.assembly,
          "M22a chained assembly not real retained native ancestor")
    check(fresh.assembly.parent is edit.scenario,
          "M22a after M20b must receive immediate real PrescribedScenario")
    check(fresh.source_ancestry.parent_revision_id==edit.scenario.revision_id,
          "source certificate lost real physical parent SHA")
    check(fresh.source_ancestry.world_path==
          ("baseline","birth","retire","edit","fresh"),
          "source world path lost actual intermediate step")
    check(fresh.source_ancestry.active_source_ids==
          ("field:base","field:kept","field:fresh"),"wrong active ledger")
    check(fresh.source_ancestry.seen_source_ids==
          ("field:base","field:fleeting","field:kept","field:fresh"),
          "historically retired source lost after physical revision")
    check(fresh.source_ancestry.retired_source_ids==("field:fleeting",),
          "retired identity not conserved")
    check(fresh.source_ancestry.gravity_present is True,
          "source gravity membership falsely removed")
    for child in (bad_add,bad_swap):
        check(child.scenario is None and child.native is None and
              child.source_ancestry is None and child.assembly is None,
              "refused child invented physical evidence")
        check("retired or existing" in child.reason,
              "refusal did not demonstrate ancestry prequalification")
    for sibling in (left,right):
        check(sibling.source_ancestry.seen_source_ids==
              ("field:base","field:fleeting") and
              sibling.source_ancestry.world_path==("baseline",sibling.node.node_id),
              "unrelated sibling improperly inherits other branch retirement")
    check(left.scenario.revision_id!=right.scenario.revision_id,
          "alternative world revision identity collapsed")
    check(plan.original.as_dict()==original_snapshot,"graph mutated supplied root")
    world_results={"baseline":direct_si_check(plan.original,out.baseline_native,"baseline")}
    for e in (birth,retire,edit,fresh,left,right):
        world_results[e.node.node_id]=direct_si_check(e.scenario,e.native,e.node.node_id)
    j=out.as_dict()
    check(j["schema"]=="conductor_sim.unified_observation_graph.v2" and
          j["plan"]["schema"]=="conductor_sim.unified_observation_plan.v2" and
          j["plan"]["retain_source_ancestry"] is True,
          "v2 opt-in report schema or policy absent")
    check(j["original_source_ancestry"]["history_scope"].startswith(
          "source identities known from supplied graph root"),
          "root claims unavailable history")
    check(j["nodes"][5]["structural_assembly"]["parent_revision_id"]==
          edit.scenario.revision_id,"JSON structural parent not immediate M20b")
    check(j["nodes"][5]["source_ancestry"]["revision_path"][-1]==
          fresh.scenario.revision_id,"source revision path misreported")
    for i in (0,1,2,5,6,7):
        check(j["nodes"][i]["parent_event_time_comparisons"][0]["status"]==
              "one-resolved-pair",
              "native event comparison not unique complete signed pair")
    check(j["time_interpolation"] is False and
          j["postguard_extrapolation"] is False,
          "invented interpolation/extrapolation")
    RESULTS["novel_graph"]={"statuses":statuses,"worlds":world_results,
                            "root_revision":plan.original.revision_id,
                            "final_revision":fresh.scenario.revision_id,
                            "seen_ids":list(fresh.source_ancestry.seen_source_ids)}
    return out

def test_legacy_and_attacks(run):
    p=novel_plan()
    refuses("legacy_structural_after_physical",lambda: UnifiedObservationPlan(
        "review74:old",p.original,(p.nodes[2],)))
    # Build a valid default legacy plan without the opt-in.
    only=UnifiedObservationPlan("review74:legacy",p.original,(
        physical("massonly","baseline",(("test-particle","mass_kg",1.3e-6),),
                 "trajectory"),))
    old=run_unified_observation_graph(only).as_dict()
    check(old["schema"]=="conductor_sim.unified_observation_graph.v1" and
          old["plan"]["schema"]=="conductor_sim.unified_observation_plan.v1" and
          "original_source_ancestry" not in old and
          "retain_source_ancestry" not in old["plan"] and
          "source_ancestry" not in old["nodes"][0],
          "old v1 export keys unexpectedly changed")
    for value in (0,False, "True", object()):
        if type(value) is bool:
            continue  # False is a valid explicit legacy opt-out.
        refuses("invalid_bool_"+type(value).__name__,lambda v=value:replace(
            run.plan,retain_source_ancestry=v))
    refuses("false_flag_on_mixed_plan",lambda:replace(
        run.plan,retain_source_ancestry=False))
    refuses("changed_plan_label",lambda:replace(
        run,plan=replace(run.plan,plan_id="review74:altered")))
    refuses("mutated_replacement_note",lambda:replace(
        run,plan=replace(run.plan,nodes=(
            run.plan.nodes[0],
            replace(run.plan.nodes[1],
                    case=replace(run.plan.nodes[1].case,
                                 note="Revised unobserved source interpretation")),
            *run.plan.nodes[2:]))))
    edit=run.entries[2]
    changed_edit=replace(edit.node,edits=(CoupledPropertyEdit(
        "field:base","field_v_m",(720.,0.,-240.)),edit.node.edits[1]))
    refuses("edited_physical_values",lambda:replace(
        run,plan=replace(run.plan,nodes=(
            *run.plan.nodes[:2],changed_edit,*run.plan.nodes[3:]))))
    cert=run.entries[5].source_ancestry
    check(type(cert) is SourceWorldAncestry,"native certificate wrong type")
    refuses("cert_retired_ledger",lambda:replace(
        run,entries=(
            *run.entries[:5],
            replace(run.entries[5],source_ancestry=replace(
                cert,seen_source_ids=tuple(s for s in cert.seen_source_ids
                                          if s!="field:fleeting"),
                retired_source_ids=())),
            *run.entries[6:])))
    refuses("cert_string_type",lambda:replace(
        cert,active_source_ids=("field:base",False,"field:fresh")))
    refuses("cert_gravity_boolean",lambda:replace(cert,gravity_present=0))
    refuses("replace_cert_by_plain_json",lambda:replace(
        run,entries=(*run.entries[:5],
                     replace(run.entries[5],source_ancestry=cert.as_dict()),
                     *run.entries[6:])))
    refuses("fake_accepted_refusal",lambda:replace(
        run,entries=(*run.entries[:5],
                     replace(run.entries[5],native=None,
                             status="rejected-event-study",
                             reason="invented event-study refusal"),
                     *run.entries[6:])))
    native=run.entries[5].native
    root=next(ev for ev in native.events if ev.event_id=="x:review")
    forged=replace(root,sample=replace(root.sample,time_s=root.sample.time_s+.03),
                   time_bracket_s=tuple(t+.03 for t in root.time_bracket_s))
    refuses("root_plus_30ms",lambda:replace(
        run,entries=(*run.entries[:5],
                     replace(run.entries[5],native=replace(
                         native,events=(forged,))),*run.entries[6:])))
    refuses("boolean_root_time",lambda:replace(
        run,entries=(*run.entries[:5],
                     replace(run.entries[5],native=replace(
                         native,events=(replace(
                             root,sample=replace(root.sample,time_s=False)),))),
                     *run.entries[6:])))
    changed=replace(run.entries[5],source_ancestry=None)
    cloned=replace(run)
    object.__setattr__(cloned,"entries",(
        *cloned.entries[:5],changed,*cloned.entries[6:]))
    refuses("pre_export_ancestry_mutation",cloned.as_dict)
    RESULTS["legacy_v1"]="original schema retained with no ancestry fields"
    RESULTS["in_process_receipt"]="ordinary dataclass forgeries refused; no cryptographic assertion"

def test_event_safety():
    old=make_plan("terminal-refusal")
    p=UnifiedObservationPlan("review74:refusal",old.family.baseline,(
        physical("badstudy","baseline",
                 (("field:Eneg","field_v_m",(1000.,0.,0.)),)),
        StructuralWorldNode("repair","badstudy",StructuralCase(
            "repair","Independent structurally qualified correcting field.",
            add_sources=(NamedSource("field:repair","Independent rescue E",
                      UniformElectricField((-4200.,0.,0.))),)),"events"),
    ),"events",old.questions,old.policy,retain_source_ancestry=True)
    run=run_unified_observation_graph(p)
    parent,child=run.entries
    check(parent.scenario is not None and parent.native is None and
          parent.status=="rejected-event-study",
          "admitted physical parent did not truly refuse event-study")
    check(child.scenario is not None and child.native is not None and
          child.status=="complete" and child.assembly.parent is parent.scenario,
          "physically qualified structural descendant did not get fresh M24a run")
    check(run.as_dict()["nodes"][1]["parent_event_time_comparisons"][0]["status"]=="unpaired",
          "refused parent fabricated event-time shift")

    g=make_plan("guard-detector")
    candidate=next(c for c in g.family.cases if c.case_id=="attract-guard")
    guard=run_unified_observation_graph(UnifiedObservationPlan(
        "review74:guard",g.family.baseline,(
            physical("launch","baseline",
                    (("test-particle","initial_velocity_m_s",(1.1,0.,0.)),)),
            StructuralWorldNode("attract-guard","launch",candidate,"events"),
        ),"events",g.questions,g.policy,retain_source_ancestry=True))
    final=guard.entries[1]
    check(final.status=="censored-source-guard" and
          final.native.trajectory.termination=="source-guard",
          "real guard was not retained")
    outcomes=final.native.as_dict()["outcomes"]
    check(outcomes["x:early"]=="located" and
          outcomes["x:far"]=="search-truncated",
          "early true root or unobserved late root corrupted")
    check(all(row["status"]=="unpaired" for row in
              guard.as_dict()["nodes"][1]["parent_event_time_comparisons"]),
          "censored root improperly paired")
    d=make_plan("double-crossing")
    dc=run_unified_observation_graph(UnifiedObservationPlan(
        "review74:bidirectional",d.family.baseline,(
            physical("mass","baseline",
                     (("test-particle","mass_kg",1.1e-6),)),
            StructuralWorldNode("retarding","mass",d.family.cases[0],"events"),
        ),"events",d.questions,d.policy,retain_source_ancestry=True))
    names=[]
    for native in (dc.baseline_native,dc.entries[0].native,dc.entries[1].native):
        check(native.trajectory.termination=="duration",
              "two-crossing world did not complete")
        roots=[ev for ev in native.events if ev.event_id=="x:two-crossings"]
        check(len(roots)==2 and [ev.direction for ev in roots]==[1,-1],
              "two opposite-signed roots not truly located")
        names.append([float(ev.sample.time_s) for ev in roots])
    check(dc.as_dict()["nodes"][1]["parent_event_time_comparisons"][0]["status"]==
          "unpaired","opposite signed multi-roots falsely uniquely paired")
    RESULTS["event_boundaries"]={
        "event_study_refusal_then_child":"refused/complete",
        "source_guard":{"early":outcomes["x:early"],"late":outcomes["x:far"]},
        "two_real_signed_roots":names,
        "cross_world_pairing":"unpaired",
    }

def main():
    run=test_novel_mixed_graph()
    test_legacy_and_attacks(run)
    test_event_safety()
    out={"reviewer":"separate Chat B context","source_sha":
         "f299478224d3247e439a08425b4ad23712b20c17",
         "tree":"a7885a7f7f4a4a34e74af43af5217a71a97fe31b",
         "verdict":"PASS" ,"probes":RESULTS}
    dest=sys.argv[1] if len(sys.argv)>1 else "../review74-chatb-native.json"
    with open(dest,"w",encoding="utf-8") as f:
        json.dump(out,f,indent=2,sort_keys=True,allow_nan=False)
        f.write("\n")
    print(json.dumps({"verdict":"PASS","probe_names":list(RESULTS),
                      "world_count":len(RESULTS["novel_graph"]["worlds"])},
                     sort_keys=True))
if __name__=="__main__":
    main()
