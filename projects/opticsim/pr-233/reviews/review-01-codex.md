# Independent Codex review of Opticsim PR #233

**Outcome: pass. No unresolved blockers or demonstrated defects in the frozen immersion study.**

- [Source PR #233](https://github.com/physicsvigilante/opticsim/pull/233), production base `fb5ae8d5778212928bc11e73faefc87cbbb54148`.
- Exact reviewed head `bd1b7729a3ce4d80ee7ed10452209126f34560be`, Git tree `e294a92d42c37d24f0a208e1896af006cfe1cdd0`. [Exact source](https://github.com/physicsvigilante/opticsim/tree/bd1b7729a3ce4d80ee7ed10452209126f34560be)
- Reviewer: independent-in-context Codex agent, 2026-11-21. Scope: Problems-only calibration, explicit finite geometry, signed return-to-axis intercepts, pinned native callbacks and exact evidence. The PR changes only the freeze, study notes and tests. No production files changed in this review.

## Source and analytical scope

I read Lens Formula Problem 005 only. Its crop SHA-256 matched `4255a77f32ebf523e18e8960adb818ad685d8db547ce3322b97615cb1a24e70e`. The source archive matched SHA-256 `03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939` and the archive Git blob at `d33b45226348d9b0c701f2a3e8b86dd1285de2d0`. No Solutions material was opened. The immutable freeze at `2e8af829a1b92af564d91ca3258adb5654aa286c` precedes implementation and its JSON bytes equal the reviewed head.

The source gives a biconvex glass lens of index 1.6, focal length 10 cm in air, and two new homogeneous exterior indices, 1.5 and 1.7. The study declares the thin paraxial and unit-air approximations. In reduced slope, the reference calibrates a curvature factor of `1/60 mm⁻¹`. Holding that factor fixed gives image-side thin focal lengths of +900 mm and −1020 mm. The individual radii and thickness are unspecified by the source. Exact material matching has zero power by the analytical model. The frozen native data cover the three declared media, away from matching.

## Finite case and native evidence

The separately chosen +120/−120 mm radii share the calibrated thin curvature factor. The explicit 5 mm thickness and 20 mm aperture define a distinct finite native experiment. I rebuilt the core from PhyDemo pin `811f508d2b070898c241a568b0c167dcb8645251`; all 13 focused native and preservation tests passed. The six separately emitted SingleRays used one genuine SphericalLens and one real downstream Detector each. Independent wrappers confirmed the native relative index `n_lens/n_medium` and all 18 actual front-arc, rear-arc and detector events.

| Exterior index | Exact finite paraxial rear-pole intercept (mm) | Native rear-pole intercept (mm) |
|---:|---:|---:|
| 1 | 12600/127 | 99.20915398467608 |
| 1.5 | 689400/767 | 898.8175705085146 |
| 1.7 | −785400/769 | −1021.3183850032362 |

A separate analytical sphere/Snell reconstruction matched the actual callback positions within `3.20e-14 mm` and unit-direction components within `2.23e-16`. Minimum rim clearance exceeded 9.49 mm. Mirrored launch partners produced the same intercept in each medium. The maximum difference between sampled and finite paraxial intercepts was `0.0090267 mm`, inside the predeclared 0.5 mm tolerance. Both media below the lens index gave forward extrapolation from the measured detector line. In index 1.7 the rays still crossed the actual downstream detector moving rightward, and the virtual intercept came from extending those measured lines backward. These tests establish sampled traces and line estimates with Fresnel branching disabled.

## Hosted CI and retained evidence

All 11 hosted exact-head PR workflows passed. The optical workflow logs identify synthetic checkout `beb792cfe58c9312660bd3b9e4d4824cfba907fd`, its source head and base, all three new tests, and 1,351 passed Node tests with zero failures or skips. The incumbent real Chrome acceptance suites passed. Independent Git merge-tree computation reproduced the reviewed tree. [Optical composition CI](https://github.com/physicsvigilante/opticsim/actions/runs/44885514192) · [Unified workflow CI](https://github.com/physicsvigilante/opticsim/actions/runs/44885514264)

I verified the downloaded authoring archive `14699758011` against SHA-256 `44648f924f04d5492f083bb465ec40995822d691436f1f21aaefb58a20c83b68`. All three JSON files, with six per-ray native records, matched the isolated exact-head native replay byte for byte. SHA-256 values are `e8d89be51ab2e784dc30f4a241fb6a9b454fffcc0a2a14f47644e06932607d68` for index 1, `f562b08216847c4a39f61f7131be0ebd6cea62f522daf75dea0377eb909eea76` for index 1.5 and `f45089633eb961fad7eb161d7f6f11272a452cd2e687c935c3702c8647e5591e` for index 1.7. [Archived evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44885514192/artifacts/14699758011)

Other passing workflow run IDs are `44885514181`, `44885514186`, `44885514188`, `44885514193`, `44885514221`, `44885514228`, `44885514258`, `44885514287` and `44885514344`. This clears the exact test-only source for owner-authorized integration.
