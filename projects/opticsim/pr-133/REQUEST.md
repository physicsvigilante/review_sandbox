# Opticsim PR #133 — independent source and physics review request

**Scope:** First JEE conditional paraxial apparent-depth calculation (A). Not a native image, finite pupil, ray reconstruction, or general optical simulation.

## Source to review

- Draft [PR #133](https://github.com/physicsvigilante/opticsim/pull/133) HEAD **5dc594400a3c8d537c180d1162379b5bfda5e3b1**, source tree **d02d23e598d8211830928414fb5a1ae232d450f7**. Synthetic GitHub merge **d3dda63d6d079048e8b144d89ce6dcd92f8710b2** has the same Git tree; verify independently, not from this prose.
- Production base **d3509e82fb65d81aabe336666851f8f2962623f4**. Only source additions: src/planar-apparent-depth-queries.js, src/problem-workflow.js, test/jee-apparent-depth-analytical.test.mjs, examples/jee-apparent-depth-v1.json. No schema migration, vendor pin, optical solver, reader, Chrome UI or frozen scripts changed.
- [Design PR #132 R2 independent review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-132/reviews/review-02-chat-b.md) cleared the corrected design FOR OWNER DECISION ONLY. It did not approve this new code. [Research PR #131](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-131/reviews/review-01-chat-b.md) was test-only and proved no physical eye/image.

## First failed attempt — preserve it

The initial implementation source HEAD **693f84a20899c55129cf4163af54488411108d61** modified scripts/run-problem.mjs. Its first Node24 run [#44155490022](https://github.com/physicsvigilante/opticsim/actions/runs/44155490022) had **802 tests / 801 passed / 1 failed**. Failure: the existing detector-hit-transfer historical test correctly refused mutation of the byte-frozen public run-problem CLI. This was a real correctness/release-process gate, not native optical solver physics failure.

The builder **restored** scripts/run-problem.mjs exactly to the original Git blob **2efecbf3eddcd9322782cc1667b02fe495fd4fa8** and moved only this new method's verification block to scoped planner/coverage metadata. On explicit reduced-A verifyNative true, the math remains conditional while coverage/report status is blocked-native-verification, typed NATIVE_SCENE_REQUIRED diagnostic, no native run and exit 2. Without verifyNative, a conditional calculation is native-free. Older family coverage semantics remain unchanged. Critically, verify this solution is compatible with existing problem consumers rather than weakening or rewriting historical test evidence. The first failure must remain visible in the final review.

## Review checks

1. Independently derive real-depth formula: paraxial d_a=d*n_receiving/n_object; conditional symmetric-pair d_s=d_a*sqrt(1-(n_object/n_receiving*sin i)^2)/cos i. Check i is **object-medium incident** angle, not observer-medium direction. Confirm 120 mm / 1.5 to 1 / 5 deg gives 80 mm paraxial and 79.61636684775047 mm stipulated pair with relative difference 0.47954%; 30 deg refuses. Confirm 4 to 1 at 5 deg refuses (5.916% difference), while 4 to 1 at 1 deg admits (0.229% difference). Equal indices have undeviated continuation. No pupil or image claim.
2. Exact reduced-facts and typed query contracts: one named kind paraxial-apparent-depth, one-plane assumption, explicit normalDepth, lengthUnit mm/cm/m, two indices [1,4], stated viewing.model paraxial. No implicit scene/v20, point-source, brightness, ray or eye. Check strict nested validation and request-field uniqueness/4-calculation cap.
3. Numeric/refusal safeguards: after conversion real depth [0.01,10000] mm, finite positive output <=50000 mm. If supplied, maximum object-medium incident cone strictly >0, <=5 degrees, AND <=1% relative paraxial-vs-symmetric construction difference; any larger or high-contrast failure gives unavailable/null. No cone means null envelope and explicit no-numeric-bound warning. Check grazing, TIR/critical, nearly equal indices, 0/negative, invalid type, missing and extra fields, unit precision. The 1% is a chosen geometric-model admission policy, not physical image or numerical accuracy.
4. Distinguish conditional/missing facts/invalid facts/outside supported model/numerically indeterminate. Preserve method, assumption-dependent qualification, limitations/warnings, native.status not-run, nativeObservation false and unverified original JEE interpretation in both plan, saved analytical-results and report. No magic "available" promotion.
5. Inspect actual CLI behavior on native-free valid facts and explicitly requested native verification: no original run-problem source edits; no native calls, scenes, qualified packages or native evidence, preserved input bytes and sha256, blocked overall status if native requested, exit2. Check mixed analytical/native request without invented apparatus. Existing problem dispatcher and method-suitability should bind only exact known kinds.
6. Independently confirm all **final source** CI workflow conclusions and source/tested-merge tree equality. Previous failed workflow and source edits must be disclosed, not erased. Existing native and Chrome regressions are NOT evidence that an apparent-depth browser feature exists.

## Independence and release

If the final source SHA/tree changes or final Node24/CI is not complete, mark INSUFFICIENT EVIDENCE or request refreshed identity. Preserve all historical freezes. Do not merge, deploy, or claim independent native/Chrome execution unless actually performed. Feature B (short finite-window observer rays) remains separately gated; main protection issue #123 and held #129 / v14-v19 branches remain independent.

Publish projects/opticsim/pr-133/reviews/review-01-chat-b.md with exact SHA/tree, ranked P0-P3 issues, evidence limits and **one verdict: CLEARED FOR OWNER DECISION / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**.

## Builder final exact-head evidence now ready — review, do not trust the summary blindly

- [Full Node24 native/planar/browser run #44156145655](https://github.com/physicsvigilante/opticsim/actions/runs/44156145655): actual CI checkout `d3dda63d6d079048e8b144d89ce6dcd92f8710b2`, same Git tree as authored source; supported Node24.19.0 and pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`. Logged **802/802 Node tests PASS**, including 12 new A tests; native planar/browser steps pass.
- All **11/11** existing workflow conclusions SUCCESS for exact HEAD `5dc594400a3c8d537c180d1162379b5bfda5e3b1`, **with transparent targeted retry**: [qualified authoring run #44156145539](https://github.com/physicsvigilante/opticsim/actions/runs/44156145539), initial attempt failed browser startup with **Chrome/Chromium unavailable** (Node and previous steps passed). A **job-only attempt 2** succeeded on exact unchanged source; both browser qualification and three supported Chrome demonstration steps passed. No claim of proven runner cause.
- Independently inspect complete Git tree, source and CI run objects, raw native logs, Chrome job step summaries and early failure; don't label 11 workflows 11 independent physics replications.
