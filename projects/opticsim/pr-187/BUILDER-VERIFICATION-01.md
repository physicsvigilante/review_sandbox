# Opticsim PR #187 — exact-source JEE J17 inverse and native witness: builder verification

**Date: 2026-11-20 (IST). Builder evidence only. Status: DRAFT/UNMERGED; independent physics review PENDING.** This is a source-backed developmental physics milestone, not a blind independent LLM interpretation grade, not real image reconstruction, and not an automatically re-scored 20-case JEE success rate.

## 1. Exact original source and frozen protocol

J17 is the frozen **Problems-only** image from the established PR165 20-case sample:

- Path: `08_Ray_Optics_Explanations/07_Lens_Formula/Problems/001.png`
- Original PNG SHA-256: **`42364c9242e377fbdf4de4360450e980530626cbfe14992ac1fa089908a62e7b`**
- Source: two point light sources separated by 24 cm, converging lens focal length 9 cm, find where to place lens so the sources' images coincide.
- Source inspection: the **problem image only** was independently re-opened from the frozen CI artifact; source PNG bytes were checked against its saved manifest. **No Solutions image was opened.**
- The original does **not** state finite lens aperture, source brightness, emitted ray directions, source/detector coordinates or a native detector. Coaxial 1D point sources and ideal/paraxial imaging are *explicit added modelling assumptions*.
- The mathematical and native test expectations were frozen in `evaluation/jee-two-source-lens-coincidence-v1/frozen-protocol.json`, committed **before implementation** at `c5265133fb58a742a9c16300c4c5bc8391b85d37`, including J17 lens distances [6,18] cm and shared Gaussian x [-12,+36] cm.

This first-source audit history is unchanged; this is a **same-assistant, disclosed source-backed developmental follow-up**, not an unseen benchmark or independent pedagogical evaluation.

## 2. Exact Git identity and unchanged native engine

| Identity | Verified SHA |
|---|---|
| Actual released baseline `main` (independently reviewed v25) | **`eba628e37a21030364c3fc69755e160eb4b4c81f`**, **11/11 actual postmerge workflows success** |
| PR187 exact final source head | **`3caa32fcd5d09115e0db2ef7868c427dba0f9f33`** |
| Final source Git tree | **`3eda4670db1d214c1d374dcc438f36369baa0ae1`** |
| Tested synthetic PR merge | `6689b1d4e9981803424a212be0f15617232b1264` |
| Tested synthetic PR merge Git tree | **`3eda4670db1d214c1d374dcc438f36369baa0ae1`**, identical |
| Tested synthetic merge ordered parents | [production baseline, exact PR187 head] |
| Native PhyDemo checkout pin | `811f508d2b070898c241a568b0c167dcb8645251` — **unchanged** |

The builder separately read the exact Git source and synthetic merge **commit objects** to verify equal trees; this is not a claim that CI itself tested equality in its job. Diff: **exactly seven ADDED paths, no modified/deleted production files**, no old schema or UI changes, no upstream patch, no new native tracer. The seven paths are a frozen protocol, isolated analytical query source, byte-bound standalone CLI, exact source-conditional JSON example, two tests (mathematical/CLI and raw native witness) and documentation.

## 3. Independent two-sided Gaussian derivation, including physical distinction

In a conditional first-order ideal **coaxial converging thin-lens** model, source 1 is x=0, source 2 is x=d>0. Lens coordinate a lies strictly in (0,d); left light travels +x, right light −x. Positive v is measured **along each corresponding incident-light direction**:

```text
uL = a;      vL = f*a/(a-f);       xImageFromLeft  = a + vL
uR = d-a;    vR = f*(d-a)/(d-a-f); xImageFromRight = a - vR
xImageFromLeft = xImageFromRight
=> 2*a*(d-a) = f*d
=> a = (d ± sqrt(d*(d-2*f))) / 2
```

For **d>2f** there are exactly two distinct finite roots, and the common conditional global Gaussian x is `a*d/(2*a-d)`. For the original d=24 cm and f=9 cm:

| Conditional lens x measured from source 1 | Common calculated Gaussian image x | Source 1 | Source 2 |
|---|---|---|---|
| **6 cm** | **−12 cm** | **virtual** | **real** |
| **18 cm** | **+36 cm** | **real** | **virtual** |

These are **coincident mathematical Gaussian coordinates, not two actual physical detector hits**. The virtual branch only has a **backward extension** of outgoing native rays to the common coordinate. d<2f gives negative discriminant and no finite placement; d=2f yields the unique midpoint with both objects at focal distance and no finite image (not a fabricated point at infinity); a near-double-root numerical region is withheld, not silently assigned enormous finite values. Lens positions outside both sources cannot give the same finite image for two distinct same-side object distances under the strictly injective ideal thin-lens map.

The new query `src/two-source-lens-coincidence-query.js` requires all seven explicit fields (`format,kind,model,coordinateConvention,lengthUnit,sourceSeparation,focalLength`), refuses unknown fields and nonfinite/text/invalid numeric facts, supports canonical mm/cm/m with [1,10000] mm bounded input, reports real-vs-virtual branches and `maximumSignedGaussianCoordinateMismatchMm` in **absolute millimetres**, and withholds numerical degeneracy. Both "no-finite-placement" and "numerically-indeterminate" remain distinct from an invalid input.

`scripts/two-source-lens-coincidence-query.mjs` produces byte-preserved `input.json`, SHA-256-bound `analytical-result.json` and `report.json` in a new exclusive output directory. Every analytical response has **`native:{status:'not-run',observations:null,nativeImageDetected:false}`**. No native scene is created, and negative/invalid requests do not invent detectors or images.

## 4. Genuine pinned PhyDemo native *separate teaching witness*, not an original-JEE solution

The separate **test-only** `test/jee-two-source-lens-coincidence-native.test.mjs` runs genuine pinned `SingleRay`, `IdealLens` and `Detector` objects with a new declared teaching apparatus: 100 mm native finite lens aperture, rays aimed at ±5 mm lens offsets, source brightness 0.5, a finite passive detector at the *conditionally predicted real-image coordinate*. Those facts are **not** in original J17 and never become original-source claims.

Each side/source is simulated **separately** so that actual detector crossings cannot be spuriously attributed between two sources. Native `onSimulationStart`, `IdealLens.onRayIncident` and `Detector.onRayIncident` are wrapped **only to observe**, delegate original pinned methods once with the same this/args and return, and record the real outgoing direction/endpoint and genuine detector hit.

**Exact-final CI native witness:**

| Lens x (mm) | Predicted Gaussian x (mm) | Incident source | Mathematical image type | Actual native lens encounters | Actual native detector crossings |
|---:|---:|---|---|---:|---:|
| 60 | −120 | left | virtual | 2 | **0** |
| 60 | −120 | right | real | 2 | **2** |
| 180 | +360 | left | real | 2 | **2** |
| 180 | +360 | right | virtual | 2 | **0** |

All four native scenes finished with zero errors/truncation/undefined behavior. Native outgoing ray line extensions were checked against the frozen Gaussian coordinate, with forward-direction geometry explicitly distinguished from *backward-only virtual extrapolation*. Separate rays aimed outside the true finite lens aperture **missed** it and did not produce a detector crossing. These tests **do not** detect an image from two sources or turn the analytical inverse into a native capability.

Native evidence and analytical conclusion are separate: the analytical J17 result remains `native:not-run`; independent raw native research supplies **bounded physical plausibility**, not a source-faithful original ray scenario or a native image detector. No fabricated path, source attribution or image reading is asserted.

## 5. Exact-final CI, source hashes and archive integrity

- Final PR187 source `3caa32fcd5d09115e0db2ef7868c427dba0f9f33`: **11/11 PR CI workflows SUCCESS**. [Optical composition run 44668827681](https://github.com/physicsvigilante/opticsim/actions/runs/44668827681) (job [136064610579](https://github.com/physicsvigilante/opticsim/actions/runs/44668827681/job/136064610579)), all other workflows passed including existing Node/native/real Chrome regression suites.
- Final exact-head Node 24 suite: **1,059/1,059 tests passed, 0 failed/skipped**. [Quasi-static motion run 44668827623](https://github.com/physicsvigilante/opticsim/actions/runs/44668827623) logs the native J17 witness array and the source-frozen conditional J17 root test. Neither builder CI nor this report is a blind independent reviewer rerun.
- Downloaded actual final [`llm-authoring-evidence` ZIP artifact 14599352038](https://github.com/physicsvigilante/opticsim/actions/runs/44668827681/artifacts/14599352038), recomputed SHA-256 **`4ac91a5a1ff6dda4cd9bfd18005341a1aeac0682d900d834ef9b4ac5594821b5`**, **identical to published GitHub digest**. All **1,463 ZIP members passed CRC integrity**.
- Recomputed **293/293** adjacent raw `input.json` versus `report.json.inputSha256`/`originalInputSha256` pairs **without mismatch**, including all **three J17** conditional/no-finite/refusal attempts. They preserve original input bytes, output restrictions, and no source image or solution.
- No new J17 real-Chrome view was implemented; existing historical real-Chrome workflows passed. The new output is a standalone **reduced analytical query**, not a new public native optical scene family or browser image detector.

The original J17 source PNG was separately extracted from the frozen source-audit artifact with a matching SHA-256 and **only the problem image inspected**. No Solutions files or earlier first attempts were modified.

## 6. ONE independent review required — not routine repeated reviews

Review the exact [PR187 source](https://github.com/physicsvigilante/opticsim/pull/187) at **`3caa32fcd5d09115e0db2ef7868c427dba0f9f33`**, tree **`3eda4670db1d214c1d374dcc438f36369baa0ae1`**, and tested synthetic merge `6689b1d4e9981803424a212be0f15617232b1264`.

Review scope:
1. Original frozen J17 source statement and expressly **added coaxial ideal thin-lens** assumption; no invented 3D geometry. First-order signed conjugate derivation, both quadratic roots and real/virtual branch orientation. Exact focal/infinity threshold and safe near-double-root numerical withholding.
2. Read the strict typed query, bounds, units, source-byte SHA runner and no-native distinction; check source-mutability, refusal and no finite image status.
3. Inspect **actual pinned native** witness and non-hit: true source emission, IdealLens incident/intersection, detector counts, forward real hits versus backward-only virtual extension. Test-only finite lens and detector do not become original facts or a detection claim.
4. Exact final Git source tree vs CI-tested synthetic merge; 11/11 CI, 1,059 Node tests, archived hash/CRC checks. No need to re-review unchanged upstream PhyDemo lens physics, older schemas or GRIN v25 release.

**Deliverable:** Commit one complete independent Markdown report to the default branch of `physicsvigilante/review_sandbox` at

`projects/opticsim/pr-187/reviews/review-01-chat-b.md`

Read back the committed report, return its **immutable permalink**, review commit SHA, exact Opticsim source SHA, and final verdict **CLEARED FOR OWNER DECISION** or **CHANGES REQUESTED**. Chat-only verdict is insufficient. Do not modify source or merge. If publication fails, report not published.

**Current status:** Builder CI verified, final exact-head source and artifacts fixed, PR187 **draft/open/unmerged**. Production `main` remains independently reviewed and post-merge-tested at `eba628e37a21030364c3fc69755e160eb4b4c81f`. A reviewer decision is not yet published; production J17 analytical query is not released.
