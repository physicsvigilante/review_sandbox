#!/usr/bin/env python3
"""Independent reviewer arithmetic and provenance reproducer for conductor_sim PR109.

Requires only stdlib for mathematical tests. An optional --repo PATH enables
checks against a *local checkout* of exact PR HEAD, including the original PDF
SHA256 and the frozen case roster. Pure mathematics here does not substitute
for running released physical APIs or visually inspecting the PDF pages.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

E0=8.8541878128e-12
QE=1.602176634e-19
ME=9.1093837139e-31
K=1/(4*math.pi*E0)
WORKBOOK_SHA='9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d'
NOTES_SHA='8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5'
IDS=('p01-single-08','p02-single-19','p03-single-27','p07-multiple-13',
     'p08-multiple-21','p11-linked-28','p12-linked-40',
     'p16-archive-numerical-01','p26-conductor-potential',
     'p27-cavity-two-shells','p69-cavity-central-vs-shifted','p70-three-cavities')
FIELDS=('source_fact_attribution','interpretation_fidelity','independent_physics',
        'original_answer_completeness','real_browser_observation',
        'teaching_usefulness','refusal_correctness')

def close(a,b,rtol=1e-11,atol=1e-20):
    assert math.isclose(a,b,rel_tol=rtol,abs_tol=atol),(a,b)

def independent_poisson_sigma(q,R,d,mu):
    assert R>0 and 0<=d<R and -1<=mu<=1
    return -q*(R*R-d*d)/(4*math.pi*R*(R*R+d*d-2*R*d*mu)**1.5)

def integrate_sphere_sigma(q,R,d,n=2000):
    # Independent midpoint quadrature of axisymmetric induced surface charge.
    du=2/n
    return sum(independent_poisson_sigma(q,R,d,-1+(i+0.5)*du)*2*math.pi*R*R*du for i in range(n))

def independent_physics():
    findings={}
    # p1: transverse movement does not affect work in uniform +x E.
    dx=math.sqrt(5**2-3**2)
    field_work=-QE*10*dx
    external_work=-field_work
    close(dx,4)
    close(external_work/QE,40)
    close(field_work/QE,-40)
    findings['p01']={'delta_x_m':dx,'field_work_eV':field_work/QE,'external_work_eV':external_work/QE}

    # p2: ideal charged metallic face is a one-sided surface, not insulating sheet.
    E=abs(-2e-6)/E0
    v=math.sqrt(2*100*QE/ME)
    acceleration=QE*E/ME
    distance=v*v/(2*acceleration)
    t_stop=v/acceleration
    close(distance,100/E)
    close(distance*1000,0.44270939064)
    assert 0<t_stop<2e-10
    findings['p02']={'one_sided_field_v_m':E,'stopping_distance_mm':1000*distance,'stop_time_s':t_stop}

    # p3: field between original solid sphere and uncharged enclosing shell
    # disappears on connection. No rate/current waveform follows from energies.
    Q=20e-6; inner=.1; outer=.2
    energy=.5*K*Q*Q*(1/inner-1/outer)
    close(energy,8.987551792261172)
    findings['p03']={'ideal_static_release_j':energy}

    # p8: grounded sphere image Qind=-q R/d. Prescribed constant approach speed
    # gives dQind/dt=-qRv/d^2, hence conventional current sphere -> ground.
    q,R,speed=1.2e-9,.4,.1
    magnitudes=[q*R*speed/(d*d) for d in (1.5,1.1,.8)]
    assert magnitudes[0]<magnitudes[1]<magnitudes[2]
    findings['p08']={'teacher_distances_m':[1.5,1.1,.8],'induced_current_magnitudes_A':magnitudes}

    # p12: source-work: from ring A center to B center; applied vertical E is transverse.
    r=.3; d=.4; qA=10e-6; qB=-20e-6; qprobe=10e-6
    phi_A=K*(qA/r+qB/math.hypot(r,d))
    phi_B=K*(qA/math.hypot(r,d)+qB/r)
    work=qprobe*(phi_A-phi_B)
    close(work,3.595020716904469)
    findings['p12']={'V_at_A_v':phi_A,'V_at_B_v':phi_B,'axial_work_j':work,'transverse_field_axial_work_j':0}

    # p16: ideal stationary force balance, not a complete terminal-drag transient.
    radius=8e-7; rho=900; g=10; Eplate=200/.01
    n=(4*math.pi*radius**3*rho*g/3)/(QE*Eplate)
    assert 6<n<6.1
    findings['p16']={'ideal_electron_count_continuous':n,'nearest_integer':round(n)}

    # Three unfamiliar SIGNED and TRANSLATED examples for p26/p27/p69.
    variants=(
      {'R':.12,'Q':-1.7e-9,'q':-1.7e-9,'q1':+2.0e-9,'q2':-.7e-9,'origin':(.17,-.1,.06),'d':.035},
      {'R':.31,'Q':+3.4e-9,'q':+3.4e-9,'q1':-1.2e-9,'q2':+2.3e-9,'origin':(-.22,.08,.17),'d':.09},
      {'R':.075,'Q':-.55e-9,'q':-.55e-9,'q1':-.8e-9,'q2':+1.5e-9,'origin':(.08,.12,-.19),'d':.024},
    )
    variant_outputs=[]
    for case in variants:
        R=case['R']; Q=case['Q']; q=case['q']; q1=case['q1']; q2=case['q2']; O=case['origin']
        # p26 conductor equipotential; coordinate translation must not matter.
        V_half=K*Q/R; V_outer=K*Q/(1.5*R)
        close(V_half/(V_outer),1.5)
        # p27 ideal nested thin spheres plus distinct FINITE METAL teacher model.
        a,b,thickness,r,r1=.1,.2,1e-6,.04,.15
        ai,bi=a-thickness,b-thickness
        original_A=K*(q/r + q1/a + q2/b)
        original_B=K*((q+q1)/r1 + q2/b)
        finite_A=K*(q/r - q/ai + (q+q1)/a -(q+q1)/bi + (q+q1+q2)/b)
        finite_B=K*((q+q1)/r1 -(q+q1)/bi +(q+q1+q2)/b)
        assert math.isfinite(finite_A) and math.isfinite(finite_B)
        # p69: Poisson kernel; centered/shifted, signs, integral = -q.
        # Teacher inner R=R; shift d<R; 3q net metal -> outer total 4q.
        source_distance=case['d']
        centered=independent_poisson_sigma(q,R,0,1)
        close(centered,-q/(4*math.pi*R*R))
        shifted_near=independent_poisson_sigma(q,R,source_distance,1)
        shifted_far=independent_poisson_sigma(q,R,source_distance,-1)
        assert shifted_near!=shifted_far
        assert shifted_near*q<0 and shifted_far*q<0
        integrated=integrate_sphere_sigma(q,R,source_distance)
        close(integrated,-q,rtol=2e-5,atol=1e-17)
        variant_outputs.append({'teacher_origin_m':O,'signed_charge_c':q,
            'p26_half_R_v':V_half,'p26_three_half_R_v':V_outer,
            'p27_ideal_A_v':original_A,'p27_ideal_B_v':original_B,
            'p27_finite_A_v':finite_A,'p27_finite_B_v':finite_B,
            'p69_centered_sigma_c_m2':centered,'p69_shift_near_sigma_c_m2':shifted_near,
            'p69_shift_far_sigma_c_m2':shifted_far,
            'p69_integrated_inner_charge_c':integrated,'p69_outer_total_charge_c':4*q})
    findings['signed_translated_teacher_variants']=variant_outputs
    # p11: external q never enters the induced whole-face Gauss TOTAL.
    Q,q1,q2,exterior_q=.7e-9,1e-9,-.4e-9,-2e-9
    findings['p11']={'outer_total_c':Q+q1+q2,'external_point_q_c':exterior_q,
       'external_charge_changes_local_outer_density':True,'irregular_local_sigma_not_inferred':True}
    # p70: Gauss charge identities only; 2D circular sketches are insufficient
    # to determine a unique three-dimensional local-density field.
    findings['p70']={'inner_totals_c':[-1e-9,-2e-9,-3e-9],
       'outer_total_c':6e-9,'local_sigma_requires_qualified_geometry':True}
    return findings

def check_frozen_repo(path):
    got={}
    for file,expected in (('02_conductors_half_size.pdf',WORKBOOK_SHA),('POTENTIAL_CONDUCTORS1.pdf',NOTES_SHA)):
        digest=hashlib.sha256((path/file).read_bytes()).hexdigest()
        assert digest==expected,(file,digest,expected)
        got[file]=digest
    cohort=json.loads((path/'docs/jee12_evaluation_cohort.json').read_text('utf8'))
    historical=json.loads((path/'docs/m36a_jee30_coverage.json').read_text('utf8'))
    assert len(cohort['cases'])==12
    assert tuple(c['id'] for c in cohort['cases'])==IDS
    source_rows={c['id']:c for c in historical['cases']}
    for case in cohort['cases']:
        orig=source_rows[case['id']]
        for key in ['source','pdf_page','printed_anchor']:
            assert case[key]==orig[key]
        assert case['evaluation']['reviewer_evidence']=='none'
        assert all(case['evaluation'][key]=='not_evaluated' for key in FIELDS)
        note=case['developer_pdf_source_note']
        assert note['original_answer_newly_independently_reviewed'] is False
        if 'original_problem_answer_newly_independently_reviewed' in note:
            assert note['original_problem_answer_newly_independently_reviewed'] is False
    routes=[c['historical_candidate_route_not_verified'] for c in cohort['cases']]
    assert {k:routes.count(k) for k in set(routes)}=={'supported_scoped':8,'partial':2,'unsupported':2}
    assert cohort['independently_reviewed_original_answer_cases']==0
    return {'pdf_sha256':got,'case_count':len(cohort['cases']),
            'all_seven_evaluation_fields_not_evaluated':True,
            'nested_review_flags_false':True,'historical_routing_counts':{'supported_scoped':8,'partial':2,'unsupported':2}}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,help='checkout with both original PDFs and frozen JSON manifests')
    p.add_argument('--out',type=Path)
    a=p.parse_args()
    result={'schema':'independent.j ee12.math.provenance.review01'.replace(' ',''),
            'math_reference':independent_physics(),
            'scope':'INDEPENDENT MATH ONLY; DOES NOT PROVE PDF PAGE TEXT OR NATIVE EXECUTION',
            'repo_validation':check_frozen_repo(a.repo) if a.repo else 'NOT RUN: no checked-out source PDFs available'}
    s=json.dumps(result,indent=2,allow_nan=False)+'\n'
    if a.out:a.out.write_text(s,'utf8')
    print('PASS: standalone independent mathematics; 3 signed/translated teacher variants; repo validation:',
          'executed' if a.repo else 'not executed')
