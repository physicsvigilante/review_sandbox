"""Reviewer-owned, source-pinned *actual* Chromium/WebGL2 tests for PR53.
Independent fixtures. No Python field law or production repository writes.
"""
from copy import deepcopy
from functools import partial
from hashlib import sha256
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright
import json, math, shutil, sys

source=Path(sys.argv[1]).resolve()
out=Path(sys.argv[2]).resolve()
out.mkdir(parents=True,exist_ok=False)
runtime=out/'preview'
runtime.mkdir()
web=source/'web/three_preview'
three=web/'node_modules/three'
assert json.loads((three/'package.json').read_text())['version']=='0.180.0'
for name in ('index.html','style.css','app.js','model.js'):
    shutil.copyfile(web/name,runtime/name)
for name,target in (
    ('build/three.module.js','vendor/three.module.js'),
    ('build/three.core.js','vendor/three.core.js'),
    ('examples/jsm/controls/OrbitControls.js','vendor/addons/controls/OrbitControls.js'),
    ('LICENSE','vendor/THREE-LICENSE.txt')):
    dest=runtime/target
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(three/name,dest)

base={
 'visualization_version':1,'title':'Reviewer independent physical samples',
 'units':{'position':'m','time':'s','field':'N/C','potential':'V'},
 'moving_slice':False,'has_uniform_source':True,
 'bounds_m':[-10.,10.,-10.,10.,-10.,10.],
 'animation':{'samples':41,'duration_s':20.,'time_unit':'s','role':'saved_trajectory_sample_display_only'},
 'geometry':[{'id':'A','shape':'sphere','role':'physical_extent','center_m':[0.,0.,0.],'radius_m':1.},
             {'id':'B','shape':'none','role':'uniform_field_has_no_source_shape','center_m':[1.,0.,0.]}],
 'trajectories':[{'id':'probe','role':'calculated_test_particle_trajectory_not_field_line',
  'marker_role':'schematic_particle_marker_not_physical_size_or_charge_sign','marker_radius_m':.2,
  'positions_m':[[i*.05-1.,0.,.5] for i in range(41)]}],
 'field':{'role':'schematic_field_direction_glyphs_not_field_lines','unit':'N/C',
          'positions_m':[[0.,0.,0.]],'vectors_SI':[[1.,0.,0.]],
          'schematic_arrows':{'origins_m':[[0.,0.,0.],[2.,0.,0.]],
            'unit_directions':[[1.,0.,0.],[0.,1.,0.]],'display_length_m':2.,
            'not_calibrated_field_lines':True}},
 'potential':{'role':'physical_potential_samples_on_display_slice','unit':'V',
              'sample_order':'x_fastest_fortran',
              'points_m':[[[-2.,-2.,0.],[-2.,2.,0.]],[[2.,-2.,0.],[2.,2.,0.]]],
              'values':[-1e308,1e308,-.5e308,.5e308]},
 'annotations':[{'id':'playback_help','role':'display_annotation','text':'Space: play / pause\nHome: restart paused'},
                {'id':'legend','role':'display_annotation','text':'Potential, not material surface'}],
 'missing_geometry':[]
}
huge=deepcopy(base)
huge['title']='Reviewer positive 9e307 midpoint'
O=9e307;R=4e306
huge['bounds_m']=[O-R,O+R]*3
def mapped(p):return [O+(x/10.)*R for x in p]
for g in huge['geometry']:
    g['center_m']=mapped(g['center_m'])
    if 'radius_m' in g:g['radius_m']*=R/10.
for t in huge['trajectories']:
    t['positions_m']=[mapped(p) for p in t['positions_m']]
    t['marker_radius_m']*=R/10.
arrows=huge['field']['schematic_arrows']
arrows['origins_m']=[mapped(p) for p in arrows['origins_m']]
arrows['display_length_m']*=R/10.
huge['field']['positions_m']=[mapped(p) for p in huge['field']['positions_m']]
huge['potential']['points_m']=[[mapped(p) for p in row] for row in huge['potential']['points_m']]
role=deepcopy(base)
role['geometry'][1]['role']='schematic_marker'
subnormal=deepcopy(base)
subnormal['field']['schematic_arrows']['display_length_m']=5e-324
precision=deepcopy(base)
precision['title']='Reviewer independent Float32-collapse probe'
precision['trajectories'][0]['positions_m']=[[(999999+.0001*i)*20.,999999*20.,999999*20.] for i in range(41)]
point=lambda x,y:[(999999+x)*20.,(999999+y)*20.,999999*20.]
precision['potential']['points_m']=[[point(0,0),point(0,.001)],[point(.001,0),point(.001,.001)]]
inbounds=deepcopy(base)
inbounds['title']='Reviewer Float32 collapse inside declared bounds'
inbounds['animation']['samples']=61
inbounds['trajectories'][0]['positions_m']=[[20*(.25+i*1e-11),0.,.5] for i in range(61)]
def close_point(x,y):return [20*(.25+x),20*(.25+y),0.]
inbounds['potential']['points_m']=[
    [close_point(0,0),close_point(0,1e-9)],
    [close_point(1e-9,0),close_point(1e-9,1e-9)]
]

# New independent R3 scenarios reuse the R2 fixture-generating scaffold, but
# must now demand REFUSAL for its formerly-admitted Float32-loss examples.
path_only=deepcopy(inbounds)
path_only['potential']=deepcopy(base['potential'])
triangle_only=deepcopy(inbounds)
triangle_only['trajectories']=deepcopy(base['trajectories'])
triangle_only['animation']=deepcopy(base['animation'])

line_collapse=deepcopy(base)
line_collapse['geometry']=[{'id':'f32-line','shape':'line','role':'truncated_infinite_source',
                           'center_m':[19999980.,0.,0.],
                           'direction':[1.,0.,0.],'display_span_m':2e-5}]
line_collapse['has_uniform_source']=False

collinear=deepcopy(base)
collinear['potential']['points_m']=[
    [[2.5,2.5,0.],[2.5,7.5,0.]],
    [[5.,5.,0.],[7.5,7.5+2e-8,0.]]
]

# New reviewer-chosen boundary: first emitted triangle remains nonzero, second
# has nonzero physical area but vanishes after Float32BufferAttribute storage.
second_triangle=deepcopy(base)
A=[5.,5.,0.]; B=[7.,5.,0.]; C=[5.,7.,0.]; D=[5.+2e-8,5.+2e-8,0.]
second_triangle['potential']['points_m']=[[A,D],[B,C]]

below_ulp=deepcopy(base)
below_ulp['trajectories'][0]['positions_m']=[
    [5.,0.,.5],[5.+20e-8,0.,.5],
    *[[6.+.02*i,0.,.5] for i in range(39)]
]
above_ulp=deepcopy(below_ulp)
above_ulp['trajectories'][0]['positions_m'][1]=[5.+40e-8,0.,.5]
binary64_loss=deepcopy(base)
binary64_loss['bounds_m']=[0.,20.,0.,20.,0.,20.]
binary64_loss['trajectories'][0]['positions_m']=[
    [1e-16*i,0.,.5] for i in range(41)
]
exact_degenerate=deepcopy(base)
exact_degenerate['potential']['points_m']=[
    [[0.,0.,0.],[3.,0.,0.]],[[1.,0.,0.],[2.,0.,0.]]
]

gravity=deepcopy(base)
gravity['units']['field']=gravity['field']['unit']='m/s²'
gravity['units']['potential']=gravity['potential']['unit']='J/kg'
line_plane=deepcopy(base)
line_plane['geometry']+= [
    {'id':'line','shape':'line','role':'truncated_infinite_source',
     'center_m':[2.,1.,0.],'direction':[1.,0.,0.],'display_span_m':2.},
    {'id':'plane','shape':'plane','role':'truncated_infinite_source',
     'center_m':[-2.,0.,0.],'direction':[0.,0.,1.],'display_span_m':2.}
]
stationary=deepcopy(base)
stationary['trajectories'][0]['positions_m']=[[5.,0.,.5] for _ in range(41)]
hole=deepcopy(base)
hole['potential']['values'][0]=None
fine=deepcopy(base)
fine['trajectories'][0]['positions_m']=[
    [5.+20*(i*1e-6),0.,.5] for i in range(41)
]
fine['potential']['points_m']=[
    [[0.,0.,0.],[0.,2e-8,0.]],
    [[2e-8,0.,0.],[2e-8,2e-8,0.]]
]

positives=[
    ('ordinary',base),('huge',huge),('gravity',gravity),('line-plane',line_plane),
    ('fine',fine),('stationary',stationary),('null-hole',hole),('above-ulp',above_ulp)
]
negatives=[
    ('wrong-role',role,'source geometry role'),
    ('subnormal-arrow',subnormal,'arrow length'),
    ('float32-far-path',precision,'Float32 trajectory segment'),
    ('float32-inbounds-path-only',path_only,'Float32 trajectory segment'),
    ('float32-inbounds-triangle-only',triangle_only,'Float32 potential triangle'),
    ('float32-inbounds-combined',inbounds,'Float32 trajectory segment'),
    ('float32-source-line',line_collapse,'Float32 source line segment'),
    ('float32-three-distinct-collinear',collinear,'Float32 potential triangle'),
    ('float32-second-triangle',second_triangle,'Float32 potential triangle'),
    ('float32-below-ulp',below_ulp,'Float32 trajectory segment'),
    ('float32-binary64-loss',binary64_loss,'Float32 trajectory segment'),
    ('float32-exact-degenerate',exact_degenerate,'Float32 potential triangle')
]
fixtures=positives+[(n,s) for n,s,_ in negatives]
by_name={name:scene for name,scene in fixtures}
records={}
for name,scene in fixtures:
    blob=(json.dumps(scene,separators=(',',':'),allow_nan=False)+'\n').encode()
    (runtime/(name+'.json')).write_bytes(blob)
    records[name]={'title':name,'file':name+'.json',
                   'input':'independent reviewer R3 fixture',
                   'sha256':sha256(blob).hexdigest()}

(runtime/'manifest.json').write_text(json.dumps({
    'scenes':list(records.values()),'physics_in_browser':False,'prototype':True
}))
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(runtime)))
thread=Thread(target=server.serve_forever,daemon=True)
thread.start()
baseurl='http://127.0.0.1:'+str(server.server_port)+'/'
page_errors=[]
positive_evidence=[]
refusals=[]
recoveries=[]
failure=None

def own_page(browser,items):
    page=browser.new_page(viewport={'width':1280,'height':900})
    page.on('pageerror',lambda error:page_errors.append(str(error)))
    manifest={'scenes':[records[n] for n in items],
              'physics_in_browser':False,'prototype':True}
    page.route('**/manifest.json',lambda route:route.fulfill(
        status=200,content_type='application/json',body=json.dumps(manifest)))
    page.goto(baseurl,wait_until='networkidle',timeout=30000)
    return page

def loaded(page,name,construction_count):
    expect_sha=records[name]['sha256']
    page.wait_for_function('(sha)=>{const s=window.emfeeldPreview?.inspect();return !!s?.available && s?.source?.sha256===sha && !document.querySelector("#scene").disabled}',
                           arg=expect_sha,timeout=20000)
    s=page.evaluate('window.emfeeldPreview.inspect()')
    assert s['three_revision']=='180',s['three_revision']
    assert 'WebGL 2.0' in s['webgl_version'],s['webgl_version']
    assert s['snapshot']==by_name[name]
    assert s['source']['sha256']==expect_sha
    assert s['actor_count']>0 and s['construction_count']==construction_count,s
    assert s['frame']['index']>=0
    assert page.locator('#play').is_enabled()
    assert page.locator('#error').is_hidden()
    return s

def refused(page,expected,construction_count):
    page.wait_for_function('(reason)=>!!window.emfeeldPreviewError && window.emfeeldPreviewError.includes(reason) && !document.querySelector("#scene").disabled',
                           arg=expected,timeout=20000)
    message=page.evaluate('window.emfeeldPreviewError')
    assert expected in message and 'checksum' not in message.lower(),message
    s=page.evaluate('window.emfeeldPreview.inspect()')
    assert not s['available'] and s['actor_count']==0,s
    assert s['construction_count']==construction_count,s
    assert s['frame'] is None and s['snapshot'] is None and s['source'] is None,s
    assert page.locator('#error').is_visible()
    assert page.locator('#title').inner_text()=='Preview unavailable'
    for k in ('frame','play','reset','potential'):
        assert page.locator('#'+k).is_disabled(),k
    for k in ('positions','time','range','notes','provenance'):
        assert page.locator('#'+k).text_content()=='',k
    return message

def advanced_real_playback(page):
    page.click('#play')
    page.wait_for_function('Number(document.querySelector("#frame").value)>0',
                           timeout=10000)
    assert page.locator('#time').inner_text().startswith('Sample ')
    assert page.locator('#positions').inner_text().startswith('Particle ')
    return int(page.locator('#frame').input_value())

try:
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,args=[
            '--no-sandbox','--enable-unsafe-swiftshader','--disable-dev-shm-usage'
        ])
        for name,_ in positives:
            page=own_page(browser,[name])
            try:
                s=loaded(page,name,1)
                assert s['snapshot']==by_name[name]
                assert s['source']['sha256']==records[name]['sha256']
                if name=='ordinary':
                    page.locator('#frame').fill('17')
                    page.locator('#frame').dispatch_event('input')
                    t=page.evaluate('window.emfeeldPreview.inspect()')
                    expected=by_name[name]['trajectories'][0]['positions_m'][17]
                    assert t['frame']['positions_m'][0]==expected
                    assert t['frame']['index']==17
                    assert math.isclose(t['frame']['time_s'],8.5,rel_tol=1e-14)
                    assert 'Play/Pause button' in page.locator('#notes').inner_text()
                    page.uncheck('#potential')
                    assert page.evaluate('window.emfeeldPreview.inspect().potential_visible') is False
                    page.check('#potential')
                    assert page.evaluate('window.emfeeldPreview.inspect().potential_visible') is True
                    page.screenshot(path=str(out/'r3-ordinary-webgl2.png'))
                if name=='huge':
                    assert all(math.isfinite(x) for x in s['transform']['origin_m'])
                    page.screenshot(path=str(out/'r3-huge-webgl2.png'))
                if name=='null-hole':
                    assert s['omitted_cells']==1
                if name=='stationary':
                    assert len({tuple(pt) for pt in by_name[name]['trajectories'][0]['positions_m']})==1
                if name=='fine':
                    assert s['potential_visible'] is True
                    page.screenshot(path=str(out/'r3-fine-webgl2.png'))
                positive_evidence.append({'case':name,'webgl':s['webgl_version'],
                                          'sha256':records[name]['sha256'],
                                          'construction_count':1,'actors':s['actor_count']})
            finally:
                page.close()
        # Each refusal is a separate matched SHA request so one failing validator
        # does not mask a different geometry case.
        for name,scene,reason in negatives:
            page=own_page(browser,[name,'ordinary'])
            try:
                msg=refused(page,reason,0)
                if name in ('float32-inbounds-path-only','float32-inbounds-triangle-only',
                            'float32-source-line','float32-second-triangle'):
                    page.screenshot(path=str(out/(name+'-startup-refusal.png')))
                refusals.append({'case':name,'expected':reason,'reported_error':msg,
                                 'sha256':records[name]['sha256'],
                                 'startup_actor_count':0,'startup_construction_count':0})
                page.select_option('#scene','1')
                loaded(page,'ordinary',1)
                ix=advanced_real_playback(page)
                page.click('#play')
                recoveries.append({'case':name,'path':'invalid startup -> valid advancing replay',
                                   'advanced_to_index':ix,'construction_count':1})
            finally:
                page.close()
            # Start with an actually playing valid scene, force a refusal, then
            # verify disposal of old actors/readouts and a fresh playable scene.
            page=own_page(browser,['ordinary',name])
            try:
                loaded(page,'ordinary',1)
                ix=advanced_real_playback(page)
                page.select_option('#scene','1')
                msg2=refused(page,reason,1)
                assert msg2==msg
                page.select_option('#scene','0')
                s=loaded(page,'ordinary',2)
                assert s['actor_count']>0
                ix2=advanced_real_playback(page)
                page.click('#play')
                recoveries.append({'case':name,
                                   'path':'valid -> playing -> invalid -> valid advancing replay',
                                   'advanced_before_refusal':ix,
                                   'advanced_after_recovery':ix2,'construction_count':2})
            finally:
                page.close()
        assert not page_errors,page_errors
        browser.close()
except Exception as error:
    failure=repr(error)
    raise
finally:
    server.shutdown()
    server.server_close()
    thread.join()
    report={
      'execution_owner':'new independent reviewer R3 using prior reviewer scaffold',
      'source_merge_commit':'5c0f5a2480510177f1f6be329936945bb9b16efc',
      'source_head':'f90d536b29d1d253966d1e53bcfe3ae22b36f4fe',
      'source_tree':'77c03d1092fe1c55a1c4641b82402894eb5d4155',
      'browser':'Chromium with actual WebGL2',
      'result':'PASS' if failure is None and not page_errors else 'FAIL',
      'failure':failure,
      'page_errors':page_errors,
      'positive_controls':positive_evidence,
      'matched_hash_refusals':refusals,
      'advancing_recovery_paths':recoveries,
      'note':'This is reviewer-authored execution, not author CI or physics re-review'
    }
    (out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
print('R3 new independent Chromium WebGL2 checks PASS: %d positives, %d refusals, %d replay recovery paths, %d page errors'
      %(len(positive_evidence),len(refusals),len(recoveries),len(page_errors)))
