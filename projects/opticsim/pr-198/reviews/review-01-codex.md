# Independent Codex review of Opticsim PR #198

**CLEARED FOR OWNER DECISION.** I found no blocker in the conditional meridional analytical model, its numerical boundaries, the public authoring workflow or the pinned native comparisons.

| Reviewed identity | Value |
| --- | --- |
| Reviewer | Codex, independently assigned by the owner |
| Head | `19b85cadb7e9085573673016bdf8510995f93b71` |
| Tree | `4af969b1b8db9867aeaf0cab4c69becca1d213a9` |
| Base | `854e870f5a51453fa75bcc9fffbe989f53adac50` |
| Protocol commit | `61a3613dbabadd54316cb6a42c5a7ca5c64e1d82` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source and freeze

I verified the protocol commit is the direct child of the base and the direct parent of the implementation. The protocol retained blob `5c726f4a3740392c2071d9ecb79cf245095aad67` and SHA-256 `3a94ace7ddee5d5cecdc8d173a21c180baba08ae89816b38612930cd2cfa2d3f`. That history establishes the order of the committed records. I independently hashed the pinned source archive and inspected only the two named Problems images. Both PNG digests matched the freeze. A17 shows grazing entry at AB and emergence at adjacent BC. A19 gives pipe index 1.36 and air outside. The examples explicitly identify the common exterior and the meridional and air-index assumptions. [Frozen protocol](https://github.com/physicsvigilante/opticsim/blob/61a3613dbabadd54316cb6a42c5a7ca5c64e1d82/evaluation/perpendicular-dielectric-faces-v1/frozen-protocol.json)

## Reviewer execution and physics checks

I built the existing test core from the installed upstream pin in a disposable export. All eight changed files were checked against or restored from their exact head Git blobs before the final run. All 61 tests in the two-face, v29 fan, method suitability, suitability hardening, reduced prism and public workflow suites passed.

- **A17.** Snell transmission at entry gives an internal angle approaching the critical angle α as launch approaches 90° from below. At the perpendicular wall the complementary angle gives sin θ = cot α = √(m²−1), for a common exterior and relative index m. The returned bound √2 is a relative-index bound. Below it the limit permits transmission. At equality the limiting exterior direction is tangent and every finite launch below grazing is on the TIR side. Above it the limit is on the TIR side. The symbolic result distinguishes the equality, and a numerical input of binary64 √2 correctly withheld classification.
- **A19.** For an interior ray reaching the sidewall, strict TIR requires nEntrance sin i < √(nCore²−nWall²). With the example's explicit air approximation, the open interval is 0° < i < 67.1814275379747°. An axial ray misses the wall and an interior equality is critical. The 90° grazing endpoint stays excluded when the numerical aperture reaches or exceeds the full input range. An exact representable Pythagorean material tuple, e.g. entrance 1.5, core 2.5 and wall 2, distinguished equality from a nearby unresolved binary64 tuple.
- **Independent numerical controls.** I checked 728 valid absolute-index tuples on a quarter-index grid over [1,4] against bisection on the internal angle and critical incidence. Every endpoint and all-interior classification agreed, with 2 × 10⁻¹⁰ degree tolerance away from exact equality. The exact-equality predicate is valid over the specified binary64 index range. Tests also covered near-matched indices, rounded √2, material contradictions and missing facts.
- **Native controls.** I reran the four frozen off-boundary v9 square Glass controls. A17 at 75° transmitted for index 1.25 and reflected internally for 1.6. A19 at 1.36 reflected internally at 50° and transmitted at 75°. The tests checked native entry and target face, points, branch and direction against their frozen tolerances. I also constructed 32 independent single-ray scenes with four core indices, four finite angles, both launch signs, a different rectangle and translated entry points. All completed without warnings. The actual upper or lower wall, hit point, outgoing direction and branch matched analytic expectations in all 32 cases, including 18 transmissions and 14 TIRs. These finite controls establish selected rays and encounters. Finite reach for arbitrary sources, equality and exactly grazing launch remain outside their evidence.
- **Integration and withholding.** Both examples ran via the public CLI with method suitability reporting the proper analytical contract, zero native calls and four analytical evidence files each. Neither generated a qualified native scene. I checked a mismatched fact family, unresolved boundaries and a mixed analytical/native request. Correct analytical results remained conditional while the reduced facts supplied no native run. The existing v29 critical-sample, absent callback, stop and missing-marker tests passed, and the native engine and v29 qualification logic have no delta in this PR.

## Exact-head CI

All eleven GitHub pull-request workflows succeeded on the reviewed head. I checked the optical job's full-suite and real-Chrome v29 steps. The hosted runs are CI evidence. The numerical grid, independent rectangle runs, four frozen controls, original-image inspection and CLI runs above are my own. The decision covers conditional geometrical optics at perpendicular faces. General cylindrical skew rays, waveguide modes and finite wall reach require different evidence. [Exact-head optical job](https://github.com/physicsvigilante/opticsim/actions/runs/44852173069/job/136685837990)

I downloaded the optical workflow's authoring ZIP and verified SHA-256 `fab9f5afc49c51b4f42b7a7f077633f66be4c8d8063c2ef76bfcaaca6b2d0322`. All 12 two-face members matched the reviewer run byte for byte, including the four native controls and both sets of public analytical evidence files. [Authoring artifact](https://github.com/physicsvigilante/opticsim/actions/runs/44852173069/artifacts/14685468579)
