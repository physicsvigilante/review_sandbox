# Independent Codex review of Opticsim PR #206

**CLEARED FOR OWNER DECISION.** I found no outstanding blocker for the conditional paraxial coordinates, native corroboration, or authoring dispatch.

| Identity | Reviewed value |
| --- | --- |
| Reviewer | Codex, independently assigned by the owner |
| Head | `a85e34c3eb10fbbfee64d34db3982325ec4c374d` |
| Tree | `3626e6ac05d51a0c1659a870a57ee24d747012e1` |
| Base | `5e53cd6be055b8fd89ac3f6656b6210d60aa940b` |
| Protocol commit | `853f6dfede781403aec63de27bde47a3a8bf7ee3` |
| First native control commit | `5086a27204ab99370ceb266738e501eed9d91c32` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

## A35 and coordinate interpretation

I read the original A35 Problems PNG and verified its SHA-256 `85c88a0d9215a19d8207d812963dcbb56b0daa207621267f46b23fd493076b47`. It gives two equal converging lenses, separation 3f, and a small upward shift d of the rear lens. The indicated origin is the first lens centre, positive x is to the right and positive y is up. Absolute f, d and aperture dimensions are absent. The public CLI returned **x = 5f, y = 2d**, or a distance 2f downstream of lens two, conditional on transmission through both lenses. It retained the input bytes, the two scale factors and the distinction between conditional mathematics and native measurement. The frozen protocol retained blob `1c462f7ee9fffbe17625750c0c90f5cd8eca0795` and preceded the native controls and production query. [Frozen study](https://github.com/physicsvigilante/opticsim/blob/853f6dfede781403aec63de27bde47a3a8bf7ee3/evaluation/offset-lens-parallel-focus-v1/frozen.json)

## Independent physics and numerical checks

I rebuilt the pinned native test core and ran 45 focused tests in an isolated export. For an independent calculation, I recovered each input's exact rational value from its binary64 bits. I propagated two incoming parallel rays at independent heights, applied each lens about its own axis, and intersected the resulting lines without intermediate floating-point rounding.

- Across 1,122 in-scope parameter pairs, 1,078 qualified and 44 near-degenerate cases withheld the numerical value. All 1,078 qualified results agreed with the rational oracle, including 540 downstream, 473 upstream, 19 afocal and 46 second-lens-plane results. The largest normalized numerical error across reported finite coordinates and coefficients was 5.02 × 10⁻¹⁴, rounded up.
- With k = gap/f₁ and q = f₂/f₁, exact k = 1 + q yields a collimated output with common slope (d/f₁)/q. At k = 1 all participating rays meet at the rear lens plane on the front axis, giving zero back distance and transverse coefficient. Exact q = k(k−1) gives x = 0, the first lens plane. The latter is an upstream extrapolation relative to the rear lens. Fifteen independently tested representations landed exactly in this first plane. I tested perturbations on both sides of each cancellation, excessive extrapolation and out-of-domain ratios.
- The A35 native v20 baseline used f₁ = 200 mm, d = 2 mm and eight rays, with two detector sections corroborating concurrence at (1000, 4) mm. I reran its original aperture-miss checks along with the new virtual, collimated and rear-plane tests. The added controls observe actual per-object lens calls and retain the encounter order L1 then L2. Each uses two downstream sections with eight observed directions. An upstream point is inferred by backward extrapolation.
- In a separate native grid I checked 192 detector readings over twelve settings, including both signs of offset and two distinct exact first-plane examples. All finite-focus residuals were below 10⁻⁶ mm and collimated slopes agreed within 10⁻⁹. These tests establish the stated conditional line geometry for sampled rays. They do not measure an image or imply a common focus for a bundle that bypasses either lens.
- The A35 analytical CLI produced its report with zero native calls and no portable scene. A mixed request using valid v20 native facts continued running and marked only the inapplicable analytical query unavailable. All 45 previous public problem plans matched the base-equivalent #205 export.

## Hosted verification

All eleven exact-head pull-request workflows passed. The optical job logged 1,217 passing Node tests, including the existing v20 numerical baseline and the three new native controls. I checked the authoring archive SHA-256 `6dc07cc61406d0e999f4529d2c7ef5ca83052d8ed0ccfcd39a6cb7dcc0a385e1`. Its four A35 public files and three native witness records matched the independent runs byte for byte. The full-suite count is hosted evidence. The focused tests, source inspection, rational calculation, additional native controls and artifact comparison were independently performed. [Optical CI job](https://github.com/physicsvigilante/opticsim/actions/runs/44860566573/job/136712744403) · [Authoring evidence ZIP](https://github.com/physicsvigilante/opticsim/actions/runs/44860566573/artifacts/14689297951)
