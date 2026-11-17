# Opticsim PR #110 — R2 independent physical review request

**Status: REQUEST PREPARED, NO INDEPENDENT REVIEW VERDICT.** Do not merge PR #110 or treat Node/Chrome success as independent physics proof.

- Source [PR #110](https://github.com/physicsvigilante/opticsim/pull/110), exact source candidate HEAD **`610d748e91f25f6233fb057932cabe6a62ed2a1a`**, branch `feature/native-thick-lens-train-v15`.
- Source depends on reviewed but not yet released two-glass feature PR #107 at **`fe3a030be7bfba8e5808e4e1e2e66d6815e7add7`**. Production main currently `d3509e82fb65d81aabe336666851f8f2962623f4`. **Neither PR #107 nor PR #110 is authorized to merge to main by this request.**
- Pinned upstream PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`. Its original SphericalLens/Glass code is unmodified.

## New claimed scope

Isolated `schemaVersion:15`, model `native-thick-lens-tracing`, with **1–2 independently authored stationary finite biconvex spherical thick lenses**, **1–4 explicitly directed native SingleRay point sources**, **0–2 passive external detectors**, common explicit exterior index; no other optical components, no source inside lens, no nested or overlapping media, no 3D/wavelength/motion or image prediction. Every lens supplies `x,y,apertureHeight,centerThickness,frontRadius,backRadius,insideIndex,outsideIndex,partialReflection`. Front and back radii are positive magnitudes; native `DR1R2` uses r1 positive and r2 negative. Zero optical radius, invalid geometry or a missing material fact is not replaced by a default.

The validator uses spherical cap sag `a²/(R+sqrt(R²-a²))` for half-aperture a; positive radius at least `a+1 mm`, aperture at least 4 mm, centre thickness at least 2 mm, **rim >=1 mm**, full optic bounds ±10000 mm, separate entire x extents of two lenses by >=0.01 mm. Each source and detector endpoint must lie outside the lens complete x extent with a common separation side. Forward near-rim/circle-tangent initial rays are refused by conservative guards. These admission margins are **not ray-tracing precision guarantees**.

The compile adapter constructs the original upstream native `SphericalLens` from the explicit input, and read-only `onRayIncident` observations identify real `front-arc/back-arc/top-rim/bottom-rim` events, assign per-ID counts, first normal/index/direction/relative branch power, and delegate exactly once to native propagation. The original completeness/hash gates suppress incomplete, stopped, undefined or stale requested measurements; Fresnel-off warns of transmitted-only approximation, TIR remains. No new ray propagation, custom Snell/Fresnel solver, numerical cutoff or hidden route constraint.

## Author's synthetic software evidence — NOT an independent verdict

- Test fixture [native-thick-lens-train.json](https://github.com/physicsvigilante/opticsim/blob/610d748e91f25f6233fb057932cabe6a62ed2a1a/examples/native-thick-lens-train.json): S1 at (−200,10) mm, zero-degree rightward ray, L1 x=0 n=1.5, L2 x=150 n=1.3, both Rfront=Rback=100 mm, aperture=100 mm, central thickness=30 mm, shared outside n=1.
- Source native trace on a real Node24 CI job: exactly four actual lens callbacks `L1,L1,L2,L2` at x ≈ −14.49874, +14.59178, +135.03299 and +164.89432 mm; 1 actual detector crossing. Native L1 first 5.73917° incident and 3.82255° transmitted; L2 first 6.97054° incident, 5.35654° transmitted; independent sin(Snell) invariants asserted in test. All four events classify as distinct curved faces, not a prescribed itinerary.
- Native full-Fresnel two-body fixture logged **incomplete, truncation ≈0.016327373393958983**, all five requested measurements `suppressed`. Forced depth cap is also incomplete/suppressed.
- v15 test checks reversed object ordering, one-lens scene, genuine ray misses, explicit non-air common ambient, invalid radius/rim/overlap/vertex-source/detector/source-mode, historical schema isolation, revisions/exports/stale hash/readout limits. The test-only earlier [PR #109](https://github.com/physicsvigilante/opticsim/pull/109) was feasibility, not public admission. Baseline existing CI was corrected for one additional catalog profile and append-only app source hash provenance; historical frozen evidence files were not rewritten.
- [v15 scope document](https://github.com/physicsvigilante/opticsim/blob/610d748e91f25f6233fb057932cabe6a62ed2a1a/docs/NATIVE-SPHERICAL-THICK-LENSES.md) lists intentional omissions.
- **Node 24 software tests:** 812/812 passed on latest candidate. **Real Chrome v15 workflow is pending completion at the time this request is prepared**. Reviewer must inspect final exact-head CI metadata, logs and screenshots before rendering a verdict. Do not equate source CI with separate native reproduction.

## Independent adversarial study requested

1. Verify native `SphericalLens` DR1R2 parameter/sign convention, real curved-arc and rim path geometry, guaranteed valid biconvex body across allowed parameter bounds, and geometry bounds with separately calculated reference cases. Look specifically for finite-aperture corner collisions, large radius cancellation, near-minimum rim, two-lens separation and source/detector false admission.
2. Verify observer’s signed local normals at actual **front, back and rim** faces, including reverse illumination and total internal reflection if admissible; do not count a passing front-face Snell check as rim/numerical certification. Check ambiguous native incidents are withheld, not fabricated.
3. Independently compute one- and two-lens oblique Snell and polarisation-aware Fresnel relations, native truncation handling, exact observed face encounters and detector crossings. Review independent material indices and exterior normalization.
4. Check all old v1–v14 scenes, frozen R1/Stage2 measurement policies, native pin, and existing browser/editor source-mode coherence remain isolated. Confirm that adding v15 does not bypass v14 release gate or silently migrate old saves.
5. Inspect exact-head Node/Chrome CI, source provenance and any failures; if pinned-native execution is unavailable to reviewer, distinguish independent numerical calculations from source-CI observations clearly.

## Review disposition

A separate Chat B must publish a new report at `projects/opticsim/pr-110/reviews/review-01-chat-b.md` with exact HEAD and verdict **CLEARED FOR OWNER DECISION**, **INSUFFICIENT EVIDENCE**, or **CHANGES REQUESTED**; severity and reproducibility of findings, residual physical/numerical limitations, and whether additional native tests are necessary. AI-assisted independent-context review is **not** the same as a human expert's endorsement, and no reviewer can authorize merge independently of the project owner.

No original textbook interpretation fidelity, image reconstruction, detector ancestry, continuous power, student assessment or textbook answer completeness is claimed. Engineering objective is physically faithful, bounded native simulation of an explicitly authored apparatus.
