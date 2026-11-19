"""Independent Chat B #02: rendered M39b six-cavity browser audit.

This is a NEW reviewer-authored browser checker. It does not import the
author-coordinated supplemental checker or rely on HTML string equality.
Its extra occlusion and two-sided table-scroll probes are distinct.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path("evidence-out/independent-browser")
ROOT.mkdir(parents=True, exist_ok=True)
EXPECTED = [
    ("Alpha_Mixed", [("A_positive", 4e-9), ("A_negative", -1e-9)]),
    ("Beta_TrulyEmpty", []),
    ("Gamma_NetZero", [("C_plus", 2.5e-9), ("C_minus", -2.5e-9)]),
    ("Delta_MixedNegative", [("D_minus", -7e-9), ("D_plus", 0.5e-9)]),
    ("Epsilon_Single", [("E_solo", 1.25e-9)]),
    ("Zeta_LongLabel", [("Zeta_signed_teacher_source_with_stable_ID_2026_11_19", 4.25e-9),
                        ("Zeta_subtract", -0.75e-9)]),
]
ROLE = "TEACHER HYPOTHETICAL · NO VERIFIED ORIGINAL JEE ANSWER"
WARNING = "TOPOLOGY ONLY — NOT TO SCALE — CARD ORDER IS NOT PHYSICAL POSITION"
MEMBERSHIP = ("Teacher-authored source membership. No physical shape, coordinates or "
              "geometric charge containment was verified.")
REFUSAL = ("Whole-face Gauss-law totals ONLY. No local E(x), V(x), sigma(x), "
           "forces, ground-wire current or real 3D field map.")

def demand(ok, why):
    if not ok:
        raise AssertionError(why)

def si(x, unit):
    demand(type(x) in (float, int), "non-numeric SI")
    x = float(x)
    return ("0 " if x == 0 else ("+" if x > 0 else "−") + repr(abs(x)) + " ") + unit

def witness(page, selector, wanted, output):
    loc = page.locator(selector)
    demand(loc.count() == 1, "selector count: " + selector)
    demand(loc.is_visible(), "not visible: " + selector)
    loc.scroll_into_view_if_needed(timeout=5000)
    got = loc.inner_text().strip()
    demand(got == wanted, "rendered value: " + selector + " got=" + repr(got) +
           " wanted=" + repr(wanted))
    css = loc.evaluate("""el => {
      let opacity=1, cursor=el, pseudofakes=[];
      for(;cursor;cursor=cursor.parentElement){
        const st=getComputedStyle(cursor);
        opacity*=Number(st.opacity);
        for(const pse of ['::before','::after']){
          const t=getComputedStyle(cursor,pse).content;
          if(!['none','normal','""'].includes(t)) pseudofakes.push(cursor.tagName+pse+':'+t);
        }
      }
      const s=getComputedStyle(el),r=el.getBoundingClientRect();
      const x=Math.max(1,Math.min(innerWidth-2,r.left+Math.min(48,r.width/2)));
      const y=Math.max(1,Math.min(innerHeight-2,r.top+r.height/2));
      const upper=document.elementFromPoint(x,y);
      const owns=upper && (upper===el || el.contains(upper) || upper.contains(el));
      return {opacity,display:s.display,visibility:s.visibility,
              color:s.color,background:s.backgroundColor,
              fontSize:s.fontSize,clip:s.clipPath,transform:s.transform,
              stroke:s.webkitTextStrokeWidth,x:r.x,y:r.y,
              width:r.width,height:r.height,hit:upper?.tagName,
              hitId:upper?.id || '',unoccluded:!!owns,pseudofakes};
    }""")
    demand(css["opacity"] >= 0.98 and css["display"] != "none"
           and css["visibility"] == "visible" and css["unoccluded"],
           "hidden/occluded text: " + selector + " " + str(css))
    demand(css["width"] > 0 and css["height"] > 0
           and float(css["fontSize"].replace("px","")) >= 10,
           "unreadably small or zero glyph box: " + selector)
    demand(css["clip"] in ("none", "") and css["transform"] in ("none", "")
           and css["stroke"] in ("0px", "0", ""),
           "clipped/masked/transformed: " + selector)
    demand(not css["pseudofakes"], "ancestor or target pseudo text overlay: " +
           selector + " " + str(css["pseudofakes"]))
    demand(not re.search(r"rgba?\([^)]*,\s*0(?:\.0+)?\)$", css["color"])
           and css["color"] != "rgba(0, 0, 0, 0)",
           "transparent value: " + selector)
    output[selector] = {"text": got, "computed": css}

def verify_render(page, m, label, out):
    observations = {}
    demand(page.locator("script,iframe,canvas,svg,img,video,object,embed,link[rel=stylesheet]").count() == 0,
           "script/asset/false spatial graphics inserted")
    witness(page, "#m39b-provenance", ROLE, observations)
    witness(page, "#m39b-warning", WARNING, observations)
    witness(page, "#m39b-membership", MEMBERSHIP, observations)
    witness(page, "#m39b-refusal", REFUSAL, observations)
    witness(page, "#m39b-title", "Gauss law · multiple sealed cavities", observations)
    witness(page, "#m39b-metal", "ReviewerMetal_R6", observations)
    witness(page, "#m39b-original-count",
            "Original JEE source problems newly solved: 0. Workbook p11 and irregular three-cavity notes p70 remain unsupported for local 3D field/density.",
            observations)
    witness(page, "#m39b-zero-warning",
            "A zero entire-face net charge does NOT imply zero local surface charge density throughout that face.",
            observations)
    demand(m["source_role"] == "teacher_hypothetical_topology_gauss_only"
           and type(m["original_workbook_items_newly_solved"]) is int
           and m["original_workbook_items_newly_solved"] == 0
           and m["geometry_verified"] is False
           and m["diagram_is_spatial_geometry"] is False
           and m["time_evolution_defined"] is False,
           "manifest provenance/spatial limit")
    demand(page.locator("#m39b-cavities > .cavity").count() == 6,
           "card count not six")
    for i, (cid, src) in enumerate(EXPECTED):
        row = m["cavities"][i]
        demand(row["cavity_id"] == cid
               and [(s["source_id"],s["charge_c"]) for s in row["authored_sources"]] == src,
               "authored cavity/source mismatch " + cid)
        witness(page, f"#m39b-cavity-{i}", cid, observations)
        witness(page, f"#m39b-q-{i}", si(row["source_charge_sum_c"], "C"), observations)
        witness(page, f"#m39b-inner-{i}",
                si(row["induced_inner_face_total_charge_c"], "C"), observations)
        tag = ("empty cavity" if not src else
               "signed cancellation (local sigma unknown)" if row["source_charge_sum_c"] == 0
               else "charged cavity")
        witness(page, f"#m39b-card-{i} .tag", tag, observations)
        for j, (sid, q) in enumerate(src):
            witness(page, f"#m39b-source-{i}-{j} code", sid, observations)
            witness(page, f"#m39b-source-{i}-{j} .charge", si(q, "C"), observations)
        if not src:
            witness(page, f"#m39b-source-empty-{i}", "No sources assigned", observations)
        box = page.locator(f"#m39b-card-{i}").bounding_box()
        demand(box and box["x"] >= -2 and box["x"]+box["width"] <=
               page.viewport_size["width"]+2, "horizontal card clip: "+cid)
    for state in ("isolated", "grounded"):
        s = m["states"][state]
        for key, value, unit in (
            ("sources", s["total_interior_source_charge_c"], "C"),
            ("metal", s["conductor"]["equilibrium_net_metal_charge_c"], "C"),
            ("outer", s["outer_face_total_charge_c"], "C"),
            ("flux", s["exterior_electric_flux_v_m"], "V·m"),
        ):
            witness(page, f"#m39b-{key}-{state}", si(value, unit), observations)
    witness(page, "#m39b-fixed-isolated",
            si(m["states"]["isolated"]["conductor"]["authored_isolated_metal_charge_c"], "C"),
            observations)
    witness(page, "#m39b-fixed-grounded", "Not a fixed-charge input", observations)
    witness(page, "#m39b-theorem-isolated",
            "Not generally implied for isolated metal", observations)
    witness(page, "#m39b-theorem-grounded",
            "Yes, under declared no-exterior-source boundary", observations)
    demand(page.evaluate("document.documentElement.scrollWidth <= innerWidth + 3"),
           "page-wide horizontal clipping")
    # Novel independent mobile test: both the LEFT LABELS and the RIGHT
    # GROUNDED VALUES must be physically reachable by scrolling this container.
    wrap = page.locator(".table-scroll")
    wrap.scroll_into_view_if_needed()
    geom = wrap.evaluate("""el => {
       const r=el.getBoundingClientRect();
       el.scrollLeft=0;
       const a=el.querySelector('thead th:first-child').getBoundingClientRect();
       const left={position:el.scrollLeft,firstColumnX:a.left,frameX:r.left,
                   reachable:a.right>r.left && a.left<r.right};
       el.scrollLeft=el.scrollWidth;
       const b=el.querySelector('#m39b-flux-grounded').getBoundingClientRect();
       const right={position:el.scrollLeft,groundedX:b.left,
                    reachable:b.right>r.left && b.left<r.right};
       return {clientWidth:el.clientWidth,scrollWidth:el.scrollWidth,left,right};
    }""")
    if page.viewport_size["width"] == 375:
        demand(geom["scrollWidth"] > geom["clientWidth"] and
               geom["right"]["position"] > 0 and
               geom["left"]["reachable"] and geom["right"]["reachable"],
               "both sides of SI comparison table are not scroll-reachable")
        wrap.evaluate("el => el.scrollLeft=0")
        page.screenshot(path=str(ROOT/(label+"-mobile-left.png")),full_page=True)
        wrap.evaluate("el => el.scrollLeft=el.scrollWidth")
        page.screenshot(path=str(ROOT/(label+"-mobile-right.png")),full_page=True)
    evidence={"observed":len(observations),"valuesAndCss":observations,
              "tableBothSides":geom,"viewport":page.viewport_size}
    (ROOT/(label+"-computed-dom.json")).write_text(
        json.dumps(evidence,indent=2,ensure_ascii=False)+"\n")
    return evidence

def forge_cases(html):
    def exact(old,new):
        demand(html.count(old)==1,"hostile replacement anchor missing "+old[:35])
        return html.replace(old,new,1)
    def css(rule):
        return exact("</style>",rule+"</style>")
    # Novel: a DOM overlay retains authentic underlying values, unlike
    # straightforward falsified HTML text. Only hit-testing catches it.
    return {
      "novel-solid-dom-overlay": exact("</body>",
          '<div style="position:fixed;inset:0;z-index:2147483647;background:white;'
          'color:black;font-size:28px;display:flex;align-items:center">'
          'ORIGINAL JEE 7 NEW SOLUTIONS · PHYSICAL 3D FIELD CERTIFIED</div></body>'),
      "novel-card-pseudo-overlay": css(
          '.cavity:first-child::before{content:"ORIGINAL JEE SOLVED";'
          'position:absolute;inset:0;z-index:900;background:#fff;color:#000}'),
      "novel-parent-opacity": css(".metal{opacity:0.02!important}"),
      "false-face-sign": exact('id="m39b-inner-0">−3.0000000000000004e-09 C',
                               'id="m39b-inner-0">+3.0000000000000004e-09 C'),
      "false-exterior-uniqueness": exact(
          "Yes, under declared no-exterior-source boundary",
          "Yes, with any exterior source"),
      "false-flux-unit": exact(
          'id="m39b-flux-isolated" class="charge">−112.94090673730184 V·m',
          'id="m39b-flux-isolated" class="charge">−112.94090673730184 C'),
      "fake-original-claim": exact(ROLE,"ORIGINAL JEE VERIFIED 7 SOLUTIONS"),
    }

def main():
    manifest_file = Path("source/reviewer-six-cavity/manifest.json")
    html_file = Path("source/reviewer-six-cavity/topology.html")
    m = json.loads(manifest_file.read_text())
    html = html_file.read_text()
    assert html.startswith("<!doctype html>")
    result={"manifest_sha256":hashlib.sha256(manifest_file.read_bytes()).hexdigest(),
            "html_sha256":hashlib.sha256(html_file.read_bytes()).hexdigest(),
            "cases":[],"attacks":[]}
    (ROOT/"first-attempt.txt").write_text(
        "First independent reviewer GitHub Actions browser attempt. "
        "All initial navigation/validation failures are retained here or in job logs.\n")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        result["chromium"] = browser.version
        try:
            for enabled in (True, False):
                for width in (1280, 375):
                    label=("js" if enabled else "nojs")+"-"+str(width)
                    context=browser.new_context(
                        viewport={"width":width,"height":900},
                        java_script_enabled=enabled,device_scale_factor=1)
                    page=context.new_page()
                    requests=[]; errors=[]
                    page.on("request", lambda req: requests.append(req.url)
                            if req.url.startswith(("http:","https:")) else None)
                    page.on("pageerror", lambda e:errors.append(str(e)))
                    try:
                        page.goto(html_file.resolve().as_uri(),wait_until="load",timeout=45000)
                        proof=verify_render(page,m,label,result)
                        demand(not requests and not errors,"network/JS errors "+str((requests,errors)))
                        screenshot=ROOT/(label+"-full.png")
                        page.screenshot(path=str(screenshot),full_page=True)
                        result["cases"].append({
                            "label":label,"verifiedSelectors":proof["observed"],
                            "tableBothSides":proof["tableBothSides"],
                            "externalRequests":requests,"pageErrors":errors,
                            "screenshot":screenshot.name,
                            "screenshotSha256":hashlib.sha256(screenshot.read_bytes()).hexdigest()})
                        print("REAL CHROMIUM PASS",label,"values",proof["observed"],flush=True)
                    except Exception as ex:
                        with (ROOT/"first-attempt.txt").open("a") as f:
                            f.write(label+" ERROR "+repr(ex)+"\n")
                        page.screenshot(path=str(ROOT/(label+"-failed.png")),full_page=True)
                        raise
                    finally:
                        context.close()
            # Every forged case is visited in genuine JS-DISABLED Chromium.
            for name, modified in forge_cases(html).items():
                attack_path=ROOT/(name+".html")
                attack_path.write_text(modified)
                context=browser.new_context(
                    viewport={"width":1280,"height":900},
                    java_script_enabled=False)
                page=context.new_page()
                try:
                    page.goto(attack_path.resolve().as_uri(),wait_until="load",timeout=45000)
                    try:
                        verify_render(page,m,"attack-"+name,result)
                    except AssertionError as ex:
                        outcome={"name":name,"rejected":True,"why":str(ex)[:700]}
                        page.screenshot(path=str(ROOT/(name+"-rejected.png")),full_page=True)
                        result["attacks"].append(outcome)
                        print("RENDERED HOSTILE REFUSED",name,repr(str(ex)[:160]),flush=True)
                    else:
                        result["attacks"].append({"name":name,"rejected":False})
                        raise AssertionError("browser accepted visible falsification: "+name)
                finally:
                    context.close()
        finally:
            browser.close()
            (ROOT/"independent-browser-evidence.json").write_text(
                json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False)+"\n")
    demand(len(result["cases"])==4 and len(result["attacks"])==7
           and all(a["rejected"] for a in result["attacks"]),
           "missing independent browser cases/attack refusals")
    print("INDEPENDENT REVIEWER BROWSER PASS 4 modes, 7 rendered attacks",flush=True)

if __name__=="__main__":
    main()
