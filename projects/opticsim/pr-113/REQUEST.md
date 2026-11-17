# Opticsim PR #113 — R2 independent physics review request (v16)

**Status: REQUEST PREPARED; NO INDEPENDENT R2 VERDICT. DO NOT MERGE SOURCE.**

## Source and dependency

- Candidate: [draft source PR #113](https://github.com/physicsvigilante/opticsim/pull/113), development branch `feature/native-thick-lens-mirror-v16`. Current candidate SHA at request creation `b0d5eef12a465dd9f4c935a5ae477b356ba86f0f` (**may change during CI fixes**); reviewer must fetch actual final head SHA and refuse stale source. The PR targets main temporarily to trigger CI, then must return to v15 dependency base.
- Parent reviewed v15 [PR #110](https://github.com/physicsvigilante/opticsim/pull/110) at `80fec0bb05200ad6034bf55a00c6e522740b27e1`, with [Chat B clearance](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-110/reviews/review-02-chat-b.md). Its v14 prerequisite [PR #107](https://github.com/physicsvigilante/opticsim/pull/107) is also R2-cleared. **Neither prerequisite has owner merge authorization and neither is released on main.** The new v16 physical scope requires a separate independent R2 review and owner decision.
- Pinned native PhyDemo SHA `811f508d2b070898c241a568b0c167dcb8645251`; no native vendor or custom ray solver change.

## Claimed physical contract

An isolated schema v16 model `native-thick-lens-mirror-tracing`: exactly **one** stationary nonrotated finite biconvex `spherical-lens`, exactly **one** independently specified finite `plane-mirror`, **1–4 explicitly directed single rays** and **0–2 passive finite detectors**. No second lens, blocker, prism, nested/overlapping medium, implicit source beam, material dispersion, 3D imaging, complete irradiance or inferred optical image.

New geometry code `src/thick-lens-mirror-composition.js` uses the **unchanged v15 validation function** on a temporary validation view excluding the mirror, then certifies the entire mirror segment is strictly left or right of the full thick-lens x extent with >=0.01 mm clearance. Existing general-optical and detector validation checks bound mirror/source/detector conflicts. These are conservative *admission* constraints, not universal tracing precision guarantees; valid off-axis arrangements may refuse. The original canonical/natively compiled scene retains the mirror and every other authored component.

The existing `src/adapter.js` independently emits pinned native `SphericalLens`, `Mirror` and `Detector` objects. PhyDemo performs all surface intersections and reflection/refraction; Opticsim DOES NOT impose a lens→mirror→lens route, complete return or image. Existing interface, mirror, source and detector observations report sampled native callbacks with per-ID semantics, and incomplete/truncated/stale results remain suppressed. Fresnel-off is an explicit approximation while TIR remains native.

## Synthetic evidence being checked

The explicit [v16 synthetic source](https://github.com/physicsvigilante/opticsim/blob/b0d5eef12a465dd9f4c935a5ae477b356ba86f0f/examples/native-thick-lens-mirror-v16.json) has S1 at (−200,10) directed 0°, one 100 mm aperture / 30 mm center-thickness thick lens with Rfront=Rback=100 mm and n=1.5 at x=0, one 200 mm-long native mirror at (130,0), orientation +90°, and a finite detector at x=−100. Native research-only [PR #112](https://github.com/physicsvigilante/opticsim/pull/112) independently established the feasibility of a true native `D1,L1,L1,M1,L1,L1,D1` callback sequence and a genuine missed mirror. That research PR did **not** admit a public scene.

The v16 production candidate adds canonical authoring, validation, source controls, browser physical edits, revision/qualified export, and Node regressions. Tests check actual front/back curved-face Snell across forward/return rays, mirror specular law, native missed mirror, reverse illumination, mirror tilt, a non-air ambient medium, near-clearance interactions, invalid nearby geometry, old schema isolation, and incomplete-result suppression. **A published native CI log or Chrome screenshot is source evidence, not independent physical correctness proof.** The reviewer must verify exact head, all workflow conclusions and independent physical reference calculations.

## Adversarial review priorities

1. Whole-system admission and model-selection correctness: do v16 sources/lens/mirror/detectors remain strictly separated and no old v15 save or v4 mixed-optical path get upgraded silently? Audit the validation-only subset, full finite-segment clearance for rotated mirrors, source/detector conflicts and 0.009/0.011 mm neighbors. Check actual input units and numerical limits rather than trusting a positive fixture.
2. Actual native mixed-object outcomes: independent Snell/curved-face intersections for return at all four native SphericalLens arcs, mirror front/back and oblique reflection, reverse source direction, multiple sources/misses, truncation, TIR and ray-depth cases. Explicitly distinguish zero measured native reflection from missing qualification. Verify no imposed route or manufactured mirror hit; repeated lens hits are not a guaranteed image.
3. Browser/UI/saved exports: confirm real Chrome edits of mirror and lens cause a fresh native run, invalid mirror overlap withholds old results, qualified reopen keeps physical IDs/material index, source picker stays exact single-ray, and old v15/v14 viewer semantics/hashes remain preserved.
4. Numerical limitations: near-grazing curves, reflective returns near a rim, near-coincident intersections, weak Fresnel branches, 0.01-mm geometry admission guard vs actual floating-point reliability. Do not silently relax the original pin or threshold. If no independent native runtime is available, use separate geometry/Snell/Fresnel calculations and clearly label CI values as source-observed only.
5. Correct source provenance: compare against v15 reviewed HEAD `80fec0bb...`, check frozen historical tests and app SHA-chain, and verify no source-correctness claims beyond sampled/qualified scenes. Original textbook interpretation, educational effectiveness and final-answer completeness are NOT goals of this review.

## Independent verdict

When the source candidate is final and all CI evidence is available, **a separate Chat B** must write a new report at `physicsvigilante/review_sandbox/projects/opticsim/pr-113/reviews/review-01-chat-b.md`, with the exact reviewed SHA and an explicit **CLEARED FOR OWNER DECISION**, **INSUFFICIENT EVIDENCE**, or **CHANGES REQUESTED** verdict, severity/reproducibility and limits. This independent AI-assisted technical review is not authorization to merge and is not a human optics expert certification.

**HOLD source PR #113** until that independent review plus explicit owner approval after its v14 and v15 prerequisites.
