# conductor_sim PR #65 — M28a independent R2 trajectory-sweep review request

**Status: AWAITING A SEPARATE CHAT B REVIEW. Source PR #65 is DRAFT and UNMERGED.** This request is authored by Chat A and is not a reviewer verdict. Owner approved beginning M28, **not** merging this source PR.

| Pin | Exact value |
| --- | --- |
| projectId | `conductor_sim` |
| sourceRepo | [physicsvigilante/conductor_sim](https://github.com/physicsvigilante/conductor_sim) |
| Source PR | [draft #65](https://github.com/physicsvigilante/conductor_sim/pull/65) |
| baseSha | `c0102111bd9c13ef8b02a13ba6431cefada69e70` (verified fully-green M27b F-01 merge) |
| **exact reviewed headSha** | **`730c239bc174092058a66fcf373da14f54aad663`** |
| **source Git tree** | **`24a3c1111210f4f10719cf872d38d27bcc8d4371`** |
| frozen charter commit | `764b56489f55919a2a434605fd4eafd65116ea08`, before implementation |
| riskClass | **R2** — new physically meaningful trajectory-comparison, censoring, and provenance evidence semantics; no new field law |
| reportDestination | `projects/conductor_sim/pr-65/reviews/review-01-chat-b.md` (only Chat B authors) |

Read [central protocol](../../../PROTOCOL.md), [risk policy](../../../REVIEW-RISK-POLICY.md), [report template](../../../REVIEW-TEMPLATE.md), source [M28a charter](https://github.com/physicsvigilante/conductor_sim/blob/730c239bc174092058a66fcf373da14f54aad663/docs/m28a_charter.md), [M28a API/design](https://github.com/physicsvigilante/conductor_sim/blob/730c239bc174092058a66fcf373da14f54aad663/docs/m28a.md), [composability contract](https://github.com/physicsvigilante/conductor_sim/blob/730c239bc174092058a66fcf373da14f54aad663/docs/composability_contract.md) and [evaluation contract](https://github.com/physicsvigilante/conductor_sim/blob/730c239bc174092058a66fcf373da14f54aad663/docs/evaluation_contract.md). Independently check whether source `AGENTS.md` exists.

## Changed capability and source audit

The existing M20b `PrescribedScenario`/`revise_scenario` API already admits typed revisions of individually identified fixed sources, particle mass/charge/position/velocity and existing medium/gravity parameters. M27b already integrated genuine planar curved off-axis charged-ring dynamics using a qualified physical plane, actual full-3D ring E/V and the historical adaptive RK controller; it was independently reviewed and merged. **M28a adds no new Coulomb formula, force law, model-admission epsilon, RK code, contact physics or source geometry.**

New files:
- `src/conductor_sim/trajectory_sweep.py`: `SweepAxis`, `TrajectorySweepPlan`, `run_trajectory_sweep`, immutable `TrajectorySweepRun`/entries and detached JSON audit. One physical parameter/axis, 1..6 distinct scalar or full 3-vector values. Every child is built **from the same unchanged parent** using the exact existing `revise_scenario`; each is newly integrated using unchanged `integrate_test_charge`.
- `src/conductor_sim/trajectory_sweep_viewer.py`: world-plane particle-trajectory-only plot (not ring apparatus), shared clock selecting **exact saved native timestamps**; rejected/guard-censored variants visibly absent at times without solved data. No browser-side ODE or invented force.
- `tests/test_m28a_trajectory_sweep.py`: source-ID charge, full ring-centre geometry, mass and launch sweeps; independent constant-acceleration analytic reference; novel rigid 90° rotation of a held-point + uniform-field arrangement; refusal, singular guard censoring, no postguard comparison, JSON detachment/HTML safety.
- `examples/m28a_ring_sweep.py`: four teacher-authored controlled studies of existing workbook geometry.
- `tools/check_m28a_browser.py`, visualization workflow: real Chromium with native charge, separation and guard-censor cases, saved-time play/slider, source identities, no network/JS errors and 390px acceptance. Public exports, docs, README are added.

**Workbook attribution:** Physical PDF p12 Q40–41 gives ring A +10 µC, ring B -20 µC, each radius .30 m, separation .40 m, upward 100 kV/m field, and test-particle **charge +10 µC**. The free-motion particle mass .01 kg, changed x=.20 m and v_x=.1 m/s launch, duration .015 s, and all M28 sweep variants are **teacher hypotheses**. Do not claim exact original symbolic-mass/rest/axial Q41 simulation or the visual overlay to be a full ring apparatus drawing.

**Physics semantics reviewers should challenge:**
1. Finite typed axis, stable-ID addressing, no numerical controls in a sweep, rejection of duplicates/non-finite/bool, source-index substitution and value shape mismatches; baseline identity and immutability, true per-sibling lineage.
2. Whole-model requalification; a model may be physically rejected, numerically fail, fully complete or be **source-guard censored**. These are distinct outcomes, never silently omitted; no guard crossing or postguard state invented.
3. Variations and baseline use only identical saved physical timestamps for component and Euclidean `Δr`, `Δv`. Exact float matching intentionally refuses unsupported interpolation; a terminal extra saved guard sample need not align with the baseline. Energy across different scenarios should not be called work, and source charges are not dynamically updated during playback.
4. Renderer projects positions through the same certified plane (basis signed in JSON), shows full solved paths but only current native saved-state markers; when a censored variant has no sample at selected time, no marker is shown. It is explicitly **trajectory space**, not ring source geometry.
5. `as_dict()` detached, finite and versioned; revision SHA-256 is **not authentication or independent correctness proof**. The viewer requires native `TrajectorySweepRun`, not an arbitrary untrusted JSON schema.

## Exact-head CI and original failures

**All 16/16 workflow runs returned for final head completed SUCCESS.** [Python 3.10/3.12](https://github.com/physicsvigilante/conductor_sim/actions/runs/43835150378): **1,820 passed, 97 real FEMM-only skipped and 10 warnings per interpreter**. The [real FEMM5 workflow](https://github.com/physicsvigilante/conductor_sim/actions/runs/43835151218) independently executed **97 passed** (conductor nonregression, **not** full-ring ODE verification). The [full visualization and M28a real Chromium run](https://github.com/physicsvigilante/conductor_sim/actions/runs/43835150525) PASSED, including historical M5–M27a browser checks. A separate [push Python run](https://github.com/physicsvigilante/conductor_sim/actions/runs/43835140516) also passed.

**M28a browser evidence at exact final head:** Charge and separation variants each 3 active curves at t=.015s, 16 real saved baseline states, stable source IDs `ring:A`, `ring:B`, `field:up`. New guard example has 26 baseline states to .25s but only 1 of 2 tracks has a solved state at that last time; the second is explicitly unavailable after `source-guard`. In each case 390px document width=390, SVG=348, no page/console/network errors. Downloadable [visualization artifact 14210786886](https://github.com/physicsvigilante/conductor_sim/actions/runs/43835150525/artifacts/14210786886), **GitHub-reported** SHA256 `efe984aa96563f42f76198030346a51edbf0b2d64829e36b41c3a6ef3e381f4b` — Chat A did **not independently rehash** this ZIP.

Preserve the original first candidate failures rather than rewriting history:
- [run 43834505558](https://github.com/physicsvigilante/conductor_sim/actions/runs/43834505558): new Chromium check failed because first viewer text lacked explicit `source-given` wording; the Python source-given probe q was correct.
- [run 43834595279](https://github.com/physicsvigilante/conductor_sim/actions/runs/43834595279): first mobile view had 480px document width at requested 390px due long unbroken provenance/ID text; corrected CSS wrapping without weakening `<=390` requirement.
- Original native Python 3.10/3.12 passed before these presentation corrections. The last candidate added rigid-rotation acceptance, still without changing any physical law or solver.

## Proposed independent new adversarial checks

Author **at least one unexposed physical layout**, not merely rerun our workbook/ring/rotation cards: e.g. a qualified differently oriented ring + external point field, an unfamiliar point/shell + gravity, or a uniform-field system with an independently calculated kinematics reference. Sweep one stable-identity source/physical launch, verify numerical trajectories and baseline no-mutation. Independently derive or execute a separate direct Coulomb/simple analytical/alternate ODE reference as applicable; do not mistake two uses of the same RK integrator for independent physics verification.

Deliberately attempt to cause a *baseline* source guard while one variation lasts longer, or a variation guard at a non-grid time, and challenge exact-time comparison and viewer non-extrapolation. Challenge a changed ring centre/axis that invalidates the common motion plane, unapproved numerical property, typed shape/duplicate/bool, misleading energy-work comparison, identity spoofing, HTML input escaping and mobile overflow. Check model/source provenance against the actual original page if accessible, distinguishing direct page inspection from trusting the implementer's summary.

State what you observed in pinned GitHub CI versus executed yourself. If unable to inspect/browser/rehash artifacts, do not pretend to have done so. Report **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE** with exact reviewed head/tree, findings and limitations. **No production source changes or merge by Chat B; explicit owner merge approval is still required.**
