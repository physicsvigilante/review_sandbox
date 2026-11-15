# Opticsim PR #86 — permanent retention of independently authored R2 reviewer regressions

**Status: OWNER-APPROVED TEST-ONLY PR #86 MERGED; ALL 11/11 POST-MERGE WORKFLOWS PASSED.** No new production physics, scene schema, native core, numerical policy, or UI feature was implemented. See the [canonical release report](MERGE-REPORT.md) for every workflow run ID, artifact digest, exact source tree identity and history.

## Exact provenance

- [Opticsim PR #86](https://github.com/physicsvigilante/opticsim/pull/86), now **merged**, contains **only** `test/reviewer-pr83-chat-b-adversarial.test.mjs`, added as 179 lines without editing.
- **Original PR #86 production base:** `39cdfda9b8e0244e6877bfb3656bc66da557df02`, the previously released and [11/11 post-merge verified PR #83](../pr-83/MERGE-REPORT.md).
- **New main commit after owner-approved PR #86 merge:** `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`, same Git tree `3a1a18c91d010f26b827544cbb337530fcfcc7d2` as approved PR #86 head.
- **Exact PR #86 head:** `86a8e32d1121fa80f6761a68ec7e1881c3a2a7d0`, one commit above main. [Single-file diff](https://github.com/physicsvigilante/opticsim/compare/39cdfda9b8e0244e6877bfb3656bc66da557df02...86a8e32d1121fa80f6761a68ec7e1881c3a2a7d0).
- **Original corrected Chat B reviewer test commit:** `647260ec6225bc208e744362e908803fd8cec603` from review-only [draft PR #85](https://github.com/physicsvigilante/opticsim/pull/85), descended from reviewed PR #83 head `366037a3ed68c2110434e2132899cd0a2cbc610a`.
- **Original and copied test file Git blob SHA are identical:** `28bc2c96a7bcbf53322e52b31d46d887cb36deff`. Verified by fetching both files; all **8,905 UTF-8 characters** and trailing newline match; five `node:test` tests. No normalization or changes to the reviewer's text.
- The original reviewer-authored test fixture error was preserved on review-only [draft PR #84](https://github.com/physicsvigilante/opticsim/pull/84), [failed CI 43744286362](https://github.com/physicsvigilante/opticsim/actions/runs/43744286362); corrected reviewer branch and CI remain distinct from this new main-based integration.

## Verification on exact test-only branch

- **All 11/11 GitHub Actions workflows completed successfully**, at head `86a8e32d1121fa80f6761a68ec7e1881c3a2a7d0`.
- [Unified run 43747351867](https://github.com/physicsvigilante/opticsim/actions/runs/43747351867): **750/750 Node tests passed**, including five independently authored adversarial tests; ordinary public parentage acceptance **5/5** expected outcomes; real Chrome **9/9** checks and two retained screenshots passed.
- [Native run artifact ID 14174413089](https://github.com/physicsvigilante/opticsim/actions/runs/43747351867/artifacts/14174413089) ZIP SHA-256 (GitHub metadata) `9c77dfc5fa799d8966509a11a7826e6212cbe3abc8ec984008f5a9bbf291dc83`.
- [Real-Chrome artifact ID 14174843403](https://github.com/physicsvigilante/opticsim/actions/runs/43747351867/artifacts/14174843403) ZIP SHA-256 (GitHub metadata) `fb85c8848baeded35364d06fab61f7e1221209bd46f39d697bac04e279900b56`.
- These artifact digests were obtained from GitHub Actions metadata; a separate post-PR86 independent ZIP download/re-hash was **not** conducted in this turn. Original reviewer checks are documented in [Chat B PR #83 report](../pr-83/reviews/review-01-chat-b.md).

## What the five regressions protect

1. Actual source/interface/detector **component ordering** and source-parent identity, detector power and crossings.
2. Native high→low **Snell transmission at 30°** versus **TIR at 50°**, with in-place primary identity.
3. Test-injected **33-crossing per-detector cap isolation**, distinguishing selected and nonselected detectors.
4. **Actual native nonselected detector callback bypass** while detector power still changes, preventing falsely complete selected provenance.
5. **Native warning suppression**, with no leaked parent tokens.

These tests preserve exact narrow v5 source-object semantics. Passing them is not proof of all physical ray paths, near/exact-critical numerical precision, continuous illumination, image formation, source-image interpretation, textbook answer completeness or teacher/student outcomes.

## Release gate

**The owner separately approved and merged PR #86 only.** The exact reviewed one-file copy passed all 11 push-event workflows after merge, including **750/750 Node tests, 5/5 public native cases, and 9/9 real Chrome checks**. Review-only PRs #84/#85 remain unmerged historical review artifacts. No new R2 code review was required for the byte-identical unchanged test file; future production/evidence changes require their own appropriate verification. [Full merge report](MERGE-REPORT.md).

No deployment or unrelated repository operation is authorized by this status record.
