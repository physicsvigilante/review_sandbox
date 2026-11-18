"""Independent reviewer-owned exact-head native/source/browser probes for conductor_sim PR90.
Run from conductor_sim repo root, with review_sandbox code on Python path.
Do not modify the production repository, branch, or supplied original PDF.
"""
import ast
import copy
import json
import math
import re
from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory

from conductor_sim import (
    author_prescribed_grounded_sphere, PrescribedSphereRadialSpec,
    sample_prescribed_sphere_radial, PointCharge,
)
from conductor_sim.grounded_sphere_wire import observe_grounded_sphere_wire
from conductor_sim.prescribed_wire_viewer import viewer_manifest
from tools.m37b_source_approach import run_all, SOURCE
from tools.m37b_source_reference import check as source_check
from tools.check_m37b_prescribed_browser import check as browser_check

OUT=Path('review-outputs')
OUT.mkdir(exist_ok=True)
result={'native_worlds':[],'json_mutations':{},'html_mutations':{},'source':{}}

# The standalone reference must contain no imports of production physics.
source=Path('tools/m37b_source_reference.py').read_text()
for node in ast.walk(ast.parse(source)):
    if isinstance(node,ast.Import):
        assert all(not x.name.startswith('conductor_sim') for x in node.names)
    elif isinstance(node,ast.ImportFrom):
        assert not (node.module or '').startswith('conductor_sim')

with TemporaryDirectory(prefix='independent-m37b-') as tmp:
    folder=Path(tmp)
    genuine=run_all(folder)
    assert source_check(genuine)['verified_python_kelvin_states']==31
    saved=json.loads((folder/'p8-ground-current.json').read_text())
    assert saved==genuine
    result['source']={'states':31,'authentic_json_equal':True,'source_reference_imports_production':False}

    # Unfamiliar hostile datasets, distinct from development tests.
    mutations=[
      ('negative_charge',('trace','source_charge_c'),-1e-9),
      ('radius',('trace','sphere_radius_m'),.105),
      ('epsilon',('trace','permittivity_f_per_m'),1.2e-11),
      ('centre',('trace','sphere_center_m',1),.06),
      ('duration',('trace','duration_s'),4.),
      ('reverse_speed',('trace','signed_constant_radial_speed_m_s'),.04),
      ('timestamp',('trace','samples',23,'time_s'),2.4),
      ('bool_index',('trace','samples',11,'index'),True),
      ('position',('trace','samples',8,'source_position_m',2),.999),
      ('velocity',('trace','samples',8,'source_velocity_m_s',2),.12),
      ('charge_on_sphere',('trace','samples',9,'induced_sphere_net_charge_c'),1e-10),
      ('positive_current',('trace','samples',9,'wire_current_sphere_to_ground_a'),-3e-11),
      ('opposite_current',('trace','samples',9,'wire_current_ground_to_sphere_a'),3e-11),
      ('reversed_force',('trace','samples',17,'induced_force_on_source_n',2),.0001),
      ('wrong_half_energy',('trace','samples',4,'induced_mechanical_energy_j'),genuine['trace']['samples'][4]['induced_mechanical_energy_j']*2),
      ('si_unit',('trace','units','force'),'mN'),
      ('teacher_caption',('source','numeric_attribution'),'Source printed 1nC'),
      ('source_kind',('source','source_kind'),'Official JEE 2026 paper'),
      ('answer_indices',('source','original_correct_option_indices'),[1,2]),
      ('bool_count',('source','original_question_apparatus_count'),True),
      ('extra_false_claim',('source','extra_false_claim'),True),
      ('chart_y',('readouts',6,'chart_y_px'),640.),
      ('readout',('readouts',6,'wire_current_label'),'100 A'),
      ('layout_radius',('layout','sphere_radius_px'),20.),
    ]
    rejected=[]
    for label,path,bad_value in mutations:
        corrupted=copy.deepcopy(genuine)
        item=corrupted
        for key in path[:-1]:item=item[key]
        item[path[-1]]=bad_value
        try:source_check(corrupted)
        except (ValueError,TypeError):rejected.append(label)
        else:raise AssertionError('Source checker incorrectly accepted '+label)
    result['json_mutations']={'attempted':len(mutations),'rejected':len(rejected),'names':rejected}

    # Real Playwright Chromium on genuine viewer, then HTML-only attacks.
    browser_check(folder)
    htmlfile=folder/'p8-ground-current.html'
    original=htmlfile.read_text()
    attacks={
       'static_marker_cx':(r'(<circle id="m37b-current-marker" cx=")[^"]+',r'\g<1>500'),
       'static_time':(r'(<strong id="m37b-time">)[^<]+',r'\g<1>100 s'),
       'static_distance':(r'(<strong class="value" id="m37b-distance">)[^<]+',r'\g<1>999 m'),
       'static_opposite':(r'(<strong class="value" id="m37b-opposite">)[^<]+',r'\g<1>999 A'),
    }
    for label,(search,replacement) in attacks.items():
        forged,n=re.subn(search,replacement,original,count=1)
        assert n==1,label
        htmlfile.write_text(forged)
        try:browser_check(folder)
        except Exception as exc:result['html_mutations'][label]={'browser_checker_accepted':False,'error':repr(exc)}
        else:result['html_mutations'][label]={'browser_checker_accepted':True}
        finally:htmlfile.write_text(original)
    assert result['html_mutations']['static_marker_cx']['browser_checker_accepted'] is True, 'Known reviewer no-JS marker blind spot not reproduced'
    # This is a NEGATIVE finding: allowing HTML-only forgery means release
    # browser checker passed despite invalid offline first-frame physical display.

# Three novel reviewer scientific worlds: original source attribution forbidden.
worlds=[
 ('negative_inward',-2.31e-9,-.019,(-.35,.71,.42),(2/7,3/7,6/7),4.2e-11,.11,.29,.57),
 ('positive_outward',1.67e-9,.023,(.4,-.8,.1),(-3/7,6/7,2/7),1.9e-11,.085,.22,.64),
 ('near_guard',8.1e-10,-.00004,(.02,.05,.4),(0,1,0),8.8541878128e-12,.13,.131,.9),
]
for label,q,v,c,axis,epsilon,radius,d0,duration in worlds:
    assert math.isclose(math.hypot(*axis),1.,rel_tol=1e-12)
    p0=tuple(c[j]+axis[j]*d0 for j in range(3))
    problem=author_prescribed_grounded_sphere(q,p0,radius,sphere_center_m=c,permittivity_f_per_m=epsilon)
    trace=sample_prescribed_sphere_radial(PrescribedSphereRadialSpec(problem,v,duration,9,1e-6))
    for row in trace.samples:
        d=d0+v*row.time_s
        image_charge=-q*radius/d
        image_distance=radius**2/d
        K=1/(4*math.pi*epsilon)
        true_force=K*q*image_charge/(d-image_distance)**2
        true_U=.5*K*q*image_charge/(d-image_distance)
        true_I=-q*radius*v/(d*d)
        for actual,expected in (
            (row.radial_distance_m,d),
            (row.induced_sphere_net_charge_c,image_charge),
            (row.wire_current_sphere_to_ground_a,true_I),
            (row.wire_current_ground_to_sphere_a,-true_I),
            (row.induced_mechanical_energy_j,true_U),
        ):assert math.isclose(actual,expected,rel_tol=4e-12)
        for j in range(3):
            assert math.isclose(row.induced_force_on_source_n[j],axis[j]*true_force,rel_tol=4e-11,abs_tol=1e-24)
        # New genuine Kelvin solver calls on two slightly shifted native states:
        h=.001
        nets=[]
        for shift in (-h,h):
            point=tuple(c[j]+axis[j]*(d+v*shift) for j in range(3))
            moved=replace(problem,charges=(PointCharge(q,point),))
            obs=observe_grounded_sphere_wire(moved,row.source_velocity_m_s)
            nets.append(obs.induced_sphere_net_charge_c)
        I_from_native_charge=-(nets[1]-nets[0])/(2*h)
        assert math.isclose(I_from_native_charge,true_I,rel_tol=3e-7),label
    hypothetical={'role':'teacher_hypothetical','statement':f'Independent hypothetical {label}','numeric_attribution':'All values TEACHER-CHOSEN; NONE is a printed numerical given.'}
    assert viewer_manifest(trace,hypothetical)['source']['role']=='teacher_hypothetical'
    if q<0 or v>0:
        try:viewer_manifest(trace,SOURCE)
        except ValueError:pass
        else:raise AssertionError('A non-original world was labelled as original Q21')
    result['native_worlds'].append({'name':label,'native_frames':len(trace.samples),'fresh_native_shifted_kelvin_checks':len(trace.samples),'I_first_A':trace.samples[0].wire_current_sphere_to_ground_a})

# New raw Boolean and nonfinite refusal cases.
for key,bad in [('source_charge_c',True),('sphere_radius_m',False),('permittivity_f_per_m',True)]:
    args={'source_charge_c':1e-9,'source_position_m':(0.,0.,.31),'sphere_radius_m':.1,'permittivity_f_per_m':8.8541878128e-12}
    args[key]=bad
    try:author_prescribed_grounded_sphere(**args)
    except ValueError:pass
    else:raise AssertionError('Raw SI Boolean accepted for '+key)
for position in ((0.,True,.3),(float('nan'),0.,.3)):
    try:author_prescribed_grounded_sphere(1e-9,position,.1)
    except ValueError:pass
    else:raise AssertionError('Bad raw charge position was accepted')
for center in ((False,0.,0.),(float('inf'),0.,0.)):
    try:author_prescribed_grounded_sphere(1e-9,(0.,0.,.3),.1,sphere_center_m=center)
    except ValueError:pass
    else:raise AssertionError('Bad raw sphere center was accepted')

(OUT/'native-review-evidence.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
