import json, os
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path('/mnt/data/conductor_review_109')
files=[('p2-sheet-stop',root/'m36b/sheet-stop.html'),('p27-two-shells',root/'m36c/p27-cavity-two-shells.html'),('p26-solid',root/'m36e/p26-true-solid-sphere.html')]
res={}
with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-gpu'])
  for case,file in files:
    entries={}
    for mode in ['desktop-js','mobile-js','mobile-nojs']:
      context=browser.new_context(viewport={'width':1280,'height':850} if mode=='desktop-js' else {'width':375,'height':740},device_scale_factor=1,is_mobile=mode!='desktop-js',has_touch=mode!='desktop-js',java_script_enabled=mode!='mobile-nojs')
      page=context.new_page()
      errs=[]
      page.on('pageerror',lambda e:errs.append(str(e)))
      page.set_content(file.read_text(encoding='utf8'),wait_until='load',timeout=30000)
      page.wait_for_timeout(280)
      v=page.evaluate('''() => {let b=document.body;return {text:b.innerText.slice(0,1800),width:b.scrollWidth,viewWidth:window.innerWidth,inputs:[...document.querySelectorAll('input[type=range]')].map(x=>({id:x.id,value:x.value,max:x.max})),readouts:[...document.querySelectorAll('[id]')].filter(e=>/status|potential|answer|value|frame|state/i.test(e.id)).slice(0,35).map(e=>({id:e.id,text:(e.innerText||'').slice(0,100)}))}}''')
      out={'js':mode!='mobile-nojs','errors':errs,'horizontal_overflow_px':v['width']-v['viewWidth'],'inputs':v['inputs'],'readout_elements':v['readouts'][:12], 'body_text_head':v['text'][:700]}
      if mode=='desktop-js':
        slider=page.locator('input#frame')
        if slider.count():
          mx=int(slider.get_attribute('max') or 0)
          if mx>0:
            slider.fill(str(mx))
            slider.dispatch_event('input')
            page.wait_for_timeout(200)
            out['after_last_state_text']=page.locator('body').inner_text()[:1800]
            out['last_state_selected']=slider.input_value()
      if mode!='desktop-js':
        page.screenshot(path=str(root/f'{case}-{mode}.png'),full_page=True)
      entries[mode]=out
      context.close()
    res[case]=entries
  browser.close()
(root/'browser_review_results.json').write_text(json.dumps(res,indent=2))
for case,modes in res.items():
 print('\n===',case,'===')
 for mode,data in modes.items():
  print(mode, 'over',data['horizontal_overflow_px'], 'js-errors',data['errors'], 'inputs',data['inputs'])
  print('TEXT:',data['body_text_head'][:500].replace('\n',' // '))
  if 'after_last_state_text' in data: print('AFTER:',data['after_last_state_text'][:420].replace('\n',' // '))
