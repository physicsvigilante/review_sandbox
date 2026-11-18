# Opticsim PR #140 — B1b numerical stress feasibility (not product geometry)

**2026-11-18: PREREGISTERED TEST-ONLY NATIVE EXPERIMENT; BUILDER CI STARTED, INDEPENDENT REVIEW PENDING.**

[Draft PR #140](https://github.com/physicsvigilante/opticsim/pull/140) is **one new test file only**, atop actual production main, not held B1a #138 or prior research #135. [Issue #139](https://github.com/physicsvigilante/opticsim/issues/139) was opened **before** new native execution and freezes the physical input matrix, Snell conditional reference, numerical-alarm tolerances and intended negative controls.

| Identity | Expected source |
| --- | --- |
| Authored HEAD | `713dfcf083baed4743e3c94cca703bf58c9a49d9` |
| Authored Git tree | `a2308fe2c5baf7570b8d692c8595084eae001e37` |
| Synthetic PR merge | `122c7787dce613e063d4cef40a167adf2b9a05e4` |
| Synthetic merge tree | `a2308fe2c5baf7570b8d692c8595084eae001e37`, identical |
| Production main | `d3509e82fb65d81aabe336666851f8f2962623f4`, unprotected |
| Diff vs main | One new `test/jee-b1b-native-numerical-stress.test.mjs`, 798 inserted lines; zero `src/`/native/schema/CLI/UI/workflow changes |
| Reused independent research test fixture | Previously independently reviewed #135 native harness, exact blob `1a57c562bdf8eb00ebbc5e21569cc2cd179f9876`, itself unmerged |

**Scientific scope:** Actual existing pinned-native PhyDemo SingleRay/one PlaneGlass/short finite detector measurements across preregistered indices, source/receiver depths, widths, normals, units, large translations and negative TIR/miss/incomplete cases. The new **plane-centred 2D line intersection** and perturbation comparisons are *test-only post-native derived geometry*, not a propagated ray or a public observer/image. Engineering matrix alarms **0.02mm** normal / **0.1mm** long-range compare with an independent **conditional symmetric-pair** Snell construction; they **do not** bound the upstream native error. Hypothetical ±1e-4mm detector-point and ±1e-6rad direction changes are **not measured native errors or confidence intervals**. Research near-parallel and endpoint thresholds are noncertifying.

**No B1b released feature exists.** Reviewed source #138 B1a remains held/draft/unmerged and **public geometry is always null/withheld**. Test-only #140 cannot establish an eye, pupil, real optical image, simultaneous ray bundle or continuous power. Any future numerical admission/public B1b contract requires *separate independent review* and a genuine native-error/conditioning validity domain, or must remain withheld.

[**Copy-ready independent Chat B review prompt**](REVIEWER-PROMPT-01.md) · [**Full preregistered source/CI research review request**](REQUEST.md) · [**Preregistration #139**](https://github.com/physicsvigilante/opticsim/issues/139).

**CI and independent physics review currently PENDING** — do not claim the matrix passed before inspecting exact-source actual native logs. No merges, owner release, B1b accuracy/eye/image claim or change to main protection #123.


## Log-identity hygiene revision — 18 November 2026

The original one-file research source `4742462e17db672d02e25dcf9e38ea0ff3cb54ad` passed the first **807/807** native Node24 suite, including all positive index/width and orientation cases, but an inherited log helper allowed the trial's case `label` to override the structural `B1B_TEST_ONLY_STRESS`/NEGATIVE/SENSITIVITY event name. The corrected **exact review target** `713dfcf083baed4743e3c94cca703bf58c9a49d9` uses separate `caseLabel` while preserving numeric physics/test assertions and the one-file-only scope. It has the authored/tested synthetic Git tree `a2308fe2c5baf7570b8d692c8595084eae001e37` with merge `122c7787dce613e063d4cef40a167adf2b9a05e4`. **New exact-head 11/11 CI and independent review pending.** Original source/CI preserved for audit.
