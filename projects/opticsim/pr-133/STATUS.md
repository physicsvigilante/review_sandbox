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
