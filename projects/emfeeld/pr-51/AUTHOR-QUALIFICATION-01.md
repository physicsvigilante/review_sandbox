# PR51 — JEE electric dipole V1 author qualification, checkpoint 01

2026-11-18. **Implemented DRAFT, not independently reviewed or released.** Current local suites and five specialized hosted workflows are complete; the full hosted Windows workflow and its original archive are still pending at this entry. A later completion addendum must close that gate; passed individual steps are not a completed workflow.

## Exact source and bounded scope

Candidate **f7cdf370fa44c40e6b5cb6d0c3ff580a7a364e52**, tree **00592c7cc15d5013b4702951ff0db9baa7376b25**, fully released base/main **6bfeb2c314841ef861d7d66b67c894a6295b705e**. PR51 on feature/jee-dipole-v1 adds exactly nine files; all394 baseline paths are byte-identical, including existing field laws, workflows, tests, PDFs and historical evidence. There are403 tracked files and36 package modules. GitHub CI preview **d14d78886ba366e6d0115e583cfcc25c7e7f9a80** has the same tree and ordered parents [base,candidate], verified through the connected Git-commit endpoint. The original source ZIP was independently reconstructed locally using git init/add/write-tree to that403-file tree, not merely compared with an author's claimed hash.

One rigid held pair of opposite charges in a prescribed uniform external electric field. Existing UniformField supplies E. Finite-pair endpoint forces, zero net external force, origin-independent couple torque, external orientation energy excluding mutual pair energy, and quasistatic work under fixed q/separation/E are implemented. These are static configurations, not free rotation or time integration. New conservative bounded SI/admission/cancellation guards are part of this R2 scope; no baseline numerical tolerance changed. Small nonzero torque is not snapped to zero, and a nonzero result below float64 range is refused. Zero q/E has no preferred orientation and unavailable p/E angle. A changed work constraint produces typed unavailable/null work, not a fulfilled rotation-work request.

The real PyVista controller provides six sliders and keys for orientation, field, separation, charge reversal/strength, pair translation, torque origin, presets, prediction and work reference. Actual force application points, right-hand torque axis/plane and a rotation-sense cue are shown with separately labeled schematic glyph scales. The cue is not solved motion. The display is explicitly recentered/rescaled; that transform is recorded. Snapshots retain current state, original input bytes, work reference, numerical arrays, actual controls/camera/font settings, versions and PNG/module hashes with shared output protection. Execution-complete records mean the capture completed, not that an unavailable angle/work or a whole JEE question was answered.

## Original textbook mapping

The committed original01_theory_elec.pdf was opened and actual PDF page48 / printed1.48 rendered and visually inspected. SHA256 **dfed5a5cf241a365a2d94ebfeb73a9473aad66184d73af38be7fbfd81e6876ab**. Illustration35 specifies +e at(1,2,1), -e at(0,1,0), E=(2,3,0), yielding p=e(1,1,1), torque=e(-3,2,1). SI coordinate/field interpretation is separately adopted, since units are not printed beside every given. q=1nC in the example is explicitly illustrative, not a printed numerical value; a test also uses the elementary-charge scale. The same page's orientation-energy/work discussion motivates U and deltaU; the rotating-rod dynamics exercise is outside V1. This visible source is not a blind teacher trial. The new contract documents primary MIT Coulomb-law and PyVista Arrow references; no textbook diagrams or long prose were copied into the application.

## Completed current-source local execution

Isolated Linux: Python3.13.5, NumPy2.3.5, SciPy1.17.0, pytest9.0.2, PyVista0.48.4, VTK9.6.2/software EGL. Only the already-declared viewer dependencies were used. Five original pure-Python wheels from the prior PR44 overlay were hash checked and installed offline with --no-index --no-deps --target into a separate container overlay; nothing was installed on the owner's computer. The overlay is not a complete Python/NumPy/VTK runtime.

Commands used source/src and the isolated overlay on PYTHONPATH, PYTEST_DISABLE_PLUGIN_AUTOLOAD=1, PYVISTA_OFF_SCREEN=true, VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow, LIBGL_ALWAYS_SOFTWARE=1 and MPLBACKEND=Agg. Final code was unchanged throughout the completed candidate runs:

- python -W error -m pytest -q tests: **1894 passed**,221.76s.
- python -W error -m pytest -q --color=no pilots/authorability_v1/test_pilot.py -k 'not test_all_available_parent_files_remain_frozen': **18 passed,1 existing obsolete guard deselected**.
- python -W error -m pytest -q viewer_tests, fresh separate serial invocation: **62 passed**,180.64s.
- New focused core/IO/graphics selection: **83 passed** =53 physics+19 IO+11 actual graphics. These overlap the full suites. New headless coverage72 and graphics11 are included, not additional unique counts.
- tools/qualify_dipole_lesson.py: **ten actual production scenes** completed at default1440x960 and supported840x560 sizes.

The physics tests use separately expressed endpoint-force lever arms, uniform-field potential differences, proper rotations/translations, energy gradients, work signs, zero/near-collinear/cancellation and strict-input cases. Graphics tests instantiate actual PyVista, native VTK sliders/key events, real arrow meshes/tips/application points, resize/camera independence, persistent visible slider representations and current-state snapshots. No surrogate graphics execution is relabeled as PyVista.

Additional same-author challenges executed15 actual bound key events, work-reference/changed-constraint/zero-field refusal transitions, and two small-window scenes at tiny and large admitted magnitudes. They passed, with fresh screenshots and event records. They are not independent reviewer tests or a statistical validation. Actual default/small/prediction/zero/parallel/antiparallel/changed-reference images and the two extreme scenes were visually inspected. Native font bounds and all six slider labels fit in these inspected cases; no all-DPI or all-camera usability claim follows.

## Completed hosted artifacts audited read-only

All listed artifacts are tied by GitHub metadata to candidate head and contain preview source, not actual-main release evidence. Each whole ZIP digest matches the original server metadata; unique safe paths, CRC and source preservation were checked.

| Kind | Run | Artifact | Original ZIP SHA256 |
|---|---:|---:|---|
| Source |44319905552|14435605157|46e885c79cc4d011a5845156b676b372267a041508e5ecd8f2b608832b3d2b0e|
| Dipole |44319905924|14434077716|68794fc92d7f460f3d8014df3e96f654a823da7c8a85e383e921b8b30abf78d2|
| Gauss/usability |44319905664|14434253713|8d9b6cbcec82b0e5dd6dd9ba1be5e7dce9bf96e55eb53ee8e07fe08b18781224|
| Existing viewer |44319905714|14434576422|263cd16529749298c0ef328285797a217e8eb803e205f5baa2801f5bf333d417|
| Conductor |44319905520|14434592015|6a81d30b8eff5d867872c7cb27d60747075dd3aca11f207262504a3bdf522ebf|
| Full Ubuntu |44319905997|14436020601|76950977e6083aec8c255a43a22b735b2fa12acb806e6e959ea874a01a3a500b|

The five original source TARs are byte-identical, SHA256 **805b06d1014f7574f879e583ebb82880223b55585a2ee4858974fdd807e106c0**. All403 source files and Git blob hashes match. The specialized workflows completed SUCCESS. Full Ubuntu job134855776278 completed SUCCESS; Windows job134855777052 was still completing downstream evidence at the checkpoint, after its graphics tests had passed. **No complete Windows/archive PASS is claimed here.**

Dipole original97-member ZIP:83 focused passes/ten scenes,11 inventories with171 matching hash references,10 sets of36 matching module hashes,10 PNG receipts. All ten archived current-state physics/work reports replayed exactly locally; original authored bytes, work references, physical NPZ arrays, image sizes and zero/prediction semantics were checked. Gauss114-member ZIP:127 overlapping focused tests/14 scenes,92 manifest references,504 module references. Conductor49-member ZIP:71 focused/six scenes,36 manifest references,216 module references. Existing viewer22-member ZIP: nine runtime cases and17 checked PNG receipts. Author inspected new contact sheets for each set.

Ubuntu2186-member ZIP:1894 headless+18 historical+62 graphics and downstream evidence.173 manifests/1750 references;1749 match plus exactly the previously declared deliberate corrupt negative derived-001/G1/review-challenge-resealed-native/native/result.json, preserved separately, not called valid evidence. All82 implementation receipt sets match36 modules. E1 remains complete and G1 partial; the old physics demonstration and native view logs remain present. Hash consistency is not independent authorship authentication.

## First failures and incomplete attempts retained

The handoff retains original logs, superseded source snippets, scene receipts and later corrected runs. No earlier failure is rewritten as a pass:

1. Initial numeric test harness exceeded the coordinate cap while intending to test unresolved separation. Only that harness position was corrected within the cap; the expected DomainError then exercised the intended guard.
2. First live scene exposed clipped footer text and removed slider representations after clearing the right renderer. The implementation stopped clearing widgets, replaced VTK table-like separators in text, and added real representation-presence checks.
3. Repeated redraws exposed a font-cache/render-order defect at snapshot time. New actors invalidate layout state, capture records actual font settings after rendering, and a regression checks repeated redraw/capture bounds. Slider titles were moved clear of the lower edge.
4. Charge cycling at the upper bound could repeat a duplicate choice; options are deduplicated and a regression verifies leaving that value.
5. A zero-charge work probe evaluated an irrelevant tiny dot product and raised underflow. Zero-strength work now short-circuits to its true zero result, with a new core regression. No nonzero physical value was softened.
6. One graphics harness attempted an upper-magnitude setup that rounded just outside its valid limit. The setup was moved below the cap; the actual invalid-slider/refusal assertion remains. No production bound was relaxed.
7. Earlier source versions and overlapping runs were stopped when source changed, and are incomplete, not final qualification. Two full graphics subprocesses ended -9 without verdict. The container recorded two OOM kills; per-process attribution is inferred, not separately proven. Orphan artifact_tool helpers from this session were cleared, then a distinct unchanged-source serial graphics run passed62.
8. The container's unrelated artifact_tool spreadsheet startup warmup prints a traceback; original stderr is retained. Successful emfeeld invocations still returned0 with completed assertions. An incorrect historical command collected no tests (exit5); the exact existing workflow command subsequently passed18/deselected1. A pre-final headless1893-pass run is not promoted to the final1894-case source.
9. Inspection replaced the overly general turning-effect heading with a neutral force/torque/energy title before the first commit, so zero-field and parallel scenes do not assert a nonzero torque. Final-source suites/scenes were rerun.

## Remaining gate

Complete the full hosted Windows job and audit its new original archive, then obtain a genuinely separate-context **R2 physics/graphics review on this exact head**. Do not merge from author or CI results alone. Exact-head guarded integration and fresh actual-main Linux/Windows/viewer/lesson/archive qualification remain later gates. Human Windows operation, independent teacher usefulness, unseen-JEE success and arbitrary-scale accuracy remain unclaimed. The released PR49 source and historical studies are preserved.
