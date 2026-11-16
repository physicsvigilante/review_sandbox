"""M30a pre-review exact-source native transfer + independent SI numerical reference.

This is DEV-AUTHORED supplementary CI evidence, not an independent Chat B
verdict. All M30a assembly/integration/lineage operations call the frozen
conductor_sim source. The numerical comparator independently computes
Coulomb point fields + 96-node Gauss-Legendre rod quadrature and integrates
the force equation using SciPy DOP853; native trajectories are not fed to it.
"""
from __future__ import annotations

import hashlib
import json
from math import pi
from pathlib import Path
import subprocess

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp

from conductor_sim import (
    BranchSweep, FixedPointField, PointCharge, PrescribedField, StructuralParameterPlan,
    SweepAxis, TestChargeMotionSpec, UniformGravity, UniformRodField,
    run_structural_parameter_family,
)
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.structural_family import StructuralCase, StructuralFamilyPlan
from conductor_sim.structural_scenarios import NamedSource

PINNED_SOURCE = "4d22b6966cfe2e704d26df8438c35bb22f2662f7"
PINNED_TREE = "4b9b28f593c3d64bb07e71f339db12c480c449ea"
Q_PROBE, MASS = 8e-10, 9e-6
ROD_Q = 2.8e-9
ROD_A = np.array((.095, -.08, 0.), dtype=float)
ROD_B = np.array((.14, .11, 0.), dtype=float)
HELD = (
    (1.3e-9, (.19, .14, 0.)),
    (-.8e-9, (-.17, .09, 0.)),
)
NEW_POS = (.18, -.085, 0.)
PARENT_NEW_Q = 1.5e-9
VARIANT_Q = (.6e-9, 2.4e-9)
G = np.array((0., -.08, 0.))
Y0 = np.array((0., 0., 0., .045, .016, 0.), dtype=float)
DURATION = .42


def require(value, msg):
    if not value:
        raise AssertionError(msg)


def author():
    original = PrescribedScenario(
        "m30a:transfer-original",
        TestChargeMotionSpec(
            PrescribedField((
                UniformRodField(ROD_Q, tuple(map(float, ROD_A)), tuple(map(float, ROD_B))),
                FixedPointField(HELD[0][0], HELD[0][1]),
                FixedPointField(HELD[1][0], HELD[1][1]),
            )),
            PointCharge(Q_PROBE, (0., 0., 0.)),
            MASS,
            (.045, .016, 0.),
            DURATION,
            .0042,
            plane_normal=(0., 0., 1.),
            relative_tolerance=2e-9,
            gravity=UniformGravity((0., -.08, 0.)),
            source_guard_m=.001,
        ),
        (
            ("rod:slant", "Tilted held finite rod"),
            ("point:upper", "Held +1.3 nC original point"),
            ("point:lower", "Held -0.8 nC original point"),
        ),
        "Independent-authored teaching hypothesis: no metal response or source motion.",
    )
    cases = (
        StructuralCase(
            "added-point", "Add an independent held point; vary its charge later.",
            add_sources=(NamedSource(
                "point:added", "New held adjustable positive charge",
                FixedPointField(PARENT_NEW_Q, NEW_POS)),),
        ),
        StructuralCase(
            "bad-offplane", "Attempt one unpaired out-of-plane held point.",
            add_sources=(NamedSource(
                "point:unpaired", "Unpaired off-plane held point",
                FixedPointField(1e-9, (.15, .05, .08))),),
        ),
    )
    family = StructuralFamilyPlan("m30a:transfer-worlds", original, cases)
    return StructuralParameterPlan(
        "m30a:transfer-experiment", family, (
            BranchSweep("added-point", SweepAxis("point:added", "charge_c", VARIANT_Q)),
            BranchSweep("bad-offplane", SweepAxis("point:unpaired", "charge_c", (2e-9,))),
            BranchSweep("baseline", SweepAxis("point:added", "charge_c", (.6e-9,))),
        ),
    )


def reference(charge_added, query_t):
    """No import, field, integration or state data from the native engine."""
    k = 1 / (4 * pi * 8.8541878128e-12)
    nodes, weights = leggauss(96)
    rod_sites = ROD_A[None, :] + ((nodes + 1) / 2)[:, None] * (
        ROD_B - ROD_A)[None, :]
    fixed = list(HELD)
    if charge_added is not None:
        fixed.append((charge_added, NEW_POS))

    def electric_field(pos):
        diff = pos[None, :] - rod_sites
        norms = np.linalg.norm(diff, axis=1)
        total = k * ROD_Q * np.sum(
            (weights / (2 * norms ** 3))[:, None] * diff, axis=0)
        for q, loc in fixed:
            d = pos - np.asarray(loc, dtype=float)
            total += k * q * d / np.linalg.norm(d) ** 3
        return total

    def rhs(_t, state):
        pos, vel = state[:3], state[3:]
        return np.concatenate((vel, Q_PROBE / MASS * electric_field(pos) + G))

    solution = solve_ivp(
        rhs, (0, DURATION), Y0, method="DOP853",
        rtol=2e-12, atol=1e-14, max_step=.001, dense_output=True,
    )
    require(solution.success, "independent SciPy DOP853 integration failed")
    query_t = np.asarray(query_t, dtype=float)
    states = solution.sol(query_t).T
    forces = np.array([
        Q_PROBE * electric_field(state[:3]) + MASS * G for state in states
    ])
    return states, forces


def validate_sampled_run(named, native, charge_added):
    require(native.termination == "duration", named + ": not duration-complete")
    rows = native.samples
    require(len(rows) == 101, named + ": expected 101 original native saved samples")
    times = [x.time_s for x in rows]
    require(times[0] == 0 and abs(times[-1] - DURATION) < 1e-14,
            named + ": incorrect saved physical time span")
    require(all(a < b for a, b in zip(times, times[1:])),
            named + ": nonmonotone physical timestamps")
    ref_state, ref_force = reference(charge_added, times)
    native_state = np.array([
        [*r.position_m, *r.velocity_m_s] for r in rows
    ])
    native_force = np.array([r.force_n for r in rows])
    abs_position = float(np.max(np.linalg.norm(
        native_state[:, :3] - ref_state[:, :3], axis=1)))
    abs_velocity = float(np.max(np.linalg.norm(
        native_state[:, 3:] - ref_state[:, 3:], axis=1)))
    abs_force = float(np.max(np.linalg.norm(native_force - ref_force, axis=1)))
    # Resolved SI checks, not error bounds on exact ODE solutions.
    require(abs_position <= 4e-7, named + ": independent position disagreement")
    require(abs_velocity <= 3e-6, named + ": independent velocity disagreement")
    require(abs_force <= 1e-10, named + ": independent force disagreement")
    require(max(abs(r.position_m[2]) for r in rows) < 1e-12,
            named + ": plane-preservation failed")
    return {
        "name": named, "added_source_charge_c": charge_added,
        "saved_count": len(rows), "last_time_s": times[-1],
        "max_3d_position_error_m": abs_position,
        "max_3d_velocity_error_m_s": abs_velocity,
        "max_3d_total_force_error_n": abs_force,
        "native_final_position_m": list(rows[-1].position_m),
        "independent_final_position_m": ref_state[-1, :3].tolist(),
        "native_final_velocity_m_s": list(rows[-1].velocity_m_s),
        "independent_final_velocity_m_s": ref_state[-1, 3:].tolist(),
    }


def main():
    root = Path(__file__).resolve().parents[4]
    native_source = root / "native_source"
    head = subprocess.check_output(
        ["git", "-C", str(native_source), "rev-parse", "HEAD"],
        text=True).strip()
    tree = subprocess.check_output(
        ["git", "-C", str(native_source), "rev-parse", "HEAD^{tree}"],
        text=True).strip()
    require(head == PINNED_SOURCE and tree == PINNED_TREE,
            "native source commit/tree are not the frozen reviewed candidate")
    output = root / "m30a-transfer-output"
    output.mkdir(exist_ok=True, parents=True)

    plan = author()
    before = plan.family.baseline.as_dict()
    run = run_structural_parameter_family(plan)
    detached = run.as_dict()
    require(before == plan.family.baseline.as_dict(), "original physical model mutated")
    require(detached["original_revision_id"] == before["revision_id"],
            "original source identity lost")
    require([entry.status for entry in run.entries] == [
        "evaluated", "skipped-structural-model", "rejected-sweep-axis"],
        "refusal stages were conflated or valid branch was not solved")

    new_world = run.entries[0]
    parent = new_world.parent_scenario
    assembly = new_world.structural_entry.assembly
    require(assembly.parent is plan.family.baseline, "source child not from original world")
    require(assembly.as_dict()["parent_revision_id"] == before["revision_id"],
            "source assembly parent SHA incorrect")
    require(assembly.as_dict()["child_revision_id"] == parent.revision_id,
            "source assembly child SHA incorrect")
    require([x["operation"] for x in assembly.changes] == ["add-source"],
            "source assembly altered anything other than the named held point")
    require([x["id"] for x in detached["entries"][0]["source_inventory"]] == [
        "rod:slant", "point:upper", "point:lower", "point:added"],
        "original source names/identities not retained on new world")
    require([c.status for c in new_world.sweep_run.entries] == [
        "complete", "complete"], "parameter grandchildren were not both solved")
    require(new_world.sweep_run.baseline_trajectory.as_dict() ==
            new_world.structural_entry.trajectory.as_dict(),
            "same structural parent reintegration changed saved results")
    for charge, child in zip(VARIANT_Q, new_world.sweep_run.entries):
        require(child.scenario is not None and child.trajectory is not None,
                "grandchild has a fabricated admission/trajectory")
        require(child.scenario.parent_revision_id == parent.revision_id,
                "grandchild parent SHA does not name structural world")
        require(child.scenario.source_annotations == parent.source_annotations,
                "grandchild changed source inventory or names")
        require(len(child.scenario.changes) == 1
                and child.scenario.changes[0].component_id == "point:added"
                and child.scenario.changes[0].property == "charge_c",
                "property revision changed more than the named source charge")
        require(child.scenario.spec.field.sources[-1].charge_c == charge,
                "property sweep did not apply to real introduced charge")
        comparisons = child.as_dict(new_world.sweep_run.baseline_trajectory)["comparisons"]
        require(len(comparisons) == 101, "M28a literal-time deltas omitted samples")
        parent_times = {row.time_s: row for row in new_world.sweep_run.baseline_trajectory.samples}
        child_times = {row.time_s: row for row in child.trajectory.samples}
        for delta in comparisons:
            t = delta["time_s"]
            require(t in parent_times and t in child_times,
                    "invented interpolated physical timestamp")
            expected_dr = [
                child_times[t].position_m[i] - parent_times[t].position_m[i]
                for i in range(3)
            ]
            expected_dv = [
                child_times[t].velocity_m_s[i] - parent_times[t].velocity_m_s[i]
                for i in range(3)
            ]
            require(tuple(delta["delta_position_m"]) == tuple(expected_dr)
                    and tuple(delta["delta_velocity_m_s"]) == tuple(expected_dv),
                    "incorrect source-world local same-time displacement/velocity")

    require(run.entries[1].parent_scenario is None
            and run.entries[1].structural_entry.assembly is None,
            "structural refusal fabricated an accepted inventory")
    require(run.entries[2].parent_scenario is plan.family.baseline
            and run.entries[2].sweep_run is None
            and detached["entries"][2]["source_inventory"] is not None,
            "sweep-axis refusal lost an accepted source inventory")

    results = [
        validate_sampled_run("original", run.structural_run.baseline_trajectory, None),
        validate_sampled_run("added-parent", new_world.structural_entry.trajectory,
                             PARENT_NEW_Q),
    ]
    for q, entry in zip(VARIANT_Q, new_world.sweep_run.entries):
        results.append(validate_sampled_run(
            "added-variation-"+str(q), entry.trajectory, q))
    last_a = np.array(new_world.sweep_run.entries[0].trajectory.samples[-1].position_m)
    last_b = np.array(new_world.sweep_run.entries[1].trajectory.samples[-1].position_m)
    require(np.linalg.norm(last_a-last_b) > 1e-5,
            "different source-property revisions did not yield distinguishable dynamics")

    native_file = output / "native-structural-parameter.json"
    native_file.write_text(json.dumps(detached, sort_keys=True, indent=2) + "\n",
                           encoding="utf-8")
    summary = {
        "result": "HARNESS PASS — not independent reviewer PASS",
        "pinned_source_sha": head, "pinned_source_tree": tree,
        "original_revision_id": plan.family.baseline.revision_id,
        "source_added_revision_id": parent.revision_id,
        "source_assembly_revision_id": assembly.revision_id,
        "grandchild_revision_ids": [
            entry.scenario.revision_id for entry in new_world.sweep_run.entries
        ],
        "branch_statuses": [entry.status for entry in run.entries],
        "grandchild_statuses": [
            entry.status for entry in new_world.sweep_run.entries
        ],
        "independent_reference": "96-node Gauss-Legendre Coulomb rod + SciPy DOP853",
        "native_vs_independent": results,
        "original_native_JSON_sha256": hashlib.sha256(native_file.read_bytes()).hexdigest(),
        "limitations": "Numerical comparison not rigorous exact-ODE error proof; "
                       "all structures are independent static teacher hypotheses, "
                       "no conductor induction, free-3D motion, browser physics, "
                       "post-guard continuation or work across changed source inventories.",
    }
    receipt = output / "transfer-receipt.json"
    receipt.write_text(json.dumps(summary, sort_keys=True, indent=2) + "\n",
                       encoding="utf-8")
    print(json.dumps(summary, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
