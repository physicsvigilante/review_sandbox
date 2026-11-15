# SIM_HEAT PR #13 — H2-01 focused viewer/evidence review request

- **projectId:** `sim_heat`
- **sourceRepo:** `physicsvigilante/sim_heat`
- **sourcePR:** https://github.com/physicsvigilante/sim_heat/pull/13 (draft, unmerged).
- **baseSha:** `ecebc38dd3f6eaffd297bd3df97a0883e591c6ac` (owner-approved H2-00 integration merge).
- **headSha:** `e8449989ba55a972976ebba7e9708bc4e2351a18` (pin exact source, do not review floating head).
- **sourceTreeSha:** `c342ace7233dd112fa494be91785f79f23debeca`.
- **reviewClass:** **R1, focused independent-in-context review required**, because existing physical evidence, heat-flow signs, energy units and qualification statuses are displayed to users; no physics, measurement, simulation or checker semantics were changed.
- **scope:** a single static read-only viewer of existing developer-authored native bridge results, not a generic network authoring engine or new native simulation.
- **known limitations:** the included preview has 23 samples; full 2001-sample history requires user to import original archived `normalized.csv`. Source artifact availability may expire. Browser data are historical `diagnostic_only` / `nativeQualified=false`, not independently authenticated measurements. No classroom-effectiveness, general topology visualization or unfamiliar-author C1 success is claimed.
- **report destination:** `projects/sim_heat/pr-13/reviews/review-01-chat-b.md`. Chat B only; never have Chat A prewrite its findings.
- **review status:** `awaiting-review`, no merge approval.

## Source and physical meaning

Read source [AGENTS.md](https://github.com/physicsvigilante/sim_heat/blob/e8449989ba55a972976ebba7e9708bc4e2351a18/AGENTS.md), [H2-01 scope](https://github.com/physicsvigilante/sim_heat/blob/e8449989ba55a972976ebba7e9708bc4e2351a18/docs/H2_01_VIEWER_SCOPE.md), [viewer README](https://github.com/physicsvigilante/sim_heat/blob/e8449989ba55a972976ebba7e9708bc4e2351a18/viewer/README.md), `viewer/index.html`, `viewer/trace.mjs`, `viewer/data/bridge-preview.json`, `viewer/tests/trace.test.mjs`, `viewer/tests/browser_smoke.py` and exact PR diff.

The native bridge topology has fixed-temperature reservoirs at 353.15 and 283.15 K, two uniform-temperature bodies and five storage-free conductors. The `bridge.Q_flow` channel is **positive left → right**, negative the reverse. Saved native samples are `-0.009653756395368874 W` at 1,720 s and `+0.005807881808732419 W` at 1,730 s. This brackets, but does not measure, an exact unsampled crossing time. Temperatures are K; body `dU` is cumulative J relative to initial values; reservoir `Q_to_network` values are instantaneous W, not energy. The logical diagram cannot be treated as real-world geometry.

The 23-sample preview is sourced from **the historical** [OpenModelica bridge run 43699424883](https://github.com/physicsvigilante/sim_heat/actions/runs/43699424883), source commit `b3779603563db4b26aeef8c2dd552965698deb4f`, artifact 14155084346, ZIP SHA-256 `f16975a25eea79f61f7819fb9e704ab04a33630044a51a0d062b8399c1c9ce38`; original `normalized.csv` SHA-256 `4b1a822680c03742e3031f5be653b48e7dd736613be355796862de483c0e39fe` and raw MAT SHA `e1da06d7223dd271317881b2d737b73c40ec643a8d533568bf7ef3bfbb5443a9`. Original run had one build/launch and 98/98 diagnostic physical/numerical checks passing, with `nativeQualified=false`. No new native execution here. Historic MATv4 v1 sidecar's misleading channel-"independence" field is not copied into the viewer.

Only **8 newly added files** relative to merge base; `h1/`, `tools/`, `experiments/`, original source PDF and existing CI remain unchanged. Only new CI workflow is `.github/workflows/h2-viewer-ci.yml`, an offline Python/Node/browser job with no OMC.

## Exact current-head test and visual evidence

**Final CI:** https://github.com/physicsvigilante/sim_heat/actions/runs/43736122931 — **SUCCESS** on exact source SHA `e8449989ba55a972976ebba7e9708bc4e2351a18`, run attempt 1.

- 151/151 existing H1 offline tests, 4/4 analytical arithmetic tests and 7/7 new viewer unit tests PASS.
- Real headless Chromium desktop and mobile smoke PASS: preview source pin, signed arrows/flow reversal, keyboard slider, play/pause, jump, wrong-file SHA refusal, mobile width, no JS page errors.
- Artifact [14169479149](https://github.com/physicsvigilante/sim_heat/actions/runs/43736122931/artifacts/14169479149), ZIP SHA-256 `f5100b7f9ab2ddb2e8634eda1b11d4a3f9b1d31c67031aa59c0ebf35c91bf640`, 669,621 bytes. Contains clean browser screenshot `bridge-desktop.png`, **separate SHA-refusal** screenshot `bridge-desktop-refusal.png`, source identity/hash manifest, browser logs, H1/analytical/Node tests, and dependency versions.
- Chat A downloaded this artifact and verified full ZIP SHA/CRC, recorded head SHA and screenshot file presence; browser smoke reports PASS. This is **author CI evidence**, not a Chat B independently driven browser.
- The initial [failed CI run 43735810229](https://github.com/physicsvigilante/sim_heat/actions/runs/43735810229) passed H1/math but a new viewer negative fixture incorrectly required a sample validator to catch an isolated numeric mutation that is actually caught by the Git blob integrity check. The fixture was corrected to mutate the physical sign-reversal bracket, preserving original failure evidence. [Second CI 43735933432](https://github.com/physicsvigilante/sim_heat/actions/runs/43735933432) passed. Final source screenshot capture was split before/after the deliberate file refusal; no acceptance threshold or physics logic changed.

## High-value independent reviewer questions

1. **Native-source authenticity:** With the original artifact, check that all 23 numeric preview rows match the corresponding time-indexed native `normalized.csv` channels; the viewer's embedded Git blob source pin matches the bytes. Confirm no hand-fitted, interpolated, guessed or silently rounded physics data. If the artifact is inaccessible, disclose this rather than claim an independent source comparison.
2. **Flow orientation and topology:** Check all five signed arrows and labels against the authored rod port_a/port_b connections; test initial negative flow and 1,730 s positive flow with real UI interaction. Check there is no implied physical geometry.
3. **Truthful units and qualification:** Body energy changes are J and reservoir power is W; no invalid J/W sum or manufactured conservation verdict; `nativeQualified=false` / `diagnostic_only` accurately displayed, historic MATv4 v1 misleading flag not reused.
4. **Refusal and file trust:** A changed preview byte, a missing channel, altered sample time, nonfinite value, false qualification, wrong imported full CSV hash, and changed duplicate terminal sample must refuse. Full import is accepted **only** when exact byte-level original SHA matches, and the browser does not upload the file.
5. **Browser and accessibility:** Inspect the screenshot and if able drive the page in a real browser: desktop/mobile, keyboard range, play/pause, reversal jump, color-independent text direction, missing-data state, and responsive layout. Record real browser tests separately from read-only screenshot inspection.
6. **Scope and risk:** Verify no new physical law, MAT adapter/checker edit, source-data meaning, or native compilation. Any genuine evidence-semantics changes require R2 escalation; otherwise a focused R1 report is sufficient.

## Verdict and handoff

Use [REVIEW-TEMPLATE.md](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-TEMPLATE.md); report separate source interpretation, numerical/physical correctness, historical native coverage, evidence integrity, educational usefulness and answer completeness. Give a scoped `pass`, `changes-requested` or `insufficient-evidence` with source paths, reproducible inputs and exact evidence for each finding. Distinguish source/CI inspection from any new actual execution.

Write **a new unique Chat B file** at `projects/sim_heat/pr-13/reviews/review-01-chat-b.md` directly in the central repository or in a review-only PR. Never overwrite historical reports, modify/merge source PR #13, assert a different independent model family or human expertise, or broaden the simulation budget. The owner will say "Review complete" in Chat A, which fetches this GitHub report directly; merge requires separate owner approval even if review passes.