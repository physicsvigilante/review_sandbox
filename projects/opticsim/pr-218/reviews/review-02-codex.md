# Opticsim PR #218 independent focused review R2

**CLEARED for owner-authorized integration at the exact candidate below.** The opposite-circle reflection blocker is resolved.

| Identity | SHA |
|---|---|
| Candidate | `bf80e03aa1b0fdf997a094a3976890a4857b6af6` |
| Candidate tree | `2c90a07d86f6d311d6fc84e3fe83d8786711500a` |
| Production base | `f6fa244f58993e2e741561d3395b91eb015d7314` |
| GitHub PR test merge | `15d75ebb6a54334866ec195373151d68bab2e7f0` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

The two parents of the test merge are the base and candidate. Its Git tree is identical to the candidate. [Original blocked review](https://github.com/physicsvigilante/review_sandbox/blob/f22875619c86efbc9a3f1d304c25323877ec2d3e/projects/opticsim/pr-218/reviews/review-01-codex.md).

## Focused correction and optical evidence

- The authored concave minor arc has its centre left of the pole. A hit must be on the positive radial-x branch, inside the y rim clearance, and agree with the actual reflection and direction checks. That condition excludes the opposing backing-circle root without narrowing the declared minor arc. Native `ArcMirror` still chooses and propagates its own contacts.
- The original delegated wrong-root v34 case now withholds readings after all three contradictory reports. The genuine arrangement still qualifies. I separately used a v31 geometry in which the wrong backing-circle root lies after the detector on the outgoing leg. Three genuine native intersection reports were replaced after the first detector encounter. The audit withholds the resulting native readings. The genuine v31 control still qualifies.
- I independently recorded 702 actual native ray histories across 216 v34 and 18 v31 configurations on the final source. For v34, direct and reflected rays traverse only their respective authored native sequences. Across positive and negative world translations, three radius/index combinations, three source depths and both detector orientations, the finite reflection and planar refraction calculation agreed with the measured positions and tangential directions within 1.40e−8 mm and 1.03e−11. In the A28 geometry the finite-ray intercept estimates agreed with the separately modeled paraxial coordinates within 0.007713 mm. At the focal setting the finite sampled reflected slope was at most 7.27e−7.
- The common audit verifies both channels from native emission through each interaction, actual segment origins and directions, finite mirror and detector rims, per-contact signed power and the terminal accumulator. v31 preserved outward and return detector increments of opposite sign for both orientations and densities 0.95, 0.97 and 1. The six v31 and six v33 genuine CLI example files were byte-identical to independent execution on the previously reviewed production tree.
- The original A28 Problems image matched its frozen hash and stated radius, refractive index and bubble depth. The independent conjugate calculations and inherited six native A28 controls retain their separate meaning. v34 explicitly represents a near-axis patch in a half-space with selected finite sampling. Its public outputs are measured callback counts and detector events, with signed detector power expressed in relative units. Conditional Gaussian positions and the exact paraxial focal limit are studied separately.
- Independent execution passed 30 focused Node tests including inherited A28 and A15 cases, and all seven v31 and seven v34 checks in real Windows Chrome 158.0.8127.37.

## Hosted evidence

All 11 exact-head workflows succeeded. Optical composition job [136743300171](https://github.com/physicsvigilante/opticsim/actions/runs/44870365425/job/136743300171) passed 1,268 Node tests and both seven-check browser suites on Chrome for Testing 158.0.8127.36.

The exact-head [authoring archive](https://github.com/physicsvigilante/opticsim/actions/runs/44870365425/artifacts/14693107958) matched SHA-256 `9a2c2c6deb8710a2c2644a1da1cdd60fc0dec2ae9578590c37551f3542d90fe7`. All 18 independently replayed records matched the archive byte for byte, comprising the six v34 example files, six v31 example files, and six inherited native A28 files.

The [browser archive](https://github.com/physicsvigilante/opticsim/actions/runs/44870365425/artifacts/14693986090) matched SHA-256 `2c0d27abba301cf9e357d29cf6c7d5e14e3c16ede727a1f1479f2412d87140e6`. It contains both browser reports with the same seven independently passing check identities per profile, a screenshot per profile and a qualified revision download per profile.

The exact candidate passes focused review. Integration and merged-tree CI remain separate gates.
