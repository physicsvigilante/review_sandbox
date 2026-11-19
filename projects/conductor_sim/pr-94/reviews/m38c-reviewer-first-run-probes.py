"""Independent first-run M38c real Chromium adversarial review, pinned PR #94.

This file lives only in review_sandbox, not the source code tree. It must run
from a checkout of conductor_sim HEAD 3a973f1d... with separately generated
original teacher-only Kelvin files in --output-dir. Real Chromium is mandatory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from math import isclose, isfinite
from pathlib import Path
import statistics
import subprocess
import sys
import traceback

from playwright.sync_api import sync_playwright
from tools.check_m38b_line_browser import (
    LABELS, _check_frame, _freeze_actual_playback_frame,
)

EXPECTED_SHA = "3a973f1d340e060bc05d0c879113747a95111686"
EXPECTED_TREE = "6cb46942d1aba0c1a28fc9696419c08334b441eb"
COORD_KEYS = (
    "scene_x_px", "scene_y_px", "sign_x_px", "sign_y_px",
    "chart_x_px", "chart_y_px",
)
SELECTORS = {
    "scene_x_px": ("#m38b-charge", "cx"),
    "scene_y_px": ("#m38b-charge", "cy"),
    "sign_x_px": ("#m38b-q-sign", "x"),
    "sign_y_px": ("#m38b-q-sign", "y"),
    "chart_x_px": ("#m38b-current-marker", "cx"),
    "chart_y_px": ("#m38b-current-marker", "cy"),
}


def cmd(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def record_live(page):
    """New reviewer-owned JS read only: one snapshot of unmodified Play DOM."""
    return page.evaluate(
        """(cfg) => {
          const slider=document.getElementById('m38b-index');
          const v=window.m38bViewer;
          const labels={};
          for(const [sel,key] of Object.entries(cfg.labels)){
            labels[key]=(document.querySelector(sel)?.textContent || '').trim();
          }
          const coords={};
          for(const [key,pair] of Object.entries(cfg.coords)){
            coords[key]=Number(document.querySelector(pair[0]).getAttribute(pair[1]));
          }
          return {index:Number(slider.value), viewerIndex:v.selectedIndex,
                  sampleCount:v.sampleCount, labels, coords};
        }""",
        {"labels": LABELS, "coords": SELECTORS},
    )


def assert_saved_row(snapshot, manifest, *, prefix):
    """Reviewer independently checks all 10 labels and six SVG coordinates."""
    idx = snapshot["index"]
    assert type(idx) is int and 0 < idx < len(manifest["readouts"]), (prefix, idx)
    assert snapshot["viewerIndex"] == idx
    assert snapshot["sampleCount"] == len(manifest["readouts"])
    expected = manifest["readouts"][idx]
    for key in LABELS.values():
        assert snapshot["labels"][key] == expected[key], (prefix, idx, key)
    for key in COORD_KEYS:
        got = snapshot["coords"][key]
        assert type(got) in (float, int) and isfinite(got), (prefix, idx, key)
        assert isclose(got, expected[key], rel_tol=4e-11, abs_tol=2e-7), (
            prefix, idx, key, got, expected[key]
        )
    return idx


def measure_real_play_ticks(page):
    """Observe actual browser timer transitions without touching playback."""
    ticks = page.evaluate(
        """async () => {
          const s=document.getElementById('m38b-index');
          const ticks=[{i:Number(s.value),t:performance.now()}];
          const began=performance.now();
          while (ticks.length < 5 && performance.now()-began < 2400) {
            await new Promise(resolve=>setTimeout(resolve,12));
            const idx=Number(s.value);
            if (idx !== ticks[ticks.length-1].i)
              ticks.push({i:idx,t:performance.now()});
          }
          return ticks;
        }"""
    )
    assert len(ticks) >= 4, ("no genuine timer ticks", ticks)
    for a, b in zip(ticks, ticks[1:]):
        assert b["i"] == a["i"] + 1, ("timer skipped/faked index", ticks)
    intervals = [round(b["t"] - a["t"], 3) for a, b in zip(ticks[1:-1], ticks[2:])]
    assert all(60 <= ms <= 210 for ms in intervals), ("timer not ~100ms", intervals)
    assert 70 <= statistics.median(intervals) <= 170, intervals
    return {"ticks": ticks, "measured_intervals_ms": intervals}


def test_play_and_freeze(page, manifest, screenshots, minimum_index):
    page.locator("#m38b-reset").click()
    _check_frame(page, manifest, 0, no_js=False)
    page.locator("#m38b-play").click()
    page.wait_for_function(
        "(min) => window.m38bViewer?.selectedIndex >= min",
        minimum_index,
        timeout=5000,
    )
    # This first live snapshot is our independent inspector; neither helper
    # nor slider redraw has been called and the real Play timer is still live.
    before = record_live(page)
    before_index = assert_saved_row(
        before, manifest, prefix="independent live running Play"
    )
    assert before_index >= minimum_index
    # The source helper re-captures unmodified LIVE display, then issues the
    # actual slider-input pause in its same JS callback. It may see a later
    # real frame than the separately captured before_index; that is normal.
    frozen_index = _freeze_actual_playback_frame(page, manifest)
    assert frozen_index >= before_index
    after = record_live(page)
    assert_saved_row(after, manifest, prefix="post-slider real freeze")
    assert after["index"] == frozen_index
    _check_frame(page, manifest, frozen_index, no_js=False)
    page.wait_for_timeout(240)
    still = record_live(page)
    assert_saved_row(still, manifest, prefix="after 240ms no-tick")
    assert still == after, "timer kept running after official slider pause"
    _check_frame(page, manifest, frozen_index, no_js=False)
    screenshot = screenshots / f"genuine-play-frozen-min{minimum_index}-index{frozen_index}.png"
    page.screenshot(path=str(screenshot), full_page=True)
    return {
        "minimum_requested": minimum_index,
        "live_unmodified_index": before_index,
        "frozen_index": frozen_index,
        "paused_stability_ms": 240,
        "screenshot": screenshot.name,
        "sample_time_s": manifest["trace"]["samples"][frozen_index]["time_s"],
        "sample_signed_current_a": manifest["trace"]["samples"][frozen_index][
            "wire_current_sphere_to_ground_a"
        ],
    }


def reach_real_played_stable_state(page, manifest):
    """Allowed adversarial staging: halt at a genuinely Play-advanced frame.

    We deliberately stop via the real slider input before hostile mutation, so
    random timer ticks cannot erase our forged on-screen value. Crucially, the
    corrected helper's OWN atomic pre-redraw capture must still catch it.
    """
    page.locator("#m38b-reset").click()
    page.locator("#m38b-play").click()
    page.wait_for_function(
        "() => window.m38bViewer?.selectedIndex >= 4", timeout=5000
    )
    played_index = page.evaluate(
        """() => {
          const slider=document.getElementById('m38b-index');
          const index=Number(slider.value);
          slider.dispatchEvent(new Event('input',{bubbles:true}));
          return index;
        }"""
    )
    assert played_index >= 4
    _check_frame(page, manifest, played_index, no_js=False)
    page.wait_for_timeout(170)
    _check_frame(page, manifest, played_index, no_js=False)
    return played_index


def expect_live_forgery_refusal(page, manifest, screenshots, *, name,
                               selector, mode, value, key, wanted):
    i = reach_real_played_stable_state(page, manifest)
    if mode == "attr":
        page.locator(selector).evaluate(
            "(el,args) => el.setAttribute(args[0], args[1])", [key, value]
        )
    else:
        page.locator(selector).evaluate("(el,text) => el.textContent=text", value)
    forged = page.locator(selector).get_attribute(key) if mode == "attr" else (
        page.locator(selector).text_content()
    )
    assert forged == value, ("hostile display not injected", name, forged)
    pic = screenshots / f"forged-live-{name}-index{i}.png"
    page.screenshot(path=str(pic), full_page=True)
    # Identical original source and embedded JSON; the helper's slider event
    # *will repair the DOM*, so only the live pre-redraw snapshot can reject.
    try:
        _freeze_actual_playback_frame(page, manifest)
    except AssertionError as exc:
        reason = str(exc)
    else:
        raise AssertionError(f"{name}: forged pre-redraw display was ACCEPTED")
    assert wanted in reason, (name, "wrong refusal", reason)
    assert key in reason or mode == "text", (name, "wrong data key", reason)
    _check_frame(page, manifest, i, no_js=False)
    return {
        "attack": name, "genuine_played_index": i, "forged_value": value,
        "intended_refusal": reason, "original_physics_unchanged": True,
        "pause_redraw_repaired_dom_after_refusal": True,
        "screenshot": pic.name,
    }


def test_unfamiliar_html_css_attack(directory, browser, screenshots):
    """New HTML-only blur attack: actual visible effect with JS disabled."""
    html = directory / "m38b-line.html"
    raw = html.read_bytes()
    native = (directory / "m38b-line-physics.json").read_bytes()
    manifest = (directory / "m38b-line-viewer.json").read_bytes()
    injection = b'<style>#m38b-world{filter:blur(8px)!important}'
    assert raw.count(b"<style>") == 1
    assert injection not in raw
    forged_html = raw.replace(b"<style>", injection, 1)
    proof = {}
    ctx = browser.new_context(java_script_enabled=False, viewport={
        "width": 980, "height": 860
    })
    try:
        html.write_bytes(forged_html)
        page = ctx.new_page()
        page.goto(html.resolve().as_uri(), wait_until="load")
        css = page.locator("#m38b-world").evaluate(
            "(el) => getComputedStyle(el).filter"
        )
        assert css != "none" and "blur(8px)" in css, ("not visibly forged", css)
        pic = screenshots / "forged-html-only-world-blur-nojs.png"
        page.screenshot(path=str(pic), full_page=True)
        page.close()
        assert (directory / "m38b-line-physics.json").read_bytes() == native
        assert (directory / "m38b-line-viewer.json").read_bytes() == manifest
        assert html.read_bytes() == forged_html
        attempt = subprocess.run([
            sys.executable, "-m", "tools.check_m38b_line_browser",
            "--output-dir", str(directory),
        ], capture_output=True, text=True, timeout=165, check=False)
        detail = attempt.stderr.strip().splitlines()[-1] if attempt.stderr else ""
        assert attempt.returncode != 0, (
            "new hostile HTML-only CSS blur accepted", attempt.stdout
        )
        assert detail.startswith("AssertionError:") and (
            "noncanonical visible HTML/CSS" in detail
        ), ("wrong CSS refusal", detail)
        proof = {
            "attack": "new-html-only-nojs-world-readout-css-blur",
            "actual_nojs_computed_filter": css,
            "returncode": attempt.returncode,
            "refusal": detail,
            "original_external_and_embedded_si_unchanged": True,
            "screenshot": pic.name,
        }
    finally:
        html.write_bytes(raw)
        ctx.close()
    assert html.read_bytes() == raw, "original HTML not byte-for-byte restored"
    return proof


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    d = args.output_dir.resolve()
    screenshot_dir = d / "reviewer-probe-screenshots"
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((d / "m38b-line-viewer.json").read_text())
    out = {
        "type": "independent-reviewer-first-attempt-m38c-pr94",
        "source_sha": cmd("git", "rev-parse", "HEAD"),
        "source_tree": cmd("git", "rev-parse", "HEAD^{tree}"),
        "browser_engine": "actual Chromium from Playwright",
        "tests": [],
    }
    logfile = d / "reviewer-first-run-probes.json"
    try:
        assert out["source_sha"] == EXPECTED_SHA
        assert out["source_tree"] == EXPECTED_TREE
        assert len(manifest["readouts"]) == 41
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            out["chromium_version"] = browser.version
            errors = []
            external_requests = []
            page = browser.new_page(viewport={"width": 1250, "height": 900})
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.on("request", lambda r: external_requests.append(r.url)
                    if r.url.startswith(("https://", "http://")) else None)
            page.goto((d / "m38b-line.html").as_uri(), wait_until="load")
            _check_frame(page, manifest, 0, no_js=False)
            # Real 100-ms timer observation across multiple original states.
            page.locator("#m38b-play").click()
            ticks = measure_real_play_ticks(page)
            out["tests"].append({"timer": ticks, "status": "PASS"})
            # Unfamiliar probes: minimum index 1 and at least 4.
            for minimum in (1, 4):
                result = test_play_and_freeze(
                    page, manifest, screenshot_dir, minimum
                )
                out["tests"].append({"real_play_freeze": result, "status": "PASS"})
            # Novel forged LIVE pre-pause current-marker AND physical SI label.
            for attack in (
                dict(name="chart-y", selector="#m38b-current-marker",
                     mode="attr", key="cy", value="999",
                     wanted="LIVE playback scene/current marker"),
                dict(name="current-text", selector="#m38b-current",
                     mode="text", key="", value="-9 A",
                     wanted="LIVE playback SI/world label"),
                dict(name="world-xyz-text", selector="#m38b-world",
                     mode="text", key="", value="(99,99,99) m",
                     wanted="LIVE playback SI/world label"),
            ):
                outcome = expect_live_forgery_refusal(
                    page, manifest, screenshot_dir, **attack
                )
                out["tests"].append({"adversarial_live": outcome, "status": "PASS"})
            page.locator("#m38b-reset").click()
            _check_frame(page, manifest, 0, no_js=False)
            assert not errors, ("browser JS errors", errors)
            assert not external_requests, ("external HTTP", external_requests)
            out["tests"].append({"runtime_errors": 0, "external_http": 0})
            page.close()
            css = test_unfamiliar_html_css_attack(
                d, browser, screenshot_dir
            )
            out["tests"].append({"adversarial_html": css, "status": "PASS"})
            browser.close()
        out["status"] = "PASS"
    except BaseException as exc:
        out["status"] = "FAIL"
        out["exception"] = repr(exc)
        out["traceback"] = traceback.format_exc()
        raise
    finally:
        logfile.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"status": out["status"], "evidence": str(logfile),
                          "checks_completed": len(out["tests"])}, sort_keys=True))


if __name__ == "__main__":
    main()
