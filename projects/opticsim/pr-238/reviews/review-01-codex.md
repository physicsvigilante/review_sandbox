# Independent Codex review of Opticsim PR #238

**Outcome: pass. No unresolved blockers or demonstrated defects in the bounded public afocal-placement query.**

- [Source PR #238](https://github.com/physicsvigilante/opticsim/pull/238), production base `7d404f5e4ea442a58b88b6235aae65a89a6bb6fb`.
- Exact reviewed head `4aca16f75e989a13649590f3d63bf87082c5e941`, Git tree `21261932fcfcc6eb7ad37d439d5ef0814db77715`. [Exact source](https://github.com/physicsvigilante/opticsim/tree/4aca16f75e989a13649590f3d63bf87082c5e941)
- Reviewer: independent-in-context Codex agent, 2026-11-21. Scope: uniqueness/completeness of the two positive roots, signed height and infinity scope, dimensional and representation limits, native evidence and normal public dispatch. No production files changed by this review.

## Independent verification

For a positive lens of focal length f and facing concave mirror of radius magnitude R at pole distance d, I multiplied the full exact lens/drift/reflection round-trip matrix in travel coordinates. The return-slope coefficient for an axial collimated input is `−2(1−d/f)[1/f+(1−d/f)/R]`. Positive f and R give exactly two distinct positive roots. At d = f, the front focus lies at the mirror pole and the lens-plane return height is −h. At d = f+R, the focus lies at the mirror centre and the ray retraces to +h. Both give the paraxial image at infinity for the authored parallel input. A finite object's conjugate remains outside this query.

An independent rational matrix sweep checked 15,017 admitted geometries and both roots in each, including mm, cm, m, endpoints and rounding ties. It also checked 24 immediate input-boundary or excluded-sign cases. All 30,034 physically exact roots and signed height scales agreed. The two public spacings remained distinct, with the upper allowed centre-retrace gap of 20,000 mm. Exact midpoint comparisons confirmed nearest-even rounding for the serialized distances. The worst residual slope coefficient when propagating the reported rounded gaps was `1.11e-12` per mm of input height.

The unequal geometry was frozen before implementation at `7530122cd213fa6bff6e354165c5e973f1b9f4b4` and its JSON is unchanged. For f = 400 mm and R = 600 mm I independently verified the 400 and 1000 mm roots, with −1 and +1 height scales, and the 700 mm non-afocal control with height scale `−3/4` and travel slope coefficient `+3/1600` per mm. In a separate reviewer-only native replay, twelve genuine SingleRays exercised all three unequal spacings through the same pinned IdealLens, ArcMirror and Detector. The largest afocal return-slope magnitude was `2.19e-15`. The non-afocal control was within `2.82e-7` in slope of its first-order prediction. The unequal native checks supplement the PR's frozen analytical cases.

The normal CLI returned the original 1 and 2 m roots, both unequal roots and the 10,000/20,000 mm boundary pair, with zero native calls and no qualified scene. It withheld the finite-object substitution and a separately requested native detector result. The published example input and independent report SHA-256 values are `520e00bd8d8cdad06697b5c79acfb921baea0fd6cd2d8bedfa97fc609ef7ed14` and `4ace6b7937f46a8c476e743f511801ef6979fb7c422de0082749a8ef8b738349`.

The rebuilt headless core used PhyDemo pin `811f508d2b070898c241a568b0c167dcb8645251`; all 14 focused tests passed. The inherited exact #237 native cases cover two root placements and a non-afocal control with finite apertures. The public result makes a conditional paraxial claim and does not certify aperture coverage or a native image. [Independent #237 review](https://github.com/physicsvigilante/review_sandbox/blob/6190ad9fecb3bd6dd56f73b7bf582d3824dc3c16/projects/opticsim/pr-237/reviews/review-01-codex.md)

## Hosted CI and retained evidence

All 11 hosted exact-head PR workflows passed. The optical workflow logs identify synthetic checkout `0de28fa1be8235419bd3cd903f7ec5deb2b14b34`, its stated head and base, both relevant afocal query tests and 1,370 passed Node tests with zero failures or skips. The existing real Chrome acceptance suites passed. Independent Git merge-tree computation reproduced the exact reviewed tree. [Optical composition CI](https://github.com/physicsvigilante/opticsim/actions/runs/44887953175) · [Unified workflow CI](https://github.com/physicsvigilante/opticsim/actions/runs/44887953176)

I verified authoring archive `14700627801` against SHA-256 `8788ed37170993e7960c3a3ae8d431b2f8a01e3af8f3e87d9d5d42beb6aaffad`. Its three retained native afocal study files, with twelve genuine traces, matched independent current-head and previously verified #237 replays byte for byte. The new public CLI evidence and separate unequal native checks are documented above. [Archived evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44887953175/artifacts/14700627801)

Other passing workflow run IDs are `44887953171`, `44887953184`, `44887953189`, `44887953197`, `44887953229`, `44887953247`, `44887953262`, `44887953290` and `44887953291`. This clears the exact reviewed source for owner-authorized integration.
