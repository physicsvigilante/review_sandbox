# Independent Codex review of Opticsim PR #209

**CLEARED FOR OWNER DECISION.** I found no outstanding blocker in the conditional A12 comparison, its numerical guards, public dispatch, or the corrected v30 browser sequence.

| Identity | Reviewed value |
| --- | --- |
| Final candidate | `2bfd351f1c31eee2d9afd99c537743488eec1bad` |
| Tree | `3bd0baa7cb8ce3e0e6575b27565829b66868dde4` |
| Base | `f1ab2ae934837fe963f2b0c765290adf5f17deff` |
| CI merge | `2f115d4ee39c8c3f49ab4946ae762832c748fc45` |
| Frozen protocol commit | `0a78e0737a78e35e7d1715ec80ccdc12f1ae6e4a` |
| Analytical source blob | `1f5592c6de7184acbdee35c2753292c792875191` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

## Physical and numerical review

I checked the Problems-only A12 source against SHA-256 `d98c8b3aa6086b340c3d038d9821baf4be516bec27eb7892b94286bc7bed170d`. The parallel slab lies between the real object and the centre of curvature. The example uses explicitly assumed unit-index air. The unknown slab placement can stay symbolic because every fit in that region gives the same reduced distance and puts the first real image between the plate and the mirror. The bare image is 15 cm from the pole. The inserted slab gives a conjugate at 140/9 cm and changes signed magnification from −1/2 to −5/9. The image shifts 5/9 cm toward the object and its size grows by 10/9. No absolute object height is needed.

I independently traced two paraxial slopes from one transverse object coordinate and found their reflected intersection using the signed reduced slope and the appropriate return medium. The 16,362 comparisons covered three length units, different indices and placements, images before, in and beyond the plate, exact near and far faces including nonmatched interfaces, local virtual conjugates, and afocal branches. Of these, 16,318 qualified and 44 numerical guard cases withheld. Maximum finite position and shift discrepancies were below 7.7 × 10⁻¹⁰ mm, and maximum magnification discrepancy was below 3.1 × 10⁻¹². The exact arithmetic distinguishes equality in the supplied binary64 facts from unresolved near-focus or near-interface inputs. With equal indices and clear branch placement, insertion has zero shift and unit size ratio. The virtual result refers to a local continuation behind the mirror.

All 47 prior example inputs and plans matched the base. I independently exercised mixed requests in both directions. A v31 scenario still executed and reported all four native observations when the analytical query was unavailable. An analytical-only input retained its conditional answer and diagnosed the absence of a native scene for the incompatible observation. Native v31 and the earlier six test-only controls remain the finite sampling corroboration. The A12 analytical byte report explicitly records native status as not run.

## CI and archived evidence

The previous head passed the Node suite and failed the v30 browser test after a width edit could race the asynchronous restoration of the qualified file. The final change waits for the completed centred baseline before editing it. It changes only that browser test. The isolated final tree passed 27 focused tests. Real Chrome 158.0.8127.37 passed the corrected v30 workflow five consecutive times and passed the separate v31 workflow. The final hosted merge has the candidate tree and expected parents. All eleven workflows passed, including 1,228 Node tests and both profile-specific Chrome suites. [Optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44863249006)

The four archived analytical A12 files and the six archived v31 CLI files matched the independent runs byte for byte. Both profile Chrome downloads also matched the independent saves, including all five v30 attempts. I verified the CLI archive SHA-256 `6b13cf5ec07cbcd07953f4f8eb4bd9b3380a6be4bafaca724cb71704c32047f4` and the profile Chrome archive SHA-256 `897f11dae865bc7bfe0d2fc60789addfead54c4285ee7c729ba0f4597852b5a6`. [CLI archive](https://github.com/physicsvigilante/opticsim/actions/runs/44863249006/artifacts/14691180628) · [Profile Chrome archive](https://github.com/physicsvigilante/opticsim/actions/runs/44863249006/artifacts/14691170618)
