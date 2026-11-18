"""Fresh Chat B M36e p26 review probes; independently authored, source pinned by workflow.
Reads a *fresh* native source export, uses real offline Chromium, tests a set of
novel forgeries against the source browser verifier and separate SI invariants.
No source repo modifications or physics replacement.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from html import escape
import io
import json
from math import isclose, hypot, pi, sqrt
from pathlib import Path
import re
import tempfile

from playwright.sync_api import sync_playwright

EPS0 = 8.8541878128e-12
K = 1 / (4 * pi * EPS0)
PIN = "75ef212d79dc26ff97621fb1f2ed4e287bbed56d"
TREE = "f5be8433b39cf8827c19da1cd0586869347a33f4"
SPECS = (
    (0.10, +1e-9, (0.0, 0.0, 0.0), "FixedNetCharge"),
    (0.12, -2e-9, (0.025, 0.0, 0.0), "FixedNetCharge"),
    (0.08, 0.0, (0.0, 0.0, 0.0), "Grounded"),
)


def demand(ok, message):
    if not ok:
        raise AssertionError(message)


def close(actual, expected, name, rel=1e-8, abs_=2e-10):
    demand(actual is not None and isclose(float(actual), expected, rel_tol=rel, abs_tol=abs_),
           f"{name}: observed={actual!r} expected={expected!r}")


def physics(manifest, bundle=None):
    demand(len(manifest["native_states"]) == 3, "wrong native state count")
    demand(manifest["original_source_apparatus_count"] == 1, "invented original apparatus")
    demand(manifest["teacher_hypothetical_worlds"] == 2, "invented teacher cases")
    demand(manifest["physical_time_evolution"] is False, "fake physical time")
    result = []
    for idx, (r, q, centre, constraint) in enumerate(SPECS):
        s = manifest["native_states"][idx]
        geom = s["physical_geometry"]
        samples = s["native_samples"]
        actual = s["observed_conductor_results"][0]
        close(geom["radius_m"], r, f"state {idx} R", abs_=1e-14)
        close(geom["inner_radius_m"], 0, f"state {idx} inner radius")
        demand(s["physical_source_id"] == "Sphere A", "identity changed")
        demand(s["constraint_type"] == constraint, "authored charge constraint changed")
        demand(s["source_time_axis"] is False, "static world falsely dynamic")
        for j in range(3):
            close(geom["center_m"][j], centre[j], f"centre {idx}/{j}", abs_=1e-12)
        close(actual["net_charge_c"], q, f"charge {idx}", rel=1e-11, abs_=1e-20)
        close(actual["inner_surface_charge_c"], 0, f"inner bookkeeping {idx}", abs_=1e-20)
        close(actual["outer_surface_charge_c"], q, f"outer charge {idx}", abs_=1e-20)
        v_inside = K * q / r
        v_outside = K * q / (1.5 * r)
        sigma = q / (4 * pi * r * r)
        close(samples["half_radius_potential_v"], v_inside, f"V half {idx}", rel=3e-11)
        close(samples["three_half_radius_potential_v"], v_outside, f"V 3half {idx}", rel=3e-11)
        close(samples["outer_sigma_c_m2"], sigma, f"sigma {idx}", rel=3e-11, abs_=1e-20)
        close(sum(v*v for v in samples["metal_half_radius_e_v_m"]), 0, f"E inside {idx}")
        close(samples["external_pos_x_e_v_m"][0], K*q/(1.5*r)**2,
              f"E outside signed {idx}", rel=3e-11)
        close(samples["external_neg_x_e_v_m"][0], -K*q/(2*r)**2,
              f"E negative-x signed {idx}", rel=3e-11)
        result.append({"index": idx, "V_R2": v_inside,
                       "V_3R2": v_outside, "sigma_outer": sigma,
                       "E_3R2_x": K*q/(1.5*r)**2})
    if bundle is not None:
        demand(len(bundle["frames"]) == 3, "embedded source frames missing")
        for idx, (r, q, centre, constraint) in enumerate(SPECS):
            frame = bundle["frames"][idx]
            grid = frame["grid"]
            demand(len(grid["x_m"]) == len(grid["y_m"]) == 65,
                   "source physical sample resolution wrong")
            demand(len(frame["geometry"]) == 1 and frame["geometry"][0]["inner_radius_m"] == 0,
                   "embedded shape not true solid")
            demand(frame["geometry"][0]["name"] == "Sphere A", "wrong embedded sphere")
            demand(len(frame["profiles"]) == 1 and
                   frame["profiles"][0]["surface"] == "outer",
                   "missing/extra physical sigma surface")
            demand(not frame["source_masks"], "invented point sources")
            for ix, iy in ((2, 2), (2, 62), (62, 2), (62, 62), (32, 57), (39, 39)):
                x, z = grid["x_m"][ix], grid["y_m"][iy]
                distance = hypot(x-centre[0], z-centre[2])
                expected = K*q/max(distance, r)
                close(grid["potential_v"][iy][ix], expected,
                      f"independent embedded Gauss grid state={idx} xy={ix},{iy}",
                      rel=3e-10, abs_=1e-8)
    return result


def replace_once(text, old, new):
    n = text.count(old)
    demand(n == 1, f"mutation anchor must be unique, got {n}: {old[:90]!r}")
    return text.replace(old, new, 1)


def patch_state(html, index, change):
    pat = re.compile(r'<section data-m36e-state="' + str(index) +
                     r'"[^>]*>.*?</section>', re.S)
    match = pat.search(html)
    demand(match is not None, f"no state {index} section to mutate")
    new = change(match.group(0))
    demand(new != match.group(0), "mutation did not change state")
    return html[:match.start()] + new + html[match.end():]


def alter_readout(section, key, new_visible=None, new_native=None):
    rx = re.compile(r'(<strong data-m36e-number="' + re.escape(key) +
                    r'" data-native-value=")([^"]+)(">)([^<]+)(</strong>)')
    m = rx.search(section)
    demand(m is not None, "missing readout "+key)
    number = m.group(2) if new_native is None else str(new_native)
    visible = m.group(4) if new_visible is None else new_visible
    return section[:m.start()] + m.group(1) + number + m.group(3) + visible + m.group(5) + section[m.end():]


def get_bundle(html):
    m = re.search(r'(<script id="simulation-data" type="application/json">)(.*?)(</script>)',
                  html, re.S)
    demand(m is not None, "no real embedded source grid")
    return json.loads(m.group(2))


def set_bundle(html, bundle):
    return re.sub(r'(<script id="simulation-data" type="application/json">)(.*?)(</script>)',
                  lambda m: m.group(1) + json.dumps(bundle, separators=(",", ":")) + m.group(3),
                  html, count=1, flags=re.S)


def no_js_visible(html, viewer, folder):
    with tempfile.TemporaryDirectory(prefix="m36e-chat-b-nojs-") as tmp:
        filepath = Path(tmp)/viewer
        filepath.write_text(html, encoding="utf-8")
        with sync_playwright() as p:
            b = p.chromium.launch(headless=True)
            try:
                page = b.new_page(java_script_enabled=False)
                page.goto(filepath.resolve().as_uri())
                visible = [i for i in range(3)
                           if page.locator(f'[data-m36e-state="{i}"]').is_visible()]
                page.close()
                return visible
            finally:
                b.close()


def target_browser_gate(html, manifest, viewer):
    # The actual implementation's Chromium verifier is the target under attack,
    # not the independent checker used above.
    from tools.check_m36d_solid_browser import check
    with tempfile.TemporaryDirectory(prefix="m36e-chat-b-adversary-") as temp:
        folder = Path(temp)
        (folder/viewer).write_text(html, encoding="utf-8")
        (folder/"native-solid-sphere.json").write_text(
            json.dumps(manifest, allow_nan=False), encoding="utf-8")
        try:
            check(folder)
        except AssertionError as exc:
            return {"target": "REJECTED", "reason": str(exc)}
        except Exception as exc:
            return {"target": "ERROR", "reason": type(exc).__name__+": "+str(exc)}
        return {"target": "ACCEPTED", "reason": "source Chromium gate did not flag tamper"}


def save_thumbnail(src, dest):
    from PIL import Image
    with Image.open(src) as image:
        image = image.convert("RGB")
        if image.width > 1000:
            image.thumbnail((1000, 5000))
        dest.parent.mkdir(parents=True, exist_ok=True)
        image.save(dest, "JPEG", quality=72, optimize=True)


def physical_pdf_page(source_root, output):
    # Actual page rendering for possible later human visual inspection.
    import fitz
    pdf = source_root/"POTENTIAL_CONDUCTORS1.pdf"
    with fitz.open(pdf) as doc:
        demand(len(doc) >= 26, "original PDF has no physical page 26")
        page = doc[25]
        text = page.get_text()
        pix = page.get_pixmap(matrix=fitz.Matrix(1.0, 1.0), alpha=False)
        from PIL import Image
        with Image.open(io.BytesIO(pix.tobytes("png"))) as im:
            im.thumbnail((1000, 1500))
            im.convert("RGB").save(output/"reviewer-thumbs"/"original-pdf-page26.jpg",
                                   "JPEG", quality=72, optimize=True)
        (output/"p26-extracted-text.txt").write_text(text[:10000], encoding="utf-8")
        return {"page": 26, "total_physical_pages": len(doc),
                "extracted_characters": len(text),
                "illustration_1_text_found": "Illustration 1" in text}


def browser_positive(html_file, manifest, output):
    metrics = {"three_states": [], "js_errors": [], "http_requests": []}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 820})
            page.on("pageerror", lambda e: metrics["js_errors"].append(str(e)))
            page.on("request", lambda r: metrics["http_requests"].append(r.url)
                    if r.url.startswith(("https://", "http://")) else None)
            page.goto(html_file.resolve().as_uri(), wait_until="load", timeout=45000)
            demand(page.evaluate("window.conductorViewer?.mode") == "static",
                   "viewer incorrectly implies time")
            demand(page.evaluate("window.conductorViewer?.frameCount") == 3,
                   "expected three native static worlds")
            demand(page.locator("#density-panel h2").inner_text() ==
                   "Surface-charge density (one real outer face)",
                   "false induced sigma heading")
            bundle = page.evaluate(
                'JSON.parse(document.getElementById("simulation-data").textContent)')
            physics(manifest, bundle)
            for idx in range(3):
                page.locator("#frame").evaluate(
                    "(el,i)=>{el.value=String(i);el.dispatchEvent(new Event('input',{bubbles:true}));}",
                    idx)
                active = page.locator(f'[data-m36e-state="{idx}"]')
                visible = [j for j in range(3)
                           if page.locator(f'[data-m36e-state="{j}"]').is_visible()]
                demand(visible == [idx], f"slider state {idx} shows panels {visible}")
                q = SPECS[idx][1]; r = SPECS[idx][0]
                expected = {
                    "V_half_R": (K*q/r, "V"),
                    "V_three_half_R": (K*q/(1.5*r), "V"),
                    "E_inside": (0.0, "V/m"),
                    "sigma_outer": (q/(4*pi*r*r), "C/m²"),
                }
                row = {}
                for key, (calc, unit) in expected.items():
                    label = active.locator(f'[data-m36e-number="{key}"]')
                    demand(label.count() == 1, f"missing/duplicate {key} in state {idx}")
                    raw = float(label.get_attribute("data-native-value"))
                    shown = label.inner_text()
                    demand(shown.endswith(" "+unit), f"wrong unit {idx}/{key}: {shown!r}")
                    numeric = float(shown.split()[0])
                    close(raw, calc, f"browser-native {idx}/{key}", rel=3e-10, abs_=1e-11)
                    close(numeric, calc, f"browser-visible {idx}/{key}", rel=5e-9, abs_=1e-10)
                    row[key] = numeric
                label = page.locator("#case").inner_text()
                demand(("PRINTED p26 SOLID sphere" in label) if idx==0 else
                       ("TEACHER HYPOTHETICAL" in label),
                       f"source/teacher case lost {idx}")
                screenshot = output/f"state-{idx}.png"
                page.screenshot(path=str(screenshot), full_page=True, animations="disabled")
                save_thumbnail(screenshot,
                               output/"reviewer-thumbs"/f"state-{idx}.jpg")
                if idx == 0:
                    canvas = output/"scene-0.png"
                    page.locator("canvas#scene").screenshot(path=str(canvas))
                    save_thumbnail(canvas, output/"reviewer-thumbs"/"scene-0.jpg")
                metrics["three_states"].append({"state": idx, "visible": visible,
                                                "shown": row, "case": label})
            nojs = browser.new_page(java_script_enabled=False)
            nojs.goto(html_file.resolve().as_uri(), wait_until="load")
            metrics["no_js_visible"] = [j for j in range(3)
                                       if nojs.locator(f'[data-m36e-state="{j}"]').is_visible()]
            nojs.close()
            demand(metrics["no_js_visible"] == [0], "positive original no-JS fallback failed")
            demand(not metrics["js_errors"], "positive Chromium JS error")
            demand(not metrics["http_requests"], "positive Chromium made external requests")
            page.close()
        finally:
            browser.close()
    return metrics


def injection_probe(manifest, output):
    from tools.m36d_true_solid_sphere import _source_answer_panel
    payload = '"><img id="forged-image" src=x onerror="window.__m36e_attack=true"><script>window.__m36e_attack=true</script>'
    poisoned = deepcopy(manifest["native_states"][:1])
    poisoned[0]["case_role"] = payload
    fragment = _source_answer_panel(poisoned)
    demand('<img id="forged-image"' not in fragment, "unsafe role HTML escaped incorrectly")
    injection = output/"injection-safe.html"
    injection.write_text("<!doctype html><html><body>" + fragment + "</body></html>",
                         encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        try:
            page = b.new_page()
            page.goto(injection.resolve().as_uri())
            result = {"escaped_role_attribute":
                      page.locator('[data-m36e-state="0"]').get_attribute("data-m36e-role") == payload,
                      "executed": bool(page.evaluate("window.__m36e_attack===true")),
                      "injected_image_count": page.locator("#forged-image").count()}
            demand(result["escaped_role_attribute"] and not result["executed"] and
                   result["injected_image_count"] == 0,
                   "source role metadata can inject HTML/JS")
            page.close()
            return result
        finally:
            b.close()


def run_attacks(original_html, manifest):
    viewer = manifest["viewer_file"]
    attacks = []
    def add(name, html, data=None, check_nojs=False, check_science=False):
        native = manifest if data is None else data
        actual = target_browser_gate(html, native, viewer)
        if check_nojs:
            actual["no_js_visible"] = no_js_visible(html, viewer, None)
        if check_science:
            try:
                physics(native, get_bundle(html))
            except AssertionError as exc:
                actual["independent_science"] = "REJECTED: " + str(exc)
            else:
                actual["independent_science"] = "ACCEPTED"
        attacks.append({"name": name, **actual})

    # Distinct from author's original state-0 visible/attribute mutation:
    # attack negative teacher output, signs, and scientific metadata semantics.
    add("A1: negative teacher V(3R/2) display tampered",
        patch_state(original_html, 1, lambda s: alter_readout(s, "V_three_half_R",
                                                            new_visible="9999 V")))
    add("A2: negative teacher sigma visible sign inverted",
        patch_state(original_html, 1, lambda s: alter_readout(s, "sigma_outer",
                                                            new_visible="1.1052426604e-08 C/m²")))
    add("A3: actual negative charge labeled positive while native fields stay negative",
        replace_once(original_html, "Isolated net Q=-2 nC (authored teacher value)",
                     "Isolated net Q=+2 nC (authored teacher value)"))
    add("A4: grounded teacher claims nonzero solved Q",
        replace_once(original_html, "Grounded · actual solved Q=0 C in empty space",
                     "Grounded · actual solved Q=7 nC in empty space"))
    add("A5: teacher radius in visible caption falsified only",
        replace_once(original_html, "R=0.12 m; ", "R=1.2 m; "))
    add("A6: symbolic source claims specified numerical R/Q while other disclaimers remain",
        replace_once(original_html, "The printed source supplies SYMBOLIC R and Q.",
                     "The printed source supplies SYMBOLIC R and Q, exactly R=0.10m and Q=+1nC."))
    add("A7: no-JS teacher panel made visible; JS hides it on normal load",
        replace_once(original_html,
                     'data-m36e-role="teacher_changed_radius_charge_and_centre" hidden>',
                     'data-m36e-role="teacher_changed_radius_charge_and_centre">'),
        check_nojs=True)
    add("A8: negative teacher numeric HTML attribute forged",
        patch_state(original_html, 1, lambda s: alter_readout(s, "V_half_R",
                                                            new_native="10000")))
    # Lockstep artifact forgery: browser manifest and rendered readout both lie.
    both = deepcopy(manifest)
    old = both["native_states"][0]["native_samples"]["half_radius_potential_v"]
    bogus = old + 17
    both["native_states"][0]["native_samples"]["half_radius_potential_v"] = bogus
    html = patch_state(original_html, 0, lambda s: alter_readout(
        s, "V_half_R", new_native=format(bogus, ".17g"),
        new_visible=format(bogus, ".11g") + " V"))
    add("A9: fake native manifest and matching visible value in lockstep",
        html, both, check_science=True)
    # Embedded 65x65 physical grid lies but the answer card/manifest remains true.
    bundle = get_bundle(original_html)
    bundle["frames"][0]["grid"]["potential_v"][2][2] = 1000000.0
    add("A10: embedded source-sampled potential grid forged to 1e6 V",
        set_bundle(original_html, bundle), check_science=True)
    return attacks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--source-dir", type=Path, required=True)
    args = parser.parse_args()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    native = json.loads((output/"native-solid-sphere.json").read_text(encoding="utf-8"))
    html_file = output/native["viewer_file"]
    html = html_file.read_text(encoding="utf-8")
    first = {
        "reviewer": "Chat B independent first authored probes",
        "pin": PIN, "tree": TREE, "status": "FIRST ATTEMPT",
        "physics": physics(native, get_bundle(html)),
        "pdf_p26": physical_pdf_page(args.source_dir.resolve(), output),
        "positive_browser": browser_positive(html_file, native, output),
        "role_html_injection": injection_probe(native, output),
    }
    # Retain first attempts and exact reasons without rerunning negatives to obtain green.
    first["negative_probes"] = run_attacks(html, native)
    (output/"chat-b-first-attempt-results.json").write_text(
        json.dumps(first, indent=2, ensure_ascii=False, allow_nan=False)+"\n",
        encoding="utf-8")
    for a in first["negative_probes"]:
        print(a["name"], "=>", a["target"], a["reason"][:180],
              a.get("independent_science", ""), flush=True)
    print("Independent source, physical, real Chromium, static/no-JS and injection probes done.")
    print("FIRST ATTEMPT JSON:", output/"chat-b-first-attempt-results.json")


if __name__ == "__main__":
    main()
