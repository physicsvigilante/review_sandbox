# Independent Codex review of Opticsim PR #210

**CLEARED FOR OWNER DECISION.** I found no outstanding blocker in the A22 limiting inverse, the strict direct minimum, public dispatch or the native corroboration.

| Identity | Reviewed value |
| --- | --- |
| Candidate | `a60797edf9c46b1d27b5febe1618bc413f02523b` |
| Tree | `ed07a68d92a59077542d7979ef9144851d65212e` |
| Base | `20d2f2527376c461a973bd51a7a09a047249541c` |
| CI merge | `9e5e97d5f1f218b7fedb3f8c779617a6c51f9af8` |
| Protocol commit | `3161503ba987924755e9077b3879070a448c5250` |
| Protocol blob | `75ec6da3fc0487e560fedbff0f2b14cfd9a1f1bd` |
| Analytical source blob | `62f99d9ddb1aa69a5a38736d573b9f05706cf636` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source and mathematical review

I inspected the Problems-only A22 image at `08_Ray_Optics_Explanations/05_Prism/Problems/004.png` and checked SHA-256 `ab8949d8594431b2e88cd81b3fdaa683255ce2925a938531738a72f82cbad7aa`. The source gives a 45° isosceles prism and a 45° incident angle at grazing emergence. The example declares a common unit-index exterior and the nonnegative direct two-face meridional branch. The inferred relative index is √5, which gives the absolute index under that exterior assumption. At strictly transmitted minimum deviation the symmetric incidence and emergence are both 58.837837° and deviation is 72.675674°.

For the dense prism the inverse uses the positive Snell root. I solved the critical residual separately by bracketing 4,644 input and exterior cases. The 1,985 qualified inverses agreed within 1.4 × 10⁻¹⁵ in relative index. The remaining 2,659 could not reach the grazing premise within the declared absolute index domain. For a known index, each nonnegative internal angle must lie below the same critical angle. A strict direct branch exists only when their sum can be less than twice that angle. On this interval the exterior-angle function is strictly convex, and the symmetric pair minimizes deviation once it is admissible. I checked 1,161 known-index branch cases and 85,244 strictly transmitted deviation samples. Critical and near-matching statuses withheld where required. Both sides of the numerical critical band were checked. An actual finite ray must still reach the two faces.

## Native and integration evidence

The isolated candidate passed 94 focused tests. I reproduced all five v8 runs and compared the actual face contacts, incoming directions and outgoing vectors against the face equation and vector Snell/reflection conditions. The 44° sample experienced TIR at the second face, while the 46° sample transmitted. The 55° and 62° deviations exceeded the 58.837837° sample. The maximum face equation residual was below 3 × 10⁻¹⁴ mm and the maximum tangential or reflected component residual was below 6.4 × 10⁻¹⁵. The exact 45° boundary is analytical.

All 48 prior public example inputs and plans matched the base exactly. In a mixed request against a v22 Beam prism scene, all seven native observations remained qualified and both incompatible new calculations returned unavailable. For reduced A22 facts the two conditional results stayed available alongside the diagnostic for a requested native observation. Real Chrome independently passed the v22 prism Beam and v29 critical fan regressions.

All eleven hosted workflows passed on the candidate tree and expected merge parents, including 1,232 Node tests and the real Chrome v22 and v29 suites. The four byte-bound analytical files and five native archive files matched my independent runs byte for byte. I verified the archive SHA-256 `5751e7b2d6e266bedc0beea1c76e5ef208018f96e4c12082ba1e03bc5994deb2`. [Optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44863686908) · [A22 authoring evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44863686908/artifacts/14690024271)
