# Opticsim PR #86 — exact-copy reviewer regression tests: merge and verification

**Status: MERGED and all 11 post-merge workflows PASS. No deployment.** This is a Chat A-written release record following separate explicit owner approval, not a new independent Chat B review or any change to the simulator's physical interpretation.

## Commit identity and scope

- Source repository: https://github.com/physicsvigilante/opticsim
- [PR #86 — five independent Chat B native parentage regressions](https://github.com/physicsvigilante/opticsim/pull/86): **merged** after owner approval.
- Parent production main / base: `39cdfda9b8e0244e6877bfb3656bc66da557df02` (previously released PR #83).
- Exactly approved PR head: `86a8e32d1121fa80f6761a68ec7e1881c3a2a7d0`.
- **Merge SHA / new main at verification: `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`.** [Merge commit](https://github.com/physicsvigilante/opticsim/commit/fa158fc78da7a35b6a02eaed58c0cdbd4b699220).
- Merge parents are exactly base `39cdfda...` and approved head `86a8e...`. Git tree SHA is **identical** for approved head and merge: `3a1a18c91d010f26b827544cbb337530fcfcc7d2`. GitHub commit diff lists **one added file**, 179 lines, zero deletions.
- Only newly included file: `test/reviewer-pr83-chat-b-adversarial.test.mjs`; original corrected Chat B [review-only PR #85](https://github.com/physicsvigilante/opticsim/pull/85) commit `647260ec6225bc208e744362e908803fd8cec603`. **Source and copied blob SHA match byte-for-byte:** `28bc2c96a7bcbf53322e52b31d46d887cb36deff`. Exactly five Node test declarations. The earlier failed reviewer attempt on review-only [PR #84](https://github.com/physicsvigilante/opticsim/pull/84) remains historical evidence, not rewritten or relabeled successful.
- No production optics source code, PhyDemo pin, numerical physics policy, saved-scene schema, UI behavior, workflow file, or deployment changed in this PR. The original [independent R2 implementation review of PR #83](../pr-83/reviews/review-01-chat-b.md) and [previous merge report](../pr-83/MERGE-REPORT.md) remain authoritative for the bounded source-parentage capability.

## What was actually verified

**Pre-merge PR #86:** all 11 GitHub Actions workflows passed at exact head `86a8e32d1121fa80f6761a68ec7e1881c3a2a7d0`. [Unified CI 43747351867](https://github.com/physicsvigilante/opticsim/actions/runs/43747351867) recorded **750/750 Node tests**, five public native parentage acceptance outcomes, nine real-Chrome checks and two screenshots.

**Post-merge:** all **11/11 push-event workflows passed** at exact merge SHA `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`. Post-merge [unified CI 43747971465](https://github.com/physicsvigilante/opticsim/actions/runs/43747971465) on Node 24.19.0 has **750/750 Node tests, zero failures**, five correct synthetic native public-workflow cases, **nine real-Chrome checks** and two retained screenshots.

Post-merge workflow IDs (all completed with conclusion `success`):

| Workflow | Run |
|---|---|
| Unified problem workflow checks | [43747971465](https://github.com/physicsvigilante/opticsim/actions/runs/43747971465) |
| Parameter experiment checks | [43747971435](https://github.com/physicsvigilante/opticsim/actions/runs/43747971435) |
| Original refraction problem pair | [43747971361](https://github.com/physicsvigilante/opticsim/actions/runs/43747971361) |
| Curved mirror checks | [43747971430](https://github.com/physicsvigilante/opticsim/actions/runs/43747971430) |
| Optical composition checks | [43747971429](https://github.com/physicsvigilante/opticsim/actions/runs/43747971429) |
| Plane-mirror angular inverse checks | [43747971426](https://github.com/physicsvigilante/opticsim/actions/runs/43747971426) |
| Deterministic planar angular query checks | [43747971378](https://github.com/physicsvigilante/opticsim/actions/runs/43747971378) |
| Numerical ray reliability diagnostics | [43747971377](https://github.com/physicsvigilante/opticsim/actions/runs/43747971377) |
| Qualified authoring checks | [43747971481](https://github.com/physicsvigilante/opticsim/actions/runs/43747971481) |
| Planar refraction checks | [43747971392](https://github.com/physicsvigilante/opticsim/actions/runs/43747971392) |
| Quasi-static source motion checks | [43747971375](https://github.com/physicsvigilante/opticsim/actions/runs/43747971375) |

Post-merge artifacts retained:

- [Native parentage evidence artifact 14174778027](https://github.com/physicsvigilante/opticsim/actions/runs/43747971465/artifacts/14174778027): GitHub-reported ZIP SHA-256 `32de4a78f0db288db41fb86f2ba6f115d9742f9a514b2d26134f10a1bdf30d3c`.
- [Real-Chrome parentage evidence artifact 14174693477](https://github.com/physicsvigilante/opticsim/actions/runs/43747971465/artifacts/14174693477): GitHub-reported ZIP SHA-256 `3f8394bd208d9d79cbf80ed0ef47d8fdf026abb9ce9db7dbfb86d147d47fe5d3`.

The post-merge log was inspected and the original GitHub Actions statuses verified. These ZIP digests were read from GitHub's artifact metadata, **not** independently downloaded and rehashed in this run. The underlying Chat B test is the same independently authored source that was earlier reviewed; replaying it in production CI is verification of reproducibility, not a new blind model evaluation.

## Scope and limitations

The five new checks permanently exercise: (1) actual native component-order invariance and source/child attribution, (2) independent 30° high-to-low-index Snell and 50° TIR with in-place native object identity, (3) injected per-detector 33-hit limit isolation, (4) bypass of a nonselected detector callback while real native power is measured and provenance refused, and (5) native warning refusing to publish lineage tokens.

Passing 750 tests is **not** proof of generalized ray trajectories, exact/near-critical numerical reliability, source interpretation of textbook images, continuous light, physical detected images, or classroom utility. These remain separate future capability and evaluation tasks.

## Review-only PR handling

- Reviewer PRs [#84](https://github.com/physicsvigilante/opticsim/pull/84) and [#85](https://github.com/physicsvigilante/opticsim/pull/85) remain unmerged. Their stacked branches are not production merge candidates; the corrected test source from #85 is now integrated independently through PR #86.
- Earlier research [#79](https://github.com/physicsvigilante/opticsim/pull/79) / [#80](https://github.com/physicsvigilante/opticsim/pull/80) and design documentation [#81](https://github.com/physicsvigilante/opticsim/pull/81) were not implicitly merged.
- No live provider connection, public deployment or additional feature was authorized.

**Release result: PR #86 merged into main, identical file/blob verified, all 11 post-merge workflows green.**
