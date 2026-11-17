"""Independent Chat B M34b R2 science/hostile probes; NOT a developer fixture.

Run only at pinned source SHA/tree in review_sandbox GitHub Actions.
Novel oblique normal (2,-1,3), E, q, gravity, launch and source hypotheses.
Original history and first-attempt CI logs must be retained unchanged.
"""
from __future__ import annotations

import argparse
from dataclasses import replace
from hashlib import sha256
from math import sqrt
from pathlib import Path
import json
from unittest import mock

from conductor_sim import (
    CoupledPropertyEdit, PhysicalWorldNode, PointCharge, PrescribedField,
    StructuralWorldNode, TestChargeMotionSpec, UniformElectricField,
    UniformGravity, UnifiedObservationPlan, WorldComparison,
    run_unified_observation_graph,
)
from conductor_sim.motion_events import EventPolicy, PlaneEvent
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.structural_family import StructuralCase
from conductor_sim.structural_scenarios import NamedSource, SourceReplacement

QUESTIONS = (PlaneEvent("review:x", (.16, 0., 0.), (1., 0., 0.),
                        "New reviewer authored positive x detector", direction=1),)
POLICY = EventPolicy(.025, 1e-9, 1e-9, 1e-7)
FAILURES = []


def plain(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False).encode("utf-8")


def digest(value):
    return sha256(plain(value)).hexdigest()


def must_fail(label, thunk):
    try:
        thunk()
    except (TypeError, ValueError, RuntimeError, AttributeError) as exc:
        FAILURES.append(dict(probe=label, outcome="properly-rejected",
                             exception=type(exc).__name__, message=str(exc)[:180]))
        return
    raise AssertionError("hostile probe was improperly accepted: " + label)


def original_model():
    # Plane n=(2,-1,3). Each physical 3-vector is in the plane, unlike a
    # dyadic x/y/z test plane, and n becomes genuinely non-dyadic when normalized.
    return PrescribedScenario(
        "review01:oblique-original",
        TestChargeMotionSpec(
            PrescribedField((UniformElectricField((450.,720.,-60.)),)),
            PointCharge(2e-9, (.016,.020,-.004)),
            4e-6, (.11,.16,-.02), 1.2, .06,
            plane_normal=(2.,-1.,3.),
            gravity=UniformGravity((.115,.20,-.01)),
        ),
        (("field:base", "Reviewer original 3D-vector held field"),),
        "Reviewer-generated unknown non-dyadic oblique-plane SI Newtonian problem.")


def graph_nodes():
    # Same source ID on independent old sibling hypotheses: distinct E values.
    return (
        StructuralWorldNode("old-west", "baseline", StructuralCase(
            "old-west", "Old A introduces a genuinely held in-plane field",
            add_sources=(NamedSource("field:shared", "West new E",
                                   UniformElectricField((120.,240.,0.))),)),
            "events"),
        StructuralWorldNode("old-east", "baseline", StructuralCase(
            "old-east", "Old B introduces the same ID with different physics",
            add_sources=(NamedSource("field:shared", "East alternate E",
                                   UniformElectricField((210.,0.,-140.))),)),
            "events"),
        PhysicalWorldNode("old-heavy", "old-west",
            "Real parent mass edit before later newly forked structure",
            (CoupledPropertyEdit("test-particle","mass_kg",5e-6),), "events"),
    )


def old_graph(variant="v2"):
    if variant == "v1":
        retain, comparisons = False, ()
    elif variant == "v2":
        retain, comparisons = True, ()
    elif variant == "v3":
        retain, comparisons = True, (
            WorldComparison("legacy-old-pair", "old-west", "old-east"),)
    else:
        raise ValueError("bad variant")
    return run_unified_observation_graph(UnifiedObservationPlan(
        "review01:old-graph", original_model(), graph_nodes(),
        "events", QUESTIONS, POLICY, retain_source_ancestry=retain,
        comparisons=comparisons))


def new_fork_plan(graph):
    from conductor_sim import GraphWorldForkPlan
    nodes = (
        StructuralWorldNode("add", "old-heavy", StructuralCase(
            "add", "Add entirely new reviewer in-plane held field",
            add_sources=(NamedSource("field:fork", "New fork source",
                                   UniformElectricField((90.,180.,0.))),)), "events"),
        PhysicalWorldNode("recharge", "add", "Atomic true physical charge edit",
            (CoupledPropertyEdit("test-particle","charge_c",3e-9),), "events"),
        StructuralWorldNode("replace", "recharge", StructuralCase(
            "replace", "Retire fork source after the M20b physical edit",
            replace_sources=(SourceReplacement(
                "field:fork", NamedSource("field:replacement", "Final held source",
                                           UniformElectricField((120.,0.,-80.)))),)),
            "events"),
        StructuralWorldNode("revive", "replace", StructuralCase(
            "revive", "Attempt forbidden retired-ID resurrection",
            add_sources=(NamedSource("field:fork", "Illegal historical identity",
                                   UniformElectricField((50.,100.,0.))),)), "events"),
        StructuralWorldNode("sibling", "old-east", StructuralCase(
            "sibling", "Independent sibling can legitimately reuse fork source ID",
            add_sources=(NamedSource("field:fork", "Independent distinct fork source",
                                   UniformElectricField((150.,300.,0.))),)), "events"),
    )
    return GraphWorldForkPlan(
        graph, "review01:fork", nodes, QUESTIONS, POLICY,
        comparisons=(
            WorldComparison("west-to-add","old-heavy","add"),
            WorldComparison("new-to-new","add","recharge"),
            WorldComparison("independent-siblings","replace","sibling"),
            WorldComparison("refused-comparison","revive","sibling"),
        ))


def independent_state(spec, t):
    # No engine force callback, trajectory evaluator, root locator, test fixture
    # or developer-provided numeric oracle is imported or called here.
    E = tuple(sum(source.field_v_m[i] for source in spec.field.sources)
              for i in range(3))
    g = ((0.,0.,0.) if spec.gravity is None
         else spec.gravity.acceleration_m_s2)
    mass = spec.mass_kg
    q = spec.particle.charge_c
    a = tuple((q * E[i] + mass * g[i]) / mass for i in range(3))
    p = tuple(spec.particle.position_m[i] +
              t * spec.initial_velocity_m_s[i] + (t*t/2)*a[i]
              for i in range(3))
    v = tuple(spec.initial_velocity_m_s[i] + t * a[i] for i in range(3))
    force = tuple(q * E[i] + mass * g[i] for i in range(3))
    return p,v,force,a


def independent_root(spec, x=.16):
    _, _, _, accel = independent_state(spec, 0.)
    d = x-spec.particle.position_m[0]
    v0 = spec.initial_velocity_m_s[0]
    discr = v0*v0 + 2*accel[0]*d
    assert d>0 and discr>0 and accel[0]>0
    return (2*d)/(v0+sqrt(discr))


def validate_native(worlds):
    max_p=max_v=max_f=max_event_t=max_plane=0.
    n_samples=0
    roots={}
    for name, (model,native) in worlds.items():
        assert model is not None and native is not None, (name,model,native)
        assert native.trajectory.termination == "duration", name
        spec=model.spec
        n=spec.plane_normal
        assert len(n)==3 and all(abs(x)>0.1 for x in n), (name,n)
        ex=tuple(sum(src.field_v_m[i] for src in spec.field.sources)
                 for i in range(3))
        for vec in [ex,spec.particle.position_m,spec.initial_velocity_m_s,
                    spec.gravity.acceleration_m_s2]:
            dot=sum(n[i]*vec[i] for i in range(3))
            max_plane=max(max_plane,abs(dot))
            assert abs(dot)<1e-9, (name,vec,dot,n)
        expected=independent_root(spec)
        located=[e for e in native.events if e.event_id=="review:x"]
        assert len(located)==1, (name,len(located),native.as_dict()["outcomes"])
        assert located[0].direction==1 and located[0].terminal is False
        assert located[0].time_bracket_s[0] <= located[0].sample.time_s <= located[0].time_bracket_s[1]
        dt=abs(located[0].sample.time_s-expected)
        max_event_t=max(max_event_t,dt)
        assert dt<3e-6, (name,expected,located[0].sample.time_s,dt)
        roots[name]=dict(native_s=located[0].sample.time_s,
                         analytic_s=expected, error_s=dt)
        for sample in native.trajectory.samples:
            p,v,f,_=independent_state(spec,sample.time_s)
            for i in range(3):
                max_p=max(max_p,abs(sample.position_m[i]-p[i]))
                max_v=max(max_v,abs(sample.velocity_m_s[i]-v[i]))
                max_f=max(max_f,abs(sample.force_n[i]-f[i]))
            n_samples+=1
    assert max_p<1e-7 and max_v<1e-7 and max_f<2e-11
    return dict(native_worlds=len(worlds), actual_samples=n_samples,
                max_position_error_m=max_p, max_velocity_error_m_s=max_v,
                max_force_error_n=max_f, max_root_error_s=max_event_t,
                max_offplane_dot=max_plane, detector_roots=roots)


def pair_check(graph,fork):
    worlds={"baseline":(graph.plan.original,graph.baseline_native)}
    worlds.update((e.node.node_id,(e.scenario,e.native)) for e in graph.entries)
    worlds.update((e.node.node_id,(e.scenario,e.native)) for e in fork.entries
                  if e.scenario is not None)
    records=fork.as_dict()["cross_world_comparisons"]
    assert [r["status"] for r in records] == [
        "compared","compared","compared","unpaired"]
    n_pairs=n_rows=0
    for row in records[:3]:
        left,right=row["left_world_id"],row["right_world_id"]
        left_model,left_native=worlds[left]
        right_model,right_native=worlds[right]
        assert row["numerical_orientation"]=="right minus left"
        assert row["event_study_compatible"] is True
        ltimes={s.time_s for s in left_native.trajectory.samples}
        rtimes={s.time_s for s in right_native.trajectory.samples}
        expected_times=sorted(ltimes & rtimes)
        samples=row["exact_time_trajectory_comparisons"]
        assert [s["time_s"] for s in samples]==expected_times
        for sample in samples:
            t=sample["time_s"]
            lp,lv,_,_=independent_state(left_model.spec,t)
            rp,rv,_,_=independent_state(right_model.spec,t)
            assert max(abs(sample["delta_position_m"][j]-(rp[j]-lp[j]))
                       for j in range(3)) < 1e-7
            assert max(abs(sample["delta_velocity_m_s"][j]-(rv[j]-lv[j]))
                       for j in range(3)) < 1e-7
            n_rows+=1
        erow=row["event_time_comparisons"][0]
        assert erow["status"]=="one-resolved-pair",erow
        exact_shift=(independent_root(right_model.spec)-
                     independent_root(left_model.spec))
        assert abs(erow["estimated_numerical_shift_s"]-exact_shift)<3e-6
        n_pairs+=1
    assert records[3]["event_time_comparisons"][0]["status"]=="unpaired"
    return dict(native_pairs=n_pairs, literal_saved_time_rows=n_rows,
                statuses=[r["status"] for r in records])


def hostile(graph,plan,run):
    from conductor_sim import GraphWorldForkPlan, run_graph_world_fork
    from conductor_sim.graph_world_fork import GraphWorldForkRun
    a=plan.nodes[0]
    must_fail("JSON is not native graph",
              lambda: GraphWorldForkPlan({"schema":"fake"},"review01:bad",(a,)))
    must_fail("nodes list not immutable tuple",
              lambda: GraphWorldForkPlan(graph,"review01:list",[a]))
    must_fail("duplicate new node",
              lambda: GraphWorldForkPlan(graph,"review01:dup",(a,a)))
    must_fail("old node ID reused",
              lambda: GraphWorldForkPlan(graph,"review01:oldid",(
                  replace(a,node_id="old-west",
                          case=replace(a.case,case_id="old-west")),)))
    must_fail("forward parent",
              lambda: GraphWorldForkPlan(graph,"review01:forward",(
                  replace(a,parent_id="unknown"),)))
    must_fail("old old comparison",
              lambda: GraphWorldForkPlan(graph,"review01:oldpair",(a,),
                  QUESTIONS,POLICY,
                  comparisons=(WorldComparison("old-only","old-west","old-east"),)))
    must_fail("duplicated unordered reverse pair",
              lambda: GraphWorldForkPlan(graph,"review01:reverse",(a,),
                  QUESTIONS,POLICY,
                  comparisons=(WorldComparison("lr","old-west","add"),
                               WorldComparison("rl","add","old-west"))))
    must_fail("too many new nodes",
              lambda: GraphWorldForkPlan(graph,"review01:six",(a,)*6))
    depth_nodes=tuple(
        PhysicalWorldNode(f"d{i}", "old-heavy" if i==1 else f"d{i-1}",
            "Genuine node to challenge maximum lineage depth",
            (CoupledPropertyEdit("test-particle","mass_kg",6e-6+i*1e-7),))
        for i in range(1,6))
    must_fail("source-root depth exceeds six",
              lambda: GraphWorldForkPlan(graph,"review01:depth",depth_nodes))
    four_edits=(
        CoupledPropertyEdit("test-particle","mass_kg",6e-6),
        CoupledPropertyEdit("test-particle","charge_c",3e-9),
        CoupledPropertyEdit("test-particle","initial_velocity_m_s",(.12,.18,-.02)),
        CoupledPropertyEdit("field:base","field_v_m",(600.,900.,-100.)),
    )
    budget_nodes=tuple(PhysicalWorldNode(
        f"budget{i}","old-west",f"Independent source mass/property budget {i}",
        four_edits) for i in range(4))
    must_fail("thirteen or more physical edits",
              lambda: GraphWorldForkPlan(graph,"review01:budget",budget_nodes))
    must_fail("fabricate alternate runner issue",
              lambda: GraphWorldForkRun(plan,run.entries))
    must_fail("forge new node status",
              lambda: replace(run,entries=(replace(run.entries[0],status="complete-fake"),)
                                      +run.entries[1:]))
    must_fail("forge refused node reason",
              lambda: replace(run,entries=run.entries[:3] + (
                  replace(run.entries[3],reason="fictitious model certificate"),)
                                   +run.entries[4:]))
    must_fail("forge immediate physical parent object",
              lambda: replace(run,entries=(replace(
                  run.entries[0],parent_scenario=graph.plan.original),)
                  +run.entries[1:]))
    root=run.entries[0].native.events[0]
    forged_root=replace(root,
        sample=replace(root.sample,time_s=root.sample.time_s+.03),
        time_bracket_s=tuple(t+.03 for t in root.time_bracket_s))
    forged_event=replace(run.entries[0].native, events=(forged_root,))
    must_fail("forged event root and bracket +0.03s",
              lambda: replace(run,entries=(replace(
                  run.entries[0],native=forged_event),)+run.entries[1:]))
    trajectory=run.entries[0].native.trajectory
    def forged_boolean_time():
        first=replace(trajectory.samples[0],time_s=False)
        fake=replace(trajectory,samples=(first,)+trajectory.samples[1:])
        event=replace(run.entries[0].native,trajectory=fake)
        return replace(run,entries=(replace(
            run.entries[0],native=event),)+run.entries[1:])
    must_fail("boolean False substituted for true zero time",forged_boolean_time)
    exported=run.as_dict()
    exported["source_graph_sha256"]="totally_fake"
    exported["nodes"][0]["status"]="fabricated"
    assert run.as_dict()["source_graph_sha256"]!="totally_fake"
    assert run.as_dict()["nodes"][0]["status"]!="fabricated"
    # Plain object.__setattr__ bypasses frozen dataclass setters, but
    # cannot bypass revalidation on export under the normal API.
    tampered=replace(run.entries[0],reason="deliberate forged provenance")
    object.__setattr__(run,"entries",(tampered,)+run.entries[1:])
    must_fail("object.__setattr__ changes issued result",run.as_dict)
    assert len(FAILURES)>=14


def negative_models(graph):
    from conductor_sim import GraphWorldForkPlan, run_graph_world_fork
    bad=PhysicalWorldNode("bad","old-west","Negative probe mass",
                          (CoupledPropertyEdit("test-particle","mass_kg",-1.),),
                          "trajectory")
    skipped=StructuralWorldNode("skipped","bad",StructuralCase(
        "skipped","No fake children of physically refused parent",
        add_sources=(NamedSource("field:child","Child source",
                  UniformElectricField((30.,60.,0.))),)),"trajectory")
    good=PhysicalWorldNode("good","old-east","Independent valid sibling mass",
        (CoupledPropertyEdit("test-particle","mass_kg",6e-6),),"trajectory")
    badplane=StructuralWorldNode("offplane","old-west",StructuralCase(
        "offplane","Invalid actual out-of-plane field",
        add_sources=(NamedSource("field:illegal","Out of plane electric source",
                    UniformElectricField((0.,0.,180.))),)),"trajectory")
    fork=run_graph_world_fork(GraphWorldForkPlan(
        graph,"review01:refusals",(bad,skipped,good,badplane)))
    statuses=[e.status for e in fork.entries]
    assert statuses==["rejected-physical-model","skipped-parent-model",
                      "complete","rejected-structural-model"],statuses
    assert all(e.scenario is None and e.native is None
               and e.source_ancestry is None for e in [fork.entries[0],
                                                       fork.entries[1],
                                                       fork.entries[3]])
    assert fork.entries[2].native is not None
    return statuses


def old_event_refusal_can_parent():
    from conductor_sim import GraphWorldForkPlan, run_graph_world_fork
    # Physically qualified world, but an author-declared ideal-stop surface
    # is already BEHIND the launch position (x=0.01 < x0=0.016).
    stop=(PlaneEvent("review:invalid-old-stop",(.01,0.,0.),(1.,0.,0.),
          "Old original event study deliberately invalid",direction=1,
          terminal=True,role="ideal-stop-surface"),)
    old=run_unified_observation_graph(UnifiedObservationPlan(
        "review01:old-event-refusal",original_model(),(
            StructuralWorldNode("unobserved","baseline",
                 StructuralCase("unobserved",
                     "Genuinely allowed in-plane field, old event refused",
                     add_sources=(NamedSource("field:extra","Extra valid held",
                     UniformElectricField((45.,90.,0.))),)),"events"),),
        "trajectory",stop,POLICY,retain_source_ancestry=True))
    parent=old.entries[0]
    assert parent.scenario is not None and parent.native is None
    assert parent.status=="rejected-event-study",parent.status
    new=run_graph_world_fork(GraphWorldForkPlan(old,"review01:after-old-refusal",(
        PhysicalWorldNode("genuine-child","unobserved",
            "Qualified physical mass after old refused event observation",
            (CoupledPropertyEdit("test-particle","mass_kg",5.5e-6),),
            "trajectory"),)))
    assert new.entries[0].status=="complete"
    assert new.entries[0].parent_scenario is parent.scenario
    assert new.entries[0].native is not None
    return dict(parent_status=parent.status,child_status=new.entries[0].status)


def cross_event_study_incompatibility(graph):
    from conductor_sim import GraphWorldForkPlan,run_graph_world_fork
    n=(PhysicalWorldNode("new","old-west","True changed mass for event mismatch",
        (CoupledPropertyEdit("test-particle","mass_kg",6.5e-6),),"events"),)
    results=[]
    for forkid,q,policy in [
        ("review01:geometry",(PlaneEvent("review:x",(.20,0.,0.),(1.,0.,0.),
                                       "Same ID, different plane",direction=1),),POLICY),
        ("review01:policy",QUESTIONS,EventPolicy(.021,1e-9,1e-9,1e-7)),
        ("review01:direction",(PlaneEvent("review:x",(.16,0.,0.),(1.,0.,0.),
                                   "Same ID, opposite direction",direction=-1),),POLICY),
        ("review01:terminal",(PlaneEvent("review:x",(.16,0.,0.),(1.,0.,0.),
                                   "Same ID now terminal",direction=1,
                                   terminal=True),),POLICY),
    ]:
        result=run_graph_world_fork(GraphWorldForkPlan(
            graph,forkid,n,q,policy,
            (WorldComparison("cross","old-west","new"),)))
        comparison=result.as_dict()["cross_world_comparisons"][0]
        assert comparison["event_study_compatible"] is False
        assert comparison["exact_time_trajectory_comparisons"]
        assert comparison["event_time_comparisons"][0]["status"]=="unpaired"
        assert "estimated_numerical_shift_s" not in comparison["event_time_comparisons"][0]
        results.append(dict(fork=forkid,status=comparison["status"],
                            event_status=comparison["event_time_comparisons"][0]["status"],
                            saved_rows=len(comparison["exact_time_trajectory_comparisons"])))
    return results


def two_opposite_signed_roots():
    """New analytic two-root parabola, neither developer event-family fixture nor
    a saved-sample interpolation. Both whole-duration worlds have two physical
    crossings in opposite directions: never an admissible unique event shift.
    """
    from conductor_sim import GraphWorldForkPlan,run_graph_world_fork
    base=PrescribedScenario(
        "review01:two-root-baseline",
        TestChargeMotionSpec(
            PrescribedField((UniformElectricField((-1500.,0.,1000.)),)),
            PointCharge(2e-9,(.016,.020,-.004)),
            4e-6,(.6,1.2,0.),2.0,.05,
            plane_normal=(2.,-1.,3.),
            gravity=UniformGravity((.115,.20,-.01))),
        (("field:retarding","New reviewer oblique retarding field"),),
        "Original independently constructed genuine signed-double-root physics.")
    q=(PlaneEvent("review:double",(.16,0.,0.),(1.,0.,0.),
                 "New signed double crossing",direction=0),)
    old=run_unified_observation_graph(UnifiedObservationPlan(
        "review01:two-root-old",base,(
            PhysicalWorldNode("old-decel","baseline",
                "Increase negative deceleration for two x crossings",
                (CoupledPropertyEdit("test-particle","mass_kg",3.5e-6),),
                "events"),),"events",q,POLICY,retain_source_ancestry=True))
    fork=run_graph_world_fork(GraphWorldForkPlan(
        old,"review01:two-root-new",(
            PhysicalWorldNode("new-decel","old-decel",
                "Independently revise deceleration to different double crossing",
                (CoupledPropertyEdit("test-particle","mass_kg",3.9e-6),),
                "events"),),q,POLICY,
        (WorldComparison("double","old-decel","new-decel"),)))
    all_worlds=(("old",old.entries[0]),("new",fork.entries[0]))
    calculated={}
    for name,row in all_worlds:
        native=row.native
        assert native is not None and native.trajectory.termination=="duration"
        ev=sorted((ev for ev in native.events
                   if ev.event_id=="review:double"),key=lambda item:item.sample.time_s)
        assert len(ev)==2,(name,len(ev))
        assert (ev[0].direction,ev[1].direction)==(1,-1),name
        spec=row.scenario.spec
        p0=spec.particle.position_m[0]
        u=spec.initial_velocity_m_s[0]
        ax=independent_state(spec,0)[3][0]
        disc=u*u+2*ax*(.16-p0)
        assert ax<0 and disc>0
        roots=sorted(((-u+sqrt(disc))/ax,(-u-sqrt(disc))/ax))
        assert roots[0]>0 and roots[-1]<spec.duration_s
        for e,t in zip(ev,roots):
            assert abs(e.sample.time_s-t)<3e-6,(name,t,e.sample.time_s)
        calculated[name]=roots
    record=fork.as_dict()["cross_world_comparisons"][0]
    assert record["status"]=="compared"
    assert record["exact_time_trajectory_comparisons"]
    assert record["event_time_comparisons"][0]["status"]=="unpaired"
    assert "estimated_numerical_shift_s" not in record["event_time_comparisons"][0]
    return calculated


def genuine_source_guard_prefix():
    """Reviewer-chosen nearly force-neutral fixed point exactly on a Newtonian
    trajectory: the original Coulomb singularity guard must truncate native
    evidence without inventing late detector crossings.
    """
    from conductor_sim import GraphWorldForkPlan, run_graph_world_fork, FixedPointField
    baseline=original_model()
    strike=independent_state(baseline.spec,.65)[0]
    questions=(
        PlaneEvent("review:early",(.05,0.,0.),(1.,0.,0.),
                   "Reviewer's early actual detector",direction=1),
        PlaneEvent("review:late",(.30,0.,0.),(1.,0.,0.),
                   "Reviewer's late censored detector",direction=1),
    )
    old=run_unified_observation_graph(UnifiedObservationPlan(
        "review01:guard-original",baseline,(
            PhysicalWorldNode("old-mass","baseline",
                "Extra old physically observed world",
                (CoupledPropertyEdit("test-particle","mass_kg",4.1e-6),),
                "events"),),"events",questions,POLICY,
        retain_source_ancestry=True))
    node=StructuralWorldNode("point-guard","baseline",StructuralCase(
        "point-guard",
        "New genuine fixed near-neutral Coulomb point on predicted path",
        add_sources=(NamedSource(
            "source:guard","Weak held singular source requiring honest native guard",
            FixedPointField(1e-30,strike)),)), "events")
    fork=run_graph_world_fork(GraphWorldForkPlan(
        old,"review01:guard-new",(node,),questions,POLICY,
        (WorldComparison("prefix","baseline","point-guard"),)))
    e=fork.entries[0]
    assert e.scenario is not None and e.native is not None
    assert e.status=="censored-source-guard",(e.status,e.reason)
    assert e.native.trajectory.termination=="source-guard"
    outcomes=e.native.as_dict()["outcomes"]
    assert outcomes["review:early"]=="located",outcomes
    assert outcomes["review:late"]=="search-truncated",outcomes
    last=e.native.trajectory.samples[-1].time_s
    assert last<baseline.spec.duration_s
    comparison=fork.as_dict()["cross_world_comparisons"][0]
    assert comparison["status"]=="compared"
    assert comparison["exact_time_trajectory_comparisons"]
    assert all(row["time_s"]<=last for row in comparison["exact_time_trajectory_comparisons"])
    assert all(root["status"]=="unpaired" and
               "estimated_numerical_shift_s" not in root
               for root in comparison["event_time_comparisons"])
    return dict(termination=e.native.trajectory.termination,
                last_saved_s=last,source_position_m=strike,
                outcomes=outcomes,saved_rows=len(comparison["exact_time_trajectory_comparisons"]))


def legacy(out):
    from conductor_sim import GraphEventInquiryPlan,run_graph_event_inquiry
    hashes={}
    out.mkdir(parents=True,exist_ok=True)
    for v in ("v1","v2","v3"):
        graph=old_graph(v)
        data=plain(graph.as_dict())
        (out/(v+".json")).write_bytes(data)
        hashes[v]=sha256(data).hexdigest()
        assert graph.as_dict()["schema"].endswith("."+v)
        if v=="v3":
            q=(PlaneEvent("review:inquiry",(.19,0.,0.),(1.,0.,0.),
                "A distinct later old-model inquiry",direction=1),)
            run=run_graph_event_inquiry(GraphEventInquiryPlan(
                graph,"review01:legacy-inquiry",
                ("baseline","old-west","old-east"),q,POLICY,
                comparisons=(WorldComparison("inquiry-pair","old-west","old-east"),)))
            inquiry=plain(run.as_dict())
            (out/"inquiry.json").write_bytes(inquiry)
            hashes["inquiry"]=sha256(inquiry).hexdigest()
    print("LEGACY_BYTES "+json.dumps(hashes,sort_keys=True))
    return hashes


def full(out):
    from conductor_sim import GraphWorldForkPlan,run_graph_world_fork
    from conductor_sim import GraphEventInquiryPlan,run_graph_event_inquiry
    import conductor_sim.graph_world_fork as adapter
    out.mkdir(parents=True,exist_ok=True)
    graph=old_graph("v2")
    before=plain(graph.as_dict())
    old_objects=(graph.baseline_native,*(e.native for e in graph.entries))
    old_models=(graph.plan.original,*(e.scenario for e in graph.entries))
    plan=new_fork_plan(graph)
    observed,assembled,revised=[],[],[]
    orig_observe,orig_reassemble,orig_revise=(
        adapter._observe,adapter.reassemble_scenario,adapter.revise_scenario)
    def spy_observe(model,*args,**kw):
        assert all(model is not old for old in old_models)
        observed.append(model.scenario_id)
        return orig_observe(model,*args,**kw)
    def spy_reassemble(parent,*args,**kw):
        assembled.append(kw.get("scenario_id"))
        return orig_reassemble(parent,*args,**kw)
    def spy_revise(parent,*args,**kw):
        revised.append(kw.get("scenario_id"))
        return orig_revise(parent,*args,**kw)
    with (mock.patch.object(adapter,"_observe",side_effect=spy_observe),
          mock.patch.object(adapter,"reassemble_scenario",side_effect=spy_reassemble),
          mock.patch.object(adapter,"revise_scenario",side_effect=spy_revise)):
        fork=run_graph_world_fork(plan)
    statuses=[e.status for e in fork.entries]
    assert statuses==["complete","complete","complete",
                      "rejected-structural-model","complete"],statuses
    assert len(observed)==4 and len(assembled)==3 and len(revised)==1
    assert set(observed)=={e.scenario.scenario_id for e in fork.entries
                          if e.scenario is not None}
    assert all(obj is original for obj,original in zip(
        (graph.baseline_native,*(e.native for e in graph.entries)),old_objects))
    assert plain(graph.as_dict())==before
    assert fork.entries[0].parent_scenario is graph.entries[2].scenario
    assert fork.entries[1].parent_scenario is fork.entries[0].scenario
    assert fork.entries[2].parent_scenario is fork.entries[1].scenario
    assert fork.entries[4].parent_scenario is graph.entries[1].scenario
    assert "field:fork" in fork.entries[2].source_ancestry.retired_source_ids
    assert "field:fork" in fork.entries[4].source_ancestry.active_source_ids
    assert "field:fork" not in graph.entries[1].source_ancestry.seen_source_ids
    assert fork.entries[3].scenario is fork.entries[3].native is None
    assert fork.entries[3].source_ancestry is None
    assert fork.entries[2].scenario.spec.plane_normal == graph.plan.original.spec.plane_normal
    assert fork.entries[1].source_ancestry.parent_revision_id == (
        fork.entries[0].scenario.revision_id)
    assert fork.entries[2].source_ancestry.parent_revision_id == (
        fork.entries[1].scenario.revision_id)
    worlds={"baseline":(graph.plan.original,graph.baseline_native)}
    worlds.update((e.node.node_id,(e.scenario,e.native)) for e in graph.entries)
    worlds.update((e.node.node_id,(e.scenario,e.native)) for e in fork.entries
                  if e.scenario is not None)
    physics=validate_native(worlds)
    comparisons=pair_check(graph,fork)
    assert fork.as_dict()["source_graph_sha256"]==digest(graph.as_dict())
    second=run_graph_world_fork(plan)
    assert plain(graph.as_dict())==before
    assert all(a is b for a,b in zip(
        (graph.baseline_native,*(e.native for e in graph.entries)),old_objects))
    assert second.as_dict()["source_graph_sha256"]==fork.as_dict()["source_graph_sha256"]
    q=(PlaneEvent("review:postgraph",(.19,0.,0.),(1.,0.,0.),
                    "Independently new postgraph M33b detector",direction=1),)
    inquiry=run_graph_event_inquiry(GraphEventInquiryPlan(
        graph,"review01:new-inquiry",("baseline","old-west"),q,POLICY))
    assert plain(graph.as_dict())==before
    assert len(inquiry.entries)==2
    mismatch=cross_event_study_incompatibility(graph)
    refused=negative_models(graph)
    event_refused=old_event_refusal_can_parent()
    opposing_roots=two_opposite_signed_roots()
    guard_prefix=genuine_source_guard_prefix()
    hostile(graph,plan,fork)
    (out/"old.json").write_bytes(before)
    (out/"fork.json").write_bytes(plain(second.as_dict()))
    (out/"inquiry.json").write_bytes(plain(inquiry.as_dict()))
    # Last: mutate original issued graph then demonstrate fork is no longer exportable.
    altered=replace(graph.entries[0],status="forged-original-status")
    object.__setattr__(graph,"entries",(altered,)+graph.entries[1:])
    must_fail("mutated original graph detected after issuing fork",second.as_dict)
    result=dict(physical_reference=physics, comparisons=comparisons,
                new_world_statuses=statuses, new_integration_ids=observed,
                actual_structural_reassemblies=assembled,
                actual_physical_revisions=revised,
                second_fork_reused_old_native_identities=True,
                mismatched_studies=mismatch, physical_refusals=refused,
                eligible_old_event_refusal=event_refused,
                opposite_signed_roots=opposing_roots,
                source_guard_prefix=guard_prefix,
                hostile_checks=FAILURES,original_graph_sha256=sha256(before).hexdigest())
    (out/"review-results.json").write_bytes(plain(result))
    print("INDEPENDENT_RESULT "+json.dumps(result,sort_keys=True))
    return result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--legacy-only",action="store_true")
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    if args.legacy_only:
        legacy(args.out)
    else:
        full(args.out)
        legacy(args.out/"legacy")


if __name__=="__main__":
    main()
