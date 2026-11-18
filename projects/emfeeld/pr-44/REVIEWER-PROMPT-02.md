# Chat B — focused R2-B01 continuation, PR #44 (unchanged source)

**18 November 2026. Author handoff only; do not merge.** Your original [review-01](reviews/review-01-chat-b.md) remains immutable **INSUFFICIENT EVIDENCE**, with favorable independently executed physics/state/archive checks but missing real PyVista control/capture execution. Complete that narrow missing check in your independent conversation context; do not restart the whole project review or substitute author tests for your own cases.

## Same exact candidate

- HEAD `e253d0acf15e7505f1da8ab95cb519b59b0d720b`
- Git tree `8a4a14d70ba824e8a338add08356003e79a248bc`
- Main/base `60b6e751363d0b922a02c3a259110547b79cf25c`
- Original candidate source artifact `14401692570`, ZIP SHA256 `33059d044eb2b8ce824ecd6c7b65e3e05033b2fd30ca1f77676cd2f8e0437367`.

No product source file was changed to address this environment gap. Verify current source refs/tree and your imports. A separate author provisioning branch is NOT the source under review.

## PyVista is now available without network installation

Read [REVIEW-RUNTIME-01.md](REVIEW-RUNTIME-01.md). Download original runtime artifact **14406007331** from repository `physicsvigilante/emfeeld`, workflow **44256323755**. Original whole ZIP SHA256 **`2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295`**; 3,241,942 bytes; 14 entries. Independently validate metadata, entire ZIP hash/CRC/path safety and all five wheel hashes from its manifest before installing. The same original ZIP may be supplied as `PR44_Offline_PyVista_Runtime.zip` in this handoff.

Safely extract to a fresh directory outside source and old sealed evidence. Install the five original wheels into a fresh isolated target with `python -m pip install --no-index --no-deps --find-links RUNTIME/wheels --target OVERLAY -r RUNTIME/requirements-overlay.txt`. These supplement your existing NumPy/VTK/matplotlib/Pillow/pooch/rich dependencies; they are not a full replacement environment. Start a fresh process with `PYTHONPATH=OVERLAY:PINNED_SOURCE/src`, `PYVISTA_OFF_SCREEN=true`, `VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow`, `LIBGL_ALWAYS_SOFTWARE=1`, `MPLBACKEND=Agg`, and `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1` to avoid thread oversubscription. Record actual imports/versions. Verified author-container versions include PyVista0.48.4 and VTK9.6.2; do not assume the rest of your environment equals the hosted build.

The author verified offline imports and a small production-controller capture in a local container. This merely establishes a usable runtime and is **not reviewer-owned execution**. A longer author rerun of four old graphics tests timed out and is explicitly not counted as successful; preserve your own failures/timeouts too.

## Independently execute the missing live graphics checks

Write and run your own compact tests of the actual unmodified `CavityLesson`/PyVista/VTK instances. Use bounded low display resolutions/line counts where adequate, not fake/surrogate renderers. Execute small groups with fresh output directories and retain completed exit statuses rather than treating timeout/progress as success.

1. Original input/model is unchanged by opening widgets. Four original slider representations are enabled, visible in the intended renderer, and consistent with model/preset values.
2. Trigger actual slider interaction events for offset/polar/azimuth/isolated-Q, and actual registered keyboard G/N/C/L events. Check grounded Q-preset semantics, state changes, visible values, redraw and labels, rather than merely calling mathematical model methods.
3. Verify camera/cutaway consistency and field exclusions. Inspect vertices of the actual production `pv.Arrow` meshes near the admitted wall for positive/negative charge and an off-axis orientation; independently reconstructed surrogate VTK glyphs are not sufficient for this missing gate.
4. Save a new rendered snapshot after changing the controller. Inspect the actual PNG content and compare its current model, widget values, camera, arrays, original-input bytes, report and image receipt. Exercise failed capture and sealed-root/output aliases in the live path without altering old evidence.

Retain first failures, corrected harness errors separately, exact source/imports, dependency manifest, commands, exit codes, raw logs and screenshots. Do not claim human Windows mouse/keyboard usability or teacher acceptance from programmatic VTK events.

## Append a new independent verdict

Publish **your own** `projects/emfeeld/pr-44/reviews/review-02-chat-b.md`: scoped PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE on the unchanged exact head/tree, expressly resolving or retaining R2-B01. Reference your existing favorable 42 physics/state cases, 15 native-VTK reconstructions and original archive audit without counting author executions or relabeling them. You need not repeat the incomplete full-headless run to claim a full rerun; be explicit that original cross-platform product CI remains author evidence. Preserve review-01 and its evidence unchanged. If execution remains unavailable or a defect is found, state that and keep the gate blocked.

**No merge permission follows from author runtime provisioning.** Actual-main release testing is a later gate after independent verdict and guarded integration.
