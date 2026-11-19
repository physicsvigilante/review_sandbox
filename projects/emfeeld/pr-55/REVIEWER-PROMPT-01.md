# EMFEELD PR55 — independent Gauss 3D V2 desktop review

This handoff is self-contained and may be used in a NEW review conversation. Act as a separate reviewer, not the builder. Production PR55 is DRAFT/UNMERGED. Do not merge, change production source, or treat the builder's tests as your own. Write a NEW report at `projects/emfeeld/pr-55/reviews/review-01-chat-b.md`; do not overwrite any existing report.

## Immutable candidate and baseline

- Repository: https://github.com/physicsvigilante/emfeeld
- PR: https://github.com/physicsvigilante/emfeeld/pull/55
- Exact HEAD: `82b99982bac21bb56fc4e3738192a2446c38b160`
- Exact Git tree: `45fc03e72f6bddf791b65573464af1d059f19015`
- Qualified base/main: `c2ae1e0c6944bed7440fd4b185fd931d8eb71209`, tree `77c03d1092fe1c55a1c4641b82402894eb5d4155`.
- GitHub synthetic PR merge: `1d6e45d129ab1f9c27200e8c924b2bf45e51cb43`, tree IDENTICAL to candidate. Synthetic merge is not actual-main release.
- Issue54 records the bounded scope before implementation. Ten paths changed/added (+860/-76), 428 tracked files. Check the live head has not moved before concluding.

Original current-source artifact: run `44518155017`, artifact `14526635825`, ZIP 12,541,461 bytes, SHA256 `a8f0ce5cfe7557189c9a1af9a32906d179f5fc33f73b694fa7cdca7db3084fa1`. Nested `tested-source.tar` SHA256 `b197788b9dd03a60b06c711a64dfed7afc8836454e9cb2cad992501e18a308b8`. Builder checked CRC, unique safe paths, all 428 file identities/modes and native Git tree; independently reproduce rather than merely citing the claim. Source artifact is not graphical qualification.

## Narrow scope

Read new `gauss_presentation.py`, `gauss_teaching.py`, changes to `gauss_view.py`, new pure/native tests, `tools/qualify_gauss_v2.py`, docs, and the small extension of existing Gauss CI. Exact source diff is in the transfer kit as CHANGES.patch.

The existing `gauss_lesson.py`, `fields.py`, `integrals.py`, `dynamics.py`, other JEE lessons and browser renderer are unchanged. Do NOT repeat a broad Coulomb/Gauss-law proof or PDF/exam review unless a new relevant regression is demonstrated. No new field solver, numerical tolerance, browser migration or server is intended.

### Data preparation and rendering

New renderer-neutral Python data contains SI vertices/cells, surface probes/normals, sampled E and E dot n, original physical report and existing sampling caution. It imports no PyVista/VTK. Arrays are detached immutable-bytes-backed NumPy buffers; report and caution are read-only mappings. The unchanged physical evaluator owns field/flux results. A single-result cache is keyed by validated immutable state, sampling resolution and quadrature order. It commits only after complete successful preparation. PyVista constructs its own copies from this data.

Challenge: no imports of graphics during data preparation; actual immutability and alias safety; correct SI/report association after repeated edits; cache hit on equivalent state; invalidation on physical changes/resolution/refinement; no stale data following boundary refusal or an exception. Instrument physics independently and prove no calls for face/reveal/cutaway/active-charge/target/camera/resize changes. Verify sampling and report values against unchanged physics APIs, not a duplicated new law.

### Geometry and explicit V1 difference

Cube geometry and sampling preserve V1 ordering/arithmetic; face IDs are LOCAL +x,-x,+y,-y,+z,-z even after translation/rotation. Independently compare original and new cube geometry, actual selected PyVista face mesh, outward winding, probe/normal correspondence and signed face report. Selection and cutaway MUST NOT remove mathematical integration faces.

Sphere display connectivity retains VTK latitude/longitude triangles, but float64 analytic angle vertices replace VTK's float32 generator; display samples are NOT byte-identical. Builder native comparisons at resolutions 4/6/12/40 found unit-point/probe differences <5e-8. This is a presentation-comparison bound, not a changed physical acceptance tolerance. Physical sphere quadrature and exact total remain independent of the display mesh. Challenge closed seam/poles, outward normals, probes on analytic sphere and unchanged physical report; do not demand fictional pixel parity or mistake this representation change for a new solver.

### Student-facing controls/provenance

F cycles none/6 cube-local faces and outlines the selected face, with existing signed integrated face flux. It is not local E dot n coloring, and selection must clear on sphere. V hides/reveals selected flux and total. Boundary states show unavailable rather than stale values.

Actual native keys 1/2/3/4 choose synthetic center/off-center/outside/equal-opposite-inside configurations, using INITIAL authored surface and first signed charge, intentionally replacing the charge list. Zero first charge is refused rather than invented. Each begins in prediction mode; all answers come from the unchanged engine. Physical edits clear the exact-preset label; 0 returns to the authored state. Test a rotated/translated initial surface, negative charge, prior active second charge, sphere-specific questions and multiple switches. These are author-created conceptual cases, not original examination questions or measured teacher acceptance.

Live saved evidence must bind original authored input separately from current physical state, actual camera/widgets, selected-face/preset provenance, SI arrays and captured PNG. Snapshot should not rerun unchanged physics, nor reveal hidden numeric values on the screen. Stored evidence deliberately still contains the full physical answer. Inspect native PNGs at 1440x960 and minimum 840x560 for readable labels and actual selected geometry; newly run reviewer-owned controls are preferable to trusting existing PNGs.

## Evidence already available — explicitly BUILDER evidence

Final local full headless regression: 1,984 PASS, warnings as errors. New data/teaching subset: 55 PASS (included in 1,984, not additional). Original+new actual Gauss PyVista tests: 24 PASS (14 old +10 new). Eight final current-source screenshots and state-bound receipts passed integrity checks. Environment Python3.13.5, NumPy2.3.5, SciPy1.17.0, PyVista0.48.4, VTK9.6.2. External pytest plugins disabled locally; warnings remain errors.

Original local pip installation failed because network was disabled. An archived original runtime artifact was then verified and installed offline. First pytest invocation was interrupted BEFORE tests by unrelated auto-loaded pytest-asyncio configuration warnings. Both setup failures are preserved, not presented as product-test success. A first screenshot's overlapping face/charge label was corrected before the final candidate. Final logs and final scenes are clearly separate from earlier attempts.

Offline optional runtime ZIP in the review kit: artifact `14406007331`, original run `44256323755`, SHA256 `2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295`. It has five pure-Python wheels, NOT a bundled VTK/native platform distribution. Use only with a compatible already-installed NumPy/VTK environment. Native window/OpenGL support remains required. This provisioning is not independent review.

## Hosted checks — refresh before acceptance

At prompt creation, source `44518155017`, unchanged browser `44518155097` and cavity `44518154995` have completed SUCCESS. Gauss `44518154950`, general PyVista `44518154888`, dipole `44518154889`, and Linux/Windows release candidate `44518154894` remain in progress. Do NOT convert pending jobs into PASS; original successful current-source graphical artifacts must be fetched/audited when available. No current-source failure cause has been established. An old-source success is not this candidate's qualification.

## Suggested independent execution and disposition

Extract the original source TAR safely. Install the exact source into a suitable isolated Python environment, or put its `src` on PYTHONPATH while avoiding an older installed checkout in subprocesses. Read pyproject for native dependencies. Useful existing commands (rerunning these remains a rerun of BUILDER test cases, not new independent case authorship):

`PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -W error -m pytest -q tests/test_gauss_presentation.py tests/test_gauss_teaching.py`

`PYVISTA_OFF_SCREEN=true VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow LIBGL_ALWAYS_SOFTWARE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -W error -m pytest -q viewer_tests/test_gauss_runtime.py viewer_tests/test_gauss_usability.py viewer_tests/test_gauss_v2_runtime.py`

Independently design additional exact-state/cache/geometry/teaching-boundary probes and execute actual PyVista keys, slider events, camera/resize and a changed-state snapshot. If native execution is unavailable locally, a separately reviewer-owned hosted workflow may check out the exact pinned source in review_sandbox; do not circumvent environment policy or call surrogates native success.

Verdict PASS (scoped), CHANGES REQUESTED, or INSUFFICIENT EVIDENCE. Cite exact source, original artifacts, your new tests, first failures and any residual gaps. Keep PR draft/unmerged. Independent acceptance is not owner integration authorization; actual-main source equality, fresh postmerge CI and human usefulness remain separate. No recommendation to migrate to the browser is requested.
