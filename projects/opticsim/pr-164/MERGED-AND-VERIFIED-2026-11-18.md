# PR #164 — merged and post-merge verified

**18 November 2026. PR #164 is now merged; older draft/hold notices describe earlier history, not the present state.**

## Owner authorization and actual integration

The owner approved the explicit recommendation to integrate PR #164 and continue with real JEE coverage evaluation: “approved and continue.” The preceding owner discussion deferred GitHub ruleset setup as a recommended administrative safeguard, not a physics-correctness prerequisite. An authorization note was posted before merging; the pull request was marked ready and merged through the normal GitHub PR merge API with an expected-head SHA guard. No protection setting was changed or claimed installed.

- Merged PR: https://github.com/physicsvigilante/opticsim/pull/164
- Frozen reviewed source: **58ec0c237950d71e7b93b9b1639a52ada243e262**.
- Previous main: **d3509e82fb65d81aabe336666851f8f2962623f4**.
- Actual merge commit / new main baseline: **8b4ffee3c9deb34fcf7d657221f917fab321de4c**.
- Actual merged Git tree: **f371366765c8aa96029a0b29d6ae3f770e9b0eb2**, independently fetched and exactly equal to the previously reviewed source tree and pre-merge CI tree.
- Merge parents: previous main and the frozen reviewed source, in that order.
- GitHub PR metadata confirms closed, merged=true, draft=false; merged at 2026-11-18T17:09:59Z.

The independent exact-source review remains https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-164/reviews/review-01-chat-b.md (CLEARED FOR OWNER DECISION, no P0/P1). Reviewer source/math inspection is distinct from builder-CI native/Chrome execution. User's later authorization—not the review by itself—permitted the actual integration.

## Actual post-merge evidence, not reused pre-merge checks

GitHub Actions push runs filtered to **8b4ffee3c9deb34fcf7d657221f917fab321de4c** returned 11 standard workflows; the final success-filtered query returned **11 successful workflows**. These are push runs on merged main, not pull_request runs on the former synthetic merge.

Actual post-merge optical composition run: https://github.com/physicsvigilante/opticsim/actions/runs/44355559880
Job: **134982607188**. Its decoded log explicitly checked out main at the actual merge SHA, used Node **24.19.0** and pinned PhyDemo **811f508d2b070898c241a568b0c167dcb8645251**, and recorded:

- **860 Node tests, 860 passed, zero failed, zero skipped.**
- JEE_PLANAR_V19_ANALYTIC_CROSS_CONTRACT: 30 analytical comparisons; native not-run and image false preserved.
- JEE_PLANAR_V19_NATIVE_COEXISTENCE: genuine v19 samples, **8 emitted / 6 absorbed / 2 detector crossings / 2 actual hit events**.
- JEE_OBSERVER_NATIVE_WITNESS: actual native completed, hit approximately **(100.00000000000001,40) mm**, finite arrival error, no image claim.
- JEE_PARALLEL_BEAM_PUBLIC_ACCEPTANCE: **7 cases** (4 completed native, 1 deliberately incomplete, 2 refused). These are synthetic engine controls, NOT seven original JEE questions solved.
- JEE_PARALLEL_BEAM_CHROME: **11 checks / 6 screenshots**.
- Baseline real-Chrome browser acceptance: **27 checks / 15 screenshots**.
- Hosted smoke: **5 checks / 1 screenshot**. This is local CI site/path testing, **not a claim of public-site deployment**.

The native-complete, genuine measured-zero, stale/incomplete suppression, signed reflection and malformed-event refusal regressions remain in this exact post-merge suite. Tests injecting native-shaped contradictory records are synthetic classifier tests, not impossible native optical events.

## What is available in main, and what remains held

The merged baseline now includes bounded one-plane explicit-angle apparent-depth and observer-position analytical queries, a separately physically specified native SingleRay arrival witness, and version-isolated native parallel Beam v19 with supported lens/pre-lens aperture/planar-media configurations and conservative refusals. No perceived-image/eye, continuous irradiance, arbitrary mixed optical route or general native inverse solver is claimed.

Only **PR #164** was merged. Earlier overlapping source PRs were not separately merged. CI-trigger PR #162, thick-lens v14–v18 and other held candidates remain outside this owner authorization. Issue #123 and recommended branch protection remain unresolved/deferred, not silently installed or treated as a new optical blocker. Future material safety changes still require appropriate independent review.

## Next stage initiated: source-faithful original JEE coverage

[20-case frozen selection](../evaluation/jee-coverage-post164-v1/selection.json) and [evaluation protocol](../evaluation/jee-coverage-post164-v1/PLAN.md) are published in review_sandbox, using this exact merged engine baseline. The deterministic selection spans eight chapters from the existing 114-image original-problem inventory, excluding entries already marked reviewed by that atlas. That is NOT a guarantee of no prior exposure elsewhere, nor a blind independent model benchmark.

At the time of this record, the individual selected original images have **not** been newly inspected, first attempts have **not** been authored, and original-problem simulation success has **not** been scored. Direct binary source archive retrieval was attempted but did not produce usable image bytes in this session; no contents were inferred from filenames or substituted with synthetic cases. The next evidence work is verified Problems-only image retrieval, saved first interpretations/JSON/refusals, and baseline execution. The engine stays unchanged while those coverage gaps are measured. No additional optical feature or independent per-question review has been requested.
