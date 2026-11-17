# Chat B — targeted independent R2 re-review of Opticsim native thick lenses (PR #110)

You are a **separate-context Chat B reviewer**, NOT the source implementer. The [original independently authored report](reviews/review-01-chat-b.md) remains immutable, with verdict **INSUFFICIENT EVIDENCE** on original source SHA `610d748e91f25f6233fb057932cabe6a62ed2a1a`; it found no demonstrated production defect but required adversarial native evidence R2-01/02/03. **Do not rewrite the first review or merely endorse the builder's new passing tests.**

## Exact source / dependency

- Source [draft PR #110](https://github.com/physicsvigilante/opticsim/pull/110), current follow-up HEAD **`80fec0bb05200ad6034bf55a00c6e522740b27e1`**. Compare from `610d748e91f25f6233fb057932cabe6a62ed2a1a`: **one newly added file only** `test/native-thick-lens-r2-review-regressions.test.mjs`, 411 lines; zero production edits. The author merged test-only [PR #111](https://github.com/physicsvigilante/opticsim/pull/111) into the v15 branch, then created an empty same-tree CI-attestation commit and added a final *test-only* polarization case. Verify this compare independently.
- Dependency v14 feature source `fe3a030be7bfba8e5808e4e1e2e66d6815e7add7`, [PR #107](https://github.com/physicsvigilante/opticsim/pull/107), remains reviewed but **NOT** merged/released; production main `d3509e82fb65d81aabe336666851f8f2962623f4`. PR #110 is likewise draft and must NOT merge to main before separate owner decisions.
- Native pinned PhyDemo SHA `811f508d2b070898c241a568b0c167dcb8645251`; test fixtures and source use unchanged original `SphericalLens`. No solver, randomness, cutoff, core native code, geometry admission or result-qualification semantics changed by this follow-up.

## What to independently evaluate

First inspect the [new exact-head test file](https://github.com/physicsvigilante/opticsim/blob/80fec0bb05200ad6034bf55a00c6e522740b27e1/test/native-thick-lens-r2-review-regressions.test.mjs), plus original `src/spherical-lens.js`, `src/planar-media.js`, `src/contract.js`, `src/observables.js`, `src/adapter.js` and original upstream `SphericalLens.js`/Glass. The test is not an independent numerical solver: it wraps actual native callbacks, classifies them with an *additional* reference geometry/Snell/reflection check and logs raw per-face outcomes. Verify that the test does not prescribe ray routes or retrofit native rays to expected points.

### R2-01 — reverse illumination and actual top/bottom rim faces

- Reverse source **(400,10) mm directed 180°**, exterior indices 1, two ordinary biconvex lenses. Actual source-CI lens encounter order **L2 back, L2 front, L1 back, L1 front**, with x approximately `164.498743711, 135.435871918, 14.973863408, -14.996035356` mm. Reverse incoming side and both front/back exiting media must use actual native observed normals, indices `1 -> nInside` then `nInside ->1`. Recompute an independent reversed ray/circle/Snell reference, and confirm detector crossing without a prescribed authored route.
- Both rim cases use **one lens**, R=100, a=50, d=2·sag+1.02 mm (about a 1.02 mm rim), source at (−200,+55) or (−200,−55) targeting the middle of the top/bottom straight rim. Actual native first callback is **(0,+50) or (0,−50)**, with `faceId` top-rim/bottom-rim, outward normals (0,+1)/(0,−1), `outside -> inside 1 -> 1.5`, incidence **88.5679038158°**, transmitted angle **41.7943097408°**. Both complete natively without truncation and qualify sampled counts. Validate independently against a separate rim-line and Snell calculation. A subsequent native ray can interact with other faces: do not invent a full route.

### R2-02 — numerical/clearance boundary controls

- Actual pinned native six-point paths are finite and actual curved-face callbacks completed for the admitted extreme cases: **a=50, Rfront=Rback=51, d=90** (near minimum allowable R), **a=2, R=10000, d=2** at x=0 and x=9998 near coordinate limit, and **a=50,R=100,d=2·sag+1.0001** giving a near-minimum rim. Test independently whether native path endpoints agree with the continuous spherical geometry and identify remaining floating-point sensitivity.
- Verify conservative **0.011 mm** interlens axial gap, source-to-first-vertex entry and exit-to-detector crossing: the tested axial rays recorded actual two lens events per component and a real detector crossing. Verify **0.009 mm** neighboring cases reject before native execution and do not treat a tolerance as a universally certified numerical precision.
- Forward near-rim incident ray geometry: a horizontally displaced target by **0.005 or 0.02 mm** from a rim/arc corner still has perpendicular ray-to-corner clearance *below* 0.01 mm and must be refused. A **0.5 mm** target shift clears the actual perpendicular guard; native callbacks recorded an unambiguous top-rim hit at about (−1.1025403784,+50) with completion. The earlier test's mistaken assumption that 0.02 mm horizontal offset was sufficient produced a genuine failed CI run. Do not retroactively mark that first failure as success: the positive-control geometry was corrected, not the numerical guard weakened.
- These are representative finite test points, not a proof of all floating-pathological parameters. Identify any reproducible unsafe admissions.

### R2-03 — stable near-critical TIR and s/p Fresnel power

- Use the one-lens fixture with entry front face at `(-6.6515138991,40)` mm. Source is at x=−200, with angle **−21.3°** and y≈**115.383424687**, or angle **−22°** and y≈**118.117859110**. Actual back-arc inside-to-outside incidence angles **41.680155112°** (subcritical, transmitted) and **42.039189973°** (TIR/reflected). Critical n1.5→1 is **41.810314896°**. Source-CI confirms per-face normals, 1.5→1 material indices, correct reflected direction, absent transmitted TIR branch and completed native status; no route was forced.
- Actual first-interface Fresnel input before s/p powers **0.25 each**, with independent references **Rs≈0.04053886672369661**, **Rp≈0.039464440142489655**. Actual pinned native reflected powers **s≈0.010134716680924152**, **p≈0.009866110035622414**; transmitted **s≈0.23986528331907586**, **p≈0.2401338899643776**. Verify separately, not merely by summed relative intensity. The complete Fresnel tree is still **incomplete**, with truncation about 0.00078118545 in the single-lens test; public requested outputs remain suppressed. Never silently call omitted branches physically zero.
- For all cases, inspect and distinguish **native execution observed by source CI**, separate independent calculations, and any native execution that you actually performed.

## Source CI and execution provenance

- The test-branch candidate `5bb0b59d1b60e5f163392a9703f0e89116e6c7a9` passed **819/819 Node 24 tests and 11/11 workflows**, including real Chrome. The additional polarized-power test was added at exact new source HEAD `80fec0bb05200ad6034bf55a00c6e522740b27e1`; Node suite **820/820 passed** in a completed source CI job. **Inspect final 11-workflow conclusions at this exact new head before signing off.** Existing standard workflows run on PRs targeting main; the source PR was temporarily main-targeted solely to trigger CI and must be retargeted to its proper v14 dependency afterwards.
- Source CI may check out a generated synthetic merge commit, not directly a detached HEAD. Independently check the synthetic merge and source Git tree SHAs to confirm identical file contents. A green CI is NOT a distinct reviewer's native reproduction.
- If your environment cannot install the pinned Node >=24.19/native core, report it, and independently recompute physical scalars using your own method. Do not claim human-expert endorsement or browser screenshots you did not actually inspect.

## Required independent output

Write a **new** separately authored report at `physicsvigilante/review_sandbox/projects/opticsim/pr-110/reviews/review-02-chat-b.md`. Record exact final source HEAD, changed-file isolation, independent calculations vs native CI evidence, any confirmed bugs or residual numerical regimes, and a clear verdict:

- **CLEARED FOR OWNER DECISION** only if all material R2-01/02/03 evidence gaps are sufficiently closed for bounded v15;
- **INSUFFICIENT EVIDENCE** for remaining essential uncertainty;
- **CHANGES REQUESTED** for a reproducible implementation defect.

Never edit the first review or source code and never merge source PR #110. Its separate v14 dependency #107 is also held pending owner decision. Do not treat original-text interpretation, detected images, or educational usefulness as certified by this physics review.
