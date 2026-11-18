"""Independent Chat B R2-02: actual source-pinned p26 physics, Chromium and forged-evidence probes.

Reviewer-owned tests. Do not use developer hostile harness or the production
Gauss implementation to compute the independent SI expected values.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from hashlib import sha256
from math import isclose, hypot, pi
from pathlib import Path
import json
import re
import tempfile

from playwright.sync_api import sync_playwright

HEAD = "69d740c82b3b79877389da1433cef2bc9a25bdb1"
TREE = "60b4f21aa88a2031ec50c5d1e7c15a5135a7becf"
K = 1 / (4 * pi * 8.8541878128e-12)
WORLDS = (
    (.10, 1e-9, (0., 0., 0.)),
    (.12, -2e-9, (.025, 0., 0.)),
    (.08, 0., (0., 0., 0.)),
)
GRID_SCRIPT = re.compile(
    r'(<script id="simulation-data" type="application/json">)(.*?)(</script>)',
    re.S,
)


def require(test, description):
    if not test:
        raise AssertionError(description)


def close(got, expected, label, rel=1e-8, absolute=1e-10):
    require(isclose(float(got), expected, rel_tol=rel, abs_tol=absolute),
            f"{label}: observed={got!r} independent_SI={expected!r}")


def replace_unique(html, needle, replacement):
    require(html.count(needle) == 1, f"tamper fixture not unique: {needle[:95]!r}")
    return html.replace(needle, replacement, 1)


def read_bundle(html):
    found = GRID_SCRIPT.search(html)
    require(found is not None, "authentic embedded simulation JSON missing")
    return json.loads(found.group(2))


def change_grid(html, modify):
    found = GRID_SCRIPT.search(html)
    require(found is not None, "missing embedded field-grid JSON")
    data = json.loads(found.group(2))
    modify(data)
    encoded = json.dumps(data, separators=(",", ":"), allow_nan=False)
    return html[:found.start(2)] + encoded + html[found.end(2):]


def verify_true_native_and_grid(manifest, embedded):
    require(manifest["printed_source"]["page"] == 26, "wrong source page")
    require(manifest["original_source_apparatus_count"] == 1
            and manifest["teacher_hypothetical_worlds"] == 2,
            "false new-original-problem count")
    require(manifest["physical_time_evolution"] is False,
            "source static states incorrectly called dynamics")
    require(len(embedded["frames"]) == 3, "viewer lacks three static states")
    rows = []
    checked = 0
    for i, (radius, charge, center) in enumerate(WORLDS):
        state = manifest["native_states"][i]
        frame = embedded["frames"][i]
        geom = state["physical_geometry"]
        probes = state["native_samples"]
        require(state["physical_shape_type"] == "SolidSphere",
                f"state {i}: shape not a physical solid sphere")
        require(geom["inner_radius_m"] == 0 and geom["is_physically_solid"],
                f"state {i}: phantom hollow shell")
        require(state["physical_source_id"] == "Sphere A",
                f"state {i}: source conductor identity changed")
        require(len(frame["profiles"]) == 1 and
                frame["profiles"][0]["surface"] == "outer",
                f"state {i}: nonphysical inner charge face")
        require(frame["source_masks"] == [], f"state {i}: false point source")
        close(geom["radius_m"], radius, f"native radius state {i}")
        for j in range(3):
            close(geom["center_m"][j], center[j],
                  f"native center state {i}/{j}")
        observed_q = state["observed_conductor_results"][0]["net_charge_c"]
        close(observed_q, charge, f"native Q state {i}", absolute=1e-19)
        if i == 2:
            require(state["constraint_type"] == "Grounded"
                    and state["authored_charge_c"] is None,
                    "grounded teacher not source-free")
        else:
            close(state["authored_charge_c"], charge,
                  f"author Q state {i}", absolute=1e-19)
        expect_half = K * charge / radius
        expect_outer = (2 / 3) * expect_half
        expect_sigma = charge / (4 * pi * radius ** 2)
        expect_field = K * charge / ((1.5 * radius) ** 2)
        close(probes["half_radius_potential_v"], expect_half,
              f"V(R/2) state {i}")
        close(probes["three_half_radius_potential_v"], expect_outer,
              f"V(3R/2) state {i}")
        close(probes["outer_sigma_c_m2"], expect_sigma,
              f"one-face sigma state {i}")
        for component in probes["metal_half_radius_e_v_m"]:
            close(component, 0., f"inside E state {i}", absolute=1e-10)
        close(probes["external_pos_x_e_v_m"][0], expect_field,
              f"signed outside Ex state {i}")
        for component in probes["external_pos_x_e_v_m"][1:]:
            close(component, 0., f"outside transverse E state {i}")
        g = frame["grid"]
        plane = frame["plane"]
        require(len(g["x_m"]) == len(g["y_m"]) == 65,
                f"state {i}: actual sampled grid not 65x65")
        counts = {"metal": 0, "vacuum": 0, "surface": 0}
        for iy, y in enumerate(g["y_m"]):
            for ix, x in enumerate(g["x_m"]):
                world = [
                    plane["origin_m"][d] + x * plane["u"][d] + y * plane["v"][d]
                    for d in range(3)
                ]
                delta = [world[d] - center[d] for d in range(3)]
                length = hypot(*delta)
                expected_v = K * charge / max(radius, length)
                close(g["potential_v"][iy][ix], expected_v,
                      f"SI grid potential state {i}, xy={ix},{iy}",
                      rel=4e-8, absolute=1e-6)
                region = ("surface"
                          if isclose(length, radius, abs_tol=1e-14,
                                     rel_tol=1e-12)
                          else "metal" if length < radius else "vacuum")
                require(g["region"][iy][ix] == region,
                        f"SI grid region state {i}, xy={ix},{iy}")
                e = g["electric_field_v_per_m"][iy][ix]
                if region == "surface":
                    require(e is None,
                            f"single E on ideal discontinuity {i}:{ix},{iy}")
                else:
                    require(isinstance(e, list) and len(e) == 3,
                            f"missing 3D field at {i}:{ix},{iy}")
                    expected_e = ([0., 0., 0.] if region == "metal"
                                  else [K * charge * d / length ** 3
                                        for d in delta])
                    for j in range(3):
                        close(e[j], expected_e[j],
                              f"signed E state {i}, xy={ix},{iy}, {j}",
                              rel=4e-8, absolute=1e-6)
                counts[region] += 1
                checked += 1
        require(counts["metal"] > 0 and counts["vacuum"] > 0,
                f"state {i}: no physical solid/vacuum grid split")
        rows.append({"state": i, "radius_m": radius, "charge_c": charge,
                     "V_R_over_2": expect_half, "V_3R_over_2": expect_outer,
                     "E_x_3R_over_2": expect_field,
                     "outer_sigma_c_m2": expect_sigma, "grid_counts": counts})
    require(checked == 12675, "independent full grid check not complete")
    return {"worlds": rows, "independently_checked_grid_sites": checked}


def thumbnail(image, destination):
    from PIL import Image
    with Image.open(image) as picture:
        picture = picture.convert("RGB")
        picture.thumbnail((1050, 2400))
        picture.save(destination, format="JPEG", quality=70, optimize=True)


def render_original_pdf(repo, output):
    import fitz
    pdf = repo / "POTENTIAL_CONDUCTORS1.pdf"
    require(pdf.is_file(), "original physical textbook PDF is absent")
    with fitz.open(pdf) as doc:
        require(len(doc) >= 26, "PDF physical page 26 missing")
        page = doc[25]
        text = page.get_text()
        require("Illustration 1" in text and "Illustration 2" in text,
                "page 26 does not contain both distinct illustrations")
        (output / "p26-extracted.txt").write_text(text, encoding="utf-8")
        raster = output / "original-page26.png"
        page.get_pixmap(matrix=fitz.Matrix(1.4, 1.4),
                        alpha=False).save(str(raster))
        thumbnail(raster, output / "original-page26.jpg")
        return {"physical_page": 26, "original_pdf_sha256":
                sha256(pdf.read_bytes()).hexdigest(),
                "contains_distinct_illustrations": True,
                "source_text_excerpt": text[:1300]}


def visible_ids(page):
    return [i for i in range(3)
            if page.locator(f'[data-m36e-state="{i}"]').is_visible()]


def actual_nojs(html, viewer_name, output=None):
    with tempfile.TemporaryDirectory(prefix="r2-nojs-") as temp:
        file = Path(temp) / viewer_name
        file.write_text(html, encoding="utf-8")
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            try:
                page = browser.new_page(java_script_enabled=False)
                page.goto(file.resolve().as_uri(), wait_until="load",
                          timeout=45000)
                ids = visible_ids(page)
                if output:
                    png = Path(output).with_suffix(".png")
                    page.screenshot(path=str(png), full_page=True)
                    thumbnail(png, Path(output).with_suffix(".jpg"))
                page.close()
                return ids
            finally:
                browser.close()


def inspect_real_chromium(page_file, manifest, output):
    observed = []
    requests = []
    errors = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 820})
            page.on("request", lambda request: requests.append(request.url)
                    if request.url.startswith(("http://", "https://")) else None)
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(page_file.resolve().as_uri(), wait_until="load",
                      timeout=45000)
            require(page.evaluate("window.conductorViewer?.mode") == "static",
                    "real viewer mislabeled physical time")
            require(page.evaluate("window.conductorViewer?.frameCount") == 3,
                    "real viewer missing teacher states")
            require(page.locator("#density-panel h2").inner_text() ==
                    "Surface-charge density (one real outer face)",
                    "misleading induced density heading")
            for i, (radius, charge, center) in enumerate(WORLDS):
                page.locator("#frame").evaluate(
                    "(el,i)=>{el.value=String(i);"
                    "el.dispatchEvent(new Event('input',{bubbles:true}));}", i)
                ids = visible_ids(page)
                require(ids == [i], f"real slider state {i} shows {ids}")
                card = page.locator(f'[data-m36e-state="{i}"]')
                caption = card.locator("p").nth(1).inner_text()
                expected_charge = ("actual solved Q=0 C" if i == 2
                                   else f"Q={format(charge*1e9,'.11g')} nC")
                require(expected_charge in caption,
                        f"state {i} physically false charge caption")
                require(f"R={format(radius,'.11g')} m" in caption,
                        f"state {i} false radius caption")
                require(f"center=({format(center[0],'.11g')}, " in caption,
                        f"state {i} false center caption")
                if i == 0:
                    require("PRINTED ORIGINAL GEOMETRY" in card.inner_text(),
                            "printed geometry role missing")
                else:
                    require("TEACHER HYPOTHETICAL" in card.inner_text(),
                            "teacher role falsely claims source original")
                expect_v = (K * charge / radius, (2 * K * charge) / (3 * radius))
                for key, expected in zip(("V_half_R", "V_three_half_R"), expect_v):
                    label = card.locator(f'[data-m36e-number="{key}"]')
                    text = label.inner_text()
                    require(text.endswith(" V"), f"no V unit for {key}")
                    close(float(text.split()[0]), expected,
                          f"visible browser SI {i}/{key}", rel=5e-9)
                sigma_label = card.locator('[data-m36e-number="sigma_outer"]')
                require(sigma_label.inner_text().endswith(" C/m²"),
                        "signed sigma units absent")
                close(float(sigma_label.inner_text().split()[0]),
                      charge / (4 * pi * radius * radius),
                      f"browser sigma state {i}", rel=5e-9)
                screenshot = output / f"state-{i}.png"
                page.screenshot(path=str(screenshot), full_page=True,
                                animations="disabled")
                thumbnail(screenshot, output / f"state-{i}.jpg")
                if i == 0:
                    scene = output / "scene-0.png"
                    page.locator("canvas#scene").screenshot(path=str(scene))
                    thumbnail(scene, output / "scene-0.jpg")
                observed.append({"index": i, "visible": ids,
                                 "caption": caption,
                                 "V_R_over_2": expect_v[0],
                                 "V_3R_over_2": expect_v[1]})
            page.close()
        finally:
            browser.close()
    require(not errors, "real Chromium JS errors: " + str(errors))
    require(not requests, "real Chromium requested remote URLs: " + str(requests))
    nojs = actual_nojs(page_file.read_text(encoding="utf-8"),
                       manifest["viewer_file"], output / "nojs-original")
    require(nojs == [0], f"unmodified HTML no-JS leaks teacher: {nojs}")
    return {"states": observed, "nojs_visible": nojs,
            "external_http_requests": requests, "browser_errors": errors}


def target_validator(html, manifest, viewer_name):
    """Attack the actual corrected production Chromium gate; classify only targeted exceptions."""
    from tools.check_m36d_solid_browser import check
    with tempfile.TemporaryDirectory(prefix="r2-actual-target-") as temp:
        dest = Path(temp)
        (dest / viewer_name).write_text(html, encoding="utf-8")
        (dest / "native-solid-sphere.json").write_text(
            json.dumps(manifest, allow_nan=False), encoding="utf-8")
        try:
            check(dest)
        except AssertionError as error:
            return "REJECTED", str(error)
        except Exception as error:
            return "ERROR", f"{type(error).__name__}: {error}"
        else:
            return "ACCEPTED", "forged evidence was accepted"


def build_hostile(original, manifest):
    """Original A3/A4/A5/A6/A7/A9/A10 plus reviewer-created unfamiliar variants."""
    cases = []
    def add(label, html, fragment, altered=None, nojs=None):
        cases.append({"label": label, "html": html,
                      "manifest": deepcopy(manifest) if altered is None else altered,
                      "reason_fragment": fragment, "nojs_expected": nojs})

    add("A3 negative teacher falsely positive Q",
        replace_unique(original, "Isolated net Q=-2 nC (authored teacher value)",
                       "Isolated net Q=+2 nC (authored teacher value)"),
        "visible isolated signed Q contradicts")
    add("A4 grounded Q falsely nonzero",
        replace_unique(original, "Grounded · actual solved Q=0 C in empty space",
                       "Grounded · actual solved Q=7 nC in empty space"),
        "visible grounded sphere charge caption contradicts")
    add("A5 teacher sphere physical radius falsified",
        replace_unique(original, "TRUE SOLID Sphere A: R=0.12 m;",
                       "TRUE SOLID Sphere A: R=1.2 m;"),
        "visible source solid radius contradicts")
    add("A6 symbolic textbook falsely assigned exact numeric R/Q",
        replace_unique(original, "The printed source supplies SYMBOLIC R and Q.",
                       "The printed source supplies SYMBOLIC R and Q, exactly R=0.10m and Q=+1nC."),
        "source-given symbols and teacher numbers not distinguished")
    add("A7 teacher state 1 visible without JavaScript",
        replace_unique(original,
                       'data-m36e-role="teacher_changed_radius_charge_and_centre" hidden>',
                       'data-m36e-role="teacher_changed_radius_charge_and_centre">'),
        "no-JS source fallback must show only original", nojs=[0, 1])
    native_both = deepcopy(manifest)
    original_v = manifest["native_states"][0]["native_samples"]["half_radius_potential_v"]
    fraud = original_v + 17
    native_both["native_states"][0]["native_samples"]["half_radius_potential_v"] = fraud
    old_markup = ('data-m36e-number="V_half_R" data-native-value="' +
                  format(original_v, ".17g") + '">' + format(original_v, ".11g") + ' V</strong>')
    new_markup = ('data-m36e-number="V_half_R" data-native-value="' +
                  format(fraud, ".17g") + '">' + format(fraud, ".11g") + ' V</strong>')
    add("A9 co-forged numeric visible answer and native manifest",
        replace_unique(original, old_markup, new_markup),
        "independent Gauss", altered=native_both)
    add("A10 impossible 1-million-volt embedded sample",
        change_grid(original, lambda b: b["frames"][0]["grid"]["potential_v"][2].__setitem__(2, 1e6)),
        "embedded grid SI mismatch")
    add("N1 changed teacher centre caption y versus native centre",
        replace_unique(original, "center=(0.025, 0, 0) m.",
                       "center=(0.025, 0.03, 0) m."),
        "visible sphere world centre contradicts")
    add("N2 no-JS hidden-state leak of teacher state 2",
        replace_unique(original,
                       'data-m36e-role="teacher_grounded_no_external_sources" hidden>',
                       'data-m36e-role="teacher_grounded_no_external_sources">'),
        "no-JS source fallback must show only original", nojs=[0, 2])
    add("N3 false nC-to-pC charge unit on negative teacher",
        replace_unique(original, "Isolated net Q=-2 nC (authored teacher value)",
                       "Isolated net Q=-2 pC (authored teacher value)"),
        "visible isolated net-charge caption malformed")
    def reverse_e(b):
        g = b["frames"][1]["grid"]["electric_field_v_per_m"]
        require(g[2][2] is not None and any(abs(v) > 1e-10 for v in g[2][2]),
                "signed E-falsification target unexpectedly zero")
        g[2][2] = [-v for v in g[2][2]]
    add("N4 reverse full signed teacher E vector",
        change_grid(original, reverse_e), "embedded grid SI mismatch")
    def forged_metal(b):
        g = b["frames"][0]["grid"]["region"]
        require(g[32][32] == "metal", "metal mutation site not actual metal")
        g[32][32] = "vacuum"
    add("N5 forged real metal grid cell to vacuum",
        change_grid(original, forged_metal),
        "embedded grid incorrectly paints solid interior")
    def forged_plane(b):
        b["frames"][0]["plane"]["u"][0] += .03
    add("N6 falsify embedded physical plane basis",
        change_grid(original, forged_plane),
        "embedded grid SI mismatch plane u unit")
    add("N7 append false exact source values to provenance banner",
        replace_unique(original,
                       "Printed values R and Q are SYMBOLIC.",
                       "Printed values R and Q are SYMBOLIC but numerically fixed in the textbook."),
        "source-authentic banner falsely changes")
    return cases


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    repo = args.source_dir.resolve()
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)
    main_result = {"review": "Chat B independent R2-02",
                   "head": HEAD, "native_git_tree": TREE,
                   "review_target": "conductor_sim PR #88",
                   "positive": None, "hostile_first_attempts": []}
    report_path = out / "review-02-first-attempt.json"

    def save():
        report_path.write_text(
            json.dumps(main_result, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
            encoding="utf-8")

    save()
    main_result["pdf"] = render_original_pdf(repo, out)
    manifest = json.loads((out / "native-solid-sphere.json").read_text(encoding="utf-8"))
    viewer_file = out / manifest["viewer_file"]
    html = viewer_file.read_text(encoding="utf-8")
    main_result["positive"] = {
        "reviewer_analytic_SI": verify_true_native_and_grid(manifest, read_bundle(html)),
        "real_chromium": inspect_real_chromium(viewer_file, manifest, out)}
    save()
    # The production browser gate is a target, not independent math evidence.
    result, reason = target_validator(html, manifest, manifest["viewer_file"])
    require(result == "ACCEPTED", "unmodified corrected production browser gate refuses real source: " + reason)
    main_result["positive"]["authentic_target_browser"] = result
    save()

    for probe in build_hostile(html, manifest):
        if probe["nojs_expected"] is not None:
            special = out / ("hostile-" + probe["label"].split()[0] + "-nojs")
            nojs = actual_nojs(probe["html"], manifest["viewer_file"], special)
            require(nojs == probe["nojs_expected"],
                    f"{probe['label']}: real no-JS visible states {nojs}, not {probe['nojs_expected']}")
        else:
            nojs = None
        status, reason = target_validator(probe["html"], probe["manifest"],
                                          manifest["viewer_file"])
        proper = status == "REJECTED" and probe["reason_fragment"] in reason
        record = {"probe": probe["label"], "target_status": status,
                  "first_reason": reason, "intended_rejection": proper,
                  "actual_nojs_visible": nojs}
        main_result["hostile_first_attempts"].append(record)
        save()
        print(json.dumps(record, ensure_ascii=False), flush=True)
        require(proper, f"real Chromium failed intended attack {probe['label']}: {status}, {reason}")
    main_result["completed"] = True
    save()
    print("R2-02 independent actual browser, SI all-grid and first hostile attempts complete",
          len(main_result["hostile_first_attempts"]), flush=True)


if __name__ == "__main__":
    main()
