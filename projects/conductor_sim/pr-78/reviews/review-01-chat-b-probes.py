"""Chat B original M34a R2 probes; no use of developer tests or reference oracle.
Runs against separately pinned released/candidate source using PYTHONPATH.
"""
from __future__ import annotations

import argparse
from dataclasses import replace
from hashlib import sha256
import json
from math import hypot, nextafter, pi, sqrt, ulp, isfinite
from pathlib import Path

from conductor_sim import (
    CoupledPropertyEdit, FixedPointField, PhysicalWorldNode, PointCharge,
    PrescribedField, StructuralWorldNode, TestChargeMotionSpec,
    UniformElectricField, UniformGravity, UnifiedObservationPlan,
    WorldComparison, run_unified_observation_graph,
)
from conductor_sim.motion_events import EventPolicy, PlaneEvent
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.structural_family import StructuralCase
from conductor_sim.structural_scenarios import (
    NamedSource, ScenarioReassembly, SourceReplacement, reassemble_scenario,
)
from conductor_sim.graph_event_inquiry import GraphEventInquiryPlan, run_graph_event_inquiry
from conductor_sim.prescribed_fields import UniformRodField
from conductor_sim.solver import UnsupportedProblem

# New review world, NOT the developer's (1,2,-1) oblique example.
NORMAL = (3., 5., -7.)
E0 = (140., 70., 110.)
EA = (56., -14., 14.)
EB = (-21., 35., 16.)
EC = (14., 28., 26.)
CHARGE = 3.2e-9
M0 = 2.4e-6
M1 = 3.1e-6
P0 = (.006, -.010, .005)
V0 = (.14, .07, .11)
G = (.035, .042, .045)
X_STOP = .100
POINT_POSITION = (.076, .060, .085)
POINT_Q = 2e-11
POINT_K = 1 / (4 * pi * 8.8541878128e-12)
CHECKS = []


def check(test, reason):
    if not test:
        raise AssertionError(reason)
    CHECKS.append(reason)


def near(a, b, tol, name):
    if not (isfinite(a) and isfinite(b) and abs(a-b) <= tol):
        raise AssertionError(f"{name}: actual={a!r} independent={b!r}, tol={tol}")


def vec_near(actual, expected, tol, name):
    check(len(actual)==3, name+" is genuine 3-vector")
    for k in range(3):
        near(actual[k], expected[k], tol, name+f"[{k}]")


def sha(record):
    return sha256(json.dumps(record, sort_keys=True,
                             separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def model_hash(scenario):
    d = scenario.as_dict()
    original = dict(d)
    expected = original.pop("revision_id")
    check(sha(original) == expected == scenario.revision_id,
          "independently recomputed SHA256 of native source-model record")
    return expected


def source_model():
    spec = TestChargeMotionSpec(
        PrescribedField((UniformElectricField(E0),)),
        PointCharge(CHARGE,P0), M0, V0, .85, .017,
        plane_normal=NORMAL, gravity=UniformGravity(G))
    return PrescribedScenario(
        "chatb34:root", spec, (("held:root","Original fixed source"),),
        "Reviewer independently authored SI planar noncardinal world.")


def add_A():
    return StructuralCase(
        "introduce", "Introduce first separate held electrostatic field.",
        add_sources=(NamedSource("held:A","Alternative physical field A",
                                UniformElectricField(EA)),))


def old_new():
    parent=source_model()
    first=model_hash(parent)
    initial=parent.as_dict()
    n=parent.spec.plane_normal
    check(hypot(*n)==0.9999999999999999,
          "novel (3,5,-7) normal has one below-unit binary64 hypot")
    check(n != NORMAL, "original raw normal normalized once")
    d={"root_revision_id":first, "original_normal_hex":[v.hex() for v in n]}
    try:
        result=reassemble_scenario(
            parent, scenario_id="chatb34:child",
            note=add_A().note, add_sources=add_A().add_sources)
    except (ValueError,UnsupportedProblem,TypeError) as exc:
        d["accepted"]=False
        d["reason"]=f"{type(exc).__name__}: {exc}"
    else:
        d["accepted"]=True
        d["reason"]="actual new qualified source model"
        d["child_revision_id"]=model_hash(result.scenario)
        check(result.parent is parent, "M22a exact immediate original object")
        check(result.scenario.spec.plane_normal == n,
              "new assembly preserved original exact normalized plane bits")
        check(result.as_dict()["parent_revision_id"]==parent.revision_id,
              "new assembly binds actual original revision")
        check(len(result.scenario.spec.field.sources)==2,
              "new assembly physically added a held field")
    check(initial==parent.as_dict(), "source original unmutated after attempt")
    return d


def fields(world):
    f={"baseline":(E0,M0),
       "introduce":(tuple(E0[k]+EA[k] for k in range(3)),M0),
       "tune":(tuple(E0[k]+EA[k] for k in range(3)),M1),
       "exchange":(tuple(E0[k]+EB[k] for k in range(3)),M1),
       "remove":(E0,M1),
       "alternate":(tuple(E0[k]+EC[k] for k in range(3)),M0)}
    return f[world]


def math_reference(field,mass,t):
    e=field
    force=tuple(CHARGE*e[k] + mass*G[k] for k in range(3))
    a=tuple(force[k]/mass for k in range(3))
    pos=tuple(P0[k]+V0[k]*t+.5*a[k]*t*t for k in range(3))
    vel=tuple(V0[k]+a[k]*t for k in range(3))
    return pos,vel,force,a


def independent_x_root(field,mass,x_target):
    ax=CHARGE*field[0]/mass + G[0]
    delta=x_target-P0[0]
    return 2*delta/(V0[0]+sqrt(V0[0]**2+2*ax*delta))


def policy():
    return EventPolicy(.008, 1e-8, 1e-8, 1e-6)


def detector(x, id):
    return PlaneEvent(id, (x,0.,0.), (1.,0.,0.),
                      "New independently asked signed x-coordinate crossing",
                      direction=1)


def graph():
    root=source_model()
    swap=StructuralCase("exchange","Replace real independently held A with B.",
        replace_sources=(SourceReplacement(
            "held:A",NamedSource("held:B","New B different field",UniformElectricField(EB))),))
    rm=StructuralCase("remove","Actually remove newly held B.",remove_sources=("held:B",))
    alt=StructuralCase("alternate","Independent branch may use A without sharing history.",
        add_sources=(NamedSource("held:A","Sibling field A independent",UniformElectricField(EC)),))
    bad=StructuralCase("resurrect","Attempt invalid return of retired source A.",
        add_sources=(NamedSource("held:A","Forged resurrected field A",UniformElectricField(EA)),))
    point=StructuralCase("pointkind","Add a finite-distanced point charge in original physical plane.",
        add_sources=(NamedSource("held:point","Nonuniform charge field",
                                FixedPointField(POINT_Q, POINT_POSITION)),))
    nodes=(
        StructuralWorldNode("introduce","baseline",add_A(),"events"),
        PhysicalWorldNode("tune","introduce",
             "Actually change probe inertial mass for another whole-model integration.",
             (CoupledPropertyEdit("test-particle","mass_kg",M1),),"events"),
        StructuralWorldNode("exchange","tune",swap,"events"),
        StructuralWorldNode("remove","exchange",rm,"events"),
        StructuralWorldNode("alternate","baseline",alt,"events"),
        StructuralWorldNode("resurrect","exchange",bad,"events"),
        StructuralWorldNode("pointkind","baseline",point,"events"),
    )
    return UnifiedObservationPlan(
        "chatb34:graph",root,nodes,"events",(detector(X_STOP,"x:first"),),
        policy(),True,(
            WorldComparison("ab","introduce","exchange"),
            WorldComparison("ac","alternate","tune"),
        ))


def true_time_samples(native, world):
    field,mass=fields(world)
    samples=native.trajectory.samples
    check(native.trajectory.termination=="duration",
          world+" genuinely completed native observation")
    check(len(samples)>20, world+" many actual saved native times")
    check(len(native.events)==1, world+" exactly one signed M24a root")
    e=native.events[0]
    check(e.event_id=="x:first" and e.direction==1 and not e.terminal,
          world+" native signed positive passive event")
    t=e.sample.time_s
    near(t,independent_x_root(field,mass,X_STOP),5e-7,world+" event true root time")
    check(e.time_bracket_s[0] <= t <= e.time_bracket_s[1],
          world+" native event within actual bracket")
    check(e.time_bracket_s[1]-e.time_bracket_s[0] < 2e-4,
          world+" finite resolution root bracket narrow")
    for s in samples:
        p,v,f,a=math_reference(field,mass,s.time_s)
        vec_near(s.position_m,p,7e-8,world+" position")
        vec_near(s.velocity_m_s,v,7e-8,world+" velocity")
        vec_near(s.force_n,f,3e-12,world+" Newtonian force")
        vec_near(s.acceleration_m_s2,a,6e-8,world+" acceleration")
        vec_near(s.electric_field_v_m,field,3e-9,world+" SI electric field")
    return {"n_samples":len(samples),"root_s":t,
            "analytic_root_s":independent_x_root(field,mass,X_STOP),
            "max_native_bracket_s":e.time_bracket_s[1]-e.time_bracket_s[0]}


def point_force(state):
    p=state[:3]
    delta=tuple(p[k]-POINT_POSITION[k] for k in range(3))
    d=hypot(*delta)
    field=tuple(E0[k]+POINT_K*POINT_Q*delta[k]/d**3 for k in range(3))
    accel=tuple(CHARGE*field[k]/M0+G[k] for k in range(3))
    return (*state[3:],*accel),field


def point_reference(native):
    """New independent fixed-step explicit RK4 for true off-axis point Coulomb field;
    does not call conductor_sim force/ODE/RK implementations."""
    samples=native.trajectory.samples
    check(native.trajectory.termination=="duration", "point Coulomb world completed")
    check(len(samples)>20, "point Coulomb world saved native trajectory")
    state=(*P0,*V0)
    current=0.
    for sample in samples:
        target=sample.time_s
        check(target>=current, "point times sorted")
        while current<target-1e-14:
            h=min(.0002,target-current)
            k1,_=point_force(state)
            z=tuple(state[j]+h*k1[j]/2 for j in range(6))
            k2,_=point_force(z)
            z=tuple(state[j]+h*k2[j]/2 for j in range(6))
            k3,_=point_force(z)
            z=tuple(state[j]+h*k3[j] for j in range(6))
            k4,_=point_force(z)
            state=tuple(state[j]+h*(k1[j]+2*k2[j]+2*k3[j]+k4[j])/6 for j in range(6))
            current +=h
        rhs,field=point_force(state)
        vec_near(sample.position_m,state[:3],2e-5,"point 3D RK4 position")
        vec_near(sample.velocity_m_s,state[3:],3e-5,"point 3D RK4 velocity")
        vec_near(sample.force_n,
                 tuple(CHARGE*field[k]+M0*G[k] for k in range(3)),
                 1.2e-7,"point independent Coulomb force")
    check(len(native.events)>=1,"point world genuine positive signed event")
    e=next(e for e in native.events if e.event_id=="x:first")
    check(e.direction==1 and e.time_bracket_s[0]<=e.sample.time_s<=e.time_bracket_s[1],
          "point native signed bracket and root")
    return {"samples":len(samples),"event_s":e.sample.time_s}


def refusal_check(label,do):
    try:
        do()
    except (UnsupportedProblem,ValueError,TypeError) as exc:
        CHECKS.append("REFUSED "+label+": "+type(exc).__name__)
        return
    raise AssertionError("FALSE ADMISSION: "+label)


def negative_physics(root):
    s=root.spec
    zero_field=PrescribedField((UniformElectricField((0.,0.,0.)),))
    for normal in ((0.,0.,0.),(float("nan"),0.,1.),
                   (float("inf"),0.,1.),(1.,2.),("1",2.,3.),
                   (True,0.,0.)):
        refusal_check("invalid normal "+str(normal),
                      lambda n=normal: replace(s,plane_normal=n))
    refusal_check("out-of-plane initial launch",
                  lambda: replace(s,initial_velocity_m_s=(.15,.07,.11)))
    refusal_check("out-of-plane gravity",
                  lambda: replace(s,gravity=UniformGravity((.036,.042,.045))))
    refusal_check("out-of-plane uniform field",
                  lambda: replace(s,field=PrescribedField(
                      (UniformElectricField((141.,70.,110.)),))))
    refusal_check("unpaired out-of-plane point source",
                  lambda: replace(s,field=PrescribedField((
                      UniformElectricField(E0),FixedPointField(1e-11,(0.,0.,.10))))))
    refusal_check("unpaired out-of-plane rod",
                  lambda: replace(s,field=PrescribedField((
                      UniformElectricField(E0),
                      UniformRodField(1e-11,(.04,.01,.01),(.07,.02,.02))))))
    # Zero/one ULP normalization, and genuinely beyond the one-ULP window.
    exact=(1.,0.,0.)
    up=(nextafter(1.,float("inf")),0.,0.)
    down=(nextafter(1.,0.),0.,0.)
    down2=(1.-ulp(1.),0.,0.)
    outside_up=(1.+2*ulp(1.),0.,0.)
    outside_down=(nextafter(down2[0],0.),0.,0.)
    for n in (exact,up,down,down2):
        t=replace(s,field=zero_field,gravity=None,
                  initial_velocity_m_s=(0.,.11,.0),plane_normal=n)
        check(t.plane_normal==n,"near-unit one-ULP normal preserved "+repr(n))
        check(replace(t, duration_s=.75).plane_normal==n,
              "near-unit dataclass replacement fixed "+repr(n))
    for n in (outside_up,outside_down):
        t=replace(s,field=zero_field,gravity=None,
                  initial_velocity_m_s=(0.,.11,.0),plane_normal=n)
        check(t.plane_normal==(1.,0.,0.),
              "outside one-ULP normal still normalized "+repr(n))
    for n in ((3.,5.,-7.),(-3.,-5.,7.),(1.,2.,-1.),(3.,5.,7.)):
        t=replace(s,field=zero_field,gravity=None,
                  initial_velocity_m_s=(0.,0.,0.),plane_normal=n)
        check(replace(t, duration_s=.75).plane_normal==t.plane_normal,
              "mixed-sign normalized plane exactly stable "+repr(n))
    # Structural equality invariant remains exact even if edited child is planar.
    good = reassemble_scenario(root,scenario_id="chatb34:valid",note=add_A().note,
                              add_sources=add_A().add_sources)
    changed=replace(good.scenario.spec,initial_velocity_m_s=(.28,.14,.22))
    bad=PrescribedScenario("chatb34:cheat",changed,
                           good.scenario.source_annotations,"Changed launch independently")
    refusal_check("structural edit cannot silently change real launch",
                  lambda: ScenarioReassembly(root,bad))


def guard_export(label,run,obj,field,new):
    original=getattr(obj,field)
    object.__setattr__(obj,field,new)
    try:
        try:
            run.as_dict()
        except (ValueError,TypeError,UnsupportedProblem,AssertionError) as exc:
            CHECKS.append("HOSTILE REFUSED "+label+": "+type(exc).__name__)
        else:
            raise AssertionError("HOSTILE EXPORT ACCEPTED "+label)
    finally:
        object.__setattr__(obj,field,original)
    check(type(run.as_dict()) is dict,"source evidence restored after "+label)


def full():
    plan=graph()
    initial=plan.original.as_dict()
    run=run_unified_observation_graph(plan)
    out=run.as_dict()
    check(out["schema"]=="conductor_sim.unified_observation_graph.v3",
          "genuine source-ancestry and comparison graph schema")
    check(run.baseline_status=="complete","baseline physically admitted")
    check(initial==plan.original.as_dict(),"plan original stable after real integrations")
    statuses={row.node.node_id:row.status for row in run.entries}
    for name in ("introduce","tune","exchange","remove","alternate","pointkind"):
        check(statuses[name]=="complete","genuinely admitted "+name)
    check(statuses["resurrect"]=="rejected-structural-model",
          "branch-local retired source A cannot resurrect")
    check(run.entries[5].scenario is None and run.entries[5].native is None,
          "retired source refusal has no fabricated observations")
    worlds={"baseline":(plan.original,run.baseline_native)}
    worlds.update({row.node.node_id:(row.scenario,row.native) for row in run.entries
                   if row.scenario is not None})
    expected_norm=plan.original.spec.plane_normal
    check(hypot(*expected_norm)==.9999999999999999,
          "complete graph uses novel native one-ULP-below-unit plane")
    physics={}
    for name in ("baseline","introduce","tune","exchange","remove","alternate"):
        sc,native=worlds[name]
        model_hash(sc)
        check(tuple(v.hex() for v in sc.spec.plane_normal)==
              tuple(v.hex() for v in expected_norm),
              "identical source normal float bits throughout "+name)
        physics[name]=true_time_samples(native,name)
    physics["pointkind"]=point_reference(worlds["pointkind"][1])
    expected={"introduce":("held:root","held:A"),
              "tune":("held:root","held:A"),
              "exchange":("held:root","held:B"),
              "remove":("held:root",),
              "alternate":("held:root","held:A"),
              "pointkind":("held:root","held:point")}
    for row in run.entries:
        if row.scenario is None:continue
        anc=row.source_ancestry
        parent=worlds[row.node.parent_id][0]
        check(row.parent_scenario is parent,
              "actual immediate parent *object* "+row.node.node_id)
        check(anc.parent_revision_id==parent.revision_id and
              anc.model_revision_id==row.scenario.revision_id,
              "exact native model SHA parent chain "+row.node.node_id)
        check(anc.active_source_ids==expected[row.node.node_id],
              "branch-local true active source IDs "+row.node.node_id)
        check(anc.world_path[-1]==row.node.node_id,
              "branch-local path ends at real node "+row.node.node_id)
        if row.assembly is not None:
            # M22a retains a previous ScenarioReassembly wrapper when the
            # graph's immediately preceding structural node has one.
            prior_row=next((earlier for earlier in run.entries
                            if earlier.node.node_id==row.node.parent_id),None)
            expected_assembly_parent=(prior_row.assembly if prior_row is not None
                                      and prior_row.assembly is not None else parent)
            check(row.assembly.parent is expected_assembly_parent,
                  "M22a exact native assembly-parent object "+row.node.node_id)
            check((row.assembly.parent.scenario if
                   isinstance(row.assembly.parent,ScenarioReassembly)
                   else row.assembly.parent) is parent,
                  "M22a actual immediate physical source parent object "+row.node.node_id)
            check(row.assembly.as_dict()["parent_revision_id"]==parent.revision_id,
                  "M22a stored actual physical parent SHA "+row.node.node_id)
    check(run.entries[2].source_ancestry.retired_source_ids==("held:A",),
          "true source identity A retired after physical change")
    check(run.entries[3].source_ancestry.retired_source_ids==("held:A","held:B"),
          "two source identities remain retired after removal")
    check(run.entries[4].source_ancestry.seen_source_ids==("held:root","held:A"),
          "independent sibling did not inherit other branch retirement")
    check(any(r["status"]=="compared" for r in out["cross_world_comparisons"]),
          "real native cross-world comparison emitted")
    for comparison in out["cross_world_comparisons"]:
        check(comparison["numerical_orientation"]=="right minus left",
              "comparison orientation explicit")
        left=worlds[comparison["left_world_id"]][0]
        right=worlds[comparison["right_world_id"]][0]
        check(comparison["left_revision_id"]==left.revision_id and
              comparison["right_revision_id"]==right.revision_id,
              "comparison genuine source world revision identities")
    # A new question on already-qualified source worlds, not reused event frames.
    iq=GraphEventInquiryPlan(
        run,"chatb34:reask",("baseline","tune","exchange"),
        (detector(.160,"x:later"),),policy(),
        (WorldComparison("laterdelta","baseline","exchange"),))
    inquiry=run_graph_event_inquiry(iq)
    idata=inquiry.as_dict()
    check(idata["schema"]=="conductor_sim.graph_event_inquiry.v1",
          "M33b new typed inquiry, true new M24a event study")
    check(idata["plan"]["source_graph_sha256"]==sha(run.as_dict()),
          "new inquiry binds hashed real old source graph")
    for entry in inquiry.entries:
        check(entry.status=="complete" and entry.scenario is worlds[entry.world_id][0],
              "M33b events reobserve same source model *object* "+entry.world_id)
        field,mass=fields(entry.world_id)
        ev=next(e for e in entry.native.events if e.event_id=="x:later")
        near(ev.sample.time_s,independent_x_root(field,mass,.160),
             7e-7,"independent new question second true root "+entry.world_id)
    # Reject direct whole-model physical violations and forged evidence.
    negative_physics(plan.original)
    guard_export("normal bits",run,plan.original.spec,"plane_normal",
                 (nextafter(expected_norm[0],float("inf")), *expected_norm[1:]))
    guard_export("original author label",run,plan.original,"source_annotations",
                 (("held:root","A forged teacher label"),))
    guard_export("original plan ID",run,plan,"plan_id","chatb34:fakeplan")
    guard_export("parent world identity",run,run.entries[2],"parent_scenario",
                 plan.original)
    guard_export("forged source ancestry",run,run.entries[2],"source_ancestry",
                 run.entries[4].source_ancestry)
    guard_export("invented source-guard",run,run.baseline_native.trajectory,
                 "termination","source-guard")
    e=run.baseline_native.events[0]
    guard_export("plus 0.03 seconds event root",run,e.sample,"time_s",
                 e.sample.time_s+.03)
    guard_export("Boolean False equals 0.0",run,
                 run.baseline_native.trajectory.samples[0],"time_s",False)
    detached=run.as_dict()
    detached["original_observation_status"]="fabricated"
    check(run.as_dict()["original_observation_status"]=="complete",
          "detached JSON edit does not mutate trusted native graph")
    # Attack new M33b inquiry report too.
    guard_export("new typed inquiry forged status",inquiry,inquiry.entries[0],
                 "status","terminal-event")
    return {"statuses":statuses, "independent_physics":physics,
            "inquiry_roots":{e.world_id:e.native.events[0].sample.time_s
                             for e in inquiry.entries},
            "source_revision_ids":{k:v[0].revision_id for k,v in worlds.items()},
            "native_graph_sha256":sha(out),
            "source_origin":"author-asserted teacher hypothetical, NOT authenticated PDF",
            "checks":len(CHECKS),"check_messages":CHECKS}


def legacy():
    base=PrescribedScenario("chatb34:legacy",
        TestChargeMotionSpec(
            PrescribedField((UniformElectricField((120.,30.,0.)),)),
            PointCharge(2e-9,(.006,.001,0.)), 2e-6,
            (.12,.01,0.),.6,.02, plane_normal=(0.,0.,1.),
            gravity=UniformGravity((.02,.01,0.))),
        (("held:base","Unchanged old normal source"),),
        "Reviewer legacy baseline unchanged old contract")
    node=StructuralWorldNode(
        "simple","baseline",StructuralCase(
            "simple","Original legitimate simple stationary source addition",
            add_sources=(NamedSource("held:add","Second field",
                                    UniformElectricField((20.,8.,0.))),)))
    versions={}
    for v in (1,2,3):
        kwargs={"retain_source_ancestry":v>=2}
        if v==3:kwargs["comparisons"]=(WorldComparison("a","baseline","simple"),)
        plan=UnifiedObservationPlan("chatb34:legacy"+str(v),base,(node,),**kwargs)
        run=run_unified_observation_graph(plan)
        d=run.as_dict()
        check(d["schema"].endswith(".v"+str(v)),
              "native legacy graph version "+str(v))
        check(run.entries[0].status=="complete",
              "legacy source addition admitted version "+str(v))
        versions["v"+str(v)]=d
        if v==3:
            iq=GraphEventInquiryPlan(
                run,"chatb34:legacyquery",("baseline","simple"),
                (detector(.055,"x:legacy"),),policy(),
                (WorldComparison("after","baseline","simple"),))
            ans=run_graph_event_inquiry(iq)
            check(all(e.status=="complete" for e in ans.entries),
                  "genuinely newly run M33b event inquiry for unaffected legacy source")
            versions["m33b_inquiry"]=ans.as_dict()
    return versions


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=("old","new","legacy"),required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    if a.mode=="old":
        d=old_new()
        check(not d["accepted"] and
              "structural operation cannot edit particle, analysis or numerical controls" in d["reason"],
              "released M33b native false structural refusal reproduced")
    elif a.mode=="new":
        d={"old_new":old_new()}
        check(d["old_new"]["accepted"],"candidate true structural source admission")
        d["reviewer_full"]=full()
    else:
        d=legacy()
    a.output.parent.mkdir(parents=True,exist_ok=True)
    payload=json.dumps(d, sort_keys=True, indent=2, allow_nan=False)+"\n"
    a.output.write_text(payload, encoding="utf-8")
    print(json.dumps({"mode":a.mode,"sha256":sha256(payload.encode()).hexdigest(),
                      "checks":len(CHECKS),
                      "source_model":d.get("root_revision_id") if a.mode=="old"
                         else d.get("old_new",{}).get("root_revision_id") },
                    sort_keys=True))


if __name__=="__main__":
    main()
