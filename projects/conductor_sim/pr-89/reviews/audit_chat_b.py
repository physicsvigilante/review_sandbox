"""Chat B read-only production identity/CI collection; no API mutations."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import urllib.request

MODE, SOURCE, OUTPUT = sys.argv[1:]
SOURCE, OUTPUT = Path(SOURCE), Path(OUTPUT)
OUTPUT.mkdir(parents=True, exist_ok=True)
REPO='physicsvigilante/conductor_sim'
HEAD='75c984aaae18e44997332e330ed3a519a7b6a8da'
TREE='e1dbb9bb673f4efc2950939d0c1e021697393d59'
BASE='dc347251c14e449c53d51820b4481d1bfbee2cfb'
BASE_TREE='60b4f21aa88a2031ec50c5d1e7c15a5135a7becf'
CHARTER='89dae06df53403a8fab6743ad8bdcc10fc76c514'
EXPECTED={'.github/workflows/m37a-grounded-sphere-wire.yml','docs/m37a.md',
'docs/m37a_charter.md','examples/grounded_sphere_wire_current.py',
'src/conductor_sim/__init__.py','src/conductor_sim/grounded_sphere_wire.py',
'tests/test_m37a_grounded_wire_current.py','tools/m37a_ground_wire_reference.py'}

def git(*args):
    return subprocess.check_output(['git','-C',str(SOURCE),*args],text=True).strip()

def save(name,data):
    (OUTPUT/name).write_text(json.dumps(data,indent=2)+'\n')

def raw_api(path):
    req=urllib.request.Request('https://api.github.com/repos/'+REPO+'/'+path,
        headers={'Accept':'application/vnd.github+json','User-Agent':'independent-chat-b-pr89',
                 'Authorization':'Bearer '+os.environ['GH_TOKEN']})
    with urllib.request.urlopen(req,timeout=60) as response:
        return response.read()

def api(path): return json.loads(raw_api(path))

def pages(path,key):
    output=[]
    page=1
    while True:
        sep='&' if '?' in path else '?'
        data=api(path+sep+f'per_page=100&page={page}')
        output.extend(data[key])
        if len(data[key])<100: return output
        page+=1

pr=api('pulls/89')
identity=dict(observed_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    live_head=pr['head']['sha'],live_base=pr['base']['sha'],draft=pr['draft'],
    merged=pr['merged'],state=pr['state'],native_head=git('rev-parse','HEAD'),
    native_tree=git('rev-parse','HEAD^{tree}'),native_base_tree=git('rev-parse',BASE+'^{tree}'),
    changed_files=git('diff','--name-only',BASE,HEAD).splitlines(),
    workflow_run_id=os.environ.get('GITHUB_RUN_ID'),workflow_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
    review_script_sha=os.environ.get('GITHUB_SHA'))
save('identity-'+MODE+'.json',identity)
assert identity['live_head']==HEAD and identity['native_head']==HEAD, 'STALE: head changed'
assert identity['native_tree']==TREE, 'STALE: native tree changed'
assert identity['native_base_tree']==BASE_TREE
assert identity['draft'] and not identity['merged'] and identity['state']=='open'
assert set(identity['changed_files'])==EXPECTED and len(identity['changed_files'])==8
subprocess.run(['git','-C',str(SOURCE),'merge-base','--is-ancestor',CHARTER,HEAD],check=True)
assert git('diff-tree','--no-commit-id','--name-only','-r',CHARTER)=='docs/m37a_charter.md'
assert git('show',CHARTER+':docs/m37a_charter.md')==git('show',HEAD+':docs/m37a_charter.md')
print('NATIVE_IDENTITY '+json.dumps(identity),flush=True)
if MODE=='identity': sys.exit(0)

all_runs=pages('actions/runs?head_sha='+HEAD,'workflow_runs')
full=[]
compact=[]
for run in all_runs:
    assert run['head_sha']==HEAD
    jobs=pages('actions/runs/'+str(run['id'])+'/jobs?filter=latest','jobs')
    full.append(dict(run=run,jobs=jobs))
    compact.append(dict(id=run['id'],name=run['name'],event=run['event'],
        path=run['path'],status=run['status'],conclusion=run['conclusion'],
        head_sha=run['head_sha'],attempt=run['run_attempt'],url=run['html_url'],
        jobs=[dict(id=j['id'],name=j['name'],status=j['status'],conclusion=j['conclusion'],
                   steps=[dict(name=s['name'],status=s['status'],conclusion=s.get('conclusion')) for s in j.get('steps',[])]) for j in jobs]))
save('exact-head-ci-full.json',full)
save('exact-head-ci-summary.json',compact)
for entry in compact:
    print('EXACT_HEAD_RUN '+json.dumps(entry),flush=True)

base=pages('actions/runs?head_sha='+BASE+'&event=push','workflow_runs')
base_summary=[{k:r.get(k) for k in ('id','name','event','head_sha','status','conclusion','html_url')} for r in base]
save('released-base-push-ci.json',base_summary)
print('BASE_PUSH_CI '+json.dumps(base_summary),flush=True)

historical=pages('actions/workflows/m37a-grounded-sphere-wire.yml/runs?branch=m37a-grounded-sphere-wire-current','workflow_runs')
reds=[]
for r in historical:
    if r['head_sha']==HEAD or r['conclusion']!='failure': continue
    item={k:r.get(k) for k in ('id','name','event','head_sha','status','conclusion','html_url','run_attempt')}
    jobs=pages('actions/runs/'+str(r['id'])+'/jobs?filter=latest','jobs')
    item['failed_jobs']=[]
    for j in jobs:
        if j['conclusion']!='failure': continue
        detail=dict(id=j['id'],name=j['name'],conclusion=j['conclusion'])
        try:
            logs=raw_api('actions/jobs/'+str(j['id'])+'/logs').decode('utf-8',errors='replace')
            (OUTPUT/f'historical-red-job-{j["id"]}.log').write_text(logs)
            detail['test_summary_lines']=[line for line in logs.splitlines()
                if re.search(r'\d+ failed.*\d+ passed|\d+ passed.*\d+ failed',line)]
        except Exception as exc:
            detail['log_retrieval_error']=repr(exc)
        item['failed_jobs'].append(detail)
    reds.append(item)
save('historical-red-m37a-runs.json',reds)
print('PRESERVED_HISTORICAL_REDS '+json.dumps(reds),flush=True)

pdf=SOURCE/'02_conductors_half_size.pdf'
pdf_identity=dict(path=str(pdf.name),bytes=pdf.stat().st_size,
    sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
    git_blob=git('rev-parse',HEAD+':02_conductors_half_size.pdf'),
    base_git_blob=git('rev-parse',BASE+':02_conductors_half_size.pdf'))
assert pdf_identity['git_blob']==pdf_identity['base_git_blob']
save('original-pdf-identity.json',pdf_identity)
print('PDF_IDENTITY '+json.dumps(pdf_identity),flush=True)
summary=dict(exact_head_runs=len(compact),
    successful_runs=sum(r['status']=='completed' and r['conclusion']=='success' for r in compact),
    pending_runs=sum(r['status']!='completed' for r in compact),
    failed_or_cancelled_runs=sum(r['status']=='completed' and r['conclusion']!='success' for r in compact),
    all_success=bool(compact) and all(r['status']=='completed' and r['conclusion']=='success' for r in compact),
    released_base_push_runs=len(base_summary),
    released_base_push_success=sum(r['status']=='completed' and r['conclusion']=='success' for r in base_summary),
    historical_failed_runs=len(reds))
save('ci-totals.json',summary)
print('CI_TOTALS '+json.dumps(summary),flush=True)
