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


## First final-source native evidence and numerical meaning (2026-11-18)

[**Actual pinned-native Node24 run #44265168150**](https://github.com/physicsvigilante/opticsim/actions/runs/44265168150) executed the exact corrected test-only HEAD `713dfcf083baed4743e3c94cca703bf58c9a49d9`, with **807/807 tests PASS** in the first completed workflow. Structured log records exactly **19 positive B1B_TEST_ONLY_STRESS cases, six B1B_TEST_ONLY_NEGATIVE cases and two B1B_TEST_ONLY_SENSITIVITY probes** with their own caseLabel keys. The 19 positive cases all met **preregistered engineering test alarms**, not calibrated precision limits. The negative cases recorded genuine finite-width misses, TIR/near-critical misses or near-parallel numerical withholding without a fabricated intersection.

**Stress contrast that matters:** baseline ±0.5°/120/40mm yielded ~0.00152917 mm test-local 2-ray intersection displacement under **assumed** ±0.0001 mm point / ±0.000001 rad direction perturbations. The 1000/500mm ±0.05° geometry gave ~**0.815497 mm** under the same artificial perturbations (over 500× more sensitive). High-contrast **1→4** required measured backward extension/`L`≈**3.25** despite the preregistered conditional Snell geometry differing by only ~2.9e−12 mm in that single constructed fixture. Neither number is a native uncertainty bound or a reason to release arbitrary numerical intersections. Maximum observed transform-vs-reference difference among the 19 samples was on order **1.65e−7 mm**, also a fixture-specific diagnostic only.

The final HEAD's **full 11-workflow CI and independent Chat B numerical/physics review remain pending** at this update. The study is **TEST-ONLY**, all B1b intersection coordinates remain absent from public B1a and there is no physical observer/eye/image claim.


## FINAL exact-source native and browser regression CI complete — 18 November 2026

**11/11 standard GitHub Actions workflows completed SUCCESS** at authored HEAD **`713dfcf083baed4743e3c94cca703bf58c9a49d9`**; source Git tree `a2308fe2c5baf7570b8d692c8595084eae001e37` identical to the tested synthetic merge `122c7787dce613e063d4cef40a167adf2b9a05e4`, first parent production main `d3509e82fb65d81aabe336666851f8f2962623f4`. Only one new test file (798 lines), all production source/CLI/PhyDemo pin, saved schemas and browser untouched.

[**Raw full native test output #44265168150**](https://github.com/physicsvigilante/opticsim/actions/runs/44265168150) and [**planar/native #44265168184**](https://github.com/physicsvigilante/opticsim/actions/runs/44265168184) both passed **807/807 Node v24.19.0 tests**, pinned PhyDemo **`811f508d2b070898c241a568b0c167dcb8645251`**. The final log includes **19 positive**, **6 negative/refused** and **2 post-native hypothetical sensitivity** diagnostics, distinguished by stable `B1B_TEST_ONLY_*` event types and `caseLabel`. [**Optical composition/Chrome #44265167963**](https://github.com/physicsvigilante/opticsim/actions/runs/44265167963) passed all existing native, real Chrome browser acceptance and hosted-path checks. This is unchanged UI compatibility, **NOT** B1b implementation or independent native replay.

**Numerical research insight:** the shallow/long ±0.05° /1000/500mm pair had a **~0.815497mm** change in its test-local derived intersection under chosen hypothetical input perturbations, while the standard ±0.5° /120/40mm pair changed ~**0.00152917mm** for the same assumed perturbations. A 1→4 high contrast positive case has extension/scene scale ~3.25 and conditional Snell match; it is not evidence of a calibrated error threshold. All **19** positive cases passed preregistered conditional/reference engineering alarms, six negative cases withheld points. This is **not** a proven native uncertainty distribution, quantitative image accuracy or a release domain. Public B1a geometry remains null/withheld and no physical eye/pupil/unique image claim exists.

[**Copy-ready Chat B independent review prompt**](REVIEWER-PROMPT-01.md) · [**Full preregistered source and final CI review request**](REQUEST.md). **Independent exact-source B1b research review PENDING**. Original preregistration #139 and initial-source CI are preserved; no PR merged, main unprotected under #123.
