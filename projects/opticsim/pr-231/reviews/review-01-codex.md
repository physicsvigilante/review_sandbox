# Independent Codex review of Opticsim PR #231

**Outcome: pass. No unresolved blockers or demonstrated defects within the frozen study.**

- [Source PR #231](https://github.com/physicsvigilante/opticsim/pull/231), production base `99b0c6d419f3cfead53915198472a14c67cc39ab`.
- Exact reviewed head `4a1f3f31d4c7c795a4cc9924cdfc6279043a62b9`, Git tree `9ed1e5c963b0df0bdae57c4d7425bd0b3ffa4156`. [Exact source](https://github.com/physicsvigilante/opticsim/tree/4a1f3f31d4c7c795a4cc9924cdfc6279043a62b9)
- Reviewer: independent-in-context Codex agent, 2026-11-21. Scope: Problems-only interpretation, thin and finite return optics, real native callback topology, control validity and evidence integrity. Production code and browser UI are unchanged by the study. No production source changed during the review.

## Source and signed optical model

I read only Lens Formula Problems 004 and 006. Their SHA-256 values matched the frozen `f26b8374f0bd334d9c0dc20b4cf2c0a1adacd1ad52e6b309ef7bff4b05da0dab` and `cc731e23171c515bea95c236474b2077c9634bd881e3a2b54aaee1226d9cb15d`. The source ZIP matched `03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939` and the archived Git blob at `d33b45226348d9b0c701f2a3e8b86dd1285de2d0`. Solutions material remained unopened. The protocol at `b9ace7c371d0cb9d429786ea265398ac3d8bebb4` precedes the test implementation and has the same frozen JSON bytes.

004 supplies an equiconvex lens of index 1.5 and focal length 60 cm with one silvered face. Its thin-element interpretation in air gives curvature magnitudes of 600 mm. 006 supplies a thin equiconvex lens of index 1.5 with both radii 25 cm and asks for a self-conjugate object position. Unit-index exterior and incidence from the uncoated face are explicit assumptions. Neither problem supplies a 20 mm internal pole separation, a finite mirror patch or a detector.

In an unfolded travel coordinate with the transverse axis fixed, the entrance and return refractions each have power `(n−1)/R`. The concave immersed patch contributes `2n/R`. Two translations by the declared in-glass pole separation divided by n give the finite matrix. Exact independent matrix calculation verified the signed left-side limits of −150 mm for collimated return and −125 mm for the nonzero incident-side self-conjugate. The actual synthetic 20 mm pole separation predicts `−1477200/10591 mm` and `−5750/49 mm` respectively. The second finite self-conjugate root is `+1000/73 mm` in the authored x coordinate and lies outside the incident-side object branch.

## Pinned native evidence

I rebuilt the isolated test core from PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`. Both study tests and 11 adjacent native optical preservation tests passed. The study launches one genuine native SingleRay per run. The four reflected runs produced Detector → front CircleGlass → ArcMirror → front CircleGlass → Detector, with rightward incident and leftward return directions. The four mirror-removed runs used the same launches, traveled through both sides of the circle and produced a single rightward detector crossing.

Independently solved the finite circle and selected mirror-patch intersections, applied vector Snell refraction and specular reflection, and compared all 32 raw callback points and slopes. The largest component-wise point discrepancy was `2.28e-13 mm`, and the largest slope discrepancy was `6.16e-17`. The closest mirror hit was 11.5056 mm from its transverse aperture endpoint. The measured returning rays crossed the axis at `−139.47615460632053 mm` and `−117.34627003264947 mm`. Both symmetric launch partners agreed in each case. The maximum axial residual from the finite first-order prediction was `0.000759755 mm` against the predeclared 0.05 mm tolerance.

The CircleGlass and separate internal mirror agree with the experiment's local first surface and separated reflection. The mirror-removed control exposes the actual far side of that circle. The study measures sampled outgoing lines. It carries no claim of native image detection or a native touching silvered lens.

## Hosted CI and retained evidence

All 11 exact-head PR workflows completed successfully. The optical workflow logs identify synthetic checkout `f7d3fb968da3eb741e7aa2f9a578c262d3dc702d`, its stated base and head, both study tests and 1,343 passed Node tests with zero failures or skips. Independent Git merge-tree computation reproduced the reviewed tree. The incumbent real Chrome acceptance suites also passed. [Optical composition CI](https://github.com/physicsvigilante/opticsim/actions/runs/44884125218) · [Unified workflow CI](https://github.com/physicsvigilante/opticsim/actions/runs/44884125235)

I downloaded authoring archive `14699271603` and verified SHA-256 `138eca795087e8b961e154906b253c3ba3ff60859c098fe26150f1316b6b148f`. Both raw study JSON files matched the isolated native replay byte for byte, including all mirror-present and mirror-removed callbacks. The collimated file hash is `358534ef87e1156134805119ab648fe647120f89a40fe595cc3a321a315712f6` and the self-conjugate file hash is `55a733b5c0b27951bd6ecbac66eac5aaf3759aa0a263c893307db6a7d8124d81`. [Archived evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44884125218/artifacts/14699271603)

The other passing workflow IDs are `44884125220`, `44884125239`, `44884125240`, `44884125245`, `44884125248`, `44884125253`, `44884125255`, `44884125262` and `44884125286`. This clears the exact test-only source for owner-authorized integration.
