#!/usr/bin/env python3
"""Independent Chat B R2: actual pinned HTML/JSON Chromium and first-frame forgeries.

Reviewer-owned; never treats author hostile-loop status as independent proof.
Run from source-pinned production checkout with project installed, with the
review_sandbox copy of this script as the entrypoint.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path

from playwright.sync_api import sync_playwright
from tools.check_m37b_prescribed_browser import check as actual_production_browser_gate
from tools.m37b_source_reference import check as stdlib_si_oracle

ROOT = Path("review-outputs")
DATA = ROOT / "m37b-source"
HTML = DATA / "p8-ground-current.html"
JSON = DATA / "p8-ground-current.json"
SHOTS = ROOT / "independent-screenshots"

# Distinctly authored against literal pre-script HTML, not the production
# hostile-loop function or its mutation machinery.
ATTACKS = [
    ("marker-x", r'(<circle id="m37b-current-marker" cx=")[^"]+', "500",
     "#m37b-current-marker", "cx",
     "no-JS physical scene/graph coordinate #m37b-current-marker.cx"),
    ("marker-y", r'(<circle id="m37b-current-marker" cx="[^"]+" cy=")[^"]+', "230",
     "#m37b-current-marker", "cy",
     "no-JS physical scene/graph coordinate #m37b-current-marker.cy"),
    ("charge-x", r'(<circle id="m37b-charge" cx=")[^"]+', "690",
     "#m37b-charge", "cx",
     "no-JS physical scene/graph coordinate #m37b-charge.cx"),
    ("charge-sign-x", r'(<text id="m37b-q-sign" x=")[^"]+', "690",
     "#m37b-q-sign", "x",
     "no-JS physical scene/graph coordinate #m37b-q-sign.x"),
    ("initial-time", r'(<strong id="m37b-time">)[^<]+', "999 s",
     "#m37b-time", "text", "no-JS first physical SI label #m37b-time"),
    ("initial-distance", r'(<strong class="value" id="m37b-distance">)[^<]+', "333 m",
     "#m37b-distance", "text", "no-JS first physical SI label #m37b-distance"),
    ("opposite-current-sign", r'(<strong class="value" id="m37b-opposite">)[^<]+', "+9 A",
     "#m37b-opposite", "text", "no-JS first physical SI label #m37b-opposite"),
    ("source-sign-text", r'(<text id="m37b-q-sign"[^>]*>)[^<]+', "−q",
     "#m37b-q-sign", "text", "source says q positive but actual plotted charge sign differs"),
    ("sphere-radius", r'(<circle id="m37b-sphere"[^>]* r=")[^"]+', "7",
     "#m37b-sphere", "r", "visible drawn physical geometry #m37b-sphere.r"),
    ("slider-index", r'(<input id="m37b-index"[^>]* value=")[^"]+', "15",
     "#m37b-index", "input", "no-JS first physical time index/slider range"),
    # Novel beyond the author's original ten: orthogonal first-frame quantities.
    ("new-charge-y", r'(<circle id="m37b-charge" cx="[^"]+" cy=")[^"]+', "270",
     "#m37b-charge", "cy", "visible drawn physical geometry #m37b-charge.cy"),
    ("new-induced-Q", r'(<strong class="value" id="m37b-Q">)[^<]+', "+8e-9 C",
     "#m37b-Q", "text", "no-JS first physical SI label #m37b-Q"),
]

def sha(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()

def say(message: str) -> None:
    print(message, flush=True)

def embedded_json(html: str) -> str:
    matches = re.findall(
        r'<script id="m37b-data" type="application/json">(.*?)</script>',
        html, flags=re.S
    )
    assert len(matches) == 1, "Missing/unexpected static embedded JSON"
    return matches[0]

def phys_equal(actual: float, expected: float, field: str, tolerance: float = 2e-11) -> None:
    assert math.isclose(actual, expected, rel_tol=tolerance, abs_tol=2e-25), (
        field, actual, expected
    )

def independent_replay(manifest: dict) -> None:
    """Direct textbook image-charge formulas; unchanged source physics replay."""
    science = manifest["trace"]
    q = science["source_charge_c"]
    r = science["sphere_radius_m"]
    v = science["signed_constant_radial_speed_m_s"]
    d0 = science["samples"][0]["radial_distance_m"]
    samples = science["samples"]
    assert q > 0 and r > 0 and v < 0 and len(samples) == 31
    assert manifest["source"]["original_correct_option_indices"] == [1, 3]
    assert "TEACHER-CHOSEN" in manifest["source"]["numeric_attribution"]
    for idx, row in enumerate(samples):
        d, t = row["radial_distance_m"], row["time_s"]
        assert row["index"] == idx
        assert math.isclose(d, d0 + v*t, rel_tol=2e-12, abs_tol=2e-13)
        phys_equal(row["induced_sphere_net_charge_c"], -q*r/d, f"Q[{idx}]")
        phys_equal(row["wire_current_sphere_to_ground_a"], -q*r*v/(d*d), f"I[{idx}]")
        phys_equal(row["wire_current_ground_to_sphere_a"], q*r*v/(d*d), f"Iop[{idx}]")
    assert all(a["wire_current_sphere_to_ground_a"] < b["wire_current_sphere_to_ground_a"]
               for a,b in zip(samples, samples[1:]))
    si = stdlib_si_oracle(manifest)
    assert si["verified_python_kelvin_states"] == 31
    say("INDEPENDENT_KELVIN_FORMULA_REPLAY 31/31 PASS; standalone SI oracle PASS")

def check_original_in_real_chromium(manifest: dict) -> None:
    """Load actual HTML on disk; directly inspect JS enabled and JS disabled."""
    positions = manifest["readouts"]
    layout = manifest["layout"]
    first = positions[0]
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            for js_enabled in (True, False):
                context = browser.new_context(java_script_enabled=js_enabled,
                            viewport={"width":1210 if js_enabled else 940,
                                      "height":840})
                try:
                    page = context.new_page()
                    network, errors = [], []
                    page.on("request", lambda req: network.append(req.url)
                        if req.url.startswith(("http://","https://")) else None)
                    page.on("pageerror", lambda err: errors.append(str(err)))
                    page.goto(HTML.resolve().as_uri(), wait_until="load", timeout=45000)
                    assert page.locator("#m37b-source").is_visible()
                    assert page.locator("#m37b-teacher-attribution").is_visible()
                    assert "TEACHER-CHOSEN" in page.locator("#m37b-teacher-attribution").inner_text()
                    assert "(1) and (3)" in page.locator("#m37b-original-statement").inner_text()
                    assert page.locator("#m37b-time").inner_text().strip() == first["time_label"]
                    for selector,key in [
                        ("#m37b-distance","distance_label"),
                        ("#m37b-Q","induced_charge_label"),
                        ("#m37b-current","wire_current_label"),
                        ("#m37b-opposite","opposite_current_label"),
                    ]:
                        assert page.locator(selector).inner_text().strip() == first[key], selector
                    for selector,attr,truth in [
                        ("#m37b-sphere","cx",layout["sphere_cx_px"]),
                        ("#m37b-sphere","cy",layout["sphere_cy_px"]),
                        ("#m37b-sphere","r",layout["sphere_radius_px"]),
                        ("#m37b-charge","cx",first["charge_x_px"]),
                        ("#m37b-charge","cy",layout["charge_cy_px"]),
                        ("#m37b-q-sign","x",first["charge_x_px"]),
                        ("#m37b-current-marker","cx",first["chart_x_px"]),
                        ("#m37b-current-marker","cy",first["chart_y_px"]),
                    ]:
                        actual = float(page.locator(selector).get_attribute(attr))
                        assert math.isclose(actual, truth, rel_tol=2e-12, abs_tol=5e-9), (selector,attr)
                    assert page.locator("#m37b-q-sign").text_content().strip() == "+q"
                    static_points = page.locator("#m37b-current-line").get_attribute("points").split()
                    assert len(static_points) == len(positions) == 31
                    for row, point in zip(positions, static_points):
                        x,y = (float(z) for z in point.split(","))
                        assert math.isclose(x,row["chart_x_px"],rel_tol=3e-10,abs_tol=2e-7)
                        assert math.isclose(y,row["chart_y_px"],rel_tol=3e-10,abs_tol=2e-7)
                    slider = page.locator("#m37b-index")
                    assert slider.input_value() == "0" and slider.get_attribute("min") == "0"
                    assert slider.get_attribute("max") == "30"
                    if js_enabled:
                        assert not slider.is_disabled()
                        assert page.evaluate("window.m37bPrescribedViewer.sampleCount") == 31
                        slider.evaluate(
                            "(el)=>{el.value='30';el.dispatchEvent(new Event('input',{bubbles:true}));}"
                        )
                        assert page.locator("#m37b-time").inner_text().strip() == positions[30]["time_label"]
                        page.locator("#m37b-start").click()
                        assert slider.input_value() == "0"
                    else:
                        assert page.locator("#m37b-nojs").is_visible()
                        assert slider.is_disabled() and page.locator("#m37b-start").is_disabled()
                        assert page.locator("#m37b-play").is_disabled()
                    page.screenshot(path=str(SHOTS / ("genuine-js-on.png" if js_enabled
                                                     else "genuine-nojs-first.png")), full_page=True)
                    assert not network, ("unwanted external HTTP",network)
                    assert not errors, ("unexpected JS exception",errors)
                    say("INDEPENDENT_ACTUAL_CHROMIUM_ORIGINAL "
                        + ("JS-ON" if js_enabled else "NO-JS")
                        + " PASS first DOM, scene, 31 points, controls and provenance")
                finally:
                    context.close()
        finally:
            browser.close()

def nojs_observed_mutation(selector: str, attr: str, target: str, output_name: str) -> str:
    """Verify the hostile first-frame claim really appears in Chromium."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            context = browser.new_context(java_script_enabled=False,
                                          viewport={"width":940,"height":740})
            try:
                page = context.new_page()
                external, errors = [], []
                page.on("request", lambda req: external.append(req.url)
                        if req.url.startswith(("http://","https://")) else None)
                page.on("pageerror", lambda err: errors.append(str(err)))
                page.goto(HTML.resolve().as_uri(), wait_until="load", timeout=45000)
                locator = page.locator(selector)
                assert locator.is_visible() or attr == "input", f"{selector} was not visible"
                if attr == "text":
                    actual = locator.text_content().strip()
                elif attr == "input":
                    actual = locator.input_value()
                else:
                    actual = locator.get_attribute(attr)
                assert actual == target, ("mutant not rendered in real noJS Chromium",
                                          selector, actual, target)
                page.screenshot(path=str(SHOTS / (output_name+".png")),full_page=True)
                assert not external and not errors, (output_name,external,errors)
                return actual
            finally:
                context.close()
        finally:
            browser.close()

def main() -> None:
    ROOT.mkdir(parents=True,exist_ok=True)
    SHOTS.mkdir(parents=True,exist_ok=True)
    original_bytes = HTML.read_bytes()
    science_bytes = JSON.read_bytes()
    original = original_bytes.decode("utf-8")
    assert original.startswith("<!doctype html>")
    manifest = json.loads(science_bytes)
    original_embedded = embedded_json(original)
    assert json.loads(original_embedded) == manifest

    independent_replay(manifest)
    check_original_in_real_chromium(manifest)
    authentic = actual_production_browser_gate(DATA)
    assert authentic["no_javascript_original_state"] is True
    say("ACTUAL_PRODUCTION_BROWSER_GATE_UNALTERED PASS")

    outcomes = []
    try:
        for label,pattern,replacement,selector,attr,reason_fragment in ATTACKS:
            forged, count = re.subn(pattern, lambda m:m.group(1)+replacement,
                                    original, count=1)
            assert count == 1 and forged != original, ("invalid mutation",label)
            assert embedded_json(forged) == original_embedded, ("embedded JSON changed",label)
            HTML.write_text(forged,encoding="utf-8")
            assert JSON.read_bytes() == science_bytes, ("SI JSON changed",label)
            seen = nojs_observed_mutation(selector,attr,replacement,"hostile-"+label)
            try:
                actual_production_browser_gate(DATA)
            except AssertionError as error:
                reason = str(error)
                assert reason_fragment in reason, (
                    "wrong reason / setup error", label,reason,reason_fragment
                )
                outcomes.append({"case":label,"nojs_rendered":seen,
                                 "refused_by_actual_production_gate":True,
                                 "scientific_reason":reason})
                (ROOT/"independent-attack-results.json").write_text(
                    json.dumps(outcomes,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"
                )
                say("REFUSED_AS_EXPECTED "+label+" "+reason)
            else:
                raise AssertionError(
                    f"RELEASE BLOCKER: actual checker ACCEPTED false static HTML: {label}"
                )
        assert len(outcomes) == len(ATTACKS) == 12
    finally:
        HTML.write_bytes(original_bytes)
        assert HTML.read_bytes() == original_bytes, "original HTML not byte-restored"
        assert JSON.read_bytes() == science_bytes, "SI JSON bytes altered after hostiles"

    second = actual_production_browser_gate(DATA)
    assert second["no_javascript_original_state"] is True
    result = {
        "verdict_of_browser_experiment":"PASS",
        "source_head":"c8333b61dd5a147086842ab9162a3ed0ef495373",
        "native_tree":"44b754e005c3d720cb3e59c1debd363ca2d8d639",
        "original_html_sha256":sha(original_bytes),
        "original_science_json_sha256":sha(science_bytes),
        "physical_Kelvin_rows_replayed":31,
        "real_chromium_original_js_enabled_and_disabled":True,
        "actual_production_browser_original_pass_before_and_after":True,
        "independently_attacked_HTML_only":len(outcomes),
        "actual_prod_browser_rejected":len(outcomes),
        "original_bytes_restored":True,
        "science_bytes_unchanged":True,
        "outcomes":outcomes
    }
    (ROOT/"independent-review-result.json").write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"
    )
    say("INDEPENDENT_REAL_CHROMIUM_COMPLETE 12/12 refused, baseline PASS, bytes preserved")

if __name__ == "__main__":
    main()
