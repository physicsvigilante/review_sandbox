# Independent R4 — Opticsim PR #157: signed specular reflected-event integrity

**Date:** 18 November 2026  
**Reviewer:** Chat B — independent GitHub source/diff/Git-object/CI-log inspection; independent signed-vector calculations and execution of the exact-source extracted JavaScript `validTransmittedEvent` + `evidenceResult` logic on constructed, hash-consistent synthetic records. **No independent PhyDemo or Chrome/browser rerun.**  
**Verdict: CHANGES REQUESTED. P0: none. P1: one newly introduced malformed-evidence exception / lost result-report regression.** The R3 reflected-ray physics bypass is corrected in the tested complete-vector cases, but the new check must first fail closed when the reflected direction is absent or null. This report is not release approval.

## 1. Exact frozen identity and reviewed scope

| Object | Independently checked identity and state |
| --- | --- |
| Target | [Opticsim draft PR #157](https://github.com/physicsvigilante/opticsim/pull/157), open/draft/unmerged at review |
| Exact source HEAD | **c1bcf2b5537767e6c0bd710590f9a763b0db40d7** |
| Exact source Git tree | **317eff764dd82c2c42dc1cffca5c5f856d92d464** |
| True base | Frozen [PR #155](https://github.com/physicsvigilante/opticsim/pull/155) HEAD **4d4939516ec96accb1b168d0884b35b850bbbcae**, tree **f2237c19309c829725109e0fad208fc287b94ad5** |
| Base/HEAD comparison | **3 commits ahead, zero behind; merge-base exactly PR #155 HEAD** |
| Exactly three changed files | scripts/jee-observer-native-witness.mjs (+27), test/jee-observer-native-witness-v1.test.mjs (+84), docs/JEE-OBSERVER-NATIVE-WITNESS-V1.md (+15); no deletions |
| Temporary CI-only PR | [#158](https://github.com/physicsvigilante/opticsim/pull/158) **closed unmerged** |
| Verified CI synthetic merge | **359ae0f66f49d5a54b8c1c10108e959701e44f9e**; Git tree **317eff764dd82c2c42dc1cffca5c5f856d92d464** (exact source-tree match); ordered parents **d3509e82fb65d81aabe336666851f8f2962623f4** (actual production main), **c1bcf2b5537767e6c0bd710590f9a763b0db40d7** (exact PR #157 source) |

I checked the [raw source commit object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/c1bcf2b5537767e6c0bd710590f9a763b0db40d7), [raw synthetic-merge object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/359ae0f66f49d5a54b8c1c10108e959701e44f9e), GitHub base/HEAD comparison, live PR states and main branch ref, rather than accepting those identities from prose. Source/CI identity is sound. Production main remains at the specified commit; its branch is **not protected**, and [issue #123](https://github.com/physicsvigilante/opticsim/issues/123) is still open. No pinned PhyDemo, native adapter, planar-media producer, observable projector, v5 schema, or prior independent analytical parent changes are in the child diff. Previous [PR #155 R3 CHANGES REQUESTED review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-155/reviews/review-01-chat-b.md) remains unchanged, at its original source identity.

## 2. Independent signed-reflection derivation and physical admission

For source-to-observer unit normal n and oriented tangent t = (-n_y, n_x), the explicitly authored one-ray incident direction is d_i = cos(α)n + sin(α)t for signed α with positive normal component. Ideal reflection requires

**d_ref = d_i − 2(d_i · n)n = −cos(α)n + sin(α)t**.

The tangent coefficient **keeps its sign**, and the normal coefficient reverses sign. A reflected vector with tangent −sin(α) has a negative normal dot product and the correct **unsigned** normal angle but is physically wrong for this input.

For the original R3 attack at normal 0°, the authored incident direction normalized from (+0.98288359,+0.18422770) requires reflected (-0.98288359,+0.18422770). The forged (-0.98288359,-0.18422770) is displaced from the required reflected unit vector by approximately **0.3684554**, massively exceeding the new 1e-7 tolerance. A coherent 5° reflection instead of 10.61610898° differs by about **0.09798036** in unit direction and by 5.6161° in angle, exceeding both vector and 1e-5° angle limits.

The exact [R4 source validator](https://github.com/physicsvigilante/opticsim/blob/c1bcf2b5537767e6c0bd710590f9a763b0db40d7/scripts/jee-observer-native-witness.mjs#L115-L198) calculates incident direction from the **explicitly authored** SingleRay heading and compares the native reflected branch to that vector formula. Its required angle equalities also compare reflection to the first recorded native incidence and to the authored incident-angle magnitude. This input is legitimate **only** because the authored canonical scene has one point-source SingleRay, one ideal planar interface and one passive finite detector, with no preceding intervening element. It is **not** a measured native incoming direction. In [native adapter](https://github.com/physicsvigilante/opticsim/blob/c1bcf2b5537767e6c0bd710590f9a763b0db40d7/src/adapter.js#L21-L27), the SingleRay native p2 y coordinate uses −20 sin(heading); the [native planar meter](https://github.com/physicsvigilante/opticsim/blob/c1bcf2b5537767e6c0bd710590f9a763b0db40d7/src/planar-media.js#L48-L104) turns native y-down back to world y-up, then delegates once to original PhyDemo. For normals 0°, +90°, −90°, 180°, 37° and an additional independent 123°, signed-frame reflection is consistent with that conversion.

The first-event checks continue to require one native emission, complete/fresh native status and canonical digest, qualified native observation methods, matching actual detector-crossing count and full hit list, exactly one interface interaction plus transmitted branch for qualified positive/one-interaction zero cases, correct medium side/indices/Fresnel policy, finite unit transmitted direction and angle, nonnegative branch powers, no TIR/invalid/truncated record, and first-event transmitted geometry consistent with conditional analysis. **The same validator protects positive arrival and one-interface measured zero.** A separately completed **zero-interface/zero-detector** case remains an available negative measurement with no fabricated first event.

## 3. Independent exact-source JavaScript adversarial probe

I loaded the two frozen witness files and planar-normal helper via GitHub, extracted their actual `validTransmittedEvent` and `evidenceResult` function bodies into an isolated JS evaluator, and supplied synthetic complete-status / method-qualified / matching-hash records with one transmitted plus one reflected branch and either one synthetic matching hit or a synthetic measured-zero summary. The evaluator used a local JSON-based stand-in for `structuredClone` in this isolated runtime; it did **not** change the checked functions or represent a real native run.

At an **18.5°** signed incidence with indices 1.5 → 1, transmitted angle **28.4216775031°**, I probed six normals (0, +90, −90, 180, 37 and independent oblique 123 degrees), both tangent signs, five event shapes and two detector-result paths: **120 synthetic exact-source classifier evaluations**:

| Event shape | One-hit result, 12/12 cases | Measured-zero result, 12/12 cases |
| --- | --- | --- |
| Physically consistent complete event | verified-sampled-arrival | native-observed-no-crossing |
| Reversed signed reflected tangent | native-evidence-unavailable | native-evidence-unavailable |
| Reflected direction and angle coherently forged to 5° | native-evidence-unavailable | native-evidence-unavailable |
| **New challenge:** physically correct reflected vector but incidentAngleDeg spoofed +0.01° | native-evidence-unavailable | native-evidence-unavailable |
| **New challenge:** reflected branch exists but direction key omitted | **TypeError thrown** | **TypeError thrown** |

An additional direct R3-versus-R4 isolated function comparison at normal 0° covered **both missing and explicitly null** reflected-direction values. Frozen R3 returned **native-evidence-unavailable** on both paths. R4 throws **TypeError** on both paths. These records were constructed by the reviewer, never produced by pinned native PhyDemo, and no claim of independently executed full witness CLI, Chrome or native transport follows.

## 4. P1 — New pre-validation dereference throws on missing/null reflected direction

**Location:** [scripts/jee-observer-native-witness.mjs lines 179–184](https://github.com/physicsvigilante/opticsim/blob/c1bcf2b5537767e6c0bd710590f9a763b0db40d7/scripts/jee-observer-native-witness.mjs#L179-L184); [unprotected evidence classifier call at line 419](https://github.com/physicsvigilante/opticsim/blob/c1bcf2b5537767e6c0bd710590f9a763b0db40d7/scripts/jee-observer-native-witness.mjs#L404-L425).

The new code computes the specular vector mismatch by reading `r.direction.x` and `r.direction.y` **before** the following conditional can invoke `finiteUnit(r.direction)` and reject missing/non-object/non-unit directions:

~~~js
const specularError = Math.hypot(
  r.direction.x - expectedReflected.x,
  r.direction.y - expectedReflected.y);
if (!finiteAngle(r.angleDeg) || !finiteUnit(r.direction) || ...) return false;
~~~

**Concrete minimal counterexample:** take an otherwise valid, complete, hash-matched, full-Fresnel, single-source/single-plane native-shaped result (one transmission, one reflected branch, native methods/counts and angular fields consistent), and delete the reflected branch's `direction` property; equivalently set it to null. Keep the transmitted branch, incident/reflection angle values and source/plane/detector counts intact. On **both** synthetic detector-hit and completed-zero paths, R4 raises `TypeError: Cannot read properties of undefined/null (reading 'x')`. R3 gracefully rejected these identical malformed reflected records with status `native-evidence-unavailable`. The [observable projector](https://github.com/physicsvigilante/opticsim/blob/c1bcf2b5537767e6c0bd710590f9a763b0db40d7/src/observables.js#L156-L165) qualifies first-event presence/method but does not validate reflected-branch internals, so the malformed record can reach the witness validator.

The witness catches exceptions only around native execution and observable projection. It invokes `evidenceResult` **outside** that catch, before saving the final report. Therefore the exact-source function throws instead of writing the required withheld `actualNativeResult` / null accepted hit and report; the outer CLI catch can print a generic infrastructure error, but **the final structured result report is missing**. This is a regression in refusal/reporting integrity for malformed input evidence, **not** a demonstrated physically wrong native reflection or a false verified positive.

**Severity: P1 for this critical evidence/refusal gate.** A deliberately contradictory, complete native-shaped record must produce a durable qualified refusal rather than escape the classifier. Nothing in the green 40-case builder corruption set covers deleting or nulling the *reflected* direction; the older changed tests cover transmitted-direction nonfiniteness.

**Required bounded correction:** check `finiteUnit(r.direction)` (and any fields to be dereferenced) **before** computing `specularError`, returning false if invalid. Keep the 1e-7 signed-specular distance and 1e-5° incident/reflected angular consistency checks unchanged. Add complete/hash-matched synthetic refusal tests for reflected direction **absent and null**, with both positive-hit and measured-zero summaries, asserting status `native-evidence-unavailable`, exit code 2, null accepted hit/incoming direction and an actual saved report. If a narrower fail-closed guard is chosen, prove identical behavior at the exact corrected source. Re-run builder checks/exact-tree CI, freeze a **new child SHA/tree**, and request **one focused independent correction review**; do not rewrite the R3/R4 historical verdicts.

**P0:** none detected. The checked malformed cases do not get falsely labeled verified arrival or native-observed zero; the serious issue is loss of the structured evidence/refusal result.

## 5. Builder CI checked; source correctness is a separate judgment

At the exact source HEAD, the GitHub Actions runs API lists **11 standard PR workflows, currently 11 concluded success**. I inspected actual decoded logs rather than only check badges:

- [Plane-mirror workflow run 44321863943](https://github.com/physicsvigilante/opticsim/actions/runs/44321863943), job **134862636069**: pinned PhyDemo setup, **820 tests / 820 passed / 0 failed** and marker **JEE_OBSERVER_SPECULAR_REFLECTION_ADVERSARIAL** with five authored normals, tangent ±, **10 genuine pinned-native full-Fresnel positive controls admitted** and **40 injected contradictory summary cases withheld** across detector-hit and artificially measured-zero classification. Synthetic corruptions **are not PhyDemo-produced rays**.
- [Optical composition run 44321863739](https://github.com/physicsvigilante/opticsim/actions/runs/44321863739), job **134862635824**: 820/820 Node pass; browser acceptance **27 checks / 15 screenshots** and hosted smoke **5 checks / 1 screenshot** with Chrome 157.0.8103.50. These are builder CI executions, not reviewer reruns.
- [Curved-mirror run 44321864087](https://github.com/physicsvigilante/opticsim/actions/runs/44321864087): **attempt 1** job **134862637368** passed Node tests, original native follow-ups and build, then failed the browser step with **“No Chrome/Chromium available; browser evidence cannot be claimed.”** On unchanged source, **attempt 2**, job **134864030941**, succeeded including **7 browser checks / 2 screenshots**. Preserve both attempts; infrastructure failure is not a new optics physics defect.

The 40 builder corruptions verify two relevant **complete-vector** physical attacks. They do not test the independently identified **missing-direction** pre-validation exception, so the green suite does not remove the new P1. Legitimate genuine pinned-native full-Fresnel output being accepted is valuable evidence, but the reviewer did not rerun that package.

## 6. Nonblocking scope boundaries and disposition

- **N1 — No Fresnel energy/power certification.** Branch powers are required finite and nonnegative, but this narrow validator does not establish R/T energy conservation or polarization correctness. This is an explicit limitation, not an additional P1 in the targeted R4 diff.
- **N2 — Measured, modeled and perceived are different.** A successful first-event consistency check plus native detector crossing is a **sampled** finite-detector observation; complete measured zero is detector-specific negative data. Neither reconstructs a human eye, physical image, continuous irradiance, complete ray ancestry or all untraced rays.
- **N3 — Digest is freshness, not authentication.** The synthetic, hash-matched records are purposeful classifier adversaries, not evidence that real PhyDemo generated impossible light. The authored heading is a known source input, not independent native incident-ray telemetry.
- **N4 — Scope of review.** Unchanged analytical geometry, other optical families, and combined JEE integration have **not** been independently re-audited; tests and CI source identities were inspected in the limited R4 scope.

**Final verdict: CHANGES REQUESTED — one P1; no P0 identified.** The central signed-specular physical correction is mathematically sound and refuses the original forged reflection forms. However, the new reflected-direction dereference breaks clean refusal/report persistence for a malformed complete first event. Apply the minimal ordering guard and targeted regression at a **new exact source identity**, then request one bounded confirmation; afterward prefer **one consolidated JEE integration candidate and one cross-feature integration review** rather than another experimental optics branch. This source review does **not** authorize merging PRs #155/#157/#158, publishing a release or marking branch-protection issue #123 resolved. No Opticsim source/branch/PR state or old report was changed by this review.
