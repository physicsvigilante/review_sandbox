# Independent Chat B R2 review — conductor_sim PR #65 (M28a)

**Verdict: CHANGES-REQUESTED.** Reviewer: fresh ChatGPT conversation, GPT-6; 2026-11-16. Risk: R2. Source PR [#65](https://github.com/physicsvigilante/conductor_sim/pull/65) was draft, open and unmerged; no source edits, approvals, comments or merge by reviewer.

- **Exact HEAD:** `1b0ca1687f6ac7ce63afc59e286336d3210b0b36` (verified live twice).
- **Exact Git tree:** `bd432191516da457e2bbbc0c61a382d40419c207` (verified from GitHub commit object).
- **Base:** `c0102111bd9c13ef8b02a13ba6431cefada69e70`.
- Reviewed central protocol/risk/template and request, frozen charter, M28a design, evaluation/composability contracts, source implementation/tests, pinned CI logs and downloadable binary artifact. Root `AGENTS.md` was absent.

## Findings

**F-01 — MAJOR, demonstrated source-fidelity defect — false workbook attribution.** `src/conductor_sim/trajectory_sweep_viewer.py:176-179` unconditionally asserts ring-workbook Q40–41 source facts and source-given probe q=+10 µC in every generated page. The actual archived `m28a/guard.html` is a **teacher-hypothetical fixed point-source system**, with `source_ids=["point:held"]` and no ring; yet the workbook attribution appears in its browser-visible model-lineage section. Independently verified by examining archived HTML and replaying in local Chromium. **Fix:** move workbook claims to workbook-specific example; in reusable viewer display actual baseline `origin`, `provenance` and source IDs (author assertions must be identified as such). Add point-only/uniform-only browser regressions.

**F-02 — MAJOR, high-confidence code/physics counterexample — gauge-only variations mislabeled physical.** `trajectory_sweep.py:37-58,94-109` and `scenarios.py:178-184` admit every built-in source dataclass field, including `UniformElectricField.reference_potential_v` and `reference_point_m`, and `gravity.reference_position_m`. These adjust potential reference, not physical force/trajectory. For `E=(40,0,0) V/m`, changing `reference_potential_v` by +75 V leaves `F=qE` and all position/velocity samples unchanged, but shifts `qV` by +7.5e-8 J for `q=+1 nC`. Yet output describes a physical-parameter sweep. **Fix:** reject gauge/reference axes in this physical interface or explicitly type/label separate gauge-only comparisons while retaining M20b's general revision API. Test unchanged dynamics and energy-reference difference. Exact new native gauge case not executed here.

**F-03 — MAJOR, high-confidence numerical projection counterexample — different parallel planes can still overlap.** `trajectory_sweep_viewer.py:60-74` refuses parallel-plane separation only if `separation > max(1e-12,64*ulp(world_scale))`. At z = 1e12 m, launch z shifts by 0.003 m, represented as **0.0030517578125 m** physical separation (~25 ULP), but the cutoff is **0.0078125 m**, and thus refusal fails. For two individually valid uniform-field in-plane launches, projection into u/v hides an actual 3.05 mm z difference even though full-3D initial delta detects it. Reproduced predicate arithmetic independently, not a native renderer invocation. **Fix:** use a genuine certified plane-identity/equivalence criterion rather than a blanket 64-ULP scale threshold. Test high-offset parallel-plane refusal, ordinary in-plane acceptance, continued full-3D JSON comparison.

**F-04 — MINOR, presentation limitation.** `trajectory_sweep_viewer.py:121` makes slider times baseline-only. If baseline censors earlier but child completes, valid later child states are drawn in the line yet cannot be selected by slider/readout. This is *not* data extrapolation. Prefer union of actual saved timestamps with honest unavailable cases, or explicitly label baseline-only clock.

## Independent evidence and actual tests

**Verified exact-head CI, not rerun locally:** [Python run 43836411513](https://github.com/physicsvigilante/conductor_sim/actions/runs/43836411513) successfully ran **1,821 passed, 97 skipped, 10 warnings** per Python 3.10 and 3.12; [real FEMM run 43836411499](https://github.com/physicsvigilante/conductor_sim/actions/runs/43836411499) reported **97 passed**; [visualization run 43836411518](https://github.com/physicsvigilante/conductor_sim/actions/runs/43836411518) passed. These are three independently inspected workflow runs, not an independent count of all 16 claimed workflows. Retain historical failed Chromium runs [43834505558](https://github.com/physicsvigilante/conductor_sim/actions/runs/43834505558) and [43834595279](https://github.com/physicsvigilante/conductor_sim/actions/runs/43834595279), not mistaken for current-head failures.

**Artifact integrity:** Downloaded actual 50 MB [visualization artifact 14210733766](https://github.com/physicsvigilante/conductor_sim/actions/runs/43836411518/artifacts/14210733766) and **independently SHA256-hashed ZIP**: `cfe8592eefbbccf28b97e7b592c6ce078ebf525de1d765dd0475c1f570394a30` (matches reported). Parsed actual charge, separation and guard HTML/JSON. Guard: 26 baseline samples to .25 s, 21 guarded variation samples to .19489773173431751 s; only 20 literal shared sample times to .19 s, no postguard invented delta. Charge/separation: each 3 complete tracks, 16 saved baseline times to .015 s.

**Independent local Chromium replay:** Opened all three downloaded, already-generated HTML files with Playwright `set_content`, 390px viewport; checked source IDs, active/unavailable markers at selected exact times, absence of interpolated comparison, no errors, no external requests and document width exactly 390. **Passed**, while also reproducing F-01. The *first attempt*, using `file://` navigation, was blocked by environment policy (`ERR_BLOCKED_BY_ADMINISTRATOR`); switching to `set_content` of the **same archived HTML** succeeded. This was not a new native renderer build.

**Independent physics calculation against real archived native samples:** Implemented direct Coulomb `a=kqQ(r-r_s)/(m|r-r_s|³)` with SciPy DOP853, not the project field/RK. Actual guard example: held Q=-1e-10 C at (.2,0,0) m, probe +1e-9 C, mass 1e-4 kg, v_x=0 or 1 m/s, radius guard .005 m. Compared **all 47 native saved states** with an independent integrator at literally matching times. Max baseline position/velocity disagreement: **9.32e-21 m / 6.10e-20 m/s**. Max guarded variation disagreement: **3.61e-10 m / 6.22e-8 m/s**. Independent exact-guard crossing t=.194975628585 s; native conservatively stops earlier at .194897731734 s, with distance .00507803228 m > .005 m. All 20 archived delta components and norm values matched direct recomputation.

**Preserved reviewer first failure:** Initial independent check erroneously demanded native terminal time within 1 µs of mathematical source-guard crossing, and failed. Revised only **the reference expectation**, not source code: a conservative preguard stop is lawful. The native result remains censored, never falsely extended.

**New held-out teacher-authored physical system (independent reference executed, native path NOT executed):** negative fixed point Q=-1e-10 C at (.18,0,.03) m, probe +1 nC at origin, m=1e-4 kg, initial v=(.8,0,2/15) m/s, plane normal y, duration .30 s, .02 s saved grid, guard .006 m. Sweep **existing gravity.acceleration_m_s2** from (0,0,0) to (-4,0,-2/3) m/s². Direct Coulomb + gravity with independent DOP853: baseline reaches ideal source guard at **.217560852346 s** and variation completes at **.30 s**. At .20 s, positions baseline (0.160017636988,0,0.026669606165) m versus variation (0.080009584389,0,0.013334930732) m; difference (-0.080008052598,0,-0.013334675433) m. Reference remains in xz plane. Reproduce as native after correction, checking actual baseline censoring and variation-only late states. No checkout was possible in local runtime (GitHub hostname unavailable), so **no independent new native conductor_sim run** was performed.

**Source-code checks:** M28a calls unchanged `revise_scenario` and `integrate_test_charge` for each child from same parent, distinguishes accepted/rejected/integration-failed, aligns literal saved timestamps, keeps detached finite JSON and avoids browser ODE/interpolation. No unexpected newly added field law/RK found. Source textbook p12 was **not independently inspected**, so claimed workbook constants remain author assertions, not reviewer-authenticated page transcription.

## Separate judgments

| Dimension | Judgment |
| --- | --- |
| Source interpretation fidelity | **FAIL** — F-01 proven false attribution |
| Physics/numerical correctness | **PASS for independently checked archived point-guard samples**; broader native transfer unverified |
| Native simulation and observable coverage | **PARTIAL** — correct archived guard and deltas; missing new native held-out test, F-04 |
| Evidence integrity/provenance | **PARTIAL/FAIL on presentation** — artifact SHA proven, archived samples sound; F-01 and F-02 |
| Teacher-facing usefulness | **CHANGES NEEDED** — correct 390px UI but false attribution and potential plane collapse |
| Textbook answer completeness | **NOT ATTEMPTED**, appropriately optional |

## Release advice

**Keep draft, do not merge.** Resolve **F-01, F-02 and F-03** with focused regressions; F-04 is optional. Rerun appropriate full current-head Python/FEMM/Chromium CI, execute held-out baseline-censored/variation-complete gravity case, and obtain targeted independent re-review against the **new head**. Review status does **not** constitute the owner's separate merge approval.