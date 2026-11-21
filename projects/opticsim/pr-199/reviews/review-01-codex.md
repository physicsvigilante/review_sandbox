# Independent Codex review of Opticsim PR #199

**CLEARED FOR OWNER DECISION.** I found no blocker in the four common-plane power operations, numerical qualification, source-backed examples or native separation.

| Reviewed identity | Value |
| --- | --- |
| Reviewer | Codex, independently assigned by the owner |
| Head | `96d47e8ede54b848fc43db6e1b32bc4e3231e429` |
| Tree | `3d7b07dfc0e238e19451fa99709188a1843be1d9` |
| Base | `d9f03827b6bc91afd5760eea966ec698579a7444` |
| Protocol commit | `ee624882ab607c2a3336e73b95d05ac4f1e31da3` |
| Native pin | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source, model and acceptance

I verified the protocol commit directly precedes the implementation and directly follows the base. The protocol retained blob `a6f7fd67bf2f7a3cd61a0a04fd651419ff39326a` and SHA-256 `420a37d5c9c7166e590174f31922951d9b5ebb7deae25bed4ba64dd98f50cb92`. I independently read the three named Problems images and verified all three frozen image digests. The commit ordering establishes the order of the repository records. [Frozen protocol](https://github.com/physicsvigilante/opticsim/blob/ee624882ab607c2a3336e73b95d05ac4f1e31da3/evaluation/coincident-power-v1/frozen-protocol.json)

| Case | Independently reproduced public result | Scope of interpretation |
| --- | --- | --- |
| A32 | +10 D and +0.10 m equivalent focal length | +5 cm converging and −10 cm diverging focal lengths in thin optical contact. |
| A36 | Approximately +20 to +24 D adjustable eye-lens power, a +4 D change. Fixed outgoing vergence +60 D. | The source gives approximate corneal and minimum eye-lens powers. Co-location, fixed corneal power and fixed retinal conjugate are explicit assumptions. No anatomical retinal distance is inferred. |
| A37 | −0.5 D correction and −2 m virtual output conjugate | The 2 m far point is given. Unit-index air, relaxed eye, distant collimated input and zero vertex distance are explicit idealizations. |

## Reviewer tests

I used an isolated export of the named head, restored the nine changed files from their exact Git blobs, and rebuilt the existing pinned test core. The 52 focused tests in the new power, perpendicular-face, prism-angle, method-suitability and problem-workflow suites all passed.

- **Independent arithmetic.** I evaluated 1,764 public requests using a separate rational oracle that recovered each binary64 input's mantissa and exponent and retained exact reciprocal denominators. The cases covered 144 contact sums, 720 forward conjugates, 720 missing component inversions and 180 fixed-output changes. They included positive and negative distances, collimated input, powers at allowed magnitude limits, zero powers, mixed distance and power representations, and fixed or adjustable components selected by ID. I checked exact afocal results and finite results against the oracle, including 52 exact-zero checks and 16 unresolved near-cancellation checks. The latter counts are field checks. Several fields can come from one request.
- **Numerical policy.** The code applies the near-zero guard to the full sum, then tests the exact rational sum of the represented inputs before issuing zero power or an infinite conjugate. Every admitted binary64 input is an integer multiple of 2⁻⁷² under the documented bounds. Equal and opposite represented distances cancel exactly. A reciprocal rounded to 10 D from the binary64 representation of 0.1 m and a directly supplied −10 D correctly return indeterminate. I also checked that a retinal fixed-output request with a nonpositive outgoing vergence is unavailable, while the generic common-plane calculation preserves signed output.
- **Native scope.** The supplied native test rejected coincident native lenses and reproduced the sampled focus of one +100 mm lens. I added four disposable surrogate controls with independently assigned focal lengths of −250, −125, +80 and +200 mm. Across 32 actual detector callbacks, ray directions extrapolated to the signed focal plane with axial-intercept height error below 10⁻⁷ mm. For diverging lenses the backward extrapolation is an analytical check of measured outgoing direction. The native detector remained downstream. These runs corroborate the single equivalent lens under collimated illumination. A36 and A37 remain reduced analytical models.
- **Public authoring.** I invoked the CLI on all three examples. Each reported conditional method suitability, zero native calls and no portable scene. Each produced original input, plan, analytical results and report. Source interpretation and the explicit reference plane survived into the evidence. Method selection, missing or incompatible conditions and historical prism and perpendicular-face routes were covered by the focused suites.

## Hosted evidence

All eleven exact-head pull-request workflows passed. The optical job log records 1,175 passing Node tests, including the single-lens focus and native contact refusal. I downloaded the authoring evidence archive and verified SHA-256 `1da805cdb69dbdcd7e1c78a4c0abc35905b7e934d355dbe4c499861e7aae8e30`. All twelve A32/A36/A37 files in the archive matched the independently produced CLI files byte for byte. The full-suite count is hosted CI evidence. The focused runs, rational checks and surrogate ray tests above were executed independently. [Optical CI job](https://github.com/physicsvigilante/opticsim/actions/runs/44853453859/job/136689980855) · [Authoring evidence ZIP](https://github.com/physicsvigilante/opticsim/actions/runs/44853453859/artifacts/14686507525)

The decision covers ideal paraxial powers at a common plane. Finite spacing, physical eye anatomy, physiological response and clinical prescribing are outside its scope.
