# Opticsim PR #133 — first native-free JEE apparent-depth engine capability

**2026-11-18: Draft implementation; final independent source review PENDING. No PR merged or released.**

[Draft PR #133](https://github.com/physicsvigilante/opticsim/pull/133) implements candidate A of the independently R2-reviewed [design #132](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-132/reviews/review-02-chat-b.md). It computes an explicitly **conditional near-normal apparent-depth** relation from reduced facts without running PhyDemo or inventing an observer eye/image. Candidate B native finite detector-window research remains separate.

| Item | Exact source identity |
| --- | --- |
| Source HEAD | 5dc594400a3c8d537c180d1162379b5bfda5e3b1 |
| Source tree | d02d23e598d8211830928414fb5a1ae232d450f7 |
| Synthetic PR merge | d3dda63d6d079048e8b144d89ce6dcd92f8710b2 |
| Synthetic tree | d02d23e598d8211830928414fb5a1ae232d450f7 (identical) |
| Production base main | d3509e82fb65d81aabe336666851f8f2962623f4 |
| Diff vs main | 4 files: new pure evaluator, changed planner, new tests, example JSON |
| Frozen CLI | scripts/run-problem.mjs unchanged, blob 2efecbf3eddcd9322782cc1667b02fe495fd4fa8 |

**Real first CI failure preserved:** initial source 693f84a20899c55129cf4163af54488411108d61 ran Node24 802 tests, **801 pass, 1 fail** because a changed historically frozen scripts/run-problem.mjs failed test/detector-hit-transfer.test.mjs. Builder restored exact frozen bytes and moved the new verification-refusal signal to the new planner result and coverage reducer. The final build needs its own exact-head CI before being called validated. See [REQUEST.md](REQUEST.md).

**Open questions for independent reviewer:** formula, 5°+1% conditional regime, missing/invalid/scope refusal distinctions, near-grazing/critical refusals, zero-native CLI persistence, resultCoverage's new status blocked-native-verification while leaving old statuses unchanged, and raw input SHA. No new PhyDemo path, scene schema, browser UI or pupil model is authorized.

[Copy-ready Chat B prompt](REVIEWER-PROMPT-01.md) · [Detailed request](REQUEST.md).

**Independent source/physics review pending.** CI progress and final evidence must be rechecked at the actual source HEAD. Passing existing native/Chrome regressions does not establish an apparent-depth native or browser image feature. Main remains unchanged/unprotected (issue #123) and held #129/#131/v14–v19 PRs remain separate.

## Exact corrected-source CI completed (builder) — 18 November 2026

**Final/source HEAD `5dc594400a3c8d537c180d1162379b5bfda5e3b1`, Git tree `d02d23e598d8211830928414fb5a1ae232d450f7`**, identical to synthetic merge commit `d3dda63d6d079048e8b144d89ce6dcd92f8710b2` tree. GitHub CI checkout on Node **24.19.0** and pinned native PhyDemo **811f508d2b070898c241a568b0c167dcb8645251** executed **802/802 Node tests PASS**, including all **12 new candidate-A tests**. [Full planar native/browser CI #44156145655](https://github.com/physicsvigilante/opticsim/actions/runs/44156145655) records exact-head output.

**11/11 standard GitHub Actions workflow conclusions SUCCESS**, with one targeted successful retry documented below. All older native/Chrome regression checks passed; **there is no new candidate-A browser simulator or native image**.

**Preserved failures and repairs, not relabelled:** (1) Initial source HEAD `693f84a20899c55129cf4163af54488411108d61` had one real Node historical-SHA freeze failure (801/802 pass) because the original attempt modified a protected `scripts/run-problem.mjs`. The builder restored that file to exact production blob `2efecbf3eddcd9322782cc1667b02fe495fd4fa8` and moved new A-native-verification reporting solely into scoped planner and coverage. No frozen manifest was rewritten. (2) The [qualified-authoring workflow #44156145539](https://github.com/physicsvigilante/opticsim/actions/runs/44156145539) initial attempt at FINAL unchanged source failed at Chrome launch with the explicit diagnostic **Chrome/Chromium unavailable** after successful Node/CLI steps. Other workflow Chrome regressions passed; runner causality is not proved. Targeted **job-only retry, run_attempt=2 SUCCESS**, including browser qualification and real-Chrome supported demos, no source changes. Preserve both attempts when reviewing evidence.

**Gate:** exact-source independent **Chat B implementation/physics R2 review PENDING**; see [reviewer prompt](REVIEWER-PROMPT-01.md) and [full request](REQUEST.md). These are builder CI results, not independent reviewer PhyDemo/Chrome reruns. No merge, owner release or production image claims; held #129, #131, v14–v19 and main protection #123 unchanged.


## Independent Chat B implementation/physics R2 complete (2026-11-18)

[**Published independent exact-source review**](reviews/review-01-chat-b.md): **CLEARED FOR OWNER DECISION — candidate A only** at immutable source `5dc594400a3c8d537c180d1162379b5bfda5e3b1`, Git tree `d02d23e598d8211830928414fb5a1ae232d450f7` matching CI merge. Reviewer independently checked Git objects, full source, actual test/logs and separate high-precision Snell/paraxial calculations; **did NOT independently rerun PhyDemo, Node24 or Chrome**. No P0/P1 implementation blockers.

**P2-1:** concurrent cross-level missing+unknown facts can return `needs-information` rather than `invalid-input`; both remain strict refusals and never create values or native calls. **P2-2:** recommend exact 1.000000% boundary/metamorphic tests and document unreachable defensive numeric branches. **P3:** display the conditional nature, not “image found” or “native verified”. Keep original reviewed source unchanged absent new separate review.

All 11 GitHub CI workflow conclusions passed after one transparent qualified-Chrome job retry, and first source revision's historical frozen-file failure remains documented. **Owner release decision not made**; PR #133 draft/unmerged; production main unmodified. Future candidate B needs separate native finite-detector research and review; held #129/#131/#132 and main protection #123 remain distinct gates.
