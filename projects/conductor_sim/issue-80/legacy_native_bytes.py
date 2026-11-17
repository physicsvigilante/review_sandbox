"""M35b original M28a/M28b real source output archive for byte identity.

This script is executed in two SEPARATE checkouts (released M35a, M35b).
It has no custom physics or synthetic JSON, and calls the actual old native
M20b/M19/M24a runners. Only historical schema records are compared.
"""
from __future__ import annotations
import argparse
from hashlib import sha256
import json
from pathlib import Path

from conductor_sim import run_trajectory_sweep, run_event_sweep
from examples.m28b_event_sweep import make_plan

CASE_NAMES = ("uniform-mass","ring-detector","multi-crossing","gravity-guard")


def main():
    a=argparse.ArgumentParser()
    a.add_argument("--output",type=Path,required=True)
    args=a.parse_args()
    out={}
    for name in CASE_NAMES:
        plan=make_plan(name)
        sweeps=(("trajectory",run_trajectory_sweep(plan.sweep)),
                ("events",run_event_sweep(plan)))
        for kind,native in sweeps:
            key=f"{kind}-{name}"
            # Prove this output truly came from a native typed M28a/M28b run.
            if kind=="events":
                assert native.baseline_run.study.scenario is native.plan.sweep.baseline
                assert len(native.entries)==len(native.plan.sweep.axis.values)
            else:
                assert native.baseline_trajectory.spec is native.plan.baseline.spec
            record=native.as_dict()
            assert record["schema"]==f"conductor_sim.{'event' if kind=='events' else 'trajectory'}_sweep.v1"
            out[key]=record
    payload=json.dumps(out,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n"
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(payload,encoding="utf-8")
    print(json.dumps(dict(records=len(out),bytes=len(payload.encode()),
        sha256=sha256(payload.encode()).hexdigest(),
        categories={key: [row["status"] for row in value["entries"]]
                    for key,value in out.items()}),sort_keys=True))


if __name__=="__main__":
    main()
