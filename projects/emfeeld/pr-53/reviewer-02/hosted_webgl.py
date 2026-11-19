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
fixtures=[('ordinary',base),('huge',huge),('wrong-role',role),('subnormal-arrow',subnormal),('float32-collapse',precision),('float32-inbounds',inbounds)]
entries=[]
for name,scene in fixtures:
    blob=(json.dumps(scene,separators=(',',':'),allow_nan=False)+'\n').encode()
    (runtime/(name+'.json')).write_bytes(blob)
    entries.append({'title':name,'file':name+'.json','input':'reviewer-created fixture',
                    'sha256':sha256(blob).hexdigest()})
(runtime/'manifest.json').write_text(json.dumps({'scenes':entries,'physics_in_browser':False,'prototype':True}))
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(runtime)))
worker=Thread(target=server.serve_forever,daemon=True)
worker.start()
errors=[];evidence=[]
baseurl='http://127.0.0.1:'+str(server.server_port)+'/'
def loaded(page,expected):
    # The previous scene can remain available during an asynchronous selection.
    # Wait for the exact SHA of the requested scene, not a truthy stale group.
    expected_hash=next(e['sha256'] for (name,scene),e in zip(fixtures,entries) if scene is expected)
    page.wait_for_function('(sha)=>{const r=window.emfeeldPreview?.inspect();return r?.available && r?.source?.sha256===sha}',arg=expected_hash,timeout=20000)
    s=page.evaluate('window.emfeeldPreview.inspect()')
    assert s['three_revision']=='180'
    assert 'WebGL 2.0' in s['webgl_version'],s['webgl_version']
    assert s['snapshot']==expected
    assert s['actor_count']>0 and s['source']['sha256'] in [e['sha256'] for e in entries]
    return s
def refused(page,previous_count):
    page.wait_for_function('!!window.emfeeldPreviewError',timeout=15000)
    assert page.locator('#error').is_visible()
    s=page.evaluate('window.emfeeldPreview.inspect()')
    assert not s['available'] and s['actor_count']==0
    assert s['construction_count']==previous_count
    assert s['snapshot'] is None and s['frame'] is None and s['source'] is None
    for id in ('play','frame','potential','reset'):assert page.locator('#'+id).is_disabled(),id
    for id in ('positions','time','range','notes','provenance'):assert page.locator('#'+id).text_content()=='',id
    assert 'checksum' not in page.locator('#error').text_content().lower()
def frame(page,expected,index):
    page.locator('#frame').fill(str(index))
    page.locator('#frame').dispatch_event('input')
    s=page.evaluate('window.emfeeldPreview.inspect()')
    assert s['frame']['index']==index
    assert math.isclose(s['frame']['time_s'],index*expected['animation']['duration_s']/40,rel_tol=1e-13)
    pos=expected['trajectories'][0]['positions_m'][index]
    assert s['frame']['positions_m'][0]==pos
    target=[(v-o)/s['transform']['scale_m'] for v,o in zip(pos,s['transform']['origin_m'])]
    assert all(math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-12) for a,b in zip(target,s['marker_display'][0]))
    assert s['snapshot']==expected
try:
    with sync_playwright() as playwright:
        browser=playwright.chromium.launch(headless=True,args=['--no-sandbox','--enable-unsafe-swiftshader','--disable-dev-shm-usage'])
        page=browser.new_page(viewport={'width':1280,'height':900})
        page.on('pageerror',lambda error:errors.append(str(error)))
        page.goto(baseurl,wait_until='networkidle')
        loaded(page,base)
        for i in (0,17,40):frame(page,base,i)
        assert 'Play/Pause button' in page.locator('#notes').text_content()
        assert 'Space:' not in page.locator('#notes').text_content()
        assert page.evaluate('window.emfeeldPreview.inspect().snapshot')['annotations'][0]['text'].startswith('Space:')
        page.uncheck('#potential')
        assert page.evaluate('window.emfeeldPreview.inspect().potential_visible') is False
        page.check('#potential')
        assert page.evaluate('window.emfeeldPreview.inspect().potential_visible') is True
        old=page.evaluate('window.emfeeldPreview.inspect().camera')
        box=page.locator('#canvas canvas').bounding_box()
        page.mouse.move(box['x']+box['width']/2,box['y']+box['height']/2)
        page.mouse.down()
        page.mouse.move(box['x']+box['width']*.65,box['y']+box['height']*.62,steps=8)
        page.mouse.up()
        page.wait_for_function('(c)=>JSON.stringify(window.emfeeldPreview.inspect().camera)!==JSON.stringify(c)',arg=old)
        page.screenshot(path=str(out/'reviewer-ordinary-webgl2.png'))
        evidence.append('ordinary: WebGL2, actual marker transforms and times, help, orbit, potential toggle')
        page.select_option('#scene','1')
        s=loaded(page,huge);frame(page,huge,20)
        assert all(math.isfinite(x) for x in s['transform']['origin_m'])
        assert not math.isfinite((huge['bounds_m'][0]+huge['bounds_m'][1])/2)
        page.screenshot(path=str(out/'reviewer-huge-positive-webgl2.png'))
        evidence.append('positive: finite huge midpoint, real WebGL2')
        page.select_option('#scene','2')
        refused(page,2)
        page.screenshot(path=str(out/'reviewer-role-refusal.png'))
        evidence.append('wrong meaning role: matched-hash visible refusal, no stale actors/readouts')
        page.select_option('#scene','3')
        refused(page,2)
        evidence.append('subnormal arrow: matched-hash refusal before THREE construction')
        page.select_option('#scene','0')
        loaded(page,base)
        page.click('#play')
        page.wait_for_function('Number(document.querySelector("#frame").value)>0',timeout=8000)
        page.click('#play')
        evidence.append('valid-invalid-valid: actual replay advanced after recovery')
        page.select_option('#scene','4')
        loaded(page,precision)
        # Renderer creates Float32BufferAttribute for triangles; line.setFromPoints also stores Float32.
        x=[p[0]/20. for p in precision['trajectories'][0]['positions_m']]
        import struct
        q=lambda v:struct.unpack('f',struct.pack('f',v))[0]
        assert len(set(x))==41 and len(set(map(q,x)))==1
        evidence.append('ADMISSION DEFECT: 41 distinct saved trajectory samples collapse to 1 Float32 coordinate')
        page.screenshot(path=str(out/'reviewer-float32-loss-admitted.png'))
        page.select_option('#scene','5')
        loaded(page,inbounds)
        # All positions are inside the declared bounds; strict Float64 distinctions
        # nevertheless vanish in the Float32BufferAttribute used by THREE.
        x=[(p[0]-0.)/20. for p in inbounds['trajectories'][0]['positions_m']]
        assert len(set(x))==61 and len(set(map(q,x)))==1
        points=inbounds['potential']['points_m']
        corners=[points[0][0],points[1][0],points[1][1]]
        display_corners=[tuple(v/20. for v in p) for p in corners]
        assert len(set(display_corners))==3
        assert len(set(tuple(q(v) for v in p) for p in display_corners))==1
        evidence.append('ADMISSION DEFECT: 61/61 in-bounds physical positions and triangle collapse to Float32 point')
        page.screenshot(path=str(out/'reviewer-float32-loss-inbounds-webgl2.png'))
        page.close()
        startup=browser.new_page(viewport={'width':1280,'height':900})
        startup.on('pageerror',lambda error:errors.append(str(error)))
        startup.route('**/manifest.json',lambda route:route.fulfill(status=200,content_type='application/json',
            body=json.dumps({'scenes':[entries[2],entries[0]]})))
        startup.goto(baseurl,wait_until='networkidle')
        refused(startup,0)
        startup.select_option('#scene','1')
        loaded(startup,base)
        startup.click('#play')
        startup.wait_for_function('Number(document.querySelector("#frame").value)>0',timeout=8000)
        startup.click('#play')
        evidence.append('invalid startup: inspection hook survived; real recovered replay advanced')
        startup.screenshot(path=str(out/'reviewer-startup-recovery.png'))
        startup.close()
        assert not errors,errors
        browser.close()
finally:
    server.shutdown()
    server.server_close()
    worker.join()
report={'reviewer_owned':True,'source_commit':'640c1d0d83981a7a39fe9bef989bab54199689a7',
        'source_tree':'84135a2482ab8d277a206120f1de90bb7ce297e7',
        'browser_executed':'Chromium WebGL2','browser_page_errors':errors,
        'checks':evidence,'known_defect':'Distinct Float32 trajectory/surface geometry collapses despite validator admission'}
(out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
print('REVIEWER OWNED WEBGL2 EVIDENCE:',len(evidence),'checks, zero page errors; known defect reproduced')
