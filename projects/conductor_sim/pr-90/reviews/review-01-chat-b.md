# Independent Chat B review 01 — conductor_sim M37b / PR #90

**Verdict: CHANGES REQUESTED (one bounded browser release-checker integrity blocker).**

**Reviewer:** ChatGPT GPT-6, independently authored tests in this conversation, 2026-11-18 UTC.
**Production PR:** https://github.com/physicsvigilante/conductor_sim/pull/90
**Exact source HEAD:** `155b0544684d3d880a83a661cc8e14a0ce22f26b`
**Native Git TREE:** `f48f54b8c49217b7c66179fe014b6fab1ea4dc4d`
**Base:** M37a released commit `133acf97a123e6167aeaac3ca2a2b2094af1d36f`, tree `c728041ca5118013c6979d120c8805f31ee09fa0`.
**Original workbook PDF SHA256:** `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d`.
**Pre-implementation charter commit:** `24300b2050430634532bb1978cba38eb7d3f39e4`.

No changes were made to the production PR or production branch. The draft PR remains open, draft and unmerged. This report is not owner merge approval.

## Scope / independence

Read full REQUEST-01, REVIEWER-PROMPT-01, charter, ten changed file paths, M37b protocol, source-specific validator, viewer, browser checker and relevant M37a observer/M16a context. Confirmed only 10 declared PR files change; no original PDFs, previously qualified Kelvin solver, FEMM or M16a implementation were changed. Verified the live production PR HEAD and its Git commit's native tree.

**Developer exact-head CI:** independently fetched GitHub Actions' live head-SHA-filtered runs. **26 of 26** were **terminal SUCCESS**, all for `155b054...`, including Python 3.10/3.12, actual FEMM5, historical source/visualization checks and M37b dedicated browser/source jobs. This is developer evidence, not an independent PASS.

Downloaded the **actual** PR-run artifact `m37b-original-source-chromium` (artifact ID `14445071517`, workflow `44343506560`) containing the 31-state JSON, generated HTML, original browser screenshots, native SI report, head/tree records. One provenance nuance: the developer pull-request job's **checkout** file records GitHub's synthetic PR merge `240c38bbddde3e3c518716b82af3d17544ecfdc7`, not candidate `155b054...`. Its recorded **Git TREE is identical** to the candidate tree `f48f...`. Thus the run's source *content* is pinned by tree equality, but its checkout HEAD file should not be described as the literal candidate commit. The independent review workflow checks out the literal candidate SHA.

Independent review workflow (reviewer-owned; production unchanged):
https://github.com/physicsvigilante/review_sandbox/actions/runs/44353866101
Reviewer-only native tests:
`projects/conductor_sim/pr-90/reviews/independent-native-probes-chat-b.py`
A separate real Chromium/stdlib scientific probe was also executed locally against the authentic exact-tree output. Local Chromium `file://` navigation is disallowed in that environment, so the identical generated HTML was loaded using Playwright's `set_content`; this is real Chromium rendering and DOM execution, **not** a claim of successful file URL navigation.

## Source interpretation / physical correctness

The unchanged original workbook physical p8 **Multiple Correct Q21** describes one positive charge approaching one grounded metallic sphere with an **externally maintained constant small inward speed**; p17 key **(1),(3)**. The source supplies symbolic conditions, **not** q=1nC, R=.10m, d0=.30m, v=.04m/s or T=3s. These values are clearly teacher chosen. This is one original apparatus, not 31 source problems or an asserted official JEE past-paper question.

Independently recomputed **all 31 genuine saved time samples** (time, fixed-speed separation, position, induced Q, both signed currents, force vector, mechanical energy including its essential half factor, SI readouts, plot and scene positions) using a separately authored stdlib Kelvin image-charge calculation with **no production physics imports**. All 31 pass. Five independent finite differences of separate shifted Kelvin charge states reproduce the analytic current within floating-point tolerances. Concrete example:

| time | distance | expected conventional sphere→ground current |
|---|---|---|
| 0 s | .30 m | +4.4444444444e-11 A |
| 1.5 s | .24 m | +6.9444444444e-11 A |
| 3 s | .18 m | +1.2345679012e-10 A |

`Q=-qR/d`, `I=-qRv_r/d²` and `U=-kq²R/[2(d²-R²)]` match the output. Constant radial speed is *prescribed*, not integrated free M16a motion; the source's positive/inward case necessarily has increasing positive conventional current sphere→ground. The M37b public raw-SI factory rejects Booleans and nonfinite source/centre coordinates and scalar parameters before historical constructors coerce them. Such coercion cannot retroactively be detected in preconstructed older models; the implementation documents this fact without falsely attesting original raw types.

The local independently authored JSON oracle rejected **27/27** unfamiliar data and provenance mutations (q, R, eps, geometry, timestamps, signs, force, half-energy, units, Boolean source metadata, wrong answer choices, extra false claims, plot readouts and more). The production source-specific standalone checker was read in full; it has stdlib-only imports and a tight dataset domain.

## Actual browser verification

The authentic offline HTML passed independent Chromium checks: correct visible workbook/teacher split, all **31 drawn polyline points**, fixed sphere radius/proportion, charge sign, precomputed marker positions, seven selected real frames (0,3,10,15,22,29,30), t/d/Q/I/opposite-current readouts, restart, playback, a **390px mobile viewport**, and a meaningful JavaScript-disabled original first frame with inert controls. No external HTTP request or JS pageerror occurred for the baseline. Independently challenged **11 HTML-only modifications**: visible false workbook claim, false numerical attribution, graph points, sphere radius, charge sign, first-frame current/time, embedded JSON, hidden teacher attribution and an unauthorized request. The *reviewer-owned comparison harness* caught all 11. This does **not** imply the production browser checker catches all 11.

### CR-01 — release-blocking no-JavaScript HTML integrity blind spot

**Affected production file:** `tools/check_m37b_prescribed_browser.py`.

The release checker validates original rendered SVG and selected numbers after script-enabled `show(0)` has already replaced them from embedded JSON. The second **JavaScript-disabled** pass only checks the source exists, a noscript legend, disabled controls and initial Q/current. It omits the first-frame marker and point geometry, time, distance, opposite current, and other visible static physical claims.

**Actual independent Chromium reproducer:** change **only the HTML** initial `<circle id="m37b-current-marker" cx="61"...>` to `cx="500"`; leave the authentic JSON and JS unchanged. In script-disabled Chromium the chart marker is indeed at x=500 while the correct physics-based first point is at x=61. In script-enabled Chromium `show(0)` silently resets it to x=61. The existing production browser checker does not independently examine the initial no-JS marker and therefore can accept a false no-JS first frame. The exact same mechanism can conceal altered static initial time/distance/opposite-current labels. A focused same-repo reproducer is also available at `projects/conductor_sim/pr-90/reviews/reproduce-nojs-checker-gap.py`; independent real HTML inspection and script-on/off Chromium behaviour agree.

**Required correction:** in `tools/check_m37b_prescribed_browser.py`, require that the **no-JS first frame** matches independently verified saved JSON for its time, separation, net induced Q, both signed currents, charge marker x, sign position, current marker x/y, sphere fixed geometry, and original provenance. Add HTML-only hostile regression tests for initial marker and static labels that must fail the checker while untouched HTML still passes. Prefer checking static HTML both before JS initialization and with JS disabled so a script's auto-repair cannot disguise a tampered fallback. Preserve actual hostile screenshots and first-attempt logs. This is a narrow **browser verification** fix; no changed Kelvin law or new broad M37a review is justified.

### NR-01 — synthetic PR checkout provenance (non-blocking if tree equality is retained)

Production pull_request workflow artifacts record HEAD `240c38...` (synthetic merge) while the PR HEAD is `155b054...`. Native Git TREE is exactly `f48f...` for both. Report the distinction honestly; optionally use explicit PR-head checkout if literal HEAD assertions are desired. The reviewer workflow uses the literal commit as a further check. This does not invalidate source-equivalent scientific calculations.

## Qualification ceiling

This is one symbolic workbook apparatus with 31 **teacher-authored physical observations**, and a reusable one-sphere/one-charge externally prescribed **radial** protocol. It does not implement Maxwell transients, resistive or heating-wire dynamics, electron drift, automatic PDF parsing or general nonradial mechanics. These limits are appropriate and explicit.

## Decision and follow-up

**CHANGES REQUESTED — bounded correction CR-01.** The original physical series and full developer CI are scientifically consistent in the inspected source-equivalent dataset, but the release browser checker has a demonstrable accepted-forgery blind spot in its no-JS fallback. Do not merge, do not mark PR #90 ready, and do not treat 26/26 developer green jobs as an independent PASS. Correct that focused checker gap, add negative regression evidence, run full exact-head CI, and request a targeted fresh reviewer verification of the changed browser validator; unchanged M37a Kelvin and M16a need not be re-reviewed.

*Independent native reviewer-run detail is separately tracked by the linked exact-commit review_sandbox workflow. A job still in progress does not count as completed new native execution and must not be silently reported as PASS.*
