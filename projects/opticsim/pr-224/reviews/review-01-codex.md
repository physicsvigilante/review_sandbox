# Opticsim PR #224 independent review R1

**BLOCKED at exact candidate `f713d79422e3957128387f7deeb25c9c194f665e`.** One omitted early opaque hit can qualify, and the inherited browser provenance test still binds the active app to v34.

| Identity | SHA |
|---|---|
| Candidate tree | `612e0ca89018802f5e695149a41fd01220d11343` |
| Production base | `85c0534a4e5199bf989ae81a857b1d4077c2dbb6` |
| GitHub PR test merge | `4279e06eb3df4763caa51db52a2c950df9b9463f` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

The hosted test merge has both expected parents and the exact review tree.

## B1 — omitted early native target collision can still certify the four-wall route

Use a 100 by 100 mm box with 0.2 mm gaps, a source at (30,70) heading 45°, and a native vertical opaque 10 mm target at (40,80). Genuine PhyDemo immediately absorbs this ray at B, and the scoped four-wall result correctly fails.

I wrapped the genuine Blocker intersection call, delegated once, and suppressed its positive report only for the initial segment origin. The unchanged native Mirror and Blocker callbacks then reported top, right, bottom, left and a final absorption. The previous event sequence auditor returned `v35MirrorBoxVerified:true` despite the initial continuous segment physically crossing the opaque target en route to the first wall. This is a deliberately omitted native contact, rather than a defect in the pinned unmodified run.

A read-only guard can check each actual finite incoming wall segment against the already authored opaque segment. It need not choose intersections, steer rays or prescribe a wall order.

## B2 — active browser provenance omits v35

The append-only historical app provenance test at `test/native-thick-lens-aperture-v18.test.mjs` still expects active app blob `94e5c54e8c9076856b75ac2cce7a574d9e24b3b1` from the v34 record. The new public app blob is `8e2d783783a5b953f58ac2264a1e0e6f7df11ce0`. I independently ran the affected test and reproduced the mismatch. Add a v35 provenance fixture and retain the previous v34 binding.

## Positive scoped controls

Independent real Chrome passed the seven v35 checks. A separate 144-scene native test matrix varied the aspect ratio, coordinate translation, target orientation, traversal direction and component ordering. Its 96 genuinely qualified traces all had one actual wall hit per ID and real absorption, and the other 48 withheld results. These controls leave B1 and B2 open. A corrected source needs exact-head evidence before integration.
