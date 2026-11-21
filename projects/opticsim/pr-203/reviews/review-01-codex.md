# Independent Codex review of Opticsim PR #203

**CLEARED FOR OWNER DECISION.** The final head qualifies the finite sampled flat-face range through the public v30 workflow and withholds it on incomplete or inconsistent execution. I found no outstanding blocker within the declared scope.

| Identity | Reviewed value |
| --- | --- |
| Reviewer | Codex, independently assigned by the owner |
| Head | `a85f2f78e2f5d6f773129eeb979832eb4a33dfb9` |
| Tree | `9f70f738d45530d394de9b6ca9032c8ee57a0a46` |
| Base | `9f8faf2b3bbef2486b7fafaf079aba260c6d900c` |
| Pinned native engine | `811f508d2b070898c241a568b0c167dcb8645251` |

## Authoring and provenance

I checked the explicit v30 selector, finite Beam geometry, signed leftward direction, native midpoint sampling and two-component profile. The public example preserves the A14 beam-to-hemisphere radius ratio and glass index. The revised record distinguishes assumed source brightness from numerical ray density and declares the chosen scale, source position, exterior index, disabled partial reflection and omitted table. The source asks about a continuous spot on the table. The qualified public quantity is the minimum and maximum **world y** among actual native flat-face callbacks, with sample count.

Schema v21 keeps its flat-entry Beam, v24 keeps its curved-entry SingleRay observation model and v29 keeps its planar fan. I checked the v30 browser fixture's parent against the v29 app blob `40ac623ed20887ff44e353f74c3fedce315b1695` and verified the v30 app blob `15655cc6ea8a25aea7fc0758c111841fd60bee51`. The frozen A14 protocol and study stayed at blobs `e39869486803761cb6f136e0a28cb5fd9a593977` and `3c736234b99481d92472754e02d68db3cd02742a`. [Public model and numerical policy](https://github.com/physicsvigilante/opticsim/blob/a85f2f78e2f5d6f773129eeb979832eb4a33dfb9/docs/CURVED-ENTRY-BEAM.md)

## Independent native and numerical checks

I rebuilt the existing pinned native core and browser bundle in an isolated export and ran the revised public example. The 37 focused tests passed, including the frozen study, prior v21/v24/v29 behavior and the historical v18 browser provenance chain.

- **Native continuity.** The audit keys each emitted native object by identity, compares its observed position and direction at consecutive callbacks, and checks that the reported intersection lies ahead on the incoming line. It checks the outgoing origin, side of the boundary and Snell tangential component after the delegate returns. Completion requires one source start, no pending ray identities, two transmissions per emitted sample, the per-face counts, clean diagnostics and the terminal completion event. Only then does the audit attach the measured extrema to the flat-face result.
- **Numerical reproduction.** I ran 162 admitted variants with radii 50, 100 and 1,000 mm, large positive and negative translations, three exterior/interior choices including near-matched indices and ratio 1.6, both signs of 180°, three densities and both component orders. I independently enumerated native midpoint ordinates and used vector Snell transmission at the circular arc to predict the flat ordinate. Across 2,358 native rays all counts agreed and the largest error in a reported extremum was 1.26 × 10⁻⁸ mm. The published centred example gave 20 samples spanning −32.145125913 to +32.145125913 mm.
- **Boundary controls.** I bracketed the v26 half-integer guard on both sides of 20.5. Values inside the uncertainty band were refused, and values just outside produced the expected 20 and 21 samples. The 100-sample endpoint qualified. Thirteen additional invalid cases covered direction, brightness, density, beam width, central illumination, clearance, material ratio, radius limits, disabled Fresnel branches, extra optics and missing opt-in.
- **Withholding.** I independently injected nine faults spanning missing, cloned and repeated ray identities, shifted ray geometry, incorrect outgoing direction, absorption, unexpected child rays, undefined behavior and warning state. The accepted observations were withheld. I also checked changed-scene hash suppression and an older summary with a v29 flag but no v30 proof. The latter failed snapshot, notebook creation, replay and comparison qualification; a two-sample sweep retained the failed sample and qualified the fresh run.
- **Real Chrome.** Using a Windows-specific launcher in the disposable export, Chrome 158.0.8127.37 ran the final-head public package. It reproduced the baseline, cleared the measurement and disabled qualified save on an invalid source offset, measured eight rays after narrowing the Beam to 40 mm, restored the original and freshly retraced the downloaded edit on reopen. The downloaded package recorded the 100→40 mm physical edit without per-run readings. The browser report recorded six checks and one screenshot.

## Exact-head hosted evidence

All eleven pull-request workflows succeeded. The optical job logged 1,192 passing Node tests. The v30 real-Chrome step passed six checks and produced one screenshot with Chrome for Testing 158.0.8127.36. I downloaded and checked both ZIP digests. All six archived public authoring files matched my independently generated files byte for byte. The browser's downloaded qualified revision also matched my local Chrome export byte for byte. The full-suite count and Linux Chrome result are hosted CI evidence. The numerical grid, callback faults, historical-summary checks and Windows Chrome run above were independently executed. [Exact-head optical job](https://github.com/physicsvigilante/opticsim/actions/runs/44857670433/job/136703556463)

| Archive | SHA-256 |
| --- | --- |
| [Public authoring evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44857670433/artifacts/14688478069) | `9b855d91a0ce5542a9d1440c90ee8c98cc41d3a9a8dfbd2ceee61c884cef72e5` |
| [Browser evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44857670433/artifacts/14688169462) | `a8942358404ffeb6e5e72755437a89378c96e468480af730b358f2b399bd350e` |
