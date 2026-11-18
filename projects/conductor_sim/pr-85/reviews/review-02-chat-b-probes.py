"""Separate-context Chat B R2 probes for M36b PR85; source-pin is asserted by workflow.

Real source APIs are invoked for novel teacher worlds. Physical expectations are
derived separately from standard-library SI formulae, not copied from M36b
developer transfer/reference output. Preserves failure results and native data.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import traceback
from dataclasses import replace
from pathlib import Path

EPS0 = 8.8541878128e-12
ELEMENTARY_CHARGE = 1.602176634e-19
M_E = 9.1093837139e-31
K_COULOMB = 1.0 / (4.0 * math.pi * EPS0)
records = []


def near(actual, expected, *, atol=0.0, rtol=1e-10, label=""):
    if not math.isfinite(actual) or not math.isclose(actual, expected, rel_tol=rtol, abs_tol=atol):
        raise AssertionError(f"{label}: actual {actual!r}; independently expected {expected!r}")


def vector(actual, expected, *, atol=1e-12, rtol=1e-10, label=""):
    if len(actual) != len(expected):
        raise AssertionError(f"{label}: vector length mismatch")
    for index, (got, want) in enumerate(zip(actual, expected)):
        near(got, want, atol=atol, rtol=rtol, label=f"{label}[{index}]")


def run(label, fn):
    try:
        result = fn()
        records.append(dict(probe=label, outcome="PASS", evidence=result))
        print("REVIEW02 PASS", label, json.dumps(result, sort_keys=True, allow_nan=False), flush=True)
    except Exception:
        error = traceback.format_exc()
        records.append(dict(probe=label, outcome="FAIL", traceback=error))
        print("REVIEW02 FAIL", label, error, flush=True)


def expect_rejection(baseline, label, modify, expected_phrase):
    from tools.m36b_jee_reference import check_native
    forged = copy.deepcopy(baseline)
    modify(forged["source_apparatus"])
    try:
        check_native(forged)
    except (AssertionError, ValueError, TypeError, KeyError) as exc:
        msg = str(exc)
        if expected_phrase not in msg:
            raise AssertionError(f"{label}: rejected for unexpected reason: {msg}") from exc
        return dict(rejected=True, checker_error=msg, adversarial_target=label)
    raise AssertionError(f"{label}: FORGED real saved physical record was ACCEPTED")


def change(case, path, value):
    node = case
    for part in path[:-1]:
        node = node[part]
    node[path[-1]] = value


def original_and_attacks(folder):
    from tools.m36b_jee_replay import run_all
    from tools.m36b_jee_reference import check_native
    from examples.jee_potential_explorer import make_case as field_case
    from conductor_sim.jee_potential_explorer import validate_fixed_potential_map

    genuine = run_all(folder / "original-native")
    verified = check_native(genuine)
    assert genuine["source_apparatus_count"] == 7
    assert genuine["unsupported_refusal_count"] == 1
    assert genuine["explicit_refusal"]["native"] is False
    assert verified["independent_math_verified_scoped_apparatus"] == 7
    sheet = genuine["source_apparatus"]["p02-single-19"]
    ring = genuine["source_apparatus"]["p12-linked-40"]
    early = sheet["early_surface_variant"]
    actual_root = 2*.0002/(
        math.sqrt(2*100*ELEMENTARY_CHARGE/M_E) +
        math.sqrt(2*100*ELEMENTARY_CHARGE/M_E * (2*100*ELEMENTARY_CHARGE/M_E) -
                  2*(ELEMENTARY_CHARGE*2e-6/EPS0/M_E)*.0002)
    )
    near(early["event_time_s"], actual_root, atol=2e-14, rtol=0, label="first physical contact root")
    result = {
        "seven_genuine_native_cases_accepted": True,
        "explicit_three_cavity_3D_refusal": genuine["explicit_refusal"],
        "native_sheet_stop": sheet["events"][0],
        "native_early_contact": early["actual_native_contact_event"],
        "first_root_s": actual_root,
        "ring_work_components": ring["observed_source_work_components"],
        "ring_axial_field_A_B_v_m": [
            ring["start_electric_field_v_m"][0], ring["end_electric_field_v_m"][0]],
        "circle_sources": genuine["source_apparatus"]["jee2021-p1-q09-q10-equipotential"]["sources"],
        "circle_masks": genuine["source_apparatus"]["jee2021-p1-q09-q10-equipotential"]["source_masks"],
        "far_sphere_teacher_transfer": genuine["source_apparatus"]["p02-single-15"]["teacher_transfer_variant"],
    }
    run("baseline seven actual source cases+first root/source identities", lambda: result)

    attacks = [
        ("F01 stopped energy physically impossible", "p02-single-19",
         lambda c: change(c, ("events",0,"kinetic_energy_j"), 1e-34),
         "stopping kinetic energy"),
        ("F01 full-stop y velocity", "p02-single-19",
         lambda c: change(c, ("events",0,"velocity_m_s",1), 250.0),
         "stopped electron full velocity vector"),
        ("F01 full-stop z velocity", "p02-single-19",
         lambda c: change(c, ("events",0,"velocity_m_s",2), -13.0),
         "stopped electron full velocity vector"),
        ("F01 full-stop z displacement", "p02-single-19",
         lambda c: change(c, ("events",0,"position_m",2), .0004),
         "real stopped electron position vector"),
        ("F01 false full-stop flag", "p02-single-19",
         lambda c: change(c, ("events",0,"full_stop"), False),
         "real complete stop event missing"),
        ("F02 near but wrong earlier quadratic root", "p02-single-19",
         lambda c: (
             change(c,("early_surface_variant","event_time_s"),actual_root+5e-12),
             change(c,("early_surface_variant","actual_native_contact_event","time_s"),actual_root+5e-12)),
         "FIRST metal-surface root time"),
        ("F02 false first-event velocity", "p02-single-19",
         lambda c: change(c,("early_surface_variant","actual_native_contact_event","velocity_m_s",0),-12.0),
         "native impact-threshold velocity"),
        ("F03 signed ring work cancellation", "p12-linked-40",
         lambda c: (
             change(c,("observed_source_work_components",0,"field_work_j"),
                    c["observed_source_work_components"][0]["field_work_j"]+.25),
             change(c,("observed_source_work_components",1,"field_work_j"),
                    c["observed_source_work_components"][1]["field_work_j"]-.25)),
         "independent signed work from ring A"),
        ("F03 wrong signed Ex at A", "p12-linked-40",
         lambda c: change(c,("start_electric_field_v_m",0),-575203.3147),
         "independent E vector at ring centre A"),
        ("F03 wrong signed Ex at B", "p12-linked-40",
         lambda c: change(c,("end_electric_field_v_m",0),-287601.6574),
         "independent E vector at ring centre B"),
        ("F04 forged zero transfer energy", "p02-single-15",
         lambda c: change(c,("teacher_transfer_variant","released_field_energy_j"),0.0),
         "independent positive released field energy"),
        ("F04 forged signed transfer", "p02-single-15",
         lambda c: change(c,("teacher_transfer_variant","charge_transfers_c",1),-3e-9),
         "independent signed Q transfer 1"),
        ("F05 moved original 2021 source mask", "jee2021-p1-q09-q10-equipotential",
         lambda c: change(c,("source_masks",0,"center_m",0),.3),
         "source mask centre 0"),
        ("F05 false mask radius", "jee2021-p1-q09-q10-equipotential",
         lambda c: change(c,("source_masks",1,"radius_m"),.23),
         "source display-only exclusion radius 1"),
        ("F05 false conductor-boundary mask", "jee2021-p1-q09-q10-equipotential",
         lambda c: change(c,("source_masks",0,"kind"),"conductor-boundary"),
         "source singularities cannot masquerade"),
    ]
    for label, cid, mutation, message in attacks:
        run(label, lambda label=label,cid=cid,mutation=mutation,message=message:
            expect_rejection(genuine, label, lambda data:mutation(data[cid]), message))

    _html, bundle = field_case("2021-equipotential")
    assert validate_fixed_potential_map(bundle) is True
    run("F05 actual native 2021 fixed grid valid", lambda: {
        "native_full_grid_validation": True,
        "mask_count": len(bundle["frames"][0]["source_masks"]),
        "samples_per_axis": len(bundle["frames"][0]["grid"]["x_m"]),
    })

    def raw_rejection(kind, mutate, expected):
        bad = copy.deepcopy(bundle)
        mutate(bad)
        try:
            validate_fixed_potential_map(bad)
        except (ValueError, AssertionError, TypeError) as exc:
            if expected not in str(exc):
                raise AssertionError(f"{kind}: unexpected rejection {exc}") from exc
            return dict(native_exporter_rejected=True, error=str(exc))
        raise AssertionError(f"{kind}: raw original native model forgery accepted")

    run("F05 production native verifier rejects moved mask", lambda:
        raw_rejection("native-moved-mask",
                      lambda c: change(c,("frames",0,"source_masks",0,"center_m",0),.3),
                      "saved source exclusion geometry changed"))

    def damage_grid(b):
        g=b["frames"][0]["grid"]
        for row in g["potential_v"]:
            for i, value in enumerate(row):
                if isinstance(value,(int,float)):
                    row[i] = value+50
                    return
        raise AssertionError("no unmasked real grid node")

    run("F05 production native verifier rejects forged 2D grid", lambda:
        raw_rejection("raw-grid-forgery", damage_grid,
                      "saved static V/E disagrees with authored sources"))

    def damage_highlight(b):
        highlight=next(c for c in b["frames"][0]["contours"] if c.get("highlight"))
        highlight["segments_m"][0][0][0] += .4

    run("F05 production native verifier rejects foreign contour", lambda:
        raw_rejection("raw-contour-forgery",damage_highlight,
                      "saved highlighted contour is not the physical sampled potential"))


def novel_sheet():
    from examples.motion_event_studies import make_case
    from conductor_sim import PointCharge, PrescribedField, UniformElectricField
    from conductor_sim.motion_events import EventStudy, investigate_motion
    from conductor_sim.scenarios import PrescribedScenario

    original=make_case("sheet-stop")
    kinetic_eV=130.0
    sigma=-4.8e-6
    clearance=.002
    speed=math.sqrt(2*kinetic_eV*ELEMENTARY_CHARGE/M_E)
    accel=ELEMENTARY_CHARGE*abs(sigma)/(EPS0*M_E)
    modified=replace(
        original.scenario.spec,
        field=PrescribedField((UniformElectricField((sigma/EPS0,0.,0.)),)),
        particle=PointCharge(-ELEMENTARY_CHARGE,(clearance,0.,0.)),
        initial_velocity_m_s=(-speed,0.,0.))
    scenario=PrescribedScenario("chat-b02-novel-sheet-130ev",
        modified,original.scenario.source_annotations,
        "Reviewer-invented teacher hypothetical, not a source JEE original.")
    native=investigate_motion(EventStudy(scenario,original.questions,original.policy))
    assert len(native.events)==1 and native.events[0].event_id=="stop:x"
    assert native.trajectory.termination=="terminal-event"
    e=native.events[0].sample
    expected_t=speed/accel
    expected_x=clearance-speed*speed/(2*accel)
    near(e.time_s,expected_t,atol=1.5e-13,rtol=0,label="fresh sheet reversal t")
    vector(e.position_m,(expected_x,0.,0.),atol=3e-11,rtol=0,label="fresh sheet stopped world point")
    vector(e.velocity_m_s,(0.,0.,0.),atol=1e-3,rtol=0,label="fresh full-stop 3 velocity")
    near(e.kinetic_energy_j,.5*M_E*sum(x*x for x in e.velocity_m_s),
         atol=1e-40,rtol=1e-6,label="fresh kinetic-energy from saved true velocity")
    return dict(family="one-sided metal sheet",inputs=dict(kinetic_eV=kinetic_eV,sigma_c_m2=sigma,clearance_m=clearance),
                native_time_s=e.time_s,analytic_time_s=expected_t,
                native_stop_position_m=list(e.position_m),analytic_stop_x_m=expected_x,
                native_stop_velocity_m_s=list(e.velocity_m_s),
                native_stop_kinetic_energy_j=e.kinetic_energy_j)


def novel_dipole():
    from examples.rigid_dipoles import make_model
    from conductor_sim import UniformElectricField
    from conductor_sim.dipoles import dipole_work, observe_dipole, orient_dipole

    original,_=make_model("workbook-q47")
    q=.85e-9
    length=.075
    field=155.0
    degrees=127.0
    theta=math.radians(degrees)
    modified=replace(original,
        dipole=replace(original.dipole,charge_c=q,separation_m=length),
        sources=(replace(original.sources[0],
                         source=UniformElectricField((field,0.,0.))),),
        model_id="chat-b02-dipole-127",
        provenance="Reviewer-authored static orientation; no rotating body timeline.")
    observed=observe_dipole(orient_dipole(modified,theta))
    work=dipole_work(modified,0.,theta)
    native_work=work["external_quasistatic_work_j"]
    native_torque=observed["torque_n_m"]
    analytic_work=q*length*field*(1-math.cos(theta))
    analytic_torque_z=-q*length*field*math.sin(theta)
    near(native_work,analytic_work,atol=5e-19,label="new static dipole ΔU")
    vector(native_torque,(0.,0.,analytic_torque_z),atol=5e-19,label="new static dipole torque")
    return dict(family="finite dipole STATIC",charge_c=q,separation_m=length,
                field_v_m=field,angle_deg=degrees,native_delta_u_j=native_work,
                analytic_delta_u_j=analytic_work,
                native_torque_n_m=list(native_torque),
                analytic_torque_z_n_m=analytic_torque_z,not_rotational_dynamics=True)


def novel_3d_electric_gravity():
    from examples.electric_gravity_motion import build_case
    from conductor_sim import PrescribedField, UniformElectricField
    from conductor_sim.conservative_forces import UniformGravity
    from conductor_sim.prescribed_motion import integrate_test_charge

    source,_,_=build_case("jee2012-proton")
    mass=3.1e-27
    charge=1.1e-19
    field=2.7e-7
    gravity=12.4
    until=.0135
    v0=(.015,.04,.065)
    scenario=replace(source.spec,mass_kg=mass,
        particle=replace(source.spec.particle,charge_c=charge),
        field=PrescribedField((UniformElectricField((field,0.,0.)),)),
        gravity=UniformGravity((0.,-gravity,0.)),
        initial_velocity_m_s=v0,duration_s=until,
        sample_interval_s=.0005)
    native=integrate_test_charge(scenario)
    assert len(native.samples)>=25
    assert native.termination=="duration"
    acceleration=(charge*field/mass,-gravity,0.)
    for i,row in enumerate(native.samples):
        t=row.time_s
        position=tuple(v0[j]*t+.5*acceleration[j]*t*t for j in range(3))
        velocity=tuple(v0[j]+acceleration[j]*t for j in range(3))
        vector(row.position_m,position,atol=1e-11,rtol=1e-8,label=f"native 3D position sample {i}")
        vector(row.velocity_m_s,velocity,atol=3e-9,rtol=1e-8,label=f"native 3D velocity sample {i}")
    end=native.samples[-1]
    near(end.time_s,until,atol=1e-14,rtol=0,label="3D final time")
    analytic_p=tuple(v0[j]*until+.5*acceleration[j]*until*until for j in range(3))
    analytic_v=tuple(v0[j]+acceleration[j]*until for j in range(3))
    return dict(family="3D velocity + independent electric/gravity accelerations",
                mass_kg=mass,charge_c=charge,field_v_m=field,gravity_m_s2=gravity,
                initial_velocity_m_s=list(v0),time_s=until,samples=len(native.samples),
                native_final_position_m=list(end.position_m),
                analytic_final_position_m=list(analytic_p),
                native_final_velocity_m_s=list(end.velocity_m_s),
                analytic_final_velocity_m_s=list(analytic_v))


def novel_non_equilibrium_spheres():
    from examples.distant_connected_spheres import make_case
    from conductor_sim import FixedNetCharge
    from conductor_sim.distant_spheres import APPROXIMATION, DistantSphereConnectionBackend

    previous,_=make_case("surface-ratio")
    initial=(8e-9,-2e-9)
    old=previous.plan.initial.conductors
    new_initial=replace(previous.plan.initial,conductors=tuple(
        replace(c,constraint=FixedNetCharge(q)) for c,q in zip(old,initial)))
    plan=replace(previous.plan,initial=new_initial)
    backend=DistantSphereConnectionBackend()
    real=backend.solve(plan,approximation=APPROXIMATION)
    radii=[c.outer_radius_m for c in old]
    total=sum(initial)
    expected_final=[total*r/sum(radii) for r in radii]
    expected_transfer=[q-new for q,new in zip(expected_final,initial)]
    actual_final=[c.charge_c for c in real.after.conductors]
    actual_transfer=[b.charge_c-a.charge_c for a,b in zip(real.before.conductors,real.after.conductors)]
    for i in range(2):
        near(actual_final[i],expected_final[i],atol=1e-23,label=f"new actual sphere final charge {i}")
        near(actual_transfer[i],expected_transfer[i],atol=1e-23,label=f"new signed sphere transfer {i}")
        near(real.after.conductors[i].outer_field_normal_v_m,K_COULOMB*expected_final[i]/radii[i]**2,
             atol=1e-9,label=f"new sphere surface E {i}")
    independent_release=.5*K_COULOMB*(
        sum(q*q/r for q,r in zip(initial,radii))-
        sum(q*q/r for q,r in zip(expected_final,radii)))
    near(real.released_field_energy_j,independent_release,
         atol=2e-19,label="new positive static released self-energy")
    assert real.released_field_energy_j>0
    assert real.as_dict()["qualification"]["is_relative_error_bound"] is False

    near_second=replace(old[1],center_m=tuple(
        old[0].center_m[i]+(.45 if i==0 else 0.) for i in range(3)))
    invalid_plan=replace(plan,initial=replace(new_initial,
        conductors=(new_initial.conductors[0],replace(near_second,
                    constraint=FixedNetCharge(initial[1])))))
    try:
        backend.solve(invalid_plan,approximation=APPROXIMATION)
    except Exception as exc:
        assert "far-separation admission failed" in str(exc),f"wrong refusal: {exc}"
        refusal=str(exc)
    else:
        raise AssertionError("Unqualified close connected spheres accepted")
    return dict(family="non-equilibrium two connected spheres; leading self capacitances",
                teacher_initial_c=list(initial),source_radii_m=radii,
                native_final_charges_c=actual_final,analytic_final_charges_c=expected_final,
                native_signed_transfers_c=actual_transfer,analytic_transfers_c=expected_transfer,
                native_released_field_energy_j=real.released_field_energy_j,
                analytic_released_field_energy_j=independent_release,
                close_geometry_refusal=refusal,
                not_full_induction_and_not_a_5percent_error_bound=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    run("original native+corrected source-free saved-evidence adversarial suite",
        lambda: original_and_attacks(args.output.parent))
    run("NEW reviewer-authored native one-sided sheet",novel_sheet)
    run("NEW reviewer-authored native finite dipole",novel_dipole)
    run("NEW reviewer-authored native 3D electric plus gravity",novel_3d_electric_gravity)
    run("NEW reviewer-authored native far-sphere charge transfer/refusal",novel_non_equilibrium_spheres)
    report=dict(schema="independent-chat-b-m36b-pr85-review02.v1",
                source_head="524a6e07f17cd8bf53eaeec543031f1ec7bbb9eb",
                source_tree="c7c411d5602ada9db0f3b867c19ec4da6d317f6b",
                results=records,failed=[r["probe"] for r in records if r["outcome"]=="FAIL"])
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    print("REVIEW02 TOTAL",len(records),"FAILURES",len(report["failed"]),flush=True)
    if report["failed"]:
        raise SystemExit(1)


if __name__=="__main__":
    main()
