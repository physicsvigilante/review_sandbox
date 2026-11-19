# EMFEELD PR #58 — narrow independent JEE capacitor V1 review (new context)

**Review target:** https://github.com/physicsvigilante/emfeeld/pull/58 (DRAFT / UNMERGED). **No merge or release authority.** Charter: https://github.com/physicsvigilante/emfeeld/issues/57.

- Exact HEAD `6f073802aa36601c7a78bc1bd320b74f43dbbfd1`; branch tree `841fe1c8b876363a2872ba98655ca9cffc0d5e3b`.
- Qualified original main `51eee59836aac801c989e31712960571ceb94f39`, tree `45fc03e72f6bddf791b65573464af1d059f19015`.
- GitHub synthetic PR merge `afa8b4006d9b6fef21a098dee980b6e42ac68874` (not actual production main). Eleven **only added** files; 428 original tracked source files unchanged. No changes to old Coulomb/gravity/Gauss/conductor/dipole physics, trajectories, PyVista viewer or Three.js.
- Primary source `src/emfeeld/capacitor_lesson.py`; renderer-neutral `capacitor_presentation.py`; actual PyVista `capacitor_view.py`; tests `tests/test_capacitor_lesson.py`, `tests/test_capacitor_presentation.py`, `viewer_tests/test_capacitor_runtime.py`; original source and native evidence in developer's **PR58_Capacitor_Review_Kit.zip**.

## Review what this new science promises—and what it refuses

One ideal, linear, full-gap homogeneous dielectric between parallel conducting plates with **no fringing**. Finite-looking plate meshes are schematic; display gap enlarged 20×. Separately hold **signed free Q** (isolated) or **signed terminal V** (ideal battery). Physics: `C=ε0 κ A/d`, `Q=CV`, `E_z=V/d`, `U=Q V/2`, lower/upper free charges `(+Q,-Q)`, polarization `P_z=ε0(κ−1) E_z`, bound lower/upper `(-P,+P)`. Check changing κ, d, charge sign and zero. Energy stored **not** battery work or mechanical work; no capacitor-network, partial insertion, exact finite plates, charge-transfer dynamics, force or dielectric boundary solver.

Use reviewer-authored independent SI/Gauss-law or Decimal reference cases, not just production test reruns. Verify strict JSON inputs, duplicate/unknown/nonfinite refusal, no silent coercion, no unrepresentable fields, mathematical plate-interface E one-sided, continuous scalar potential, origin/units/provenance. Check actual PyVista slider/key/scene changes, negative polarity plate colours and E arrows, prediction-hide versus actual physical measurements retained in evidentiary reports, no physical recomputation on camera/reveal, and all eight actual hosted screenshot/sample/evidence integrity chains.

## Original author CI evidence (do not count as your own execution)

- **Source workflow 44552107923** SUCCESS; original artifact **14543297469**, SHA-256 `52246ac326a00f3cbee0f3895b790777604f4fe2c4d22af6b4b7307e5199c8ec`. Original TAR SHA-256 `f8ab404f2e59f1986737aa762edd05f803e5d530c7567385fb23b47629b75024`, 439 intact Git source files, reconciled with exact synthetic merge tree.
- **Capacitor 3D workflow 44552107954** SUCCESS; original artifact **14542299072**, SHA-256 `765183d34e4fe502d0a7e846e8eb9718a2abbd30ff90b99b7a782ce03ad56148`. Eight actual native PyVista scenes (including isolated/battery vacuum/dielectric, predict, negative Q, zero and manual adjustment); original ZIP CRC, each scene 7 hash references, physical reports and SI samples verified by builder.
- **Builder local:** 67 focused tests including native PyVista; full 2,047 inherited Python tests PASS with warnings as errors. No global install necessary with packaged source and existing compatible Conda/PyVista environment.
- Other dedicated PyVista/Three.js/Gauss/cavity/dipole PR workflows green; exact-head Linux/Windows clean-install 44552107447 was IN PROGRESS when this handoff was recorded. Reviewer must check its actual final result before concluding acceptance, preserving any failure.

## Disposition

Publish **review-01-chat-b.md** under `projects/emfeeld/pr-58/reviews/` with immutable reviewed source SHA/tree, new reviewer-owned challenge results (or missing execution clearly named), scoped PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE. Distinguish developer CI, reviewer tests, actual native screenshots and human teacher effectiveness. Do **not** merge production PR or edit developer evidence. Keep draft until qualified current-head CI and scoped independent acceptance; later guarded merge and fresh actual-main qualification are separate requirements.
