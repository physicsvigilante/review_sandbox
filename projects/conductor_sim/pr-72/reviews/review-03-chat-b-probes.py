"""Chat B independent review #03: source-pinned F-04 provenance challenges.

This is newly authored review code for 7f52376...; not production code.
No caller may mint a trusted event receipt through a dataclass copy.
"""
from dataclasses import replace
import json
import sys
import traceback

from conductor_sim import CoupledEventRun, run_coupled_event_family
from conductor_sim.coupled_physical_family import run_coupled_physical_family
from examples.m31b_coupled_events import example

OUTCOMES = {}
FAILURES = []


def record(name, state, detail=""):
    OUTCOMES[name] = {"outcome": state, "detail": str(detail)}
    print(name, state, str(detail)[:240], flush=True)
    if state in ("ACCEPTED_UNEXPECTEDLY", "PROBE_ERROR", "FAILED"):
        FAILURES.append(name)


def expect_reject(name, action):
    try:
        observed = action()
        if isinstance(observed, CoupledEventRun):
            observed.as_dict()
    except (ValueError, TypeError) as exc:
        record(name, "REJECTED", type(exc).__name__ + ": " + str(exc))
    except Exception as exc:
        record(name, "PROBE_ERROR", repr(exc))
        traceback.print_exc()
    else:
        record(name, "ACCEPTED_UNEXPECTEDLY",
               "Unauthorised public construction and detached export accepted")


def rebind_hypothesis(native, hypothesis):
    """Keep ALL genuine source models, trajectories and M24a observations."""
    revised_plan = replace(native.plan.physical_plan, hypotheses=(hypothesis,))
    revised_entry = replace(native.physical_family.entries[0], hypothesis=hypothesis)
    revised_family = replace(native.physical_family, plan=revised_plan,
                             entries=(revised_entry,))
    revised_question = replace(native.plan, physical_plan=revised_plan)
    revised_child = replace(native.children[0], physical_entry=revised_entry)
    return revised_question, revised_family, revised_child


def run():
    original = run_coupled_event_family(example("added-mass"))
    baseline_record = original.as_dict()
    physical = baseline_record["physical_model_family"]
    entry = physical["entries"][0]
    hypothesis = original.plan.physical_plan.hypotheses[0]
    assert hypothesis.edits[0].value == (150., 0., 0.)
    assert hypothesis.edits[1].value == 2e-5
    assert physical == original.physical_family.as_dict()
    assert physical["plan_id"] == original.plan.physical_plan.plan_id
    assert entry["hypothesis"]["edits"][0]["value"] == [150., 0., 0.]
    assert entry["hypothesis"]["edits"][1]["value"] == 2e-5
    assert entry["parent_scenario"]["revision_id"]
    assert entry["revised_scenario"]["revision_id"]
    assert entry["revised_source_inventory"]
    assert entry["physical_trajectory"]["samples"]
    assert entry["exact_time_comparisons"] is not None
    assert physical["original_scenario"]["revision_id"]
    assert physical["structural_family"]
    assert baseline_record["coupled_events"][0]["event_status"] == "complete"
    assert original._observation_digest and original._issuer is not None
    record("AUTHENTIC_NATIVE_AND_FULL_M31A_RECORD", "PASS",
           "Original plan, child edits, identities, inventories, native trajectories and comparisons retained")

    wrong_edits = replace(hypothesis, edits=(
        replace(hypothesis.edits[0], value=(175., 0., 0.)),
        replace(hypothesis.edits[1], value=3e-5),
    ))
    amended_plan, amended_family, amended_child = rebind_hypothesis(
        original, wrong_edits)
    assert amended_family.entries[0].scenario is original.physical_family.entries[0].scenario
    assert amended_family.entries[0].trajectory is original.physical_family.entries[0].trajectory
    assert amended_child.event_run is original.children[0].event_run
    expect_reject("F04_DOUBLE_VALUE_COPY_OLD_RECEIPT",
                  lambda: replace(original, plan=amended_plan,
                                  physical_family=amended_family,
                                  children=(amended_child,)))
    expect_reject("F04_DOUBLE_VALUE_DIRECT_OLD_ISSUER_DIGEST",
                  lambda: CoupledEventRun(
                      amended_plan, amended_family, original.original_event_run,
                      original.parents, (amended_child,),
                      original._observation_digest, original._issuer))

    # Source-backed values are not frozen only at construction: export rechecks.
    altered_after = run_coupled_event_family(example("added-mass"))
    alt_plan, alt_family, alt_child = rebind_hypothesis(altered_after, wrong_edits)
    object.__setattr__(altered_after, "plan", alt_plan)
    object.__setattr__(altered_after, "physical_family", alt_family)
    object.__setattr__(altered_after, "children", (alt_child,))
    expect_reject("F04_DOUBLE_VALUE_POSTCONSTRUCTION_EXPORT",
                  altered_after.as_dict)

    changed_plan_id = replace(original.plan.physical_plan,
                              plan_id="review03:foreign-plan")
    changed_plan_family = replace(original.physical_family, plan=changed_plan_id)
    expect_reject("F04_FOREIGN_PLAN_ID",
                  lambda: replace(original,
                                  plan=replace(original.plan,
                                               physical_plan=changed_plan_id),
                                  physical_family=changed_plan_family))

    new_note = replace(hypothesis, note="Untrue educational explanation of physics.")
    nplan, nfamily, nchild = rebind_hypothesis(original, new_note)
    expect_reject("F04_HYPOTHESIS_NOTE",
                  lambda: replace(original, plan=nplan, physical_family=nfamily,
                                  children=(nchild,)))

    new_target = replace(hypothesis, edits=(
        replace(hypothesis.edits[0], component_id="field:otherE"),
        hypothesis.edits[1]))
    tplan, tfamily, tchild = rebind_hypothesis(original, new_target)
    expect_reject("F04_STABLE_COMPONENT_ID",
                  lambda: replace(original, plan=tplan, physical_family=tfamily,
                                  children=(tchild,)))

    new_property = replace(hypothesis, edits=(
        replace(hypothesis.edits[0], property_name="acceleration_m_s2"),
        hypothesis.edits[1]))
    pplan, pfamily, pchild = rebind_hypothesis(original, new_property)
    expect_reject("F04_EDIT_PROPERTY_NAME",
                  lambda: replace(original, plan=pplan, physical_family=pfamily,
                                  children=(pchild,)))

    new_case = replace(hypothesis, case_id="relabelled-case")
    cplan, cfamily, cchild = rebind_hypothesis(original, new_case)
    expect_reject("F04_CASE_ID",
                  lambda: replace(original, plan=cplan, physical_family=cfamily,
                                  children=(cchild,)))

    # Even an actual externally run NEW M31a family cannot issue M31b provenance.
    alternate_native_physical = run_coupled_physical_family(amended_plan.physical_plan)
    assert alternate_native_physical.entries[0].scenario is not None
    assert alternate_native_physical.entries[0].scenario.revision_id != (
        original.physical_family.entries[0].scenario.revision_id)
    modified_child = replace(original.children[0],
                             physical_entry=alternate_native_physical.entries[0])
    expect_reject("F04_REAL_OTHER_M31A_WITH_OLD_M24A_AND_RECEIPT",
                  lambda: CoupledEventRun(
                      amended_plan, alternate_native_physical,
                      original.original_event_run, original.parents,
                      (modified_child,), original._observation_digest,
                      original._issuer))

    # Changing source labels/membership and revised scenario without solving.
    entry_obj = original.physical_family.entries[0]
    annotated = entry_obj.scenario.source_annotations
    wrong_annotations = tuple(
        (identity, label + " review03-false" if i == 0 else label)
        for i, (identity, label) in enumerate(annotated))
    if wrong_annotations != annotated:
        fake_model = replace(entry_obj.scenario,
                             source_annotations=wrong_annotations)
        def changed_source_label():
            fake_entry = replace(entry_obj, scenario=fake_model)
            fake_family = replace(original.physical_family, entries=(fake_entry,))
            fake_child = replace(original.children[0], physical_entry=fake_entry)
            return replace(original, physical_family=fake_family,
                           children=(fake_child,))
        expect_reject("F04_REVISED_SOURCE_LABEL", changed_source_label)
    else:
        record("F04_REVISED_SOURCE_LABEL", "FAILED", "No source labels to challenge")

    expect_reject("NO_PUBLIC_UNISSUED_TYPED_CONSTRUCTION",
                  lambda: CoupledEventRun(
                      original.plan, original.physical_family,
                      original.original_event_run,
                      original.parents, original.children))
    expect_reject("DETACHED_JSON_NOT_A_TRUSTED_NATIVE_MODEL",
                  lambda: run_coupled_event_family(baseline_record))

    # The supported remedy is to ask the runner to solve the changed model.
    legitimate_alternative = run_coupled_event_family(amended_plan)
    new_doc = legitimate_alternative.as_dict()
    assert new_doc["physical_model_family"]["entries"][0]["hypothesis"]["edits"][0]["value"] == [175., 0., 0.]
    assert new_doc["physical_model_family"]["entries"][0]["hypothesis"]["edits"][1]["value"] == 3e-5
    assert new_doc["physical_model_family"]["entries"][0]["revised_scenario"]["revision_id"] != (
        entry["revised_scenario"]["revision_id"])
    assert legitimate_alternative._observation_digest != original._observation_digest
    record("FRESH_REAUTHOR_AND_GENUINE_NATIVE_REEXECUTION", "PASS",
           "Changed edits produce changed real source model and newly issued receipt")

    detached = original.as_dict()
    detached["physical_model_family"]["entries"][0]["hypothesis"]["edits"][0]["value"][0] = 999.
    assert original.as_dict()["physical_model_family"]["entries"][0]["hypothesis"]["edits"][0]["value"][0] == 150.
    record("DETACHED_JSON_CANNOT_MUTATE_ORIGINAL", "PASS")

    summary = {
        "actual_source_head": "7f52376c197d4667dba8c54463f995fce4d7df73",
        "actual_git_tree": "fe3df0fff668887d8f938b8be35ea124f6b22816",
        "outcomes": OUTCOMES, "failures": FAILURES
    }
    with open("../review03-results.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, sort_keys=True, indent=2, allow_nan=False)
    print("REVIEW03_FINAL_JSON", json.dumps(summary, sort_keys=True), flush=True)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except Exception as exc:
        record("UNCAUGHT_PROBE_ERROR", "PROBE_ERROR", repr(exc))
        traceback.print_exc()
        raise
