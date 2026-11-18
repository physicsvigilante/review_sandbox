"""Reviewer-authored M38a PR91 experiments: NOT imported from production tests.

Runs on a fresh GitHub Actions checkout of the literal pinned source commit.
No production repository mutation. First-attempt evidence is saved separately.
"""
from __future__ import annotations
import copy
import json
import math
import sys
from dataclasses import replace
from pathlib import Path

from conductor_sim.model import EPSILON_0
from conductor_sim.prescribed_ground_wire import (
    PrescribedSphereRadialSpec, author_prescribed_grounded_sphere,
    sample_prescribed_sphere_radial,
)
from conductor_sim.prescribed_ground_line import (
    PrescribedSphereLineSpec, sample_prescribed_sphere_line,
    validate_prescribed_sphere_line,
)
from conductor_sim.solver import UnsupportedProblem
from tools.m38a_line_reference import check_line_record


def close(actual, expected, what, *, rel=3e-9, absolute=1e-27):
    if type(actual) not in (float, int) or not math.isfinite(actual):
        raise AssertionError(f"{what}: invalid numerical type/value {actual!r}")
    if not math.isclose(actual, expected, rel_tol=rel, abs_tol=absolute):
        raise AssertionError(f"{what}: {actual!r} not equal independently computed {expected!r}")


def autonomous_si_audit(data):
    """Compute directly from Coulomb constant and x(t), not project physics."""
    c = data["sphere_center_m"]
    x0 = data["initial_source_position_m"]
    v = data["constant_cartesian_velocity_m_s"]
    T = data["duration_s"]
    a = data["sphere_radius_m"]
    q = data["source_charge_c"]
    eps = data["permittivity_f_per_m"]
    n = data["sample_count"]
    dot0 = sum((x0[j]-c[j])*v[j] for j in range(3))
    vsq = sum(w*w for w in v)
    tc = max(0., min(T, -dot0/vsq))
    xc = [x0[j]+v[j]*tc for j in range(3)]
    dc = math.sqrt(sum((xc[j]-c[j])**2 for j in range(3)))
    close(data["closest_approach_time_s"], tc, "analytic constrained closest time")
    close(data["closest_approach_distance_m"], dc, "analytic constrained closest radius")
    assert dc > a + data["surface_guard_m"]
    assert type(data["sphere_is_solid"]) is bool and data["sphere_is_solid"]
    assert "teacher" in data["source_role"]
    assert "RADIAL" in data["original_workbook_case"]
    assert "NOT Newtonian" in data["protocol"]
    assert len(data["samples"]) == n
    for i, row in enumerate(data["samples"]):
        t = T*i/(n-1)
        p = [x0[j] + v[j]*t for j in range(3)]
        r = [p[j]-c[j] for j in range(3)]
        d = math.sqrt(sum(z*z for z in r))
        projection = sum(r[j]*v[j] for j in range(3))
        vr = projection / d
        Q = -q*a/d
        I = -q*a*projection/d**3
        k = 1/(4*math.pi*eps)
        f = [-k*q*q*a*r[j]/(d*d-a*a)**2 for j in range(3)]
        U = -k*q*q*a/(2*(d*d-a*a))
        assert type(row["index"]) is int and row["index"] == i
        close(row["time_s"], t, f"sample[{i}].t")
        close(row["radial_distance_m"], d, f"sample[{i}].d")
        close(row["radial_velocity_m_s"], vr, f"sample[{i}].vr")
        close(row["induced_sphere_net_charge_c"], Q, f"sample[{i}].Q")
        close(row["wire_current_sphere_to_ground_a"], I, f"sample[{i}].I")
        close(row["wire_current_ground_to_sphere_a"], -I, f"sample[{i}].opposite terminal")
        close(row["induced_mechanical_energy_j"], U, f"sample[{i}].U")
        assert sum(f[j]*r[j] for j in range(3)) < 0  # attractive for q != 0
        for j in range(3):
            close(row["source_position_m"][j], p[j], f"sample[{i}].x{j}")
            close(row["source_velocity_m_s"][j], v[j], f"sample[{i}].v{j}")
            close(row["induced_force_on_source_n"][j], f[j], f"sample[{i}].F{j}")
    return {"rows_independently_checked": n, "t_closest_s": tc,
            "d_closest_m": dc, "current_first_a": data["samples"][0]["wire_current_sphere_to_ground_a"],
            "current_last_a": data["samples"][-1]["wire_current_sphere_to_ground_a"]}


def spec_for(q, x0, c, v, T, count=23, guard=.015, eps=EPSILON_0):
    problem = author_prescribed_grounded_sphere(
        q, x0, .1, sphere_center_m=c, sphere_name="Translated metal",
        permittivity_f_per_m=eps,
    )
    return PrescribedSphereLineSpec(problem, v, T, sample_count=count, surface_guard_m=guard)


def must_reject(f, token, label):
    try:
        f()
    except (ValueError, TypeError, UnsupportedProblem) as error:
        msg = str(error)
        if token.casefold() not in msg.casefold():
            raise AssertionError(f"{label} rejected for WRONG reason: {type(error).__name__}: {msg}")
        return {"attack": label, "reason": msg}
    raise AssertionError(f"{label} unexpectedly ACCEPTED")


def main(out):
    result = {"category": "independent M38a reviewer01 actual native probes",
              "examples": {}, "attacks": [], "scope": "Kelvin SI and typed authoring only"}
    from examples.m38a_line_approach import example_data
    example = json.loads(json.dumps(example_data()))  # genuine JSON document types
    result["examples"]["teacher_41"] = autonomous_si_audit(example)
    result["examples"]["teacher_41"]["stdlib_oracle_rows"] = check_line_record(example)["independently_checked_kelvin_states"]
    assert example["samples"][0]["wire_current_sphere_to_ground_a"] > 0
    assert example["samples"][20]["wire_current_sphere_to_ground_a"] == 0
    assert example["samples"][-1]["wire_current_sphere_to_ground_a"] < 0
    close(example["closest_approach_time_s"], 2., "teacher exact closest time")
    close(example["closest_approach_distance_m"], .2, "teacher exact closest distance")

    c = (.75, -.45, 1.2)
    r0 = (-.4, .26, .18)
    x0 = tuple(c[j]+r0[j] for j in range(3))
    v = (.19, -.06, .04)
    neg = sample_prescribed_sphere_line(spec_for(-1.7e-9, x0, c, v, 3.6, eps=EPSILON_0*1.3))
    neg_data = json.loads(json.dumps(neg.as_dict()))
    result["examples"]["unfamiliar_negative_3axis"] = autonomous_si_audit(neg_data)
    result["examples"]["unfamiliar_negative_3axis"]["stdlib_oracle_rows"] = check_line_record(neg_data)["independently_checked_kelvin_states"]
    assert all(z != 0 for z in v)
    assert neg_data["samples"][0]["wire_current_sphere_to_ground_a"] < 0
    assert neg_data["samples"][-1]["wire_current_sphere_to_ground_a"] > 0
    pos = sample_prescribed_sphere_line(spec_for(+1.7e-9, x0, c, v, 3.6, eps=EPSILON_0*1.3))
    for a,b in zip(neg.samples,pos.samples):
        close(a.wire_current_sphere_to_ground_a, -b.wire_current_sphere_to_ground_a, "q reversal I")
        close(a.induced_mechanical_energy_j, b.induced_mechanical_energy_j, "q reversal U")
        for j in range(3):
            close(a.induced_force_on_source_n[j], b.induced_force_on_source_n[j], "q reversal F")

    p_radial = author_prescribed_grounded_sphere(2e-9, (0.,0.,.4), .1)
    old = sample_prescribed_sphere_radial(PrescribedSphereRadialSpec(
        p_radial, -.06, 1.5, sample_count=13, surface_guard_m=.01))
    new = sample_prescribed_sphere_line(PrescribedSphereLineSpec(
        p_radial, (0.,0.,-.06), 1.5, sample_count=13, surface_guard_m=.01))
    for a,b in zip(old.samples,new.samples):
        close(a.induced_sphere_net_charge_c, b.induced_sphere_net_charge_c, "M37b radial Q")
        close(a.wire_current_sphere_to_ground_a, b.wire_current_sphere_to_ground_a, "M37b radial I")
        close(a.induced_mechanical_energy_j,b.induced_mechanical_energy_j,"M37b radial U")
        for j in range(3): close(a.induced_force_on_source_n[j], b.induced_force_on_source_n[j], "M37b radial force")
    result["examples"]["radial_compatibility"] = {"matched":len(old.samples)}
    crossing_x0=(-.4,.05,0.)
    times=[4*i/3 for i in range(4)]
    sample_distances=[math.hypot(-.4+.2*t,.05) for t in times]
    assert all(d>.11 for d in sample_distances)
    result["attacks"].append(must_reject(
        lambda: spec_for(1e-9,crossing_x0,(0.,0.,0.),(.2,0.,0.),4.,count=4,guard=.01),
        "continuous path", "hidden between 4 individually safe saved frames"))
    result["examples"]["crossing_safe_stored_distances_m"] = sample_distances

    for y in (.11, .11 + 1e-16):
        result["attacks"].append(must_reject(
            lambda y=y: spec_for(1e-9,(-.4,y,0.),(0.,0.,0.),(.2,0.,0.),4.,count=4,guard=.01),
            "continuous path", f"unresolved tangent y={y:.17g}"))
    near = sample_prescribed_sphere_line(
        spec_for(1e-9,(-.4,.11+1e-13,0.),(0.,0.,0.),(.2,0.,0.),4.,count=4,guard=.01))
    autonomous_si_audit(json.loads(json.dumps(near.as_dict())))
    # Constrained minimizer on exact interval boundaries (not unbounded line).
    start = spec_for(1e-9,(.2,.15,.15),(0.,0.,0.),(.04,.02,.01),.5)
    end = spec_for(1e-9,(.2,.15,.15),(0.,0.,0.),(-.04,-.02,-.01),.5)
    close(start.closest_approach[0],0.,"start-constrained closest")
    close(end.closest_approach[0],.5,"end-constrained closest")
    autonomous_si_audit(json.loads(json.dumps(sample_prescribed_sphere_line(start).as_dict())))
    autonomous_si_audit(json.loads(json.dumps(sample_prescribed_sphere_line(end).as_dict())))
    result["examples"]["endpoint_constrained_closest"] = [start.closest_approach,end.closest_approach]

    attacks = [
      (("samples",0,"time_s"), False, "non-Boolean", "Boolean zero timestamp"),
      (("samples",0,"index"), False, "index/order", "Boolean index"),
      (("samples",0,"wire_current_sphere_to_ground_a"), -1., "wire_current_sphere_to_ground", "forged signed terminal current"),
      (("samples",0,"wire_current_ground_to_sphere_a"), 1., "wire_current_ground_to_sphere", "forged reverse terminal"),
      (("source_charge_c",), -1e-9, "induced_sphere_net_charge", "forged source charge sign"),
      (("samples",2,"induced_force_on_source_n",2), 3., "induced force", "forged force component"),
      (("samples",2,"induced_mechanical_energy_j"),0., "energy", "forged half-factor energy"),
      (("samples",20,"source_position_m",1),0., "physical x1", "forged Cartesian coordinate"),
      (("closest_approach_time_s",),1.1, "closest-approach physical time", "forged closest time"),
      (("closest_approach_distance_m",),.1, "closest-approach distance", "forged closest distance"),
      (("units","current"),"mA", "SI unit", "forged unit"),
      (("source_role",),"original_p8_offaxis", "workbook", "forged JEE attribution"),
      (("sphere_constraint",),"FixedNetCharge", "grounded", "forged constraint"),
      (("sphere_is_solid",),False, "grounded solid", "forged physical status"),
    ]
    for path,new_value,keyword,label in attacks:
        forged = json.loads(json.dumps(example))
        node = forged
        for key in path[:-1]: node=node[key]
        node[path[-1]]=new_value
        result["attacks"].append(must_reject(lambda f=forged: check_line_record(f), keyword, label))

    native = sample_prescribed_sphere_line(spec_for(1e-9,(-.4,.2,0.),(0.,0.,0.),(.2,0.,0.),4.))
    fake_row=replace(native.samples[0],time_s=False)
    fake_trace=replace(native,samples=(fake_row,)+native.samples[1:])
    result["attacks"].append(must_reject(
       lambda: validate_prescribed_sphere_line(fake_trace),
       "native re-execution", "dataclasses.replace fake native trace"))
    result["attacks"].append(must_reject(
       lambda: fake_trace.as_dict(),
       "native re-execution", "dataclasses.replace fake JSON export"))
    mutated=spec_for(1e-9,(-.4,.2,0.),(0.,0.,0.),(.2,0.,0.),4.)
    object.__setattr__(mutated.problem.charges[0],"charge_c",False)
    result["attacks"].append(must_reject(
       lambda: sample_prescribed_sphere_line(mutated),
       "moving charge", "nested frozen typed spec object.__setattr__ Boolean charge"))

    assert len(result["attacks"])>=20
    Path(out).write_text(json.dumps(result,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    print("REVIEWER FIRST-ATTEMPT native SI: 41 rows + 23 non-coplanar reversed-q rows + 13 radial + guard boundary cases")
    print("REVIEWER FIRST-ATTEMPT hostile refusals:",len(result["attacks"]))
    print(json.dumps(result["examples"],indent=2))
    print("REVIEWER AUTHORED PROBES PASS")


if __name__=="__main__":
    main(sys.argv[1])
