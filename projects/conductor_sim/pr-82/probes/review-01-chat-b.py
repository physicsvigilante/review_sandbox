"""Independent Chat B R2 probes for M35b, NOT copied from developer tests.

Run with PYTHONPATH pointing to one *pinned* source tree, first released then
candidate. Uses standard-library Coulomb law and independently integrated
2-D RK4 trajectories as reference; no project field callback is the oracle.
"""
from __future__ import annotations
import argparse
from dataclasses import replace
import json
import math
from pathlib import Path

from conductor_sim import (FixedPointField, PointCharge, PrescribedField,
    TestChargeMotionSpec, SweepAxis, TrajectorySweepPlan,
    run_trajectory_sweep, run_event_sweep)
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.event_sweep import EventSweepPlan, EventSweepRun
from conductor_sim.trajectory_sweep import TrajectorySweepRun
from conductor_sim.motion_events import EventPolicy, PlaneEvent
from examples.m28b_event_sweep import make_plan

Q = 5e-9
SOURCE = (.1, .03)  # x,z; y=0
EPSILON = 8.8541878128e-12
K = 1.0 / (4.0 * math.pi * EPSILON)
MASS = 2e-6
POS = 1e-9
VARIATIONS = (-1e-9, 2e-9)
V0 = (.6, .1)


def author(duration=.4, interval=.02, tag="original"):
    base = PrescribedScenario(
        "chat-b:offaxis-" + tag,
        TestChargeMotionSpec(
            PrescribedField((FixedPointField(Q, (SOURCE[0], 0., SOURCE[1])),)),
            PointCharge(POS, (0., 0., 0.)),
            MASS, (V0[0], 0., V0[1]), duration, interval,
            plane_normal=(0., 1., 0.), source_guard_m=.02,
            relative_tolerance=1e-9, max_internal_steps=200000),
        (("source:offaxis-Q", "Fixed positive point Q at x=.1,z=.03"),),
        "Independent two-coordinate Coulomb charge and signed detector.")
    sweep = TrajectorySweepPlan(
        "chat-b:" + tag, base, SweepAxis(
            "test-particle", "charge_c", VARIATIONS))
    questions = tuple(
        PlaneEvent(name, (.02, 0., 0.), (1., 0., 0.),
                   "Signed off-axis point-field crossing",
                   direction=direction)
        for name, direction in
        (("forward", 1), ("return", -1), ("either", 0)))
    return EventSweepPlan(sweep, questions, EventPolicy(.01, 1e-8, 1e-7, 1e-5))


def rhs(y, q):
    x, z, vx, vz = y
    dx, dz = x - SOURCE[0], z - SOURCE[1]
    r2 = dx * dx + dz * dz
    a = K * Q * q / (MASS * r2 ** 1.5)
    return (vx, vz, a * dx, a * dz)


def step(y, h, q):
    k1 = rhs(y, q)
    k2 = rhs(tuple(y[i] + .5 * h * k1[i] for i in range(4)), q)
    k3 = rhs(tuple(y[i] + .5 * h * k2[i] for i in range(4)), q)
    k4 = rhs(tuple(y[i] + h * k3[i] for i in range(4)), q)
    return tuple(y[i] + h * (k1[i]+2*k2[i]+2*k3[i]+k4[i])/6
                 for i in range(4))


def integrate_to(targets, q, hmax=2e-5):
    y = (0., 0., V0[0], V0[1])
    t = 0.
    result = []
    for wanted in targets:
        assert wanted >= t, ("unordered native clock", wanted, t)
        while t + 1e-13 < wanted:
            h = min(hmax, wanted - t)
            y = step(y, h, q)
            t += h
        result.append(y)
    return result


def close(a, b, absolute, relative=.003):
    assert math.isfinite(a) and math.isfinite(b)
    assert abs(a-b) <= absolute + relative*max(abs(a),abs(b)), (a,b,absolute,relative)


def physical_check(native, q):
    spec = native.spec
    assert spec.particle.charge_c == q
    assert spec.mass_kg == MASS
    assert len(spec.field.sources) == 1
    s = spec.field.sources[0]
    assert type(s) is FixedPointField and s.charge_c == Q
    assert s.position_m == (SOURCE[0],0.,SOURCE[1])
    assert spec.plane_normal == (0.,1.,0.)
    rows = native.samples
    assert rows and rows[0].time_s == 0.
    times = [r.time_s for r in rows]
    ref = integrate_to(times, q)
    max_position_error = 0.
    for row, (x,z,vx,vz) in zip(rows, ref):
        assert type(row.time_s) in (int,float)
        assert row.position_m[1] == row.velocity_m_s[1] == 0.
        max_position_error = max(max_position_error,
                                 math.hypot(row.position_m[0]-x,row.position_m[2]-z))
        for actual, expected in ((row.position_m[0],x),
                                 (row.position_m[2],z)):
            close(actual,expected,2e-5,.0005)
        for actual, expected in ((row.velocity_m_s[0],vx),
                                 (row.velocity_m_s[2],vz)):
            close(actual,expected,3e-4,.001)
        dx,dz=x-SOURCE[0],z-SOURCE[1]
        r=math.hypot(dx,dz)
        assert r >= spec.source_guard_m - 4e-4
        V=K*Q/r
        ex,ez=K*Q*dx/r**3,K*Q*dz/r**3
        ke=.5*MASS*(vx*vx+vz*vz)
        pe=q*V
        for actual, expected in ((row.potential_v,V),
                                 (row.electric_field_v_m[0],ex),
                                 (row.electric_field_v_m[2],ez)):
            close(actual,expected,.03,.006)
        for actual,expected in ((row.force_n[0],q*ex),
                                (row.force_n[2],q*ez),
                                (row.acceleration_m_s2[0],q*ex/MASS),
                                (row.acceleration_m_s2[2],q*ez/MASS)):
            close(actual,expected,1e-4,.006)
        for actual,expected in ((row.kinetic_energy_j,ke),
                                (row.potential_energy_j,pe),
                                (row.total_energy_j,ke+pe)):
            close(actual,expected,2e-9,.006)
    if native.termination == "duration":
        assert rows[-1].time_s == spec.duration_s
    else:
        assert native.termination in ("source-guard","terminal-event")
        assert rows[-1].time_s < spec.duration_s
    return {"samples":len(rows),"max_position_error_m":max_position_error,
            "last_time_s":rows[-1].time_s,"last_time_type":type(rows[-1].time_s).__name__,
            "termination":native.termination}


def roots_reference(q, horizon, threshold=.02, hmax=1e-5):
    y=(0.,0.,V0[0],V0[1])
    t=0.
    roots=[]
    while t < horizon-1e-13:
        h=min(hmax,horizon-t)
        z=step(y,h,q)
        g0,g1=y[0]-threshold,z[0]-threshold
        if g0*g1<0:
            direction=1 if g1>g0 else -1
            roots.append((t+h*(-g0)/(g1-g0),direction))
        t+=h
        y=z
    return roots


def event_check(run, q):
    trajectory=run.trajectory
    summary=physical_check(trajectory,q)
    ref=roots_reference(q,trajectory.samples[-1].time_s)
    expected={"forward":1,"return":-1,"either":0}
    for event_id,direction in expected.items():
        nr=[(t,d) for t,d in ref if direction==0 or d==direction]
        found=[e for e in run.events if e.event_id==event_id]
        assert len(found)==len(nr),(event_id,q,found,nr)
        for observed,(t,expected_direction) in zip(found,nr):
            assert observed.direction==expected_direction
            lo,hi=observed.time_bracket_s
            assert 0<lo<=observed.sample.time_s<=hi<=trajectory.spec.duration_s
            assert hi-lo<=run.study.policy.time_tolerance_s*1.01
            close(observed.sample.time_s,t,.001,0.)
    summary["signed_roots"]=len(run.events)
    summary["independent_root_times"]=[(round(t,7),d) for t,d in ref]
    return summary


def expect_refusal(action,label):
    try: action()
    except (ValueError,TypeError,AttributeError) as err:
        return {"attack":label,"refused_by":type(err).__name__,
                "message":str(err)[:180]}
    raise AssertionError("Native tamper escaped validation: "+label)


def flip_and_restore(obj,attribute,value,run,label):
    before=run.as_dict()
    old=getattr(obj,attribute)
    try:
        object.__setattr__(obj,attribute,value)
        evidence=expect_refusal(run.as_dict,label)
    finally:
        object.__setattr__(obj,attribute,old)
    assert run.as_dict()==before, ("Mutation leaked",label)
    return evidence


def adversarial(m,e):
    failures=[]
    em=e.entries[1]  # genuine complete, positive 2e-9
    mm=m.entries[1]
    for run,entry,native_field in ((m,mm,"trajectory"),(e,em,"run")):
        bad=replace(entry,scenario=None,**{native_field:None})
        failures.append(expect_refusal(
            lambda run=run,bad=bad: replace(run,
                entries=(run.entries[0],bad)).as_dict(),"issue80-replace-"+native_field))
        if native_field=="trajectory":
            failures.append(expect_refusal(
                lambda:bad.as_dict(m.baseline_trajectory),"issue80-standalone-motion"))
        else:
            failures.append(expect_refusal(
                lambda:bad.as_dict(e.baseline_run,e.plan.questions),"issue80-standalone-event"))
    failures.append(expect_refusal(lambda: TrajectorySweepRun(m.plan,m.baseline_trajectory,m.entries),
                        "unissued-native-trajectory-run"))
    failures.append(expect_refusal(lambda: EventSweepRun(e.plan,e.baseline_run,e.entries),
                        "unissued-native-event-run"))
    failures.append(flip_and_restore(m.entries[1],"status","censored",m,"postissue-status"))
    failures.append(flip_and_restore(e.plan.sweep.baseline,"provenance",
                  "altered physical source claim",e,"changed-baseline-source"))
    failures.append(flip_and_restore(m.entries[1].scenario,"parent_revision_id",
                   "f"*64,m,"wrong-parent-revision"))
    failures.append(flip_and_restore(e.plan.sweep.baseline,"source_annotations",
                   (("source:offaxis-Q","renamed held source"),),e,"changed-held-label"))
    failures.append(flip_and_restore(e.plan.sweep.axis,"values",
                   (-1e-9,3e-9),e,"changed-axis-values"))
    failures.append(flip_and_restore(e.plan.questions[0],"direction",
                   -1,e,"changed-detector-direction"))
    failures.append(flip_and_restore(e.plan.questions[0],"normal",
                   (-1.,0.,0.),e,"changed-detector-normal"))
    failures.append(flip_and_restore(e.plan.questions[0],"role",
                   "ideal-stop-surface",e,"changed-detector-role"))
    failures.append(flip_and_restore(e.plan.policy,"max_step_s",.015,e,
                                     "changed-typed-numerical-policy"))
    failures.append(flip_and_restore(m.entries[1],"explanation",
                   "falsified observation",m,"postissue-reason"))
    failures.append(flip_and_restore(e,"_issued_digest","0"*64,e,"bad-issuer-receipt"))
    sample=mm.trajectory.samples[0]
    bool_native=replace(mm.trajectory,samples=(
      replace(sample,time_s=False),)+mm.trajectory.samples[1:])
    failures.append(expect_refusal(
       lambda:replace(m,entries=(m.entries[0],replace(mm,trajectory=bool_native))),
       "bool-false-clock-motion"))
    bad_row=replace(sample,force_n=(3.,0.,5.),total_energy_j=42.)
    bad_native=replace(mm.trajectory,samples=(bad_row,)+mm.trajectory.samples[1:])
    failures.append(expect_refusal(
       lambda:replace(m,entries=(m.entries[0],replace(mm,trajectory=bad_native))),
       "forged-native-force-energy"))
    neg=e.entries[0]
    assert neg.status=="censored"
    fake=replace(neg.run,trajectory=replace(neg.run.trajectory,termination="duration"))
    failures.append(expect_refusal(
       lambda:replace(e,entries=(replace(neg,run=fake,status="complete"),e.entries[1])),
       "guard-overwritten-as-complete-duration"))
    root=neg.run.events[0]
    forged=replace(root,time_bracket_s=(.39,.399))
    fake_events=replace(neg.run,events=(forged,)+neg.run.events[1:])
    failures.append(expect_refusal(
       lambda:replace(e,entries=(replace(neg,run=fake_events),e.entries[1])),
       "forged-root-outside-guard"))
    good=e.as_dict()
    detached=e.as_dict()
    detached["entries"][1]["status"]="INVENTED"
    detached["baseline_event_run"]["events"]=[]
    assert e.as_dict()==good
    return failures


def refusals(p):
    s=p.sweep.baseline
    oblique=TrajectorySweepPlan("chat-b:bad-source",s,SweepAxis(
        "source:offaxis-Q","position_m",((.1,.005,.03),(.11,0.,.03))))
    r=run_event_sweep(EventSweepPlan(oblique,p.questions,p.policy))
    assert [x.status for x in r.entries]==["rejected-physical-model","complete"]
    stop=PlaneEvent("stop",(.03,0.,0.),(1.,0.,0.),
                   "Signed ideal stop in retained field",direction=1,
                   terminal=True,role="ideal-stop-surface")
    launch=TrajectorySweepPlan("chat-b:bad-stop",s,SweepAxis(
        "test-particle","position_m",((.05,0.,0.),(-.01,0.,0.))))
    terminal=run_event_sweep(EventSweepPlan(launch,(stop,),p.policy))
    assert terminal.baseline_run.trajectory.termination=="terminal-event"
    assert terminal.entries[0].status=="rejected-event-study"
    assert terminal.entries[1].status=="censored"
    return {"physical_rejection":[x.status for x in r.entries],
            "terminal_variations":[x.status for x in terminal.entries],
            "terminal_baseline":terminal.baseline_run.trajectory.termination}


def issue80_old():
    p=make_plan("uniform-mass")
    e=run_event_sweep(p)
    m=run_trajectory_sweep(p.sweep)
    ebad=replace(e.entries[0],scenario=None,run=None,
                 status="complete",reason="invented")
    mbad=replace(m.entries[0],scenario=None,trajectory=None,
                 status="complete",explanation="invented")
    fakee=replace(e,entries=(ebad,)+e.entries[1:]).as_dict()
    fakem=replace(m,entries=(mbad,)+m.entries[1:]).as_dict()
    assert fakee["entries"][0]["status"]=="complete" and fakee["entries"][0]["event_run"] is None
    assert fakem["entries"][0]["status"]=="complete" and fakem["entries"][0]["trajectory"] is None
    return {"original_released_event_complete_without_native":"reproduced",
            "original_released_motion_complete_without_native":"reproduced"}


def historical_bytes(out):
    fixtures=[("motion-uniform","uniform-mass","motion"),
              ("event-uniform","uniform-mass","event"),
              ("motion-ring","ring-detector","motion"),
              ("event-ring","ring-detector","event"),
              ("motion-guard","gravity-guard","motion"),
              ("event-guard","gravity-guard","event"),
              ("event-double-root","multi-crossing","event"),
              ("event-terminal","coincident-terminal","event"),
              ("event-dense-terminal","dense-terminal","event")]
    for name,case,kind in fixtures:
        p=make_plan(case)
        r=run_event_sweep(p) if kind=="event" else run_trajectory_sweep(p.sweep)
        (out/(name+".json")).write_text(json.dumps(r.as_dict(),
              indent=2,allow_nan=False,ensure_ascii=True)+"\n")
    return [x[0] for x in fixtures]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode",choices=("old","candidate"),required=True)
    parser.add_argument("--out",required=True,type=Path)
    args=parser.parse_args()
    out=args.out;out.mkdir(parents=True,exist_ok=True)
    p=author()
    m=run_trajectory_sweep(p.sweep)
    e=run_event_sweep(p)
    assert [r.status for r in m.entries]==["censored","complete"]
    assert [r.status for r in e.entries]==["censored","complete"]
    print("Original off-axis native statuses:",[x.status for x in e.entries],flush=True)
    checks={}
    for kind,run in (("motion",m),("event",e)):
        items=[("baseline",POS,run.baseline_run.trajectory if kind=="event"
                            else run.baseline_trajectory)]
        items += [(f"variant_{i}", q,(r.run.trajectory if kind=="event"
                            else r.trajectory)) for i,(q,r) in enumerate(zip(VARIATIONS,run.entries))]
        for name,q,native in items:
            checks[kind+"_"+name]=physical_check(native,q)
            if kind=="event":
                checks[kind+"_"+name+"_roots"]=event_check(
                    run.baseline_run if name=="baseline" else run.entries[int(name[-1])].run,q)
    pairs=e.as_dict()["entries"]
    assert {x["event_id"]:x["status"] for x in pairs[0]["event_time_comparisons"]}["forward"]=="unpaired"
    paired={x["event_id"]:x["status"] for x in pairs[1]["event_time_comparisons"]}
    assert paired=={"forward":"one-resolved-pair","return":"one-resolved-pair","either":"unpaired"},paired
    # Distinct native integer clock and non-dividing decimal interval.
    intp=author(duration=1,interval=.03,tag="int-clock")
    im=run_trajectory_sweep(intp.sweep); ie=run_event_sweep(intp)
    for n in (im.baseline_trajectory,im.entries[1].trajectory,
              ie.baseline_run.trajectory,ie.entries[1].run.trajectory):
        assert n.termination=="duration" and type(n.samples[-1].time_s) is int
        assert n.samples[-1].time_s==1
        physical_check(n,n.spec.particle.charge_c)
    checks["native_integer_horizon"]={"cases":4,"endpoint_type":"int","value":1,
                                     "interval_s":.03}
    checks["physical_refusals_and_terminal"]=refusals(p)
    if args.mode=="old":
        checks["inherited_issue80"]=issue80_old()
    else:
        checks["inherited_issue80_fixed"]=len(adversarial(m,e))
        assert checks["inherited_issue80_fixed"]>=17
    for name,run in (("new-motion",m),("new-event",e),
                     ("new-int-motion",im),("new-int-event",ie)):
        (out/(name+".json")).write_text(json.dumps(run.as_dict(),
                  indent=2,allow_nan=False,ensure_ascii=True)+"\n")
    checks["historical_outputs"]=historical_bytes(out)
    (out/"review-summary.json").write_text(json.dumps(checks,indent=2,allow_nan=False)+"\n")
    print("CHAT_B_ORIGINAL_PROBES PASS",args.mode,json.dumps(
          {"samples":sum(a["samples"] for a in checks.values()
                      if isinstance(a,dict) and "samples" in a),
           "new_science_cases":len([a for a in checks if a.startswith("event_") or a.startswith("motion_")]),
           "integrity_attack_count":checks.get("inherited_issue80_fixed"),
           "legacy_files":len(checks["historical_outputs"])},sort_keys=True),flush=True)


if __name__=="__main__":
    main()
