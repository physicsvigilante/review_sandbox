"""M34a developer regression: exact historic graph v1/v2/v3 and M33b inquiry byte evidence.

Runs the SAME unchanged, already qualified historical M29a model under
independently checked-out old M33b and M34a Python source trees. All outputs
are detached genuine runner-issued native models, not imported JSON physics.
"""
from __future__ import annotations
import json

from conductor_sim import (
    GraphEventInquiryPlan, StructuralWorldNode, UnifiedObservationPlan,
    WorldComparison, run_graph_event_inquiry, run_unified_observation_graph,
)
from conductor_sim.motion_events import EventPolicy, PlaneEvent
from examples.m29a_structural_family import model


def main():
    family=model("uniform-edits")
    added=next(case for case in family.cases if case.case_id=="add-E")
    node=StructuralWorldNode("add-E","baseline",added)
    cases={}
    for mode,retain,compare in (
        ("v1",False,()),
        ("v2",True,()),
        ("v3",True,(WorldComparison("cross","baseline","add-E"),)),
    ):
        plan=UnifiedObservationPlan(
            "m34a:legacy-"+mode,family.baseline,(node,),
            retain_source_ancestry=retain,comparisons=compare)
        run=run_unified_observation_graph(plan)
        assert run.entries[0].status=="complete"
        assert run.entries[0].scenario.spec.plane_normal==family.baseline.spec.plane_normal
        cases[mode]=run.as_dict()
        if mode=="v3":
            detector=(PlaneEvent("x:new",(.006,0.,0.),(1.,0.,0.),
                       "New native typed detector",direction=1),)
            inquiry=GraphEventInquiryPlan(
                run,"m34a:legacy-new-events",("baseline","add-E"),
                detector,EventPolicy(.003,1e-8,1e-8,1e-6),
                (WorldComparison("followup","baseline","add-E"),))
            observation=run_graph_event_inquiry(inquiry)
            assert [entry.status for entry in observation.entries]==["complete","complete"]
            cases["m33b_inquiry"]=observation.as_dict()
    assert cases["v1"]["schema"]=="conductor_sim.unified_observation_graph.v1"
    assert cases["v2"]["schema"]=="conductor_sim.unified_observation_graph.v2"
    assert cases["v3"]["schema"]=="conductor_sim.unified_observation_graph.v3"
    assert cases["m33b_inquiry"]["schema"]=="conductor_sim.graph_event_inquiry.v1"
    print(json.dumps(cases,sort_keys=True,separators=(",",":"),allow_nan=False))


if __name__=="__main__":
    main()
