# Independent Codex review of Opticsim PR #215

**CLEARED FOR OWNER DECISION.** The corrected final head preserves exact matched-medium and qualified hemisphere-centre identities with consistent signed reference coordinates. I found no outstanding blocker in the A27 calculation or inherited v32 behavior.

| Identity | Reviewed value |
| --- | --- |
| Final candidate | `2a58b0af9883c4d0f3a889083604c757d2fc185c` |
| Tree | `2ac85111ebf8eb236ed1b91b811e695899b6ecf5` |
| Base | `3884d8167ecd65dcd7f5e1b653792a00f889285b` |
| CI merge | `24e4c982d00f736a00735063fe9a042c14fbfb0b` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source and numerical review

The A27 Problems-only image has SHA-256 `e0b938a74df9e6d302ee63a259164b9cfe31fe65b01a93e708774a3e5b404989`. It gives a 5 cm radius, index 1.6, the illustrated 3 cm cap, and an observer 8 cm above the base. The conditional A27 setup assumes unit-index exterior and a paraxial object in the interior limit at the base. The native v32 scenario instead specifies a source displaced 0.0625 mm inside the glass. The analytical CLI constructs no native source at the base.

With the positive axis from the base through the pole toward the observer, A27 gives a virtual coordinate 75/31 cm behind the curved pole. This puts it 18/31 cm from the base, so its distance from the observer is 230/31 cm, or about 7.42 cm. The prior candidate's floating-point operations could shift a matched object coordinate or exact hemisphere reference distance by an ulp. The corrected head uses the authored depth for a matched medium, and derives both reference distances from the stable apparent coordinate. The regressions cover non-round binary64 inputs exhibiting the previous drift.

I independently propagated pairs of paraxial slopes through the curved exit and to the observer reference across 4,104 cases, including 1,404 exact matched-medium and hemisphere-centre identities. The maximum coordinate discrepancy was below 1.82 × 10⁻¹² mm. All returned coordinates obeyed their declared reference expressions. Eight additional cases exercised domain and weak-contrast guards. The branch remains bounded to a minor cap or hemisphere, an observer beyond the pole, an interior index at least as high as the exterior index, and a separated interior point or declared base limit.

## Preservation and hosted evidence

The isolated candidate passed 24 focused tests. All 51 prior example inputs and plans matched the base. Mixed CLI requests worked in both directions. A v32 scene retained qualified native face and detector evidence alongside an incompatible analytical request. Reduced A27 facts retained the analytical result alongside the request for a native scene. The six independent finite-cap study runs still matched their native vector and signed projection checks. The v32 workflow passed all seven independent real Chrome checks.

All eleven hosted workflows passed, including 1,249 Node tests and real Chrome v32 qualification. The hosted merge has the candidate tree and expected parents. The four A27 analytical records, six v32 CLI records, six frozen native study records and qualified Chrome export matched my independent runs byte for byte. Archive SHA-256 values were `97182dda1314ff2005e91866b0b3b7b0e9c55b3b0fdad480ef4a17b7ac10cc2a` for authoring and `ef52c94a5831334a5f6355a68698dcfd4638a9163432610ef181214544c56536` for the profile browser archive. [Optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44867238867) · [Authoring evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44867238867/artifacts/14692657204) · [Profile Chrome evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44867238867/artifacts/14692771529)
