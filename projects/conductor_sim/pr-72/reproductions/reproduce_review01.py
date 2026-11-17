"""Developer-run reproduction of Chat B M31b review-01 probes on a pinned source.

This is a reproducer, not an independent Chat B review. The first-attempt
negative output is saved without altering the reviewed source.
"""
from dataclasses import replace
from pathlib import Path
import importlib.util
import json
import traceback

from conductor_sim import (
    CoupledEventPlan, CoupledEventRun, CoupledPropertyEdit,
    CoupledHypothesis, CoupledPhysicalPlan, run_coupled_event_family,
)
import conductor_sim.coupled_event_family as service
from conductor_sim.coupled_physical_family import (
    CoupledPhysicalRun, run_coupled_physical_family,
)
from conductor_sim.motion_events import EventPolicy, PlaneEvent
from examples.m29a_structural_family import model
from examples.m31b_rod_reference import make_plan

path=Path("../reviews/projects/conductor_sim/pr-72/reviews/review-01-chat-b-probes.py")
spec=importlib.util.spec_from_file_location("chatb_m31b_probes",str(path))
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

out={}
def record(name,action):
    try:
        result=action()
        out[name]={"result":"ACCEPTED", "detail":result}
    except Exception as exc:
        out[name]={"result":"REJECTED", "type":type(exc).__name__,
                   "detail":str(exc)[:300]}
    print(name,json.dumps(out[name],sort_keys=True),flush=True)

record("NOVEL", mod.independent_gravity_field_case)

run=run_coupled_event_family(make_plan())
child=run.children[0]
root=child.event_run.events[0]
shift=.03
fake_root=replace(root,time_bracket_s=tuple(v+shift for v in root.time_bracket_s),
                  sample=replace(root.sample,time_s=root.sample.time_s+shift))
tampered_child=replace(child,event_run=replace(child.event_run,events=(fake_root,)))
record("F01_FORGED_ROOT_TIME",lambda: CoupledEventRun(
    run.plan,run.physical_family,run.original_event_run,run.parents,
    (tampered_child,)).as_dict()["coupled_events"][0]["event_run"]["events"][0]["sample"]["time_s"])

fake_parent=replace(run.parents[0],event_run=None,status="rejected-event-study",
                    reason="fabricated refusal")
record("F02_FORGED_PARENT_REFUSAL",lambda: CoupledEventRun(
    run.plan,run.physical_family,run.original_event_run,(fake_parent,),
    run.children).as_dict()["coupled_events"][0]["parent_event_time_comparisons"])

fake_child=replace(child,event_run=None,status="rejected-event-study",
                   reason="fabricated child refusal")
record("F02_FORGED_CHILD_REFUSAL",lambda: CoupledEventRun(
    run.plan,run.physical_family,run.original_event_run,run.parents,
    (fake_child,)).as_dict()["coupled_events"][0]["event_status"])

hp=CoupledHypothesis("source-mass","add-E","Teacher atomic edits.",(
    CoupledPropertyEdit("field:Enew","field_v_m",(150.,0.,0.)),
    CoupledPropertyEdit("test-particle","mass_kg",2e-5),
))
pp=CoupledPhysicalPlan("review:physicalfail",model("uniform-edits"),(hp,))
cp=CoupledEventPlan(pp,(
    PlaneEvent("detector",(.006,0.,0.),(1.,0.,0.),"Passive x",direction=1),),
    EventPolicy(.003,1e-8,1e-8,1e-6))
native=run_coupled_physical_family(pp)
row=replace(native.entries[0],trajectory=None,comparisons=(),
            status="integration-failed",reason="controlled test-injected ordinary integration failure")
failed=CoupledPhysicalRun(native.plan,native.structural_run,(row,))
original_func=service.run_coupled_physical_family
try:
    service.run_coupled_physical_family=lambda plan: failed
    record("F03_FAILED_PHYSICAL_CHILD_REOBSERVED",lambda: {
        "physical_status": service.run_coupled_event_family(cp).children[0].physical_entry.status,
        "event_status": service.run_coupled_event_family(cp).children[0].status,
    })
finally:
    service.run_coupled_physical_family=original_func

Path("../first_attempt.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
