"""Independent Chat B review #01 for conductor_sim PR91/M38a.

Run only after exact-SHA checkout. This file lives in reviewer-owned review_sandbox,
not in the production source. Physics checks use independent Python stdlib
formulae; production public APIs only supply actual observations.
"""
from __future__ import annotations

import json
from copy import deepcopy
from dataclasses import replace
from math import hypot, isclose, isfinite, nextafter, pi, inf
from pathlib import Path
import sys

from conductor_sim.model import EPSILON_0, PointCharge
from conductor_sim.prescribed_ground_wire import (
    PrescribedSphereRadialSpec,
    author_prescribed_grounded_sphere,
    sample_prescribed_sphere_radial,
)
from conductor_sim.prescribed_ground_line import (
    PrescribedSphereLineSpec, sample_prescribed_sphere_line,
    validate_prescribed_sphere_line,
)
from conductor_sim.solver import UnsupportedProblem
from conductor_sim.external_sphere import ExternalGroundedSphereBackend
from tools.m38a_line_reference import check_line_record


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def near(a, b, label, *, rtol=2e-9, atol=2e-24):
    require(type(a) in (float, int) and isfinite(a), f"{label}: non-finite/non-real {a!r}")
    require(isclose(a, b, rel_tol=rtol, abs_tol=atol),
            f"{label}: actual {a!r} != standalone SI {b!r}")


def physics_check(doc, tag):
    """Full independent reconstruction, no production physics or oracle calls."""
    require(doc["source_role"].startswith("teacher_hypothetical"), f"{tag}: false teacher role")
    require("RADIAL" in doc["original_workbook_case"], f"{tag}: missing original radial distinction")
    require("NOT Newtonian" in doc["protocol"], f"{tag}: free-motion mislabel")
    require(doc["sphere_is_solid"] is True and doc["sphere_constraint"] == "Grounded",
            f"{tag}: invalid boundary")
    a = doc["sphere_radius_m"]
    c = doc["sphere_center_m"]
    x0 = doc["initial_source_position_m"]
    v = doc["constant_cartesian_velocity_m_s"]
    q = doc["source_charge_c"]
    eps = doc["permittivity_f_per_m"]
    T = doc["duration_s"]
    guard = doc["surface_guard_m"]
    n = doc["sample_count"]
    require(n == len(doc["samples"]), f"{tag}: sample count")
    r0 = [x0[j] - c[j] for j in range(3)]
    dot0 = sum(r0[j]*v[j] for j in range(3))
    speed2 = sum(z*z for z in v)
    require(speed2 > 0, f"{tag}: static")
    tstar = min(T, max(0., -dot0/speed2))
    rstar = [r0[j] + v[j]*tstar for j in range(3)]
    dstar = hypot(*rstar)
    require(dstar > a+guard, f"{tag}: path crosses guard")
    near(doc["closest_approach_time_s"], tstar, f"{tag}: closest time")
    near(doc["closest_approach_distance_m"], dstar, f"{tag}: closest distance")
    k = 1./(4.*pi*eps)
    checked = 0
    for i, row in enumerate(doc["samples"]):
        require(type(row["index"]) is int and row["index"] == i,
                f"{tag}: row index {i}")
        t = T*i/(n-1)
        near(row["time_s"], t, f"{tag} row {i} t")
        pos = [x0[j] + t*v[j] for j in range(3)]
        r = [pos[j]-c[j] for j in range(3)]
        d2 = sum(z*z for z in r)
        d = d2**.5
        rv = sum(r[j]*v[j] for j in range(3))
        vr = rv/d
        charge = -q*a/d
        current = -q*a*rv/(d**3)
        force = [-k*q*q*a*r[j]/((d2-a*a)**2) for j in range(3)]
        energy = -k*q*q*a/(2*(d2-a*a))
        for j in range(3):
            near(row["source_position_m"][j], pos[j], f"{tag} {i} x{j}")
            near(row["source_velocity_m_s"][j], v[j], f"{tag} {i} v{j}")
            near(row["induced_force_on_source_n"][j], force[j], f"{tag} {i} F{j}")
            checked += 3
        expected = {
            "radial_distance_m": d,
            "radial_velocity_m_s": vr,
            "induced_sphere_net_charge_c": charge,
            "wire_current_sphere_to_ground_a": current,
            "wire_current_ground_to_sphere_a": -current,
            "induced_mechanical_energy_j": energy,
        }
        for key, val in expected.items():
            near(row[key], val, f"{tag} {i} {key}")
            checked += 1
        require(sum(force[j]*r[j] for j in range(3)) < 0,
                f"{tag} {i} force not attractive")
        require(energy < 0, f"{tag} {i} energy not negative")
    return {
        "name": tag,
        "independently_checked_states": n,
        "independently_checked_scalar_fields": checked,
        "closest_time_s": tstar,
        "closest_distance_m": dstar,
        "initial_wire_current_a": doc["samples"][0]["wire_current_sphere_to_ground_a"],
        "final_wire_current_a": doc["samples"][-1]["wire_current_sphere_to_ground_a"],
    }


def expect_refusal(build, tag, match=None):
    try:
        build()
    except (ValueError, TypeError, UnsupportedProblem) as error:
        if match:
            require(match.lower() in str(error).lower(),
                    f"{tag}: rejected for wrong reason: {error}")
        return {"name": tag, "refused": True, "reason": f"{type(error).__name__}: {error}"}
    raise AssertionError(f"{tag}: dangerous input was accepted")


def spec_for(*, q=1e-9, x0=(-.4, .2, 0.), center=(0.,0.,0.),
             a=.1, v=(.2,0.,0.), T=4., n=41, guard=.01,
             epsilon=EPSILON_0):
    p = author_prescribed_grounded_sphere(
        q, x0, a, sphere_center_m=center,
        sphere_name="Reviewer sphere", permittivity_f_per_m=epsilon
    )
    return PrescribedSphereLineSpec(p, v, T, n, guard)


def attacks_json(doc):
    """Real JSON-decoded list/dict perturbations; reference must reject each."""
    cases = [
        ("false-zero-timestamp", ("samples",0,"time_s"), False, "non-boolean"),
        ("false-zero-index", ("samples",0,"index"), False, "index/order"),
        ("forged-sample-index", ("samples",0,"index"), 1, "index/order"),
        ("terminal-current-sign", ("samples",0,"wire_current_sphere_to_ground_a"),
          -doc["samples"][0]["wire_current_sphere_to_ground_a"], "wire_current_sphere_to_ground_a"),
        ("reverse-ground-terminal", ("samples",0,"wire_current_ground_to_sphere_a"),
          doc["samples"][0]["wire_current_sphere_to_ground_a"], "wire_current_ground_to_sphere_a"),
        ("charge-sign", ("source_charge_c",), -doc["source_charge_c"], "induced_sphere_net_charge_c"),
        ("force-vector", ("samples",7,"induced_force_on_source_n",0), 0., "induced force axis"),
        ("energy-half-factor", ("samples",5,"induced_mechanical_energy_j"),
          2*doc["samples"][5]["induced_mechanical_energy_j"], "induced_mechanical_energy_j"),
        ("3d-position", ("samples",10,"source_position_m",1), 0.31, "physical x1"),
        ("3d-velocity", ("samples",10,"source_velocity_m_s",2), .08, "physical v2"),
        ("closest-time", ("closest_approach_time_s",), 1., "closest-approach physical time"),
        ("closest-distance", ("closest_approach_distance_m",), .25, "closest-approach distance"),
        ("current-si-unit", ("units","current"), "mA", "SI unit"),
        ("fake-source-role", ("source_role",), "original_jee_Q21", "teacher-only"),
        ("fake-original-attribution", ("original_workbook_case",), "Off-axis was in the original", "teacher-only"),
        ("fake-solid-state", ("sphere_is_solid",), False, "grounded solid sphere"),
        ("fake-electrical-state", ("sphere_constraint",), "FixedNetCharge", "grounded solid sphere"),
        ("fake-physics-protocol", ("protocol",), "free Newtonian integration", "protocol"),
        ("fake-schema", ("schema",), "conductor_sim.newtonian.v1", "protocol"),
        ("missing-sphere-identity", ("sphere_name",), "", "identity"),
    ]
    results = []
    for name,path,value,reason in cases:
        forged = json.loads(json.dumps(doc))
        require(type(forged["samples"]) is list
                and type(forged["samples"][0]["source_position_m"]) is list,
                f"{name}: forged data is not real decoded JSON lists")
        obj = forged
        for part in path[:-1]:
            obj = obj[part]
        obj[path[-1]] = value
        results.append(expect_refusal(lambda f=forged: check_line_record(f), name, reason))
    return results


def attacks_geometry():
    results=[]
    # All saved endpoints are outside guard, while t=2 (never sampled) is inside metal.
    times = [4*i/3 for i in range(4)]
    stored = [hypot(-.4+.2*t,.05) for t in times]
    require(all(d > .11 for d in stored), "hidden crossing seed has unsafe stored sample")
    results.append(expect_refusal(lambda: spec_for(x0=(-.4,.05,0),n=4),
                                 "hidden-between-four-frames", "continuous path"))
    results.append(expect_refusal(lambda: spec_for(x0=(-.4,.11,0),n=4),
                                 "exact-tangent-to-guard", "continuous path"))
    results.append(expect_refusal(
        lambda: spec_for(x0=(-.4, nextafter(.11,inf), 0.),n=4),
        "numerically-unresolved-just-above-guard", "continuous path"))
    clear = spec_for(x0=(-.4,.110001,0.),n=4)
    physics_check(sample_prescribed_sphere_line(clear).as_dict(), "just-clear-above-guard")
    results.append({"name":"just-clear-above-guard","accepted":True,
                    "closest_distance":clear.closest_approach[1]})
    results.append(expect_refusal(
        lambda: spec_for(x0=(.11,0.,0.),v=(.03,0,0),T=1.,n=4),
        "contact-at-time-zero","continuous path"))
    results.append(expect_refusal(
        lambda: spec_for(x0=(.2,0.,0.),v=(-.09,0,0),T=1.,n=4),
        "contact-at-time-T","continuous path"))
    first = spec_for(x0=(.3,.15,0.),v=(.04,.02,.01),T=1.,n=5)
    require(first.closest_approach[0] == 0., "endpoint-start constrained minimum incorrect")
    results.append({"name":"closest-at-start","accepted":True})
    last = spec_for(x0=(.4,.14,.1),v=(-.03,-.005,0.),T=2.,n=5)
    require(last.closest_approach[0] == 2., "endpoint-end constrained minimum incorrect")
    results.append({"name":"closest-at-end","accepted":True})
    return results,stored


def attacks_typed():
    result=[]
    native = sample_prescribed_sphere_line(spec_for())
    fake_row = replace(native.samples[0], time_s=False)
    fake_trace = replace(native, samples=(fake_row,)+native.samples[1:])
    result.append(expect_refusal(lambda: validate_prescribed_sphere_line(fake_trace),
                                 "dataclasses-replace-false-time", "native re-execution"))
    result.append(expect_refusal(lambda: fake_trace.as_dict(),
                                 "dataclasses-replace-false-time-export", "native re-execution"))
    fake_row = replace(native.samples[0],
        wire_current_sphere_to_ground_a=-native.samples[0].wire_current_sphere_to_ground_a)
    fake_trace = replace(native, samples=(fake_row,)+native.samples[1:])
    result.append(expect_refusal(lambda: validate_prescribed_sphere_line(fake_trace),
                                 "dataclasses-replace-current-sign", "native re-execution"))
    spec = spec_for()
    object.__setattr__(spec, "duration_s", False)
    result.append(expect_refusal(lambda: sample_prescribed_sphere_line(spec),
                                 "object-setattr-false-duration", "non-Boolean"))
    spec = spec_for()
    # Corrupt nested frozen legacy PointCharge, not just the outer spec.
    object.__setattr__(spec.problem.charges[0], "position_m", (False,.2,0.))
    result.append(expect_refusal(lambda: sample_prescribed_sphere_line(spec),
                                 "nested-object-setattr-false-coordinate", "non-Boolean"))
    result.append(expect_refusal(
        lambda: author_prescribed_grounded_sphere(True,(-.4,.2,0.),.1),
        "raw-authoring-bool-charge", "non-Boolean"))
    return result


def radial_agreement():
    result=[]
    for q in (+1e-9,-1.9e-9):
        for signed_v in (-.04,.04):
            p = author_prescribed_grounded_sphere(q,(0.,0.,.4),.1)
            old = sample_prescribed_sphere_radial(
                PrescribedSphereRadialSpec(p,signed_v,2.,11,.01))
            new = sample_prescribed_sphere_line(
                PrescribedSphereLineSpec(p,(0.,0.,signed_v),2.,11,.01))
            for i,(x,y) in enumerate(zip(old.samples,new.samples)):
                for field in ("time_s","radial_distance_m","induced_sphere_net_charge_c",
                              "wire_current_sphere_to_ground_a",
                              "wire_current_ground_to_sphere_a",
                              "induced_mechanical_energy_j"):
                    near(getattr(y,field),getattr(x,field),f"radial {q}/{signed_v}/{i}/{field}")
                for j in range(3):
                    near(y.induced_force_on_source_n[j],
                         x.induced_force_on_source_n[j],
                         f"radial {q}/{signed_v}/{i}/F{j}")
            result.append({"q_C":q,"signed_radial_velocity_m_s":signed_v,
                           "compared_native_states":len(new.samples)})
    return result


def finite_difference_current(spec):
    # Fresh native Kelvin backend charge at neighboring genuine source positions.
    t=2.
    dt=2e-4
    start=spec.problem.charges[0].position_m
    v=spec.velocity_m_s
    def sphere_charge(time):
        point=tuple(start[i]+v[i]*time for i in range(3))
        p=replace(spec.problem,charges=(PointCharge(
            spec.problem.charges[0].charge_c,point),))
        return ExternalGroundedSphereBackend().solve(p).conductor_results[0].net_charge_c
    derivative=(sphere_charge(t+dt)-sphere_charge(t-dt))/(2*dt)
    trace=sample_prescribed_sphere_line(spec)
    # t=2s is an actual saved time for 23 samples over T=5? Not necessarily.
    # Independently compute instant scalar wire-current directly from r(t).
    c=spec.problem.conductors[0].center_m
    r=[start[i]+v[i]*t-c[i] for i in range(3)]
    d=hypot(*r)
    expected=-spec.problem.charges[0].charge_c*spec.problem.conductors[0].radius_m*sum(
        r[i]*v[i] for i in range(3))/(d**3)
    near(-derivative,expected,"fresh-native-Q derivative",rtol=2e-7,atol=1e-20)
    return {"physical_time_s":t,"finite_difference_minus_dQ_dt_A":-derivative,
            "standalone_instant_current_A":expected,"delta_t_s":dt,
            "native_saved_samples":len(trace.samples)}


def main():
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument("--line",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    report={"source_pin":"b482aaab716bbfb5a06984d4e8678707c5235d15",
            "tree_pin":"7873a982c19f597bde4cad205d4f39ba199d5038",
            "reviewer":"Chat B independent arithmetic + adversarial authoring",
            "completed":False}
    try:
        original=json.loads(args.line.read_text(encoding="utf-8"))
        report["native_teacher_example"]=physics_check(original,"41-state-teacher-example")
        require(len(original["samples"])==41,"example isn't 41 physical samples")
        require(original["samples"][0]["wire_current_sphere_to_ground_a"]>0,
                "positive-q approach must give positive conventional current")
        require(original["samples"][20]["wire_current_sphere_to_ground_a"]==0,
                "tangent must have exactly zero net wire current")
        require(original["samples"][-1]["wire_current_sphere_to_ground_a"]<0,
                "positive-q recession must give negative conventional current")
        require(original["closest_approach_time_s"]==2.,
                "example closest time must be 2s")
        near(original["closest_approach_distance_m"],.2,"example closest 0.2m")
        unfamiliar_spec=spec_for(q=-2.3e-9,
            x0=(.85,-.45,2.17),center=(1.25,-.7,2.3),
            a=.08,v=(.09,-.035,.045),T=5.,n=23,guard=.01,
            epsilon=2.5*EPSILON_0)
        data=sample_prescribed_sphere_line(unfamiliar_spec).as_dict()
        (args.out/"unfamiliar-native-line.json").write_text(
            json.dumps(data,indent=2,allow_nan=False)+"\n",encoding="utf-8")
        require(all(x!=0 for x in unfamiliar_spec.velocity_m_s),
                "unfamiliar case must genuinely move in all three axes")
        report["unfamiliar_3d_negative_charge"]=physics_check(data,"3D-translated-negative-q")
        require(data["samples"][0]["wire_current_sphere_to_ground_a"]<0
                and data["samples"][-1]["wire_current_sphere_to_ground_a"]>0,
                "negative-q approach/recession signs fail")
        report["standalone_production_oracle_check"]=check_line_record(data)
        report["radial_m37b_baseline"] = radial_agreement()
        report["geometry_attacks"],report["hidden_crossing_sample_distances_m"]=attacks_geometry()
        report["typed_mutation_attacks"]=attacks_typed()
        report["json_decoded_attacks"]=attacks_json(original)
        report["fresh_native_charge_derivative"]=finite_difference_current(unfamiliar_spec)
        report["completed"]=True
        print("INDEPENDENT REVIEW RUN PASS: all 41 example rows, all 23 unfamiliar rows, "
              "continuous geometry, radial agreement, JSON and typed mutations",flush=True)
    except Exception as exc:
        report["failure"]=f"{type(exc).__name__}: {exc}"
        raise
    finally:
        (args.out/"reviewer-results.json").write_text(
            json.dumps(report,indent=2,allow_nan=False)+"\n",encoding="utf-8")
        print("EVIDENCE JSON",args.out/"reviewer-results.json",flush=True)


if __name__=="__main__":
    main()
