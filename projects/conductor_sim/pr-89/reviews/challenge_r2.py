"""Corrected-source R2 replay + independently added adversarial suite.
Run: PYTHONPATH=<source>/src:<source> python challenge_chat_b.py SOURCE EVIDENCE
Production is never modified. Unexpected acceptance is a failed review test;
setup/execution errors are recorded separately, not called physical refusals.
"""
from __future__ import annotations
import ast
from copy import deepcopy
from dataclasses import replace
import importlib.util
import json
from math import fsum, hypot, isclose, sqrt, ulp
from pathlib import Path
import re
import subprocess
import sys
import traceback

from r2_kelvin_oracle import EPS, reference

SOURCE = Path(sys.argv[1]).resolve()
OUT = Path(sys.argv[2]).resolve()
OUT.mkdir(parents=True, exist_ok=True)
sys.path[:0] = [str(SOURCE / 'src'), str(SOURCE)]
from conductor_sim import (ElectrostaticProblem, ExternalGroundedSphereBackend,
    FixedNetCharge, Grounded, Motion1DSpec, PointCharge, SolidSphere,
    SphericalShell, integrate_motion_1d, observe_grounded_sphere_wire,
    observe_grounded_sphere_motion)
from conductor_sim.motion_1d import MotionEvent
from conductor_sim.solver import UnsupportedProblem
from tools.m37a_ground_wire_reference import validate_examples, check_instant

EXPECTED_HEAD = 'adfe9098742c663e9f4132c3e29e86dddf7ecc1e'
EXPECTED_TREE = '43f8ebae4937eacc25143fdace324115edcfb2d0'
def git(*args):
    return subprocess.check_output(['git', '-C', str(SOURCE), *args], text=True).strip()
assert git('rev-parse', 'HEAD') == EXPECTED_HEAD
assert git('rev-parse', 'HEAD^{tree}') == EXPECTED_TREE
RESULTS = []
WORLDS = {}


def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2, allow_nan=False) + '\n')


def run(name, call, expectation='accept', reason=''):
    try:
        value = call()
    except (ValueError, TypeError, UnsupportedProblem) as exc:
        intended = expectation == 'reject' and bool(re.search(reason, str(exc), re.I))
        item = dict(name=name, expectation=expectation,
                    outcome='REJECTED_AS_INTENDED' if intended else 'WRONG_REFUSAL_OR_EXECUTION_ERROR',
                    exception=type(exc).__name__, reason=str(exc))
        if not intended:
            item['traceback'] = traceback.format_exc()
    except AssertionError as exc:
        item = dict(name=name, expectation=expectation, outcome='ASSERTION_FAILED',
                    reason=str(exc), traceback=traceback.format_exc())
    except Exception as exc:
        item = dict(name=name, expectation=expectation, outcome='SETUP_OR_EXECUTION_ERROR',
                    reason=repr(exc), traceback=traceback.format_exc())
    else:
        outcome = ('UNEXPECTED_ACCEPTANCE' if expectation == 'reject' else
                   'ACCEPTED_DOCUMENTED_LIMITATION' if expectation == 'limitation' else 'PASS')
        item = dict(name=name, expectation=expectation, outcome=outcome, details=value)
    RESULTS.append(item)
    print(json.dumps(item, default=str, sort_keys=True), flush=True)


def near(actual, expected, scale=None, rel=3e-8):
    tolerance = 256 * ulp(abs(expected))
    if scale is not None:
        tolerance = max(tolerance, 2e-12 * abs(scale))
    assert isclose(actual, expected, rel_tol=rel, abs_tol=tolerance), (actual, expected, tolerance)


def problem(q=2.4e-9, a=.083, d=.247, center=(0., 0., 0.),
            axis=(0., 0., 1.), eps=EPS, constraint=None):
    x = tuple(center[i] + d * axis[i] for i in range(3))
    return ElectrostaticProblem((PointCharge(q, x),),
        (SolidSphere(a, Grounded() if constraint is None else constraint, center,
                     'Reviewer sphere R'),), permittivity_f_per_m=eps)


def native_q(p):
    return ExternalGroundedSphereBackend().solve(p).conductor_results[0].net_charge_c


def test_state(p, velocity):
    obs = observe_grounded_sphere_wire(p, velocity)
    s, q = p.conductors[0], p.charges[0]
    ref = reference(q.charge_c, s.radius_m, s.center_m, q.position_m, velocity,
                    p.permittivity_f_per_m)
    assert obs.point_charge_c == q.charge_c
    assert obs.sphere_name == s.name
    assert obs.sphere_center_m == s.center_m
    assert obs.source_position_m == q.position_m
    assert obs.source_velocity_m_s == tuple(velocity)
    assert obs.permittivity_f_per_m == p.permittivity_f_per_m
    near(obs.distance_from_center_m, ref['distance'])
    near(obs.radial_velocity_m_s, ref['radial_speed'], hypot(*velocity))
    near(obs.induced_sphere_net_charge_c, ref['metal_charge'])
    near(native_q(p), ref['metal_charge'])
    current_scale = abs(q.charge_c) * s.radius_m * hypot(*velocity) / ref['distance']**2
    near(obs.wire_current_sphere_to_ground_a, ref['current'], current_scale)
    near(obs.wire_current_ground_to_sphere_a, -ref['current'], current_scale)
    near(obs.induced_net_charge_rate_c_per_s, ref['charge_rate'], current_scale)
    for actual, expected in zip(obs.induced_force_on_source_n, ref['force']):
        near(actual, expected, abs(ref['force_scalar']))
    near(obs.induced_mechanical_energy_j, ref['energy'])
    near(2 * obs.induced_mechanical_energy_j, q.charge_c * ref['reaction_potential'])
    speed = hypot(*velocity)
    h = 1e-5 * (ref['distance'] - s.radius_m) / speed
    def shifted(t):
        return replace(p, charges=(PointCharge(q.charge_c,
            tuple(q.position_m[i] + t * velocity[i] for i in range(3))),))
    finite_difference = -(native_q(shifted(h)) - native_q(shifted(-h))) / (2*h)
    assert abs(finite_difference - ref['current']) <= 3e-7 * current_scale + 256*ulp(abs(ref['current'])), (finite_difference, ref)
    # Independent derivative of induced mechanical energy gives the force.
    dh = 1e-5 * (ref['distance'] - s.radius_m)
    n = tuple((q.position_m[i] - s.center_m[i]) / ref['distance'] for i in range(3))
    def energy_at(offset):
        x = tuple(q.position_m[i] + offset*n[i] for i in range(3))
        return reference(q.charge_c, s.radius_m, s.center_m, x, velocity,
                         p.permittivity_f_per_m)['energy']
    near(-(energy_at(dh)-energy_at(-dh))/(2*dh), ref['force_scalar'], rel=3e-7)
    check_instant(json.loads(json.dumps(obs.as_dict())))
    return dict(reference=ref, native_charge_fd_current_a=finite_difference,
                observed_current_a=obs.wire_current_sphere_to_ground_a)


n = (2/7, 3/7, 6/7)
tangent = (-3/sqrt(13), 2/sqrt(13), 0.)
for sign in (-1, 1):
    for world, center, axis, d, eps in (
        ('axis', (0.,0.,0.), (0.,0.,1.), .247, EPS),
        ('translated-oblique', (.125,-.25,.375), n, .247, 2.7*EPS),
        ('near-surface', (0.,0.,0.), n, .083*(1+2e-4), EPS)):
        t = (1.,0.,0.) if world == 'axis' else tangent
        for vname, rv, tv in (('inward',-.073,.11), ('outward',.049,.07), ('tangent',0.,.13)):
            v = tuple(rv*axis[i] + tv*t[i] for i in range(3))
            p = problem(q=sign*2.4e-9, center=center, axis=axis, d=d, eps=eps)
            run(f'physics/{sign}/{world}/{vname}', lambda p=p,v=v: test_state(p,v))


def test_motion(label, p, mass, axis, v, duration, interval, guard=None, termination='duration', turning=False):
    spec = Motion1DSpec(p, 0, mass, axis, v, duration, interval, surface_guard_m=guard)
    motion = integrate_motion_1d(spec, ExternalGroundedSphereBackend())
    WORLDS[label] = motion
    write(label+'-native-motion.json', motion.as_dict())
    trace = observe_grounded_sphere_motion(motion)
    write(label+'-trace.json', trace.as_dict())
    assert motion.termination == termination
    assert trace.motion is motion
    assert len(trace.observations) == len(motion.samples)
    initial = motion.samples[0]
    assert initial.time_s == 0 and initial.velocity_m_s == v
    assert initial.displacement_m == 0 and initial.position_m == p.charges[0].position_m
    prev = -1.
    max_drift = 0.
    reference_energies = []
    native_charges = []
    for row, obs in zip(motion.samples, trace.observations):
        assert prev < row.time_s <= duration
        prev = row.time_s
        x = tuple(p.charges[0].position_m[i] + spec.axis[i]*row.displacement_m for i in range(3))
        assert x == row.position_m
        velocity = tuple(spec.axis[i]*row.velocity_m_s for i in range(3))
        pp = replace(p, charges=(PointCharge(p.charges[0].charge_c, x),))
        ref = test_state(pp, velocity)
        r = ref['reference']
        f = fsum(r['force'][i]*spec.axis[i] for i in range(3))
        near(row.force_n, f)
        near(row.acceleration_m_s2, f/mass)
        kinetic = .5*mass*row.velocity_m_s*row.velocity_m_s
        near(row.kinetic_energy_j, kinetic)
        near(row.interaction_energy_j, r['energy'])
        near(row.total_energy_j, kinetic+r['energy'], abs(kinetic)+abs(r['energy']))
        reference_energies.append((kinetic, r['energy']))
        independent_drift = fsum((kinetic-reference_energies[0][0], r['energy']-reference_energies[0][1]))
        scale = sum(abs(z) for z in (*reference_energies[0],kinetic,r['energy']))
        assert abs(row.energy_drift_j-independent_drift) <= 5e-13*scale+3e-8*abs(independent_drift)
        stored_drift = fsum((row.kinetic_energy_j-initial.kinetic_energy_j,
                            row.interaction_energy_j-initial.interaction_energy_j))
        near(row.energy_drift_j, stored_drift)
        max_drift = max(max_drift,abs(row.energy_drift_j))
        assert obs.point_charge_c == p.charges[0].charge_c and obs.sphere_name == p.conductors[0].name
        assert obs.source_position_m == row.position_m
        native_charges.append(native_q(pp))
        assert obs.distance_from_center_m > p.conductors[0].radius_m + (guard or 1e-6*p.conductors[0].radius_m)
    near(motion.max_abs_energy_drift_j,max_drift)
    fd_count = 0
    if termination == 'duration':
        assert motion.samples[-1].time_s == duration
        # Real integrated timestamps and native equilibria, not a linear path.
        currents = [o.wire_current_sphere_to_ground_a for o in trace.observations]
        scale = max(map(abs,currents))
        for i in range(1,len(motion.samples)-1):
            before,mid,after = motion.samples[i-1:i+2]
            if abs((after.time_s-mid.time_s)-(mid.time_s-before.time_s)) > 1e-12:
                continue
            derivative = -(native_charges[i+1]-native_charges[i-1])/(after.time_s-before.time_s)
            assert abs(derivative-currents[i]) <= .004*scale, (i,derivative,currents[i])
            fd_count += 1
        assert fd_count >= 5
    else:
        assert motion.events[-1].kind == 'surface-guard'
        assert motion.events[-1].time_s == motion.samples[-1].time_s < duration
        assert motion.events[-1].position_m == motion.samples[-1].position_m
    if turning:
        assert any(e.kind == 'turning-point' for e in motion.events)
        assert motion.samples[0].velocity_m_s > 0 and motion.samples[-1].velocity_m_s < 0
    return dict(samples=len(motion.samples), final_time_s=motion.samples[-1].time_s,
                termination=motion.termination, events=[e.kind for e in motion.events],
                native_time_difference_checks=fd_count, max_energy_drift_j=max_drift)

run('motion/inward',lambda:test_motion('inward',problem(center=(.125,-.25,.375),axis=n),.002,n,-.06,.08,.005))
run('motion/outward-negative',lambda:test_motion('outward',problem(q=-3.1e-9,d=.23,center=(-.5,.25,.125),axis=n),.001,n,.09,.12,.01))
run('motion/guard-negative',lambda:test_motion('guard',problem(q=-1.7e-9,a=.09,d=.131,axis=(-1.,0.,0.)),2e-6,(-1.,0.,0.),-.27,.3,.01,3e-4,'surface-guard'))
run('motion/turning',lambda:test_motion('turning',problem(q=1e-9,a=.08,d=.23),1e-6,(0.,0.,1.),.01,.35,.005,turning=True))


def attack_motion(name, transform, reason):
    def challenge():
        m = WORLDS['inward']
        altered = transform(m)
        write('attack-native-'+name+'.json',altered.as_dict())
        return observe_grounded_sphere_motion(altered).as_dict()
    run('native/'+name,challenge,'reject',reason)


def modify_row(m, **kwargs):
    rows=list(m.samples)
    rows[2]=replace(rows[2],**kwargs)
    return replace(m,samples=tuple(rows))

attack_motion('locally-correct-monotonic-time',lambda m:modify_row(m,time_s=m.samples[2].time_s+.0013),'independently rerun M16a')
attack_motion('locally-correct-velocity-sign',lambda m:modify_row(m,velocity_m_s=-m.samples[2].velocity_m_s),'independently rerun M16a')
attack_motion('method',lambda m:replace(m,method='FEMM transient Maxwell solver'),'method')
attack_motion('made-up-turning',lambda m:replace(m,events=(MotionEvent('turning-point',m.samples[2].time_s,m.samples[2].displacement_m,m.samples[2].position_m,'Fabricated but geometrically consistent turning'),)),'independently rerun M16a')
attack_motion('made-up-surface',lambda m:replace(m,events=(MotionEvent('surface-guard',m.samples[2].time_s,m.samples[2].displacement_m,m.samples[2].position_m,'Fabricated approach'),)),'impossible surface guard')
attack_motion('unknown-event',lambda m:replace(m,events=(MotionEvent('rebound',m.samples[2].time_s,m.samples[2].displacement_m,m.samples[2].position_m,'Unsupported collision'),)),'invalid event')
attack_motion('force-sign',lambda m:modify_row(m,force_n=-m.samples[2].force_n),'force.*Kelvin')
attack_motion('energy-no-half',lambda m:modify_row(m,interaction_energy_j=2*m.samples[2].interaction_energy_j),'interaction energy.*Kelvin')
attack_motion('boolean-time',lambda m:modify_row(m,time_s=True),'Boolean')
attack_motion('boolean-velocity',lambda m:modify_row(m,velocity_m_s=False),'Boolean')
attack_motion('changed-source-magnitude',lambda m:replace(m,spec=replace(m.spec,problem=replace(m.spec.problem,charges=(replace(m.spec.selected_charge,charge_c=1.1*m.spec.selected_charge.charge_c),)))),'Kelvin')
attack_motion('changed-permittivity',lambda m:replace(m,spec=replace(m.spec,problem=replace(m.spec.problem,permittivity_f_per_m=2*EPS))),'Kelvin')
attack_motion('fake-maximum-drift',lambda m:replace(m,max_abs_energy_drift_j=1e-3),'maximum energy drift')
attack_motion('false-position',lambda m:modify_row(m,position_m=(.4,.5,.6)),'position contradicts')

p = problem()
for label, bad in (
    ('isolated',replace(p,conductors=(replace(p.conductors[0],constraint=FixedNetCharge(0.)),))),
    ('shell',replace(p,conductors=(SphericalShell(.04,.083,Grounded()),))),
    ('extra-source',replace(p,charges=(*p.charges,PointCharge(7e-10,(.2,.3,.4))))),
    ('extra-metal',replace(p,conductors=(*p.conductors,SolidSphere(.04,Grounded(),(2.,0.,0.),'Second')))),
    ('zero-charge',problem(q=0.)), ('inside',problem(d=.07)), ('touching',problem(d=.083))):
    run('domain/'+label,lambda bad=bad:observe_grounded_sphere_wire(bad,(0.,0.,-.06)).as_dict(),
        'reject','one point charge|grounded solid sphere|strictly outside')
run('domain/boolean-prescribed-velocity',lambda:observe_grounded_sphere_wire(p,(True,0.,0.)).as_dict(),'reject','boolean|number')
run('domain/boolean-source-charge',lambda:observe_grounded_sphere_wire(problem(q=True),(0.,0.,-.06)).as_dict(),'reject','boolean|number|charge')
run('domain/boolean-permittivity',lambda:observe_grounded_sphere_wire(problem(eps=True),(0.,0.,-.06)).as_dict(),'reject','boolean|number|permittivity')
run('domain/boolean-radius',lambda:observe_grounded_sphere_wire(problem(a=True,d=2.),(0.,0.,-.06)).as_dict(),'reject','boolean|number|radius')

example = OUT/'genuine-example.json'
subprocess.run([sys.executable,str(SOURCE/'examples/grounded_sphere_wire_current.py'),'--output',str(example)],check=True)
genuine = json.loads(example.read_text())
run('checker/genuine-file',lambda:validate_examples(genuine))
run('checker/standalone-cli',lambda:subprocess.run([sys.executable,str(SOURCE/'tools/m37a_ground_wire_reference.py'),'--input',str(example)],check=True,capture_output=True,text=True).stdout)


def no_production_imports():
    imports=[]
    tree=ast.parse((SOURCE/'tools/m37a_ground_wire_reference.py').read_text())
    for node in ast.walk(tree):
        if isinstance(node,ast.Import): imports.extend(a.name for a in node.names)
        elif isinstance(node,ast.ImportFrom): imports.append(node.module)
        elif isinstance(node,ast.Call) and isinstance(node.func,ast.Name):
            assert node.func.id not in ('__import__','exec','eval')
    assert set(imports) <= {'__future__','argparse','json','math','pathlib'}
    return imports
run('checker/no-production-imports',no_production_imports)


def json_attack(name, edit, reason, expectation='reject'):
    def challenge():
        doc=deepcopy(genuine)
        edit(doc)
        write('attack-json-'+name+'.json',doc)
        return validate_examples(doc)
    run('json/'+name,challenge,expectation,reason)

def inst(d): return d['instantaneous_prescribed'][0]
def trace(d): return d['actual_elapsed_time']
def motion(d): return trace(d)['motion']
def obs(d): return trace(d)['observations'][2]
def row(d): return motion(d)['samples'][2]

for name,edit,reason in (
 ('current-sign',lambda d:inst(d).__setitem__('wire_current_sphere_to_ground_a',-inst(d)['wire_current_sphere_to_ground_a']),'wire_current_sphere_to_ground'),
 ('opposite-terminal',lambda d:inst(d).__setitem__('wire_current_ground_to_sphere_a',inst(d)['wire_current_sphere_to_ground_a']),'wire_current_ground_to_sphere'),
 ('charge-with-current-intact',lambda d:inst(d).__setitem__('induced_sphere_net_charge_c',-inst(d)['induced_sphere_net_charge_c']),'induced_sphere_net_charge'),
 ('negative-source-wrong-signs',lambda d:inst(d).__setitem__('point_charge_c',-inst(d)['point_charge_c']),'induced_sphere_net_charge'),
 ('boolean-charge',lambda d:inst(d).__setitem__('point_charge_c',True),'Boolean'),
 ('boolean-time',lambda d:row(d).__setitem__('time_s',True),'Boolean'),
 ('boolean-velocity',lambda d:inst(d).__setitem__('source_velocity_m_s',[0,True,0]),'Boolean'),
 ('false-center',lambda d:inst(d).__setitem__('sphere_center_m',[.01,-.02,.03]),'distance_from_center'),
 ('false-source-position',lambda d:inst(d).__setitem__('source_position_m',[.01,.02,.3]),'distance_from_center'),
 ('force',lambda d:inst(d).__setitem__('induced_force_on_source_n',[0,0,1]),'physical induced force'),
 ('energy-no-half',lambda d:inst(d).__setitem__('induced_mechanical_energy_j',2*inst(d)['induced_mechanical_energy_j']),'induced_mechanical_energy'),
 ('permittivity',lambda d:inst(d).__setitem__('permittivity_f_per_m',2*inst(d)['permittivity_f_per_m']),'energy|force'),
 ('original-givens-attribution',lambda d:d.__setitem__('source_role','Original printed q=1 nC and a=.1 m'),'provenance'),
 ('instant-mode',lambda d:inst(d).__setitem__('mode','actual simulated trajectory'),'prescribed instant'),
 ('units-current',lambda d:inst(d)['units'].__setitem__('current','mA'),'unit'),
 ('units-energy',lambda d:inst(d)['units'].__setitem__('energy','eV'),'unit'),
 ('units-time',lambda d:motion(d)['units'].__setitem__('time','ms'),'unit'),
 ('missing-units',lambda d:inst(d).pop('units'),'unit'),
 ('sphere-identity-midtrace',lambda d:obs(d).__setitem__('sphere_name','Different physical conductor'),'sphere|identity|source'),
 ('motion-method',lambda d:motion(d).__setitem__('method','FEMM time-dependent electron drift'),'method|source|origin'),
 ('motion-mode',lambda d:motion(d).__setitem__('mode','prescribed animation, not dynamics'),'mode|origin'),
 ('trace-current-sign-label',lambda d:trace(d).__setitem__('current_sign','sphere_to_ground positive for electron flux'),'sign|convention')):
    json_attack(name,edit,reason)


def consistent_timestamp_forgery(d):
    t=row(d)['time_s']+.003
    row(d)['time_s']=t
    obs(d)['time_s']=t
json_attack('monotonic-time-static-checker-limit',consistent_timestamp_forgery,'','limitation')


# ----------------------------------------------------------------------
# R2 reviewer-authored additions beyond the old independent challenge list.
# Deliberately challenge source/export fields outside the repaired F1-F3
# exemplars, including maxima and terminal-event bookkeeping.
# All hostile inputs begin from a genuinely generated, valid native record.
# ----------------------------------------------------------------------
run('r2/physics/new-negative-oblique-world',
    lambda: test_state(problem(q=-3.7e-9,a=.071,d=.303,
        center=(.4,-.8,1.2),axis=n,eps=.61*EPS),
        tuple(-.037*n[i]+.019*tangent[i] for i in range(3))))
run('r2/domain/boolean-false-charge',
    lambda: observe_grounded_sphere_wire(problem(q=False),(0.,0.,-.075)).as_dict(),
    'reject', 'source charge|boolean')
run('r2/domain/nan-charge-constructor',
    lambda: observe_grounded_sphere_wire(problem(q=float("nan")),(0.,0.,-.075)).as_dict(),
    'reject', 'finite')
run('r2/domain/infinite-permittivity-constructor',
    lambda: observe_grounded_sphere_wire(problem(eps=float("inf")),(0.,0.,-.075)).as_dict(),
    'reject', 'finite')
run('r2/domain/overlarge-source',
    lambda: observe_grounded_sphere_wire(problem(q=1e200),(0.,0.,-.075)).as_dict(),
    'reject', 'finite|overflow|represent|range|large')
run('r2/domain/speed-cutoff',
    lambda: observe_grounded_sphere_wire(problem(),(0.,0.,3.0e7)).as_dict(),
    'reject', 'speed cutoff')
def authentic_r2_roundtrip():
    q=-3.4e-9
    p=problem(q=q,a=.074,d=.201,center=(.4,-.2,.1),axis=n,eps=1.7*EPS)
    obs=observe_grounded_sphere_wire(p,tuple(-.051*n[i] for i in range(3)))
    saved=obs.as_dict()
    for field in ('point_charge_c','sphere_radius_m','permittivity_f_per_m'):
        assert type(saved[field]) in (float,int), (field,type(saved[field]))
    check_instant(json.loads(json.dumps(saved,allow_nan=False)))
    return dict(current=obs.wire_current_sphere_to_ground_a, units=saved['units'])
run('r2/export/authentic-numeric-roundtrip',authentic_r2_roundtrip)

# F2: units are exact declarations, not ignored labels or optional metadata.
for title,edit in (
 ('nested-units-absent',lambda d:motion(d).pop('units')),
 ('nested-acceleration-ms',lambda d:motion(d)['units'].__setitem__('acceleration','m/s')),
 ('nested-force-dyne',lambda d:motion(d)['units'].__setitem__('force','dyn')),
 ('instant-force-dyne',lambda d:inst(d)['units'].__setitem__('force','dyn')),
 ('instant-velocity-kmh',lambda d:inst(d)['units'].__setitem__('velocity','km/h')),
 ('instant-extra-unit-key',lambda d:inst(d)['units'].__setitem__('temperature','K')),
 ('motion-extra-unit-key',lambda d:motion(d)['units'].__setitem__('charge','C')),
 ('non-map-unit-record',lambda d:inst(d).__setitem__('units',['A','J']))
):
    json_attack('r2-'+title,edit,'declared SI units|SI units|missing or inconsistent')

# F3: a third sample is modified, leaving all other genuine data in place.
# Check rejection at physical SI or fixed identity, not missing-schema setup.
for title,edit,why in (
 ('different-name',lambda d:obs(d).__setitem__('sphere_name','Renamed sphere R2'),'identity'),
 ('different-center',lambda d:obs(d).__setitem__('sphere_center_m',[.004,0.,0.]),'SI|distance|force|energy|radial'),
 ('different-radius',lambda d:obs(d).__setitem__('sphere_radius_m',.131),'SI|induced|distance|force|energy'),
 ('different-permittivity',lambda d:obs(d).__setitem__('permittivity_f_per_m',2.5*EPS),'SI|force|energy'),
 ('wrong-third-unit',lambda d:obs(d)['units'].__setitem__('current','mA'),'SI units'),
 ('false-regime',lambda d:trace(d).__setitem__('physics_regime','FEMM full-wave electron drift'),'physical regime'),
 ('missing-third-name',lambda d:obs(d).__setitem__('sphere_name',None),'sphere name'),
 ('wrong-third-source-sign',lambda d:obs(d).__setitem__('point_charge_c',-obs(d)['point_charge_c']),'SI|induced')
):
    json_attack('r2-'+title,edit,why)

# Novel local-consistency questions.  Unlike the documented timestamp/ODE
# limitation, these summaries are individually checkable from exported data.
# A reviewer failure here is preserved; it is not turned into a waiver.
json_attack('r2-false-max-drift',
    lambda d:motion(d).__setitem__('max_abs_energy_drift_j',1e9),
    'maximum|energy drift|max_abs')
json_attack('r2-negative-surface-guard',
    lambda d:motion(d).__setitem__('guard_m',-.3),
    'guard|outside|physical|domain')
def fabricated_duration_event(d):
    m=motion(d)
    sample=m['samples'][2]
    m['events'].append(dict(kind='surface-guard',time_s=sample['time_s'],
       displacement_m=sample['displacement_m'],
       position_m=sample['position_m'],
       description='False contact claim during duration-complete motion'))
json_attack('r2-false-surface-event-on-duration',fabricated_duration_event,
    'surface|guard|event|duration')

failures=[x for x in RESULTS if x['outcome'] not in ('PASS','REJECTED_AS_INTENDED','ACCEPTED_DOCUMENTED_LIMITATION')]
summary=dict(source_head=git('rev-parse','HEAD'),source_tree=git('rev-parse','HEAD^{tree}'),
             python=sys.version,total=len(RESULTS),passed=len(RESULTS)-len(failures),
             failures=len(failures),outcomes=RESULTS,
             source_worktree_status=git('status','--porcelain','--untracked-files=no'))
assert summary['source_worktree_status']==''
write('independent-results.json',summary)
print('CHAT_B_SUMMARY '+json.dumps({k:v for k,v in summary.items() if k!='outcomes'}),flush=True)
sys.exit(1 if failures else 0)
