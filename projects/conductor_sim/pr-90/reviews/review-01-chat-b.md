# conductor_sim PR #90 — independent Chat B review #01

**Verdict: CHANGES REQUESTED.** The prescribed-speed Kelvin physics passes the new independent numerical checks, and all **26 exact-head production workflows are terminal SUCCESS**. The public viewer nevertheless accepts Boolean-for-number sample forgeries, and the release browser checker accepts scientifically false fallback output, an attempted unmonitored request, broken playback and a hidden mobile current. The genuine page also omits the actual teacher-chosen input magnitudes from its visible numerical attribution.

**Reviewer:** GPT-6 Astra Pro, independent Chat B, 18 November 2026. This is the one consolidated review requested by [REVIEWER-PROMPT-01](../REVIEWER-PROMPT-01.md) and [REQUEST-01](../REQUEST-01.md), not another broad review of M37a/M16a/FEMM. Production was not edited, marked ready, or merged.

## 1. Source identity and scope

| Gate | Independently verified result |
| --- | --- |
| Production | [physicsvigilante/conductor_sim PR #90](https://github.com/physicsvigilante/conductor_sim/pull/90), **OPEN / DRAFT / UNMERGED** |
| Exact HEAD | `155b0544684d3d880a83a661cc8e14a0ce22f26b` |
| Native Git TREE | `f48f54b8c49217b7c66179fe014b6fab1ea4dc4d` |
| Released base | `133acf97a123e6167aeaac3ca2a2b2094af1d36f` |
| Preregistered charter | `24300b2050430634532bb1978cba38eb7d3f39e4`; direct parent is released base, ancestor of candidate; charter blob unchanged |
| Original PDF SHA-256 | `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d` |
| Source worktree | Tracked production files unchanged after execution |
| Live identity and CI | Checked at the beginning and end of both reviewer executions; no moved HEAD or tree |

Fresh source checkout and native `git rev-parse HEAD^{tree}` were used, not merely a PR description. The actual ten-file diff is exactly `.github/workflows/m37b-source-current.yml`, `docs/m37b.md`, `docs/m37b_charter.md`, `src/conductor_sim/__init__.py`, `src/conductor_sim/prescribed_ground_wire.py`, `src/conductor_sim/prescribed_wire_viewer.py`, `tests/test_m37b_constant_speed_jee.py`, `tools/check_m37b_prescribed_browser.py`, `tools/m37b_source_approach.py`, and `tools/m37b_source_reference.py`. Original PDFs, the M37a native observer, M16a integrator, Kelvin/FEMM backends and historical viewers are outside the delta.

The hash-qualified PDF's physical pages **8 and 17** were rendered and visually inspected. Q21 is the workbook's positive external charge approaching a grounded sphere at constant small speed; the key gives **(1),(3)**. Constant speed is represented as externally prescribed motion, not falsely presented as a freely accelerating particle. This is **one workbook apparatus**, one teacher numerical illustration and 31 observations—not 31 problems or an asserted official JEE examination question.

## 2. Executed evidence and reviewer correction

The [first source-pinned execution, run 44352091700](https://github.com/physicsvigilante/review_sandbox/actions/runs/44352091700), used Python 3.12.16, Playwright 1.57.0 and actual Chromium 143.0.7499.4 with `set -euo pipefail`. Its unchanged raw result is **105 PASS, 14 FAIL, 1 ERROR** across 120 records. The first workflow remains **FAILURE**.

The ERROR belongs to the reviewer: `inner_text()` was used on SVG `<text>`, where Playwright requires `text_content()`. The [scoped continuation, run 44353528122](https://github.com/physicsvigilante/review_sandbox/actions/runs/44353528122), corrected only that assertion and executed the same four reviewer browser functions against the exact first-run HTML/JSON. It passed the genuine desktop/mobile/no-JavaScript checks and independently demonstrated that the accepted broken-play attack remains at index zero. **Its SUCCESS is not an overall PASS for the candidate and does not erase any first-run failure.** It did not rerun the physics or modify production.

Local clone DNS failure and a local Chromium `ERR_BLOCKED_BY_ADMINISTRATOR` file-navigation failure were infrastructure limitations, not candidate failures. The actual scientific and browser executions ran on isolated GitHub runners.

### Independent numerical and authoring results

The reviewer-owned [Kelvin oracle](chat_b_kelvin_oracle.py) imports no production code. It obtains force from the image charge and image separation, and mechanical energy from **one-half** the source charge times induced potential. It checks timestamps, physical positions/velocities, distance, net induced charge, both current signs, force and energy. In addition, each sampled state was checked using native shifted static Kelvin solves for `-dQ/dt`.

| Reviewer-authored scenario | Native observed states | Extra shifted native solves | Result |
| --- | ---: | ---: | --- |
| Original teacher illustration | 31 | 62 | PASS |
| Negative charge, inward, translated oblique axis, changed permittivity | 13 | 26 | PASS |
| Positive charge, outward, translated oblique axis, changed permittivity | 17 | 34 | PASS |
| Negative charge, outward | 9 | 18 | PASS |
| Near-surface but guard-safe approach | 11 | 22 | PASS |
| Explicit legacy coordinate-normalized model | 7 | 14 | PASS |
| **Total** | **88** | **176** | **All PASS** |

The maximum relative native finite-difference current discrepancy was `5.265143876442835e-11` for the original example and `1.7758654546895514e-9` across all six cases. The original current increases from approximately `4.4444444444e-11 A` at `t=0`, `d=0.30 m`, to `1.2345679012e-10 A` at `t=3 s`, `d=0.18 m`, with conventional current sphere→ground. The opposite terminal current has the opposite sign.

All **47** independently selected invalid raw-input/spec/domain cases were refused: scalar and raw-coordinate Booleans, nonfinite values, invalid counts/durations/speeds/guards, zero charge, extra sources/conductors, wrong conductor constraints, hollow metal, inside/surface/guard-crossing configurations. The legacy constructor's Boolean-to-float coordinate normalization was explicitly treated as unrecoverable raw-type information, not falsely certified as original raw authoring. All four teacher-hypothetical variants rendered, and false original-role assignments were refused.

The source-specific JSON checker genuinely imports only `__future__`, `argparse`, `json`, `math`, `pathlib`. It accepted the actual saved source output and rejected **29 of 30** reviewer-authored mutations covering signs, parameters, time/position, force, the energy half-factor, units, options, Boolean counts, extra claims, attribution and display geometry. The remaining accepted case is the nonblocking integer-type inconsistency C1 below.

### Genuine browser behavior

After the reviewer-only SVG correction, independent Chromium checks passed on desktop, 360-pixel mobile and JavaScript-disabled pages. They checked every one of the **31 drawn curve points**, sphere/charge geometry, all five first-state readouts and the current marker; selected indices `0,2,8,16,23,29,30` on script-enabled pages; actual play/restart; mobile width; and disabled fallback controls. Expected numbers were recomputed by the reviewer's oracle, not trusted solely because they matched the embedded readouts. No HTTP requests or JavaScript errors were observed on these genuine pages.

The genuine source identity and generic teacher-only banner are visible. **The actual q/R/v magnitudes are not visible; F5 remains.**

## 3. Required corrections

All five findings below are **P2: required for the stated bounded release/integrity contract**. None is evidence that the unchanged Kelvin law is wrong. F2–F4 are demonstrated weaknesses of the release checker, not claims that the current genuine page itself displays the injected values, makes the injected request, or has broken playback.

### F1 — Native typed sample equality accepts Boolean forgeries

**Location:** `src/conductor_sim/prescribed_wire_viewer.py:viewer_manifest`, especially `trace.samples != expected.samples`; sample types in `prescribed_ground_wire.py`.

The viewer recomputes native samples but relies on dataclass value equality. Python considers `False == 0`, so that is not strict typed validation. Four independently constructed first-sample replacements were accepted and serialized: `time_s=False`, `index=False`, `source_position_m=(False,0.,.3)`, and a force vector with `False` replacing its zero component. The corresponding exported JSON contains Booleans in scientific numeric fields. Incorrect nonzero current and energy controls were correctly refused.

**Correction:** Validate every sample's index, scalar and vector component types, finiteness and container structure before comparison/serialization. Reject Boolean numerical fields explicitly; retain fresh native recomputation. Add regressions for zero-valued components and timestamps, not only numerically different values. Do not modify legacy model coercion to solve this new boundary issue.

**Evidence:** `accepted-typed-forgeries/` and `typed-native-forgery-*` records in the first artifact.

### F2 — False no-JavaScript scientific output passes the browser release checker

**Location:** `tools/check_m37b_prescribed_browser.py:check`, JavaScript-disabled fallback block.

Four HTML-only mutations left the saved JSON and embedded physical dataset genuine but changed the fallback to display **91 s** instead of 0 s, **9 m** instead of 0.3 m, **7 A** for the opposite current instead of approximately `-4.4444444444e-11 A`, or chart-marker `cx=400` instead of 61. **All four were accepted.** Separate reviewer DOM records and screenshots confirm the false fallback states. The script-enabled page's `show(0)` repairs these values, masking the corruption from main-page tests.

**Correction:** Check the no-JavaScript DOM itself against independent first-state expectations: all five readouts, source/teacher attribution, complete curve, sphere/charge/sign and marker geometry, with controls disabled. Add each accepted attack as a regression. Do not regard a correct embedded payload or a screenshot's existence as proof of correct visible fallback values.

### F3 — Offline/no-error claims omit mobile and no-JavaScript contexts

**Location:** `tools/check_m37b_prescribed_browser.py:check`, request/error listeners and later page/context creation.

Listeners attach only to the first page. A reviewer-inserted `<noscript>` image attempted a request to `https://review-only.invalid/pr90-probe`. The independent context-level observer recorded and blocked it, while the production checker returned success with **`external_http_requests: 0`**. No external data transfer was allowed; the defect is a falsely clean report despite an attempted prohibited request.

**Correction:** Observe requests and JavaScript errors across every browser context/page, including mobile and disabled-JavaScript pages, before navigation. Block attempted HTTP(S) while recording it, then fail the checker when any attempt occurs. Include a no-JavaScript-only request regression and a mobile-only error/request control. Scope report fields to what is actually observed.

### F4 — Playback and mobile readout visibility are not release-tested

**Location:** `tools/check_m37b_prescribed_browser.py:check`, control checks and mobile block.

The checker never clicks Play. Changing `i++` to `i+=0` was accepted; the reviewer then clicked the actual button and confirmed the selected index remained **0 after 550 ms**. Separately, a mobile-only rule hiding `#m37b-current` was accepted because the mobile check verifies width, not required content visibility. The hostile DOM record reports that readout invisible.

**Correction:** Exercise real playback, verify advancement to a genuine stored index and synchronized readouts/markers, then verify restart/manual selection and termination. At mobile size, explicitly test required source/teacher claims, all readouts and controls for visibility and correct values, not just absence of horizontal overflow. Preserve genuine desktop/mobile controls as positive controls.

### F5 — Validated teacher numerical inputs are not rendered visibly

**Location:** `src/conductor_sim/prescribed_wire_viewer.py:render_prescribed_ground_wire`, plus the browser check's teacher-attribution assertion.

The metadata's concrete numerical caption is validated but never rendered in the body. Students see a generic teacher-chosen banner and induced-Q/current readouts, but not the actual input magnitudes **q=+1 nC, R=0.10 m and inward speed=0.04 m/s**. Those values exist only in the embedded JSON. This does not meet the prompt's visible teacher-numerical interpretation. The tester also accepted an inserted visible caption falsely claiming q=9 C, R=7 m, d0=9 m and v=3 m/s, showing that generic banner matching does not bind numerical claims.

**Correction:** Render a defined, escaped, canonical teacher-input region bound to the qualified trace: q, R, initial distance, signed/inward speed, duration, permittivity and relevant guard/count. Keep symbolic workbook givens visibly separate. For teacher hypotheticals, display actual authored values and the hypothetical role. Check this region against independent SI values in desktop/mobile/no-JavaScript modes, including stale/conflicting numerical-caption regressions within the defined scientific-claim regions.

### C1 — Nonblocking strict-page-type inconsistency

`tools/m37b_source_reference.py:check` accepts `physical_pdf_page=8.0`, while `viewer_manifest` requires exact integer 8. This still names the correct physical page and is **not a wrong-source or wrong-physics finding**. Align the types and add a small schema regression when touching the checker. **P3; not an independent release blocker.** This is one of the 14 raw failed challenge records, not a sixth major defect.

### Consolidated HTML-only outcomes

**Rejected, 6/14:** false visible original statement; wrong sphere radius; wrong charge sign; altered polyline point; altered embedded physical JSON; hidden generic teacher attribution.

**Accepted, 8/14:** false no-JavaScript time, distance, opposite current and marker; no-JavaScript-only request; broken Play; hidden mobile current; stale visible numerical caption. All hostile HTML, unchanged sidecar JSON, generated checker reports, screenshots and independent DOM/request observations are retained. These are real browser executions, not inferred results from source inspection.

## 4. Full exact-head production CI

Both reviewer executions independently queried all workflows for the exact candidate SHA, with no pending, cancelled or failed runs: **24 pull-request + 2 push = 26 SUCCESS**. The dedicated M37b job steps for Python 3.10, Python 3.12 and Chromium were also inspected. The actual FEMM5 workflow's build, real-solver tests and Chromium export steps were verified successful; FEMM was not redundantly rerun by this reviewer.

All rows below are complete **SUCCESS** on `155b0544684d3d880a83a661cc8e14a0ce22f26b`:

| Run ID | Event | Workflow |
| --- | --- | --- |
| 44343507219 | PR | M35a audit and dependency-aware scientific regression |
| 44343507160 | PR | M21d distant connected spheres |
| 44343507215 | PR | M34b independent certified incremental world fork physics |
| 44343507125 | PR | M21e composed electric and gravity review |
| 44343506987 | PR | FEMM 5 real-solver validation |
| 44343506532 | PR | M36d true solid conductor source JEE physics and Chromium |
| 44343507015 | PR | M33b native graph-world event inquiries and independent SI |
| 44343506746 | PR | M19a prescribed fields and test-charge physics |
| 44343506976 | PR | M18b held-source viewer and correctness |
| 44343506508 | PR | M15c authoring and browser acceptance |
| 44343506853 | PR | M37a grounded-sphere wire-current science and SI export audit |
| 44343506596 | PR | M17c motion authoring and review |
| 44343506959 | PR | M19e source identity and world-oriented ring viewer |
| 44343507025 | PR | M36e actual JEE solid-source answers and Chromium integrity |
| 44343506522 | PR | M20a paired prescribed-field exploration |
| 44343506626 | PR | M19b fixed-source offline viewer and physics integrity |
| 44343507044 | PR | Visualization and source checks |
| 44343506933 | PR | Python checks |
| 44343506548 | PR | M18c held-source authoring and independent physics |
| 44343506644 | PR | M36c real conductor-JEE source physics and Chromium |
| 44343506932 | PR | M36b real source-JEE replays, independent physics and Chromium |
| 44343506560 | PR | M37b original workbook constant-speed physics and Chromium |
| 44343506512 | PR | M22a structural composability review |
| 44343507004 | PR | M21c composite symmetry review |
| 44343488940 | Push | Python checks |
| 44343488972 | Push | M37b original workbook constant-speed physics and Chromium |

The raw CI inventories include full run URLs and head SHAs. Green existing CI does not negate the newly demonstrated accepted forgeries. Earlier development failures and the first reviewer failure remain historical failures.

## 5. Retained evidence and limits

[Attributed machine-readable summary](evidence/review-01-summary.json) retains exact identities, counts, attack outcomes and file/archive hashes. Reviewer scripts are [main suite](chat_b_review_01.py), [independent oracle](chat_b_kelvin_oracle.py), and [scoped browser continuation](browser_continuation_01.py). Their source-pinned workflows are retained on the review branch; all production access was read-only.

**First raw artifact:** [run 44352091700 / artifact 14449870049](https://github.com/physicsvigilante/review_sandbox/actions/runs/44352091700/artifacts/14449870049), SHA-256 `ed84ec82b5e4c6309c3b0e946fa5766ee582b5697ea37f3f4b8220bd2a7ca088`. Includes the unmodified first log/results, native scenarios, 30 JSON attacks, 14 HTML attacks, screenshots, original PDF-page renders, source/CI identities and dependency versions.

**Scoped continuation artifact:** [run 44353528122 / artifact 14449442255](https://github.com/physicsvigilante/review_sandbox/actions/runs/44353528122/artifacts/14449442255), SHA-256 `c3e46076bb012f5b0e5e61acc0adf77a1e9e6e29d237770069051cf137df3d60`. Includes independent desktop/mobile/no-JavaScript screenshots, corrected baseline results, broken-play confirmation and fresh live CI/source checks. Both downloaded archive hashes were independently checked. Actions artifacts currently expire **18 December 2026**; scripts, report and summary are Git-retained. Artifact retention is not represented as permanent storage.

This review establishes bounded ideal quasistatic grounded-sphere/prescribed-radial behavior in the tested domain. It does not certify arbitrary Maxwell transients, wire resistance/current density, actuator work, heating, microscopic drift, free trajectories, arbitrary topologies, cryptographic authenticity of exported JSON, or broader workbook coverage. The teacher numerical choices are not printed workbook numerical givens.

## 6. Disposition

**Keep PR #90 DRAFT and UNMERGED.** Correct F1–F5 narrowly, retain these first-attempt inputs/results, and request a targeted continuation on a newly pinned HEAD/TREE. Replay the accepted forgeries and genuine controls, preserve native physics and legacy behavior, and recheck exact-head full CI. There is no evidence here requiring a new Kelvin solver, new physical law, M16a replacement, or another broad architecture review. Even a later PASS would require separate explicit owner merge approval.
