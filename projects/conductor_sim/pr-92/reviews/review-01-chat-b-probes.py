"""Independent M38b / PR92 pinned-source SI and real Chromium adversarial probes.

Reviewer-authored after reading original source. No production changes.
All hostile changes affect only a generated local HTML copy. Preserve first run.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from math import hypot, isclose, pi
from pathlib import Path
import re
import subprocess
import sys

from playwright.sync_api import sync_playwright

from conductor_sim.model import EPSILON_0
from conductor_sim.prescribed_ground_wire import author_prescribed_grounded_sphere
from conductor_sim.prescribed_ground_line import (
    PrescribedSphereLineSpec, sample_prescribed_sphere_line,
)
from conductor_sim.prescribed_line_viewer import (
    line_view_manifest, render_prescribed_line_viewer,
)
from tools.m38a_line_reference import check_line_record
from tools.m38b_line_view_reference import check_line_view
from tools.check_m38b_line_browser import check as check_production_chromium
from tools.m38b_line_viewer_example import run_all


HEAD = "1ef915fdae72a032250c75fed2391ca40fab634c"
TREE = "001cf922c6f89140e33e40e9c7379a2558a124dd"
BASE = "efff38c1608b76ebcd57ab02d51aea359b841f10"
CHARTER = "ff3c020b228f027f8a73cf22c48529ba261182d8"
EXPECTED = {
    ".github/workflows/m38b-line-viewer.yml",
    "docs/m38b.md",
    "docs/m38b_charter.md",
    "src/conductor_sim/prescribed_line_viewer.py",
    "tests/test_m38b_line_viewer.py",
    "tools/check_m38b_line_browser.py",
    "tools/check_m38b_line_hostility.py",
    "tools/m38b_line_view_reference.py",
    "tools/m38b_line_viewer_example.py",
}
WORK = Path("../review01-evidence")
WORK.mkdir(parents=True, exist_ok=True)
events = []


def cmd(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout.strip()


def report(kind, **kw):
    line = {"kind": kind, **kw}
    events.append(line)
    print(json.dumps(line, ensure_ascii=False), flush=True)


def close(a, b, name, rtol=5e-10, atol=5e-21):
    if not isclose(float(a), float(b), rel_tol=rtol, abs_tol=atol):
        raise AssertionError(f"{name}: {a} != independently computed {b}")


def vec_close(a, b, name):
    assert len(a) == len(b) == 3
    for j in range(3):
        close(a[j], b[j], f"{name}[{j}]")


assert cmd("git", "rev-parse", "HEAD") == HEAD
assert cmd("git", "rev-parse", "HEAD^{tree}") == TREE
assert cmd("git", "merge-base", BASE, HEAD) == BASE
changed = cmd("git", "diff", "--name-status", f"{BASE}..{HEAD}").splitlines()
assert set(changed) == {"A\t" + p for p in EXPECTED}, changed
assert cmd("git", "rev-list", "--parents", "-n1", CHARTER).split() == [CHARTER, BASE]
assert cmd("git", "diff", "--name-status", f"{BASE}..{CHARTER}") == "A\tdocs/m38b_charter.md"
for p in (
    "02_conductors_half_size.pdf",
    "src/conductor_sim/grounded_sphere_wire.py",
    "src/conductor_sim/prescribed_ground_line.py",
):
    assert cmd("git", "rev-parse", f"{BASE}:{p}") == cmd("git", "rev-parse", f"{HEAD}:{p}")
report("source_identity", head=HEAD, tree=TREE, nine_added=True, charter_prior=True,
       representative_original_blobs_identical=True)

standard = WORK / "standard-41"
standard_manifest = run_all(standard)
check_line_record(standard_manifest["trace"])
check_line_view(standard_manifest)
base_chrome = check_production_chromium(standard)
report("author_sample_replayed", states=41, source="teacher", actual_chromium=base_chrome)

# Reviewer-owned unfamiliar Cartesian problem; all components, centre coords nonzero.
center = (.83, -.71, 1.09)
x0 = (.21, -.23, 1.37)
velocity = (.28, -.10, .05)
q = -2.3e-9
a = .13
eps = 1.6 * EPSILON_0
duration = 4.2
count = 29
problem = author_prescribed_grounded_sphere(
    q, x0, a, sphere_center_m=center,
    sphere_name="Translated <reviewer> & grounded",
    permittivity_f_per_m=eps,
)
trace = sample_prescribed_sphere_line(PrescribedSphereLineSpec(
    problem, velocity, duration, sample_count=count, surface_guard_m=.015
))
manifest = line_view_manifest(trace)
check_line_record(manifest["trace"])
check_line_view(manifest)
samples = manifest["trace"]["samples"]
layout = manifest["layout"]
readouts = manifest["readouts"]
speed = hypot(*velocity)
u = tuple(vi/speed for vi in velocity)
r0 = tuple(x0[j]-center[j] for j in range(3))
offset = sum(r0[j]*u[j] for j in range(3))
perp = tuple(r0[j]-offset*u[j] for j in range(3))
w = tuple(z/hypot(*perp) for z in perp)
normal = (
    u[1]*w[2]-u[2]*w[1],
    u[2]*w[0]-u[0]*w[2],
    u[0]*w[1]-u[1]*w[0],
)
vec_close(layout["local_u_world"], u, "novel u")
vec_close(layout["local_w_world"], w, "novel w")
vec_close(layout["local_normal_world"], normal, "novel normal")
assert abs(sum(u[i]*w[i] for i in range(3))) < 1e-14
t_closest = -sum(r0[j]*velocity[j] for j in range(3))/speed**2
d_closest = hypot(*(r0[j]+velocity[j]*t_closest for j in range(3)))
assert 0 < t_closest < duration
assert d_closest > a+.015
close(manifest["trace"]["closest_approach_time_s"], t_closest, "closest time")
close(manifest["trace"]["closest_approach_distance_m"], d_closest, "closest radius")

projected = []
for i, sample in enumerate(samples):
    t = duration*i/(count-1)
    x = tuple(x0[j]+velocity[j]*t for j in range(3))
    r = tuple(x[j]-center[j] for j in range(3))
    d = hypot(*r)
    vd = sum(r[j]*velocity[j] for j in range(3))/d
    induced = -q*a/d
    current = -q*a*vd/(d*d)
    K = 1/(4*pi*eps)
    force_r = -K*q*q*a*d / ((d-a)**2*(d+a)**2)
    f = tuple(force_r*r[j]/d for j in range(3))
    energy = -K*q*q*a / (2*(d-a)*(d+a))
    close(sample["time_s"], t, f"t{i}")
    vec_close(sample["source_position_m"], x, f"x{i}")
    vec_close(sample["source_velocity_m_s"], velocity, f"v{i}")
    for field, expected in (
        ("radial_distance_m",d),
        ("radial_velocity_m_s",vd),
        ("induced_sphere_net_charge_c",induced),
        ("wire_current_sphere_to_ground_a",current),
        ("wire_current_ground_to_sphere_a",-current),
        ("induced_mechanical_energy_j",energy),
    ):
        close(sample[field], expected, f"SI {i} {field}")
    vec_close(sample["induced_force_on_source_n"], f, f"force{i}")
    projected.append((
        sum(r[j]*u[j] for j in range(3)),
        sum(r[j]*w[j] for j in range(3))
    ))
peak = max(abs(r["wire_current_sphere_to_ground_a"]) for r in samples)
scale = min(
    275/max(a, *(abs(x) for x,_ in projected)),
    122/max(a, *(abs(y) for _,y in projected)),
    106/a
)
close(layout["pixels_per_meter"], scale, "pixel scale")
close(layout["sphere_r_px"], a*scale, "physical sphere radius")
for i, ((pu,pw),sample,row) in enumerate(zip(projected,samples,readouts)):
    close(row["scene_x_px"], 360+pu*scale, f"scene x {i}")
    close(row["scene_y_px"], 190-pw*scale, f"scene y {i}")
    close(row["chart_x_px"], 64+506*sample["time_s"]/duration, f"chart t {i}")
    close(row["chart_y_px"], 151-97*sample["wire_current_sphere_to_ground_a"]/peak, f"chart I {i}")
for axis, row_index, pos in (("start",0,0),("end",count-1,-1)):
    close(layout["path_"+axis+"_x_px"], readouts[pos]["scene_x_px"], f"path {axis} x")
    close(layout["path_"+axis+"_y_px"], readouts[pos]["scene_y_px"], f"path {axis} y")
assert samples[0]["wire_current_sphere_to_ground_a"] < 0
assert samples[-1]["wire_current_sphere_to_ground_a"] > 0
assert all(velocity)
novel = WORK / "novel-negative-29"
novel.mkdir(parents=True, exist_ok=True)
(novel/"m38b-line-physics.json").write_text(json.dumps(trace.as_dict()), encoding="utf-8")
(novel/"m38b-line-viewer.json").write_text(json.dumps(manifest), encoding="utf-8")
(novel/"m38b-line.html").write_text(render_prescribed_line_viewer(trace), encoding="utf-8")
novel_chrome=check_production_chromium(novel)
assert "&lt;reviewer&gt; &amp; grounded" in (novel/"m38b-line.html").read_text()
report("novel_3d_native_and_browser", center=center, x0=x0, velocity=velocity,
       source_charge_c=q, samples=count, closest_time_s=t_closest,
       closest_distance_m=d_closest,
       negative_to_positive_current=True, independent_si_states=count,
       chromium=novel_chrome)

# A radial teacher special case is not the printed source item.
radial = author_prescribed_grounded_sphere(1e-9,(0.,.4,0.),.1)
radial_trace=sample_prescribed_sphere_line(PrescribedSphereLineSpec(
    radial,(0.,-.05,0.),2.,sample_count=11,surface_guard_m=.01
))
radial_manifest=line_view_manifest(radial_trace)
check_line_view(radial_manifest)
assert radial_manifest["source"]["role"]=="teacher_hypothetical"
assert radial_manifest["source"]["newly_solved_original_workbook_items"]==0
report("radial_special_case", source_role="teacher_hypothetical", states=11)

# Novel CSS/SVG first-frame deceptions preserving full native, manifest and
# embedded JSON. Original developer attacks mutate numeric attributes/text;
# these instead exploit appearance changes invisible to nominal DOM checks.
pagefile = standard / "m38b-line.html"
original = pagefile.read_bytes()
external = (standard/"m38b-line-physics.json").read_bytes()
manifest_bytes = (standard/"m38b-line-viewer.json").read_bytes()
pattern = re.compile(r'(<script id="m38b-data" type="application/json">)(.*?)(</script>)', re.S)
embedded = pattern.search(original.decode()).group(2)


def insert_style(code, css):
    assert code.count("</style>")==1
    return code.replace("</style>",css+"</style>",1)


cases = (
    (
        "pseudo-original-source",
        lambda s: insert_style(s, '#m38b-heading{font-size:0!important}#m38b-heading::after{content:"OFFICIAL PRINTED WORKBOOK Q21 - OFF-AXIS";display:block;font-size:24px;color:#a00}'),
        "pseudo_heading",
    ),
    (
        "pseudo-forged-current",
        lambda s: insert_style(s, '#m38b-current{font-size:0!important}#m38b-current::after{content:"-9 A";display:block;font-size:18px;color:#a00}'),
        "pseudo_current",
    ),
    (
        "invisible-physical-path",
        lambda s: s.replace('stroke="#9e6b30"', 'stroke="none"', 1),
        "path_no_stroke",
    ),
    (
        "invisible-zero-current-axis",
        lambda s: s.replace('stroke="#567185"', 'stroke="none"', 1),
        "zero_no_stroke",
    ),
    (
        "invisible-grounded-sphere",
        lambda s: insert_style(s, '#m38b-sphere{fill:none!important;stroke:none!important}'),
        "sphere_no_stroke",
    ),
    (
        "mirrored-local-axes",
        lambda s: insert_style(s, '#m38b-scene{transform:scaleX(-1)!important}'),
        "mirrored",
    ),
)
outcomes = []
with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    context = browser.new_context(java_script_enabled=False,
                                  viewport={"width":960,"height":800})
    try:
        for name, mutation, mode in cases:
            bad = mutation(original.decode("utf-8"))
            assert bad != original.decode("utf-8"), name
            assert pattern.search(bad).group(2)==embedded, name
            pagefile.write_text(bad, encoding="utf-8")
            try:
                assert (standard/"m38b-line-physics.json").read_bytes() == external
                assert (standard/"m38b-line-viewer.json").read_bytes() == manifest_bytes
                page = context.new_page()
                page.goto(pagefile.resolve().as_uri(),wait_until="load")
                evidence = page.evaluate("""mode => {
                  const sel = (x)=>document.querySelector(x);
                  const cs = (x)=>getComputedStyle(sel(x));
                  const pseudo = (x)=>getComputedStyle(sel(x),'::after').content;
                  return {
                    mode, heading_dom:sel('#m38b-heading').textContent,
                    current_dom:sel('#m38b-current').textContent,
                    heading_pseudo:pseudo('#m38b-heading'),
                    current_pseudo:pseudo('#m38b-current'),
                    heading_font:cs('#m38b-heading').fontSize,
                    current_font:cs('#m38b-current').fontSize,
                    path_stroke:cs('#m38b-path').stroke,
                    zero_stroke:cs('#m38b-zero').stroke,
                    sphere_fill:cs('#m38b-sphere').fill,
                    sphere_stroke:cs('#m38b-sphere').stroke,
                    scene_transform:cs('#m38b-scene').transform,
                    slider_disabled:sel('#m38b-index').disabled
                  };
                }""", mode)
                assert evidence["slider_disabled"] is True
                if mode == "pseudo_heading":
                    assert "OFFICIAL PRINTED" in evidence["heading_pseudo"]
                    assert evidence["heading_font"] == "0px"
                    assert "TEACHER HYPOTHETICAL" in evidence["heading_dom"]
                elif mode == "pseudo_current":
                    assert "-9 A" in evidence["current_pseudo"]
                    assert evidence["current_font"] == "0px"
                    assert evidence["current_dom"] != "-9 A"
                elif mode == "path_no_stroke":
                    assert evidence["path_stroke"] == "none"
                elif mode == "zero_no_stroke":
                    assert evidence["zero_stroke"] == "none"
                elif mode == "sphere_no_stroke":
                    assert evidence["sphere_fill"] == evidence["sphere_stroke"] == "none"
                elif mode == "mirrored":
                    assert evidence["scene_transform"] != "none"
                screenshot = WORK/(name+".png")
                page.screenshot(path=str(screenshot),full_page=True)
                page.close()
                subprocess_result = subprocess.run(
                    [sys.executable,"-m","tools.check_m38b_line_browser",
                     "--output-dir",str(standard)],
                    capture_output=True,text=True,timeout=150,
                )
                status = "ACCEPTED_FALSE_VISUAL" if subprocess_result.returncode == 0 else "REJECTED"
                entry = {
                    "attack":name,"visible_nojs_css_or_svg_proved":True,
                    "gate_status":status,
                    "exit_code":subprocess_result.returncode,
                    "reason":(subprocess_result.stderr.strip().splitlines()[-1]
                              if subprocess_result.stderr.strip() else ""),
                    "evidence":evidence,"screenshot":screenshot.name,
                    "html_sha256":hashlib.sha256(bad.encode()).hexdigest(),
                }
                outcomes.append(entry)
                report("html_only_adversarial", attack=name, gate_status=status,
                       reason=entry["reason"], screenshot=screenshot.name)
            finally:
                pagefile.write_bytes(original)
    finally:
        context.close()
        browser.close()
assert pagefile.read_bytes()==original
assert (standard/"m38b-line-physics.json").read_bytes()==external
assert (standard/"m38b-line-viewer.json").read_bytes()==manifest_bytes
check_production_chromium(standard)
report("restoration", exact_html_and_native=True, baseline_chromium_pass=True)

# The intended outcome of this probe is to REPORT independent blockers honestly,
# not to redefine acceptance as PASS or silently swallow failed probes.
results={
    "schema":"conductor_sim.pr92.independent_chatb_review01.v1",
    "source_head": HEAD, "source_tree":TREE,
    "events":events, "attacks":outcomes,
    "unexpected_browser_acceptances": [
        v["attack"] for v in outcomes if v["gate_status"]=="ACCEPTED_FALSE_VISUAL"
    ],
    "original_html_restored_sha256":hashlib.sha256(original).hexdigest(),
}
(WORK/"review01-results.json").write_text(
    json.dumps(results,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("REVIEWER RESULTS",json.dumps({
    "novel_attacks":len(outcomes),
    "scientifically_false_html_accepted_by_browser_gate":
      results["unexpected_browser_acceptances"],
},ensure_ascii=False), flush=True)
