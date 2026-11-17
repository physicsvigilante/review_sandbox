"""M35b targeted physical compatibility: genuine integer-duration native clock.

The released M35a authored API accepts int duration_s=1. The original
integrator records the exact endpoint as int (not bool). A new evidence
validator must continue accepting this *genuine* native sample, while
rejecting Boolean False as a forged 0.0 sample.
"""
import argparse
from dataclasses import replace
import json
from pathlib import Path

from conductor_sim.event_sweep import EventSweepPlan, run_event_sweep
from conductor_sim.trajectory_sweep import SweepAxis, TrajectorySweepPlan, run_trajectory_sweep
from examples.m28b_event_sweep import make_plan


def actual_requests():
    old=make_plan("uniform-mass")
    base=replace(old.sweep.baseline, spec=replace(
        old.sweep.baseline.spec, duration_s=1))
    assert type(base.spec.duration_s) is int
    p=TrajectorySweepPlan("m35b:integer-duration",base,
        SweepAxis("test-particle","mass_kg",(.0005,)))
    return p,EventSweepPlan(p,old.questions,old.policy)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--expect",choices=("accepted","previous-overstrict"),required=True)
    args=ap.parse_args()
    t,e=actual_requests()
    try:
        motion=run_trajectory_sweep(t)
        events=run_event_sweep(e)
        assert type(motion.baseline_trajectory.samples[-1].time_s) is int
        assert type(motion.entries[0].trajectory.samples[-1].time_s) is int
        assert type(events.baseline_run.trajectory.samples[-1].time_s) is int
        assert type(events.entries[0].run.trajectory.samples[-1].time_s) is int
        assert motion.as_dict()["entries"][0]["status"]=="complete"
        assert events.as_dict()["entries"][0]["status"]=="complete"
    except ValueError as exc:
        if args.expect!="previous-overstrict" or "exact genuine types" not in str(exc):
            raise
        print(json.dumps(dict(result="REPRODUCED_M35B_REGRESSION",error=str(exc),
             status="previous candidate wrongly rejects legal integer endpoint"),sort_keys=True))
    else:
        if args.expect!="accepted":
            raise AssertionError("expected prior strict validator to falsely reject valid native int clock")
        print(json.dumps(dict(result="PASS",true_native_integer_endpoint=1,
            source_model="original M28b uniform-mass, valid authored int duration",
            genuine_models=2,actual_event_models=2),sort_keys=True))


if __name__=="__main__":
    main()
