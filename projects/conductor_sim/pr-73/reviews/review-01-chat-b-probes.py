"""Separate-context Chat B R2: authored M32a native tests and independent SI references.

No production physics or event-locator functions are used to form reference
accelerations, trajectories, crossing times or expected source identities.
Run only against conductor_sim HEAD e62856dd... / tree b734f58....
"""
from dataclasses import replace
from math import sqrt
import json
from pathlib import Path
import sys

from conductor_sim import (
    CoupledPropertyEdit, PhysicalWorldNode, StructuralWorldNode,
    UnifiedObservationPlan, UnifiedObservationRun, UniformElectricField,
    UniformGravity, PointCharge, PrescribedField, TestChargeMotionSpec,
    run_unified_observation_graph,
)
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.structural_family import StructuralCase
from conductor_sim.structural_scenarios import NamedSource, SourceReplacement
from conductor_sim.motion_events import EventPolicy, PlaneEvent
from examples.m29a_structural_family import model
from examples.m29b_structural_events import make_plan


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def must_reject(label, fn, failures):
    try:
        fn()
    except (ValueError, TypeError):
        return "REJECTED"
    except Exception as exc:
        failures.append((label, "unexpected exception", type(exc).__name__, str(exc)))
        return "UNEXPECTED-EXCEPTION"
    failures.append((label, "accepted forged/unqualified evidence"))
    return "ACCEPTED"


def physical(id_, parent, *edits, mode="events"):
    return PhysicalWorldNode(
        id_, parent, "Independent reviewer SI edit and whole-world qualification.",
        tuple(CoupledPropertyEdit(*row) for row in edits), mode,
    )


def novel_world():
    # New teacher-authored ORIGINAL, not imported from the developer's demo.
    baseline = PrescribedScenario(
        "chatb:novel-original",
        TestChargeMotionSpec(
            PrescribedField((
                UniformElectricField((60., -80., 0.)),
                UniformElectricField((0., 70., 0.)),
            )),
            PointCharge(1.4e-9, (0., 0., 0.)),
            1.4e-5, (.13, .015, 0.), .04, .004,
            plane_normal=(0., 0., 1.),
            gravity=UniformGravity((0., -1.3, 0.)),
        ),
        (("field:A", "First independent held uniform field"),
         ("field:B", "Second independent held uniform field")),
        "Reviewer-authored static fields, uniform gravity, SI mass, charge and launch.",
    )
    add = StructuralCase(
        "add-diag", "Add a third diagonal source; no time-varying held charge.",
        add_sources=(NamedSource(
            "field:C", "New signed diagonal field",
            UniformElectricField((130., -230., 0.)),
        ),),
    )
    swap = StructuralCase(
        "swap-diag", "Replace C with distinct C2 identity.",
        replace_sources=(SourceReplacement(
            "field:C", NamedSource(
                "field:C2", "Replacement source",
                UniformElectricField((190., -90., 0.)),
            ),
        ),),
    )
    resurrect = StructuralCase(
        "resurrect", "Try to illegally reuse retired source C.",
        add_sources=(NamedSource(
            "field:C", "Illegally reused retired identity",
            UniformElectricField((25., 20., 0.)),
        ),),
    )
    remove = StructuralCase(
        "remove-B", "Remove independent original B source.",
        remove_sources=("field:B",),
    )
    nodes = (
        StructuralWorldNode("add-diag", "baseline", add, "events"),
        StructuralWorldNode("swap-diag", "add-diag", swap, "events"),
        StructuralWorldNode("resurrect", "swap-diag", resurrect, "trajectory"),
        physical("joint-atomic", "swap-diag",
                 ("field:C2", "field_v_m", (250., -140., 0.)),
                 ("test-particle", "mass_kg", 1.9e-5)),
        physical("follow-velocity", "joint-atomic",
                 ("test-particle", "initial_velocity_m_s", (.18, .01, 0.))),
        StructuralWorldNode("remove-B", "baseline", remove, "trajectory"),
        physical("sibling-event", "remove-B",
                 ("test-particle", "mass_kg", 2.2e-5)),
    )
    question = PlaneEvent(
        "x:gate", (.0025, 0., 0.), (1., 0., 0.),
        "Reviewer positive-x plane crossing", direction=1,
    )
    plan = UnifiedObservationPlan(
        "chatb:novel-graph", baseline, nodes, "events", (question,),
        EventPolicy(.008, 1e-8, 1e-8, 1e-7),
    )
    return plan


def independent_reference(run):
    # All expected E, mass, velocities below are independently transcribed
    # from the newly authored model above, not from output or solver callbacks.
    q = 1.4e-9
    states = {
        "baseline": (60., -10., 1.4e-5, .13, .015, "events"),
        "add-diag": (190., -240., 1.4e-5, .13, .015, "events"),
        "swap-diag": (250., -100., 1.4e-5, .13, .015, "events"),
        "joint-atomic": (310., -150., 1.9e-5, .13, .015, "events"),
        "follow-velocity": (310., -150., 1.9e-5, .18, .01, "events"),
        "remove-B": (60., -80., 1.4e-5, .13, .015, "trajectory"),
        "sibling-event": (60., -80., 2.2e-5, .13, .015, "events"),
    }
    by_id = {"baseline": run.baseline_native}
    by_id.update({entry.node.node_id: entry.native for entry in run.entries})
    comparisons = {}
    for name, (ex, ey, mass, vx, vy, mode) in states.items():
        native = by_id[name]
        check(native is not None, name + ": missing native observation")
        traj = native.trajectory if mode == "events" else native
        check(traj.termination == "duration", name + ": truncated native history")
        ax, ay = q*ex/mass, q*ey/mass - 1.3
        max_state_error_m = 0.
        max_velocity_error_m_s = 0.
        max_force_error_n = 0.
        for sample in traj.samples:
            t = sample.time_s
            expected_r = (vx*t + .5*ax*t*t, vy*t + .5*ay*t*t, 0.)
            expected_v = (vx+ax*t, vy+ay*t, 0.)
            expected_f = (q*ex, q*ey-1.3*mass, 0.)
            max_state_error_m = max(max_state_error_m,
                 *(abs(a-b) for a,b in zip(sample.position_m,expected_r)))
            max_velocity_error_m_s = max(max_velocity_error_m_s,
                 *(abs(a-b) for a,b in zip(sample.velocity_m_s,expected_v)))
            max_force_error_n = max(max_force_error_n,
                 *(abs(a-b) for a,b in zip(sample.force_n,expected_f)))
        check(max_state_error_m < 3e-7, name + ": state differs from Newton reference")
        check(max_velocity_error_m_s < 3e-5, name + ": velocity differs from Newton reference")
        check(max_force_error_n < 5e-11, name + ": force differs from qE+mg")
        record = {
            "saved_points": len(traj.samples),
            "max_position_error_m": max_state_error_m,
            "max_velocity_error_m_s": max_velocity_error_m_s,
            "max_force_error_n": max_force_error_n,
            "reference_acceleration_m_s2": [ax, ay, 0.],
        }
        if mode == "events":
            roots = [root for root in native.events if root.event_id == "x:gate"]
            check(len(roots) == 1, name + ": not one signed event root")
            root = roots[0]
            check(root.direction == 1, name + ": wrong signed crossing")
            # Stable positive quadratic root; never invoke production field/RK.
            t_ref = .005 / (vx + sqrt(vx*vx + 2*ax*.0025))
            check(abs(root.sample.time_s - t_ref) < 5e-7,
                  name + ": native event differs from analytic root")
            record["reference_root_s"] = t_ref
            record["native_root_s"] = root.sample.time_s
            record["event_time_error_s"] = root.sample.time_s - t_ref
        comparisons[name] = record
    return comparisons


def other_event_challenges():
    # Original negative uniform electric field, two real opposite-sign roots.
    baseline = PrescribedScenario(
        "chatb:two-crossing-original",
        TestChargeMotionSpec(
            PrescribedField((UniformElectricField((-9000., 0., 0.)),)),
            PointCharge(1e-9, (0., 0., 0.)), 1e-5,
            (.1, 0., 0.), .22, .01, plane_normal=(0., 0., 1.),
        ),
        (("field:brake", "Reviewer authored uniform retarding field"),),
        "Independent review: signed double crossing under constant deceleration.",
    )
    q = PlaneEvent(
        "x:twice", (.003, 0., 0.), (1., 0., 0.),
        "Bidirectional positive/negative passage", direction=0,
    )
    plan = UnifiedObservationPlan(
        "chatb:double", baseline,
        (physical("stronger-brake", "baseline",
                  ("field:brake", "field_v_m", (-10000., 0., 0.))),),
        "events", (q,), EventPolicy(.01, 1e-8, 1e-8, 1e-7),
    )
    run = run_unified_observation_graph(plan)
    check(run.baseline_status == "complete" and run.entries[0].status == "complete",
          "double crossing did not integrate completely")
    doubled = {}
    for tag, native, a in (
        ("baseline", run.baseline_native, -.9),
        ("child", run.entries[0].native, -1.),
    ):
        roots = [root for root in native.events if root.event_id == "x:twice"]
        check(len(roots) == 2, tag + ": expected two genuine roots")
        check([r.direction for r in roots] == [1, -1],
              tag + ": opposite directions not retained")
        # Solve .003 = .1*t + .5*a*t^2 independently.
        discriminant = .1*.1 + 2*a*.003
        expected = [(-.1+sqrt(discriminant))/a,
                    (-.1-sqrt(discriminant))/a]
        errs = [r.sample.time_s - t for r,t in zip(roots,expected)]
        check(max(abs(e) for e in errs) < 5e-7, tag + ": root/reference disagreement")
        doubled[tag] = {"native_roots_s":[r.sample.time_s for r in roots],
                        "reference_roots_s":expected,
                        "signed_directions":[r.direction for r in roots],
                        "errors_s":errs}
    pair = run.as_dict()["nodes"][0]["parent_event_time_comparisons"][0]
    check(pair["status"] == "unpaired" and "estimated_numerical_shift_s" not in pair,
          "double crossing silently invented unique shift")
    return doubled


def parent_rejection_challenge():
    prior = make_plan("terminal-refusal")
    family = prior.family
    invalid = family.cases[0]
    q = prior.questions
    p = UnifiedObservationPlan(
        "chatb:parent-rejection", family.baseline, (
            StructuralWorldNode("reversed-force", "baseline", invalid, "events"),
            physical("correct-child", "reversed-force",
                     ("field:Eplus", "field_v_m", (500., 0., 0.)),
                     ("test-particle", "mass_kg", 2e-6)),
        ), "events", q, prior.policy,
    )
    run = run_unified_observation_graph(p)
    parent, child = run.entries
    check(parent.scenario is not None and parent.native is None
          and parent.status == "rejected-event-study", "event-study refusal lost")
    check(child.status == "complete" and child.native is not None,
          "qualified physical child was incorrectly suppressed")
    check(child.scenario.parent_revision_id == parent.scenario.revision_id,
          "child has wrong physical parent")
    pair = run.as_dict()["nodes"][1]["parent_event_time_comparisons"][0]
    check(pair["status"] == "unpaired", "refused parent got invented event shift")
    return {"parent_status": parent.status, "child_status": child.status,
            "child_parent_revision_id": child.scenario.parent_revision_id,
            "pair_status":pair["status"]}



def source_guard_challenge():
    # Deliberately reuse a baseline guarded physical setup only; this is a NEW
    # independently selected graph composition and its assertions.
    from examples.m29a_structural_family import model
    fam=model("guard-and-refusal")
    new_source=StructuralCase(
        "independent-guard",
        "Chat B authored attracting held charge inside physical time horizon.",
        add_sources=(NamedSource(
            "point:reviewer-attract", "New strongly attractive fixed point",
            __import__("conductor_sim", fromlist=["FixedPointField"]).FixedPointField(
                -1e-10, (.2,0.,0.)),
        ),),
    )
    events = (
        PlaneEvent("first", (.05,0.,0.), (1.,0.,0.),
                   "Earlier positive x crossing", direction=1),
        PlaneEvent("beyond", (.22,0.,0.), (1.,0.,0.),
                   "Unobserved detector beyond source guard", direction=1),
    )
    p=UnifiedObservationPlan(
        "chatb:guarded",fam.baseline,
        (StructuralWorldNode("independent-guard","baseline",new_source,"events"),),
        "events",events,EventPolicy(.007,1e-8,1e-7,1e-6),
    )
    result=run_unified_observation_graph(p)
    child=result.entries[0]
    check(child.status=="censored-source-guard","source guard not classified")
    d=child.native.as_dict()
    check(d["outcomes"]["first"]=="located","pre-guard root lost")
    check(d["outcomes"]["beyond"]=="search-truncated",
          "after-guard detector falsely resolved or absent")
    pairs=result.as_dict()["nodes"][0]["parent_event_time_comparisons"]
    check(all(x["status"]=="unpaired" for x in pairs),
          "guard event shift was improperly claimed")
    check(all("estimated_numerical_shift_s" not in x for x in pairs),
          "guard event shift carries fabricated numeric time")
    return {"status":child.status, "outcomes":d["outcomes"],
            "pair_statuses":[x["status"] for x in pairs],
            "last_saved_time_s":child.native.trajectory.samples[-1].time_s}

def attack_evidence(run, errors):
    attacks = {}
    def probe(label, fn):
        attacks[label] = must_reject(label, fn, errors)
    plan = run.plan
    entry = run.entries[0]
    probe("direct_construction_without_receipt", lambda: UnifiedObservationRun(
        run.plan, run.baseline_native, run.baseline_status,
        run.baseline_reason, run.entries))
    probe("old_receipt_reused_for_changed_status", lambda: replace(
        run, baseline_status="integration-failed"))
    probe("altered_plan_id", lambda: replace(
        run, plan=replace(plan, plan_id="chatb:fake-author")))
    tampered = replace(entry.node.case, note="Invented structural rationale.")
    bad_node = replace(entry.node, case=tampered)
    changed_plan = replace(plan, nodes=(bad_node,) + plan.nodes[1:])
    probe("altered_original_structural_hypothesis", lambda: replace(
        run, plan=changed_plan,
        entries=(replace(entry, node=bad_node),)+run.entries[1:]))
    bogus = replace(entry, status="integration-failed", native=None,
                    reason="fabricated numerical rejection")
    probe("fabricated_refusal", lambda: replace(
        run, entries=(bogus,)+run.entries[1:]))
    root = entry.native.events[0]
    shifted = replace(root, sample=replace(root.sample, time_s=root.sample.time_s+.03),
                      time_bracket_s=tuple(t+.03 for t in root.time_bracket_s))
    probe("fabricated_root_and_bracket", lambda: replace(
        run, entries=(replace(entry, native=replace(entry.native, events=(shifted,))),)
            +run.entries[1:]))
    false_clock = replace(root, sample=replace(root.sample, time_s=False))
    probe("boolean_clock", lambda: replace(
        run, entries=(replace(entry, native=replace(entry.native,
            events=(false_clock,))),) + run.entries[1:]))
    altered_child = replace(plan.nodes[3], edits=(
        replace(plan.nodes[3].edits[0], value=(320., -140., 0.)),
        plan.nodes[3].edits[1],
    ))
    probe("forged_atomic_physical_edit", lambda: replace(
        run, plan=replace(plan, nodes=plan.nodes[:3]+(altered_child,)+plan.nodes[4:]),
        entries=run.entries[:3]+(replace(run.entries[3], node=altered_child),)
            +run.entries[4:]))
    probe("structural_after_physical_rejected", lambda: UnifiedObservationPlan(
        "chatb:wrong-edge", plan.original, (
            physical("mass-first", "baseline", ("test-particle", "mass_kg", 2e-5)),
            StructuralWorldNode("add-diag", "mass-first", plan.nodes[0].case),
        ), "events", plan.questions, plan.policy))
    doc = run.as_dict()
    doc["nodes"][0]["status"] = "INVENTED"
    check(run.as_dict()["nodes"][0]["status"] == "complete",
          "detached JSON unexpectedly mutated native result")
    second = run_unified_observation_graph(plan)
    object.__setattr__(second, "baseline_reason", "invented after construction")
    probe("postconstruction_export", second.as_dict)
    return attacks


def main(output):
    errors = []
    plan = novel_world()
    run = run_unified_observation_graph(plan)
    check(run.baseline_status == "complete", "novel baseline is not complete")
    expected = ["complete", "complete", "rejected-structural-model",
                "complete", "complete", "complete", "complete"]
    actual = [entry.status for entry in run.entries]
    check(actual == expected, "novel graph statuses wrong: "+str(actual))
    rows = run.as_dict()["nodes"]
    check(run.entries[1].assembly.parent is run.entries[0].assembly,
          "nested structural ancestry lost")
    check(run.entries[3].scenario.parent_revision_id
          == run.entries[1].scenario.revision_id,
          "joint atomic revision attached to wrong real parent")
    check(run.entries[4].scenario.parent_revision_id
          == run.entries[3].scenario.revision_id,
          "physical-after-physical lost real parent")
    check([s for s,_ in run.entries[1].scenario.source_annotations]
          == ["field:A","field:B","field:C2"], "retired/new IDs incorrect")
    check(run.entries[2].scenario is None and run.entries[2].native is None,
          "retired ID wrongly resurrected")
    check(rows[6]["parent_event_time_comparisons"][0]["status"] == "unpaired",
          "mixed-mode parent created fake numerical shift")
    check(rows[3]["parent_event_time_comparisons"][0]["status"] == "one-resolved-pair",
          "genuine same-signed event parent/child pair lost")
    analytic = independent_reference(run)
    crossings = other_event_challenges()
    guard = source_guard_challenge()
    parent = parent_rejection_challenge()
    attacks = attack_evidence(run, errors)
    check(not errors, "adversarial probes: "+str(errors))
    result = {
        "reviewer": "separate-context Chat B",
        "source_head": "e62856ddcee5cdc2cae30cbaf3122d4d93e3a04a",
        "git_tree": "b734f58ef92d5b4d7832f1a25d8457d65fbe5bf9",
        "verdict": "PASS_NEW_REVIEWER_PROBES_ONLY",
        "statuses": actual,
        "real_parent_ids": [e.node.parent_id for e in run.entries],
        "analytic_3d_uniform_gravity": analytic,
        "double_crossing": crossings,
        "source_guard": guard,
        "parent_refusal_child_success": parent,
        "attacks": attacks,
        "errors": errors,
        "source_evidence_schema": run.as_dict()["schema"],
    }
    Path(output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",
                            encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv)>1 else "../review01-native-evidence.json")
