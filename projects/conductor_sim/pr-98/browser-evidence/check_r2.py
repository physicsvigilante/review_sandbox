"""Supplemental independent-*environment* Chromium evidence for M39b PR98.

Author-side verification harness, NOT an independent review verdict.
The six-cavity inputs come from the reviewer's exact PR20 reproducer, not
the production three-cavity example. A future reviewer must evaluate the
actual screenshots, computed DOM/CSS, hostile cases and FIRST attempt logs.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction
import hashlib
import json
from math import isfinite, ulp
from pathlib import Path
import re

from playwright.sync_api import sync_playwright

PRODUCTION_SHA = "965da98b5079829bd39a370cc660c97b1b9b189f"
PRODUCTION_TREE = "cb9f9822252f982d5691493b7d54b0fae5917049"
REVIEWER_SHA = "77a8013480e8be667ea34eea3d932bf0c07f2321"
WARNING = "TOPOLOGY ONLY — NOT TO SCALE — CARD ORDER IS NOT PHYSICAL POSITION"
PROVENANCE = ("Teacher-authored source membership. No physical shape, coordinates or "
              "geometric charge containment was verified.")
REFUSAL = ("Whole-face Gauss-law totals ONLY. No local E(x), V(x), sigma(x), "
           "forces, ground-wire current or real 3D field map.")
CAVITIES = (
    ("Alpha_Mixed", (("A_positive",4e-9),("A_negative",-1e-9))),
    ("Beta_TrulyEmpty", ()),
    ("Gamma_NetZero", (("C_plus",2.5e-9),("C_minus",-2.5e-9))),
    ("Delta_MixedNegative", (("D_minus",-7e-9),("D_plus",0.5e-9))),
    ("Epsilon_Single", (("E_solo",1.25e-9),)),
    ("Zeta_LongLabel", (("Zeta_signed_teacher_source_with_stable_ID_2026_11_19",4.25e-9),
                        ("Zeta_subtract",-0.75e-9))),
)


def demand(condition, message):
    if not condition:
        raise AssertionError(message)


def signed(value, unit):
    demand(type(value) in (int, float) and isfinite(value), "nonfinite/Boolean SI")
    if value == 0:
        return "0 " + unit
    return ("+" if value > 0 else "−") + repr(abs(float(value))) + " " + unit


def math_admissibility(doc):
    demand(doc["metal_id"] == "ReviewerMetal_R6", "wrong reviewer-authored metal")
    demand(doc["source_role"] == "teacher_hypothetical_topology_gauss_only",
           "unsupported original-JEE role")
    demand(type(doc["original_workbook_items_newly_solved"]) is int
           and doc["original_workbook_items_newly_solved"] == 0, "fabricated source coverage")
    demand(doc["warning"] == WARNING and doc["unsupported"] == REFUSAL, "physics warning changed")
    demand(doc["geometry_verified"] is False and doc["diagram_is_spatial_geometry"] is False
           and doc["time_evolution_defined"] is False, "geometry/time falsely certified")
    demand(len(doc["cavities"]) == 6, "six-cavity inventory missing")
    exact_sum = Fraction()
    n = 0
    for idx, (cid, contents) in enumerate(CAVITIES):
        row = doc["cavities"][idx]
        demand(row["cavity_id"] == cid, "cavity ID mismatch")
        got = [(s["source_id"], s["charge_c"]) for s in row["authored_sources"]]
        demand(got == list(contents), "source membership/ID/charge mismatch")
        q = sum((Fraction.from_float(qv) for _, qv in contents), Fraction())
        exact_sum += q
        for key, target in (("source_charge_sum_c", q),
                            ("induced_inner_face_total_charge_c", -q)):
            value = row[key]
            demand(type(value) in (int, float) and (value == 0) == (target == 0),
                   "true zero vs signed nonzero lost: " + cid)
            if target:
                expected = float(target)
                demand((value > 0) == (target > 0)
                       and abs(value-expected) <= 4*ulp(expected),
                       "wrong signed Gauss face: " + cid + " " + key)
        n += len(contents)
    demand(n == 9, "nine named sources missing")
    a, b = doc["states"]["isolated"], doc["states"]["grounded"]
    demand(a["conductor"]["constraint"] == "isolated_fixed_net_charge", "fake isolated")
    demand(b["conductor"]["constraint"] == "grounded_zero_potential", "fake grounded")
    demand(a["conductor"]["authored_isolated_metal_charge_c"] == -2.25e-9,
           "changed authored isolated metal charge")
    demand(b["outer_face_total_charge_c"] == 0.0 and b["exterior_electric_flux_v_m"] == 0.0,
           "grounded theorem outputs not exactly zero")
    demand(abs(a["total_interior_source_charge_c"]-float(exact_sum))
           <= 4*ulp(float(exact_sum)), "independent global sum wrong")
    expect_outer = Fraction.from_float(-2.25e-9) + exact_sum
    expect_flux = expect_outer / Fraction.from_float(8.8541878128e-12)
    demand(abs(a["outer_face_total_charge_c"] - float(expect_outer))
           <= 4*ulp(float(expect_outer)), "independent isolated outer total wrong")
    demand(abs(a["exterior_electric_flux_v_m"]-float(expect_flux))
           <= 4*ulp(float(expect_flux)), "independent Gauss flux wrong")
    return {"cavities": 6, "sources": n, "independent_source_sum_c": float(exact_sum),
            "independent_outer_c": float(expect_outer),
            "independent_flux_v_m": float(expect_flux)}


def style_of(element):
    return element.evaluate("""el => {
       const r=el.getBoundingClientRect(),s=getComputedStyle(el);
       let opacity=1, cur=el;
       while(cur && cur.nodeType===1) {
          opacity *= Number(getComputedStyle(cur).opacity);
          cur=cur.parentElement;
       }
       return {display:s.display,visibility:s.visibility,opacity:opacity,
         color:s.color,clip:s.clipPath,transform:s.transform,
         fontSize:s.fontSize,textShadow:s.textShadow,
         stroke:s.webkitTextStrokeWidth,
         x:r.x,y:r.y,w:r.width,h:r.height,
         before:getComputedStyle(el,'::before').content,
         after:getComputedStyle(el,'::after').content};
    }""")


def test_text(page, selector, expected, evidence):
    loc = page.locator(selector)
    demand(loc.count() == 1, "missing or duplicate visible selector: " + selector)
    demand(loc.is_visible(), "hidden DOM element " + selector)
    loc.scroll_into_view_if_needed(timeout=4000)
    value = loc.inner_text().strip()
    demand(value == expected,
           "rendered text mismatch at " + selector + ": " + repr(value)
           + " expected " + repr(expected))
    st = style_of(loc)
    demand(st["visibility"] == "visible" and st["display"] != "none"
           and st["opacity"] > .98 and st["w"] > 0 and st["h"] > 0,
           "CSS hidden/zero opacity: " + selector)
    demand(st["clip"] in ("none", "") and st["transform"] in ("none", ""),
           "CSS clipping or transformation: " + selector)
    demand(st["textShadow"] in ("none", "")
           and st["stroke"] in ("0px", "0", ""),
           "CSS text-shadow/stroke concealment: " + selector)
    demand(st["fontSize"] != "0px" and not re.search(r"rgba?\([^)]*,\s*0(?:\.0+)?\)$",
           st["color"]), "CSS transparent/zero-sized glyphs: " + selector)
    demand(st["before"] in ("none", "normal", '""')
           and st["after"] in ("none", "normal", '""'),
           "CSS pseudo-element textual forgery: " + selector)
    demand(st["x"] > -5 and st["x"] < page.viewport_size["width"]+5,
           "offscreen visible identifier: " + selector)
    # A table cell may require deliberate horizontal scrolling on narrow view;
    # scroll_into_view_if_needed above should bring it into the scroll container.
    demand(st["y"] > -st["h"]-10 and st["y"] < page.viewport_size["height"]+10,
           "offscreen visible vertical text: " + selector)
    evidence[selector] = {"text": value, "css": st}


def validate_browser(page, doc):
    evidence = {}
    demand(page.locator("script,iframe,object,embed,svg,canvas,video,img,link[rel=stylesheet]").count() == 0,
           "introduced remote asset/JS/false field image")
    demand(page.locator("#fake-current,#fake-shape").count() == 0,
           "fabricated current or geometry in rendered DOM")
    body_pseudo = page.locator("body").evaluate(
        "el => [getComputedStyle(el,'::before').content,getComputedStyle(el,'::after').content]")
    demand(all(x in ("none", "normal", '""') for x in body_pseudo),
           "CSS body-level pseudo-element forgery")
    test_text(page,"#m39b-title","Gauss law · multiple sealed cavities",evidence)
    test_text(page,"#m39b-warning",WARNING,evidence)
    test_text(page,"#m39b-membership",PROVENANCE,evidence)
    test_text(page,"#m39b-refusal",REFUSAL,evidence)
    test_text(page,"#m39b-provenance",
              "TEACHER HYPOTHETICAL · NO VERIFIED ORIGINAL JEE ANSWER",evidence)
    test_text(page,"#m39b-metal","ReviewerMetal_R6",evidence)
    test_text(page,"#m39b-zero-warning",
              "A zero entire-face net charge does NOT imply zero local surface charge density throughout that face.",evidence)
    test_text(page,"#m39b-original-count",
              "Original JEE source problems newly solved: 0. Workbook p11 and irregular three-cavity notes p70 remain unsupported for local 3D field/density.",evidence)
    test_text(page,"#m39b-pair",
              "Same source IDs, charges, cavity membership and permittivity (" +
              signed(doc["permittivity_f_per_m"],"F/m") +
              "). No ground-wire current or transfer history is inferred.",evidence)
    demand(page.locator("#m39b-cavities>.cavity").count()==6, "wrong count of rendered cards")
    width=page.viewport_size["width"]
    for idx, (cid, contents) in enumerate(CAVITIES):
        row=doc["cavities"][idx]
        test_text(page, "#m39b-cavity-"+str(idx), cid, evidence)
        test_text(page, "#m39b-q-"+str(idx), signed(row["source_charge_sum_c"],"C"), evidence)
        test_text(page, "#m39b-inner-"+str(idx),
                  signed(row["induced_inner_face_total_charge_c"],"C"), evidence)
        tag=page.locator("#m39b-card-"+str(idx)+" .tag")
        demand(tag.count()==1, "missing or duplicated empty/neutral label")
        want=("empty cavity" if not contents else
              "signed cancellation (local sigma unknown)" if row["source_charge_sum_c"]==0
              else "charged cavity")
        test_text(page, "#m39b-card-"+str(idx)+" .tag",want,evidence)
        for j,(sid,q) in enumerate(contents):
            source_sel="#m39b-source-"+str(idx)+"-"+str(j)
            test_text(page,source_sel+" code",sid,evidence)
            test_text(page,source_sel+" .charge",signed(q,"C"),evidence)
        if not contents:
            test_text(page,"#m39b-source-empty-"+str(idx),"No sources assigned",evidence)
        card=page.locator("#m39b-card-"+str(idx)).bounding_box()
        demand(card and card["x"]>=-2 and card["x"]+card["width"]<=width+2,
               "cavity frame clipped horizontally")
    for state in ("isolated","grounded"):
        st=doc["states"][state]
        for key,val,unit in (
          ("sources",st["total_interior_source_charge_c"],"C"),
          ("metal",st["conductor"]["equilibrium_net_metal_charge_c"],"C"),
          ("outer",st["outer_face_total_charge_c"],"C"),
          ("flux",st["exterior_electric_flux_v_m"],"V·m"),
        ):
            test_text(page,"#m39b-"+key+"-"+state,signed(val,unit),evidence)
    test_text(page,"#m39b-fixed-isolated",
              signed(doc["states"]["isolated"]["conductor"]["authored_isolated_metal_charge_c"],"C"),evidence)
    test_text(page,"#m39b-fixed-grounded","Not a fixed-charge input",evidence)
    test_text(page,"#m39b-theorem-isolated",
              "Not generally implied for isolated metal",evidence)
    test_text(page,"#m39b-theorem-grounded",
              "Yes, under declared no-exterior-source boundary",evidence)
    table=page.locator(".table-scroll")
    demand(table.count()==1 and table.is_visible(),"missing visible SI table")
    stat=table.evaluate("""el=>{
       const first=el.scrollLeft;
       el.scrollLeft=el.scrollWidth;
       const max=el.scrollLeft;
       el.scrollLeft=first;
       return {clientWidth:el.clientWidth,scrollWidth:el.scrollWidth,maxScroll:max}
    }""")
    if width<=460:
        demand(stat["scrollWidth"]>stat["clientWidth"] and stat["maxScroll"]>0,
               "mobile table cannot be horizontally scrolled")
    else:
        demand(stat["clientWidth"]>=500,"desktop table unexpectedly cramped")
    demand(page.locator("#m39b-summary").is_visible(),"summary table hidden")
    demand(page.evaluate("() => document.documentElement.scrollWidth <= window.innerWidth+3"),
           "page itself clips horizontal layout; only table may scroll")
    return {"verified":len(evidence),"textsAndComputedStyle":evidence,
            "tableOverflow":stat,"viewport":dict(page.viewport_size)}


def make_attacks(html):
    def swap_once(old,new,label):
        demand(html.count(old)==1, "authentic HTML lacks attack anchor "+label)
        return html.replace(old,new,1)
    def css(rule):
        demand(html.count("</style>")==1, "style injection anchor missing")
        return html.replace("</style>",rule+"</style>",1)
    def regex(pattern,replacement,label):
        modified,n=re.subn(pattern,replacement,html,count=1,flags=re.S)
        demand(n==1 and modified!=html,"regex attack anchor missing "+label)
        return modified
    return {
       "forged-face-sign":regex(r'(id="m39b-inner-0">)[^<]+',r'\g<1>+300 C',"face"),
       "forged-outer":regex(r'(id="m39b-outer-isolated" class="charge">)[^<]+',
                            r'\g<1>0 C',"outer"),
       "forged-flux-unit":regex(r'(id="m39b-flux-isolated" class="charge">)[^<]+',
                                r'\g<1>+12 C',"flux"),
       "falsified-provenance":swap_once("TEACHER HYPOTHETICAL · NO VERIFIED ORIGINAL JEE ANSWER",
                                        "ORIGINAL JEE VERIFIED SOLUTION","provenance"),
       "falsified-original-count":swap_once("Original JEE source problems newly solved: ",
                                            "Original JEE source problems newly solved: 7 ","original count"),
       "false-grounding":swap_once("Yes, under declared no-exterior-source boundary",
                                   "Yes, even with external sources","theorem"),
       "hidden-source":css("#m39b-source-0-0{display:none!important}"),
       "invisible-total":css("#m39b-q-0{opacity:0!important}"),
       "transparent-inner":css("#m39b-inner-0{color:transparent!important}"),
       "offscreen-source-role":css("#m39b-provenance{transform:translateX(-100000px)!important}"),
       "clipped-warning":css("#m39b-warning{clip-path:inset(100%)!important}"),
       "fake-pseudo-overlay":css('body::before{content:"ORIGINAL JEE VERIFIED";position:fixed;z-index:99999;inset:0;background:#fff}'),
       "mask-with-textstroke":css("#m39b-inner-0{-webkit-text-stroke:5px #fff!important}"),
       "minuscule-glyph":css("#m39b-inner-0{font-size:0!important}"),
       "external-stylesheet":swap_once("</head>","<link rel=\"stylesheet\" href=\"https://example.invalid/false.css\"></head>","link"),
       "fabricated-3d-picture":swap_once("</body>","<svg id=\"fake-shape\"><text x=\"0\" y=\"10\">3D E field</text></svg></body>","svg"),
       "fabricated-wire-current":swap_once("</body>","<p id=\"fake-current\">Ground wire current +7 A</p></body>","current"),
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",type=Path,required=True)
    ap.add_argument("--html",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    manifest=json.loads(args.manifest.read_text(encoding="utf-8"))
    scientific=math_admissibility(manifest)
    authentic=args.html.read_text(encoding="utf-8")
    demand(authentic.lstrip().lower().startswith("<!doctype html>"),"not an HTML document")
    (args.output/"authentic-six-cavity.html").write_text(authentic,encoding="utf-8")
    attacks=make_attacks(authentic)
    for name,forgery in attacks.items():
        (args.output/("hostile-"+name+".html")).write_text(forgery,encoding="utf-8")
    evidence={"production_head":PRODUCTION_SHA,"production_tree":PRODUCTION_TREE,
              "reviewer_head":REVIEWER_SHA,"manifest_sha256":hashlib.sha256(args.manifest.read_bytes()).hexdigest(),
              "html_sha256":hashlib.sha256(authentic.encode()).hexdigest(),
              "scientific":scientific,"cases":[],"attack_results":[]}
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True)
        evidence["chromium_version"]=browser.version
        try:
            for js_enabled in (True,False):
                for width,height in ((1280,900),(375,900)):
                    context=browser.new_context(
                        viewport={"width":width,"height":height},
                        java_script_enabled=js_enabled,device_scale_factor=1)
                    page=context.new_page()
                    outgoing, page_errors=[],[]
                    page.on("request", lambda req: outgoing.append(req.url)
                            if req.url.startswith(("http://","https://")) else None)
                    page.on("pageerror",lambda err:page_errors.append(str(err)))
                    page.goto(args.html.resolve().as_uri(),wait_until="load",timeout=45000)
                    case=validate_browser(page,manifest)
                    demand(not outgoing and not page_errors,
                           "offline page has network requests or JavaScript errors")
                    case["jsEnabled"]=js_enabled
                    case["networkRequests"]=outgoing
                    case["pageErrors"]=page_errors
                    suffix=("js" if js_enabled else "nojs")+"-"+str(width)
                    shot=args.output/(suffix+"-reviewer-six-cavity.png")
                    page.screenshot(path=str(shot),full_page=True)
                    case["screenshot"]=shot.name
                    case["screenshot_sha256"]=hashlib.sha256(shot.read_bytes()).hexdigest()
                    evidence["cases"].append(case)
                    page.close()
                    context.close()
            # Hostility is exercised against the actual rendered DOM and CSS,
            # NOT only against byte-different HTML. JS deliberately disabled.
            context=browser.new_context(viewport={"width":1280,"height":900},
                                        java_script_enabled=False)
            for name in attacks:
                page=context.new_page()
                malicious=(args.output/("hostile-"+name+".html")).resolve().as_uri()
                page.goto(malicious,wait_until="load",timeout=45000)
                try:
                    validate_browser(page,manifest)
                except (AssertionError,TimeoutError) as err:
                    record={"name":name,"rejected":True,"reason":str(err)[:500]}
                    if name in ("fake-pseudo-overlay","hidden-source","forged-face-sign"):
                        pic=args.output/("rejected-"+name+".png")
                        page.screenshot(path=str(pic),full_page=True)
                        record["screenshot"]=pic.name
                    evidence["attack_results"].append(record)
                else:
                    raise AssertionError("browser-visible attack was accepted: "+name)
                finally:
                    page.close()
            context.close()
        finally:
            browser.close()
    demand(len(evidence["cases"])==4,"not all four Chromium modes validated")
    demand(len(evidence["attack_results"])==len(attacks),"not all hostile HTML probes exercised")
    (args.output/"actual-browser-evidence.json").write_text(
        json.dumps(evidence,indent=2,ensure_ascii=False,allow_nan=False)+"\n",encoding="utf-8")
    print(json.dumps({"actual_browser_cases":4,"browser_visible_attack_refusals":len(attacks),
                      "scientific":scientific,"chromium":evidence["chromium_version"]},
                     sort_keys=True))


if __name__=="__main__":
    main()
