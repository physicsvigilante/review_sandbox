# Independent review of Opticsim PR #195

**CHANGES REQUESTED** — Codex, independent reviewer, 21 November 2026. This single review covers the frozen feasibility experiment and the public v27 implementation. One numerical admission defect remains. Ordinary separated-slab examples, historical isolation, archival integrity, and the browser workflow passed the checks below.

## B1 · An admitted ray can enter the declared 0.1-mm endpoint exclusion zone

The Snell admission calculation uses ideal slopes and actual native emitter positions. The subsequent native intersections and outgoing directions accumulate different floating-point errors. The strict comparison in the [v27 validator](https://github.com/physicsvigilante/opticsim/blob/e7e2d199b6be25265decb6f7ec7826a3477ab24f/src/native-beam-two-plane-mirror-v27.js#L109-L139) leaves no allowance for the discrepancy. The public pipeline can qualify a detector event whose own reported position violates its advertised margin.

**Reproduction through public results alone.** Start with the PR's `examples/native-parallel-two-plane-mirror-v27.json`. Apply the following parameter overrides in millimeters and degrees, retaining the baseline indices, reflection policies, width, brightness, requests and sampling policy.

| Component | Changed parameters |
| --- | --- |
| B1 | x = −9200, y = −9500, directionDeg = 9 |
| I1 | x = −9100, y = −9500 |
| I2 | x = 9000 |
| M1 | x = 9001, y = −7583.479649612028, length = 1000 |
| D1 | x = −9110, y = −6168.458044780914, length = 1000 |

Run `prepareScene`, `evaluateDocument` with the pinned core, then `evaluateObservables`. Compare D1's upper endpoint with the highest y in the public `detector-hit-events` list. The witness predicts **0.10004000000026281 mm** clearance. The upper endpoint is −5668.458044780914 mm and the highest native hit is −5668.558000367068 mm, giving **0.09995558615446498 mm** clearance. All seven requests qualified with zero truncation. Counts were 8 emissions, 16 contacts at each face, 8 reflections and 8 detector crossings. The finite detector intercepts the returning samples in this geometry. The predicted-to-observed discrepancy exceeds 0.000084 mm. An epsilon based only on the last few floating-point bits of 0.1 would miss it.

**Independent mirror reproduction.** Start again with the baseline. Translate every component by (−9000, −9000), set B1 direction to 58°, M1 length to 1000, M1 y to −9217.707181881648 and D1 length to 1200. Public authoring accepted the scene and all seven requested results qualified. A read-only wrapper around the actual Mirror instance's `onRayIncident`, delegating once, recorded maximum y = −8717.80718187171 at x = −8910. The mirror upper endpoint is −8717.707181881648. The admission margin was **0.10000000100080797 mm**, and the observed clearance was **0.09999999006322469 mm**. The mirror still reflected all eight rays. This finding concerns the numerical safety guarantee, not a demonstrated missed mirror or an error in the baseline counts.

**Required correction.** Make the v27 qualification fail closed when mirror or detector clearance from a native sampled encounter cannot be assured. Preserve the 0.1-mm optical margin and document the numerical uncertainty separately. Use defensible bounds for the admitted geometry or restrict it accordingly. If checking observed hits, address finite misses as well and retain the promised pre-native admission behavior. Cover the two reproductions, inside/outside endpoint cases, both detector legs, translated/long-span geometry and ample-clearance positives. Keep native propagation and historical contracts intact. Recheck on the corrected head.

## Source and scope

- Reviewed feature HEAD `e7e2d199b6be25265decb6f7ec7826a3477ab24f`, tree `83e3dc418784c9c233267527b0e0dd99576899a5`. I fetched and inspected the Git object for synthetic merge `3194bb332531a37950b6c6d6634951f4b1513e8c`. Its tree matches and its parents in order are `4f81a1625cc45ce731d3ee0e286ff3173f72f4fe` and the reviewed feature HEAD.
- Compared the 15-file base-to-head change (nine additions, six modifications). The eleven-case protocol at `e3f18c39bc83cae77d86d8c2e672c2411442627b` precedes the committed raw experiment. The frozen and final blob is `9ac5a79bbdc945b01c1e969964ebe4231c0aeb8d`. Protocol file SHA-256 is `398ea13f95cf9a0d6339b33466c4fc7688960a439fcb7f8386a4ad2f09a833f7`.
- Independently deep-compared all 32 historical profile definitions and historical selection entries against base. Forging the complete v27 apparatus as v19 or v26 was refused. The corrected v26 sampler is the same Git blob `18f96f68608152d176f79f43f4cc012d011a5bc8` as at `3564886de1372e4f9d74bb771f90f87a8944dd75`. The v27 witness calls it directly, checks the half-integer withholding band, and enumerates every admitted sample.
- Confirmed the explicit slab/exterior index consistency, both Fresnel-off requirements, full emitter clearance, bounded forward direction, finite vertical mirror and detector, absence of extra optics, minimum 1-mm slab and mirror separation, and the source-side detector test relative to the entire Beam. Reproduced the 1-mm positive and subthreshold refusals. A detector placed between the Beam center and its forward endpoint was refused. B1 concerns the numerical realization of the sample margin after emission.
- Rebuilt both bundles from the Git-exported head with Node 24.19.0 and the verified unmodified PhyDemo checkout at `811f508d2b070898c241a568b0c167dcb8645251`. Ran both new Node test modules and the two changed historical test modules, **29 passed**. I also ran 45 native variants spanning 0° to 60°, equal indices through a 4:1 ratio, reversed component order, flipped segment orientation, and translations to x offsets of ±9000 mm. All retained the expected counts with generously sized segments.

## Signed optics and frozen native evidence

With incident direction (cos i, sin i) and n₀ sin i = n₁ sin r, the front face changes the slope to tan r. The rear restores the exterior direction. A vertical mirror reverses x and preserves y. The return therefore adds the same vertical rise through each gap and slab. For i = 30°, n₀ = 1 and n₁ = 1.5, r = 19.47122063449069°. The front return shift is 2 × 60 tan r + 2 × 30 tan i = 77.06742302257038 mm. The source-side detector separation adds 2 × 10 tan i, giving 88.6144284063629 mm. Sorting the two observed cross-sections by y gave a maximum discrepancy of 4.95 × 10⁻¹² mm. This is a cross-section check without source ancestry.

I reran all eleven frozen controls. Baseline callback batches of eight were D, I1, I2, M, I2, I1, D. The positive controls were complete. The following counts are actual callbacks in the order emissions / front / rear / mirror / detector.

| Raw case | Counts | Terminal interpretation |
| --- | --- | --- |
| Baseline, translated, normal, higher index | 8 / 16 / 16 / 8 / 16 each | Complete |
| Denser | 16 / 32 / 32 / 16 / 32 | Complete |
| Mirror absent | 8 / 8 / 8 / 0 / 8 | Complete, no return |
| Mirror coincident with rear | 8 / 16 / **0** / 8 / 16 | simulationComplete, incorrect two-face route, public contact refused |
| 0.005-mm gap | 8 / 16 / 16 / 8 / 16 | Complete raw run, public geometry refused |
| First-face Fresnel on | 8 / 16 / 24 / 16 / 24 | Incomplete, truncation 0.1265077484007037 |
| Depth zero | 8 / 0 / 0 / 0 / 0 | Incomplete, truncation 3.1999999999999997 |
| Processing limit one | 8 / 0 / 0 / 0 / 2 | simulationStop |

Public zero- and one-detector positives completed. Two source-side detectors were refused before native execution. In a separate raw six-object control I instrumented the two detectors and three optical surfaces. At depth eight I measured eight callbacks per sample in order D2, D1, I1, I2, M, I2, I1, D1. Native truncation was 3.1999999999999997. A test-only depth-nine counterfactual measured the ninth D2 callback and zero truncation. The public depth limit stays eight. Stops and truncation suppressed the requested values. Feeding a valid edited scene its predecessor's complete execution suppressed all seven results. At 80 crossings the aggregate remained available and the entire positions value was unavailable/null.

## Public pipeline, browser, and archive audit

I reran public JSON acceptance. Four cases completed, five refused before native, and the baseline had 8 emissions / 16 front / 16 rear / 8 mirror / 16 crossings / 16 recorded positions. The four archived portable bundles passed qualification parsing. Recovered browser export preserved the origin input hash, width 40→20, and a coherent physical edit for both slab indices 1.5→1.8. It contained no cached results.

I independently ran the ten Chrome checks and produced six screenshots using installed Windows Chrome 158.0.8127.37, a fresh profile, and a loopback server. My disposable harness copy supplied the Windows binary/version and used the Chrome sandbox. The app, native bundle inputs and all acceptance assertions came from the reviewed source. I also inspected the builder's Chrome 158.0.8127.36 report and six screenshot members. The two invalid states clear the drawing and readings. Successful states include the edited and reopened configuration. The edited portable JSON downloaded by both browsers was byte-identical, SHA-256 `0230f4596f9837989d64c05b7748365eac5e90bd9c99e1bbdfec4ba8dee3d6fb`.

I downloaded these four GitHub Actions ZIPs and recomputed SHA-256 over the ZIP bytes. Each matched GitHub's run-bound digest.

| Artifact ID | SHA-256 |
| --- | --- |
| 14626013257 | `6cac155eec6cce37082581c510c7abdbc8ed23c378d5054af3edbbcc94e5b882` |
| 14626143133 | `3ed3beb32276a572c8cdacfd9d36c30b283c70604a1bf7998082cf751c43d651` |
| 14627065075 | `08d5fb0b87e27fff41068117043b922c76878b44bc9be9aaa512caca790dbbfa` |
| 14626486698 | `7a5710036eb8a6e41ba996b8afe3d998c944a55036c9e0d11494fb2a0dec6652` |

All 22 archived raw inputs/reports matched their manifest lengths and digests and my fresh output byte for byte. All nine archived public input hashes matched, and all 44 public case-directory members matched my rerun byte for byte. The raw summary SHA-256 was `4ba1e153e0d93ac91443cc8e4928a18c036064721c3905533ee3bc09cb43977d`. Public acceptance summary SHA-256 was `9ba98c60b598314fca98de9800bcf56f5ede685deaad5d5754084346c1507b49`. Baseline raw input/report hashes were `4b71b552ad479ed46c67ae102f0bcf5f1ff0f8ab228dca92a6297675e8a4e9ef` and `f9c62382f9199ce05f717fc59ecfa9e67ee6494532989a78aac752e5145873b6`. Baseline public input SHA-256 was `1f92dfaac8594b200ea1555958a20ecae130777710db11e4dc163ef038b3d26d`.

I read GitHub's eleven successful exact-head workflow statuses and the optical job log reporting 1,141 passes. The full-suite count is CI evidence. The focused Node, native controls, public acceptance, artifact verification and Windows browser results above are my own executions. The synthetic separated mirror still requires the authored gap and materials. No original J08 answer, independent teaching assessment or source-fidelity certification follows from this review.

[Builder handoff](https://github.com/physicsvigilante/review_sandbox/blob/5d27179659af42c3becd51a05ca1643e503b549b/projects/opticsim/pr-195/BUILDER-VERIFICATION-01.md) · [Reviewed source](https://github.com/physicsvigilante/opticsim/tree/e7e2d199b6be25265decb6f7ec7826a3477ab24f) · [Exact-head optical CI](https://github.com/physicsvigilante/opticsim/actions/runs/44730867302)
