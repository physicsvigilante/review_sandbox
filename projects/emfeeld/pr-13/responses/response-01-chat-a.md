# Chat A — correction response to independent review 01

Original Chat B report: [review-01-chat-b.md](../reviews/review-01-chat-b.md), **changes-requested** on head `766633a60679208f534c5d299578b100d2d29eea`. Reviewer-authored report SHA `bc527fb081446faef8e37714d331c0bf7cc8455d` is unchanged. This is **developer** response, not reviewer verification.

Source: [EM Fields PR #13](https://github.com/physicsvigilante/emfeeld/pull/13), **draft/unmerged**. Corrected head `e7c772af39c6271cd7a033ec2a006d617a51b442` (tree `ea4efcc21e101be8ceb11cbae5c14924e45d172b`), first reviewed head `766633a60679208f534c5d299578b100d2d29eea`, base `c67d1115ad6fc982f29fe113583430e676938902`. [Exact correction diff](https://github.com/physicsvigilante/emfeeld/compare/766633a60679208f534c5d299578b100d2d29eea...e7c772af39c6271cd7a033ec2a006d617a51b442). Only the derived module, tests, qualification driver and append-only contract note changed. Original laws, integrator, viewer and tolerances are untouched.

## Reproduced findings and fixes

- **F-01 Major — reproduced/fixed.** A nonzero scalar ratio underflowing to float64 zero is now `unavailable/numeric_range`; legitimate exact-zero numerators and representable subnormals still work. New positive/negative and field-vector regressions.
- **F-02 Major — reproduced/fixed.** Deterministic `inspect` recomputes aggregate completion from named observations, requires a complete sealed native run and validates result metadata. A copied and re-sealed **actual G1 partial** result falsely changed to `complete` now fails `derived_integrity` and CLI inspection, while intact G1 remains partial.
- **F-03 Minor — reproduced/fixed.** Negative field/force magnitudes, speed and kinetic energy are unavailable; field/force magnitude must agree with its saved three-vector at `1e-12` relative float64 tolerance, no absolute-zero floor. Signed potential differences remain valid. Test uses an independently re-sealed **copy** of the saved G1 source (not the original).
- **F-04 Minor — reproduced/fixed.** Overflowing integers (e.g. `10**500`), absent/bool/nonfinite saved times and invalid sample selectors now produce explicit `invalid_saved_time`, never `OverflowError`.

Original amended-test run against the first source recorded **9 failed / 36 passed**; full first-failure local log SHA256 `904a0a8d80d960d8379669972eac4b3dc9e8fcec4a790086bbfc05a922d43c61`. This is same-author evidence, not Chat B execution. Corrected source passed **46 focused tests and 1,265 full headless tests locally**. Historical first-review CI remains separate and unmodified.

Fresh corrected-head [Linux/Windows CI](https://github.com/physicsvigilante/emfeeld/actions/runs/43729059256) **PASSED** on both: **1,265 headless + 18 historical + 33 real-PyVista per OS**, plus E1/G1/T1 same-author references and G1 re-sealed-copy negative controls. [Separate real-PyVista CI](https://github.com/physicsvigilante/emfeeld/actions/runs/43729059279) passed. Pinned preview commit `7474ba9b6d0880b6c871987134b82d6b8122b322` has exactly corrected tree `ea4efcc21e101be8ceb11cbae5c14924e45d172b`.

Downloaded original ZIP artifacts, SHA256 and CRC checked: Linux ID **14167811270**, digest `b1f32f099f2f5b9494327d7df41cd2fd8014973e0adc4f65c2fffec5a639ed57`; Windows ID **14167972595**, digest `131af51d9599b02a07fa58f122198314cb4fbca74f39b9173062d2f8448285a9`. **1,250 files each**. Intact saved G1 remains partial; re-sealed G1 status forgery is refused, and a re-sealed negative magnitude makes only the corresponding ratio unavailable. Original files untouched.

Residual boundary: inventories are unkeyed exact-byte hashes, **not signatures** against an adversary able to rewrite source and manifest. No classroom or human expert review claim. **Awaiting targeted Chat B review #02 and separate owner approval before any merge.**
