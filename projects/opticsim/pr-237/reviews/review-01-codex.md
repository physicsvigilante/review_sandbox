# Independent Codex review of Opticsim PR #237

**Outcome: pass. No unresolved blockers or demonstrated defects within the frozen afocal study.**

- [Source PR #237](https://github.com/physicsvigilante/opticsim/pull/237), production base `44fe2226f8bde54217e4ec1a48f495f9d30fb9ca`.
- Exact reviewed head `eac5b1d014fd0cbade4e164add80a6f77b1756c9`, Git tree `c31c69bcfa19e497d7ff680acb39f1215990c6f8`. [Exact source](https://github.com/physicsvigilante/opticsim/tree/eac5b1d014fd0cbade4e164add80a6f77b1756c9)
- Reviewer: independent-in-context Codex agent, 2026-11-21. Scope: Problems-only interpretation, exact first-order positions and return signs, finite optical callback evidence and the intermediate control. No production source changed in the review. The PR only changes the freeze, study notes and tests.

## Source and signed afocal solution

I read Lens Formula Problem 012 only. Its crop SHA-256 matches `3e8a50b439fff120f7a69e0d356883aa38e91eb6423bace9091761ae20d6c9dc` and the source ZIP matches `03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939`. No Solutions material was opened. Freeze `f94e628206fb7ed75cf92b7a85b0e7fb81819ecb` precedes implementation and its JSON matches the reviewed bytes.

The source gives a biconvex lens of focal length 1 m, a concave spherical mirror of radius 1 m and incident axial parallel rays. In the declared coaxial paraxial model the mirror pole is a distance d beyond the lens. With fixed transverse height h and return travel measured toward decreasing x, I derive final slope `−2h(1−d/f)(1/f+(1−d/f)/R)`. The two roots for nonzero h are `d=f` and `d=f+R`, or 1 m and 2 m. Both give an image at infinity for the specified axial parallel input. An image of an independently placed finite object would require its position.

At the 1 m spacing the mirror pole coincides with the first focus, and the return reaches the lens at the opposite transverse height. At 2 m the mirror centre coincides with the first focus, and the ray retraces to the original height. Independent exact calculation gives the 1.5 m control a return-height factor of `−1/2` and a return travel slope of `h/2000` for h in mm.

## Native evidence

I rebuilt the headless core from PhyDemo pin `811f508d2b070898c241a568b0c167dcb8645251` and all ten focused tests passed. The twelve horizontal SingleRay runs used the same authored IdealLens twice, with one genuine ArcMirror callback at the selected finite patch. Each ray crossed the finite detector both before and after reflection, with opposite longitudinal signs. I independently solved the spherical intersection and vector reflection and applied the ideal lens to the incident and return slopes. The resulting 60 observed points and signed callback slopes agreed within `8.03e−12 mm` and `4.02e−15` respectively. Minimum finite segment or arc-end clearance exceeded 10.99 mm.

For input height +4 mm the observed return heights at the lens were −4 mm and +4 mm, with slope magnitudes at most `4.01e−15` across the eight afocal runs. At 1.5 m, +4 mm returned at `−1.99998000025 mm` with slope `+0.00199998800`. The control slope had the sign of the input height at every sampled height. Maximum first-order residuals were `2.00e−5 mm` in return height and `1.20e−8` in slope, inside the predeclared tolerances. The evidence concerns the selected finite rays and geometry. The PR adds no public authoring scope and no native image detection.

## Hosted CI and retained evidence

All 11 hosted exact-head PR workflows passed. The optical workflow checked synthetic merge `3ce05dbbfa60746fb857992b5c4d0046be0136d1` from the stated base and head, including the three new study tests. It passed 1,367 Node tests with zero failures or skips. The existing real Chrome suites passed. Independent Git merge-tree computation reproduced the reviewed tree. [Optical composition CI](https://github.com/physicsvigilante/opticsim/actions/runs/44887442294) · [Unified workflow CI](https://github.com/physicsvigilante/opticsim/actions/runs/44887442411)

I downloaded exact-head authoring archive `14700269620` and verified SHA-256 `bc66f06221936016696827083ae2687c55bc9e27ce5cb9c7c92afe7ed07d117d`. All three JSON files, with twelve actual native traces, matched the independent replay byte for byte. The SHA-256 values are `f8d7926ce6c39e2404de146998d3fec36ea1e25be8baa531b1ba56a9c51350aa` for the pole-focus case, `375ebe5a7c5403423c5154d190932e724f3007ff4bcb4d31fc7ead273986f8fe` for the centre-retrace case, and `df863b253effea078b3d4110439343819ca066ddcae065797f7ecfb627c8afa0` for the intermediate case. [Archived evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44887442294/artifacts/14700269620)

Other passing workflow run IDs are `44887442291`, `44887442297`, `44887442300`, `44887442318`, `44887442321`, `44887442329`, `44887442399`, `44887442401` and `44887442433`. This clears the exact test-only source for owner-authorized integration.
