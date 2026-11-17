"""Chat B, independent R2 tests for M33a conductor_sim PR #75.
Pinned immutable source HEAD 117990d239503a947f7be2896c52ffd10a2cacf1.
Author-original 3D oblique-plane qE+mg worlds and detector roots.
Only M29b established fixtures are reused for specialized *refusal* boundaries.
Never imports M33a developer tests, example or independent reference.
"""
from __future__ import annotations

from dataclasses import replace
from math import dist, isclose, isfinite, sqrt
import json
from pathlib import Path
import sys

from conductor_sim import (
    CoupledPropertyEdit, PhysicalWorldNode, StructuralWorldNode,
    PointCharge, PrescribedField, TestChargeMotionSpec, UniformElectricField,
    UniformGravity, UnifiedObservationPlan, run_unified_observation_graph,
)
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.structural_family import StructuralCase
from conductor_sim.structural_scenarios import NamedSource
from conductor_sim.motion_events import PlaneEvent, EventPolicy

CHECKS = {}
SOURCE_HEAD = "117990d239503a947f7be2896c52ffd10a2cacf1"
E0 = (180., -135., -110.)
EA = (60., -45., -20.)
EB = (-50., 37.5, -20.)
G = (.04, -.03, .02)
R0 = (.003, .012, .06)
V0 = (.15, -.1125, -.19)
Q = 2e-9
M = 1.6e-6
MH = 2.4e-6
T = .8
DETECTOR_X = .082
POLICY = EventPolicy(.009, 1e-9, 1e-8, 1e-7)
EVENT = PlaneEvent(
    "x:oblique", (DETECTOR_X, 0., 0.), (1., 0., 0.),
    "Positive x detector, oblique 3D plane", direction=1,
)
EXPECTED = {
    "baseline": {"E": E0, "mass": M, "ids": ("field:origin",),
                 "labels": ("Original diagonal held field",), "path": ("baseline",)},
    "alpha": {"E": tuple(E0[k]+EA[k] for k in range(3)), "mass": M,
              "ids": ("field:origin", "field:alternate"),
              "labels": ("Original diagonal held field", "Alpha in-plane field"),
              "path": ("baseline", "alpha")},
    "beta": {"E": tuple(E0[k]+EB[k] for k in range(3)), "mass": M,
             "ids": ("field:origin", "field:alternate"),
             "labels": ("Original diagonal held field", "Beta in-plane field"),
             "path": ("baseline", "beta")},
    "heavier": {"E": tuple(E0[k]+EA[k] for k in range(3)), "mass": MH,
                "ids": ("field:origin", "field:alternate"),
                "labels": ("Original diagonal held field", "Alpha in-plane field"),
                "path": ("baseline", "alpha", "heavier")},
    "retired": {"E": E0, "mass": MH, "ids": ("field:origin",),
                "labels": ("Original diagonal held field",),
                "path": ("baseline", "alpha", "heavier", "retired")},
}


def need(test, meaning):
    if not test:
        raise AssertionError(meaning)


def marked(label, result):
    CHECKS[label] = result


def refuses(label, fn):
    try:
        fn()
    except (ValueError, TypeError, RuntimeError) as e:
        CHECKS[label] = type(e).__name__ + ": " + str(e)[:120]
        return
    raise AssertionError("Expected a refusal: " + label)


def root_model():
    return PrescribedScenario(
        "chatb75:oblique-original",
        TestChargeMotionSpec(
            PrescribedField((UniformElectricField(E0),)),
            PointCharge(Q, R0), M, V0, T, .02,
            plane_normal=(.6, .8, 0.),
            gravity=UniformGravity(G),
        ),
        (("field:origin", "Original diagonal held field"),),
        "Reviewer-authored oblique full-3D-in-components stationary E and g.",
    )


def native_plan():
    # The two sibling worlds independently reuse the same branch-local ID.
    original = root_model()
    alpha_source = NamedSource(
        "field:alternate", "Alpha in-plane field", UniformElectricField(EA))
    beta_source = NamedSource(
        "field:alternate", "Beta in-plane field", UniformElectricField(EB))
    nodes = (
        StructuralWorldNode("alpha", "baseline", StructuralCase(
            "alpha", "Independent first held-source hypothesis.",
            add_sources=(alpha_source,)), "events"),
        StructuralWorldNode("beta", "baseline", StructuralCase(
            "beta", "Distinct second held-source hypothesis.",
            add_sources=(beta_source,)), "events"),
        PhysicalWorldNode(
            "heavier", "alpha", "Physically change probe mass.",
            (CoupledPropertyEdit("test-particle", "mass_kg", MH),), "events"),
        StructuralWorldNode("retired", "heavier", StructuralCase(
            "retired", "Remove branch-specific held source after real physical edit.",
            remove_sources=("field:alternate",)), "events"),
        StructuralWorldNode("revived", "retired", StructuralCase(
            "revived", "Illicit resurrection of branch-retired source ID.",
            add_sources=(alpha_source,)), "events"),
    )
    from conductor_sim import WorldComparison
    comparisons = (
        WorldComparison("two-siblings", "alpha", "beta"),
        WorldComparison("distant-cousins", "beta", "heavier"),
        WorldComparison("with-original", "baseline", "beta"),
        WorldComparison("after-retirement", "retired", "beta"),
    )
    return UnifiedObservationPlan(
        "chatb75:novel", original, nodes, "events", (EVENT,), POLICY,
        retain_source_ancestry=True, comparisons=comparisons,
    )


def solve_independently(name):
    """Separate Newtonian closed form using reviewer constants, no production force."""
    model = EXPECTED[name]
    e = model["E"]
    mass = model["mass"]
    f = tuple(Q*e[k]+mass*G[k] for k in range(3))
    a = tuple(f[k]/mass for k in range(3))
    dx = DETECTOR_X-R0[0]
    need(V0[0]>0 and a[0]>0, "reference positive monotonic x crossing")
    troot = 2*dx/(V0[0]+sqrt(V0[0]**2+2*a[0]*dx))
    need(0<troot<T, "analytic crossing within actual duration")
    return f, a, troot


def reference_state(a, t):
    r = tuple(R0[k] + V0[k]*t + .5*a[k]*t*t for k in range(3))
    v = tuple(V0[k]+a[k]*t for k in range(3))
    return r, v


def check_world(name, scenario, native):
    model = EXPECTED[name]
    need(scenario is not None and native is not None, name+": genuine native missing")
    need(native.study.scenario is scenario, name+": wrong M24a source model")
    need(native.trajectory.termination == "duration", name+": incomplete horizon")
    need(native.study.questions[0].event_id == EVENT.event_id, name+": mismatched event")
    need(isclose(scenario.spec.mass_kg, model["mass"], abs_tol=1e-17), name+": wrong mass")
    need(tuple(identity for identity,_ in scenario.source_annotations) == model["ids"],
         name+": incorrect side-specific active IDs")
    need(tuple(label for _,label in scenario.source_annotations) == model["labels"],
         name+": incorrect side-specific source labels")
    need(all(type(s) is UniformElectricField for s in scenario.spec.field.sources),
         name+": wrong actual native source kinds")
    need(scenario.spec.particle.position_m == R0, name+": wrong initial 3D position")
    need(scenario.spec.initial_velocity_m_s == V0, name+": wrong initial velocity")
    force, a, independent_root = solve_independently(name)
    samples = native.trajectory.samples
    need(len(samples)>=8, name+": no genuine time series")
    max_p = max_v = max_f = 0.
    for s in samples:
        need(type(s.time_s) is float and isfinite(s.time_s) and 0<=s.time_s<=T,
             name+": invalid native SI clock")
        expected_p, expected_v = reference_state(a, s.time_s)
        for k in range(3):
            max_p=max(max_p, abs(s.position_m[k]-expected_p[k]))
            max_v=max(max_v, abs(s.velocity_m_s[k]-expected_v[k]))
            max_f=max(max_f, abs(s.force_n[k]-force[k]))
    need(max_p<5e-7 and max_v<5e-6 and max_f<2e-12,
         name+f": 3D Newtonian discrepancy p={max_p},v={max_v},f={max_f}")
    roots = [ev for ev in native.events if ev.event_id==EVENT.event_id]
    need(len(roots)==1 and roots[0].direction==1,
         name+": missing actual unique positive M24a root")
    r = roots[0]
    need(r.time_bracket_s[0]<=r.sample.time_s<=r.time_bracket_s[1],
         name+": true bracket does not contain native numerical root")
    need(abs(r.sample.time_s-independent_root)<4e-6,
         name+": independently computed signed detector root differs")
    need(abs(r.sample.position_m[0]-DETECTOR_X)<2e-7,
         name+": localized point not at detector")
    need(samples[-1].time_s==T, name+": native duration not completed")
    # Independent plane closure check, without projection onto x or z axes.
    need(abs(.6*a[0]+.8*a[1])<5e-13 and abs(.6*V0[0]+.8*V0[1])<5e-13,
         name+": three-axis tangent-plane condition incorrect")
    marked("physics_"+name, dict(samples=len(samples), force_n=force, acceleration_m_s2=a,
        x_root_independent_s=independent_root, x_root_native_s=r.sample.time_s,
        root_bracket_s=r.time_bracket_s, max_position_error_m=max_p,
        max_velocity_error_m_s=max_v, max_force_error_n=max_f))
    return independent_root


def review_novel():
    p = native_plan()
    root_record = p.original.as_dict()
    r = run_unified_observation_graph(p)
    need(r.baseline_status=="complete", "baseline native M24a failed")
    need([e.status for e in r.entries] == [
        "complete","complete","complete","complete","rejected-structural-model"],
        "branch statuses mismatch "+repr([(e.status,e.reason) for e in r.entries]))
    alpha,beta,heavier,retired,revived = r.entries
    need(revived.scenario is None and revived.assembly is None and
         revived.native is None and revived.source_ancestry is None,
         "retired ID resurrection created physics")
    need("retired or existing" in revived.reason,
         "retired ID should be rejected specifically by preserved lineage")
    need(heavier.scenario.parent_revision_id==alpha.scenario.revision_id,
         "physical edit did not retain true immediate model revision")
    need(retired.assembly.parent is heavier.scenario,
         "structural-after-physical parent object identity lost")
    need(retired.assembly.as_dict()["parent_revision_id"]==heavier.scenario.revision_id,
         "structural-after-physical parent hash changed")
    need(alpha.scenario.revision_id!=beta.scenario.revision_id,
         "independent sibling model revision SHA collided")
    need(alpha.source_ancestry.seen_source_ids==
         beta.source_ancestry.seen_source_ids==
         ("field:origin","field:alternate"), "branch ledger not local")
    need(alpha.source_ancestry.world_path==("baseline","alpha") and
         beta.source_ancestry.world_path==("baseline","beta"),
         "siblings falsely merged their physical ancestry")
    need(retired.source_ancestry.seen_source_ids==
         ("field:origin","field:alternate") and
         retired.source_ancestry.retired_source_ids==("field:alternate",),
         "branch-retired ID lost across physical model revision")
    worlds = {"baseline": (p.original, r.baseline_native)}
    worlds.update((e.node.node_id,(e.scenario,e.native)) for e in r.entries if e.scenario)
    roots={}
    for name, (scenario, native) in worlds.items():
        roots[name]=check_world(name,scenario,native)
    out = r.as_dict()
    need(out["schema"]=="conductor_sim.unified_observation_graph.v3" and
         out["plan"]["schema"]=="conductor_sim.unified_observation_plan.v3",
         "explicit comparisons must export v3")
    need(len(out["cross_world_comparisons"])==4, "comparison count/order lost")
    for record, req in zip(out["cross_world_comparisons"],p.comparisons):
        left, right = req.left_world_id, req.right_world_id
        need((record["comparison_id"],record["left_world_id"],record["right_world_id"])==
             (req.comparison_id,left,right),"comparison identity/order altered")
        need(record["status"]=="compared" and
             record["numerical_orientation"]=="right minus left",
             "authentic native worlds not compared")
        ls,ln=worlds[left]; rs,rn=worlds[right]
        need(record["left_revision_id"]==ls.revision_id and
             record["right_revision_id"]==rs.revision_id,
             "one of compared full physical revisions incorrect")
        for side,name,scenario in (("left",left,ls),("right",right,rs)):
            anc = record[side+"_source_ancestry"]
            need(tuple(anc["world_path"])==EXPECTED[name]["path"] and
                 anc["model_revision_id"]==scenario.revision_id and
                 anc["revision_path"][-1]==scenario.revision_id and
                 len(anc["world_path"])==len(anc["revision_path"]),
                 "wrong full branch-local revision ancestry on "+side)
            need(record[side+"_source_inventory"]==[
                dict(id=i,label=l,kind="UniformElectricField")
                for i,l in zip(EXPECTED[name]["ids"],EXPECTED[name]["labels"])],
                 "wrong actual source inventory label or kind on "+side)
        native_left,native_right=ln.trajectory,rn.trajectory
        left_clocks={s.time_s for s in native_left.samples}
        expected_clocks=[s.time_s for s in native_right.samples if s.time_s in left_clocks]
        rows=record["exact_time_trajectory_comparisons"]
        need([row["time_s"] for row in rows]==expected_clocks and len(rows)>=8,
             "not exact literal same physical saved SI clocks")
        _,al,_=solve_independently(left)
        _,ar,_=solve_independently(right)
        for row in rows:
            t=row["time_s"]
            lp,lv=reference_state(al,t)
            rp,rv=reference_state(ar,t)
            dp=tuple(rp[k]-lp[k] for k in range(3))
            dv=tuple(rv[k]-lv[k] for k in range(3))
            need(all(abs(row["delta_position_m"][k]-dp[k])<7e-7 for k in range(3)),
                 "right-minus-left three-coordinate position delta incorrect")
            need(all(abs(row["delta_velocity_m_s"][k]-dv[k])<7e-6 for k in range(3)),
                 "right-minus-left three-coordinate velocity delta incorrect")
            need(abs(row["position_distance_m"]-sqrt(sum(d*d for d in dp)))<7e-7 and
                 abs(row["velocity_distance_m_s"]-sqrt(sum(d*d for d in dv)))<7e-6,
                 "vector delta norms do not match independent formula")
        eventpair=record["event_time_comparisons"]
        need(len(eventpair)==1 and eventpair[0]["status"]=="one-resolved-pair"
             and eventpair[0]["direction"]==1,
             "genuine same-direction whole-duration roots not paired")
        pair=eventpair[0]
        need(abs(pair["estimated_numerical_shift_s"]-(roots[right]-roots[left]))<8e-6,
             "independent signed event shift disagreement")
        lr=ln.events[0].time_bracket_s; rr=rn.events[0].time_bracket_s
        need(abs(pair["numerical_bracket_shift_interval_s"][0]-(rr[0]-lr[1]))<1e-14
             and abs(pair["numerical_bracket_shift_interval_s"][1]-(rr[1]-lr[0]))<1e-14,
             "event numerical bracket shift wrong")
        marked("pair_"+req.comparison_id,dict(rows=len(rows),
            first_position_delta_m=rows[0]["delta_position_m"],
            last_position_delta_m=rows[-1]["delta_position_m"],
            shift_s=pair["estimated_numerical_shift_s"],
            independent_shift_s=roots[right]-roots[left]))
    need(p.original.as_dict()==root_record,"root was mutated by native worlds")
    detached=out
    detached["cross_world_comparisons"][0]["status"]="forged"
    detached["nodes"][0]["source_ancestry"]["world_path"]=["fabricated"]
    need(r.as_dict()["cross_world_comparisons"][0]["status"]=="compared" and
         r.as_dict()["nodes"][0]["source_ancestry"]["world_path"]!=["fabricated"],
         "detached exported JSON changed native receipt")
    marked("detached_export_independent",True)
    return r


def attack_probes(r):
    from conductor_sim import WorldComparison
    p=r.plan
    refuses("request_boolean_id",lambda:WorldComparison("bad",True,"alpha"))
    refuses("request_bad_ascii_id",lambda:WorldComparison("bad space","alpha","beta"))
    refuses("request_same_world",lambda:WorldComparison("identical","alpha","alpha"))
    refuses("request_plain_tuple",lambda:replace(p,comparisons=(("bad","alpha","beta"),)))
    refuses("request_unknown_world",lambda:replace(p,comparisons=(
        WorldComparison("unknown","alpha","missing"),)))
    refuses("request_unordered_duplicate",lambda:replace(p,comparisons=(
        WorldComparison("one","alpha","beta"),WorldComparison("two","beta","alpha"))))
    refuses("request_duplicate_id",lambda:replace(p,comparisons=(
        WorldComparison("sameid","alpha","beta"),
        WorldComparison("sameid","alpha","heavier"))))
    refuses("request_missing_ancestry",lambda:replace(p,retain_source_ancestry=False))
    refuses("result_changed_pair_order",lambda:replace(r,plan=replace(p,comparisons=(
        *p.comparisons[::-1],))))
    refuses("result_changed_pair_label",lambda:replace(r,plan=replace(p,comparisons=(
        WorldComparison("renamed","alpha","beta"),*p.comparisons[1:]))))
    refuses("result_original_source_provenance",lambda:replace(r,plan=replace(
        p,original=replace(p.original,provenance="Forged textbook attestation"))))
    case=p.nodes[0].case
    tamper_case=replace(case,add_sources=(replace(
        case.add_sources[0],label="Unobserved alternative display label"),))
    refuses("result_source_inventory_label",lambda:replace(r,plan=replace(
        p,nodes=(replace(p.nodes[0],case=tamper_case),*p.nodes[1:]))))
    refuses("result_wrong_ancestor",lambda:replace(r,entries=(
        *r.entries[:3],
        replace(r.entries[3],source_ancestry=replace(
            r.entries[3].source_ancestry,
            parent_revision_id=r.plan.original.revision_id,
            revision_path=(
                *r.entries[3].source_ancestry.revision_path[:-2],
                r.plan.original.revision_id,
                r.entries[3].source_ancestry.model_revision_id))),
        *r.entries[4:])))
    refuses("result_wrong_physical_edit",lambda:replace(r,plan=replace(
        p,nodes=(*p.nodes[:2],
                 replace(p.nodes[2],edits=(
                     CoupledPropertyEdit("test-particle","mass_kg",2.8e-6),)),
                 *p.nodes[3:]))))
    refuses("result_wrong_status",lambda:replace(r,entries=(
        replace(r.entries[0],status="censored-source-guard"),*r.entries[1:])))
    refuses("result_wrong_refused_status",lambda:replace(r,entries=(
        *r.entries[:4],
        replace(r.entries[4],status="complete"),)))
    evt=r.entries[0].native
    root=evt.events[0]
    changed=replace(root,
        sample=replace(root.sample,time_s=root.sample.time_s+.03),
        time_bracket_s=tuple(t+.03 for t in root.time_bracket_s))
    refuses("result_root_plus_30ms",lambda:replace(r,entries=(
        replace(r.entries[0],native=replace(evt,events=(changed,))),
        *r.entries[1:])))
    refuses("result_bool_event_time",lambda:replace(r,entries=(
        replace(r.entries[0],native=replace(
            evt,events=(replace(root,sample=replace(root.sample,time_s=False)),))),
        *r.entries[1:])))
    sample=evt.trajectory.samples[0]
    forged_track=replace(evt.trajectory,samples=(
        replace(sample,time_s=False),*evt.trajectory.samples[1:]))
    refuses("result_bool_native_clock",lambda:replace(r,entries=(
        replace(r.entries[0],native=replace(evt,trajectory=forged_track)),
        *r.entries[1:])))
    refuses("result_fake_issued_digest",lambda:replace(r,_issued_digest="f"*64))
    altered=replace(r)
    object.__setattr__(altered,"baseline_reason","silently changed after construction")
    refuses("in_process_mutation_before_export",altered.as_dict)
    marked("adversarial_count",len([key for key in CHECKS if key.startswith("request_") or
        key.startswith("result_") or key.startswith("in_process_")]))


def event_boundaries():
    from conductor_sim import WorldComparison
    from examples.m29b_structural_events import make_plan
    # Real supported native event mode versus real ordinary-trajectory mode.
    original = root_model()
    event_node=PhysicalWorldNode(
        "event-one","baseline","Native event observed probe",
        (CoupledPropertyEdit("test-particle","mass_kg",MH),),"events")
    ordinary_node=StructuralWorldNode(
        "ordinary","baseline",StructuralCase(
            "ordinary","Native ordinary observation with added stationary source.",
            add_sources=(NamedSource("field:extra","Held source",
                UniformElectricField(EA)),)),"trajectory")
    mixed=UnifiedObservationPlan(
        "chatb75:mode",original,(event_node,ordinary_node),"events",(EVENT,),POLICY,
        retain_source_ancestry=True,
        comparisons=(WorldComparison("mode","event-one","ordinary"),))
    mismatch=run_unified_observation_graph(mixed).as_dict()["cross_world_comparisons"][0]
    need(mismatch["status"]=="unpaired" and
         not mismatch["exact_time_trajectory_comparisons"] and
         not mismatch["event_time_comparisons"],"mixed modes invented evidence")
    marked("event_vs_ordinary_mode",mismatch["reason"])
    physically_bad=UnifiedObservationPlan(
        "chatb75:bad",original,(
            PhysicalWorldNode("bad","baseline","Invalid negative probe mass",
                (CoupledPropertyEdit("test-particle","mass_kg",-1.),),"events"),
            PhysicalWorldNode("good","baseline","Valid other probe mass",
                (CoupledPropertyEdit("test-particle","mass_kg",MH),),"events"),
        ),"events",(EVENT,),POLICY,retain_source_ancestry=True,
        comparisons=(WorldComparison("bad-model","bad","good"),))
    bb=run_unified_observation_graph(physically_bad).as_dict()["cross_world_comparisons"][0]
    need(bb["status"]=="unpaired" and bb["left_revision_id"] is None and
         bb["right_revision_id"] is not None and
         bb["left_source_ancestry"] is None and
         bb["exact_time_trajectory_comparisons"]==[],
         "refused physical model invented comparison")
    marked("physical_model_refused",bb["reason"])
    # Old M29b fixtures are used only as independent policy regression inputs.
    old=make_plan("terminal-refusal")
    refusal=UnifiedObservationPlan(
        "chatb75:refusal",old.family.baseline,(
            StructuralWorldNode("reversed-force","baseline",old.family.cases[0],"events"),
            PhysicalWorldNode("recovery","reversed-force",
                "Real M20b correction makes an event study admissible",
                (CoupledPropertyEdit("field:Eplus","field_v_m",(500.,0.,0.)),
                 CoupledPropertyEdit("test-particle","mass_kg",2e-6)),"events"),
        ),"events",old.questions,old.policy,retain_source_ancestry=True,
        comparisons=(WorldComparison("event-refusal","reversed-force","recovery"),))
    x=run_unified_observation_graph(refusal)
    need(x.entries[0].status=="rejected-event-study" and x.entries[0].scenario is not None
         and x.entries[0].native is None and
         x.entries[1].status=="complete" and x.entries[1].native is not None,
         "actual admitted-but-event-refused model misrepresented")
    cmp=x.as_dict()["cross_world_comparisons"][0]
    need(cmp["status"]=="unpaired" and cmp["left_revision_id"] is not None
         and cmp["event_time_comparisons"][0]["status"]=="unpaired",
         "event-study refusal not carried through pair evidence")
    marked("admitted_but_event_refused",cmp["reason"])
    guard=make_plan("guard-detector")
    guard_case=next(x for x in guard.family.cases if x.case_id=="attract-guard")
    gr=run_unified_observation_graph(UnifiedObservationPlan(
        "chatb75:guard",guard.family.baseline,
        (StructuralWorldNode("attract-guard","baseline",guard_case,"events"),),
        "events",guard.questions,guard.policy,retain_source_ancestry=True,
        comparisons=(WorldComparison("guard","baseline","attract-guard"),)))
    need(gr.entries[0].status=="censored-source-guard",
         "independent old M29b guard was not genuine")
    need(any(event.event_id=="x:early" for event in gr.entries[0].native.events),
         "genuine early located event absent before source guard")
    cr=gr.as_dict()["cross_world_comparisons"][0]
    need(cr["status"]=="compared" and cr["exact_time_trajectory_comparisons"],
         "guard should retain actual preguard shared samples")
    need(all(ev["status"]=="unpaired" and
             "estimated_numerical_shift_s" not in ev
             for ev in cr["event_time_comparisons"]), "source guard paired event")
    limit=gr.entries[0].native.trajectory.samples[-1].time_s
    need(all(s["time_s"]<=limit for s in cr["exact_time_trajectory_comparisons"]),
         "source guard trajectory falsely extrapolated")
    marked("early_root_later_censored",dict(limit_s=limit,event_records=
        [e["status"] for e in cr["event_time_comparisons"]]))
    dbl=make_plan("double-crossing")
    dr=run_unified_observation_graph(UnifiedObservationPlan(
        "chatb75:double",dbl.family.baseline,
        (StructuralWorldNode("extra-retarding","baseline",dbl.family.cases[0],"events"),),
        "events",dbl.questions,dbl.policy,retain_source_ancestry=True,
        comparisons=(WorldComparison("double","baseline","extra-retarding"),)))
    need(all(len(native.events)==2 for native in (dr.baseline_native,dr.entries[0].native)),
         "genuine double signed crossings not observed")
    dcmp=dr.as_dict()["cross_world_comparisons"][0]
    need(dcmp["event_time_comparisons"][0]["status"]=="unpaired" and
         "multiple crossings" in dcmp["event_time_comparisons"][0]["reason"],
         "two genuine roots falsely called a unique shift")
    marked("double_signed_roots","unpaired")
    # Independent converse root, same detector, same full event policy.
    opposite_question=PlaneEvent(
        "x:both", (DETECTOR_X,0.,0.), (1.,0.,0.),"Signed each way",direction=0)
    reverse=UnifiedObservationPlan(
        "chatb75:opposite",original,(
            PhysicalWorldNode("reverse","baseline","Actual reverse x launch",
                (CoupledPropertyEdit("test-particle","position_m",(.16,.012,.06)),
                 CoupledPropertyEdit("test-particle","initial_velocity_m_s",(-.45,.3375,.25))),
                "events"),),
        "events",(opposite_question,),POLICY,retain_source_ancestry=True,
        comparisons=(WorldComparison("opposite","baseline","reverse"),))
    rev=run_unified_observation_graph(reverse)
    need(len(rev.baseline_native.events)==len(rev.entries[0].native.events)==1 and
         rev.baseline_native.events[0].direction==1 and
         rev.entries[0].native.events[0].direction==-1,
         "authentic opposite unique signed roots not present")
    revcmp=rev.as_dict()["cross_world_comparisons"][0]
    need(revcmp["event_time_comparisons"][0]["status"]=="unpaired" and
         "opposite signed" in revcmp["event_time_comparisons"][0]["reason"],
         "opposite signed unique roots were paired")
    marked("opposite_unique_roots","unpaired")
    terminal=make_plan("coincident-terminal")
    termrun=run_unified_observation_graph(UnifiedObservationPlan(
        "chatb75:terminal",terminal.family.baseline,
        (StructuralWorldNode("more-E","baseline",terminal.family.cases[0],"events"),),
        "events",terminal.questions,terminal.policy,retain_source_ancestry=True,
        comparisons=(WorldComparison("terminal","baseline","more-E"),)))
    tc=termrun.as_dict()["cross_world_comparisons"][0]
    need(termrun.baseline_native.trajectory.termination!="duration" and
         tc["status"]=="compared" and
         all(ev["status"]=="unpaired" for ev in tc["event_time_comparisons"]),
         "true terminal/unresolved horizon falsely compared as full")
    marked("terminal_or_unresolved",dict(baseline=termrun.baseline_native.trajectory.termination,
        side=termrun.entries[0].status,events=len(tc["event_time_comparisons"])))


def legacy_records():
    """Identical script executes with M32b *base* import and M33a *head* import."""
    orig = root_model()
    out={}
    for ancestry in (False, True):
        p=UnifiedObservationPlan(
            "chatb75:legacy",orig,
            (PhysicalWorldNode("mass","baseline","Old native mass revision",
                (CoupledPropertyEdit("test-particle","mass_kg",MH),),"trajectory"),),
            "trajectory",retain_source_ancestry=ancestry)
        rec=run_unified_observation_graph(p).as_dict()
        old=f"v{2 if ancestry else 1}"
        need(rec["schema"]=="conductor_sim.unified_observation_graph."+old and
             rec["plan"]["schema"]=="conductor_sim.unified_observation_plan."+old,
             "old plan/result schema changed")
        need("cross_world_comparisons" not in rec and
             "cross_world_comparison_rule" not in rec and
             "comparisons" not in rec["plan"],"new v3 fields leaked into old schema")
        if not ancestry:
            need("source_ancestry_policy" not in rec and
                 "original_source_ancestry" not in rec and
                 "retain_source_ancestry" not in rec["plan"],
                 "legacy v1 gained new v2 policy")
        else:
            need("original_source_ancestry" in rec and
                 rec["plan"]["retain_source_ancestry"] is True,
                 "legacy v2 lost existing source policy")
        out[old]=rec
    refuses("legacy_structural_after_physical",lambda:UnifiedObservationPlan(
        "chatb75:legacyrefuse",orig,(
            PhysicalWorldNode("edit","baseline","Existing physical edit",
                (CoupledPropertyEdit("test-particle","mass_kg",MH),)),
            StructuralWorldNode("later","edit",StructuralCase(
                "later","No unprovenanced source additions",
                add_sources=(NamedSource("field:late","Forbidden late source",
                    UniformElectricField(EA)),))),
        )))
    return out


def main():
    if len(sys.argv)>=2 and sys.argv[1]=="--legacy":
        need(len(sys.argv)==3,"usage --legacy output.json")
        Path(sys.argv[2]).write_text(json.dumps(legacy_records(),sort_keys=True,
            separators=(",",":"),allow_nan=False),encoding="utf-8")
        print("LEGACY COMPLETE",Path(sys.argv[2]),"import",__import__("conductor_sim").__file__)
        return
    need(len(sys.argv)==2,"usage output.json")
    novel=review_novel()
    attack_probes(novel)
    event_boundaries()
    Path(sys.argv[1]).write_text(json.dumps(dict(
        evidence_type="new-separate-context-reviewer-native-tests",
        source_head=SOURCE_HEAD, checks=CHECKS,
    ),indent=2,sort_keys=True,allow_nan=False)+"\n",encoding="utf-8")
    print("R2 Chat B NEW authored probes PASS",len(CHECKS),"categories")
    for name, result in CHECKS.items():
        print(name+":",json.dumps(result,sort_keys=True))
    print("genuine worlds",6,"source_sha",SOURCE_HEAD)


if __name__ == "__main__":
    main()
