"""Independent R2 for M38b PR92: source integrity and real no-JS Chromium.

Runs only against a literal source SHA. Reviewer-owned unfamiliar CSS/SVG probes
are separate from the developer's 26 attacks. All first attempts are retained.
No production files or branches are changed by this program.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from math import hypot
from pathlib import Path
import re
import subprocess
import sys
import traceback

from playwright.sync_api import sync_playwright

from conductor_sim.model import EPSILON_0
from conductor_sim.prescribed_ground_wire import author_prescribed_grounded_sphere
from conductor_sim.prescribed_ground_line import PrescribedSphereLineSpec, sample_prescribed_sphere_line
from conductor_sim.prescribed_line_viewer import line_view_manifest, render_prescribed_line_viewer
from tools.m38a_line_reference import check_line_record
from tools.m38b_line_view_reference import check_line_view
from tools.check_m38b_line_browser import _verify_canonical_html

HEAD = "424eada71313bc6da381172ec27b9be4cfc5d035"
TREE = "547b2206f35b43beb8e0c38c461f5c73364cf88b"
R1 = "1ef915fdae72a032250c75fed2391ca40fab634c"
MAIN = "efff38c1608b76ebcd57ab02d51aea359b841f10"
FIVE = {
    ".github/workflows/m38b-line-viewer.yml",
    "docs/m38b.md",
    "tests/test_m38b_line_viewer.py",
    "tools/check_m38b_line_browser.py",
    "tools/check_m38b_line_hostility.py",
}
WORK = Path("../review02-evidence")
WORK.mkdir(exist_ok=True, parents=True)
EVENTS = []

def record(kind, **kwargs):
    e = {"kind": kind, **kwargs}
    EVENTS.append(e)
    (WORK / "review02-events.json").write_text(
        json.dumps(EVENTS, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(e, ensure_ascii=False), flush=True)

def run(*args, timeout=200, expected=0):
    p = subprocess.run(args, text=True, capture_output=True, timeout=timeout)
    if expected is not None and p.returncode != expected:
        raise AssertionError(f"command {args} returned {p.returncode}, wanted {expected}\n"
                             f"stdout: {p.stdout[-4000:]}\nstderr: {p.stderr[-4000:]}")
    return p

def git(*args):
    return run("git", *args).stdout.strip()

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def verify_identity():
    assert git("rev-parse", "HEAD") == HEAD
    assert git("rev-parse", "HEAD^{tree}") == TREE
    assert git("rev-parse", "HEAD^") == R1
    assert git("merge-base", MAIN, HEAD) == MAIN
    assert git("diff", "--name-only", R1, HEAD).splitlines() == sorted(FIVE), "diff not five modified files"
    statuses = git("diff", "--name-status", R1, HEAD).splitlines()
    assert set(statuses) == {"M\t" + path for path in FIVE}, statuses
    for path in (
        "02_conductors_half_size.pdf",
        "src/conductor_sim/prescribed_ground_line.py",
        "src/conductor_sim/prescribed_ground_wire.py",
        "src/conductor_sim/prescribed_line_viewer.py",
        "tools/m38a_line_reference.py",
        "tools/m38b_line_view_reference.py",
    ):
        assert git("rev-parse", f"{R1}:{path}") == git("rev-parse", f"{HEAD}:{path}"), path
    assert not git("diff", "--name-only", R1, HEAD, "--", "src/conductor_sim")
    record("source", head=HEAD, tree=TREE, corrected_paths=sorted(FIVE),
           unchanged_physics_pdf_and_renderer_blobs=True)

def make_example():
    directory = WORK / "baseline-41"
    directory.mkdir(exist_ok=True)
    run(sys.executable, "-m", "tools.m38b_line_viewer_example",
        "--output-dir", str(directory))
    for module, name in (
        ("tools.m38a_line_reference", "m38b-line-physics.json"),
        ("tools.m38b_line_view_reference", "m38b-line-viewer.json"),
    ):
        p = run(sys.executable, "-m", module, "--input", str(directory / name))
        (WORK / (module.rsplit(".", 1)[-1] + "-original.log")).write_text(
            p.stdout + "\n" + p.stderr, encoding="utf-8")
    native = json.loads((directory / "m38b-line-physics.json").read_text(encoding="utf-8"))
    manifest = json.loads((directory / "m38b-line-viewer.json").read_text(encoding="utf-8"))
    assert native == manifest["trace"]
    assert check_line_record(native)["independently_checked_kelvin_states"] == 41
    assert check_line_view(manifest)["independently_checked_kelvin_states"] == 41
    _verify_canonical_html(manifest, directory / "m38b-line.html")
    # The JSON canonical comparison must be sensitive to integer vs float
    # even when ordinary Python scalar equality would treat them equal.
    wrong = deepcopy(manifest)
    k = wrong["source"]["newly_solved_original_workbook_items"]
    assert type(k) is int
    wrong["source"]["newly_solved_original_workbook_items"] = float(k)
    assert wrong["source"]["newly_solved_original_workbook_items"] == k
    try:
        _verify_canonical_html(wrong, directory / "m38b-line.html")
    except AssertionError as ex:
        assert "canonical rendered viewer source disagrees" in str(ex), repr(ex)
    else:
        raise AssertionError("type-sensitive canonical manifest guard accepted float for integer")
    b = run(sys.executable, "-m", "tools.check_m38b_line_browser",
            "--output-dir", str(directory), timeout=200)
    (WORK / "baseline-first-browser.log").write_text(b.stdout + "\n" + b.stderr,
                                                    encoding="utf-8")
    report = json.loads((directory / "m38b-chromium-report.json").read_text())
    assert report["physics_states_independently_checked"] == 41
    assert report["javascript_disabled_first_frame"] and report["mobile_390px_verified"]
    assert report["external_http_requests"] == report["javascript_errors"] == 0
    record("baseline", states=41, real_chromium=True, nojs=True, mobile=True,
           requests=0, js_errors=0)
    return directory, manifest

def independent_chromium_control(directory, manifest):
    target = (directory / "m38b-line.html").resolve().as_uri()
    frames = manifest["readouts"]
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        requests, errors = [], []
        try:
            on = browser.new_page(viewport={"width": 1250, "height": 900})
            on.on("request", lambda r: requests.append(r.url)
                  if r.url.startswith(("http://", "https://")) else None)
            on.on("pageerror", lambda e: errors.append(str(e)))
            on.goto(target, wait_until="load")
            assert on.evaluate("window.m38bViewer.sampleCount") == len(frames)
            assert on.evaluate("window.m38bViewer.sourceRole") == "teacher_hypothetical"
            for i in (0, 1, len(frames)//2, len(frames)-1):
                on.locator("#m38b-index").evaluate(
                    "(el, i) => { el.value=String(i); el.dispatchEvent(new Event('input',{bubbles:true})); }", i)
                assert on.locator("#m38b-current").inner_text().strip() == frames[i]["current_label"]
                assert on.locator("#m38b-world").inner_text().strip() == frames[i]["world_position_label"]
                assert on.evaluate("window.m38bViewer.selectedIndex") == i
                if i in (0, len(frames)//2, len(frames)-1):
                    on.screenshot(path=str(WORK / f"independent-js-frame-{i}.png"), full_page=True)
            on.locator("#m38b-reset").click()
            assert on.evaluate("window.m38bViewer.selectedIndex") == 0
            on.locator("#m38b-play").click()
            on.wait_for_function("window.m38bViewer.selectedIndex > 0", timeout=6000)
            on.locator("#m38b-reset").click()
            assert on.evaluate("window.m38bViewer.selectedIndex") == 0
            mobile = browser.new_page(viewport={"width":390, "height":740})
            mobile.goto(target, wait_until="load")
            assert mobile.evaluate("document.body.scrollWidth") <= 395
            mobile.screenshot(path=str(WORK/"independent-mobile.png"), full_page=True)
            mobile.close()
            off = browser.new_context(java_script_enabled=False, viewport={"width":960, "height":800})
            first = off.new_page()
            first.goto(target, wait_until="load")
            assert first.locator("#m38b-index").is_disabled()
            assert first.locator("#m38b-play").is_disabled()
            assert first.locator("#m38b-current").inner_text().strip() == frames[0]["current_label"]
            assert first.locator("#m38b-world").inner_text().strip() == frames[0]["world_position_label"]
            assert "TEACHER HYPOTHETICAL" in first.locator("#m38b-heading").inner_text()
            assert first.locator("#m38b-nojs").is_visible()
            # SVG <line> can have a zero-height bounding box despite its
            # positive-width stroke; check actual computed paint explicitly.
            path = first.locator("#m38b-path").evaluate("""el => {
              const s=getComputedStyle(el);
              return {stroke:s.stroke,width:parseFloat(s.strokeWidth),
                      x1:el.getAttribute('x1'),x2:el.getAttribute('x2')};}""")
            assert path["stroke"] != "none" and path["width"] > 0
            assert path["x1"] != path["x2"]
            first.screenshot(path=str(WORK/"independent-nojs-original.png"), full_page=True)
            first.close()
            off.close()
            on.close()
        finally:
            browser.close()
    assert requests == [] and errors == [], (requests, errors)
    record("independent_chromium", tested_frames=[0,1,20,40],
           play_restart=True, nojs_first=True, mobile=True,
           real_stroke_checked_without_bbox_shortcut=True, http_requests=0, js_errors=0)

STYLE = lambda s, css: s.replace("</style>", css + "</style>", 1)
REPLACE = lambda s, before, after: s.replace(before, after, 1)
CASES = [
    ("r1-pseudo-official", lambda s: STYLE(s,
        '#m38b-heading{font-size:0!important}#m38b-heading::after{content:"OFFICIAL PRINTED WORKBOOK Q21 - OFF-AXIS";display:block;font-size:24px;color:#a00}'), "pseudo_heading"),
    ("r1-pseudo-negative-current", lambda s: STYLE(s,
        '#m38b-current{font-size:0!important}#m38b-current::after{content:"-9 A";display:block;font-size:18px;color:#a00}'), "pseudo_current"),
    ("r1-path-stroke-none", lambda s: REPLACE(s,'stroke="#9e6b30"', 'stroke="none"'), "path"),
    ("r1-zero-axis-stroke-none", lambda s: REPLACE(s,'stroke="#567185"', 'stroke="none"'), "zero"),
    ("r1-sphere-invisible", lambda s: STYLE(s,
        '#m38b-sphere{fill:none!important;stroke:none!important}'), "sphere"),
    ("r1-scene-mirrored", lambda s: STYLE(s,
        '#m38b-scene{transform:scaleX(-1)!important}'), "mirror"),
    ("novel-source-ancestor-opacity", lambda s: STYLE(s,
        '#m38b-source{opacity:0!important}'), "source_opacity"),
    ("novel-chart-vertical-flip", lambda s: STYLE(s,
        '#m38b-current-chart{transform:scaleY(-1)!important}'), "chart_flip"),
    ("novel-world-pseudo-before", lambda s: STYLE(s,
        '#m38b-world{font-size:0!important}#m38b-world::before{content:"[999, 999, 999] m";display:block;font-size:20px;color:#a00}'), "pseudo_world"),
    ("novel-path-css-opacity", lambda s: STYLE(s,
        '#m38b-path{opacity:0!important}'), "path_opacity"),
    ("direct-incorrect-source", lambda s: REPLACE(s,
        '<h1 id="m38b-heading">TEACHER HYPOTHETICAL',
        '<h1 id="m38b-heading">OFFICIAL WORKBOOK ORIGINAL'), "direct_source"),
    ("direct-negative-current", lambda s: re.sub(
        r'(<strong class="value" id="m38b-current">)[^<]+',
        lambda m:m.group(1)+"-9 A", s, count=1), "direct_current"),
    ("direct-wrong-charge-sign", lambda s: re.sub(
        r'(<text id="m38b-q-sign"[^>]*>)[^<]+',
        lambda m:m.group(1)+"−q", s, count=1), "direct_sign"),
    ("direct-wrong-sphere-radius", lambda s: re.sub(
        r'(<circle id="m38b-sphere" cx="[^"]+" cy="[^"]+" r=")[^"]+',
        lambda m:m.group(1)+"13", s, count=1), "direct_radius"),
]
DIRECT_REASONS = {
    "direct_source": "false visible teacher-vs-original source attribution",
    "direct_current": "no-JS first SI/world label mismatch",
    "direct_sign": "visible source charge sign contradicts physical signed q",
    "direct_radius": "false visible fixed physical sphere geometry",
}
SCRIPT = re.compile(r'(<script id="m38b-data" type="application/json">)(.*?)(</script>)', re.S)

def observed_css(page, mode):
    return page.evaluate("""(mode) => {
      const el = s=>document.querySelector(s), cs=s=>getComputedStyle(el(s));
      return {mode, heading:el('#m38b-heading').textContent,
        heading_after:getComputedStyle(el('#m38b-heading'),'::after').content,
        heading_font:cs('#m38b-heading').fontSize,
        current:el('#m38b-current').textContent,
        current_after:getComputedStyle(el('#m38b-current'),'::after').content,
        current_font:cs('#m38b-current').fontSize,
        world:el('#m38b-world').textContent,
        world_before:getComputedStyle(el('#m38b-world'),'::before').content,
        world_font:cs('#m38b-world').fontSize,
        sphere_fill:cs('#m38b-sphere').fill,
        sphere_stroke:cs('#m38b-sphere').stroke,
        path_stroke:cs('#m38b-path').stroke,
        path_opacity:cs('#m38b-path').opacity,
        zero_stroke:cs('#m38b-zero').stroke,
        scene_transform:cs('#m38b-scene').transform,
        chart_transform:cs('#m38b-current-chart').transform,
        source_opacity:cs('#m38b-source').opacity,
        qsign:el('#m38b-q-sign').textContent,
        sphere_radius:el('#m38b-sphere').getAttribute('r'),
        disabled:el('#m38b-index').disabled
      };
    }""", mode)

def assert_false_visible(d, mode):
    assert d["disabled"] is True
    if mode == "pseudo_heading":
        assert "OFFICIAL PRINTED WORKBOOK" in d["heading_after"]
        assert d["heading_font"] == "0px" and "TEACHER HYPOTHETICAL" in d["heading"]
    elif mode == "pseudo_current":
        assert "-9 A" in d["current_after"] and d["current_font"] == "0px"
        assert d["current"].strip() != "-9 A"
    elif mode == "path": assert d["path_stroke"] == "none"
    elif mode == "zero": assert d["zero_stroke"] == "none"
    elif mode == "sphere": assert d["sphere_fill"] == d["sphere_stroke"] == "none"
    elif mode == "mirror": assert d["scene_transform"].startswith("matrix(") and "-1" in d["scene_transform"]
    elif mode == "source_opacity": assert d["source_opacity"] == "0" and "TEACHER HYPOTHETICAL" in d["heading"]
    elif mode == "chart_flip": assert d["chart_transform"].startswith("matrix(") and "-1" in d["chart_transform"]
    elif mode == "pseudo_world":
        assert "999, 999, 999" in d["world_before"] and d["world_font"] == "0px"
        assert "999" not in d["world"]
    elif mode == "path_opacity": assert d["path_opacity"] == "0" and d["path_stroke"] != "none"
    elif mode == "direct_source": assert "OFFICIAL WORKBOOK ORIGINAL" in d["heading"]
    elif mode == "direct_current": assert d["current"] == "-9 A"
    elif mode == "direct_sign": assert d["qsign"] == "−q"
    elif mode == "direct_radius": assert d["sphere_radius"] == "13"
    else: raise AssertionError("unknown proof " + mode)

def adversarial(directory):
    pagefile = directory / "m38b-line.html"
    good = pagefile.read_bytes()
    original = good.decode("utf-8")
    j1 = (directory / "m38b-line-physics.json").read_bytes()
    j2 = (directory / "m38b-line-viewer.json").read_bytes()
    match = SCRIPT.search(original)
    assert match is not None
    embed = match.group(2)
    baseline_sha = sha256(good)
    findings = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        off = browser.new_context(java_script_enabled=False, viewport={"width":960, "height":800})
        try:
            for name, tamper, mode in CASES:
                bad = tamper(original)
                assert bad != original and SCRIPT.search(bad).group(2) == embed, name
                pagefile.write_text(bad, encoding="utf-8")
                try:
                    assert (directory/"m38b-line-physics.json").read_bytes() == j1
                    assert (directory/"m38b-line-viewer.json").read_bytes() == j2
                    page = off.new_page()
                    try:
                        page.goto(pagefile.resolve().as_uri(), wait_until="load")
                        d = observed_css(page, mode)
                        assert_false_visible(d, mode)
                        page.screenshot(path=str(WORK / (name+".png")), full_page=True)
                    finally:
                        page.close()
                    p = run(sys.executable, "-m", "tools.check_m38b_line_browser",
                            "--output-dir", str(directory), timeout=200, expected=None)
                    reason = p.stderr.strip().splitlines()[-1] if p.stderr.strip() else ""
                    target_reason = DIRECT_REASONS.get(mode, "noncanonical visible HTML/CSS")
                    assert p.returncode != 0, f"{name}: FORGERY ACCEPTED"
                    assert reason.startswith("AssertionError:") and target_reason in reason, (
                        name, "wrong refusal", p.returncode, reason)
                    finding = {"attack":name, "mode":mode, "actual_nojs_forgery_proved":True,
                               "reason":reason, "screenshot":name+".png",
                               "html_sha256":sha256(bad.encode("utf-8"))}
                    findings.append(finding)
                    record("attack_refused", **finding)
                finally:
                    pagefile.write_bytes(good)
                assert pagefile.read_bytes() == good
                assert (directory/"m38b-line-physics.json").read_bytes() == j1
                assert (directory/"m38b-line-viewer.json").read_bytes() == j2
        finally:
            off.close()
            browser.close()
    assert len(findings) == len(CASES)
    assert sha256(pagefile.read_bytes()) == baseline_sha
    again = run(sys.executable, "-m", "tools.check_m38b_line_browser",
                "--output-dir", str(directory), timeout=200)
    (WORK/"baseline-restored-browser.log").write_text(again.stdout+again.stderr, encoding="utf-8")
    assert pagefile.read_bytes() == good
    (WORK/"review02-attacks.json").write_text(json.dumps(findings,indent=2,ensure_ascii=False)+"\n",
                                              encoding="utf-8")
    record("all_reviewer_attacks", r1_six=6, unfamiliar_four=4,
           direct_four=4, total=len(findings), intended_rejection=len(findings),
           restored_html_sha256=baseline_sha)

def different_teacher_authoring():
    # Different from the 41-state example and the R1 review's 29-state input.
    center = (.74, -.33, .61)
    x0 = (-.11, .04, .95)
    velocity = (.21, -.09, .04)
    T, samples, a = 3.8, 29, .11
    r0 = tuple(x0[j]-center[j] for j in range(3))
    speed2 = sum(v*v for v in velocity)
    t_star = -sum(r0[j]*velocity[j] for j in range(3))/speed2
    d_star = hypot(*(r0[j]+t_star*velocity[j] for j in range(3)))
    assert 0 < t_star < T and d_star > a + .01
    obj = author_prescribed_grounded_sphere(
        -1.8e-9, x0, a, sphere_center_m=center,
        sphere_name="Teacher <novel> & copper", permittivity_f_per_m=1.4*EPSILON_0)
    trace = sample_prescribed_sphere_line(PrescribedSphereLineSpec(
        obj, velocity, T, sample_count=samples, surface_guard_m=.01))
    manifest = line_view_manifest(trace)
    oracle_native = check_line_record(manifest["trace"])
    oracle_view = check_line_view(manifest)
    assert oracle_native["independently_checked_kelvin_states"] == samples
    assert oracle_view["independently_checked_kelvin_states"] == samples
    assert manifest["source"]["role"] == "teacher_hypothetical"
    assert manifest["source"]["newly_solved_original_workbook_items"] == 0
    out = WORK / "reviewer-new-teacher-negative-29"
    out.mkdir(exist_ok=True)
    (out/"m38b-line-physics.json").write_text(json.dumps(trace.as_dict(),ensure_ascii=False))
    (out/"m38b-line-viewer.json").write_text(json.dumps(manifest,ensure_ascii=False))
    (out/"m38b-line.html").write_text(render_prescribed_line_viewer(trace),encoding="utf-8")
    assert "&lt;novel&gt; &amp; copper" in (out/"m38b-line.html").read_text()
    run(sys.executable, "-m", "tools.m38a_line_reference", "--input",
        str(out/"m38b-line-physics.json"))
    run(sys.executable, "-m", "tools.m38b_line_view_reference", "--input",
        str(out/"m38b-line-viewer.json"))
    good = run(sys.executable, "-m", "tools.check_m38b_line_browser",
               "--output-dir", str(out), timeout=200)
    (WORK/"new-teacher-browser.log").write_text(good.stdout+good.stderr,encoding="utf-8")
    assert manifest["trace"]["samples"][0]["wire_current_sphere_to_ground_a"] < 0
    assert manifest["trace"]["samples"][-1]["wire_current_sphere_to_ground_a"] > 0
    record("reviewer_new_teacher_29", new_input=True, count=samples,
           negative_source=True, current_reverses=True, t_closest=t_star,
           distance_closest=d_star, source_role="teacher_hypothetical",
           native_si=True, projection=True, js_and_nojs_chromium=True)

def developer_26_independently_rerun(directory):
    p = run(sys.executable, "-m", "tools.check_m38b_line_hostility",
            "--output-dir", str(directory), timeout=900)
    (WORK/"dev26-independent-rerun.log").write_text(p.stdout+p.stderr,encoding="utf-8")
    j = json.loads((directory/"m38b-hostile-browser-report.json").read_text())
    assert j["actual_chromium_attacks"] == j["physically_refused"] == 26
    assert j["unexpected_acceptances"] == 0
    assert j["genuine_html_byte_exact_restored"] and j["native_si_unchanged"]
    assert len(j["cases"]) == 26
    assert all(c["refusal"] == "REJECTED_AS_INTENDED" for c in j["cases"])
    record("developer_26_separate", actual=26, as_intended=26,
           restored=True, screenshots=26, original_json_unchanged=True)

def main():
    try:
        verify_identity()
        standard, manifest = make_example()
        independent_chromium_control(standard, manifest)
        adversarial(standard)
        different_teacher_authoring()
        developer_26_independently_rerun(standard)
        final = {"schema":"conductor_sim.m38b_pr92_chatb_review02.v1",
                 "source_head":HEAD,"source_tree":TREE,"verdict":"PASS",
                 "reviewer_css_svg":10,"reviewer_direct":4,"developer_26_rerun":26,
                 "new_teacher_sample_count":29,"events":EVENTS}
        (WORK/"review02-results.json").write_text(
            json.dumps(final, indent=2, ensure_ascii=False)+"\n",encoding="utf-8")
        print("INDEPENDENT R2 PASS", json.dumps({k:v for k,v in final.items() if k!="events"}),flush=True)
    except BaseException:
        (WORK/"review02-first-failure.txt").write_text(traceback.format_exc(),encoding="utf-8")
        print("INDEPENDENT R2 FAILURE",traceback.format_exc(),flush=True)
        raise

if __name__ == "__main__":
    main()
