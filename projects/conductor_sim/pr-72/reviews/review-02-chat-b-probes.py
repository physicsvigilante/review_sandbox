"""Independent Chat B R2 review #02 probes, exact source SHA 72c5f9ff... .

Execute on native, *unchanged* source via a source-pinned review_sandbox workflow.
No production source changes. Tests attack both the corrected narrow findings
and a possible unsealed physical-plan provenance boundary.
"""
from dataclasses import replace
from math import sqrt
from unittest.mock import patch
import json
import traceback
import sys

from conductor_sim import (
    CoupledPropertyEdit, CoupledHypothesis, CoupledPhysicalPlan,
    CoupledEventPlan, CoupledEventRun, run_coupled_event_family,
)
from conductor_sim.motion_events import EventPolicy, PlaneEvent
from conductor_sim.coupled_physical_family import (
    CoupledPhysicalRun, run_coupled_physical_family,
)
import conductor_sim.coupled_event_family as adapter
from examples.m29a_structural_family import model
from examples.m29b_structural_events import make_plan as m29b_plan
from examples.m31b_rod_reference import make_plan as rod_plan
from examples.m31b_coupled_events import example as event_example

OUTCOMES = {}
BLOCKERS = []


def record(label, outcome, detail=""):
    OUTCOMES[label] = dict(outcome=outcome, detail=str(detail))
    print(label, outcome, detail, flush=True)


def must_reject(label, action):
    try:
        output = action()
        if isinstance(output, CoupledEventRun):
            output.as_dict()
    except (ValueError, TypeError) as exc:
        record(label, "REJECTED", type(exc).__name__ + ": " + str(exc)[:140])
        return
    record(label, "ACCEPTED_UNEXPECTEDLY", "forged typed result and detached export accepted")
    BLOCKERS.append(label)


def check_narrow_integrity():
    genuine = run_coupled_event_family(rod_plan())
    parent, child = genuine.parents[0], genuine.children[0]
    assert parent.status == child.status == "complete"
    assert parent.event_run is not None and child.event_run is not None
    assert genuine.as_dict()["coupled_events"][0]["parent_event_time_comparisons"][0]["status"] == "one-resolved-pair"
    record("NATIVE_ROD_REFERENCE", "PASS", "genuine paired real M24a parent/child")

    root = child.event_run.events[0]
    delta = .030
    changed = replace(
        root,
        sample=replace(root.sample, time_s=root.sample.time_s + delta),
        time_bracket_s=tuple(t + delta for t in root.time_bracket_s),
    )
    forged_child = replace(child, event_run=replace(child.event_run, events=(changed,)))
    must_reject("F01_NEW_DIRECT_CONSTRUCTOR", lambda: CoupledEventRun(
        genuine.plan, genuine.physical_family, genuine.original_event_run,
        genuine.parents, (forged_child,)))
    must_reject("F01_COPY_ORIGINAL_SEAL", lambda: replace(genuine, children=(forged_child,)))
    # Even explicitly reusing the old, authentic original-issued seal must fail.
    must_reject("F01_EXPLICIT_OLD_SEAL", lambda: CoupledEventRun(
        genuine.plan, genuine.physical_family, genuine.original_event_run,
        genuine.parents, (forged_child,), genuine._observation_digest, genuine._issuer))

    fake_parent = replace(parent, event_run=None, status="rejected-event-study",
                          reason="pretend the actually observed parent refused")
    fake_child = replace(child, event_run=None, status="rejected-event-study",
                         reason="pretend the actually observed child refused")
    must_reject("F02_PARENT_MISSING_OBSERVATION", lambda: replace(genuine, parents=(fake_parent,)))
    must_reject("F02_CHILD_MISSING_OBSERVATION", lambda: replace(genuine, children=(fake_child,)))
    must_reject("F02_DIRECT_PARENT_OLD_SEAL", lambda: CoupledEventRun(
        genuine.plan, genuine.physical_family, genuine.original_event_run,
        (fake_parent,), genuine.children, genuine._observation_digest, genuine._issuer))
    must_reject("F02_DIRECT_CHILD_OLD_SEAL", lambda: CoupledEventRun(
        genuine.plan, genuine.physical_family, genuine.original_event_run,
        genuine.parents, (fake_child,), genuine._observation_digest, genuine._issuer))
    assert genuine.as_dict()["coupled_events"][0]["parent_event_time_comparisons"][0]["status"] == "one-resolved-pair"
    record("F02_AUTHENTIC_STAGES_RETAINED", "PASS")

    # Frozen outer dataclass can be overwritten by an abusive caller; export must check again.
    object.__setattr__(genuine, "children", (forged_child,))
    must_reject("F01_AFTER_CONSTRUCTION_EXPORT", lambda: genuine.as_dict())


def check_real_refusal():
    old = m29b_plan("terminal-refusal")
    phys = CoupledPhysicalPlan("review02:refusal", old.family, (
        CoupledHypothesis("correct-stop", "reversed-force", "Joint physical correction", (
            CoupledPropertyEdit("field:Eplus", "field_v_m", (500., 0., 0.)),
            CoupledPropertyEdit("test-particle", "mass_kg", 2e-6),
        )),))
    native = run_coupled_event_family(CoupledEventPlan(phys, old.questions, old.policy))
    p, c = native.parents[0], native.children[0]
    assert p.status == "rejected-event-study" and p.event_run is None and "initial release" in p.reason
    assert c.status == "complete" and c.event_run is not None
    assert c.physical_entry.status == "complete"
    assert native.as_dict()["coupled_events"][0]["parent_event_time_comparisons"][0]["status"] == "unpaired"
    record("F02_GENUINE_REFUSAL_PARENT_CHILD_SUCCEEDS", "PASS", p.reason[:160])


def check_failed_physical_sibling():
    asked = event_example("added-mass")
    h = asked.physical_plan.hypotheses[0]
    h2 = replace(h, case_id="real-sibling")
    physical_plan = replace(asked.physical_plan, hypotheses=(h, h2))
    plan = replace(asked, physical_plan=physical_plan)
    real = run_coupled_physical_family(physical_plan)
    assert len(real.entries) == 2 and all(e.trajectory is not None for e in real.entries)
    failed_entry = replace(real.entries[0], trajectory=None, comparisons=(),
                           status="integration-failed",
                           reason="Independent controlled test-injected M31a RK failure")
    injected = CoupledPhysicalRun(real.plan, real.structural_run, (failed_entry, real.entries[1]))
    genuine_observe = adapter._observe
    with patch.object(adapter, "run_coupled_physical_family", return_value=injected), \
         patch.object(adapter, "_observe", wraps=genuine_observe) as spy:
        observed = adapter.run_coupled_event_family(plan)
    assert len(observed.children) == 2
    first, sibling = observed.children
    assert first.physical_entry.scenario is failed_entry.scenario
    assert first.physical_entry.scenario is not None
    assert first.status == "integration-failed" and first.event_run is None
    assert sibling.status == "complete" and sibling.event_run is not None
    assert sibling.physical_entry.scenario is real.entries[1].scenario
    assert all(call.args[0] is not failed_entry.scenario for call in spy.call_args_list)
    assert len(spy.call_args_list) == 2, spy.call_args_list   # one parent, one successful sibling
    rows = observed.as_dict()["coupled_events"]
    assert rows[0]["physical_status"] == rows[0]["event_status"] == "integration-failed"
    assert rows[0]["event_run"] is None
    assert rows[0]["parent_event_time_comparisons"][0]["status"] == "unpaired"
    assert rows[1]["event_status"] == "complete" and rows[1]["event_run"] is not None
    record("F03_NO_RESCUE_VALID_SIBLING_PRESERVED", "PASS", "calls to M24a _observe=" + str(spy.call_count))
    attempted = replace(first, event_run=sibling.event_run, status="complete")
    must_reject("F03_FORGED_CHILD_EVENT_AT_CONSTRUCTOR", lambda: replace(
        observed, children=(attempted, sibling)))


def check_novel_analytic():
    phys = CoupledPhysicalPlan("review02:gravity", model("uniform-edits"), (
        CoupledHypothesis("gravity-field", "add-gravity",
            "Atomic gravity and y electric field re-authoring.", (
                CoupledPropertyEdit("gravity", "acceleration_m_s2", (0., -3.3, 0.)),
                CoupledPropertyEdit("field:Ey", "field_v_m", (0., 1750., 0.)),
            )),
    ))
    question = PlaneEvent("new-y-neg", (0., -.003, 0.), (0., 1., 0.),
                          "Passive y=-3mm signed downward plane", direction=-1)
    result = run_coupled_event_family(CoupledEventPlan(
        phys, (question,), EventPolicy(.001, 1e-8, 1e-9, 1e-7)))
    parent, child = result.parents[0], result.children[0]
    assert parent.status == child.status == "complete"
    assert child.physical_entry.scenario.parent_revision_id == parent.parent_scenario.revision_id
    expected = (sqrt(.006 / 1.995), sqrt(.006 / 3.125))
    times = []
    for name, item, t0 in zip(("parent", "child"), (parent, child), expected):
        assert item.event_run.trajectory.termination == "duration"
        roots = [e for e in item.event_run.events if e.event_id == "new-y-neg"]
        assert len(roots) == 1 and roots[0].direction == -1
        measured = roots[0].sample.time_s
        assert abs(measured - t0) < 1e-7, (name, measured, t0)
        times.append(measured)
    assert result.as_dict()["coupled_events"][0]["parent_event_time_comparisons"][0]["status"] == "one-resolved-pair"
    record("NOVEL_GRAVITY_EY_ANALYTIC_NATIVE", "PASS",
           "native_s=" + repr(times) + " analytic_s=" + repr(expected))


def check_unsealed_plan_provenance():
    """Try only exact built-in public dataclasses.replace, preserving unchanged receipt.

    The source scenario and native events remain original. We *do not* alter the
    digest, issuer, run objects, or private module functions.
    """
    genuine = run_coupled_event_family(event_example("added-mass"))
    old_h = genuine.plan.physical_plan.hypotheses[0]
    assert old_h.edits[0].value == (150., 0., 0.) and old_h.edits[1].value == 2e-5
    declared_wrong = replace(old_h, edits=(
        replace(old_h.edits[0], value=(175., 0., 0.)),
        replace(old_h.edits[1], value=3e-5),
    ))
    alt_plan = replace(genuine.plan.physical_plan, hypotheses=(declared_wrong,))
    alt_entry = replace(genuine.physical_family.entries[0], hypothesis=declared_wrong)
    alt_family = replace(genuine.physical_family, plan=alt_plan, entries=(alt_entry,))
    alt_asked = replace(genuine.plan, physical_plan=alt_plan)
    alt_child = replace(genuine.children[0], physical_entry=alt_entry)
    try:
        alleged = replace(genuine, plan=alt_asked, physical_family=alt_family,
                          children=(alt_child,))
        evidence = alleged.as_dict()
    except (ValueError, TypeError) as exc:
        record("F04_HYPOTHESIS_PROVENANCE_REBIND", "REJECTED",
               type(exc).__name__ + ": " + str(exc)[:160])
    else:
        asserted_edits = evidence["physical_model_family"]["entries"][0]["hypothesis"]["edits"]
        actual_scenario = evidence["physical_model_family"]["entries"][0]["revised_scenario"]
        assert asserted_edits[0]["value"] == [175., 0., 0.]
        assert asserted_edits[1]["value"] == 3e-5
        assert genuine.as_dict()["physical_model_family"]["entries"][0]["hypothesis"]["edits"][0]["value"] == [150., 0., 0.]
        assert actual_scenario == genuine.as_dict()["physical_model_family"]["entries"][0]["revised_scenario"]
        record("F04_HYPOTHESIS_PROVENANCE_REBIND", "ACCEPTED_UNEXPECTEDLY",
               "declared (Ey/Ex=175 V/m, mass=3e-5kg); native child scenario/trajectory "
               "remain 150 V/m and 2e-5kg; unchanged receipt accepted")
        BLOCKERS.append("F04_HYPOTHESIS_PROVENANCE_REBIND")
    # Less severe but related: retitle plan without changing the original
    # scenario, event study or receipt.
    try:
        relabeled_plan = replace(genuine.plan.physical_plan, plan_id="review02:foreign-plan")
        relabeled_family = replace(genuine.physical_family, plan=relabeled_plan)
        relabeled = replace(genuine,
            plan=replace(genuine.plan, physical_plan=relabeled_plan),
            physical_family=relabeled_family)
        rec = relabeled.as_dict()
    except (ValueError, TypeError) as exc:
        record("F04_PLAN_ID_REBIND", "REJECTED", type(exc).__name__ + ": " + str(exc)[:140])
    else:
        assert rec["plan_id"] == "review02:foreign-plan"
        record("F04_PLAN_ID_REBIND", "ACCEPTED_UNEXPECTEDLY",
               "top-level plan id relabeled with original native observations, receipt unchanged")
        BLOCKERS.append("F04_PLAN_ID_REBIND")


def main():
    checks = [
        ("F01_F02_NARROW", check_narrow_integrity),
        ("F02_REAL_REFUSAL", check_real_refusal),
        ("F03_SIBLING", check_failed_physical_sibling),
        ("NOVEL", check_novel_analytic),
        ("F04_UNSEALED", check_unsealed_plan_provenance),
    ]
    for label, check in checks:
        try:
            check()
        except Exception as exc:
            record(label, "PROBE_ERROR", repr(exc))
            traceback.print_exc()
            BLOCKERS.append(label + ":PROBE_ERROR")
    summary = dict(
        exact_source_sha="72c5f9ffc133da1db79b11c6ba878f95fb8d90c8",
        exact_source_tree="6033283cf38345abd2f2cace5cd7999997509984",
        outcomes=OUTCOMES, issues=BLOCKERS,
    )
    with open("../review02-results.json", "w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2, sort_keys=True, allow_nan=False)
    print("REVIEW02_FINAL_JSON", json.dumps(summary, sort_keys=True), flush=True)
    return int(bool(BLOCKERS))


if __name__ == "__main__":
    sys.exit(main())
