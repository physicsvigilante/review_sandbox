# Independent Codex review of Opticsim PR #235

**Outcome: pass. No unresolved blockers or demonstrated defects within the frozen study.**

- [Source PR #235](https://github.com/physicsvigilante/opticsim/pull/235), production base `6a7f4f8d6190eecb1fe751343e5f8c26f34d21bf`.
- Exact reviewed head `5650c835eaad77237a10839ae2f0403c276cefca`, Git tree `1899c0319a2156d97abda2506fd12685162c67d2`. [Exact source](https://github.com/physicsvigilante/opticsim/tree/5650c835eaad77237a10839ae2f0403c276cefca)
- Reviewer: independent-in-context Codex agent, 2026-11-21. Scope: Problems-only source, static signed paraxial inverse, preservation of fixed geometry, actual native interaction order and signed detector-line intercepts. The PR changes only the freeze, study notes and tests. No production source changed during the review.

## Source and signed model

I read Lens Formula Problem 009 only. Its crop SHA-256 matched `9df31b9f5af847853cc031ee898b42676925b76ad630ef954102d0e1b869f998` and the source ZIP matched `03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939`. No Solutions material was opened. The freeze at `0f21351c8fb9a1920daf66c04b2cafdc689636b6` preceded the test implementation and its JSON bytes match the reviewed head.

The original provides a 450 mm distance from the tank-bottom point to the lens, a dry image 360 mm above the lens, a 400 mm fill, and a filled image 480 mm above the same lens. The fixed ideal lens remains in the air gap. The paraxial model assumes propagation along the upward normal, represented by +x, one flat liquid–air boundary, a homogeneous liquid and unit-index air. Filling changes the optical propagation interval. Source, lens, focal length and detector stay fixed within each dry/filled pair, with no mechanical or pressure coupling.

Independently solving the thin-lens equations gives a focal length of 200 mm, a filled apparent object distance of `2400/7 mm` and an apparent depth of `2050/7 mm` after removing the 50 mm air gap. Thus the model infers index `56/41`. This static inverse uses the two given image distances. The native source-controlled run takes the inferred index as an authored input. The separate synthetic case keeps its 300 mm object distance and 250 mm focal length, with the 200 mm section changed to index 2. Its apparent object distance becomes 200 mm and the predicted wet conjugate lies at −1000 mm from the lens.

## Pinned native evidence

I rebuilt the exact source with PhyDemo pin `811f508d2b070898c241a568b0c167dcb8645251`. All twelve focused tests passed. The independent native study replay uses eight genuine SingleRay launches, with two opposite small slopes per dry/filled case. The dry order is IdealLens → Detector and the filled order is PlaneGlass → IdealLens → Detector. Both retain positive x propagation. A separate Snell and ideal-lens calculation matched all 20 callback coordinates within `1.18e−14 mm` and directional components within `1.12e−16`. Minimum lens or detector rim clearance was greater than 9.06 mm.

| Control | Signed dry/wet prediction (mm) | Signed dry/wet measured-line intercept (mm) |
|---|---:|---:|
| Source geometry with inferred index | +360 / +480 | +360.000000 / +480.000994 |
| Synthetic real-to-virtual | +1500 / −1000 | +1500.000000 / −999.985000 |

The mirrored slopes produced identical intercepts in each pair. The largest axial residual was `0.0149999 mm`, inside the frozen 0.12 mm tolerance. Each ray crossed the actual downstream detector once. The negative intercept uses backward extrapolation of the measured diverging rays. The study measures sampled ray evidence, retains the existing public authoring boundary and introduces no native index inference or image-detection claim.

## Hosted CI and retained evidence

All 11 hosted exact-head PR workflows passed. The optical job logs identify synthetic checkout `bf6c056c718d1bbb3c1932625b533db98eefce03`, its stated source head and base, all four new study tests, and 1,361 passed Node tests with zero failures or skips. Independent Git merge-tree computation reproduced the reviewed tree. Existing real Chrome acceptance passed. [Optical composition CI](https://github.com/physicsvigilante/opticsim/actions/runs/44886551422) · [Unified workflow CI](https://github.com/physicsvigilante/opticsim/actions/runs/44886551349)

I downloaded exact-head authoring archive `14699653373` and verified SHA-256 `cbd418cfa0460141de184282ed6f67519c741563bea287e8bdb5eddfb5f9bfa7`. All four dry/filled JSON files, with all eight raw native runs, matched the independently rebuilt exact-head files byte for byte. [Archived evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44886551422/artifacts/14699653373)

Other passing workflow run IDs are `44886551362`, `44886551370`, `44886551374`, `44886551404`, `44886551426`, `44886551428`, `44886551434`, `44886551444` and `44886551530`. This clears the exact test-only source for owner-authorized integration.
