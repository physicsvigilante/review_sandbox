# PR #47 — independent R2 review request: JEE 3D Gauss-law lesson

Review the completed, pinned candidate independently. Do not assume the author's desired verdict; do not merge. This is a separate-context technical review, not an independent human teacher trial or blind JEE evaluation.

## Exact target and baseline

Repository: physicsvigilante/emfeeld; draft PR47; Issue46.
Candidate: `fcf9fede87ccd37597d0ba8c9b9013ee99b764f0`.
Tree: `65935bb395552d3dfb466a6e48d03230f18b6b66`.
Qualified main/base: `aeea3fedb00de4e20304d1f88aa038f3fac1e99e`.
CI preview: `457e2e3d79b205a7bb61fe7c4af5d9d585415d96`, same tree, ordered parents [base, candidate].
Nine added paths; all382 baseline files unchanged;391 total files,34 package modules. Scope is the opt-in lesson, not changes to native observations or the old solver.

Read AGENTS.md, Issue46, docs/GAUSS_LAW_LESSON_V1.md, the actual new implementation and tests, and the original PDF problem. Treat author qualification and screenshots as evidence to verify, not as independent proof. Check live full current-source CI before issuing a readiness verdict; the dated author record states what was complete at handoff. A pending CI job is not a PASS.

## Original artifacts, available directly from GitHub

- Source: workflow44281829140, artifact14417551219. Whole ZIP SHA256 `e809ad6857199ede1188761d5f2c27f1d8be22de38f8736277147ce5cec5e97d`.
- Dedicated Gauss lesson: workflow44281828953, artifact14416219886. Whole ZIP SHA256 `372266e215c975aa26b6accfd40e3649b3bde6c0029284f73b309adec6ae5dd9`. Contains the full tested-source TAR, original83-test log, environment and eight scene directories.
- Both original TAR members: SHA256 `c9be3901bb882e9e69193b51e69ff95d4945dc500720b9ac9549a621286226ea`.
- Optional original offline PyVista overlay from PR44: artifact14406007331, whole ZIP SHA256 `2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295`. Contains five pure-Python wheels, not a full Python/VTK installer. They are dependencies, not reviewer results.

The bundle retains these ZIP bytes unchanged. Verify original GitHub artifact digests and source tree yourself; local unkeyed hashes alone do not authenticate an author. Do not edit or reseal original evidence. Extract to new paths after path/CRC validation.

## Required fresh reviewer-owned challenges

1. Derive and test central cube face flux Q/(6 epsilon_0), signed oriented integration, exterior positive/negative cancellation, off-centre closure, multiple charge signs and superposition, translation/rotation/scale covariance. Use an independently expressed reference, not the production formula copied under a new name. Challenge the near-plane evaluation switch, face/edge/corner ambiguity and far-source stability within the declared domain. No rescaling to force closure is allowed.
2. Sphere: independently compare sampled and exact totals, vary charge offset/order and approach the surface from inside/outside. Sampling error must remain truthful, not silently normalized. An undefined boundary result must not turn into a zero, a half charge or a successful requested measurement. Confirm the documented conservative zero-strength marker boundary policy.
3. Test invalid/overflowing/boolean/string geometry and rotations, bad schema/duplicate keys, invalid quadrature orders and geometry whose side is unresolved after translation. Check that refusals occur before output writes or live physical-state corruption.
4. Instantiate the **actual GaussLesson in PyVista**. Exercise real slider events and bound key callbacks; source sign/selection/pair, surface movement/size/rotation, shape, predict/reveal, cutaway and refinement. Check outward cube geometry, true rotated edge outline, no auxiliary cube around a sphere, analytic sphere probe positions and actual arrow mesh directions. Camera/cutaway must not change the closed mathematical flux. Boundary crossing must clear stale values/colors/arrows.
5. Capture a new screenshot after changing physical state and camera. Verify current state, original input bytes, SI arrays, image hash and implementation receipts; challenge sealed-output aliases/reuse and incomplete failures. Inspect the image, not just its nonzero pixel variance. Author-provided PNGs and surrogate VTK reconstructions do not establish fresh live-controller execution.
6. Verify the actual original textbook mapping: Illustration47, printed1.60–1.61 / PDF pages60–61. Square edge2l, charge+Q at perpendicular distance l, corresponding central-charge cube. Illustration46 is a different nonuniform-field cuboid. Default l=1m/Q=1nC are author display choices, not source numeric givens. Solid-angle computation is separately selected machinery, not claimed to be the book's algorithm.

## Environment guidance

Headless tests need only the declared dependencies. In an isolated environment that already has Python3.13, NumPy2.3.5, SciPy1.17.0, pytest and VTK9.6.2, the included wheel overlay supplies PyVista0.48.4 and four pure-Python dependencies without networking:

```sh
python -m pip install --no-index --no-deps --target /new/overlay /new/runtime/wheels/*.whl
export PYTHONPATH=/new/overlay:/new/source/src
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export PYVISTA_OFF_SCREEN=true
export VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow
export LIBGL_ALWAYS_SOFTWARE=1
export MPLBACKEND=Agg
python -W error -m pytest -q /new/source/tests/test_gauss_lesson.py /new/source/tests/test_gauss_lesson_extended.py /new/source/viewer_tests/test_gauss_runtime.py
```

Those commands reproduce author tests; write and execute additional reviewer-owned cases. Report unavailable dependencies or timed-out runs precisely. Do not install anything on the user's computer. A different operating system is not automatically a matching Linux/Windows CI run.

## Output

Write a separate report at `physicsvigilante/review_sandbox/projects/emfeeld/pr-47/reviews/review-01-chat-b.md` with exact head/tree, fresh commands/environment, retained first failures and any harness corrections, independently executed cases, image/source inspection, findings and explicit limitations. Choose SCOPED PASS, CHANGES REQUESTED or INSUFFICIENT EVIDENCE based on what actually ran. Provide reproducers for blocking defects. Do not change the candidate or merge. Preserve earlier author failures and the distinction between author automation, independent technical review, future main-push qualification and human teaching acceptance.
