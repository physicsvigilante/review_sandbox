"""Chat B independent Chromium look at actual M36b-generated offline HTML.

Not the production browser checker. Cross-check independent native manifest
semantics with visible text and graphics, capture all seven screenshots, and
emit a few screenshots for reviewer pixel inspection via job logs.
"""
from __future__ import annotations
import argparse
import base64
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

LABELS = {
    "p02-single-19": ("sheet-stop","Physical t"),
    "p03-single-30": ("plate-transit","Physical t"),
    "p05-single-47": ("dipole energy Q47",),
    "p12-linked-40": ("Ring A","Ring B","Upward"),
    "p15-archive-02": ("2012 proton",),
    "p02-single-15": ("far-separated connected spheres",),
    "jee2021-p1-q09-q10-equipotential": ("2021 Q9",),
}
DYNAMIC = {
    "p02-single-19":"actual_elapsed_time_trajectory_and_event",
    "p03-single-30":"actual_elapsed_time_trajectory_and_event",
    "p15-archive-02":"actual_elapsed_time_trajectory",
}
STATIC = {
    "p05-single-47":"static_orientation_observations_not_time_evolution",
    "p12-linked-40":"static_endpoint_work_not_time_evolution",
    "p02-single-15":"approximate_static_before_and_after_equilibria",
    "jee2021-p1-q09-q10-equipotential":"sampled_static_two_charge_zero_potential_contour",
}
EXPORT_PIXELS = {"jee2021-p1-q09-q10-equipotential"}  # Sheet/ring reviewed in retained previous attempt

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--native-dir",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    manifest=json.loads((args.native_dir/"native-replays.json").read_text(encoding="utf-8"))
    entries=manifest["source_apparatus"]
    assert set(entries)==set(LABELS)
    assert manifest["source_apparatus_count"]==7
    assert manifest["explicit_refusal"]["native"] is False
    assert manifest["explicit_refusal"]["viewer_file"] is None
    args.out.mkdir(parents=True,exist_ok=True)
    evidence={}
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        try:
            for case_id,expected in LABELS.items():
                row=entries[case_id]
                if case_id in DYNAMIC:
                    assert row["kind"]==DYNAMIC[case_id]
                else:
                    assert row["kind"]==STATIC[case_id]
                assert row["native"] is True
                html=args.native_dir/row["viewer_file"]
                assert html.is_file(),case_id
                page=browser.new_page(viewport={"width":1280,"height":800},device_scale_factor=1)
                external=[]
                page.on("request",lambda req:external.append(req.url) if req.url.startswith(("http://","https://")) else None)
                try:
                    page.goto(html.resolve().as_uri(),wait_until="load",timeout=45000)
                    body=page.locator("body").inner_text(timeout=15000)
                    assert len(body.strip())>100,case_id
                    assert page.locator("svg, canvas").count()>=1,case_id
                    assert not external,(case_id,external)
                    for phrase in expected:
                        assert phrase.casefold() in body.casefold(),(case_id,phrase)
                    file=args.out/(case_id+".png")
                    screenshot=page.screenshot(path=str(file),full_page=False,animations="disabled")
                    assert len(screenshot)>1000
                    evidence[case_id]={
                        "native_kind":row["kind"],
                        "evidence_class":"actual elapsed time" if case_id in DYNAMIC else "static observation only",
                        "rendered_text_length":len(body),
                        "svg_or_canvas_count":page.locator("svg, canvas").count(),
                        "required_visible_labels":list(expected),
                        "browser_http_requests":external,
                        "screenshot_file":file.name,
                        "pixel_bytes":len(screenshot),
                        "body_excerpt":body[:1600],
                    }
                    print("REVIEW02_BROWSER",case_id,json.dumps(evidence[case_id],sort_keys=True),flush=True)
                    # Permit separate-context visual inspection, not a claim of
                    # independent screenshot hashing or human learning research.
                    if case_id in EXPORT_PIXELS:
                        # Short JPEG chunks avoid GitHub log pipe nonblocking
                        # failure on a >140kB single-line PNG/base64 write.
                        photo=page.screenshot(type="jpeg",quality=60,full_page=False,animations="disabled")
                        b64=base64.b64encode(photo).decode("ascii")
                        print("REVIEW02_JPEG_BEGIN",case_id,len(b64),flush=True)
                        for k in range(0,len(b64),512):
                            print("REVIEW02_JPEG_PART",case_id,k//512,b64[k:k+512],flush=True)
                        print("REVIEW02_JPEG_END",case_id,flush=True)
                finally:
                    page.close()
        finally:
            browser.close()
    result=dict(kind="reviewer-authored independently executed Chromium inspection",
                source_apparatus=7,dynamic_count=len(DYNAMIC),static_count=len(STATIC),
                refused_p70_rendered=False,cases=evidence)
    (args.out/"independent-browser-review.json").write_text(json.dumps(result,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    print("REVIEW02_BROWSER_TOTAL 7 PASS; static=4 dynamic=3; zero HTTP requests",flush=True)

if __name__=="__main__":
    main()
