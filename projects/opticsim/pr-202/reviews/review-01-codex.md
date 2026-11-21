# Independent Codex review of Opticsim PR #202

**CLEARED FOR OWNER DECISION.** The revised test verifies native completion, ray identity, entry and exit transmission, and the flat-face positions of sampled meridional rays. I found no outstanding blocker within that scope.

| Identity | Reviewed value |
| --- | --- |
| Reviewer | Codex, independently assigned by the owner |
| Final tested head | `472bc605fdca21b38fe4e519521a18a18850ec6f` |
| Git tree | `dce388685ac2181033924bf373aa17223f782a63` |
| Base | `ec0b487e21d65c0ea7b1143d6fed3b8a9175218e` |
| Original freeze | `d52cd85f86b1ebc5c10ff11a4a312b57075282ce` |
| Pinned native core | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source and scope

I read the original A14 Problems image. Its SHA-256 matched the atlas at `f4ab4b63f956986c04a17ba0c4db99b71ce75f0c86bfef86b08b5002e24aba6a`. It describes an axially centred vertical beam of radius r entering the curved surface of a glass hemisphere of radius 2r and index 3/2. The source asks for the radius of the spot on a table. The frozen centred study chooses a 100 mm hemisphere radius and a 100 mm full beam width, preserving that ratio. Rotation of the meridional section places the flat face at x = 0. Unit exterior index, explicit brightness and transmitted-only treatment are declared choices. The offset narrow beam is a separate control.

The freeze predates the native test in the Git graph and retains blob `e39869486803761cb6f136e0a28cb5fd9a593977` at the final head. The two changed paths are the freeze and the test. The study uses the pinned Beam and one Glass with an actual circular arc and closing diameter. It calls the native loader directly in the test. Public v21 admission remains restricted to its existing direction and face. [Frozen study](https://github.com/physicsvigilante/opticsim/blob/d52cd85f86b1ebc5c10ff11a4a312b57075282ce/evaluation/curved-entry-beam-v1/frozen.json)

## Reviewer reproduction

I ran the final Git-blob test in an isolated snapshot using the installed pinned core. The snapshot's base tree matched the merged PR #201 base. The test tracks each emitted native object by identity across the two boundary callbacks. Each wrapper delegates once, and the signed outgoing direction is checked after the native refraction callback. The final assertion requires both an observed simulationComplete event and clean terminal diagnostics.

| Frozen configuration | Sampled rays | Minimum flat ordinate (mm) | Maximum flat ordinate (mm) |
| --- | ---: | ---: | ---: |
| Centred, density 0.2 | 20 | −32.145125913 | 32.145125913 |
| Centred, density 0.4 | 40 | −33.023013661 | 33.023013661 |
| Offset narrow beam | 8 | 1.666724564 | 25.218444346 |

I independently observed the actual native source and both boundary callbacks in the three frozen configurations, then added a negative offset and two other radius/width settings. For each of 106 native ray identities, I checked the launch midpoint and direction, circle entry, direction after entry, flat hit, incoming direction at the flat face and outgoing transmission. My comparison projected the incident unit vector onto the local tangent, applied the index ratio there and recovered the transmitted normal component. The largest difference between a predicted flat ordinate and its native callback was 6.253 × 10⁻¹³ mm. Both centred runs sampled symmetric extrema. Reversing the narrow beam's offset reversed its measured span.

## Negative controls and claim limits

On the original head, an isolated mutation suppressed receipt of simulationComplete while preserving the stop event. The test still passed. The revised head explicitly requires completion. I repeated the same intervention and observed the expected test failure. A separate mutation directed a flat-face outgoing ray back into the glass and failed the new transmission assertion. The unmodified final test also rejected the limited run and its reflected-ray control.

The evidence supports sampled positions on the physical flat face in a two-dimensional native model. The difference in extrema when density changes shows why the largest sampled ordinate is insufficient to establish a continuous spot radius. Table coupling, radiometry and three-dimensional illumination remain outside this test. The hosted test prints aggregate spans. It retains per-ray callbacks in process for assertions and does not publish a per-ray evidence archive.

## Exact-head hosted checks

All eleven pull-request workflows succeeded. The optical job logged 1,187 passing Node tests, including the revised A14 study. All three hosted sample counts and their full-precision extrema matched my local reproduction. I also ran the focused A14, v21, v24 and curved-entry feasibility suites locally, with 22 tests passing. The 1,187-test count is hosted CI evidence. The 106-ray vector comparison, missed-completion intervention and altered exit-direction check were independently executed. [Optical job and A14 test output](https://github.com/physicsvigilante/opticsim/actions/runs/44856266425/job/136699101538)
