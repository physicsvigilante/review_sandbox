# Independent Codex review of Opticsim PR #239

**Outcome: pass. No unresolved blockers or demonstrated defects within the frozen relay study.**

- [Source PR #239](https://github.com/physicsvigilante/opticsim/pull/239), production base `0304b1a984c9dab4850fd759c4b851ae804f4a92`.
- Exact reviewed head `0c68a7f292dc2e7f378c898f90b4360ec8aa2250`, Git tree `bae3ae4ee84fa4da4a7c80fcab50b2bd82bd77ab`. [Exact source](https://github.com/physicsvigilante/opticsim/tree/0c68a7f292dc2e7f378c898f90b4360ec8aa2250)
- Reviewer: independent-in-context Codex agent, 2026-11-21. Scope: Problems-only interpretation, exact scaled paraxial matrix, centre-lens replacement, signed native detector-line reconstruction and retained evidence. The PR changes the study, its test and a native test helper. No production source changed during this review.

## Source and paraxial proof

I read Lens Formula Problem 016 only. Its crop SHA-256 matches `5acc53f26dc50f64905646d868dbacce351ad65e970f9d8109d989e18e3abfa9`, and the source ZIP matches `03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939`. No Solutions material was opened. Freeze `babf0661007f5ac98f3e9da7bdaa8d46d62618c7` precedes the implementation and its JSON blob is byte-identical at the reviewed head.

The source gives consecutive ideal converging focal lengths 4a, a and 4a, and gaps 4a. I independently multiplied the full matrices in `(y/a, dy/dx)` from the first to the last lens plane. The rows are (−1, −8) and (0, −1). For an incident-side paraxial object pencil that passes through all three lenses, extrapolation from the last lens plane gives the original axial object coordinate and height `−y_object`. Replacing only the middle focal length by 2a gives `−I`. It retains signed magnification −1 and moves the extrapolated image downstream by 8a. In both frozen controls the images remain upstream of the last lens.

## Pinned native evidence

I rebuilt the exact archive with PhyDemo pin `811f508d2b070898c241a568b0c167dcb8645251`. Both new tests and four adjacent native/analytical tests passed. The eight observed two-ray fits came from sixteen separate native SingleRay launches, each through the three specific IdealLens instances and then the real downstream Detector. Independent ideal-lens and drift propagation matched all 64 callback positions to `1.56e-15 mm` and all unit-direction components to `1.12e-16`. Minimum finite aperture clearance was 8.3 mm.

With a = 25 mm and object positions −50/−125 mm, the source fit returned −50/−125 mm. The changed-centre fit returned +150/+75 mm, still before the last lens at 200 mm. Both tests returned the opposite of the two launched object heights ±0.3 mm. The largest measured-line fit errors against the rational predictions were `2.28e-13 mm` axial and `1.50e-15 mm` transverse. Both outgoing lines were physically measured at x = 225 mm while travelling rightward. Their intersections were found by backward extrapolation. The native evidence concerns these sampled rays, separately from the paraxial identity for arbitrary scale and incident pencils.

## Hosted CI and retained evidence

All 11 hosted exact-head PR workflows passed. The optical job logs identify synthetic checkout `626ce68539629c4ee5088f7aa7eff45672a556dd`, its stated head and base, both new study cases, and 1,372 passed Node tests with zero failures or skips. Existing real Chrome tests passed. Independent Git merge-tree computation reproduced the reviewed tree. [Optical composition CI](https://github.com/physicsvigilante/opticsim/actions/runs/44888449268) · [Unified workflow CI](https://github.com/physicsvigilante/opticsim/actions/runs/44888449272)

I verified downloaded authoring archive `14701371404` against SHA-256 `cdd3a327a8e911fd026d4a07c8bdb0525d07bcada8df3f28adf7c95c63346847`. Both archived study JSON files, containing all sixteen raw native records, matched the independently rebuilt exact-head replay byte for byte. Their SHA-256 values are `61682d69cd53b01d645b18aa1ef6a3b3123f8069a9f04a322242c59df2adeb6f` for the source relay and `ed087bcd79c004c9cdb644df3c89aff3cb22957a536c15fedcf3c5cd6baf0d71` for the changed centre lens. [Archived evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44888449268/artifacts/14701371404)

Other passing workflow run IDs are `44888449240`, `44888449280`, `44888449282`, `44888449295`, `44888449302`, `44888449338`, `44888449339`, `44888449355` and `44888449366`. This clears the exact test-only source for owner-authorized integration.
