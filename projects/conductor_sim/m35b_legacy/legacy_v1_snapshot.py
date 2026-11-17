"""Generate genuine native M28a/M28b v1 legacy exports on either pinned checkout.

Do not import developer oracle values or substitute fake records. This script
only invokes old public solver APIs, with byte-identical comparison done by
a separate shell cmp on genuinely independent source revisions.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

import conductor_sim
from conductor_sim.event_sweep import EventSweepPlan, run_event_sweep
from conductor_sim.motion_events import PlaneEvent
from conductor_sim.trajectory_sweep import SweepAxis, TrajectorySweepPlan, run_trajectory_sweep
from examples.m28b_event_sweep import make_plan

def snapshot():
    items = {}
    for name in ("uniform-mass", "ring-detector", "gravity-guard", "multi-crossing"):
        plan=make_plan(name)
        items["M28b:"+name]=run_event_sweep(plan).as_dict()
        items["M28a:"+name]=run_trajectory_sweep(plan.sweep).as_dict()
    original=make_plan("uniform-mass")
    stop=PlaneEvent("stop:x", (.05,0.,0.), (1.,0.,0.),
                    "True terminal ideal stop surface",direction=1,
                    terminal=True,role="ideal-stop-surface")
    target=TrajectorySweepPlan(
        "m35b:terminal",original.sweep.baseline,
        SweepAxis("test-particle","position_m",((.06,0.,0.),(.01,0.,0.))))
    items["M28b:terminal"]=run_event_sweep(
        EventSweepPlan(target,(stop,),original.policy)).as_dict()
    return items

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--checkout-root",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    lib=Path(conductor_sim.__file__).resolve()
    expected=(args.checkout_root.resolve()/"src"/"conductor_sim")
    if expected not in lib.parents:
        raise AssertionError("native physics module loaded from wrong source root: "+str(lib))
    records=snapshot()
    assert len(records)==9 and all("entries" in x and "baseline_scenario" in x
                                   for x in records.values())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    data=json.dumps(records,sort_keys=True,separators=(",",":"),
                    ensure_ascii=True,allow_nan=False)+"\n"
    args.output.write_text(data,encoding="utf-8")
    print(json.dumps({
        "native_source_root":str(lib),
        "genuine_old_M28a_M28b_cases":len(records),
        "record_json_sha256":sha256(data.encode("utf-8")).hexdigest(),
        "status_by_case":{k:[e["status"] for e in v["entries"]]
                          for k,v in records.items()},
    },sort_keys=True))

if __name__=="__main__":
    main()
