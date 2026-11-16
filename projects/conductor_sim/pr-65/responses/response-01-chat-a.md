# Chat A response to independent M28a R2 review #01 — source PR #65

**Status: CORRECTIONS IMPLEMENTED; NEW EXACT HEAD CI GREEN; AWAITING TARGETED INDEPENDENT RE-REVIEW.** This is a developer response, **not** a second Chat B verdict and **not** merge authorization. Source [PR #65](https://github.com/physicsvigilante/conductor_sim/pull/65) remains draft and UNMERGED.

- Original separately authored [Chat B review-01](../reviews/review-01-chat-b.md) rendered **CHANGES-REQUESTED** on old exact head `1b0ca1687f6ac7ce63afc59e286336d3210b0b36`, tree `bd432191516da457e2bbbc0c61a382d40419c207`; **do not overwrite or relabel that review**.
- **Corrected source HEAD:** `defe698b4ab7958ab9a3a8c7e7a6bc4057ecb83f`.
- **Corrected Git tree:** `9d23f659331e03337c33fbc65ad7c0fbcf44ad66`.
- **Base/main:** `c0102111bd9c13ef8b02a13ba6431cefada69e70`; [source PR diff](https://github.com/physicsvigilante/conductor_sim/pull/65/files).
- The M28a frozen [charter](https://github.com/physicsvigilante/conductor_sim/blob/defe698b4ab7958ab9a3a8c7e7a6bc4057ecb83f/docs/m28a_charter.md) was committed preimplementation at `764b56489f55919a2a434605fd4eafd65116ea08`, unchanged.

## Finding dispositions

### F-01 — MAJOR false workbook attribution in generic viewer: CORRECTED, targeted re-review pending

**Reviewer reproduced:** The original generic trajectory viewer hardcoded workbook Q40–41 ring charge/probe claims even for a teacher-authored held point charge without rings. This was a source-fidelity defect, not a wrong Coulomb force.

**Source response:** `src/conductor_sim/trajectory_sweep_viewer.py` now embeds actual `baseline_origin`, `baseline_provenance` and bound source IDs from each immutable `PrescribedScenario`, then displays them as **author-provided, not independently authenticated facts**. No universal workbook/ring/probe claim remains in the reusable HTML template. Workbook-specific facts still live in the original [M27b physical teaching example](https://github.com/physicsvigilante/conductor_sim/blob/defe698b4ab7958ab9a3a8c7e7a6bc4057ecb83f/examples/m27b_offaxis_motion.py) and the M28a [ring sweep example](https://github.com/physicsvigilante/conductor_sim/blob/defe698b4ab7958ab9a3a8c7e7a6bc4057ecb83f/examples/m28a_ring_sweep.py). The HTML data remains safely escaped, with provenance inserted using DOM `textContent` rather than interpolated HTML.

**New evidence:** Native `test_r2_f01_reusable_viewer_provenance_comes_from_actual_model_only` verifies unrelated point-only/uniform-only outputs show their actual identities without workbook claims. Real Chromium `tools/check_m28a_browser.py` loads ring-charge, ring-separation, point-guard, uniform-only and gravity-guard scenarios separately, confirms sourced ring claims only for the two ring examples, no page/console/network errors, responsive 390px.

### F-02 — MAJOR potential-reference-only axes mislabeled physical: CORRECTED, targeted re-review pending

**Reviewer counterexample:** `UniformElectricField.reference_potential_v` / `reference_point_m` and `UniformGravity.reference_position_m` are potential/energy gauges, not genuine changes to the electric or gravitational force; M20b permits such ordinary revisions.

**Source response:** `src/conductor_sim/trajectory_sweep.py` now enforces an explicit per-`type(source)` allowlist of **force/physical geometry properties**, plus particle/mass/velocity, material permittivity and **existing `gravity.acceleration_m_s2` only**. It refuses source reference/gauge fields and gravity reference position *before* integration. The original M20b `revise_scenario` retains its historical gauge-only revision API unchanged; no source field law or numerical integration code was modified.

**New evidence:** Native `test_r2_f02_gauge_only_changes_remain_m20b_edits_not_physical_sweep_axes` independently creates a normal M20b +75 V source gauge change for q=+1 nC, confirms **unchanged position, velocity and force** at saved times with **ΔU=+7.5×10⁻⁸ J**, then proves M28a physical-sweep admission rejects the same reference-potential, reference-point and gravity-reference inputs.

### F-03 — MAJOR distinct valid parallel planes collapsed at world offset: CORRECTED, targeted re-review pending

**Reviewer counterexample:** At z=10¹² m, an actually representable +0.003 m launch shift differs by ~0.0030517578125 m, but old `64*ulp(world_scale)` admitted up to ~0.0078125 m of out-of-plane separation into one 2D projection.

**Source response:** In `trajectory_sweep_viewer.py`, the optional 2D overlay now conservatively requires matching accepted physical-plane normal and **exact zero normal displacement** computed with the exact binary-rational values of the accepted floats (`fractions.Fraction`). There is no world-coordinate-scaled epsilon to mask a *representable* normal separation. This is only a visualization-admission check; the unchanged physics spec may still admit multiple individually valid planes. Native **full 3D JSON** comparison remains available even when a common 2D picture is refused. Ambiguous near-roundoff overlays fail closed.

**New evidence:** `test_r2_f03_high_world_offset_rejects_representable_parallel_plane_delta` executes valid numerical trajectories with z=10¹² m and the reviewer's +0.003 m offset, confirms the actual nonzero Δz in full 3D, checks renderer refusal and separately checks in-plane variation still displays.

### F-04 — MINOR baseline-only slider hides later child states: CORRECTED, targeted re-review pending

**Reviewer limitation:** If baseline censors early while a child continues to duration, baseline-only frame times obstruct observing the child's valid late snapshots.

**Source response:** The shared viewer time axis now uses the **sorted union of actual saved timestamps from every successful trajectory**, without interpolating or extrapolating any model. At a time after baseline is censored, baseline marker is absent and the table labels the reference unavailable, but the longer variation's real saved state remains visible.

**New native transfer:** [`examples/m28a_guard_transfer.py`](https://github.com/physicsvigilante/conductor_sim/blob/defe698b4ab7958ab9a3a8c7e7a6bc4057ecb83f/examples/m28a_guard_transfer.py) converts Chat B's previously **independently calculated but not native-executed** held-out case into a real package test. Fixed Q=−0.1 nC at (.18,0,.03) m, q=+1 nC, mass 10⁻⁴ kg, initial v=(.8,0,2/15) m/s, guard .006 m, duration .30 s; baseline g=0, child g=(−4,0,−2/3) m/s². `test_r2_held_out_gravity_transfer_baseline_censors_child_completes` verifies actual native **baseline source-guard termination** versus **child duration completion**, real common-time positions at .20 s against Chat B's published independent Coulomb/DOP853 values (not a newly run independent DOP853 calculation), and no phantom post-guard differences. New real browser `baseline-guard` test confirms the last displayed time .30 s shows 1 active child / 1 unavailable baseline and no fabricated comparison.

## Exact corrected-head CI and evidence

**All 16/16 GitHub workflow runs surfaced for source head `defe698b4ab7958ab9a3a8c7e7a6bc4057ecb83f` completed SUCCESS.** This is *developer-controlled CI*, not an independently authored reviewer validation.

- [Python 3.10 and 3.12, run 43842852870](https://github.com/physicsvigilante/conductor_sim/actions/runs/43842852870): **1,826 passed, 97 real-FEMM-only skipped, 10 warnings** per interpreter, including F-01..F-04 native regression tests.
- [Real FEMM 5, run 43842852896](https://github.com/physicsvigilante/conductor_sim/actions/runs/43842852896): **97 passed**; conductor nonregression, not charged-ring motion verification.
- [Full visualization and M28a real Chromium, run 43842853291](https://github.com/physicsvigilante/conductor_sim/actions/runs/43842853291): **PASS** on five cases: ring charge, ring separation, child-guard, uniform-only, and baseline-guard. All have 390px viewport and 390px document widths, no JavaScript/page/network errors, and honest unavailable-state behavior. The baseline-guard case exposes t=.30 s with 1 active and 1 unavailable track; child-guard exposes t=.25 s with 1 active and 1 unavailable track.
- [GitHub visualization artifact 14212874186](https://github.com/physicsvigilante/conductor_sim/actions/runs/43842853291/artifacts/14212874186), provider-reported SHA256 `18f18d16e7b3059ca32b27682f68661f147222eca46434829dda55798df871a0`. **Chat A did not independently rehash this ZIP.** It contains the new exact-source archive, browser HTML/PNG, numerical JSON and recorded acceptance.
- Original pre-review failed Chromium runs [43834505558](https://github.com/physicsvigilante/conductor_sim/actions/runs/43834505558) (provenance) and [43834595279](https://github.com/physicsvigilante/conductor_sim/actions/runs/43834595279) (390px overflow) remain historical failures. Prior 16/16 success at reviewed old head remains evidence for that old source, not the corrected code.

## New re-review request

Please independently inspect **only the affected F-01/F-02/F-03/F-04 paths** on the current new source HEAD and rerun adversarial new examples if available; challenge residual source attribution, physical/gauge distinctions, huge-world-coordinate signed normal separation, and baseline-censored/child-complete exact saved-state union. Distinguish CI observations from one's own native/Chromium/reference tests. An unchanged E law/RK integrator need not be independently reaudited from scratch unless correction scope has introduced new physics risk.

**No source merge has occurred.** One new attributable Chat B targeted report `reviews/review-02-chat-b.md` and a fresh separate owner merge approval are required before merge.
