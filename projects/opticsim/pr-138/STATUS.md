# Opticsim PR #138 — JEE B1a native finite-detector pair source status

**2026-11-18: DRAFT IMPLEMENTATION, final independent source/physics review PENDING. Nothing merged.**

[Draft PR #138](https://github.com/physicsvigilante/opticsim/pull/138) starts directly from production `main`, not held research/design/conditional branches. Its ONLY new public capability candidate is **B1a: two independent native source directions with measured sampled finite-detector hit evidence**, **never** a reported backward intersection/real or apparent image. `geometry:{status:'withheld',value:null}` even for the positive JEE fixture; `observerAssessment` and `imageAssessment` explicitly not assessed. B1b numerical/image localization is not implemented.

| Exact source identity | Value |
| --- | --- |
| PR138 final-source HEAD | `936f7d8bca9af0db950ab258e6df2f0e3a37914a` |
| Authored Git tree | `182a8c51dfcc9cd618e9d92f25ea0d5cb49edc30` |
| Proposed synthetic merge | `7970f61daea3e13789f801a82626e95bfc8ef471` |
| Synthetic merge tree | `182a8c51dfcc9cd618e9d92f25ea0d5cb49edc30` — identical |
| Production base main | `d3509e82fb65d81aabe336666851f8f2962623f4` |
| New files | Exactly 5 additions: `src/detector-pair-json.js`, `src/detector-pair-plan.js`, `scripts/detector-selected-pair.mjs`, `test/detector-selected-pair.test.mjs`, `examples/jee-detector-selected-native-pair-v1.json` |
| Historical frozen run CLI | `scripts/run-problem.mjs` blob `2efecbf3eddcd9322782cc1667b02fe495fd4fa8`, unchanged vs production |
| Native solver/pin/schema/browser | No changed tracked production source/ABI/pin/schema or UI |

**R2 design prerequisite:** [#137 independent Chat B R2](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-137/reviews/review-02-chat-b.md) **CLEARED FOR OWNER DECISION — DESIGN ONLY**. Source PR #138 requires its own independent review.

**Real first-source defect retained:** `f657b9762e4b30b847a0d69cfb47546a0366b1cb` had **803/804 tests pass, one fail** because B1a mistakenly tested length in user-authored cm/m before conversion. This was corrected and intermediate `15fee6589bd098ce88acf9cb7f3075e024e2d9f1` passed **804/804 and 11/11 workflows**. Final source further adds genuine native TIR refusal, forged native direction/capture and SHA rejection, async request mutation and finalized manifest run completeness. No previous CI is silently promoted to validate the final HEAD.

**Architecture:** new duplicate-key-safe bounded raw-UTF8 JSON parser, strict existing v5 three-component apparatus and second source direction, cloned native scenes with complete canonical family hash + per-run scene hashes, two genuine pinned-native executions and 4 independently qualified observable readings each. Native misses retain sampled 0/[], Fresnel-off remains qualified, incomplete/native warning/stale responses withhold. New standalone evidence CLI writes raw input, two canonical scene files, per-run raw/readouts, report and last-written SHA manifest, without editing byte-frozen existing CLIs. No image/pupil/observer simulation, continuous irradiance or B1b numeric position.

[**Copy-ready Chat B source review prompt**](REVIEWER-PROMPT-01.md) · [**Full independent source/native review request**](REQUEST.md).

**Final-head CI should be independently confirmed before source clearance.** No release or merge decision yet, production main unprotected (issue #123), held #129/#133/#135/#137 unchanged.


## Final lexical-hash portability hardening — 2026-11-18

Source HEAD now `936f7d8bca9af0db950ab258e6df2f0e3a37914a`, Git tree `182a8c51dfcc9cd618e9d92f25ea0d5cb49edc30` identical to tested synthetic merge `7970f61daea3e13789f801a82626e95bfc8ef471`. The new B1a plan uses fixed code-unit lexical order (instead of ICU-locale-dependent collation) for portable component-ID family canonicalization. A new source test runs genuine native rays with non-default stable IDs and reversed authored component ordering. **All modifications remain within the five newly added B1a files**, no old frozen source or native pin changed. The previous source `26131c305d2240c394edcc672b7578e615bc4f0b` passed **809/809 Node tests and 11/11 workflows**; this is separate historical evidence, not automatic final-source clearance. Verify exact-HEAD final CI before independent review.


## Final exact-source builder CI verified — 18 November 2026

**Source HEAD `936f7d8bca9af0db950ab258e6df2f0e3a37914a`, tree `182a8c51dfcc9cd618e9d92f25ea0d5cb49edc30`** matches synthetic CI merge `7970f61daea3e13789f801a82626e95bfc8ef471` tree with production main `d3509e82fb65d81aabe336666851f8f2962623f4` as first parent. Final diff is **exactly five newly added files**, no `src/` existing files modified and historical frozen CLI remains original blob `2efecbf3eddcd9322782cc1667b02fe495fd4fa8`.

**810/810 Node24.19.0 tests PASS and 11/11 workflows SUCCESS**, pinned native PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`, recorded in [raw native run #44254113527](https://github.com/physicsvigilante/opticsim/actions/runs/44254113527) and existing [native/Chrome regression #44254113567](https://github.com/physicsvigilante/opticsim/actions/runs/44254113567). Exactly 20 new B1a tests include real native CLI two-run positive, finite 2/5/10 mm, equal indices, reversed/rotated/unit/ordering, Fresnel qualified, TIR/aimed-away/shifted misses, duplicate nested JSON, wrong/extra/missing facts, old CLI immutability, stale/forged-native/uncaptured suppression, async input snapshot, 0/1/2 executor failure counters and SHA manifest tamper checks. Passing existing Chrome checks demonstrate **legacy compatibility only**, not a new B1a browser interface.

**Real emitted evidence** is logged in the tagged `[b1a-native-hit-evidence]` record: full Fresnel 1.5→1, two separate headings ±0.5°, actual finite native detector hits y≈±1.5708611274685678 mm at x=40; incoming unit vectors match actual PhyDemo transmitted first branches, one emitted and one crossing each, distinct scene SHA values. The public result is `native-hits-reported` while `geometry.value:null` and image/observer **not assessed**. No B1b mathematical image position is released. The first real cm/m length-validation test failure (803/804) and subsequent fixed 804/804 and 809/809 milestones are retained, not retroactively erased.

[**Detailed independent review with final raw CI pointers**](REQUEST.md) · [**copy-ready Chat B prompt**](REVIEWER-PROMPT-01.md).

**Independent source/physics review PENDING.** This is builder CI, not independent PhyDemo execution. Draft PR #138 remains unmerged; production `main` unchanged and unprotected (#123). Held #129/#133/#135/#137 stay independent; no eye/image or B1b numerical location claim.
