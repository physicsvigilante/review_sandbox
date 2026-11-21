# Opticsim PR #221 independent exact-head review

**CLEARED for owner-authorized integration at this exact candidate.** No release blocker found.

| Identity | SHA |
|---|---|
| Candidate | `e09680420729e779e3366d14cc6e6bda4576e164` |
| Candidate tree | `921dec7667d5b2e390a47b3398b0c351d9127b3c` |
| Production base | `cf973b912898f2524c142570ab745f8989627a2d` |
| GitHub PR test merge | `2f3d58d0bec92973192a0176f2a63e3455556617` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

The PR test merge has the reviewed base and candidate as parents and exactly the candidate tree.

## Source and physical model

I independently viewed the original A08 Problems image. Its SHA-256 `512656b8d3711783be9bb571086609872e7618c390b296a121d8d8c50f9b9f4c` matches the frozen record. Solutions stayed unopened. The source defines the displacement about the centre of curvature with the positive direction away from the mirror. Consequently the pole-origin normalized object coordinate is U=2+cos(2πτ), where τ=t/T. The first paraxial conjugate of a stationary concave mirror is V=U/(U−1), with signed lateral magnification −1/(U−1). Coincidence requires U=2 for a real object. For A08 it occurs at the centre at phases 1/4 and 3/4. The sample at 1/2 is exactly afocal and has no finite conjugate or lateral magnification.

Geometry qualification compares dyadic represented means and amplitudes before recognizing constant, extremal or interior focal and coincidence events. Amplitude zero has a separate all-phases class when the level is exact. Cardinal sample cosine values are exact for the supported phases. Nearby events and samples that lack adequate numerical resolution remain withheld. The A08 CLI ran analytically only and exposes an instantaneous prescribed configuration model, with propagation delay and physical motion outside the result.

## Adversarial and genuine checks

- I independently evaluated 27 motions, 2,754 samples and 32 interior event phases using exact represented input arithmetic and a 64-decimal cosine series. The tested samples included 105 exact afocal, 2,628 qualified finite and 21 withheld. The maximum relative finite conjugate residual was 1.41e−12. Discrete numerical event phases met their target U to within 4.73e−14.
- With mean 1.3 and amplitude 0.3, rounded subtraction appears to give U=1 at the minimum, but their represented difference is strictly greater than one. The event and phase sample correctly withhold exact afocal equality, another requested sample remains available, and whole-request coverage stays partial. Exact extrema, constants and events crossing into a virtual-image interval were checked separately. No detector or native scene is created from the inverse facts.
- The independent local run passed 31 focused tests. Each of the three v6 native control scenes emitted three genuine rays, each with incoming detector, mirror, and returning detector callbacks. The finite line intercepts were within 0.008606 mm axially and 0.0000524 mm transversely. The focal scene's maximum measured transverse slope was 4.845e−7. That scene evaluates the observed slopes without fitting a finite image. Each parameter setting ran separately.
- The 16 A07 and A09 deterministic records remained byte-identical to independent execution on the production tree.

## Hosted verification

All 11 exact-head workflows passed. [Optical composition job](https://github.com/physicsvigilante/opticsim/actions/runs/44872644670/job/136750374615) passed 1,290 Node tests. The exact-head [authoring archive](https://github.com/physicsvigilante/opticsim/actions/runs/44872644670/artifacts/14693724874) matched SHA-256 `0b99dabcca5a42477d08cadfc99f4077b506d07ae239ae3d81e52ae87c9be4c5`. All 23 relevant records matched the independent execution byte for byte, including four A08 analytical files, three A08 native controls, and 16 inherited A07/A09 files.

The release verdict certifies this exact source. The integration commit and post-merge CI are separate checks.
