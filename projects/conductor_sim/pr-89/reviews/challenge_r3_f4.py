"""R3 reviewer-owned targeted F4 JSON integrity challenges, pinned to PR89.

This suite uses freshly generated CLI JSON and *genuine* native M16a traces.
Only the separate stdlib SI checker is used for hostile JSON verification.
No production code is modified. The separate R2 replay retains its own oracle.
"""
from __future__ import annotations
import ast
from copy import deepcopy
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import traceback

SOURCE = Path(sys.argv[1]).resolve()
OUT = Path(sys.argv[2]).resolve()
OUT.mkdir(parents=True, exist_ok=True)
sys.path[0:0] = [str(SOURCE / "src"), str(SOURCE)]
from conductor_sim import (ElectrostaticProblem, ExternalGroundedSphereBackend,
                           Grounded, Motion1DSpec, PointCharge, SolidSphere,
                           integrate_motion_1d, observe_grounded_sphere_motion)
from tools.m37a_ground_wire_reference import validate_examples

HEAD = "630f6d320a1b4cb00bf7bb0780cd3deca4ec0f7e"
TREE = "796f319edf5829455e842d9bad63b770d17ff9fa"
def git(*args):
    return subprocess.check_output(["git", "-C", str(SOURCE), *args], text=True).strip()

assert git("rev-parse", "HEAD") == HEAD, "stale candidate"
assert git("rev-parse", "HEAD^{tree}") == TREE, "stale Git tree"

# The offline SI checker must remain a self-contained stdlib calculation.
checker_path = SOURCE / "tools" / "m37a_ground_wire_reference.py"
checker = ast.parse(checker_path.read_text(encoding="utf-8"))
modules = []
for node in ast.walk(checker):
    if isinstance(node, ast.Import):
        modules += [x.name.split(".")[0] for x in node.names]
    if isinstance(node, ast.ImportFrom):
        modules.append((node.module or "").split(".")[0])
assert set(modules) <= {"__future__", "argparse", "json", "math", "pathlib"}, modules

cmd = [sys.executable, str(SOURCE / "examples/grounded_sphere_wire_current.py"),
       "--output", str(OUT / "genuine-duration-cli.json")]
generated = subprocess.run(cmd, cwd=SOURCE, capture_output=True, text=True, check=True)
(OUT / "genuine-cli-stdout.txt").write_text(generated.stdout, encoding="utf-8")
template = json.loads((OUT / "genuine-duration-cli.json").read_text(encoding="utf-8"))

def attach(motion, name):
    document = deepcopy(template)
    document["actual_elapsed_time"] = observe_grounded_sphere_motion(motion).as_dict()
    encoded = json.dumps(document, allow_nan=False)
    decoded = json.loads(encoded)
    (OUT / ("genuine-" + name + ".json")).write_text(
        json.dumps(decoded, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    return decoded

turn_problem = ElectrostaticProblem(
    (PointCharge(1e-9, (0., 0., .23)),),
    (SolidSphere(.08, Grounded(), name="Sphere A"),))
turn_motion = integrate_motion_1d(
    Motion1DSpec(turn_problem, 0, 1e-6, (0., 0., 1.), .01, .35, .005),
    ExternalGroundedSphereBackend())
assert turn_motion.termination == "duration"
assert any(e.kind == "turning-point" for e in turn_motion.events)

guard_problem = ElectrostaticProblem(
    (PointCharge(-1e-9, (0., 0., -.14)),),
    (SolidSphere(.1, Grounded(), name="Sphere A"),))
guard_motion = integrate_motion_1d(
    Motion1DSpec(guard_problem, 0, 1e-6, (0., 0., 1.), .35, .25, .01,
                 surface_guard_m=2e-4),
    ExternalGroundedSphereBackend())
assert guard_motion.termination == "surface-guard"
assert guard_motion.events[-1].time_s == guard_motion.samples[-1].time_s

GOOD = {"duration": template, "turning": attach(turn_motion, "turning"),
        "guarded": attach(guard_motion, "guarded")}
RESULTS = []

def record(name, expectation, outcome, reason="", additional=None):
    row = {"name": name, "expectation": expectation, "outcome": outcome, "reason": reason}
    if additional is not None:
        row["additional"] = additional
    RESULTS.append(row)
    print(json.dumps(row, sort_keys=True, default=str), flush=True)

for name, case in GOOD.items():
    try:
        response = validate_examples(case)
        expected = "surface-guard" if name == "guarded" else "duration"
        assert response["motion_termination"] == expected
        assert response["actual_time_samples"] == len(
            case["actual_elapsed_time"]["motion"]["samples"])
    except Exception as exc:
        record("genuine/" + name, "accept", "GENUINE_FAILED", repr(exc),
               traceback.format_exc())
    else:
        record("genuine/" + name, "accept", "PASS", additional=response)

def motion(d):
    return d["actual_elapsed_time"]["motion"]

def event_at(d, idx=2, kind="turning-point"):
    row = motion(d)["samples"][idx]
    return dict(kind=kind, time_s=row["time_s"],
                displacement_m=row["displacement_m"],
                position_m=deepcopy(row["position_m"]),
                description="Reviewer-created simulated event metadata")

def add_event(d, kind="turning-point", idx=2):
    motion(d)["events"].append(event_at(d, idx, kind))

def set_event(d, edit, base_row=2):
    e = event_at(d, base_row)
    edit(e)
    motion(d)["events"] = [e]

def add_two_out_of_order(d):
    motion(d)["events"] = [event_at(d, 3), event_at(d, 2)]

def guard_to_duration_without_erasing_event(d):
    motion(d)["termination"] = "duration"

def terminal_guard_with_consistent_moved_location(d):
    e = motion(d)["events"][-1]
    e["displacement_m"] -= .001
    e["position_m"][2] -= .001

def final_guard_not_last(d):
    last = motion(d)["events"][-1]
    motion(d)["events"].append(dict(
        kind="turning-point", time_s=last["time_s"],
        displacement_m=last["displacement_m"],
        position_m=deepcopy(last["position_m"]),
        description="Fabricated event after physical guard termination"))

def add_second_guard(d):
    motion(d)["events"].append(deepcopy(motion(d)["events"][-1]))

def edited(d, key, value):
    motion(d)[key] = value

# Name, baseline, a single mutation (except explicit combined falsification), intended error regex.
ATTACKS = [
    ("f4/false-max-1e9", "duration", lambda d: edited(d, "max_abs_energy_drift_j", 1e9), r"maximum absolute energy drift"),
    ("max/negative", "duration", lambda d: edited(d, "max_abs_energy_drift_j", -1), r"maximum absolute energy drift"),
    ("max/boolean", "duration", lambda d: edited(d, "max_abs_energy_drift_j", True), r"maximum absolute energy drift"),
    ("max/NaN", "duration", lambda d: edited(d, "max_abs_energy_drift_j", float("nan")), r"maximum absolute energy drift"),
    ("max/Infinity", "duration", lambda d: edited(d, "max_abs_energy_drift_j", float("inf")), r"maximum absolute energy drift"),
    ("max/false-zero", "duration", lambda d: edited(d, "max_abs_energy_drift_j", 0), r"maximum absolute energy drift"),
    ("f4/negative-guard", "duration", lambda d: edited(d, "guard_m", -.3), r"numerical conductor approach guard"),
    ("guard/zero", "duration", lambda d: edited(d, "guard_m", 0), r"numerical conductor approach guard"),
    ("guard/boolean", "duration", lambda d: edited(d, "guard_m", True), r"numerical conductor approach guard"),
    ("guard/NaN", "duration", lambda d: edited(d, "guard_m", float("nan")), r"numerical conductor approach guard"),
    ("guard/Infinity", "duration", lambda d: edited(d, "guard_m", float("inf")), r"numerical conductor approach guard"),
    ("guard/too-large-clearance", "duration", lambda d: edited(d, "guard_m", .15), r"motion sample crosses numerical sphere surface-approach guard"),
    ("events/not-list", "duration", lambda d: edited(d, "events", {}), r"motion event history must be a list"),
    ("events/null", "duration", lambda d: edited(d, "events", None), r"motion event history must be a list"),
    ("events/non-record", "duration", lambda d: edited(d, "events", ["junk"]), r"motion event must be a finite physical record"),
    ("events/bad-kind", "duration", lambda d: add_event(d, "teleportation"), r"unsupported physical kind"),
    ("events/boolean-kind", "duration", lambda d: add_event(d, True), r"unsupported physical kind"),
    ("events/negative-time", "duration", lambda d: set_event(d, lambda e: e.update(time_s=-.01)), r"motion event time"),
    ("events/future-time", "duration", lambda d: set_event(d, lambda e: e.update(time_s=99.)), r"motion event time"),
    ("events/boolean-time", "duration", lambda d: set_event(d, lambda e: e.update(time_s=True)), r"motion event time"),
    ("events/NaN-time", "duration", lambda d: set_event(d, lambda e: e.update(time_s=float("nan"))), r"motion event time"),
    ("events/out-of-order", "duration", add_two_out_of_order, r"motion event time"),
    ("events/boolean-displacement", "duration", lambda d: set_event(d, lambda e: e.update(displacement_m=True)), r"motion event displacement"),
    ("events/wrong-displacement", "duration", lambda d: set_event(d, lambda e: e.update(displacement_m=e["displacement_m"] + .03)), r"physical authored axis"),
    ("events/NaN-displacement", "duration", lambda d: set_event(d, lambda e: e.update(displacement_m=float("nan"))), r"motion event displacement"),
    ("events/nonaxial-position", "duration", lambda d: set_event(d, lambda e: e["position_m"].__setitem__(0, .01)), r"physical authored axis"),
    ("events/boolean-position", "duration", lambda d: set_event(d, lambda e: e["position_m"].__setitem__(2, True)), r"motion event position"),
    ("events/NaN-position", "duration", lambda d: set_event(d, lambda e: e["position_m"].__setitem__(2, float("nan"))), r"motion event position"),
    ("events/blank-description", "duration", lambda d: set_event(d, lambda e: e.update(description="  ")), r"motion event description"),
    ("events/guard-crossing", "duration", lambda d: set_event(d, lambda e: e.update(displacement_m=-.09999995, position_m=[0., 0., .10000005])), r"surface-approach guard"),
    ("f4/spurious-guard-on-duration", "duration", lambda d: add_event(d, "surface-guard"), r"duration-complete history contains an impossible surface-guard event"),
    ("termination/false-surface-label-no-event", "duration", lambda d: edited(d, "termination", "surface-guard"), r"exactly one final approach event"),
    ("termination/guard-claimed-duration-with-event", "guarded", guard_to_duration_without_erasing_event, r"duration-complete history contains an impossible surface-guard event"),
    ("guarded/missing-terminal-event", "guarded", lambda d: edited(d, "events", []), r"exactly one final approach event"),
    ("guarded/duplicate-terminal-event", "guarded", add_second_guard, r"exactly one final approach event"),
    ("guarded/terminal-event-not-last", "guarded", final_guard_not_last, r"exactly one final approach event"),
    ("guarded/wrong-terminal-time", "guarded", lambda d: motion(d)["events"][-1].__setitem__("time_s", motion(d)["events"][-1]["time_s"]-.00001), r"terminal surface-guard event time"),
    ("guarded/geometry-consistent-wrong-terminal-location", "guarded", terminal_guard_with_consistent_moved_location, r"terminal surface-guard displacement"),
]

def attack(name, base, edit, expected_error):
    bad = deepcopy(GOOD[base])
    try:
        edit(bad)
        # A real JSON parse (including permissive NaN parser behavior) precedes validation.
        bad = json.loads(json.dumps(bad, allow_nan=True))
        if "/" not in name:
            raise AssertionError("no namespace")
        outpath = OUT / "hostile" / (name.replace("/", "--") + ".json")
        outpath.parent.mkdir(parents=True, exist_ok=True)
        outpath.write_text(json.dumps(bad, indent=2, allow_nan=True) + "\n",
                           encoding="utf-8")
        validate_examples(bad)
    except ValueError as exc:
        if re.search(expected_error, str(exc), re.I):
            record(name, "reject", "REJECTED_AS_INTENDED", str(exc))
        else:
            record(name, "reject", "WRONG_REASON", str(exc), traceback.format_exc())
    except Exception as exc:
        record(name, "reject", "HARNESS_OR_EXECUTION_ERROR", repr(exc), traceback.format_exc())
    else:
        record(name, "reject", "UNEXPECTED_ACCEPTANCE", "no ValueError")

for (name, base, edit, reason) in ATTACKS:
    attack(name, base, edit, reason)

# Distinct documented proof ceiling: JSON export does not encode the original
# requested integration duration. Removal of the real final guard event plus
# a false 'duration' label makes an internally plausible but historically
# unproven statement; unlike original F4 this may be undecidable from JSON.
def elide_guard_history(d):
    m = motion(d)
    m["events"] = []
    m["termination"] = "duration"

candidate = deepcopy(GOOD["guarded"])
elide_guard_history(candidate)
try:
    result = validate_examples(json.loads(json.dumps(candidate, allow_nan=False)))
except ValueError as exc:
    record("proof-limit/stripped-guard-claimed-duration", "document-only",
           "REFUSED_BY_CHECKER", str(exc))
else:
    record("proof-limit/stripped-guard-claimed-duration", "document-only",
           "ACCEPTED_DOCUMENTED_LIMITATION",
           "no authored requested duration or original event provenance in schema",
           result)

# A turning event at t=0 with an explicitly nonzero initial velocity is a
# provably false local assertion, not an ODE-authenticity question. This probe
# tests whether the checker binds event semantics to a saved matching row.
def false_initial_turn(d):
    assert motion(d)["samples"][0]["velocity_m_s"] != 0
    motion(d)["events"].append(event_at(d, 0, "turning-point"))

attack("novel/false-initial-turn-with-nonzero-saved-velocity", "duration",
       false_initial_turn, r"turning|event|velocity|physical")

bad = [r for r in RESULTS if r["outcome"] not in
       ("PASS", "REJECTED_AS_INTENDED", "ACCEPTED_DOCUMENTED_LIMITATION",
        "REFUSED_BY_CHECKER")]
summary = {
    "source_head": git("rev-parse", "HEAD"),
    "source_tree": git("rev-parse", "HEAD^{tree}"),
    "python": sys.version, "num_attacks": len(ATTACKS) + 1,
    "num_genuine": len(GOOD), "num_records": len(RESULTS),
    "num_failures": len(bad),
    "offline_checker_imports": sorted(set(modules)),
    "actual_outcomes": RESULTS, "source_tracked_status":
        git("status", "--porcelain", "--untracked-files=no")
}
(OUT / "r3-f4-results.json").write_text(json.dumps(summary, indent=2, default=str)+"\n",
                                        encoding="utf-8")
print("CHAT_B_R3_F4_SUMMARY", json.dumps({k: v for k, v in summary.items()
                                        if k != "actual_outcomes"}), flush=True)
if bad or summary["source_tracked_status"]:
    sys.exit(1)
