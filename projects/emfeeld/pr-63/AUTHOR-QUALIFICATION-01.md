# EMFEELD PR #63 — author qualification and reproducible audit (not independent review)

**Status: DRAFT / NOT MERGED / NOT RELEASED / INDEPENDENT REVIEW NOT PERFORMED.** Issue #62 is the JEE magnetic field of a circular loop at its centre and along its axis. [PR #63](https://github.com/physicsvigilante/emfeeld/pull/63) is a separate feature from the fully qualified straight-wire release PR #61.

**Current candidate HEAD:** `b2e19bad89bc70fdae7602478c55cc4002f64bf2`, Git tree `84b8b33364cd8b700984d0c51a15b7df1539c7d2`. **Main/base:** `52aecd34338662e269fba091c0ff6664e8e1eca7`, tree `047eca847cfc6bacfc3afebd51cf912a2f9deb18`. GitHub compare shows nine NEW files and zero existing tracked files modified. No changes to electrostatics, gravity, capacitor or wire physics.

## Physical scope

A single ideal perfectly thin circular current filament with radius R, signed steady current I, centre c, unit normal u and vacuum permeability; SI vacuum on-axis field **B(c+z u)=mu0 I R²/[2(R²+z²)^(3/2)] u**, signed centre field mu0 I/(2R) u. Refuses unsupported off-axis Cartesian probes; no general numerical Biot–Savart field, magnetic forces, induction, conductors or materials. Three centre presets compare original current, reversed current and R×2. Field is same sign on both halves of the axis at fixed signed I, flips with I, vanishes at exact zero. At fixed physical nonzero z, radius doubling does not in general halve B. `scipy.constants.mu_0` supplies SI mu0.

Layered code: strict numeric/versioned `src/emfeeld/circular_loop_magnetism.py` (physics), immutable detached `circular_loop_presentation.py` (SI vs schematic geometry in separate fields), `circular_loop_view.py` (PyVista rendering plus actual VTK controls). Source input/current states are separately snapshotted with field samples, PNG and per-file hashes.

## Why the current source differs from the first fully green dedicated lesson

The [earlier dedicated hosted run #44676459156](https://github.com/physicsvigilante/emfeeld/actions/runs/44676459156) passed **30 tests and nine real offscreen native scene captures** on PR synthetic commit `a968a29d7a3eb707a92ee616de7f40e529bcd068`, tree `baa08f07825e4aaeae68dde732db680b5178b5f4`, matching its feature head `e45b71848e62ea405f8279198fb429b8606738e8`. Its original uploaded artifact **14602259464** was downloaded, whole ZIP SHA256 `eac2c55a647bc8730584c37bf8d4bc0ceb3477317735c7bac2e8facd706cb03f`. I independently checked original ZIP CRC, unique entries, 461 tracked source files and reconstructed exact Git tree, every one of nine PNGs and **63 original per-file SHA receipts**, source/input hashes, signed SI centre/probe values and 3D actor/direction metadata: **316 author-side assertions passed**. Original snapshots distinguish +I, -I, 0, R×2, actual native slider changes and tilted loop. This is not an independent review.

**A visual regression was nevertheless found by looking at the real screenshots:** zero visible slider pixels in the lower-right pane, despite the VTK EndInteractionEvent tests succeeding, because both widgets had been created in the left 3D renderer which `redraw()` clears. A released PR61 straight-wire original screenshot confirmed the expected visible slider pattern in the right pane. The current PR63 code corrects the renderer selection before adding both widgets and adds pixel-level assertions to both real `viewer_tests/test_circular_loop_runtime.py` and `tools/qualify_circular_loop.py`. The fix preserves SI physics and expands test quality; prior history is preserved, not rewritten.

In an isolated Python environment using PyVista0.48.4/Vtk9.6.2 and the previous exact source archive with only that one renderer-selection fix, a new **genuine local offscreen PyVista screenshot** displayed both sliders. The specified right-pane region had **4,610 dark content pixels vs 0 in the earlier original artifact**. **30 focused tests passed locally**, warnings as errors. This is a useful author reproduction, but not yet exact-current-head hosted qualification.

## Current candidate gate (refresh before reviewer handoff)

Current exact-head GitHub runs (initially queued when this report was authored):
- [Dedicated circular loop 44678141388](https://github.com/physicsvigilante/emfeeld/actions/runs/44678141388)
- [Linux/Windows release regression 44678141157](https://github.com/physicsvigilante/emfeeld/actions/runs/44678141157)
- [General real PyVista 44678141088](https://github.com/physicsvigilante/emfeeld/actions/runs/44678141088)
- Also current-head source snapshot, Gauss, cavity, dipole, capacitor, wire and unchanged browser workflows.

Do not infer that the current source is qualified from a successful earlier SHA. **Required:** exact-head green dedicated 3D and complete Windows/Linux, original current-head screenshot + archived source tree rehash, separate scoped independent reviewer verdict, guarded merge, fresh actual-main dual-OS and real-PyVista qualification, original output audits. Neither native automation nor student/teacher usefulness or manual Windows human operation is independent classroom acceptance.

Independent review request is in [REVIEWER-PROMPT-01](REVIEWER-PROMPT-01.md). Do not merge or self-approve.
