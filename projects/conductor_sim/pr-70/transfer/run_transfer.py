"""M30b exact-source novel nested event transfer, developer-authored evidence.

Executes real source-structure→property→M24a typed observations using pinned
conductor_sim, and independently computes physical roots using a separately
written Gauss-Legendre rod Coulomb field + SciPy DOP853 with a signed detector.
This test is NOT an independent Chat B review verdict.
"""
from __future__ import annotations

from hashlib import sha256
import json
from math import pi
from pathlib import Path
import subprocess

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp

from conductor_sim import (
    BranchSweep, FixedPointField, NestedEventPlan, PointCharge, PrescribedField,
    StructuralParameterPlan, SweepAxis, TestChargeMotionSpec, UniformGravity,
    UniformRodField, run_nested_event_family,
)
from conductor_sim.motion_events import EventPolicy, PlaneEvent
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.structural_family import StructuralCase, StructuralFamilyPlan
from conductor_sim.structural_scenarios import NamedSource

SOURCE_SHA = "e40fc0452f71e3522ffc90115a740e052cd93209"
SOURCE_TREE = "fa949663147614db71a8cd509cd84440e3947b87"
Q_PROBE, MASS = .8e-9, 9e-6
ROD_Q = 2.8e-9
ROD_A = np.array((.095, -.08, 0.), dtype=float)
ROD_B = np.array((.14, .11, 0.), dtype=float)
HELD = ((1.3e-9,(.19,.14,0.)),(-.8e-9,(-.17,.09,0.)))
NEW_POS = (.18,-.085,0.)
SOURCE_PARENT_Q = 1.5e-9
VARIANTS = (.6e-9,2.4e-9)
G = np.array((0.,-.08,0.),dtype=float)
Y0 = np.array((0.,0.,0.,.045,.016,0.),dtype=float)
DURATION = .42
DETECTOR_X = .002


def require(expr, message):
    if not expr:
        raise AssertionError(message)


def author_native():
    original = PrescribedScenario(
        "m30b:transfer-original",
        TestChargeMotionSpec(
            PrescribedField((
                UniformRodField(ROD_Q,tuple(map(float,ROD_A)),tuple(map(float,ROD_B))),
                FixedPointField(HELD[0][0],HELD[0][1]),
                FixedPointField(HELD[1][0],HELD[1][1]),
            )),
            PointCharge(Q_PROBE,(0.,0.,0.)),MASS,
            (.045,.016,0.),DURATION,.0042,
            plane_normal=(0.,0.,1.),relative_tolerance=2e-9,
            gravity=UniformGravity((0.,-.08,0.)),
            source_guard_m=.001,
        ),
        (
            ("rod:slant","Tilted held finite rod"),
            ("point:upper","Original +1.3 nC held point"),
            ("point:lower","Original -0.8 nC held point"),
        ),
        "Teacher hypothesis: real Coulomb/gravity sources, no conductor induction.")
    family = StructuralFamilyPlan("m30b:transfer-worlds",original,(
        StructuralCase("add-point","Add new held source before parameter variations.",
            add_sources=(NamedSource("point:added","New adjustable held point",
                FixedPointField(SOURCE_PARENT_Q,NEW_POS)),)),
        StructuralCase("bad-offplane","Unpaired off-plane charge must physically refuse.",
            add_sources=(NamedSource("point:unpaired","Unpaired off-plane source",
                FixedPointField(1e-9,(.15,.05,.08))),)),
    ))
    plan = StructuralParameterPlan("m30b:transfer-grid",family,(
        BranchSweep("add-point",SweepAxis("point:added","charge_c",VARIANTS)),
        BranchSweep("bad-offplane",SweepAxis("point:unpaired","charge_c",(2e-9,))),
        BranchSweep("baseline",SweepAxis("point:added","charge_c",(.6e-9,))),
    ))
    question = PlaneEvent(
        "x:outbound",(DETECTOR_X,0.,0.),(1.,0.,0.),
        "Passive positive x crossing after real source edits",direction=1)
    return NestedEventPlan(plan,(question,),EventPolicy(.002,1e-9,1e-9,1e-7))


def independent_reference(source_q):
    """Separate 96-node SI Coulomb quadrature, without reading native physics."""
    nodes,weights=leggauss(96)
    sites=ROD_A[None,:]+((nodes+1)/2)[:,None]*(ROD_B-ROD_A)[None,:]
    k=1/(4*pi*8.8541878128e-12)
    points=list(HELD)
    if source_q is not None:
        points.append((source_q,NEW_POS))

    def efield(pos):
        diff=pos[None,:]-sites
        rr=np.linalg.norm(diff,axis=1)
        e=k*ROD_Q*np.sum((weights/(2*rr**3))[:,None]*diff,axis=0)
        for q,xyz in points:
            d=pos-np.asarray(xyz,dtype=float)
            norm=np.linalg.norm(d)
            e+=k*q*d/norm**3
        return e

    def rhs(_time,state):
        return np.concatenate((state[3:],(Q_PROBE/MASS)*efield(state[:3])+G))

    def detector(_time,state):
        return state[0]-DETECTOR_X

    detector.direction=1
    detector.terminal=False
    solution=solve_ivp(
        rhs,(0,DURATION),Y0,method="DOP853",
        events=detector,rtol=3e-12,atol=2e-14,max_step=.001,
    )
    require(solution.success, "independent DOP853 integration failed")
    require(len(solution.t_events[0])==1,
            "independent signed x detector did not have one outbound root")
    state=solution.y_events[0][0]
    force=Q_PROBE*efield(state[:3])+MASS*G
    return dict(
        source_charge_c=source_q,
        event_time_s=float(solution.t_events[0][0]),
        event_position_m=state[:3].tolist(),
        event_velocity_m_s=state[3:].tolist(),
        total_force_n=force.tolist(),
        t_final_s=float(solution.t[-1]),
    )


def assert_native_event(label,native,reference):
    require(native is not None,label+": missing native M24a run")
    require(native.trajectory.termination=="duration",
            label+": event observation censored unexpectedly")
    require(native.as_dict()["outcomes"]=={"x:outbound":"located"},
            label+": native event not uniquely resolved")
    require(len(native.events)==1,label+": extra/absent native roots")
    event=native.events[0]
    require(event.event_id=="x:outbound" and event.direction==1,
            label+": incorrect signed detector identity")
    lo,hi=event.time_bracket_s
    require(lo<=event.sample.time_s<=hi,
            label+": native event root escaped numerical bracket")
    require(abs(event.sample.time_s-reference["event_time_s"])<2e-7,
            label+": native crossing disagrees with independent DOP853")
    require(lo-2e-8<=reference["event_time_s"]<=hi+2e-8,
            label+": independent root is outside native numerical bracket tolerance")
    require(np.linalg.norm(
        np.asarray(event.sample.position_m)-reference["event_position_m"])<2e-7,
        label+": native root 3D position disagrees with separate solver")
    require(np.linalg.norm(
        np.asarray(event.sample.velocity_m_s)-reference["event_velocity_m_s"])<3e-6,
        label+": native root velocity disagrees with separate solver")
    require(np.linalg.norm(
        np.asarray(event.sample.force_n)-reference["total_force_n"])<1e-10,
        label+": native root SI total force disagrees with reference")
    return dict(
        label=label,
        native_time_s=event.sample.time_s,
        original_native_time_bracket_s=list(event.time_bracket_s),
        signed_direction=event.direction,
        native_position_m=list(event.sample.position_m),
        native_velocity_m_s=list(event.sample.velocity_m_s),
        native_force_n=list(event.sample.force_n),
        independent_reference=reference,
        native_minus_reference_time_s=event.sample.time_s-reference["event_time_s"],
    )


def check_pair(record,reference_shift):
    require(record["status"]=="one-resolved-pair",
            "eligible unique same-signed complete roots were left unpaired")
    require(record["direction"]==1,"wrong signed comparison")
    estimate=record["estimated_numerical_shift_s"]
    require(abs(estimate-reference_shift)<3e-7,
            "native structural/property root-time shift disagrees with reference")
    low,high=record["numerical_bracket_shift_interval_s"]
    require(low<=estimate<=high,"shift escaped native bracket difference")
    return dict(native_delta_t_s=estimate,independent_delta_t_s=reference_shift,
                native_numeric_interval_s=[low,high])


def main():
    root=Path(__file__).resolve().parents[4]
    native=root/"native_source"
    head=subprocess.check_output(
        ["git","-C",str(native),"rev-parse","HEAD"],text=True).strip()
    tree=subprocess.check_output(
        ["git","-C",str(native),"rev-parse","HEAD^{tree}"],text=True).strip()
    require(head==SOURCE_SHA and tree==SOURCE_TREE,
            "native source is not the exact pinned source commit/tree")
    output=root/"m30b-transfer-output"
    output.mkdir(parents=True,exist_ok=True)

    plan=author_native()
    before=plan.experiment.family.baseline.as_dict()
    result=run_nested_event_family(plan)
    require(before==plan.experiment.family.baseline.as_dict(),
            "authoring mutated original physical source world")
    require([b.physical_entry.status for b in result.branches]==[
        "evaluated","skipped-structural-model","rejected-sweep-axis"],
        "two distinct structural/axis refusal stages were conflated")
    require(result.branches[1].event_run is None
            and result.branches[1].physical_entry.parent_scenario is None,
            "refused off-plane source was granted event history")
    require(result.branches[2].event_run is result.original_event_run,
            "baseline selector produced a spurious new structural event run")
    require(result.branches[2].status=="complete"
            and result.branches[2].variations==(),
            "accepted original with bad new-source property request lost real event or fabricated grandchildren")

    parent_branch=result.branches[0]
    parent=parent_branch.physical_entry.parent_scenario
    assembly=parent_branch.physical_entry.structural_entry.assembly
    require(assembly.parent is plan.experiment.family.baseline,
            "structural source changed wrong original parent")
    require(assembly.as_dict()["parent_revision_id"]==before["revision_id"],
            "source structural parent SHA wrong")
    require(assembly.as_dict()["child_revision_id"]==parent.revision_id,
            "actual structural world SHA wrong")
    require([entry["operation"] for entry in assembly.changes]==["add-source"],
            "source membership change ledger is not one add-source")
    require([sid for sid,_ in parent.source_annotations]==[
        "rod:slant","point:upper","point:lower","point:added"],
        "real source stable ID/name membership not bound to added source")
    require([v.status for v in parent_branch.variations]==["complete","complete"],
            "actual source property grandchildren were not independently observed")
    require(all(v.physical_entry.scenario.parent_revision_id==parent.revision_id
                for v in parent_branch.variations),
            "grandchildren do not name their real structural parent revision")
    require([v.physical_entry.scenario.spec.field.sources[-1].charge_c
             for v in parent_branch.variations]==list(VARIANTS),
            "M20b changed the wrong physical charge or membership")
    require(all(v.event_run.study.scenario is v.physical_entry.scenario
                for v in parent_branch.variations),
            "event native integration not bound to correct source-property model")

    references=[
        independent_reference(None),
        independent_reference(SOURCE_PARENT_Q),
        independent_reference(VARIANTS[0]),
        independent_reference(VARIANTS[1]),
    ]
    native_runs=[
        result.original_event_run,
        parent_branch.event_run,
        parent_branch.variations[0].event_run,
        parent_branch.variations[1].event_run,
    ]
    comparisons=[
        assert_native_event(name,n,ref) for name,n,ref in zip(
            ("original","added-structural-parent","child-charge-0.6nC",
             "child-charge-2.4nC"), native_runs,references)
    ]
    record=result.as_dict()
    real_parent=record["branches"][0]
    root_pairs=[
        check_pair(real_parent["original_to_structural_event_comparisons"][0],
                   references[1]["event_time_s"]-references[0]["event_time_s"]),
        check_pair(real_parent["variations"][0]["parent_event_comparisons"][0],
                   references[2]["event_time_s"]-references[1]["event_time_s"]),
        check_pair(real_parent["variations"][1]["parent_event_comparisons"][0],
                   references[3]["event_time_s"]-references[1]["event_time_s"]),
    ]
    require(record["schema"]=="conductor_sim.nested_event_family.v1",
            "wrong auditable native schema")
    require(record["branches"][2]["original_to_structural_event_comparisons"][0]["status"]
            =="reference-baseline","original model was compared to itself as a source change")
    require(record["physical_model_family"]["entries"][1]["source_inventory"] is None
            and record["physical_model_family"]["entries"][2]["source_inventory"] is not None,
            "refusal inventories were fabricated or erased")
    require(not record["time_interpolation"] and not record["postguard_extrapolation"],
            "unqualified temporal evidence claim")

    native_json=output/"nested-source-property-events.json"
    native_json.write_text(
        json.dumps(record,allow_nan=False,sort_keys=True,indent=2)+"\n",
        encoding="utf-8")
    receipt=dict(
        status="DEVELOPER-AUTHORED TRANSFER HARNESS PASS; independent review still pending",
        source_pr=70,
        exact_source_sha=head,
        exact_source_git_tree=tree,
        original_model_revision=plan.experiment.family.baseline.revision_id,
        structural_model_revision=parent.revision_id,
        structural_assembly_revision=assembly.revision_id,
        grandchild_model_revisions=[
            v.physical_entry.scenario.revision_id for v in parent_branch.variations],
        physical_branch_statuses=[b.physical_entry.status for b in result.branches],
        event_branch_statuses=[b.status for b in result.branches],
        genuine_signed_roots=comparisons,
        native_pair_vs_independent_DOP853_shifts=root_pairs,
        reference="Standalone direct Coulomb + 96-node Gauss-Legendre finite rod + SciPy DOP853",
        native_json_sha256=sha256(native_json.read_bytes()).hexdigest(),
        qualification=("Exact native numerical event brackets are localizations on "
                       "integrated RK trajectories, not rigorous ODE error bounds. "
                       "Independent static teacher source hypotheticals only; "
                       "no conductor response or post-guard continuation."),
    )
    (output/"transfer-receipt.json").write_text(
        json.dumps(receipt,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(receipt,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
