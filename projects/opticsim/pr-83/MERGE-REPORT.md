# Opticsim PR #83 — owner-approved merge and post-merge verification

**Release verification: COMPLETE — 11/11 post-merge GitHub Actions workflows PASSED.** The implementation is now on `main`. This report is written by **Chat A** after explicit owner approval; it is not a new Chat B review, an independent original-text interpretation evaluation or a classroom study.

## Frozen identity and merge

- Repository: https://github.com/physicsvigilante/opticsim
- Owner-authorized source [PR #83](https://github.com/physicsvigilante/opticsim/pull/83): **merged**, after confirming its exact reviewed head and 11/11 pre-merge workflow passes.
- Original production base: `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`.
- **Exactly reviewed and merged source head:** `366037a3ed68c2110434e2132899cd0a2cbc610a`.
- **GitHub merge commit and now-current main:** `39cdfda9b8e0244e6877bfb3656bc66da557df02`. [Merge commit](https://github.com/physicsvigilante/opticsim/commit/39cdfda9b8e0244e6877bfb3656bc66da557df02).
- The merge commit has exactly two parents: original base `00e6211...` and reviewed head `366037a...`. **Git tree SHA is identical** in the reviewed source head and merged main: `4283059c8d264207583e30358ac0841ab04db3b5`. This verifies no unintended merge-content changes.
- GitHub recorded merge on **2026-11-15 at 18:21:29 UTC** (23:51:29 IST).
- Supported toolchain Node **24.19.0**; pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251` unchanged; no new saved-scene version, physics engine patch, numerical threshold change or deployment.

## Independent review prerequisites

- Separate [PR #81 design R2 review](../pr-81/reviews/review-02-chat-b.md) concluded **pass for design only** at its pinned revised design head; it does not sign off production.
- [PR #83 independent Chat B R2 code/evidence review](reviews/review-01-chat-b.md) concluded **pass at exact implementation head**, with no demonstrated blocking production defect. The review independently rehashed the original native and browser artifacts, checked numerical Snell/Fresnel facts and authored five new native adversarial tests.
- The corrected five-test reviewer branch [draft PR #85](https://github.com/physicsvigilante/opticsim/pull/85), one new test file only relative to production source, had **750/750 Node tests** and **11/11 workflows passed**. The original first-run test harness error in [draft PR #84](https://github.com/physicsvigilante/opticsim/pull/84) and failed CI was preserved, not recast as a pass. Neither PR #84 nor #85 was merged; reviewer-authored tests are external, not yet in production main.
- Explicit separate owner merge approval was received only **after** this independent code review; merging PR #83 did not implicitly authorize any other PR or public deployment.

## Actual post-merge CI on the merge SHA

All **11/11 distinct push-event workflows completed with conclusion `success`**, and every run's `head_sha` was the exact merge commit `39cdfda9b8e0244e6877bfb3656bc66da557df02`:

| Workflow | GitHub Actions run |
|---|---|
| Unified problem workflow checks | [43746305858](https://github.com/physicsvigilante/opticsim/actions/runs/43746305858) |
| Original refraction problem pair | [43746305859](https://github.com/physicsvigilante/opticsim/actions/runs/43746305859) |
| Deterministic planar angular query checks | [43746305866](https://github.com/physicsvigilante/opticsim/actions/runs/43746305866) |
| Plane-mirror angular inverse checks | [43746305874](https://github.com/physicsvigilante/opticsim/actions/runs/43746305874) |
| Curved mirror checks | [43746305908](https://github.com/physicsvigilante/opticsim/actions/runs/43746305908) |
| Numerical ray reliability diagnostics | [43746305909](https://github.com/physicsvigilante/opticsim/actions/runs/43746305909) |
| Planar refraction checks | [43746305921](https://github.com/physicsvigilante/opticsim/actions/runs/43746305921) |
| Parameter experiment checks | [43746305926](https://github.com/physicsvigilante/opticsim/actions/runs/43746305926) |
| Quasi-static source motion checks | [43746306004](https://github.com/physicsvigilante/opticsim/actions/runs/43746306004) |
| Qualified authoring checks | [43746306014](https://github.com/physicsvigilante/opticsim/actions/runs/43746306014) |
| Optical composition checks | [43746306027](https://github.com/physicsvigilante/opticsim/actions/runs/43746306027) |

The post-merge unified job `132910254046` logs **745/745 Node tests, zero failures**. Its new public native parentage acceptance reported **five expected outcomes** passed: two-source Fresnel branching, physical source revision, transmitted-only approximation, genuine zero-hit sampling, and withheld weak-Fresnel truncation. The actual Chrome acceptance reported **nine passed checks**, retaining the two screenshots `native-parentage.png` and `parentage-suppressed.png`. This is software/physical-invariant regression evidence, **not independent teacher/student evaluation**.

### Post-merge raw artifacts

- [Native parentage artifact ID **14174586268**](https://github.com/physicsvigilante/opticsim/actions/runs/43746305858/artifacts/14174586268): GitHub SHA-256 ZIP digest `0d65c5c264c2cc4f0c9b4f4c1491a0004356fdda1a489a9e8e75dc86ec31bdc2`.
- [Real-Chrome parentage artifact ID **14174318027**](https://github.com/physicsvigilante/opticsim/actions/runs/43746305858/artifacts/14174318027): GitHub SHA-256 ZIP digest `c29be26934b94dcd08b876f954e1302503a66b27add9547b99c85d46e7038939`.

**Provenance caveat:** These post-merge ZIP digests were obtained from GitHub Actions artifact metadata, and the corresponding successful job logs and steps were inspected. They were **not downloaded and independently rehashed by Chat A** in this turn; the earlier pre-merge artifacts were independently rehashed by Chat B during its R2 review. Do not claim a fresh independent post-merge ZIP audit.

## What is actually released

The new opt-in `detector-ray-provenance` result applies **only** to admitted v5 planar-media-tracing scenes with exactly one planar interface, **1–2 SingleRay sources**, **1–2 passive detectors**, zero other optical components and explicitly requested provenance. Native source-start ray objects and direct observed `newRays` child references are associated via **per-run object identity**, with actual selected detector callbacks. Unsupported or incomplete/unknown/truncated/stopped/stale evidence is unavailable/suppressed, not reconstructed. Existing detector power and crossing counts and no-opt-in output remain separate. It is **not** a continuous illumination model, optical path solver, detected image, source-authenticity guarantee or an original textbook-answer solver.

**Remaining nonblocking limitations:** near/exact-critical numerical reliability across arbitrary scenes, genuinely delayed first-A Chrome callback stress beyond the controlled Session test, and independently demonstrated teaching usefulness have not been certified. Preserve precise limits in public and teacher-facing descriptions.

## Reviewer-only PRs and next possible task

- Review/test-only PRs [#84](https://github.com/physicsvigilante/opticsim/pull/84) and [#85](https://github.com/physicsvigilante/opticsim/pull/85), and research-only PRs [#79](https://github.com/physicsvigilante/opticsim/pull/79) and [#80](https://github.com/physicsvigilante/opticsim/pull/80), remain **unmerged**. The reviewed design-only PR [#81](https://github.com/physicsvigilante/opticsim/pull/81) is not a dependency of the production merge.
- If the owner wants the five independently authored reviewer tests permanently in main, create a **new test-only branch from current main** and transfer only `test/reviewer-pr83-chat-b-adversarial.test.mjs`; validate CI and seek a **separate** merge approval. Do **not** merge the stacked reviewer branches #84/#85.
- No automatic broader ray-history project or direct LLM integration was added. The next milestone should be chosen on physical correctness and teaching value, separately from this completed release.

**Release status: MERGED AND POST-MERGE VERIFIED. No deployment.**
