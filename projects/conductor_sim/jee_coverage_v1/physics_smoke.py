"""JEE-30 Phase-1 ORIGINAL synthetic physical transfer probes on pinned M34b.

This is a developer-controlled, OPEN probe (not blind JEE interpretation,
not a score for 30 cards, not a student-viewer validation). Uses native
conductor_sim ONLY as the code under test. Independently derives expected
SI Coulomb, Kelvin, Newtonian, potential and refusal results without using
production source's force callbacks to calculate expected answers.
"""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from math import fsum, hypot, isclose, pi, sqrt
from pathlib import Path

from conductor_sim import (
    ElectrostaticProblem, ExternalGroundedSphereBackend,
    FixedPointField, Grounded, PointCharge, PrescribedField,
    SolidSphere, TestChargeMotionSpec,
    UniformDiskAxisField, UniformElectricField, UniformRingAxisField,
    UniformRodField, UniformShellField, integrate_test_charge,
)
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.motion_events import EventPolicy, EventStudy, VelocityReversal, investigate_motion
from conductor_sim.solver import SingularField, UnsupportedProblem

from validate_cards import load

# Official CODATA epsilon_0 (F/m); reference formulas do not call production
# electric field providers except to obtain the actual values under test.
EPS_0 = 8.8541878128e-12
K = 1.0 / (4.0 * pi * EPS_0)


def near(observed, expected, label, *, rtol=3e-10, atol=1e-13):
    if type(observed) not in (int, float) or not isclose(
        observed, expected, rel_tol=rtol, abs_tol=atol
    ):
        raise AssertionError(f"{label}: got {observed!r}, independent {expected!r}")


def vector_near(observed, expected, label, *, rtol=5e-10, atol=1e-13):
    if len(observed) != 3:
        raise AssertionError(label + ": missing actual three-vector")
    for i, (a, b) in enumerate(zip(observed, expected)):
        near(a, b, label + f" component {i}", rtol=rtol, atol=atol)


def probe_F01():
    field = PrescribedField((
        FixedPointField(2e-9, (-.1, 0., 0.)),
        FixedPointField(2e-9, (+.1, 0., 0.)),
    ))
    point = (0., 0., 0.)
    vector_near(field.electric_field_at(point), (0., 0., 0.), "F01 E")
    independent = K * (2e-9/.1 + 2e-9/.1)
    near(field.potential_at(point), independent, "F01 V")
    return {"V_V": independent, "E_V_m": [0., 0., 0.]}


def probe_F02():
    field = PrescribedField((
        FixedPointField(+3e-9, (+.05, 0., 0.)),
        FixedPointField(-3e-9, (-.05, 0., 0.)),
    ))
    probe = (0., .2, 0.)
    r = hypot(.05, .2)
    independent_x = -2 * K * 3e-9 * .05 / r**3
    near(field.potential_at(probe), 0., "F02 equatorial zero V", atol=1e-10)
    vector_near(field.electric_field_at(probe), (independent_x, 0., 0.), "F02 field")
    return {"V_V": 0., "Ex_V_m": independent_x}


def probe_F03():
    rod = UniformRodField(2e-9, (-.1, 0., 0.), (+.1, 0., 0.))
    probe = (0., .15, 0.)
    n = 12000
    length = .2
    dq = 2e-9/n
    dx = (-(.1) + (j+.5)*length/n for j in range(n))
    positions = tuple(dx)
    rs = tuple(hypot(x, .15) for x in positions)
    potential = K * dq * fsum(1/r for r in rs)
    ey = K * dq * fsum(.15/(r*r*r) for r in rs)
    vector_near(rod.electric_field_at(probe), (0., ey, 0.), "F03 rod quadrature",
                rtol=5e-8, atol=1e-11)
    near(rod.potential_at(probe), potential, "F03 rod V", rtol=3e-8)
    return {"V_V": potential, "Ey_V_m": ey, "quadrature_elements": n}


def probe_F04():
    ring1 = UniformRingAxisField(+5e-9, .1, (0., 0., 0.))
    ring2 = UniformRingAxisField(-3e-9, .1, (0., 0., .3))
    field = PrescribedField((ring1, ring2))
    checks = 0
    for z in (-.05, .09, .18, .30, .41):
        V = K * (5e-9/sqrt(.1**2+z*z) - 3e-9/sqrt(.1**2+(z-.3)**2))
        Ez = K * (5e-9*z/(.1**2+z*z)**1.5 -
                  3e-9*(z-.3)/(.1**2+(z-.3)**2)**1.5)
        near(field.potential_at((0., 0., z)), V, f"F04 V at z={z}")
        vector_near(field.electric_field_at((0., 0., z)), (0., 0., Ez), f"F04 E at z={z}")
        checks += 1
    return {"verified_axial_sample_positions": checks}


def probe_F05():
    disk = UniformDiskAxisField(4e-9, .2)
    for z in (0., .05):
        V = 2*K*4e-9/(sqrt(.2**2+z*z)+z)
        near(disk.potential_at((0., 0., z)), V, f"F05 V z={z}")
    z = .05
    Ez = (2*K*4e-9/.2**2)*(1-z/sqrt(.2**2+z*z))
    vector_near(disk.electric_field_at((0., 0., z)), (0.,0.,Ez), "F05 one-sided E")
    try:
        disk.electric_field_at((0.,0.,0.))
    except SingularField:
        pass
    else:
        raise AssertionError("F05 fabricated a defined surface E")
    return {"V_z0_V":2*K*4e-9/.2,"Ez_z005_V_m":Ez,"surface_E":"undefined"}


def probe_C01():
    problem = ElectrostaticProblem(
        charges=(PointCharge(1e-9, (0., 0., .3)),),
        conductors=(SolidSphere(.1, Grounded(), name="metal"),))
    sol = ExternalGroundedSphereBackend().solve(problem)
    Q_ind = -(1e-9)*.1/.3
    F_z = -K*(1e-9)**2*.1*.3/(.3**2-.1**2)**2
    U = -K*(1e-9)**2*.1/(2*(.3**2-.1**2))
    near(sol.conductor_results[0].net_charge_c, Q_ind, "C01 induced Q", atol=1e-18)
    vector_near(sol.force_on_charge_n, (0.,0.,F_z), "C01 Kelvin force", atol=1e-17)
    near(sol.interaction_energy_j, U, "C01 half-energy convention", atol=1e-17)
    near(sol.conductor_results[0].potential_v, 0., "C01 grounding")
    return {"induced_Q_C":Q_ind, "Fz_N":F_z,"U_J":U}


def probe_W01():
    E = UniformElectricField((100.,0.,0.))
    field = PrescribedField((E,))
    start, end = (0.,0.,0.),(.2,0.,0.)
    dV = -100*.2
    W = 1e-9*100*.2
    near(field.potential_at(end)-field.potential_at(start), dV, "W01 Delta V")
    near(1e-9*(field.potential_at(start)-field.potential_at(end)), W,"W01 field work")
    return {"DeltaV_V":dV,"W_field_J":W,"DeltaU_J":-W}


def probe_M01():
    spec = TestChargeMotionSpec(
        PrescribedField((UniformElectricField((0.,200.,0.)),)),
        PointCharge(1e-9, (0.,0.,0.)), 1e-9,
        (.2,0.,0.), .1, .01, plane_normal=(0.,0.,1.))
    result = integrate_test_charge(spec)
    if result.termination != "duration" or len(result.samples) < 9:
        raise AssertionError("M01 genuine finite trajectory did not finish")
    max_p=max_v=max_f=0.
    for sample in result.samples:
        t=sample.time_s
        position=(.2*t, .5*200*t*t, 0.)
        velocity=(.2, 200*t,0.)
        force=(0.,2e-7,0.)
        max_p=max(max_p,*(abs(sample.position_m[k]-position[k]) for k in range(3)))
        max_v=max(max_v,*(abs(sample.velocity_m_s[k]-velocity[k]) for k in range(3)))
        max_f=max(max_f,*(abs(sample.force_n[k]-force[k]) for k in range(3)))
        vector_near(sample.position_m,position, "M01 r(t)",rtol=2e-6,atol=1e-8)
        vector_near(sample.velocity_m_s,velocity,"M01 v(t)",rtol=2e-6,atol=1e-8)
        vector_near(sample.force_n,force,"M01 F=qE",rtol=2e-9,atol=1e-13)
    near(result.samples[-1].time_s,.1,"M01 final clock",atol=1e-13)
    return {"native_saved_states":len(result.samples),"max_position_error_m":max_p,
            "max_velocity_error_m_s":max_v,"max_force_error_N":max_f,
            "last_position_m":result.samples[-1].position_m}


def probe_M02():
    field=PrescribedField((UniformElectricField((-100.,0.,0.)),))
    spec=TestChargeMotionSpec(field,PointCharge(+1e-9,(0.,0.,0.)),
                              2e-6,(.2,0.,0.),.7,.05,plane_normal=(0.,0.,1.))
    scenario=PrescribedScenario(
        "jee30-m02",spec,(("field:E","Stationary leftward E"),),
        "Original JEE-style uniform deceleration and absent in-window reversal.")
    question=VelocityReversal("vx:turn", (1.,0.,0.),
                              "x-velocity zero and changes sign",direction=-1)
    run=investigate_motion(EventStudy(scenario,(question,),EventPolicy(.015,1e-9,1e-8,1e-8)))
    a = 1e-9*(-100.)/(2e-6)
    full_root=-.2/a
    if not full_root>.7 or run.trajectory.termination!="duration":
        raise AssertionError("M02 horizon/duration violated")
    if any(event.event_id=="vx:turn" for event in run.events):
        raise AssertionError("M02 falsely located reversal outside observation horizon")
    for sample in run.trajectory.samples:
        t=sample.time_s
        vector_near(sample.position_m,(.2*t + .5*a*t*t,0.,0.),
                    "M02 independent position",atol=5e-9,rtol=1e-6)
        vector_near(sample.velocity_m_s,(.2+a*t,0.,0.),
                    "M02 independent velocity",atol=5e-9,rtol=1e-6)
    outcomes=run.as_dict()["outcomes"]
    if outcomes["vx:turn"] in ("located","located-with-unresolved-candidates"):
        raise AssertionError("M02 falsely exported a located event outside horizon")
    return {"native_samples":len(run.trajectory.samples),
            "mathematical_reversal_time_s":full_root,
            "observed_duration_s":.7,"native_outcome":outcomes["vx:turn"]}


def probe_R01():
    shell=UniformShellField(1e-9,.1)
    a,b=.09,.11
    near(shell.potential_at((a,0.,0.)),K*1e-9/.1,"R01 V inside")
    near(shell.potential_at((.1,0.,0.)),K*1e-9/.1,"R01 continuous surface V")
    near(shell.potential_at((b,0.,0.)),K*1e-9/.11,"R01 V outside")
    vector_near(shell.electric_field_at((a,0.,0.)),(0.,0.,0.),"R01 interior E")
    vector_near(shell.electric_field_at((b,0.,0.)),(K*1e-9/b**2,0.,0.),"R01 exterior E")
    try: shell.electric_field_at((.1,0.,0.))
    except SingularField: pass
    else: raise AssertionError("R01 invented one surface field at a discontinuity")
    return {"inside_E_zero":True,"surface_E":"undefined","V_continuous":True}


def probe_R02():
    disk=UniformDiskAxisField(2e-9,.2)
    try: disk.electric_field_at((.05,0.,.04))
    except UnsupportedProblem as e: return {"typed_refusal":type(e).__name__,"why":str(e)}
    raise AssertionError("R02 silently used axial disk field off-axis")


def probe_R04():
    try:
        TestChargeMotionSpec(
            PrescribedField((FixedPointField(1e-9,(0.,0.,.1)),)),
            PointCharge(1e-9,(.03,.04,0.)),1e-6,
            (0.,0.,0.),.05,.01,plane_normal=(0.,0.,1.))
    except UnsupportedProblem as e:
        return {"typed_refusal":type(e).__name__,"why":str(e)}
    raise AssertionError("R04 illegally admitted non-planar free motion as xy")


PROBES = {
    "F01":("static",probe_F01),"F02":("static",probe_F02),
    "F03":("static",probe_F03),"F04":("static",probe_F04),
    "F05":("static",probe_F05),"C01":("static",probe_C01),
    "W01":("static",probe_W01),"M01":("trajectory",probe_M01),
    "M02":("trajectory",probe_M02),"R01":("static",probe_R01),
    "R02":("refusal",probe_R02),"R04":("refusal",probe_R04),
}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--bank",type=Path,default=Path(__file__).with_name("cases.json"))
    parser.add_argument("--output",type=Path,default=Path("output/jee30-phase1-probes.json"))
    args=parser.parse_args()
    prereg=load(args.bank)
    actual=json.loads(args.bank.read_text(encoding="utf-8"))
    bank_ids={x["id"] for x in actual["cases"]}
    if not set(PROBES)<=bank_ids:
        raise ValueError("phase one probes must be explicitly preregistered")
    rows=[]
    for name,(mode,func) in PROBES.items():
        evidence=func()
        rows.append({
            "case_id":name,"execution_type":mode,
            "physics_probe_status":"PASS",
            "independent_formula_compared":True,
            "evidence":evidence,
            "interpretation_fidelity":"not_evaluated",
            "physical_correctness":("not_applicable" if mode=="refusal" else "pass"),
            "simulation_coverage":("unsupported" if mode=="refusal" else
                                   "supported_for_tested_subset"),
            "educational_usefulness":"not_evaluated",
            "textbook_answer_completeness":"not_attempted",
        })
    counts=Counter(k for k,_ in PROBES.values())
    report={
        "schema":"conductor_sim.jee30_phase1_original_scientific_probes.v1",
        "released_source_commit":prereg["bank_sha256"] and
                                 "a5113fa4cc924ac10cbb35b2f2d7ac80e11f1bde",
        "bank_sha256":prereg["bank_sha256"],
        "registered_original_problems":30,
        "open_developer_probes_executed":len(rows),
        "native_trajectory_cases":counts["trajectory"],
        "static_physics_probes":counts["static"],
        "honest_domain_refusals":counts["refusal"],
        "blinded_problem_interpretations_scored":0,
        "educational_viewer_grades":0,
        "actual_past_year_JEE_questions_scored":0,
        "unprobed_registered_cases":30-len(rows),
        "all_executed_probes_pass":True,
        "honest_scope":"Original, author-exposed samples; NOT a 30-question solved/usable JEE benchmark",
        "rows":rows,
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,allow_nan=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k!="rows"},sort_keys=True))


if __name__=="__main__":
    main()
