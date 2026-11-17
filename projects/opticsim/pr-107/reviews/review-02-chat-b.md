# Opticsim PR #107 — Chat B independent targeted R2 follow-up (review 02)

**Verdict: CLEARED FOR OWNER DECISION** on the bounded v14 two-separated-dielectrics admission, **not an authorization to merge**. The previously open **F1** (full-Fresnel native branching, truncation and result withholding) and **F2** (G2-origin native TIR followed by a different-face exit) evidence gaps are resolved to the level required for an owner decision. No new source defect is established. Retain the source PR as **draft/unmerged** until the owner gives explicit release authorization.

This is a separately authored **AI-assisted technical review**, not an endorsement by a human optics expert and not a fresh native execution.

## Exact reviewed candidate and change isolation

- Source: [physicsvigilante/opticsim PR #107](https://github.com/physicsvigilante/opticsim/pull/107); independently inspected source **HEAD `fe3a030be7bfba8e5808e4e1e2e66d6815e7add7`**. GitHub reports this PR open, draft, unmerged; base `d3509e82fb65d81aabe336666851f8f2962623f4`.
- Prior separate review: [review-01-chat-b.md](review-01-chat-b.md), **INSUFFICIENT EVIDENCE** at `3c1bcc317689386333c4155ee414f8fa99a1caea`. That review has not been overwritten or retrospectively altered.
- GitHub commit comparison from the previous review HEAD to the current HEAD reports **five commits ahead, zero behind, exactly one changed path**: newly added `test/two-glass-r2-review-regressions.test.mjs` (**173 additions, no deletions**). This is test-only. New HEAD is a merge of the previous reviewed commit and the [PR #108](https://github.com/physicsvigilante/opticsim/pull/108) test-head `1074f1be19656ee7e0ffc3ea52fce3c517836ff5`; PR #108 was merged into the **feature branch**, not production `main`.
- Therefore no native/production component, upstream vendor, accepted-result policy, numerical cutoff, RNG seed, v1–v13 contract, frozen golden, source-SHA fixture, or historic Stage-2 measurement-withholding file changed **in this follow-up delta**. The core source still pins PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`. This is an isolation finding; it is not a new wide re-audit of the earlier reviewed v14 production diff.

## Evidence provenance and execution boundary

1. **Personally inspected code** at the exact feature HEAD: the 173-line new test, unchanged native inspection helper, fixture, composition/geometry rules, native-interface observer, CLI native-run checker, and observable qualification gate. The helper wraps actual loaded pinned-native `onRayIncident` callbacks and delegates them; it does **not** supply precomputed intersections or inject a ray itinerary.
2. **Independently executed numerical calculations**, using Python 3.13 standard-library mathematics: per-polarization Fresnel transmission through successive G1 faces and G2 entry, plus the separate F2 ray–face geometry, TIR criterion and top-face Snell refraction. These calculations are *not* executions of the opticsim JS/PhyDemo runtime.
3. **Personally inspected source GitHub Actions run metadata, jobs and log lines.** All **11/11 standard workflows** for the current PR head report success. [Unified run 44024873262](https://github.com/physicsvigilante/opticsim/actions/runs/44024873262) and [planar/real-Chrome run 44024873455](https://github.com/physicsvigilante/opticsim/actions/runs/44024873455) both report `head_sha=fe3a030be7bfba8e5808e4e1e2e66d6815e7add7`, `conclusion=success`, Node **v24.19.0**, and **806 tests / 806 passed / 0 failed**. Both logs contain `R2_F1_NATIVE_EVIDENCE` and `R2_F2_NATIVE_EVIDENCE`.
4. **Exact-code clarification:** GitHub Actions actually checks out the PR's synthetic merge commit `0206bf1d5a7ea6e9cc73b60b08a0e71f889ad84e` (against `d3509e82...`), rather than checking out the feature commit as detached HEAD. I independently compared the two commits' Git trees: **both have tree SHA `13ad1c921800a02b187acbb6e860a73dac1f68d9`**. Thus the tested file contents are identical to the specified source HEAD; do not mistake identical-tree CI for a separate reviewer-native rerun.
5. **Independent native-execution limitation:** this reviewer environment has Node **v22.16.0**, not the required >=24.19, and cannot resolve the public GitHub hostname for a fresh checkout. I did **not** run `npm run setup`, the build, native tests, or Chrome locally, and did **not** authenticate the Chrome screenshots/artifacts visually. All native values below are **source-CI-observed**, independently checked against physical mathematics and source gate code.

## F1 — native full Fresnel, polarization and qualification

The test loads the real authored synthetic fixture with source at **(-200,10) mm**, incidence direction **10°**, relative source power **0.5**, common exterior index **1**, G1 inside index **1.5**, G2 inside index **1.3**, and sets **`partialReflection:true` for both**. It evaluates through the pinned native core and captures first actual per-ID finite-glass callbacks.

Independent unpolarized Fresnel at G1's n=1 -> 1.5 first face yields `R_s=0.04165948666806429`, `R_p=0.03837148336099077`, so `R=(R_s+R_p)/2=0.04001548501452753`. Independent Snell predicts **6.647777092829°** transmission inside G1; the reflected direction reverses horizontal propagation and preserves positive vertical propagation.

| First-trace quantity | Independently computed | Source-CI native diagnostic |
|---|---:|---:|
| G1 first incident relative power | 0.5 (authored) | 0.5 |
| G1 reflected power | 0.020007742507263764 | 0.020007742507263775 |
| G1 transmitted power | 0.4799922574927362 | 0.4799922574927362 |
| G2 first incident power | 0.4607864858766648 | 0.4607864858766648 |
| G2 first transmitted power | 0.4529440199529672 | 0.4529440199529672 |
| G2 physically reflected but natively omitted power | 0.007842465923697655 | `nativeTruncation=0.007842465923697658` |

**Importantly, G2 is not assumed unpolarized.** To obtain its incident power independently, transmit each of the original 0.25 s/p components through **both G1 faces**, giving `0.25[(1-R_s,G1)^2+(1-R_p,G1)^2]=0.4607864858766648`. Then apply distinct G2 Fresnel s/p coefficients (`R_s,G2=0.017831164354990516`, `R_p,G2=0.01621385387733092`). This predicts the omitted weak G2 reflected power and surviving transmitted power above to floating-point precision. Native G2 first-angle transmission **7.676257253054°** also matches independent Snell.

The actual G1 first event has **two native outgoing branches** with correct relative powers and observed directions. The actual G2 first event has **one propagated transmitted branch**, no propagated reflected branch and the **positive, correct native truncation**. Its missing branch is **not** interpreted as zero physical reflectance; this is the unchanged native brightness cutoff.

The logged complete F1 diagnostic says `status=incomplete`, **total native truncation `0.016320925290886495`**, **`undefinedBehavior=0`**, and **all three requested statuses `suppressed`**. The separate forced-depth case reports `status=incomplete`, `truncation=0.4799922574927362`, all three results suppressed, and its test explicitly asserts each `value===null`.

**Withholding is implemented, not merely asserted in a test:** `scripts/author-scene.mjs` snapshots native observations only for completed runs, and `src/observables.js` demands both matching canonical scene SHA and `executionPassed===true` with a native status `completed` or `completed-with-warnings`. Otherwise it returns `status:'suppressed'` from a result base with `value:null`. The new test verifies that this gate is exercised in the normal incomplete F1 case and the independent low-depth case.

**F1 verdict: CLOSED as a release-evidence gap**, for the bounded source fixture and tested contract. Neither the test nor this review claims comprehensive grazing/critical-edge or deep Fresnel-tree certification.

## F2 — independent internal TIR then top-face exit

The fixture is otherwise unchanged, except the source moves to **(340,-50) mm** and points at **60°**. The test uses the native-inspection wrapper against actual Glass objects and also runs the ordinary public evaluation/qualification pipeline.

Independent geometry gives G2 first right-face hit **(350,-32.679491924311236) mm**. At the n=1.3 -> 1 boundary, critical angle **asin(1/1.3)=50.284862768174°**; **60° is unambiguously TIR**. The reflected ray goes up-left and meets a *different*, top face at **(273.3974596215561,100) mm**. This second encounter has internal normal incidence **30°**, giving outside transmitted angle **asin(1.3 sin 30°)=40.541601873505°**.

The exact-head source CI logs first G2 outcome **`total-internal-reflection`**, `from:'inside'`, indices **1.3 -> 1**, first-hit **(350,-32.67949192431115)**; second G2 actual top-face outcome **`transmission`** at **(273.3974596215559,100)** and **40.54160187350326°**. Both event directions and native branch cardinalities are checked. G1 has **zero actual callbacks** and no authored or helper-fabricated route. G2 reports **two encounters and one TIR**.

The public native run is `completed`; the three requested sampled native counts are **[1,2,0]** for G2 TIR, G2 encounters, G1 encounters, each `qualified` (not a claim to image detection, source-specific history or universally correct optics). The existing Fresnel-off fixture policy remains explicit in this separate F2 case.

**F2 verdict: CLOSED as a release-evidence gap.**

## F3 and older-contract isolation

The optional diagonal fixture has 20 x 20 mm squares centered at **(0,0)** and **(20.008,20.008)**. Their shortest Euclidean gap is **sqrt(2) x 0.008 = 0.0113137085 mm > 0.01 mm**, but projected clearances on either relevant full supporting face are **0.008 mm < 0.01 mm**. The test correctly asserts **conservative rejection**, not a spurious overlap admission. Moving the second center to **(20.011,20.011)** supplies a **0.011-mm full-face separating certificate** and is accepted. Neither margin, physical solver nor scope was relaxed.

The GitHub compare plus successful pre-existing suite and 11 standard workflows support preservation of v1–v13/goldens/native-vendor/frozen evidence and existing Stage-2 withholding under this **test-only follow-up**. Historic failures were not recast as successes.

## Residual limitations and nonblocking test-strengthening suggestions

- **No independently executed pinned-native run or browser rerun** by this reviewer: source CI and mathematical reference are distinct evidence types. The positive verdict is **scoped to resolving F1/F2 evidence gates**, not an independent complete physics certification.
- In F1, the branch that attempts a completed-run Snell check is effectively unreachable *in the current fixture* because the test already asserts `status==='incomplete'`. Direct native log angles and this review's separate Snell calculations fill that targeted evidence need; a later explicitly completed Fresnel trace could make the conditional branch useful. Optionally assert the CI-observed `undefinedBehavior===0`, the incident 10°/0.5 invariants, and `value===null` in the ordinary incomplete case, rather than relying on the retained implementation's null-base guarantee. These are **test-hardening suggestions, not substantive v14 defects or prerequisites to owner decision**.
- Near-critical self-hits, native cutoff/truncation, and limitations already documented in historical numerical issues **#21/#23** remain real residual risks. The source still must not silently qualify incomplete runs; this candidate demonstrably withholds them. No claim of physical image inference, continuous power, original-problem correctness, teacher/student outcomes, or unconstrained media composability is made.

## Final disposition

**CLEARED FOR OWNER DECISION**, explicitly **not** independent approval to merge and not `CHANGES REQUESTED`. The final candidate is test-only relative to the independently reviewed v14 production HEAD, and the two targeted missing native-composition evidence cases now have source CI traces agreeing with independent physical calculations plus correct incomplete-result handling.

Leave source **PR #107 draft/unmerged** pending explicit owner authorization and whatever separate sign-off requirements the owner retains. This review was written independently; it does not alter source PR #107, the previous Chat B review, production files, CI configuration or accepted measurement policy.
