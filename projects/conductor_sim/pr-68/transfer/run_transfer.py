"""M29b R2 follow-up: executable unfamiliar native source/event transfer.

This is a separate, independently inspectable test harness in review_sandbox.
It checks out conductor_sim at the frozen PR #68 source SHA; it does NOT
modify source or use archived native JSON as its physical reference.

The novel physical input and standalone reference targets were supplied by
independent Chat B review-01, under F-01, 2026-11-16. This harness executes
that input through the native M29b API, compares against an independently
computed Gauss-Legendre/DOP853 integration and renders fresh 390px Chromium.
Passing this AUTHOR-AUTHORED harness is not, alone, a reviewer PASS.
"""
from __future__ import annotations

from hashlib import sha256
import json
from math import pi
from pathlib import Path
import subprocess

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp
from playwright.sync_api import sync_playwright

from conductor_sim import (
    FixedPointField, PointCharge, PrescribedField, TestChargeMotionSpec,
    UniformRodField,
)
from conductor_sim.conservative_forces import UniformGravity
from conductor_sim.motion_events import EventPolicy, PlaneEvent
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.structural_family import StructuralCase, StructuralFamilyPlan
from conductor_sim.structural_scenarios import NamedSource
from conductor_sim.structural_event_family import (
    StructuralEventFamilyPlan, run_structural_event_family,
)
from conductor_sim.structural_event_viewer import write_structural_event_family_html


SOURCE_SHA = "fe63cab1994b702e7e55348a122ee76f9f5e10ed"
ROD_A = np.array((0.11, -0.10, 0.0), dtype=float)
ROD_B = np.array((0.13, 0.12, 0.0), dtype=float)
POINTS = ((2e-9, (0.18, 0.15, 0.0)), (-1e-9, (-0.16, 0.10, 0.0)))
ADDED = (1.7e-9, (0.21, -0.09, 0.0))
PROBE_Q, MASS, ROD_Q = 1e-9, 1e-5, 3e-9
GRAVITY = np.array((0.0, -0.1, 0.0))
Y0 = np.array((0., 0., 0., 0.05, 0.02, 0.), dtype=float)
DURATION = 0.7
REVIEWER_REF_TIME = (0.6172565559879, 0.5529332751694)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def make_native_plan():
    sources = (
        UniformRodField(ROD_Q, tuple(ROD_A), tuple(ROD_B)),
        FixedPointField(POINTS[0][0], POINTS[0][1]),
        FixedPointField(POINTS[1][0], POINTS[1][1]),
    )
    original = PrescribedScenario(
        "m29b:r2-original",
        TestChargeMotionSpec(
            PrescribedField(sources),
            PointCharge(PROBE_Q, (0., 0., 0.)),
            MASS,
            (0.05, 0.02, 0.),
            DURATION,
            0.005,
            plane_normal=(0., 0., 1.),
            relative_tolerance=1e-10,
            gravity=UniformGravity((0., -0.1, 0.)),
        ),
        (
            ("rod:tilted", "Teacher titled rod <img src=x onerror=window.pwned=true>"),
            ("point:positive", "Held original positive point"),
            ("point:negative", "Held original negative point"),
        ),
        "Independent Chat B teacher hypothetical; this is not a scanned PDF transcription.",
    )
    child = StructuralCase(
        "added-point",
        "Independently add one positive held source; preserve all original IDs.",
        add_sources=(
            NamedSource(
                "point:added",
                "<svg onload=window.pwned=true> Added +1.7 nC point",
                FixedPointField(ADDED[0], ADDED[1]),
            ),
        ),
    )
    family = StructuralFamilyPlan("m29b:r2-transfer", original, (child,))
    question = PlaneEvent(
        "detector:left",
        (-0.006, 0., 0.),
        (1., 0., 0.),
        "Passive negative-x detector",
        direction=-1,
    )
    return StructuralEventFamilyPlan(
        family, (question,), EventPolicy(0.002, 1e-9, 1e-9, 1e-7))


def independent_reference(with_added):
    """Standalone 3D Coulomb + 96-node rod quadrature + DOP853; no native APIs."""
    nodes, weights = leggauss(96)
    pts = ROD_A[None, :] + ((nodes + 1) / 2)[:, None] * (ROD_B - ROD_A)[None, :]
    k = 1.0 / (4 * pi * 8.8541878128e-12)
    points = POINTS + ((ADDED,) if with_added else ())

    def field(r):
        diffs = r[None, :] - pts
        norms = np.linalg.norm(diffs, axis=1)
        e = k * ROD_Q * np.sum((weights / 2 / norms**3)[:, None] * diffs, axis=0)
        for charge, position in points:
            d = r - np.asarray(position, dtype=float)
            e += k * charge * d / np.linalg.norm(d)**3
        return e

    def rhs(_t, y):
        r, v = y[:3], y[3:]
        return np.concatenate((v, (PROBE_Q / MASS) * field(r) + GRAVITY))

    def detector(_t, y):
        return y[0] + 0.006

    detector.direction = -1
    detector.terminal = False
    solution = solve_ivp(
        rhs, (0, DURATION), Y0, method="DOP853", events=detector,
        rtol=5e-12, atol=1e-14, max_step=0.001,
    )
    require(solution.success, "independent DOP853 failed")
    require(len(solution.t_events[0]) == 1, "independent event multiplicity mismatch")
    time = float(solution.t_events[0][0])
    state = solution.y_events[0][0]
    force = PROBE_Q * field(state[:3]) + MASS * GRAVITY
    return {"time_s": time, "position_m": state[:3].tolist(),
            "velocity_m_s": state[3:].tolist(), "force_n": force.tolist()}


def browser_verify(html_path, output_dir, run):
    checks = {}
    with sync_playwright() as driver:
        browser = driver.chromium.launch(headless=True)
        for width in (390, 1360):
            problems, network = [], []
            page = browser.new_page(viewport={"width": width, "height": 860})
            page.on("pageerror", lambda e: problems.append("page: " + str(e)))
            page.on("console", lambda m: problems.append("console: " + m.text) if m.type == "error" else None)
            page.on("request", lambda req: network.append(req.url))
            page.set_content(html_path.read_text(encoding="utf-8"), wait_until="load")
            widths = page.evaluate("""() => ({
                viewport: window.innerWidth,
                document: document.documentElement.scrollWidth,
                scrollOuter: document.querySelector('.scroll').clientWidth,
                scrollInner: document.querySelector('.scroll').scrollWidth,
                table: document.querySelector('.scroll table').getBoundingClientRect().width
            })""")
            require(widths["viewport"] == width and widths["document"] <= width,
                    "page overflows viewport: " + repr(widths))
            require(page.locator("#source-memberships article").count() == 2,
                    "missing named-source membership cards")
            cards = page.locator("#source-memberships").inner_text()
            for source_id in ("rod:tilted", "point:positive", "point:negative", "point:added"):
                require(source_id in cards, "missing source identity: " + source_id)
            require("<img src=x onerror=window.pwned=true>" in cards, "original hostile label missing")
            require("<svg onload=window.pwned=true>" in cards, "added hostile label missing")
            require(page.locator("img[src=x], svg[onload]").count() == 0,
                    "hostile source name executed as markup")
            require(page.evaluate("window.pwned === undefined"),
                    "hostile source name executed as script")
            require(page.locator("#event-rows tr").count() == 2,
                    "native detector table rows are absent or duplicated")
            require(page.locator("#event-rows").inner_text().count("signed direction -1") == 2,
                    "missing signed original and child roots")
            evidence = page.evaluate("""() => JSON.parse(
                document.getElementById('m29b-native-evidence').textContent)""")
            require(evidence["baseline_revision_id"] == run.plan.family.baseline.revision_id,
                    "embedded native evidence has incorrect source identity")
            require(evidence["entries"][0]["source_inventory"][-1]["id"] == "point:added",
                    "embedded native child inventory missing added point")
            if width == 390:
                require(widths["scrollInner"] > widths["scrollOuter"] + 400
                        and widths["table"] >= 1080,
                        "mobile native detail table not scrollable/readable")
                page.locator(".scroll").evaluate("(e)=>e.scrollLeft=e.scrollWidth")
                require(page.locator(".scroll").evaluate("(e)=>e.scrollLeft") > 400,
                        "horizontal scroll failed")
            require(not problems and not network,
                    "browser JS/page/network issues " + repr((problems, network)))
            page.screenshot(path=str(output_dir / ("new-native-%d.png" % width)),
                            full_page=True)
            checks[str(width)] = widths
            page.close()
        browser.close()
    return checks


def main():
    root = Path(__file__).resolve().parents[4]
    output = root / "m29b-r2-transfer-output"
    output.mkdir(parents=True, exist_ok=True)
    checkout = root / "native_source"
    sha = subprocess.check_output(
        ["git", "-C", str(checkout), "rev-parse", "HEAD"], text=True).strip()
    require(sha == SOURCE_SHA, "source checkout changed: " + sha)

    plan = make_native_plan()
    before = plan.family.baseline.as_dict()
    run = run_structural_event_family(plan)
    payload = run.as_dict()
    require(plan.family.baseline.as_dict() == before,
            "native baseline model was mutated")
    require(len(run.entries) == 1 and run.entries[0].status == "complete"
            and run.entries[0].assembly is not None,
            "new fixed-source structural child not admitted as duration-complete")
    require(run.baseline_run.trajectory.termination == "duration"
            and run.entries[0].event_run.trajectory.termination == "duration",
            "one of the two event observations was censored")

    child = run.entries[0]
    require(child.assembly.parent is plan.family.baseline,
            "child was not independently assembled from frozen parent")
    require(child.assembly.scenario.revision_id != plan.family.baseline.revision_id,
            "child did not get a fresh complete-model physical identity")
    require(payload["entries"][0]["structural_assembly"]["parent_revision_id"]
            == plan.family.baseline.revision_id,
            "parent SHA missing or wrong")
    require([x["id"] for x in payload["baseline_source_inventory"]]
            == ["rod:tilted", "point:positive", "point:negative"],
            "incorrect original native source identities")
    require([x["id"] for x in payload["entries"][0]["source_inventory"]]
            == ["rod:tilted", "point:positive", "point:negative", "point:added"],
            "incorrect new native source inventory")
    require([x["operation"] for x in payload["entries"][0]["structural_assembly"]["changes"]]
            == ["add-source"], "incorrect native change ledger")

    references = [independent_reference(False), independent_reference(True)]
    native = [run.baseline_run, child.event_run]
    check_rows = []
    for idx, (model, ref) in enumerate(zip(native, references)):
        require(model.as_dict()["outcomes"] == {"detector:left": "located"},
                "native event outcomes not uniquely located")
        require(len(model.events) == 1, "native event multiplicity not one")
        event = model.events[0]
        require(event.event_id == "detector:left" and event.direction == -1,
                "native signed event is not negative-x detector crossing")
        lo, hi = event.time_bracket_s
        require(lo <= event.sample.time_s <= hi,
                "native event sample outside its own numerical bracket")
        require(abs(event.sample.time_s - ref["time_s"]) <= 5e-7,
                "native root disagrees with independent Gauss-Legendre+DOP853")
        require(abs(ref["time_s"] - REVIEWER_REF_TIME[idx]) <= 1e-9,
                "recomputed independent reference disagrees with first reviewer")
        require(np.linalg.norm(np.array(event.sample.position_m)
                               - ref["position_m"]) < 2e-6,
                "native 3D event position disagrees with independent integrator")
        require(np.linalg.norm(np.array(event.sample.velocity_m_s)
                               - ref["velocity_m_s"]) < 5e-6,
                "native root velocity disagrees with independent integrator")
        require(np.linalg.norm(np.array(event.sample.force_n)
                               - ref["force_n"]) < 1e-10,
                "native force disagrees with independent direct Coulomb/rod force")
        check_rows.append({
            "source": "baseline" if idx == 0 else "added-point",
            "native_root_s": event.sample.time_s,
            "native_bracket_s": list(event.time_bracket_s),
            "native_position_m": list(event.sample.position_m),
            "native_velocity_m_s": list(event.sample.velocity_m_s),
            "native_force_n": list(event.sample.force_n),
            "independent_DOP853_and_quadrature": ref,
            "native_minus_reference_s": event.sample.time_s - ref["time_s"],
        })

    pairing = payload["entries"][0]["event_time_comparisons"]
    require(len(pairing) == 1 and pairing[0]["status"] == "one-resolved-pair"
            and pairing[0]["direction"] == -1,
            "same-signed unique duration-complete native roots were not paired")
    expected_shift = references[1]["time_s"] - references[0]["time_s"]
    native_shift = pairing[0]["estimated_numerical_shift_s"]
    require(abs(expected_shift - native_shift) <= 1e-6,
            "native source-change time shift mismatches independent reference")
    limits = pairing[0]["numerical_bracket_shift_interval_s"]
    require(limits[0] <= native_shift <= limits[1],
            "native numerical shift outside claimed native bracket interval")
    require(not payload["time_interpolation"]
            and not payload["postguard_extrapolation"],
            "fictitious interpolation/continuation claim")

    html = write_structural_event_family_html(
        run, output / "new-native.html",
        title="M29b independently authored tilted rod, signed points and gravity",
    )
    (output / "new-native.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    browser = browser_verify(html, output, run)
    file_sha = {}
    for file in sorted(output.glob("new-native.*")):
        file_sha[file.name] = sha256(file.read_bytes()).hexdigest()
    report = {
        "verdict": "HARNESS PASS; still requires independent follow-up reviewer PASS",
        "source_pr": 68, "exact_source_sha": sha,
        "original_revision_id": plan.family.baseline.revision_id,
        "child_revision_id": child.assembly.scenario.revision_id,
        "child_assembly_revision_id": child.assembly.revision_id,
        "independent_reference": "96-node Gauss-Legendre / SciPy DOP853 / own SI field",
        "roots": check_rows,
        "independent_reference_shift_s": expected_shift,
        "native_shift_s": native_shift,
        "native_shift_bracket_interval_s": limits,
        "new_html_browser_viewports": browser,
        "evidence_file_sha256": file_sha,
        "qualification": (
            "Numerical root brackets are native sampled/integrated evidence, "
            "not rigorous exact-ODE bounds. Fixed-source teacher hypotheticals, "
            "no induced conductor response or postguard continuation."),
    }
    (output / "transfer-receipt.json").write_text(
        json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
