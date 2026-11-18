"""Reviewer-owned PR90 execution. Never edits production; failures stay failures.
Run from an exact conductor_sim checkout; the companion SI oracle has no production imports.
"""
from __future__ import annotations
import ast
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import traceback
import urllib.request
from dataclasses import replace
from unittest.mock import patch

from chat_b_kelvin_oracle import close, verify_trace

HEAD = '155b0544684d3d880a83a661cc8e14a0ce22f26b'
TREE = 'f48f54b8c49217b7c66179fe014b6fab1ea4dc4d'
BASE = '133acf97a123e6167aeaac3ca2a2b2094af1d36f'
CHARTER = '24300b2050430634532bb1978cba38eb7d3f39e4'
PDF_SHA = '9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d'
OUT = Path(os.environ['REVIEW_OUTPUT']).resolve()
OUT.mkdir(parents=True, exist_ok=True)
RESULTS = []


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False, allow_nan=False)+'\n')


def record(name, function, refusal=False):
    try:
        value = function()
        result = {'name': name, 'status': 'FAIL' if refusal else 'PASS',
                  'detail': 'INVALID INPUT ACCEPTED' if refusal else value}
    except (ValueError, TypeError, AssertionError) as exc:
        result = {'name': name, 'status': 'PASS' if refusal else 'FAIL',
                  'detail': f'{type(exc).__name__}: {exc}'}
        if not refusal:
            result['traceback'] = traceback.format_exc()
    except Exception as exc:
        result = {'name': name, 'status': 'ERROR',
                  'detail': f'{type(exc).__name__}: {exc}', 'traceback': traceback.format_exc()}
    RESULTS.append(result)
    print(json.dumps(result, ensure_ascii=False), flush=True)
    save(OUT/'results-progress.json', RESULTS)
    return result


def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()


def api(path):
    request = urllib.request.Request('https://api.github.com/repos/physicsvigilante/conductor_sim/'+path,
        headers={'Authorization': 'Bearer '+os.environ['GH_TOKEN'],
                 'Accept': 'application/vnd.github+json', 'User-Agent': 'PR90-independent-Chat-B'})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def identity(label):
    pr = api('pulls/90')
    runs = api('actions/runs?head_sha='+HEAD+'&per_page=100')
    save(OUT/f'{label}-pr.json', pr)
    inventory = [{k: r[k] for k in ('id','name','head_sha','event','status','conclusion','html_url','run_attempt')}
                 for r in runs['workflow_runs']]
    save(OUT/f'{label}-ci-inventory.json', inventory)
    assert pr['head']['sha'] == HEAD and pr['base']['sha'] == BASE, 'STALE candidate/base'
    assert pr['draft'] and not pr['merged'] and pr['state'] == 'open'
    assert git('rev-parse', 'HEAD') == HEAD
    assert git('rev-parse', 'HEAD^{tree}') == TREE
    assert runs['total_count'] == len(inventory) == 26
    assert all(r['head_sha'] == HEAD and r['status'] == 'completed' and r['conclusion'] == 'success'
               for r in inventory)
    return {'head': HEAD, 'tree': TREE, 'exact_head_successful_workflows': 26,
            'events': {e: sum(r['event'] == e for r in inventory) for e in ('pull_request','push')}}


def provenance():
    expected = {'.github/workflows/m37b-source-current.yml','docs/m37b.md','docs/m37b_charter.md',
                'src/conductor_sim/__init__.py','src/conductor_sim/prescribed_ground_wire.py',
                'src/conductor_sim/prescribed_wire_viewer.py','tests/test_m37b_constant_speed_jee.py',
                'tools/check_m37b_prescribed_browser.py','tools/m37b_source_approach.py',
                'tools/m37b_source_reference.py'}
    actual = set(git('diff','--name-only',BASE,HEAD).splitlines())
    assert actual == expected, actual
    assert git('rev-parse', CHARTER+'^') == BASE
    subprocess.run(['git','merge-base','--is-ancestor',CHARTER,HEAD], check=True)
    assert git('rev-parse',CHARTER+':docs/m37b_charter.md') == git('rev-parse',HEAD+':docs/m37b_charter.md')
    digest = hashlib.sha256(Path('02_conductors_half_size.pdf').read_bytes()).hexdigest()
    assert digest == PDF_SHA
    assert not git('diff', BASE, HEAD, '--', '*.pdf', 'src/conductor_sim/grounded_sphere_wire.py',
                   'src/conductor_sim/motion_1d.py','src/conductor_sim/external_sphere.py')
    evidence = {'head':HEAD,'tree':TREE,'base':BASE,'charter':CHARTER,
                'changed_files':sorted(actual),'pdf_sha256':digest,'unchanged_old_paths':True}
    save(OUT/'source-provenance.json', evidence)
    import fitz
    with fitz.open('02_conductors_half_size.pdf') as pdf:
        for index in (7,16):
            pdf[index].get_pixmap(matrix=fitz.Matrix(1.7,1.7)).save(OUT/f'original-physical-page-{index+1}.png')
            (OUT/f'original-physical-page-{index+1}.txt').write_text(pdf[index].get_text())
    return evidence


if record('live-start-identity-and-all-26-runs', lambda: identity('start'))['status'] != 'PASS':
    raise SystemExit('STALE OR CI NOT QUALIFIED: no candidate testing started')
if record('ten-file-diff-charter-ancestry-and-original-pdf', provenance)['status'] != 'PASS':
    raise SystemExit('Source identity qualification failed')

from conductor_sim import (EPSILON_0, ElectrostaticProblem, Grounded, FixedNetCharge,
                           PointCharge, SolidSphere, SphericalShell, PrescribedSphereRadialSpec,
                           author_prescribed_grounded_sphere, sample_prescribed_sphere_radial)
from conductor_sim.external_sphere import ExternalGroundedSphereBackend
from conductor_sim.prescribed_wire_viewer import viewer_manifest, render_prescribed_ground_wire
from tools.m37b_source_approach import SOURCE, make_example, run_all
from tools.m37b_source_reference import check as production_reference
from tools.check_m37b_prescribed_browser import check as production_browser_check

GENUINE = OUT/'genuine'
MANIFEST = run_all(GENUINE)
TRACE = sample_prescribed_sphere_radial(make_example())
EXPECTED = verify_trace(MANIFEST['trace'])


def physics(spec, label):
    trace = sample_prescribed_sphere_radial(spec)
    payload = trace.as_dict()
    expected = verify_trace(payload)
    save(OUT/'scientific-cases'/f'{label}.json', payload)
    assert trace.samples[0].source_position_m == spec.problem.charges[0].position_m
    max_relative = 0.
    for row in trace.samples:
        h = min(2e-5, .001*(row.radial_distance_m-spec.problem.conductors[0].radius_m)/abs(spec.radial_speed_m_s))
        native_Q = []
        for direction in (-1,1):
            pos = tuple(row.source_position_m[j]+direction*h*row.source_velocity_m_s[j] for j in range(3))
            p = replace(spec.problem,charges=(PointCharge(spec.problem.charges[0].charge_c,pos),))
            native_Q.append(ExternalGroundedSphereBackend().solve(p).conductor_results[0].net_charge_c)
        derivative_current = -(native_Q[1]-native_Q[0])/(2*h)
        close(derivative_current,row.wire_current_sphere_to_ground_a,'native shifted-Q current',relative=3e-7)
        max_relative = max(max_relative, abs(derivative_current/row.wire_current_sphere_to_ground_a-1))
    return {'states':len(expected),'native_shifted_Kelvin_solves':2*len(expected),
            'maximum_relative_current_finite_difference_error':max_relative}


record('original-31-state-independent-SI-and-native-shifted-Q',lambda:physics(make_example(),'original'))
record('saved-json-equals-native-manifest',lambda: (None if json.loads((GENUINE/'p8-ground-current.json').read_text()) == MANIFEST else (_ for _ in ()).throw(AssertionError('saved JSON differs'))))
HYPOTHETICAL = {'role':'teacher_hypothetical','statement':'TEACHER HYPOTHETICAL: signed radial motion; not original Q21.',
                'numeric_attribution':'All numerical values are TEACHER-CHOSEN; NONE is a printed numerical given.'}
SCENARIOS = [
    ('negative-inward-oblique',-2.7e-9,-.017,.073,.41,(.4,-.2,.6),(1/3,2/3,-2/3),2.4,1.9,13),
    ('positive-outward-oblique',3.1e-9,.023,.081,.33,(-.27,.18,.91),(-2/3,2/3,1/3),4.7,2.2,17),
    ('negative-outward',-1.4e-9,.031,.062,.24,(0.,0.,0.),(.6,0.,.8),1.3,1.4,9),
    ('near-surface-safe',1.9e-9,-.0002,.12,.121,(0.,0.,0.),(0.,0.,1.),1.,.9,11),
]
for label,q,v,r,d,c,axis,er,duration,count in SCENARIOS:
    p = author_prescribed_grounded_sphere(q,tuple(c[j]+d*axis[j] for j in range(3)),r,
        sphere_center_m=c,permittivity_f_per_m=er*EPSILON_0,sphere_name='Teacher '+label)
    spec = PrescribedSphereRadialSpec(p,v,duration,count,1e-5)
    record(label+'-independent-SI-and-native-FD',lambda s=spec,l=label:physics(s,l))
    trace = sample_prescribed_sphere_radial(spec)
    record(label+'-teacher-render',lambda t=trace: {'role':viewer_manifest(t,HYPOTHETICAL)['source']['role'],
                                                  'html_chars':len(render_prescribed_ground_wire(t,source=HYPOTHETICAL))})
    record(label+'-false-original-role-refusal',lambda t=trace:viewer_manifest(t,SOURCE),True)

RAW = dict(source_charge_c=1e-9,source_position_m=(0.,0.,.3),sphere_radius_m=.1,
           sphere_center_m=(0.,0.,0.),permittivity_f_per_m=EPSILON_0)
for key in ('source_charge_c','sphere_radius_m','permittivity_f_per_m'):
    for bad in (True,False,float('nan'),float('inf')):
        args = dict(RAW); args[key] = bad
        record(f'raw-{key}-{bad!r}',lambda a=args:author_prescribed_grounded_sphere(**a),True)
for key in ('source_position_m','sphere_center_m'):
    for j in range(3):
        for bad in (True,float('nan')):
            args = dict(RAW); vector = list(args[key]); vector[j] = bad; args[key] = vector
            record(f'raw-{key}-{j}-{bad!r}',lambda a=args:author_prescribed_grounded_sphere(**a),True)
for key,bad in [('radial_speed_m_s',True),('radial_speed_m_s',0),('radial_speed_m_s',29979245.8),
                ('radial_speed_m_s',float('nan')),('duration_s',False),('duration_s',-1),
                ('duration_s',float('inf')),('sample_count',True),('sample_count',2),
                ('sample_count',202),('sample_count',31.),('surface_guard_m',False),
                ('surface_guard_m',0),('surface_guard_m',.2),('duration_s',5.)]:
    record(f'spec-{key}-{bad!r}',lambda k=key,b=bad:replace(make_example(),**{k:b}),True)
p0 = make_example().problem
BAD_PROBLEMS = {
    'zero-charge':replace(p0,charges=(PointCharge(0.,(0.,0.,.3)),)),
    'two-sources':replace(p0,charges=p0.charges+(PointCharge(1e-9,(0.,0.,.4)),)),
    'two-metals':replace(p0,conductors=p0.conductors+(SolidSphere(.02,Grounded(),(.9,0.,0.),'Other'),)),
    'isolated':replace(p0,conductors=(SolidSphere(.1,FixedNetCharge(0.),name='Sphere A'),)),
    'hollow':replace(p0,conductors=(SphericalShell(.08,.1,Grounded(),name='Sphere A'),)),
    'inside':replace(p0,charges=(PointCharge(1e-9,(0.,0.,.05)),)),
    'surface':replace(p0,charges=(PointCharge(1e-9,(0.,0.,.1)),)),
    'guard':replace(p0,charges=(PointCharge(1e-9,(0.,0.,.10005)),)),
}
for label,p in BAD_PROBLEMS.items():
    record('domain-'+label,lambda p=p:PrescribedSphereRadialSpec(p,-.001,.1,7,1e-4),True)
legacy = replace(p0,charges=(PointCharge(1e-9,(True,0.,.3)),))
record('legacy-canonical-float-not-false-raw-attestation',lambda:physics(PrescribedSphereRadialSpec(legacy,-.01,.4,7,1e-4),'legacy-normalized'))
for key,bad in [('wire_current_sphere_to_ground_a',-.37),('induced_mechanical_energy_j',2*TRACE.samples[0].induced_mechanical_energy_j),
                ('time_s',False),('index',False),('source_position_m',(False,0.,.3)),
                ('induced_force_on_source_n',(False,0.,TRACE.samples[0].induced_force_on_source_n[2]))]:
    forged = replace(TRACE,samples=(replace(TRACE.samples[0],**{key:bad}),*TRACE.samples[1:]))
    def typed_attempt(t=forged,k=key):
        exported = viewer_manifest(t,SOURCE)
        save(OUT/'accepted-typed-forgeries'/f'{k}.json',exported)
        return exported['trace']['samples'][0]
    record('typed-native-forgery-'+key,typed_attempt,True)


def inspect_imports():
    tree = ast.parse(Path('tools/m37b_source_reference.py').read_text())
    modules = []
    for node in ast.walk(tree):
        if isinstance(node,ast.Import): modules.extend(a.name for a in node.names)
        if isinstance(node,ast.ImportFrom): modules.append(node.module)
    assert set(modules) <= {'__future__','argparse','json','math','pathlib'},modules
    return modules
record('standalone-reference-no-production-imports',inspect_imports)
record('standalone-reference-genuine-output',lambda:production_reference(MANIFEST))
MUTATIONS = [
    ('negative-q',('trace','source_charge_c'),-1e-9),('radius',('trace','sphere_radius_m'),.1007),
    ('center',('trace','sphere_center_m',1),.013),('speed',('trace','signed_constant_radial_speed_m_s'),-.0413),
    ('duration',('trace','duration_s'),3.2),('timestamp',('trace','samples',7,'time_s'),.701),
    ('Q',('trace','samples',19,'induced_sphere_net_charge_c'),3e-10),
    ('both-current-signed',('trace','samples',17,'wire_current_sphere_to_ground_a'),-MANIFEST['trace']['samples'][17]['wire_current_sphere_to_ground_a']),
    ('opposite-current',('trace','samples',23,'wire_current_ground_to_sphere_a'),1e-12),
    ('force',('trace','samples',13,'induced_force_on_source_n',2),0.),
    ('energy-half-factor',('trace','samples',11,'induced_mechanical_energy_j'),2*MANIFEST['trace']['samples'][11]['induced_mechanical_energy_j']),
    ('units',('trace','units','energy'),'eV'),('sample-index',('trace','samples',6,'index'),7),
    ('source-position',('trace','samples',9,'source_position_m',0),.007),
    ('velocity',('trace','samples',27,'source_velocity_m_s',1),.001),
    ('wrong-options',('source','original_correct_option_indices'),[1,4]),
    ('bool-options',('source','original_correct_option_indices'),[True,3]),
    ('bool-apparatus',('source','original_question_apparatus_count'),True),
    ('bool-hypotheticals',('source','teacher_hypotheticals_counted_as_original'),False),
    ('official-exam',('source','source_kind'),'Official JEE Advanced paper'),
    ('false-numeric-origin',('source','numeric_attribution'),'Printed original gives q=1 nC.'),
    ('extra-false-metadata',('source','official_exam_year'),2026),
    ('extra-false-trace',('trace','joule_heating_computed'),True),
    ('bool-count',('trace','sample_count'),True),('boolean-zero-time',('trace','samples',0,'time_s'),False),
    ('stale-readout',('readouts',22,'wire_current_label'),'9 A'),
    ('plot-coordinate',('readouts',24,'chart_y_px'),280.),('sphere-drawing',('layout','sphere_radius_px'),10.),
    ('false-displayed-physics',('display_contract',),'FEMM electromagnetic transient'),
    ('float-source-page',('source','physical_pdf_page'),8.0),
]
for label,path,value in MUTATIONS:
    forged = copy.deepcopy(MANIFEST); cursor = forged
    for key in path[:-1]: cursor = cursor[key]
    cursor[path[-1]] = value
    save(OUT/'json-attacks'/f'{label}.json',forged)
    record('source-JSON-'+label,lambda m=forged:production_reference(m),True)

# Actual browser inspection; the independent observer never trusts payload readouts as physics.
from playwright.sync_api import sync_playwright, Browser
ALL_HTTP = []; ALL_ERRORS = []

def observe_context(context, requests, errors):
    context.on('request',lambda r:requests.append(r.url) if r.url.startswith(('http://','https://')) else None)
    context.on('page',lambda p:p.on('pageerror',lambda e:errors.append(str(e))))
    context.route('**/*',lambda route:route.abort() if route.request.url.startswith(('http://','https://')) else route.continue_())


def assert_visible_state(page,index):
    row = EXPECTED[index]
    labels = {'m37b-time':('time_s','s'),'m37b-distance':('radial_distance_m','m'),
              'm37b-Q':('induced_sphere_net_charge_c','C'),
              'm37b-current':('wire_current_sphere_to_ground_a','A'),
              'm37b-opposite':('wire_current_ground_to_sphere_a','A')}
    for element,(key,unit) in labels.items():
        loc = page.locator('#'+element)
        assert loc.is_visible(),element+' hidden'
        text = loc.inner_text().strip()
        number,actual_unit = text.rsplit(' ',1)
        assert actual_unit == unit
        close(float(number),row[key],element,relative=8e-10)
    scale = min(96/.1,515/.3)
    for element,attr,value in [('m37b-sphere','r',scale*.1),('m37b-sphere','cx',129.),
        ('m37b-sphere','cy',169.),('m37b-charge','cx',129+scale*row['radial_distance_m']),
        ('m37b-charge','cy',169.),('m37b-current-marker','cx',61+487*index/30),
        ('m37b-current-marker','cy',139-100*row['wire_current_sphere_to_ground_a']/EXPECTED[-1]['wire_current_sphere_to_ground_a'])]:
        close(float(page.locator('#'+element).get_attribute(attr)),value,element+'.'+attr,relative=8e-10)
    assert page.locator('#m37b-q-sign').inner_text() == '+q'


def assert_curve(page):
    points = page.locator('#m37b-current-line').get_attribute('points').split()
    assert len(points) == 31
    for i,point in enumerate(points):
        x,y = map(float,point.split(','))
        close(x,61+487*i/30,'actual drawn chart x',relative=8e-10)
        close(y,139-100*EXPECTED[i]['wire_current_sphere_to_ground_a']/EXPECTED[-1]['wire_current_sphere_to_ground_a'],
              'actual drawn chart y',relative=8e-10)


def browser_baseline():
    summary = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        try:
            for label,js,width,height in [('desktop',True,1280,900),('mobile',True,360,760),('nojs',False,960,760)]:
                context = browser.new_context(java_script_enabled=js,viewport={'width':width,'height':height})
                observe_context(context,ALL_HTTP,ALL_ERRORS)
                page = context.new_page(); page.goto((GENUINE/'p8-ground-current.html').as_uri())
                assert page.locator('#m37b-original-statement').is_visible()
                assert page.locator('#m37b-teacher-attribution').is_visible()
                assert 'options (1) and (3)' in page.locator('#m37b-original-statement').inner_text()
                assert 'TEACHER-CHOSEN' in page.locator('#m37b-teacher-attribution').inner_text()
                body = page.locator('body').inner_text()
                (OUT/f'{label}-visible-text.txt').write_text(body)
                embedded = json.loads(page.locator('#m37b-data').text_content())
                assert embedded == MANIFEST
                verify_trace(embedded['trace'])
                assert_curve(page); assert_visible_state(page,0)
                assert page.evaluate('document.documentElement.scrollWidth') <= width if js else True
                if js:
                    for i in (2,8,16,23,29,30):
                        page.locator('#m37b-index').evaluate("(e,i)=>{e.value=String(i);e.dispatchEvent(new Event('input',{bubbles:true}));}",i)
                        assert_visible_state(page,i)
                    page.screenshot(path=str(OUT/f'{label}-sample30.png'),full_page=True)
                    page.locator('#m37b-start').click(); assert_visible_state(page,0)
                    page.locator('#m37b-play').click()
                    page.wait_for_function('Number(document.getElementById("m37b-index").value)>=2',timeout=3000)
                    page.locator('#m37b-index').evaluate("e=>e.dispatchEvent(new Event('input',{bubbles:true}))")
                    index = int(page.locator('#m37b-index').input_value()); assert_visible_state(page,index)
                    page.locator('#m37b-start').click(); assert_visible_state(page,0)
                else:
                    for element in ('m37b-index','m37b-play','m37b-start'):
                        assert page.locator('#'+element).is_disabled()
                    assert page.locator('#m37b-nojs').is_visible()
                page.screenshot(path=str(OUT/f'{label}-first.png'),full_page=True)
                summary.append({'mode':label,'all31_curve_points':True,'all_first_readouts':True})
                context.close()
        finally: browser.close()
    assert not ALL_HTTP and not ALL_ERRORS,(ALL_HTTP,ALL_ERRORS)
    return summary
record('reviewer-real-Chromium-all-points-selected-states-play-restart-mobile-nojs',browser_baseline)

def visible_teacher_caption():
    body = (OUT/'desktop-visible-text.txt').read_text()
    assert SOURCE['numeric_attribution'] in body, 'Validated numerical q/R/d0/v/duration caption exists only in embedded JSON, not visible body'
record('teacher-numerical-inputs-actually-visible',visible_teacher_caption)

# Run production browser validator against independently authored HTML-only attacks.
# Observe/block all HTTP at the browser context boundary without changing production source.
CAPTURED_HTTP=[]; CAPTURED_ERRORS=[]
original_new_context = Browser.new_context
original_new_page = Browser.new_page

def guarded_context(self,*args,**kwargs):
    context=original_new_context(self,*args,**kwargs)
    observe_context(context,CAPTURED_HTTP,CAPTURED_ERRORS)
    return context

def guarded_page(self,*args,**kwargs):
    page=original_new_page(self,*args,**kwargs)
    observe_context(page.context,CAPTURED_HTTP,CAPTURED_ERRORS)
    page.on('pageerror',lambda e:CAPTURED_ERRORS.append(str(e)))
    return page

HTML=(GENUINE/'p8-ground-current.html').read_text()

def text_for_id(html,element,text):
    pattern=r'(<[^>]*\bid="'+re.escape(element)+r'"[^>]*>)([^<]*)(</[^>]+>)'
    changed,n=re.subn(pattern,lambda m:m.group(1)+text+m.group(3),html,count=1)
    assert n == 1,'mutation target not found: '+element
    return changed

def attr_for_id(html,element,attr,value):
    pattern=r'(<[^>]*\bid="'+re.escape(element)+r'"[^>]*\b'+attr+r'=")[^"]*(")'
    changed,n=re.subn(pattern,lambda m:m.group(1)+str(value)+m.group(2),html,count=1)
    assert n == 1,'mutation attribute not found'
    return changed

embedded_bad=copy.deepcopy(MANIFEST);embedded_bad['trace']['samples'][18]['wire_current_sphere_to_ground_a'] *= -1
html_embedded,n=re.subn(r'(<script id="m37b-data" type="application/json">).*?(</script>)',
    lambda m:m.group(1)+json.dumps(embedded_bad,ensure_ascii=False)+m.group(2),HTML,count=1,flags=re.S)
assert n == 1
points=re.search(r'<polyline id="m37b-current-line" points="([^"]+)"',HTML).group(1).split()
points[14]='288.26666667,277'
ATTACKS = {
    'visible-original-false':text_for_id(HTML,'m37b-original-statement','SOURCE-GIVEN: a negative charge freely accelerates. Correct options (2),(4).'),
    'sphere-radius':attr_for_id(HTML,'m37b-sphere','r',12),
    'charge-sign':text_for_id(HTML,'m37b-q-sign','−q'),
    'drawn-curve':attr_for_id(HTML,'m37b-current-line','points',' '.join(points)),
    'embedded-native-json':html_embedded,
    'hidden-teacher-attribution':HTML.replace('id="m37b-teacher-attribution"','id="m37b-teacher-attribution" style="display:none"',1),
    'nojs-time':text_for_id(HTML,'m37b-time','91 s'),
    'nojs-distance':text_for_id(HTML,'m37b-distance','9 m'),
    'nojs-opposite-current':text_for_id(HTML,'m37b-opposite','7 A'),
    'nojs-chart-marker':attr_for_id(HTML,'m37b-current-marker','cx',400),
    'stale-visible-teacher-caption':HTML.replace('</header>','<p id="reviewer-forged-caption">Teacher numeric example: q=+9 C, R=7 m, d0=9 m, v=3 m/s; these are the plotted inputs.</p></header>',1),
    'broken-play':HTML.replace('    i++;','    i+=0;',1),
    'mobile-current-hidden':HTML.replace('</style>','@media(max-width:400px){#m37b-current{visibility:hidden}}</style>',1),
    'nojs-unauthorized-request':HTML.replace('</noscript>','<img src="https://review-only.invalid/pr90-probe" alt="review-only request"></noscript>',1),
}
with patch.object(Browser,'new_context',guarded_context),patch.object(Browser,'new_page',guarded_page):
    record('production-browser-check-genuine-control',lambda:production_browser_check(GENUINE))
    for label,html in ATTACKS.items():
        assert html != HTML,label+' mutation did not apply'
        directory=OUT/'html-attacks'/label;directory.mkdir(parents=True,exist_ok=True)
        (directory/'p8-ground-current.json').write_text((GENUINE/'p8-ground-current.json').read_text())
        (directory/'p8-ground-current.html').write_text(html)
        CAPTURED_HTTP.clear();CAPTURED_ERRORS.clear()
        result=record('production-browser-refuses-'+label,lambda d=directory:production_browser_check(d),True)
        save(directory/'reviewer-observed-requests-errors.json',{'http_requests':list(CAPTURED_HTTP),'js_errors':list(CAPTURED_ERRORS)})
        result['reviewer_observed_http']=list(CAPTURED_HTTP)
        result['reviewer_observed_errors']=list(CAPTURED_ERRORS)

# Explicitly capture the scientifically wrong no-JS/mobile states independently of checker status.
with sync_playwright() as pw:
    browser=pw.chromium.launch()
    for label,js,width,element in [('nojs-distance',False,960,'m37b-distance'),('nojs-time',False,960,'m37b-time'),
        ('nojs-opposite-current',False,960,'m37b-opposite'),('nojs-chart-marker',False,960,'m37b-current-marker'),
        ('mobile-current-hidden',True,360,'m37b-current')]:
        context=browser.new_context(java_script_enabled=js,viewport={'width':width,'height':760})
        observed=[];errors=[];observe_context(context,observed,errors)
        page=context.new_page();page.goto((OUT/'html-attacks'/label/'p8-ground-current.html').as_uri())
        loc=page.locator('#'+element)
        save(OUT/'html-attacks'/label/'actual-hostile-DOM.json',{'element':element,'visible':loc.is_visible(),
             'text':loc.text_content(),'cx':loc.get_attribute('cx')})
        page.screenshot(path=str(OUT/'html-attacks'/label/'reviewer-hostile.png'),full_page=True)
        context.close()
    browser.close()

record('live-end-identity-and-all-26-runs',lambda:identity('end'))
assert not git('diff','--','src','tools','tests','docs','.github'),'production tracked files modified'
summary={'reviewer':'GPT-6 Astra Pro / Chat B','candidate_head':HEAD,'candidate_tree':TREE,
         'pass':sum(r['status']=='PASS' for r in RESULTS),'fail':sum(r['status']=='FAIL' for r in RESULTS),
         'error':sum(r['status']=='ERROR' for r in RESULTS),'results':RESULTS}
save(OUT/'review-results.json',summary)
print('REVIEW_SUMMARY '+json.dumps({k:v for k,v in summary.items() if k!='results'}),flush=True)
raise SystemExit(1 if summary['fail'] or summary['error'] else 0)
