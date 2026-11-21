# Independent Codex review of Opticsim PR #200

**CLEARED FOR OWNER DECISION.** The final public A40 report answers both requested adjustments. I found no outstanding blocker for the declared paraxial model.

| Identity | Value |
| --- | --- |
| Reviewer | Codex, independently assigned by the owner |
| Head | `e9859dd0497a1eeba15eb661d15b11f09ed35688` |
| Tree | `3b3e311dcf58bdde8b519df8bcd0e8ae15f115ec` |
| Base | `7c18b46c05cc49b9a39642619abaae6979c71595` |
| Protocol commit | `5ac9412e072f482eedcb5484becd0234314028ad` |
| Native control commit | `20fcba213de290c72705925a608e9c7b9324b378` |
| Upstream PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source interpretation and results

I inspected the A39 and A40 Problems images and checked both image digests against the protocol. I verified the protocol and native control were committed in sequence before the analytical implementation and that both blobs remained intact at the reviewed head. The protocol SHA-256 is `312146f626e5a6428766980abc5fb491636580dfcef82178738b3022814bc659`; the native control Git blob is `d233e45585ce1112bd03fb444e8ad1fcae03a050`. [Frozen protocol](https://github.com/physicsvigilante/opticsim/blob/5ac9412e072f482eedcb5484becd0234314028ad/evaluation/separated-lens-angular-focus-v1/frozen-protocol.json)

- **A39.** The image gives a 160 mm tube but leaves the tube-length convention unspecified. At mechanical spacing 160 mm the intermediate image lies 135 mm from the objective. The implied object distance is about 4.12214 mm and the angular gain relative to unaided viewing at 250 mm is −327.5. When 160 mm denotes the interval between focal planes, the lens spacing is 189 mm and the gain is −400. Both numbers are conditional on the explicitly chosen convention.
- **A40.** The source asks for the angular magnification in both adjustments. The final public CLI returns 0.55 m initial spacing, far gain −10, near spacing 0.5763157895 m, outward eyepiece shift 1/38 m, and objective-referenced finite gain −200/19. The example explicitly measures the 10 m object distance from the objective, treats the Moon as collimated input, and assumes a relaxed eye at both adjustments. Unchanged accommodation alone does not specify that state. Using the eyepiece as the naked-eye comparison plane changes the finite gain by (u+d)/u. I reproduced this alternative and verified both distant-reference gains agree. The first candidate's A40 report omitted the distant gain; the reviewed head includes it. A fixed finite viewing distance has no analogous infinite-object reference, and its result omits that field.

## Reviewer execution

I rebuilt the pinned test core and tested a disposable source export with the changed files restored from the reviewed Git blobs. All 58 tests in seven suites passed. These covered the new analytical and native behavior, public authoring and method suitability, and regression checks for contact power, prism and perpendicular-face analysis.

- **Independent first-order optics.** I started two rays at one finite off-axis object point and propagated height and slope separately through each lens and intervening space. I determined the spacing that made their outgoing slopes equal. Across 702 admitted combinations of focal lengths, object distances, input conventions, angle references and units, the public solution agreed with this calculation for object distance, spacing and signed gain to a scaled tolerance of 10⁻⁹. Six explicit infinite-object cases yielded parallel outgoing pencils and the expected inverted ratio. I checked ten additional invalid, unsupported or ill-conditioned cases and both sides of near-focal spacing in all three units. Each withheld the numeric result.
- **Pinned native witnesses.** I reran the frozen tests of the two microscope tube interpretations, the finite telescope adjustment and off-axis input at infinity. I also traced six independently specified scenes with other focal lengths and both signs of object height. In all 18 downstream detector callbacks, the measured direction agreed with the eyepiece-referenced gain within a scaled tolerance of 10⁻⁷. In a separate sensitivity test, moving the eyepiece 1 mm from focus changed the measured spread of outgoing slopes from approximately 6.1 × 10⁻¹⁷ to 0.01257. The sampled rays distinguish collimation from this deliberate defocus. They do not establish finite pupil throughput or a detected image.
- **Authoring and evidence.** Both source examples ran through the public CLI. Each reported a conditional analytical result and zero native calls, and produced input, plan, analytical results and report files. The assumptions survived in the evidence. Native corroboration came from separate, explicitly geometrical scenes. The upstream engine and scene admissibility have no delta here.

## Exact-head hosted evidence

All eleven pull-request workflows succeeded on the reviewed head. The optical log recorded 1,181 passing Node tests and specifically identified all four separated-lens native controls. I downloaded the authoring ZIP and verified SHA-256 `237b653405d05967b785b8032eaddbbc56bf89c5f747ff3b555dc24f691425fe`. All eight archived A39/A40 files matched the independent public CLI runs byte for byte. The full-suite count is hosted evidence. The focused suites, paraxial propagation, defocus control, source inspection and artifact comparison above were independently performed. [Optical CI job](https://github.com/physicsvigilante/opticsim/actions/runs/44854679125/job/136693973980) · [Authoring evidence ZIP](https://github.com/physicsvigilante/opticsim/actions/runs/44854679125/artifacts/14686224396)
