# Independent Codex review of Opticsim PR #236

**Outcome: pass. No unresolved blockers or demonstrated defects within the public paraxial scope.**

- [Source PR #236](https://github.com/physicsvigilante/opticsim/pull/236), integrated production base `6c235a4a07a0a666438bf14f8690fc6d6c7cb570`.
- Exact reviewed head `276def217e65834526f3318fe643685002f19bac`, Git tree `e42192a6ee682d71b1d7455bde44e0b6405284dc`. [Exact source](https://github.com/physicsvigilante/opticsim/tree/276def217e65834526f3318fe643685002f19bac)
- Reviewer: independent-in-context Codex agent, 2026-11-21. Scope: calibrated conjugates, signed forward and inverse domains, exact numerical policy, normal CLI behavior and retained native controls. No production source changed during this review.

## Independent optical and numerical verification

I derived the dry calibration from an axial ray whose height at the lens equals its slope times H. The dry image condition fixes the lens power as `P = 1/H + 1/vDry`. In the filled case the same incident exterior reduced slope accumulates an effective height for `u = H−d+de/n`. The signed emergent intercept satisfies `v = −u/(1−Pu)`. Inverting that equation gives `u = v/(Pv−1)` and hence `n = de/(u−H+d)`; it requires a finite apparent object farther from the lens than the exterior gap and an index in [1,4]. The native detector crossings supply separate corroboration of the forward controls. They supply no native measurement of the liquid index.

An independent rational replay checked 16,887 forward and inverse requests across mm, cm and m, both signs of the dry and filled conjugates, diverging and converging calibration, identified and excluded indices, and exact zero or near cancellation. Forward results included 4,273 real, 4,156 virtual and three exactly collimated cases. The inverse qualified 4,365 requests and withheld impossible or unresolved requests with the expected distinct statuses. The independent calculations agreed on all outcomes and returned values.

Independently constructed adjacent signed image observations at both exact index limits `n = 1` and `n = 4`. The endpoint and interior candidates qualified and the exterior candidates remained unavailable. A separate set of 18 cases covered exact and adjacent represented inputs on both sides of the ±10⁹ mm forward distance ceiling in all three units. Equality and the in-range neighbor qualified. The out-of-range neighbor withheld. An exact zero-power calibration remained outside scope, and exact forward collimation retained its explicit infinity state.

The ordinary CLI independently reproduced the Problem 009 index `56/41`, the synthetic signed `−1000 mm` virtual result, exact infinity, an inverse observation just beyond the physical index range, and partial coverage with an explicit native request. Each case retained original input bytes and recorded zero native calls or qualified scenes. The published example input and independent report SHA-256 values are `8d5ea22bc6b8c9c6582ec258a8ffe3fc88ec3e2fe94866145f3ae25cdfcc8589` and `b4689e8f7e58cf0f2f47a6bb5e091535c2a00917acdcdfa4e0c520572d0efeb8`.

## Inherited native evidence

I rebuilt the pinned PhyDemo core at `811f508d2b070898c241a568b0c167dcb8645251` and all 21 focused tests passed. The untouched #235 protocol still uses eight genuine native launches with fixed source/lens/detector geometry. Filled rays cross the liquid-to-exterior PlaneGlass, then the same IdealLens and the detector. The signed virtual intercept still comes from backward extrapolation of a real downstream crossing. The #235 source archive, Problems-only interpretation and frozen protocol remain unchanged. [Independent #235 review](https://github.com/physicsvigilante/review_sandbox/blob/ef8146624787625e14870d0f39e9d9e0c415a99d/projects/opticsim/pr-235/reviews/review-01-codex.md)

## Hosted CI and retained evidence

All 11 hosted exact-head PR workflows passed. The optical workflow logs identify synthetic checkout `9134f1b77d27584fb3cfa673c207d056181552dd`, its stated head and base, and 1,364 passed Node tests with zero failures or skips. This includes the new reduced-model cases and four frozen native scenarios. Existing real Chrome acceptance passed. Independent Git merge-tree computation reproduced the exact reviewed tree. [Optical composition CI](https://github.com/physicsvigilante/opticsim/actions/runs/44886950108) · [Unified workflow CI](https://github.com/physicsvigilante/opticsim/actions/runs/44886950048)

I downloaded exact-head authoring archive `14700139405` and verified SHA-256 `69f6cacfe472fc299b772eabe4096a5925852202e7e236daee2ba4705a5ee695`. Its four retained native dry/filled JSON outputs matched the independent exact-head replay and previously verified #235 replay byte for byte. The public CLI outputs were independently captured and verified above. [Archived evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44886950108/artifacts/14700139405)

The remaining passing workflow IDs are `44886950011`, `44886950017`, `44886950035`, `44886950060`, `44886950068`, `44886950076`, `44886950078`, `44886950134` and `44886950144`. This clears the exact reviewed source for owner-authorized integration.
