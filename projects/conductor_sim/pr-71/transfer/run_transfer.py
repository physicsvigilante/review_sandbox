"""M31a developer-authored exact-source unfamiliar coupled native/physics transfer.

Native M31a owns real source reassembly, atomic M20b property changes and
unchanged RK trajectories. The independent physics reference evaluates
Coulomb point charges + 96-node Gauss-Legendre finite rod, and separately
integrates ODEs with SciPy DOP853. This is supplemental CI, NOT Chat B PASS.
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
    CoupledPhysicalPlan, CoupledHypothesis, CoupledPropertyEdit,
    FixedPointField, PointCharge, PrescribedField, TestChargeMotionSpec,
    UniformGravity, UniformRodField, run_coupled_physical_family,
)
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.structural_family import StructuralCase, StructuralFamilyPlan
from conductor_sim.structural_scenarios import NamedSource

PINNED_SOURCE = "e8970e26b91f6f8dfe3bd8bffcaf8f181449870b"
PINNED_TREE = "15e658dfae00289e27a577f5f1df1c340e8e1c72"
ROD_A, ROD_B = np.array((.095,-.08,0.)), np.array((.14,.11,0.))
ROD_Q, PROBE_Q = 2.8e-9, .8e-9
HELD=((1.3e-9,(.19,.14,0.)),(-.8e-9,(-.17,.09,0.)))
NEW_POS=(.18,-.085,0.)
PARENT_SOURCE_Q=1.5e-9
G=np.array((0.,-.08,0.))
Y0=np.array((0.,0.,0.,.045,.016,0.))
T=.42


def require(v,message):
    if not v:
        raise AssertionError(message)


def author_plan():
    baseline=PrescribedScenario(
        "m31a:transfer-original",
        TestChargeMotionSpec(
            PrescribedField((
                UniformRodField(ROD_Q,tuple(map(float,ROD_A)),tuple(map(float,ROD_B))),
                FixedPointField(HELD[0][0],HELD[0][1]),
                FixedPointField(HELD[1][0],HELD[1][1]),
            )),
            PointCharge(PROBE_Q,(0.,0.,0.)),9e-6,(.045,.016,0.),
            T,.0042,plane_normal=(0.,0.,1.),
            gravity=UniformGravity((0.,-.08,0.)),
            source_guard_m=.001,relative_tolerance=2e-9),
        (("rod:tilted","Physical tilted charged rod"),
         ("point:plus","Held original positive charge"),
         ("point:minus","Held original negative charge")),
        "Teacher hypothetical with static nonresponding source identities.")
    family=StructuralFamilyPlan("m31a:transfer-worlds",baseline,(
        StructuralCase("new-point","Independently insert genuine source.",
            add_sources=(NamedSource(
                "point:added","New adjustable held source",
                FixedPointField(PARENT_SOURCE_Q,NEW_POS)),)),
        StructuralCase("bad-offplane","Unpaired off-plane source must refuse.",
            add_sources=(NamedSource(
                "point:unpaired","Unpaired off-plane held source",
                FixedPointField(1e-9,(.15,.05,.08))),)),
    ))
    def edit(identifier,property_name,value):
        return CoupledPropertyEdit(identifier,property_name,value)
    def hypo(case,branch,edit1,edit2):
        return CoupledHypothesis(
            case,branch,"Teacher coupled physical changes, checked as one full model.",
            (edit1,edit2))
    return CoupledPhysicalPlan("m31a:transfer",family,(
        hypo("strong","new-point",
             edit("point:added","charge_c",2.4e-9),
             edit("test-particle","mass_kg",1.5e-5)),
        hypo("weak","new-point",
             edit("point:added","charge_c",.6e-9),
             edit("test-particle","mass_kg",1.1e-5)),
        hypo("bad-structure","bad-offplane",
             edit("point:unpaired","charge_c",2e-9),
             edit("test-particle","mass_kg",2e-5)),
        hypo("missing-id","baseline",
             edit("point:added","charge_c",2.4e-9),
             edit("test-particle","mass_kg",1.5e-5)),
        hypo("invalid-plane","new-point",
             edit("point:added","position_m",(.18,-.085,.04)),
             edit("test-particle","mass_kg",1.5e-5)),
    ))


def numerical_reference(point_q,mass,times):
    """Separate independent SI field and DOP853 integrator; NO native data."""
    k=1/(4*pi*8.8541878128e-12)
    nodes,weights=leggauss(96)
    sites=ROD_A[None,:]+((nodes+1)/2)[:,None]*(ROD_B-ROD_A)[None,:]
    fixed=list(HELD)
    if point_q is not None:
        fixed.append((point_q,NEW_POS))

    def efield(position):
        offsets=position[None,:]-sites
        distances=np.linalg.norm(offsets,axis=1)
        e=k*ROD_Q*np.sum(
            (weights/(2*distances**3))[:,None]*offsets,axis=0)
        for charge,site in fixed:
            displacement=position-np.asarray(site)
            r=np.linalg.norm(displacement)
            e+=k*charge*displacement/r**3
        return e

    def rhs(_time,state):
        return np.concatenate((state[3:],PROBE_Q/mass*efield(state[:3])+G))

    ref=solve_ivp(
        rhs,(0,T),Y0,method="DOP853",
        dense_output=True,rtol=3e-12,atol=2e-14,max_step=.001)
    require(ref.success,"independent physical DOP853 integration failed")
    states=ref.sol(np.asarray(times)).T
    forces=np.array([
        PROBE_Q*efield(state[:3])+mass*G for state in states
    ])
    return states,forces


def validate_trajectory(name,run,charge,mass):
    require(run is not None and run.termination=="duration",
            name+": no full-duration genuine native trajectory")
    samples=run.samples
    require(len(samples)==101,name+": expected 101 authentic saved physical states")
    times=[s.time_s for s in samples]
    require(times[0]==0 and abs(times[-1]-T)<1e-14,
            name+": wrong physical time horizon")
    require(all(a<b for a,b in zip(times,times[1:])),
            name+": physical time not strictly monotone")
    ref,force=numerical_reference(charge,mass,times)
    native=np.array([
        [*s.position_m,*s.velocity_m_s] for s in samples])
    actual_force=np.array([s.force_n for s in samples])
    dx=float(np.max(np.linalg.norm(native[:,:3]-ref[:,:3],axis=1)))
    dv=float(np.max(np.linalg.norm(native[:,3:]-ref[:,3:],axis=1)))
    df=float(np.max(np.linalg.norm(actual_force-force,axis=1)))
    require(dx<2e-7,name+": physical position mismatch independent DOP853")
    require(dv<2e-6,name+": physical velocity mismatch independent DOP853")
    require(df<1e-10,name+": physical force mismatch separate Coulomb quadrature")
    require(max(abs(s.position_m[2]) for s in samples)<1e-12,
            name+": native states left qualified invariant plane")
    return dict(
        case=name,mass_kg=mass,added_source_charge_c=charge,
        physical_samples=len(times),
        last_saved_time_s=times[-1],
        max_position_error_m=dx,max_velocity_error_m_s=dv,
        max_force_error_n=df,
        native_final_position_m=list(samples[-1].position_m),
        reference_final_position_m=ref[-1,:3].tolist(),
        native_final_velocity_m_s=list(samples[-1].velocity_m_s),
        reference_final_velocity_m_s=ref[-1,3:].tolist())


def main():
    root=Path(__file__).resolve().parents[4]
    source=root/"native_source"
    source_head=subprocess.check_output(
        ["git","-C",str(source),"rev-parse","HEAD"],text=True).strip()
    source_tree=subprocess.check_output(
        ["git","-C",str(source),"rev-parse","HEAD^{tree}"],text=True).strip()
    require(source_head==PINNED_SOURCE and source_tree==PINNED_TREE,
            "source identity mismatch: no stale or synthetic PR merge HEAD")
    output=root/"m31a-transfer-output"
    output.mkdir(parents=True,exist_ok=True)
    plan=author_plan()
    original=plan.family.baseline.as_dict()
    run=run_coupled_physical_family(plan)
    require(run.plan is plan and plan.family.baseline.as_dict()==original,
            "native source assembly changed the frozen original")
    expected=("complete","complete","skipped-structural-model",
              "rejected-coupled-edit","rejected-physical-model")
    require(tuple(x.status for x in run.entries)==expected,
            "M31a refusal stage or admitted source/model classification false")
    first,second=run.entries[:2]
    structural=first.structural_entry.assembly
    require(structural.parent is plan.family.baseline,
            "source child did not reassemble from actual original")
    parent=structural.scenario
    require(structural.as_dict()["parent_revision_id"]==original["revision_id"]
            and structural.as_dict()["child_revision_id"]==parent.revision_id,
            "M22a original→structural SHA/provenance false")
    require(first.parent_scenario is parent and second.parent_scenario is parent,
            "named coupled cases were not bound to REAL new-source world")
    require([i for i,_ in parent.source_annotations]==[
        "rod:tilted","point:plus","point:minus","point:added"],
        "new physical source membership/ID is missing")
    for e,q,mass in ((first,2.4e-9,1.5e-5),(second,.6e-9,1.1e-5)):
        require(e.scenario.parent_revision_id==parent.revision_id,
                "atomic grandchild does not name structural immediate parent")
        require(e.scenario.source_annotations==parent.source_annotations,
                "atomic property revision changed physical source membership")
        require(e.scenario.spec.field.sources[-1].charge_c==q
                and e.scenario.spec.mass_kg==mass,
                "atomic source+mass revision did not take effect")
        require({(c.component_id,c.property) for c in e.scenario.changes}==
                {("point:added","charge_c"),("test-particle","mass_kg")},
                "coupled M20b ledger omitted/added unexpected physical changes")
        require(len(e.comparisons)==101,"native literal-time comparison lost samples")
        original_rows={x.time_s:x for x in first.structural_entry.trajectory.samples}
        varied_rows={x.time_s:x for x in e.trajectory.samples}
        for comp in e.comparisons:
            t=comp["time_s"]
            require(t in original_rows and t in varied_rows,
                    "interpolated or fictitious time in parent-to-grandchild comparison")
            require(tuple(comp["delta_position_m"])==tuple(
                varied_rows[t].position_m[i]-original_rows[t].position_m[i]
                for i in range(3)), "wrong exact-time 3D position delta")
            require(tuple(comp["delta_velocity_m_s"])==tuple(
                varied_rows[t].velocity_m_s[i]-original_rows[t].velocity_m_s[i]
                for i in range(3)), "wrong exact-time 3D velocity delta")

    require(run.entries[2].parent_scenario is None
            and run.entries[2].scenario is None,
            "structurally refused world has invented accepted source inventory")
    require(run.entries[3].parent_scenario is plan.family.baseline
            and run.entries[3].scenario is None,
            "valid original with unknown source ID was wrongly accepted")
    require(run.entries[4].parent_scenario is parent
            and run.entries[4].scenario is None,
            "invalid full physical plane was accepted after atomic edits")

    checks=[
        validate_trajectory("original",run.structural_run.baseline_trajectory,None,9e-6),
        validate_trajectory("new-structural-parent",
                            first.structural_entry.trajectory,1.5e-9,9e-6),
        validate_trajectory("coupled-strong",first.trajectory,2.4e-9,1.5e-5),
        validate_trajectory("coupled-weak",second.trajectory,.6e-9,1.1e-5),
    ]
    require(np.linalg.norm(np.asarray(first.trajectory.samples[-1].position_m)
                           -np.asarray(second.trajectory.samples[-1].position_m))>1e-4,
            "coupled physical hypotheses did not give distinct genuine paths")
    audit=run.as_dict()
    require(audit["schema"]=="conductor_sim.coupled_physical_family.v1"
            and not audit["time_interpolation"] and not audit["postguard_extrapolation"],
            "versioned native evidence misstates physical observations")
    require(audit["entries"][2]["accepted_parent_inventory"] is None
            and audit["entries"][3]["accepted_parent_inventory"] is not None
            and audit["entries"][4]["accepted_parent_inventory"] is not None,
            "wrong source-world inventory after a refusal")

    raw=output/"native-coupled-worlds.json"
    raw.write_text(json.dumps(audit,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    receipt=dict(
        verdict="DEVELOPER-AUTHORED TRANSFER HARNESS PASS; separate independent review pending",
        source_pr=71,
        source_commit=source_head,actual_source_tree=source_tree,
        original_model_revision_id=plan.family.baseline.revision_id,
        structural_parent_revision_id=parent.revision_id,
        structural_assembly_revision_id=structural.revision_id,
        coupled_grandchild_revisions=[first.scenario.revision_id,second.scenario.revision_id],
        statuses=list(expected),
        method="Own SI Coulomb field, 96-node Gauss-Legendre finite rod, SciPy DOP853",
        independent_numerical_checks=checks,
        native_json_sha256=sha256(raw.read_bytes()).hexdigest(),
        qualification=("Finite native trajectories and 3D deltas, not exact-ODE proof; "
                       "physically unchanged static sources during each run, "
                       "no induced conductor, contact, or postguard extrapolation."),
    )
    (output/"transfer-receipt.json").write_text(
        json.dumps(receipt,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(receipt,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
