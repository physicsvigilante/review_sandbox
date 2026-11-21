# Independent Codex review of Opticsim PR #205

**CLEARED FOR OWNER DECISION.** Both queries produce the declared first-passage geometrical intervals. I found no outstanding blocker in the physics, numerical withholding, method dispatch or native controls.

| Identity | Reviewed value |
| --- | --- |
| Reviewer | Codex, independently assigned by the owner |
| Source head | `229997057ab0ad20228bc0abffd2e98d15b2865f` |
| Git tree | `a3b21a62830724bf223a5c999eeefa0175a9e069` |
| Base | `25630fd8821f879d41553e40f4585f9f781fb1fc` |
| Protocol commit | `e7d0724a774935a65b5d8ecd8fb217fc61ade4c4` |
| First native test commit | `781cb7f4ebfbec4e3f058c0e48857431882d9936` |
| Pinned PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source and expectations

I read the two named Problems PNGs. Their SHA-256 values matched the frozen record at `f4ab4b63f956986c04a17ba0c4db99b71ce75f0c86bfef86b08b5002e24aba6a` for A14 and `214f77a38e222b9a520df73c6fc7194df22919b1e3ae82e436fa474955810f8e` for A20. The protocol preceded the native witnesses and production calculator. Its SHA-256 is `7e16ec41c799aec47ebf6d61ad1085ac77d25f62eda1281925d01540485c6881`. The native test retained Git blob `774c6f54be64062afe2f4e229de9d0f3ed2fa70a`. [Frozen expectations](https://github.com/physicsvigilante/opticsim/blob/e7d0724a774935a65b5d8ecd8fb217fc61ade4c4/evaluation/semicircular-boundary-intervals-v1/frozen.json)

- **A14.** The source has a centred beam of radius r, a hemisphere of radius R = 2r and index 3/2, and a table touching the base. With the explicit filled-beam, symmetry and exterior-index assumptions, the first-incidence disk radius is 4r/(2√6+1), approximately 0.678083389r. Its section extends from −0.339041694R to +0.339041694R about the optical axis. A visible spot with that extent requires the contacting table to register the incident light. Neither the source facts nor the native control specify the table response or intensity distribution.
- **A20.** The source specifies 45° incidence in a transverse section through a half cylinder of index √2. At the assumed unit exterior index the inner ray angle is 30°. If t is the signed flat-face entry displacement divided by R, strict transmission at the **first arc encounter** holds for |t| < √(2/3). Equality gives the critical limiting direction. Between that threshold and either excluded joint, the first arc encounter gives TIR. These coordinates describe positions at entry into the flat face. They are distinct from arc coordinates and from later paths of reflected light.

## Independent checks

I rebuilt the pinned native core in a disposable export with all nine changed files restored from their exact Git blobs. The 58 focused tests passed. The A14 and A20 public CLI inputs each yielded conditional analytical evidence with no native run.

1. **Curved entry.** I projected a horizontal entering ray onto the tangent at its circle entry, applied vector Snell transmission, and propagated to the diameter. Both endpoints agreed with the public calculator within 2 × 10⁻¹² in units of R over 30 combinations of materials and signed illumination intervals. All 15,030 ordered samples were strictly increasing and enclosed by the returned bounds. I also checked the monotonicity argument analytically: for h ≥ 0 the normal tilt minus the refracted angle grows with h when m > 1, so h/m and the positive secant factor grow together. Odd symmetry covers h < 0. Rotational symmetry supplies a disk only for the declared centred filled circular illumination.
2. **Flat entry.** I independently refracted at the plane, solved the forward line-circle intersection and computed the incident sine using the local circle normal. Across 42 angle/material combinations and 8,274 signed entry offsets, branch labels and angles agreed. Thirty-two combinations had an interior critical threshold and ten admitted the whole open diameter. I probed thresholds on both sides of the joint uncertainty band and verified that near index matching withholds the result. The arc critical limit and the excluded flat/arc joint retain separate meanings.
3. **Native corroboration.** I reran all eight frozen controls. The three v30 trials used actual emitted coordinates and the verified native flat-face span. In each trial the continuous endpoint interval strictly enclosed the sample extrema. The five v21 trials used one actual native emission each, an observed flat entry at the declared ordinate, and the first native arc callback from inside. A20 at ±0.9 reflected internally; at −0.7, 0 and +0.7 it transmitted. I added eight tests with ±45° and both signs of entry offset. Native local incidence and branch matched the independent line-circle calculation. Exact critical equality has analytical evidence only.
4. **Dispatch and history.** With both result kinds in one analytical problem, the compatible result remained conditional and the opposite entry-face request was unavailable. A valid native v30 face request alongside an incompatible analytical request still executed and qualified its 20 rays. The unrelated query returned `UNSUPPORTED_FACTS`. All 43 historical public problem plans matched the base-equivalent #204 export.

## Exact-head hosted evidence

All eleven pull-request workflows passed on the reviewed head. The optical log recorded 1,211 passing Node tests and identified each of the three v30 and five v21 trials. I downloaded the authoring ZIP and verified SHA-256 `5ee366354ec4bfe26f3f9a5712a9015d8a0c6c9cbd7c499a7a8e6c300a427be9`. All sixteen relevant files matched my runs byte for byte: eight native control records plus four public analytical files for each source. The full-suite count is hosted CI evidence. The focused tests, independent geometry, signed native controls and artifact comparison were performed separately. [Optical CI job](https://github.com/physicsvigilante/opticsim/actions/runs/44859971769/job/136710874664) · [Authoring evidence ZIP](https://github.com/physicsvigilante/opticsim/actions/runs/44859971769/artifacts/14689003534)
