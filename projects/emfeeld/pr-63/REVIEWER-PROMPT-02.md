# EMFEELD PR #63 — narrow independent R2 scientific + native PyVista review

**Prepared handoff, NOT an independent PASS or merge authorization.** Do not begin acceptance until the **fresh exact-head** hosted CI gates below have completed successfully. The original [review-01 — CHANGES REQUESTED](reviews/review-01-chat-b.md) remains a separate historical finding. This R2 is not a repeat of the author tests.

## Source to pin

- [Draft PR #63](https://github.com/physicsvigilante/emfeeld/pull/63) exact feature HEAD `d3385fc5efa023c9519510ef84207c0741861a45`.
- Candidate Git tree `c15bd147bcd0618253d906b704b06d3d864829d2`.
- Original accepted `main` base `52aecd34338662e269fba091c0ff6664e8e1eca7`.
- Compare PR head, test-merge ordered parents [base, candidate], original original artifact source TAR and tree; do not accept source identity drift.
- The PR still adds **only 9 new circular-loop-related files**. Existing electrostatics/gravity/gauss/capacitor/wire files unchanged.

## Author correction context, not reviewer verdict

- [Original review-01](reviews/review-01-chat-b.md) requests correction for **F1 source bytes/state mismatch** and **F2 seven-ULP off-axis acceptance**; independently reproduced by original reviewer.
- [Author response R1](responses/response-01-chat-a.md) details corrected code and four new headless regression tests plus a new native test. Author locally ran 126 headless circular-loop and wire-focused tests with warnings as errors; this is not native or independent qualification.
- Keep old review-01 and previous screenshots intact; **no retrospective passing label**.

## Independent R2 challenges

1. **F1 — raw input provenance**: In `circular_loop_view.save_snapshot` create a +5 A physical state and provide valid raw JSON for -5 A; it must now raise before any output directory is created. Repeat with malformed raw JSON, duplicate/unknown key, Boolean and nonfinite/underflow tokens, invalid UTF-8, and live lesson where `lesson.initial != authored`. Verify exact original accepted bytes preserved for valid alternative JSON whitespace; do not merely hash a contradictory input. `load_lesson` and `lesson_from_bytes` must agree on all cases. Challenge rotated canonical normalized normals and no-source_bytes fallback; it must round-trip without 1-ULP drift.
2. **F2 — true axis-only refusal**: Reproduce `centre=(100,0,0),normal=(0,0,1),current=4`, `point=(100+1e-13,0,0)`; this **must refuse**, for nonzero and zero signed current. Challenge one-ULP resolved perpendicular offsets. For non-axis-aligned normals, perform own rotated/translated test cases to verify a rounded `centre+z*u` is accepted only if each coordinate is within **two binary64 ULPs of an axial reconstruction**; exact-zero normal components demand exact coordinate identity. Try independently shifted transverse probes clearly above that representational allowance. Verify proper SI B using independent `mu0 I R²/[2(R²+z²)^(3/2)]`, signs at ±z, reversal, I=0, R×2 at centre and fixed z/R. No off-axis B claim.
3. **Native 3D independent acceptance — still unproven in review-01**: Reviewer must **actually run native PyVista/VTK** on the corrected source and capture at least one **new reviewer-owned real PNG**, not rely on author or earlier hosted images. Exercise real VTK `KeyPressEvent` for 1/2/3, n/k/p/v/0 and both radius and axial-position slider `EndInteractionEvent`; verify visible slider pixels in right information pane after redraw, not just widget enabled flags; signed orange current arrow, green field arrows and invariant blue positive normal; physical edits rebuild data, reveal/camera edits do not. If PyVista install unavailable, explicitly return **INSUFFICIENT EVIDENCE**, rather than claiming complete native acceptance.
4. **Artifact integrity**: Independently download original **current-head** dedicated loop/native screenshot ZIP and fresh source TAR, hash whole ZIP, verify CRC and every original source-input/content/integrity receipt and source git tree. Validate source/current state screenshot correspondence and field vectors. Check exact-head Linux and Windows regression as distinct from previous candidate runs.

## Fresh exact HEAD workflow gates (verify conclusions yourself)

- [Dedicated loop native PyVista 44696085642](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085642)
- [Full Linux+Windows clean install 44696085549](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085549)
- [General real PyVista 44696085647](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085647)
- [Source snapshot 44696085577](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085577)
- [Straight wire 44696085703](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085703)
- [Gauss 44696085617](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085617)
- [Cavity 44696085582](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085582)
- [Dipole 44696085563](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085563)
- [Capacitor 44696085660](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085660)
- [Existing browser 44696085628](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085628)

**As of prompt creation, most exact-head workflows remain in progress.** Check the actual current statuses; do not infer completion from earlier runs.

## Required output

Publish a **new** independent file `projects/emfeeld/pr-63/reviews/review-02-chat-b.md` (do not overwrite review-01), including exact source identity, independently authored test cases/results, original reviewer-owned new PNG provenance, genuine native event/slider observations, independently validated original artifact identities, unresolved limitations, and an explicit one of **PASS (scoped) / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**.

Do not edit production code, approve merge based only on author tests, call a rerun a separate reviewer, or claim general Biot–Savart/off-axis field or JEE classroom effectiveness. Guarded merge and new merged-main qualification are builder-only work after fully supported PASS.
