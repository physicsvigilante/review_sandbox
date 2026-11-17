"""Chat B reviewer01 M33b probes. NEW oblique-plane/source-history physics and attacks.
Never import developer M33b oracle. Do not modify production.
Invoked on actual pinned GitHub checkout, Python 3.12 CI.
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from dataclasses import replace
from pathlib import Path

import conductor_sim as cs
from conductor_sim.motion_events import EventPolicy, PlaneEvent
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.structural_family import StructuralCase
from conductor_sim.structural_scenarios import NamedSource

Q = 3.2e-9
M = 2e-6
P = (.004, -.002, .001)
V = (.25, -.1875, 0.)
G = (.16, -.12, .08)
E0 = (320., -240., 160.)
EA = (80., -60., 110.)
EB = (-200., 150., -500.)
EBRAKE = (-1200., 900., -600.)
N = (.6, .8, 0.)
REV_P = (.10, -.04, .02)
REV_V = (-.25, .1875, 0.)
PIN = "1c632fe347d4f0b4a41fe421d4cdb5ac0985075f"
TREE = "2ce33c744440248b4491c38f4ccb673636c08035"
MARK = []
RESULT = {"reviewer": "Chat B, separate context, authored oblique 3D SI equations",
          "source_head": PIN, "source_tree": TREE, "cases": {}, "attacks": []}


def note(label):
    MARK.append(label)
    print("PASS", label, flush=True)


def near(actual, expected, tol, context):
    if not math.isfinite(actual) or abs(actual - expected) > tol:
        raise AssertionError(f"{context}: actual={actual!r} expected={expected!r} tol={tol}")


def vec(actual, expected, tol, context):
    if len(actual) != 3:
        raise AssertionError(context + ": vector dimension")
    for axis in range(3):
        near(actual[axis], expected[axis], tol, f"{context} axis {axis}")


def must_reject(label, thunk):
    try:
        thunk()
    except (ValueError, TypeError):
        RESULT["attacks"].append(label)
        note("reject: " + label)
    else:
        raise AssertionError(f"FORGED INPUT ACCEPTED: {label}")


def plus(x, y):
    return tuple(x[k] + y[k] for k in range(3))


def graph(short=False, version=3):
    baseline = PrescribedScenario(
        "chatb:oblique-root",
        cs.TestChargeMotionSpec(
            cs.PrescribedField((cs.UniformElectricField(E0),)),
            cs.PointCharge(Q, P), M, V, .65, .025,
            plane_normal=N, gravity=cs.UniformGravity(G)),
        (("field:main", "Original stationary oblique electric field"),),
        "Reviewer new oblique 3-component planar qE + mg initial-value case.")
    nodes = [
        cs.StructuralWorldNode("alpha", "baseline", StructuralCase(
            "alpha", "Independently add held oblique electric A",
            add_sources=(NamedSource("field:fork", "A independently held field",
                                       cs.UniformElectricField(EA)),))),
        cs.StructuralWorldNode("beta", "baseline", StructuralCase(
            "beta", "Independently add held oblique electric B under SAME branch-local ID",
            add_sources=(NamedSource("field:fork", "B independently held field",
                                       cs.UniformElectricField(EB)),))),
        cs.PhysicalWorldNode("mass", "alpha", "Genuine physical mass revision",
            (cs.CoupledPropertyEdit("test-particle", "mass_kg", 2.8e-6),)),
    ]
    if not short:
        nodes += [
            cs.StructuralWorldNode("retire", "mass", StructuralCase(
                "retire", "Remove held fork source after real physical edit",
                remove_sources=("field:fork",))),
            cs.StructuralWorldNode("resurrect", "retire", StructuralCase(
                "resurrect", "Illegally reuse retired source ID",
                add_sources=(NamedSource("field:fork", "Unlawful revived source",
                    cs.UniformElectricField(EA)),))),
            cs.PhysicalWorldNode("invalid", "baseline", "Negative mass must refuse",
                (cs.CoupledPropertyEdit("test-particle", "mass_kg", -1.),)),
            cs.StructuralWorldNode("retard", "baseline", StructuralCase(
                "retard", "Retarding held source yielding two roots in one detector",
                add_sources=(NamedSource("field:brake", "Independent reversing field",
                    cs.UniformElectricField(EBRAKE)),))),
            cs.PhysicalWorldNode("opposite", "baseline", "New physical launch state",
                (cs.CoupledPropertyEdit("test-particle", "position_m", REV_P),
                 cs.CoupledPropertyEdit("test-particle", "initial_velocity_m_s", REV_V))),
        ]
    return cs.run_unified_observation_graph(cs.UnifiedObservationPlan(
        f"chatb:graph-{version}-{'short' if short else 'full'}",
        baseline, tuple(nodes),
        retain_source_ancestry=(version >= 2),
        comparisons=((cs.WorldComparison("old-siblings", "alpha", "beta"),)
                     if version == 3 else ())))


def expected_model(world):
    E = {
        "baseline": E0,
        "alpha": plus(E0, EA),
        "beta": plus(E0, EB),
        "mass": plus(E0, EA),
        "retard": plus(E0, EBRAKE),
        "opposite": E0,
    }[world]
    m = 2.8e-6 if world == "mass" else M
    p, v = (REV_P, REV_V) if world == "opposite" else (P, V)
    a = tuple(Q * E[k] / m + G[k] for k in range(3))
    f = tuple(Q * E[k] + m * G[k] for k in range(3))
    return p, v, E, a, f


def state(world, t):
    p, v, _, a, _ = expected_model(world)
    return (tuple(p[k] + v[k] * t + .5 * a[k] * t*t for k in range(3)),
            tuple(v[k] + a[k]*t for k in range(3)))


def independent_root(world, target):
    p, v, _, a, _ = expected_model(world)
    normal = (2., -1., 0.)
    x = sum(normal[k]*p[k] for k in range(3))
    speed = sum(normal[k]*v[k] for k in range(3))
    accel = sum(normal[k]*a[k] for k in range(3))
    d = target - x
    discriminant = speed**2 + 2*accel*d
    if discriminant < 0:
        return None
    if speed > 0:
        return 2*d/(speed + math.sqrt(discriminant))
    return (-speed + math.sqrt(discriminant))/accel


def policy():
    return EventPolicy(.012, 1e-8, 1e-8, 1e-6)


def detector(event_id, loc=.19, direction=1, terminal=False):
    # In detector plane, point=(x,y,z) with x+2y-z=0 and 2x-y=loc.
    x = loc / 2.5
    y = -loc / 5.
    z = x + 2*y
    return PlaneEvent(event_id, (x,y,z), (2.,-1.,0.),
                      "Reviewer new signed nonaxial detector", direction=direction,
                      terminal=terminal)


def check_native(g, run, target, worlds):
    byid = {"baseline": g.plan.original}
    byid.update((e.node.node_id, e.scenario) for e in g.entries)
    out = {}
    for entry in run.entries:
        world = entry.world_id
        if world not in worlds:
            continue
        assert entry.status == "complete", (world, entry.status, entry.reason)
        assert entry.scenario is byid[world]
        assert entry.native.study.scenario is byid[world]
        assert entry.native.study.policy is run.plan.policy
        assert entry.native.study.questions == run.plan.questions
        assert entry.native.trajectory.termination == "duration"
        p, v, field, acc, force = expected_model(world)
        assert all(abs(sum(N[k] * obj[k] for k in range(3))) < 1e-12
                   for obj in (v, field, acc, G))
        assert entry.native.trajectory.samples[0].time_s == 0.0
        samples = [*entry.native.trajectory.samples, *(e.sample for e in entry.native.events)]
        for sample in samples:
            t = sample.time_s
            pos, vel = state(world, t)
            vec(sample.position_m, pos, 7e-8, f"{world}/position t={t}")
            vec(sample.velocity_m_s, vel, 7e-8, f"{world}/velocity t={t}")
            vec(sample.force_n, force, 1e-12, f"{world}/force t={t}")
            vec(sample.acceleration_m_s2, acc, 3e-10, f"{world}/accel t={t}")
            vec(sample.electric_field_v_m, field, 2e-9, f"{world}/E t={t}")
        root = independent_root(world, target)
        actual = [e for e in entry.native.events if e.event_id == run.plan.questions[0].event_id]
        assert len(actual) == 1 and actual[0].direction == 1, (world, actual)
        near(actual[0].sample.time_s, root, 2e-7, world+"/analytic root")
        assert actual[0].time_bracket_s[0] <= actual[0].sample.time_s <= actual[0].time_bracket_s[1]
        out[world] = {"sample_count": len(entry.native.trajectory.samples),
                      "root_numeric_s": actual[0].sample.time_s,
                      "root_analytic_s": root, "revision": entry.scenario.revision_id,
                      "force_n": force}
    return out


def check_pair(record, left, right, target):
    assert record["left_world_id"] == left and record["right_world_id"] == right
    assert record["status"] == "compared"
    assert record["numerical_orientation"] == "right minus left"
    rows = record["exact_time_trajectory_comparisons"]
    assert len(rows) > 5
    for row in rows:
        t = row["time_s"]
        pl, vl = state(left, t)
        pr, vr = state(right, t)
        dp = tuple(pr[k]-pl[k] for k in range(3))
        dv = tuple(vr[k]-vl[k] for k in range(3))
        vec(row["delta_position_m"], dp, 1e-7, f"delta-position {left}/{right}")
        vec(row["delta_velocity_m_s"], dv, 1e-7, f"delta-velocity {left}/{right}")
        near(row["position_distance_m"], math.dist(pl,pr), 1e-7, "position norm")
        near(row["velocity_distance_m_s"], math.dist(vl,vr), 1e-7, "velocity norm")
    pair=record["event_time_comparisons"][0]
    assert pair["status"] == "one-resolved-pair", pair
    exact=independent_root(right,target)-independent_root(left,target)
    near(pair["estimated_numerical_shift_s"],exact,2e-7,"independent signed shift")
    lo,hi=pair["numerical_bracket_shift_interval_s"]
    assert lo <= pair["estimated_numerical_shift_s"] <= hi
    return {"shared_samples":len(rows),"analytic_shift_s":exact,
            "observed_shift_s":pair["estimated_numerical_shift_s"]}


def new_science_and_two_studies():
    g=graph()
    old=g.as_dict()
    status={e.node.node_id:e.status for e in g.entries}
    assert status["alpha"] == status["beta"] == status["mass"] == "complete", [(e.node.node_id,e.status,e.reason) for e in g.entries]
    assert status["retire"] == status["retard"] == status["opposite"] == "complete"
    assert status["resurrect"] == "rejected-structural-model", status
    assert status["invalid"] in ("rejected-physical-model","rejected-physical-edit"), status
    assert g.entries[0].source_ancestry.active_source_ids == g.entries[1].source_ancestry.active_source_ids
    assert g.entries[0].scenario.spec.field.sources != g.entries[1].scenario.spec.field.sources
    assert "field:fork" in g.entries[3].source_ancestry.retired_source_ids
    source_digest=hashlib.sha256(json.dumps(old,sort_keys=True,separators=(",",":"),
                                          allow_nan=False,ensure_ascii=True).encode("ascii")).hexdigest()
    p1=cs.GraphEventInquiryPlan(
        g,"chatb:novel-one",("baseline","alpha","beta","mass","resurrect","invalid"),
        (detector("cut:one",.19),),policy(),
        (cs.WorldComparison("sibling","alpha","beta"),
         cs.WorldComparison("cousin","beta","mass"),
         cs.WorldComparison("refused","invalid","alpha")))
    # A fresh independent M24a integration cannot reassemble/physically edit the source.
    from unittest.mock import patch
    with patch("conductor_sim.unified_observation_graph.reassemble_scenario",
               side_effect=AssertionError("M33b tried to reassemble a held source")), \
         patch("conductor_sim.unified_observation_graph.revise_scenario",
               side_effect=AssertionError("M33b tried to revise a physical source")):
        first=cs.run_graph_event_inquiry(p1)
    one=first.as_dict()
    assert one["schema"] == "conductor_sim.graph_event_inquiry.v1"
    assert one["plan"]["source_graph_schema"] == "conductor_sim.unified_observation_graph.v3"
    assert one["plan"]["source_graph_sha256"] == source_digest
    assert [e.status for e in first.entries[4:]] == ["skipped-parent-model"]*2
    assert first.entries[4].native is first.entries[5].native is None
    assert one["cross_world_comparisons"][2]["status"] == "unpaired"
    expected=check_native(g,first,.19,("baseline","alpha","beta","mass"))
    pairs={}
    for row in one["cross_world_comparisons"][:2]:
        pairs[row["comparison_id"]]=check_pair(row,row["left_world_id"],
                                               row["right_world_id"],.19)
    assert g.as_dict()==old
    note("new 3-component oblique native physics / siblings / genuine mass grandchild")
    note("independent SI positions velocities E qE+mg forces roots and pair deltas")
    note("physical refusals / branch-local reused and retired source identity")
    note("source graph canonical SHA and no reassembly under instrumented mock")
    # second questions: a physically distinct detector, still same native original world objects
    p2=cs.GraphEventInquiryPlan(
        g,"chatb:novel-two",("baseline","alpha","beta","mass"),
        (detector("cut:two",.315),),policy(),
        (cs.WorldComparison("fresh-cousin","alpha","mass"),))
    second=cs.run_graph_event_inquiry(p2)
    two=second.as_dict()
    other=check_native(g,second,.315,("baseline","alpha","beta","mass"))
    check_pair(two["cross_world_comparisons"][0],"alpha","mass",.315)
    for a,b in zip(first.entries[:4],second.entries):
        assert a.scenario is b.scenario
        assert a.native is not b.native
        assert a.native.study is not b.native.study
        assert a.native.study.questions != b.native.study.questions
        assert a.native.study.policy is p1.policy
        assert b.native.study.policy is p2.policy
    assert first.as_dict()==one and g.as_dict()==old
    note("two genuinely different fresh native M24a questions on exact SAME source model objects")
    RESULT["cases"]["oblique3D"]={"source_sha256":source_digest,
                                  "source_graph_schema":old["schema"],
                                  "status":status,"question_one":expected,
                                  "question_two":other, "pairs":pairs}
    return g, first, second


def refusal_and_signed_boundaries(g):
    # Exact unit normal z: Vz == 0 exactly, baseline acceleration z>0,
    # beta acceleration z<0. Both are physically qualified original models.
    stop=PlaneEvent("stop:initial",P,(0.,0.,1.),
                    "Qualified initial ideal boundary",direction=1,
                    terminal=True,role="ideal-stop-surface")
    run=cs.run_graph_event_inquiry(cs.GraphEventInquiryPlan(
        g,"chatb:stop",("baseline","beta"),(stop,),policy(),
        (cs.WorldComparison("stopdiff","baseline","beta"),)))
    assert run.entries[0].status=="rejected-event-study"
    assert run.entries[0].native is None and run.entries[0].scenario is g.plan.original
    assert run.entries[1].status=="complete" and run.entries[1].native is not None, [(e.status,e.reason) for e in run.entries]
    assert run.as_dict()["cross_world_comparisons"][0]["status"]=="unpaired"
    note("real ideal initial stop refusal on accepted baseline vs accepted beta")

    two=cs.run_graph_event_inquiry(cs.GraphEventInquiryPlan(
        g,"chatb:two",("baseline","retard"),
        (detector("two:bidirectional",.055,direction=0),),policy(),
        (cs.WorldComparison("two-pair","baseline","retard"),)))
    base_events=two.entries[0].native.events
    reversals=two.entries[1].native.events
    assert len(base_events)==1 and base_events[0].direction==1
    assert len(reversals)==2 and sorted(e.direction for e in reversals)==[-1,1],reversals
    item=two.as_dict()["cross_world_comparisons"][0]["event_time_comparisons"][0]
    assert item["status"]=="unpaired" and "multiple" in item["reason"],item
    assert "estimated_numerical_shift_s" not in item
    note("genuine new quadratic turnaround: 2 opposite signed M24a roots unpaired")

    opposite=cs.run_graph_event_inquiry(cs.GraphEventInquiryPlan(
        g,"chatb:opposite",("baseline","opposite"),
        (detector("directions:opposed",.19,direction=0),),policy(),
        (cs.WorldComparison("opp-pair","baseline","opposite"),)))
    assert all(e.status=="complete" for e in opposite.entries)
    assert [e.direction for e in opposite.entries[0].native.events]==[1]
    assert [e.direction for e in opposite.entries[1].native.events]==[-1]
    outcome=opposite.as_dict()["cross_world_comparisons"][0]["event_time_comparisons"][0]
    assert outcome["status"]=="unpaired" and "opposite" in outcome["reason"],outcome
    note("complete-duration unique opposite signed roots remain distinct")

    terminal=cs.run_graph_event_inquiry(cs.GraphEventInquiryPlan(
        g,"chatb:terminal",("baseline","retard"),
        (detector("stop:terminal",.055,direction=1,terminal=True),),policy(),
        (cs.WorldComparison("terminalpair","baseline","retard"),)))
    assert [e.status for e in terminal.entries]==["terminal-event"]*2
    item=terminal.as_dict()["cross_world_comparisons"][0]["event_time_comparisons"][0]
    assert item["status"]=="unpaired" and "censored" in item["reason"]
    note("native terminal crossing cannot claim complete-history pairing")

    from examples.m29b_structural_events import make_plan
    legacy=make_plan("guard-detector")
    case=next(c for c in legacy.family.cases if c.case_id=="attract-guard")
    source=cs.run_unified_observation_graph(cs.UnifiedObservationPlan(
        "chatb:guard-graph",legacy.family.baseline,
        (cs.StructuralWorldNode("attract-guard","baseline",case),),
        retain_source_ancestry=True))
    guard=cs.run_graph_event_inquiry(cs.GraphEventInquiryPlan(
        source,"chatb:guard-new",("baseline","attract-guard"),
        (PlaneEvent("new:early",(.04,0.,0.),(1.,0.,0.),
                    "Independent early passive detector",direction=1),
         PlaneEvent("new:late",(.24,0.,0.),(1.,0.,0.),
                    "Independent beyond guard detector",direction=1)),
        legacy.policy,(cs.WorldComparison("guardpair","baseline","attract-guard"),)))
    assert guard.entries[1].status=="censored-source-guard"
    outcomes=guard.entries[1].native.as_dict()["outcomes"]
    assert outcomes["new:early"]=="located",outcomes
    assert outcomes["new:late"]=="search-truncated",outcomes
    pair=guard.as_dict()["cross_world_comparisons"][0]
    assert all(e["status"]=="unpaired" for e in pair["event_time_comparisons"])
    last=guard.entries[1].native.trajectory.samples[-1].time_s
    assert all(row["time_s"]<=last for row in pair["exact_time_trajectory_comparisons"])
    note("new actual source guard: earlier root located, later time UNKNOWN, no extrapolation")

    # Old refused event study does not poison a physically valid source model.
    oldplan=make_plan("terminal-refusal")
    old=cs.run_unified_observation_graph(cs.UnifiedObservationPlan(
        "chatb:prior-study",oldplan.family.baseline,
        (cs.StructuralWorldNode("reversed-force","baseline",oldplan.family.cases[0],
                                "events"),),"events",oldplan.questions,
        oldplan.policy,retain_source_ancestry=True))
    assert old.entries[0].status=="rejected-event-study" and old.entries[0].scenario is not None
    new=cs.run_graph_event_inquiry(cs.GraphEventInquiryPlan(
        old,"chatb:post-refusal",("baseline","reversed-force"),
        (PlaneEvent("fresh:passive",(.003,0.,0.),(1.,0.,0.),
                    "Now legitimate passive measurement",direction=1),),
        oldplan.policy))
    assert new.entries[1].status=="complete"
    assert new.entries[1].native.as_dict()["outcomes"]["fresh:passive"]=="located"
    assert new.entries[1].original_graph_observation_status=="rejected-event-study"
    note("previously refused observation permits a completely different fresh valid study")
    RESULT["cases"]["boundaries"]={
        "initial_stop":[e.status for e in run.entries],
        "turnaround_events":[len(e.native.events) for e in two.entries],
        "opposite_signed":[[e.direction for e in w.native.events] for w in opposite.entries],
        "terminal":[e.status for e in terminal.entries],
        "source_guard":outcomes,"prior_refused_new_success":new.entries[1].status}


def hostile(g, run):
    from copy import deepcopy
    p=run.plan
    must_reject("unknown selected world",
        lambda: replace(p,world_ids=("baseline","ghost")))
    must_reject("duplicate unordered reversal pair",
        lambda: replace(p,comparisons=(cs.WorldComparison("a","alpha","beta"),
              cs.WorldComparison("b","beta","alpha"))))
    must_reject("world selection order changed in issued run",
        lambda: replace(run,plan=replace(p,world_ids=("alpha","baseline","beta","mass",
                                                      "resurrect","invalid"))))
    must_reject("wrong original inquiry questions",
        lambda: replace(run,plan=replace(p,questions=(detector("forged",.24),))))
    must_reject("forged event policy",
        lambda: replace(run,plan=replace(p,policy=EventPolicy(.014,1e-8,1e-8,1e-6))))
    must_reject("forged pair direction",
        lambda: replace(run,plan=replace(p,comparisons=(
            cs.WorldComparison("sibling","beta","alpha"),)+p.comparisons[1:])))
    must_reject("forged model/new event status",
        lambda: replace(run,entries=(replace(run.entries[0],status="terminal-event"),)+run.entries[1:]))
    must_reject("forged reason/label",
        lambda: replace(run,entries=(replace(run.entries[0],reason="invented refused"),)+run.entries[1:]))
    root=run.entries[0].native.events[0]
    shifted=replace(root,
                    sample=replace(root.sample,time_s=root.sample.time_s+.03),
                    time_bracket_s=tuple(t+.03 for t in root.time_bracket_s))
    badnative=replace(run.entries[0].native,events=(shifted,))
    must_reject("root/bracket time +0.03 s",
        lambda: replace(run,entries=(replace(run.entries[0],native=badnative),)+run.entries[1:]))
    s0=run.entries[0].native.trajectory.samples[0]
    assert s0.time_s == 0.
    evil=replace(s0,time_s=False)
    tr=replace(run.entries[0].native.trajectory,
               samples=(evil,)+run.entries[0].native.trajectory.samples[1:])
    modified=replace(run.entries[0].native,trajectory=tr)
    must_reject("Boolean zero clock false-equals-zero attack",
        lambda: replace(run,entries=(replace(run.entries[0],native=modified),)+run.entries[1:]))
    tr=replace(run.entries[0].native.trajectory,termination="terminal-event")
    modified=replace(run.entries[0].native,trajectory=tr)
    must_reject("fabricated event terminal",
        lambda: replace(run,entries=(replace(run.entries[0],native=modified),)+run.entries[1:]))
    payload=run.as_dict()
    tamper=deepcopy(payload)
    tamper["nodes"][0]["native_event_run"]["events"][0]["sample"]["time_s"] += .03
    tamper["nodes"][1]["source_inventory"][0]["label"]="forged native source"
    tamper["cross_world_comparisons"][0]["status"]="invented"
    assert run.as_dict()==payload
    note("detached JSON alterations do not rewrite native measurements")
    attack=replace(run.entries[0],reason="tampered via object setattr")
    object.__setattr__(run,"entries",(attack,)+run.entries[1:])
    must_reject("public in-place object.__setattr__ before export",run.as_dict)
    fresh_g=graph()
    fresh_p=cs.GraphEventInquiryPlan(fresh_g,"chatb:graphattack",("baseline","alpha"),
                                     (detector("attack:graph",.19),),policy())
    fresh_run=cs.run_graph_event_inquiry(fresh_p)
    object.__setattr__(fresh_g,"baseline_status","fabricated")
    must_reject("original graph result status forged",fresh_run.as_dict)
    fresh_g2=graph()
    fresh_p2=cs.GraphEventInquiryPlan(fresh_g2,"chatb:sourceattack",("baseline","alpha"),
                                      (detector("attack:source",.19),),policy())
    fresh_run2=cs.run_graph_event_inquiry(fresh_p2)
    object.__setattr__(fresh_g2.plan.original,"source_annotations",
                       (("field:main","forged source name"),))
    must_reject("source name/model revision changed after issued inquiry",fresh_run2.as_dict)
    note("hostile native evidence and receipt checks")


def legacy(path):
    old={}
    for version in (1,2,3):
        native=graph(short=True,version=version)
        record=native.as_dict()
        assert record["schema"] == f"conductor_sim.unified_observation_graph.v{version}"
        old[f"v{version}"]=record
    Path(path).write_text(json.dumps(old,sort_keys=True,allow_nan=False,
                                     separators=(",",":"),ensure_ascii=True)+"\n",
                          encoding="utf-8")
    note("legacy genuine source graph v1/v2/v3 exported byte-stably")


def full(path):
    g,first,second=new_science_and_two_studies()
    refusal_and_signed_boundaries(g)
    hostile(g,first)
    RESULT["passed_checks"] = len(MARK)
    RESULT["check_names"] = MARK
    Path(path).write_text(json.dumps(RESULT,sort_keys=True,indent=2,allow_nan=False)+"\n",
                          encoding="utf-8")
    print(f"Chat B native/3D/refusal/hostile: {len(MARK)} independent checks PASS")


if __name__=="__main__":
    if len(sys.argv)!=3 or sys.argv[1] not in ("--legacy","--full"):
        raise SystemExit("usage: reviewer.py --legacy|--full output.json")
    if sys.argv[1]=="--legacy":
        legacy(sys.argv[2])
    else:
        full(sys.argv[2])
