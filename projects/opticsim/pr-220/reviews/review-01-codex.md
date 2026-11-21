# Opticsim PR #220 independent exact-head review

**CLEARED for owner-authorized integration at the exact candidate below.** No release blocker found.

| Identity | SHA |
|---|---|
| Candidate | `58b537b7ce69dad5683396057fdbe663ba503272` |
| Candidate tree | `3756a9384f703673ca980152e9af7b5b2c545f8b` |
| Production base | `a7e26c5340d5ec0206a4a911dd40055e35be38b7` |
| GitHub PR test merge | `d8f002014906362bb63f7aacff8961c2e20b0945` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

GitHub's test merge has the reviewed candidate and base as parents and exactly the candidate tree.

## Source, relations and numerical branches

I viewed the original A07 Problems image. SHA-256 `3d32be9585d21f90c31e7ec3b70a314fba34c7c2b487ee0370127a1f0211fc88` matches the frozen record. Solutions stayed unopened. The source specifies a 10 cm focal length and a fourfold image size, which supplies a magnitude. Under the explicit real incident-side object and paraxial assumptions, the CLI correctly retains two answers. The upright virtual branch has u=7.5 cm and v=−30 cm. The inverted real branch has u=12.5 cm and v=50 cm. The source supplies neither orientation nor object height.

The inverse places each signed candidate using u=f(1−1/m) and v=f(1−m), then checks its magnification through the existing point query. For concave focal lengths a negative magnification gives a real inverted image, while an upright real-object branch requires m>1. For convex focal lengths only 0<m<1 yields a real positive object distance. The m=1 pole case and a required virtual object retain distinct refusal reasons. Numerical range failures stay branch-specific.

Independent exact-rational references covered 1,512 requests and 2,016 branches over three units, both focal signs, signed and magnitude targets, exact unity and adjacent values, both target limits, and small-distance and large-position guards. There were 678 qualified branches, 1,032 physically unavailable branches, and 306 numerically withheld branches. Thirty magnitude requests retained a valid branch with `partially-indeterminate` status. That status did not count the request as fully available, including with an additional native request lacking apparatus. The maximum residual versus exact-reference distance was 1.14e−10 mm for object distance and 3.64e−12 mm for image distance.

## Native verification and preservation

Twenty-five focused tests passed independently. The four genuine v6 controls traced separate 75 mm and 125 mm source placements at heights zero and 0.1 mm. Every trial had three emitted roots and six detector callbacks, with a real ArcMirror reflection between each root's outgoing and returning crossings. Returning-line estimates preserved the virtual and real spatial signs and upright/inverted height signs. Maximum coordinate residuals were 0.053793 mm axial and 0.000073 mm transverse. The lines test local finite-sample directions against the conditional conjugates. There is no native image detection or observer-visibility claim.

The helper extraction preserved all four A09 measured point records and four A09 qualitative records byte for byte against the reviewed production tree. The A07 public example remains a conditional CLI result with native status `not-run`. The existing curved-mirror analytical source, pin and browser UI are unchanged.

## Hosted evidence

All 11 exact-head workflows passed. [Optical composition job](https://github.com/physicsvigilante/opticsim/actions/runs/44872114809/job/136748730960) passed 1,284 Node tests under the normal hosted suite.

The exact-head [authoring archive](https://github.com/physicsvigilante/opticsim/actions/runs/44872114809/artifacts/14694103408) matched SHA-256 `145053b88ab788722ccd05760bd35445292a3aa5e370def7e2ce845ccdbd42b2`. All 16 relevant files matched independent execution byte for byte, comprising four A07 conditional report files, four A07 native records, and the eight inherited A09 records.

This verdict applies to the exact source. Integration and post-merge tree and CI verification remain separate.
