# Opticsim PR #83 — final R2 release status

**RELEASE: MERGED INTO MAIN AND ALL 11/11 POST-MERGE GITHUB ACTIONS WORKFLOWS PASSED.** No deployment. The exact reviewed implementation was merged following separate owner authorization.

**Canonical [merge and verification record](MERGE-REPORT.md)** includes exact parent and tree SHAs, all eleven push workflow IDs, retained native/Chrome artifact digests, independent reviewer evidence, negative test history and remaining limitations.

## Exact source and independent review

- [PR #83](https://github.com/physicsvigilante/opticsim/pull/83): **merged**.
- Original main base: `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`.
- **Exact independently reviewed production head**: `366037a3ed68c2110434e2132899cd0a2cbc610a`.
- **Merge commit, current main at verification**: `39cdfda9b8e0244e6877bfb3656bc66da557df02`, Git tree `4283059c8d264207583e30358ac0841ab04db3b5` — **same tree as reviewed head**.
- No pinned PhyDemo change (remains `811f508d2b070898c241a568b0c167dcb8645251`), new physics law, native numerical budget change or saved-scene version migration.
- [Design-only R2 Chat B review pass for PR #81](../pr-81/reviews/review-02-chat-b.md) preceded implementation. [Independent implementation R2 Chat B review-01](reviews/review-01-chat-b.md) **PASS** at exact PR #83 head, no demonstrated production blocker.
- Chat B's five new adversarial tests were independently authored on test-only corrected [PR #85](https://github.com/physicsvigilante/opticsim/pull/85), one added 179-line test file, no production source edits; reviewer CI **750/750 Node tests, 11/11 workflows passed**. Original failed test-only run in review [PR #84](https://github.com/physicsvigilante/opticsim/pull/84) remains preserved. [Developer disposition](responses/response-01-chat-a.md) acknowledged results before owner approval.

## Verified release CI

- **All eleven GitHub push-event workflows for the exact merge commit completed successfully**. [Unified run **43746305858**](https://github.com/physicsvigilante/opticsim/actions/runs/43746305858): **745/745 Node tests** (0 failures), **5/5 public native parentage acceptance outcomes**, **9/9 actual Chrome checks** and two screenshots.
- [New post-merge native artifact 14174586268](https://github.com/physicsvigilante/opticsim/actions/runs/43746305858/artifacts/14174586268): GitHub ZIP SHA-256 `0d65c5c264c2cc4f0c9b4f4c1491a0004356fdda1a489a9e8e75dc86ec31bdc2`.
- [New post-merge browser artifact 14174318027](https://github.com/physicsvigilante/opticsim/actions/runs/43746305858/artifacts/14174318027): GitHub ZIP SHA-256 `c29be26934b94dcd08b876f954e1302503a66b27add9547b99c85d46e7038939`.
- Post-merge ZIP hashes are **GitHub artifact metadata**, not independently recomputed by Chat A. Earlier pre-merge artifacts were downloaded and rehashed by Chat B during the code review.

## Capability and limitations

The released explicit `detector-ray-provenance` observation reports **actual run-local emitted ray objects and direct native parent–child objects at sampled detector callbacks**, only for existing v5 one-interface, 1–2 SingleRay, 1–2 passive-detector scenes (zero other optical components). It does not reconstruct complete ray histories, detect images, measure absolute irradiance, prove source text interpretation or solve original textbook problems. Incomplete, unknown and stale observations must be withheld. Remaining numerical near/exact critical, intentionally delayed Chrome race and classroom-use gaps are documented and **nonblocking only for this precise narrow release**.

## Pending separate decisions

- Do not merge [review-only PR #84](https://github.com/physicsvigilante/opticsim/pull/84) or [#85](https://github.com/physicsvigilante/opticsim/pull/85) as-is; they stack on old source and were not part of owner's merge approval.
- If permanent independent regression tests are desired, copy **only** the reviewer-authored test file into a new branch from the merged main, verify CI, and obtain separate merge approval.
- Research-only #79/#80 and docs-only #81 also were **not merged** as part of PR #83; no public deployment or AI provider integration was authorized.

**The requested PR #83 merge and post-merge verification are complete.**
