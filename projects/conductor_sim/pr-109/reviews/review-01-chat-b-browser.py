#!/usr/bin/env python3
"""Independent Chromium playback/accessibility probe for frozen JEE-12 HTML artifacts.

Unzip GitHub Actions artifacts into ARTIFACTS_DIR/m36b, m36c and m36e:
  m36b artifact 14611803912; m36c 14612177823; m36e 14612510752.
Run: python review-01-chat-b-browser.py --artifacts ARTIFACTS_DIR
Requires Python playwright and its Chromium browser (or --chromium /path/to/chromium).
The HTML bytes are loaded directly with set_content because some restricted
runtimes reject file://. This does not rerun the scientific solver.
"""
import argparse
import json
import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--artifacts',type=Path,default=Path.cwd(),help='directory with m36b/, m36c/, m36e/')
parser.add_argument('--chromium',help='optional Chromium executable path')
a=parser.parse_args()
root=a.artifacts.resolve()
files=[('p2-sheet-stop',root/'m36b/sheet-stop.html'),
       ('p27-two-shells',root/'m36c/p27-cavity-two-shells.html'),
       ('p26-solid',root/'m36e/p26-true-solid-sphere.html')]
for name,p in files:
    if not p.is_file(): parser.error(f'{name}: missing {p}; extract the GitHub Actions artifact first')
for group in ('m36b','m36c','m36e'):
    tree=(root/group/'source-tree.txt').read_text().strip()
    assert tree=='ddcc0b9923584495f78e2ea05a7f1ff56622e8d2',(group,tree)
results={}
with sync_playwright() as p:
    opts={'headless':True,'args':['--no-sandbox','--disable-gpu']}
    binary=a.chromium or shutil.which('chromium') or shutil.which('chromium-browser')
    if binary: opts['executable_path']=binary
    browser=p.chromium.launch(**opts)
    for case,source in files:
        entries={}
        for mode in ('desktop-js','mobile-js','mobile-nojs'):
            context=browser.new_context(viewport={'width':1280,'height':850} if mode=='desktop-js'
                      else {'width':375,'height':740},device_scale_factor=1,
                      is_mobile=mode!='desktop-js',has_touch=mode!='desktop-js',
                      java_script_enabled=mode!='mobile-nojs')
            page=context.new_page()
            errors=[]
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.set_content(source.read_text(encoding='utf8'),wait_until='load',timeout=30000)
            page.wait_for_timeout(250)
            view=page.evaluate('''() => {let b=document.body;return {
              text:b.innerText.slice(0,2400),
              width:b.scrollWidth, viewWidth:window.innerWidth,
              sliders:[...document.querySelectorAll('input[type=range]')]
                    .map(x=>({id:x.id,value:x.value,max:x.max}))}}''')
            result={'errors':errors,'horizontal_overflow_px':view['width']-view['viewWidth'],
                    'sliders':view['sliders'],'visible_text_head':view['text']}
            assert result['horizontal_overflow_px']<=1,(case,mode,'horizontal overflow')
            assert case!='p27-two-shells' or 'TEACHER EXTENSION ONLY' in view['text']
            if mode!='mobile-nojs':
                assert not errors,(case,mode,errors)
                assert 'Physical t' in view['text'] if case=='p2-sheet-stop' else 'Stored state' in view['text']
            if mode=='desktop-js':
                slider=page.locator('input#frame')
                maximum=int(slider.get_attribute('max') or 0)
                assert maximum>0
                slider.fill(str(maximum));slider.dispatch_event('input');page.wait_for_timeout(200)
                ending=page.locator('body').inner_text()
                ending_norm=' '.join(ending.split())
                result['final_state_excerpt']=ending[:1800]
                if case=='p2-sheet-stop':
                    assert '1.492873584e-10 s' in ending
                    assert 'computed state 9/9' in ending
                elif case=='p27-two-shells':
                    assert 'Stored state 2 / 2' in ending_norm,repr(ending_norm[:1100])
                    assert 'TEACHER EXTENSION ONLY: shifted q' in ending_norm
                elif case=='p26-solid':
                    assert 'Stored state 3 / 3' in ending_norm,repr(ending_norm[:1100])
            if mode!='desktop-js':
                image_path=root/f'{case}-{mode}.png'
                page.screenshot(path=str(image_path),full_page=True)
                result['screenshot']=str(image_path)
            entries[mode]=result
            context.close()
        results[case]=entries
    browser.close()
(root/'browser_review_results.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf8')
print('PASS: three original HTML files; desktop/mobile JS states, zero JS errors, no horizontal overflow; no-JS observation captured')
print('No-JS finding: explanatory source banners remain, but rendered diagram/result panels may be empty; no explicit noscript notice')
