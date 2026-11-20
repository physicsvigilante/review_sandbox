# Independent Chat B review — Opticsim PR #187 (JEE J17)

**Date:** 2026-11-20 (IST)  
**Final verdict: CLEARED FOR OWNER DECISION**  
**Review type:** independent source/physics/code/evidence review, read-only on `opticsim`; not a blind LLM assessment or independent full-suite execution.

## Frozen identities and scope

- Reviewed PR: [physicsvigilante/opticsim#187](https://github.com/physicsvigilante/opticsim/pull/187), **draft, open, unmerged** at review.
- Exact source commit: **`3caa32fcd5d09115e0db2ef7868c427dba0f9f33`**; Git tree **`3eda4670db1d214c1d374dcc438f36369baa0ae1`**.
- Tested GitHub synthetic merge: `6689b1d4e9981803424a212be0f15617232b1264`, independently fetched as a Git commit; tree **`3eda4670db1d214c1d374dcc438f36369baa0ae1`**, exactly the source tree; ordered parents `eba628e37a21030364c3fc69755e160eb4b4c81f` (production baseline) and exact PR head.
- PR changes **seven added files only**, no modified or deleted production files: analytical query, byte-bound CLI, frozen protocol, JSON example, two tests, and documentation.
- Native PhyDemo pin remains `811f508d2b070898c241a568b0c167dcb8645251` (`upstream-pin.json`). The existing `scripts/setup.mjs`/`scripts/build.mjs` verify the checkout commit and clean vendor tree.
- Frozen protocol `evaluation/jee-two-source-lens-coincidence-v1/frozen-protocol.json` was independently retrieved at earlier commit `c5265133fb58a742a9c16300c4c5bc8391b85d37`. A commit comparison confirms the six implementation/documentation/test paths were added afterward. This is a frozen developmental protocol, not an unseen solution.

## 1. Original problem and source-fact boundary — PASS

I independently downloaded the original source audit CI archive from run [44360693719](https://github.com/physicsvigilante/opticsim/actions/runs/44360693719), artifact `14454755556`, extracted **only** `jee-post164-coverage-v1/sources/J17.png`, and visually inspected the original **Problems** image. Its independently recomputed SHA-256 was **`42364c9242e377fbdf4de4360450e980530626cbfe14992ac1fa089908a62e7b`**, matching the frozen manifest and protocol. I did **not** open any Solutions image.

Actual statement: two point light sources are 24 cm apart; find placement of a converging lens with focal length 9 cm so their images form at the same point. The statement does not specify a three-dimensional alignment, lens aperture, ray emission directions, brightness, or detector. The PR correctly labels coaxial sources and an ideal/paraxial thin lens between them as **explicit additional modelling assumptions**, not measurements inferred from the source. Its original-JEE-success and physical-image claims remain limited.

## 2. Independent mathematical audit — PASS

Take source coordinates `0` and `d>0`, lens at `0<a<d`, focal length `f>0`. With left-incident light moving +x and right-incident light moving −x, positive image distance is along its own incident direction. Thus

```text
uL = a,       vL = f*a/(a-f),       xL = a+vL
uR = d-a,     vR = f*(d-a)/(d-a-f), xR = a-vR
xL = xR (finite) <=> 2*a*(d-a) = f*d
a = (d +/- sqrt(d*(d-2*f)))/2
xcommon = a*d/(2*a-d)
```

The two conjugate relations and algebra were checked independently of the implementation. For `d=24 cm, f=9 cm`, solutions are **`a=6 cm`** with global image **`x=-12 cm`** (left virtual/right real), and **`a=18 cm`** with **`x=+36 cm`** (left real/right virtual). A common *signed Gaussian coordinate* is not two coincident native detector detections.

For `d<2f`, the discriminant is negative; for exact `d=2f` the only algebraic root has both objects at the respective focal distances and there is **no finite image**. For `d>2f` there are two distinct finite roots before the stated conservative numerical guard. A lens wholly outside the two distinct same-side sources cannot produce equal finite image coordinates because the Gaussian same-side distance map `u -> f*u/(u-f)` is injective wherever finite. Thus excluding exterior placements is justified in the explicitly restricted model.

I inspected the implementation's strict seven required fields, explicit model and coordinate convention, finite numeric validation, units mm/cm/m, 1–10,000 mm bounds, unknown-field refusal, and separate status values for `no-finite-placement`, `numerically-indeterminate`, and rejected input. Exact `d=2f` is checked before the near-double-root guard; the guard conservatively withholds near-singular outputs, and focal/coordinate/residual checks prevent silently assigning divergent finite images. `maximumSignedGaussianCoordinateMismatchMm` is computed as a **nonnegative absolute mm residual** among independently evaluated conjugates, not a dimensionless ratio. No mathematical blocker found.

## 3. Pinned-native witness and non-hit — PASS WITH EXPLICIT SCOPE LIMIT

I read all of `test/jee-two-source-lens-coincidence-native.test.mjs` and the exact-head GitHub Actions test log (run [44668827623](https://github.com/physicsvigilante/opticsim/actions/runs/44668827623), job `136064633093`). The test constructs actual `SingleRay`, `IdealLens`, and `Detector` instances from `core.loadNative`, uses source rays directed to lens offsets ±5 mm, an **added** finite 100-mm lens aperture, finite brightness and detector, and runs **each source side separately**. Native callback wrappers delegate to their previous methods with the original arguments/this, then observe outgoing rays and actual detector intersections. The test checks lens incidents, emitted rays, completion, errors/truncation/undefined behavior, actual detector crossings, forward-vs-backward geometry, and a finite-aperture non-hit.

The exact-head log contains:

| Lens x (mm) | Gaussian x (mm) | Native incident source | Gaussian type | Native lens encounters | Actual detector crossings |
| ---: | ---: | :--- | :--- | ---: | ---: |
| 60 | −120 | left | virtual | 2 | 0 |
| 60 | −120 | right | real | 2 | 2 |
| 180 | +360 | left | real | 2 | 2 |
| 180 | +360 | right | virtual | 2 | 0 |

This is credible **pinned-native, test-only ray evidence**, not a reconstructed original J17 scene: real-source rays cross the passive detector and virtual-source rays only extrapolate backward to the mathematical point. The independent miss test verifies zero native lens encounters and detector crossings for rays aimed outside the declared aperture. The production analytical response and standalone CLI explicitly retain `native:{status:'not-run',observations:null,nativeImageDetected:false}`. The test does not assert simultaneous physical convergence or a source-independent image detector. I did not perform an additional local native-engine rerun; this conclusion uses source inspection plus the actual CI log.

## 4. Exact-head CI, original input and artifact integrity — PASS

- Read the GitHub Actions runs associated with the **exact PR head**. **11/11** pull-request workflows finished successfully. The existing native and real-Chrome regressions ran; there is **no new J17-specific Chrome scene/view**, and none is claimed.
- Inspected [run 44668827623](https://github.com/physicsvigilante/opticsim/actions/runs/44668827623) log: full Node 24 suite reported **1,059 tests, 1,059 passed, 0 failed, 0 skipped**. J17 signed inverse, negative input, near-focal and pinned-native witness tests appear explicitly.
- Independently downloaded exact-final [authoring archive artifact 14599352038](https://github.com/physicsvigilante/opticsim/actions/runs/44668827681/artifacts/14599352038). Its recomputed ZIP SHA-256 was **`4ac91a5a1ff6dda4cd9bfd18005341a1aeac0682d900d834ef9b4ac5594821b5`**, exactly matching GitHub artifact metadata. All **1,463** ZIP members passed the ZIP CRC test. All **293/293** adjacent input/report pairs *containing a declared original-input SHA-256* matched SHA-256 of the actual archived `input.json` bytes; seven other older pairs contain no such SHA field and were correctly excluded rather than treated as hash failures.
- The three new J17 analytical/negative/refusal archive attempts preserve their raw input bytes and `native:not-run`. `scripts/two-source-lens-coincidence-query.mjs` writes to an exclusively reserved new output directory, preserves `input.json` before analysis, hashes the original Buffer, and never synthesizes a native scene on successful, negative or rejected input. The reused output guard checks real ancestor directories; existing infrastructure explicitly does not claim protection against an adversarial concurrent filesystem process.

These are independent checks of remotely produced CI evidence and downloaded artifact bytes, **not** claims that I executed the entire pipeline myself.

## Findings and owner decision

**Blocking findings:** none within the stated narrowly conditional analytical-query scope.

**Nonblocking limitations to retain in release notes:**
1. Coaxial geometry, opposite illumination and an ideal/paraxial lens remain additional assumptions absent from the original image. No general 3-D source placement or real-image reconstruction is provided.
2. Native rays are a distinct, deliberately added teaching apparatus. A shared virtual/real Gaussian coordinate does not mean two source light fields physically converge on the same detector.
3. No new browser J17 visualization, blinded image-to-model grading, or update to the historical 20-case JEE success rate was established. Builder CI, even with independently audited archives, does not substitute for those evaluations.

**Final verdict: CLEARED FOR OWNER DECISION.** The math, strict bounded model, real/virtual distinction, provenance, native observations, and exact CI identities are sufficient for the proposed isolated scope. This is **not** an instruction to merge: retain the draft/release hold pending the owner's explicit decision. I made no changes to `physicsvigilante/opticsim`, did not merge, and did not modify any historical attempt or solution evidence.
