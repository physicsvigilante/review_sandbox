# Independent review 01 — conductor_sim PR 94 / M38c

**Verdict: PASS — scoped browser playback-race correction only.** Date: 2026-11-19. Reviewer: separate Chat B context with reviewer-owned GitHub Actions, exact Git checkout, native data generation and actual Playwright Chromium. **This is not an owner merge authorization.**

## Reviewed identity and scope

- Production: https://github.com/physicsvigilante/conductor_sim/pull/94 — observed OPEN, DRAFT, UNMERGED after final checks.
- Literal production HEAD: **3a973f1d340e060bc05d0c879113747a95111686**
- Independently computed native Git TREE: **6cb46942d1aba0c1a28fc9696419c08334b441eb**
- Released base commit: **44e0c50f3258452d112ab7a16b87759063054832**, historical released tree **547b2206f35b43beb8e0c38c461f5c73364cf88b**.
- Separate frozen charter ancestor: **216ef595025083708e9fe5abbaccdd75e67e639a**. The reviewer confirmed its commit modifies only docs/m38c_charter.md.
- Independently verified base-to-HEAD paths, exactly four: ADD docs/m38c_charter.md, ADD docs/m38c.md, MODIFY tools/check_m38b_line_browser.py, MODIFY tests/test_m38b_line_viewer.py.
- Original physics and presentation files unchanged by native Git blob identity: prescribed_line_viewer.py, prescribed_ground_line.py, prescribed_ground_wire.py, both M38a/M38b independent references, the pre-existing M38b hostility checker and both original PDF inputs. No new viewer code or scientific equations were introduced.
- Source developer CI: API returned **22/22 SUCCESS** exact-SHA runs, including focused https://github.com/physicsvigilante/conductor_sim/actions/runs/44474313750 . Developer CI is explicitly not independent review evidence.

**Original failure remains preserved:** genuine post-merge main-push workflow https://github.com/physicsvigilante/conductor_sim/actions/runs/44471869184 is still **FAILURE**. Its browser test compared a separately sampled selectedIndex with SVG current-marker coordinates while the 100 ms timer was allowed to advance between Playwright calls. No Kelvin numerical fault is demonstrated by this failure.

## Source and browser findings

The corrected source helper _freeze_actual_playback_frame first obtains the genuine selected index, ten visible science/world readouts and six SVG coordinate attributes **inside one synchronous JavaScript callback**. It captures all these values **before** issuing the ordinary slider input event, which stops the timer and redraws that same saved frame. The browser event loop cannot run a timer callback between those synchronous reads and the stop. The Python side rejects incorrect LIVE labels/coordinates independently of the post-redraw DOM, then the full paused scene is separately checked, including stability after an interval longer than 100 ms. Strict SI tolerances and the original student renderer remain unchanged. Source review found no blocking defect.

The reviewer separately performed exact-head native generation and standalone reference checks with:

- python -m tools.m38b_line_viewer_example
- python -m tools.m38a_line_reference
- python -m tools.m38b_line_view_reference
- python -m tools.check_m38b_line_browser

**Results:** 41/41 physical Kelvin saved states and 41/41 native/viewer reference rows independently checked. The original production Chromium checker accepted genuine JS-on frames, signed-current graph and real local u–w projection, the mobile 390 px layout, and the unmodified JS-disabled first frame. It recorded three actual playback witnesses [1,1,1], zero external HTTP requests and zero JavaScript errors. The displayed teacher hypothetical path remained clearly distinguished from the original workbook radial question. The local physical u–w basis and full world-xyz position/velocity/force labels were intact. The source example uses signed sphere-to-ground currents +8.94427190999916e-11 A at t=0 s, negative zero at t=2 s, and -8.94427190999916e-11 A at t=4 s.

## Two NEW reviewer-owned real live Play/freeze controls

The separate independent Python/Chromium probe captures an **unmodified running Play DOM** in its own single JavaScript callback before invoking the production freeze helper. It independently validates **all ten SI/world labels and six marker coordinates** against one genuine saved physical row, then confirms the official pause remains frozen for 240 ms and the full scene stays consistent. Restart/Play works across both controls.

| New independent control | Genuine live index | Helper frozen index | Physical time | Real signed current | Stability |
|---|---:|---:|---:|---:|---:|
| A | **1** | **1** | 0.1 s | +9.597811522581158e-11 A | 240 ms |
| B, beyond index 1 | **4** | **4** | 0.4 s | +1.1910088539397304e-10 A | 240 ms |

An additional independent noninterfering timer witness captured physical saved index progression **0 → 1 → 2 → 3 → 4** at successive actual presentation ticks. Measured intervals were **97.0, 109.2, and 96.8 ms**. This is real 100 ms Play, not a test-generated surrogate for motion. The original 41 state values were precomputed in Python, not simulated afresh inside JavaScript.

## Three NEW live pre-redraw adversarial refusals

To avoid a random subsequent playback tick repairing a hostile mutation, the reviewer used a real Play-advanced index **4** and deliberately stopped via the original slider event before injecting each visible forgery. Source/embedded and external SI data were not modified. Then the **production helper's own atomic LIVE pre-redraw snapshot** was invoked; a slider redraw would repair the display afterward, so a post-redraw-only check would have missed these failures.

1. Forged current-marker SVG attribute: **#m38b-current-marker.cy = 999**; marker visibly disappears from its true current curve. Required and observed rejection: **LIVE playback scene/current marker differs from genuine Kelvin frame: chart_y_px**.
2. Forged visible current text: **-9 A**. Required and observed rejection: **LIVE playback SI/world label differs from genuine Kelvin frame: current_label**.
3. Forged displayed physical world position: **(99,99,99) m**. Required and observed rejection: **LIVE playback SI/world label differs from genuine Kelvin frame: world_position_label**.

**All three were rejected for the intended original scientific reason before the input-event redraw could hide the forgery.** The authentic saved index and all restored post-pause physical values remained correct. Screenshot files of each forged science state are retained.

## Canonical HTML and no-JavaScript visual hostility

The reviewer reran the unchanged full production hostility checker. Its independently preserved artifact reports **26/26 actual Chromium HTML-only CSS/SVG attacks REFUSED**, zero unexpected acceptances, 41 physical states unchanged and exact HTML restoration.

An additional **unfamiliar** attack injected only a CSS filter on the displayed world position: **#m38b-world { filter: blur(8px) !important; }**. In actual JavaScript-disabled Chromium the computed style was **blur(8px)** and the physical XYZ readout was visibly obscured; screenshot retained. Native/external manifest and embedded SI data were unchanged. Calling the actual production browser verifier produced nonzero exit 1 with the intended message: **AssertionError: noncanonical visible HTML/CSS: source, signed SI, sphere, path, current-axis or physical projection differs from the verified native renderer**. The original HTML was restored byte-for-byte. Whole-page canonical regeneration is an integrity gate, not a third-party cryptographic signature.

## First-attempt honesty and evidence

**Do not rewrite the following reviewer-controlled failures as green:**

- **First review Actions attempt #44477888784 — FAILURE:** https://github.com/physicsvigilante/review_sandbox/actions/runs/44477888784 . The exact-head/tree, source scope, charter, 41-frame native reference and original real Chromium baseline PASSED. The novel reviewer probe was blocked by reviewer import-path setup (ModuleNotFoundError for tools). No new adversarial result was claimed from that attempt.
- **Second review Actions attempt #44478075901 — FAILURE:** https://github.com/physicsvigilante/review_sandbox/actions/runs/44478075901 . Fixed reviewer import path. New true-Play index 1 and index 4 probes and timer interval observations passed. The source correctly rejected the forged live marker, but the reviewer harness mistakenly asserted that its error string must contain the SVG attribute name **cy** instead of physical evidence key **chart_y_px**. This was a reviewer assertion error, not a source defect.
- **Third review Actions attempt #44478291686 — SUCCESS:** https://github.com/physicsvigilante/review_sandbox/actions/runs/44478291686 . After correcting **only the reviewer assertion** and keeping production exact HEAD/TREE unchanged, the full independent run passed: real source regeneration, SI/original page, new live Play/freeze, three live hostile refusals, one new no-JS CSS hostile refusal and all 26 preexisting hostiles.

The reviewer inspected genuine and forged real-browser screenshot images. Final artifact **#14506853780** contains exact source head/tree, diff, charter proof, PDF hashes, generated native physical JSON, viewer manifest, original and reviewer Chromium reports, actual screenshots, original 26 hostile refusals and first-run logs:

https://github.com/physicsvigilante/review_sandbox/actions/runs/44478291686/artifacts/14506853780

The earlier red runs and their separately retained artifacts remain visible. The workflow artifact's reviewer-first-run-probes.json metadata label is generic; the actual **reviewer attempt numbers** and their outcome are the three GitHub Actions runs above, not three alleged initial successes.

## Scope limit and final release verdict

This is a **narrow independent PASS for M38c browser-test synchronization and integrity**. It is **not** a fresh review of the unchanged M38a/M38b Kelvin laws, the old independently reviewed negative-q/translated 3D teacher case, every JEE problem, or all real FEMM5/3.10/3.12 jobs. The already independently reviewed original physics and unchanged blobs do not justify redoing that full work for a test-only timer correction; the verified 41-state regeneration, real Chromium and extra unfamiliar nonzero Play probes adequately target the new risk.

**No blocking defect found. Recommended independent decision: PASS.**

**No merge authorization.** Production PR #94 remains draft/unmerged and needs separate explicit owner approval. Only an expected-head guarded source merge followed by confirmation of **the exact reviewed native tree on main** and **all actual NEW main-push CI green** (especially the previously failing M38b Chromium workflow) completes the release. The historical main-push failure #44471869184 remains failed. M39a issue #95 is separate and must not be mixed into this maintenance correction.
