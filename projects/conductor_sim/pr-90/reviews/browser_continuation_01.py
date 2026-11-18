"""Finish genuine Chromium baseline after reviewer's SVG API error.
Does not alter production or relabel the first failed review. Reuses exact
first-run generated data and the same four browser assertions, correcting
only SVG inner_text to text_content. Run from pinned production checkout.
"""
import ast
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.request
from playwright.sync_api import sync_playwright

HEAD='155b0544684d3d880a83a661cc8e14a0ce22f26b'
TREE='f48f54b8c49217b7c66179fe014b6fab1ea4dc4d'
first=Path(sys.argv[1]).resolve()
out=Path(sys.argv[2]).resolve()
out.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(first))
from chat_b_kelvin_oracle import verify_trace, close


def save(name,data):
    (out/name).write_text(json.dumps(data,indent=2)+'\n')


def api(path):
    req=urllib.request.Request('https://api.github.com/repos/physicsvigilante/conductor_sim/'+path,
        headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json',
                 'User-Agent':'PR90-Chat-B-scoped-browser-continuation'})
    with urllib.request.urlopen(req,timeout=60) as response:
        return json.load(response)


def identity(label):
    assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==HEAD
    assert subprocess.check_output(['git','rev-parse','HEAD^{tree}'],text=True).strip()==TREE
    pr=api('pulls/90')
    assert pr['head']['sha']==HEAD and pr['draft'] and not pr['merged'] and pr['state']=='open','STALE production'
    runs=api('actions/runs?head_sha='+HEAD+'&per_page=100')
    assert runs['total_count']==len(runs['workflow_runs'])==26
    assert all(r['status']=='completed' and r['conclusion']=='success' and r['head_sha']==HEAD for r in runs['workflow_runs'])
    save(label+'-identity-ci.json',{'head':HEAD,'tree':TREE,'draft':pr['draft'],'merged':pr['merged'],
         'runs':[{k:r[k] for k in ('id','name','head_sha','event','status','conclusion','html_url')} for r in runs['workflow_runs']]})


identity('start')
assert json.loads((first/'source-provenance.json').read_text())['head']==HEAD
assert json.loads((first/'source-provenance.json').read_text())['tree']==TREE
source=(first/'chat_b_review_01.py').read_text()
old="page.locator('#m37b-q-sign').inner_text() == '+q'"
new="page.locator('#m37b-q-sign').text_content().strip() == '+q'"
assert source.count(old)==1
corrected=source.replace(old,new)
functions={'observe_context','assert_visible_state','assert_curve','browser_baseline'}
selected=[node for node in ast.parse(corrected).body if isinstance(node,ast.FunctionDef) and node.name in functions]
assert len(selected)==4
manifest=json.loads((first/'genuine/p8-ground-current.json').read_text())
namespace=dict(json=json,OUT=out,GENUINE=first/'genuine',MANIFEST=manifest,
               EXPECTED=verify_trace(manifest['trace']),close=close,verify_trace=verify_trace,
               sync_playwright=sync_playwright,ALL_HTTP=[],ALL_ERRORS=[])
exec(compile(ast.Module(body=selected,type_ignores=[]),'<reviewer-baseline-one-line-correction>','exec'),namespace)
baseline=namespace['browser_baseline']()
with sync_playwright() as pw:
    browser=pw.chromium.launch()
    version=browser.version
    context=browser.new_context(viewport={'width':1280,'height':900})
    requests=[];errors=[]
    namespace['observe_context'](context,requests,errors)
    page=context.new_page()
    page.goto((first/'html-attacks/broken-play/p8-ground-current.html').as_uri())
    initial=page.locator('#m37b-index').input_value()
    page.locator('#m37b-play').click()
    page.wait_for_timeout(550)
    after=page.locator('#m37b-index').input_value()
    assert initial==after=='0',(initial,after)
    page.screenshot(path=str(out/'broken-play-remains-at-zero.png'),full_page=True)
    context.close();browser.close()
assert not requests and not errors
identity('end')
assert not subprocess.check_output(['git','diff','--'],text=True).strip()
result={
    'reviewer':'GPT-6 Astra Pro / Chat B','candidate_head':HEAD,'candidate_tree':TREE,
    'source_run':44352091700,
    'source_artifact_sha256':'ed84ec82b5e4c6309c3b0e946fa5766ee582b5697ea37f3f4b8220bd2a7ca088',
    'scope':'Actual Chromium on exact first-run generated HTML/JSON, fresh pinned source identity; no native rerun or production edits',
    'reviewer_harness_correction':{'old':old,'new':new},
    'python_version':sys.version,'playwright_version':importlib.metadata.version('playwright'),
    'chromium_version':version,'genuine_browser_baseline':'PASS','details':baseline,
    'selected_indices':[0,2,8,16,23,29,30],'play_restart_checked_desktop_and_mobile':True,
    'all31_drawn_curve_points_independently_verified':True,
    'nojs_all5_SI_readouts_and_scene_marker_checked':True,
    'baseline_http_requests':namespace['ALL_HTTP'],'baseline_javascript_errors':namespace['ALL_ERRORS'],
    'broken_play_forgery_confirmed':{'initial_index':initial,'index_after_550ms':after},
    'input_hashes':{name:hashlib.sha256((first/'genuine'/name).read_bytes()).hexdigest()
                   for name in ('p8-ground-current.html','p8-ground-current.json')},
    'first_reviewer_script_sha256':hashlib.sha256((first/'chat_b_review_01.py').read_bytes()).hexdigest(),
    'first_failed_workflow_and_error_preserved':True,
    'local_infrastructure_attempts_not_production_failures':[
        'Initial clone could not resolve github.com; no local production tests ran.',
        'Local scoped browser continuation failed before reading page: net::ERR_BLOCKED_BY_ADMINISTRATOR on file URL.']
}
save('browser-continuation-results.json',result)
print(json.dumps(result,indent=2),flush=True)
