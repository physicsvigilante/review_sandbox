#!/usr/bin/env python3
"""Reviewer-owned JEE-12 PR109 direct released-API reproducer.

This does not import developer JEE-12 probes, developer test code or
saved CI answer JSON. PDF visual inspection is a separate requirement.
"""
import json
from pathlib import Path
from math import isclose, pi, sqrt
from conductor_sim import (EPSILON_0, PrescribedField, UniformElectricField,
 ElectrostaticProblem, FixedNetCharge, Grounded, PointCharge, SolidSphere,
 SphericalShell, MixedRadialBackend, NestedShellBackend, ConnectedShellBackend,
 ConnectionPlan, ElectricalLink, TestChargeMotionSpec,
 observe_grounded_sphere_wire)
from conductor_sim.jee_potential_explorer import endpoint_field_work
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.motion_events import (EventStudy, EventPolicy, VelocityReversal,
 PlaneEvent, investigate_motion)
from conductor_sim.cavity_gauss import (CavityCharge, SealedCavity, GaussCavityAssembly,
 solve_cavity_gauss)
from conductor_sim.spherical_multicavity import (NamedSourcePosition, SphericalVoid,
 SphericalMetalGeometry, SphericalSigmaModel, solve_spherical_sigma)
from conductor_sim.solver import UnsupportedProblem

E_CHARGE=1.602176634e-19
M_E=9.1093837139e-31
K=1/(4*pi*EPSILON_0)
report={}
def near(label, measured, predicted, rel=1e-10, abs_=1e-19):
    if not isclose(measured,predicted,rel_tol=rel,abs_tol=abs_):
        raise AssertionError(f'{label}: measured={measured!r}, independent={predicted!r}')
def record(key, **kwargs):
    report[key]=kwargs
    print('PASS',key,json.dumps(kwargs,allow_nan=False),flush=True)

# p1: public endpoint work; there is no simulated free electron path.
field=PrescribedField((UniformElectricField((10.,0.,0.)),))
work=endpoint_field_work(field,source_annotations=(('prescribed','uniform source'),),
    probe_charge_c=-E_CHARGE,start_m=(1.,-2.,0.),end_m=(5.,1.,0.))
near('p1 external',work['external_quasistatic_work_j']/E_CHARGE,+40.)
near('p1 field',work['field_work_j']/E_CHARGE,-40.)
record('p01',external_eV=work['external_quasistatic_work_j']/E_CHARGE,
    field_eV=work['field_work_j']/E_CHARGE,mode='static endpoint work')

# p2: original K0 and sheet sigma; 1 mm is explicitly a teacher launch gap.
E=2e-6/EPSILON_0
x0=.001
speed=sqrt(2*100*E_CHARGE/M_E)
spec=TestChargeMotionSpec(PrescribedField((UniformElectricField((-E,0.,0.)),)),
    PointCharge(-E_CHARGE,(x0,0.,0.)),M_E,(-speed,0.,0.),
    4e-10,2e-11,plane_normal=(0.,1.,0.),length_scale_m=.01,
    relative_tolerance=1e-9)
scenario=PrescribedScenario('independent-r2-sheet',spec,
    (('physical-sheet','UniformElectricField'),),
    'Teaching gap is not source-given; one-sided prescribed metal field')
study=EventStudy(scenario,(
    VelocityReversal('turn',(1.,0.,0.),'electron x reversal',1,True),
    PlaneEvent('metal',(0.,0.,0.),(1.,0.,0.),'surface x=0',-1,True,'ideal-stop-surface')
),EventPolicy(1e-11,1e-18,1e-12,1e-3))
motion=investigate_motion(study)
event=next(e for e in motion.events if e.event_id=='turn')
distance=x0-event.sample.position_m[0]
near('p2 stopping distance',distance,100/E,rel=3e-7,abs_=1e-10)
near('p2 stopping time',event.sample.time_s,speed/(E_CHARGE*E/M_E),
    rel=3e-5,abs_=5e-14)
assert event.full_stop_within_tolerance and motion.trajectory.termination=='terminal-event'
record('p02',stopping_distance_mm=distance*1000,stop_time_s=event.sample.time_s,
    termination=motion.trajectory.termination,teacher_launch_gap_mm=1.)

# p3: two real native static states with authentic solid and finite metal shell.
original=ElectrostaticProblem(conductors=(
    SolidSphere(.1,FixedNetCharge(20e-6),name='solid'),
    SphericalShell(.199999,.2,FixedNetCharge(0.),name='shell')))
connected=ConnectedShellBackend().solve(ConnectionPlan(
    original,(ElectricalLink(('solid','shell')),)))
independent_energy=K*(20e-6)**2*(1/.1-1/.2)/2
near('p3 static release',connected.released_field_energy_j,
    independent_energy,rel=5e-5,abs_=5e-4)
assert connected.radial_field_energy_before_j>connected.radial_field_energy_after_j
near('p3 final gap field',connected.after.electric_field_at((.15,0.,0.))[0],0.,abs_=1e-5)
record('p03',released_field_energy_j=connected.released_field_energy_j,
    ideal_thin_energy_j=independent_energy,
    state='before-and-after static equilibria, not wire-current waveform')

# p8: grounded sphere, teacher-prescribed velocities, not solved source motion.
currents=[]
for d in (.9,.6):
    problem=ElectrostaticProblem(
        conductors=(SolidSphere(.3,Grounded(),name='ball'),),
        charges=(PointCharge(2e-9,(d,0.,0.)),))
    ans=observe_grounded_sphere_wire(problem,(-.05,0.,0.))
    near('p8 induced charge',ans.induced_sphere_net_charge_c,-2e-9*.3/d)
    near('p8 current',ans.wire_current_sphere_to_ground_a,2e-9*.3*.05/d**2)
    currents.append(ans.wire_current_sphere_to_ground_a)
assert 0<currents[0]<currents[1]
record('p08',sphere_to_ground_current_a=currents,prescribed_speed_m_s=.05)

# Three unfamiliar signed/translated native teacher variations.
variants=((.165,-1.1e-9,.7e-9,-.4e-9,(.13,-.08,.06),.05),
          (.23,2.6e-9,-1.4e-9,1.3e-9,(-.17,.11,.09),.075),
          (.093,-.8e-9,.55e-9,-.7e-9,(.09,.04,-.18),.025))
witnesses=[]
for j,(R,q,q1,q2,origin,shift) in enumerate(variants,1):
    sphere=SolidSphere(R,FixedNetCharge(q),center_m=origin,name='solid')
    physical=MixedRadialBackend().solve(ElectrostaticProblem(conductors=(sphere,)))
    Vi=physical.potential_at((origin[0]+R/2,origin[1],origin[2]))
    Vo=physical.potential_at((origin[0]+1.5*R,origin[1],origin[2]))
    near('p26 V interior',Vi,K*q/R,abs_=1e-11)
    near('p26 V exterior',Vo,K*q/(1.5*R),abs_=1e-11)

    a,b,th,ra,rb=.1,.2,1e-6,.04,.15
    nested=ElectrostaticProblem(conductors=(
        SphericalShell(a-th,a,FixedNetCharge(q1),center_m=origin,name='one'),
        SphericalShell(b-th,b,FixedNetCharge(q2),center_m=origin,name='two')),
        charges=(PointCharge(q,origin),))
    shell=NestedShellBackend().solve(nested)
    VA=shell.potential_at((origin[0]+ra,origin[1],origin[2]))
    VB=shell.potential_at((origin[0]+rb,origin[1],origin[2]))
    expected_A=K*(q/ra-q/(a-th)+(q+q1)/a-(q+q1)/(b-th)+(q+q1+q2)/b)
    expected_B=K*((q+q1)/rb-(q+q1)/(b-th)+(q+q1+q2)/b)
    near('p27 finite V(A)',VA,expected_A,abs_=1e-11)
    near('p27 finite V(B)',VB,expected_B,abs_=1e-11)
    near('p27 inner face',shell.conductor_by_name('one').inner_surface_charge_c,-q)

    ledger=GaussCavityAssembly('metal',(
        SealedCavity('cavity',(CavityCharge('source',q),)),),
        FixedNetCharge(3*q))
    geom=SphericalMetalGeometry(origin,2*R,(
        SphericalVoid('cavity',origin,R,(
            NamedSourcePosition('source',(origin[0]+shift,origin[1],origin[2])),)),))
    solution=solve_spherical_sigma(SphericalSigmaModel(ledger,geom))
    near('p69 inner total',solution.gauss_ledger.faces[0].induced_inner_face_charge_c,-q)
    near('p69 outer total',solution.gauss_ledger.outer_face_charge_c,4*q)
    densities=[]
    for cosine,direction in ((1.,(1.,0.,0.)),(-1.,(-1.,0.,0.))):
        expected=-q*(R*R-shift*shift)/(4*pi*R*(R*R+shift*shift-2*R*shift*cosine)**1.5)
        observed=solution.inner_surface_charge_density('cavity',direction)
        near('p69 local signed density',observed,expected,rel=3e-11)
        densities.append(observed)
    assert not isclose(densities[0],densities[1],rel_tol=.01,abs_tol=0.)
    witnesses.append(dict(index=j,center_m=origin,q_c=q,p26_inside_v=Vi,
        p26_outside_v=Vo,p27_A_v=VA,p27_B_v=VB,p69_sigma=densities))
record('three_unfamiliar_signed_translated_native_variants',values=witnesses)

# p11: original exterior q makes a local irregular-sigma solution unqualified.
gauss=solve_cavity_gauss(GaussCavityAssembly('irregular',(
    SealedCavity('c1',(CavityCharge('q1',.7e-9),)),
    SealedCavity('c2',(CavityCharge('q2',-.2e-9),))),
    FixedNetCharge(.3e-9)))
near('p11 Gauss outer total',gauss.outer_face_charge_c,.8e-9)
refused=[]
for label,fn in (('sigma',lambda:gauss.surface_charge_density_at('outer',(1.,0.,0.))),
                 ('E',lambda:gauss.electric_field_at((2.,0.,0.))),
                 ('V',lambda:gauss.potential_at((2.,0.,0.)))):
    try:fn()
    except UnsupportedProblem:refused.append(label)
assert len(refused)==3
record('p11',outer_face_c=gauss.outer_face_charge_c,external_q_c=-1e-9,
    external_q_not_in_local_solver=True,refused=refused)

# p70: do not infer 3D geometry from a 2D printed cross-section.
gauss3=GaussCavityAssembly('body',tuple(
    SealedCavity('S'+str(i),(CavityCharge('q'+str(i),q),))
    for i,q in enumerate((.6e-9,-.8e-9,1.9e-9),1)),FixedNetCharge(0.))
topology=solve_cavity_gauss(gauss3)
try:topology.surface_charge_density_at('outer',(1.,0.,0.))
except UnsupportedProblem:pass
else:raise AssertionError('topology incorrectly supplied local 3D sigma')
voids=(
    SphericalVoid('S1',(-1.3,0.,0.),.45,(NamedSourcePosition('q1',(-1.3,0.,0.)),)),
    SphericalVoid('S2',(1.4,.8,0.),.5,(NamedSourcePosition('q2',(1.52,.81,.02)),)),
    SphericalVoid('S3',(0.,-1.65,0.),.43,(NamedSourcePosition('q3',(.08,-1.5,.02)),)),
)
teacher=solve_spherical_sigma(SphericalSigmaModel(
    gauss3,SphericalMetalGeometry((0.,0.,0.),4.,voids)))
near('p70 Gauss outer total',teacher.gauss_ledger.outer_face_charge_c,1.7e-9)
sample=teacher.inner_surface_charge_density('S2',(1.,0.,0.))
record('p70',original_local_refusal=True,teacher_3d_sample_sigma_c_m2=sample,
    teacher_geometry_source_given=False)

Path('review02-native-results.json').write_text(
    json.dumps(report,indent=2,allow_nan=False)+'\n',encoding='utf8')
print('REVIEW02_NATIVE_PASS; real released APIs plus three signed/translated variants',flush=True)
