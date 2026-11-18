# PR #44 — fresh independent Chat B handoff (original reviewer chat unavailable)

**Prepared by the AUTHOR on 18 November 2026. This is a handoff, NOT a reviewer verdict.** The prior separate-context Chat B conversation is unavailable to the user. Do **not** claim to be the same Chat B assistant or to have executed its previous tests yourself. The original independent [review-01](reviews/review-01-chat-b.md), verdict **INSUFFICIENT EVIDENCE**, remains immutable. Its favorable 42 reviewer-owned physics/state cases, 15 independent reconstructed VTK cases and original archive inspection are **historical evidence**, not re-executions in a new context. The existing blocking issue **R2-B01** was inability to instantiate real PyVista `CavityLesson` controls and make a fresh screenshot/state report in reviewer context. No product source defect was demonstrated by the old reviewer, but independent real controls evidence is mandatory before any merge.

## Your role and decision

You are a **NEW independent Chat B reviewer in a fresh, separate conversation context**. Review the published report and original source, verify the exact candidate Git identity, execute **your own** focused real production PyVista/VTK tests, preserve first failures and publish an attributable new-context report at `projects/emfeeld/pr-44/reviews/review-02-chat-b.md`. You may cite review-01 as historical evidence but must label its executions as belonging to the *previous unavailable reviewer context*, and support any new PASS with your **own actual executed PyVista tests**, original screenshots and recorded exit statuses. A new PASS is permitted only if it is adequately supported; otherwise report CHANGES REQUESTED or INSUFFICIENT EVIDENCE. **DO NOT MERGE.**

## Exact immutable source (not the author support branch)

- Source repository: `physicsvigilante/emfeeld`; [draft PR #44](https://github.com/physicsvigilante/emfeeld/pull/44).
- Exact HEAD `e253d0acf15e7505f1da8ab95cb519b59b0d720b`.
- Exact Git tree `8a4a14d70ba824e8a338add08356003e79a248bc`.
- Qualified main/base `60b6e751363d0b922a02c3a259110547b79cf25c`.
- Source-equivalent CI preview `04f8926ff15697ecccd9d89f71e837f2eb45bf56` with identical tree, ordered parents [base, HEAD]; not an actual main merge.
- Original candidate source ZIP artifact ID **14401692570**, SHA256 `33059d044eb2b8ce824ecd6c7b65e3e05033b2fd30ca1f77676cd2f8e0437367`; 382 tracked files.
- PR remains OPEN, DRAFT, UNMERGED. No physics/lesson code change occurred after old review-01. Candidate feature is an opt-in 3D JEE conductor-cavity lesson, not a general conductor/PDE solver.

## Original independent review and author qualifications

Read in this order:

1. [Original independent review-01: INSUFFICIENT EVIDENCE](reviews/review-01-chat-b.md) — full evidence, **R2-B01**, 42+15 tests (old context), its initial failures and caveats.
2. [Original review requirements](REVIEWER-PROMPT-01.md) and [full requested scope](REQUEST.md).
3. [Focused live PyVista continuation](REVIEWER-PROMPT-02.md).
4. [Original offline runtime record](REVIEW-RUNTIME-01.md) and [author response](responses/response-01-chat-a.md).
5. [Original five-archive author qualification](AUTHOR-QUALIFICATION-01.md). Prior author CI passed **1,709 headless +18 historical +37 real-PyVista** on each OS; dedicated lesson 71 overlapping focused tests and six captured scenes. Author CI/screenshots do **not** substitute for your new executions.

You need not repeat unrelated full regression or 42+15 old tests solely because the original Chat B chat is lost, but **perform independent source/physics spot checks sufficient to contextualize your new graphics finding** and cite exactly whose prior cases you rely on.

## Offline PyVista runtime — already prepared, independently verify it

- Original GitHub provisioning workflow [#44256323755](https://github.com/physicsvigilante/emfeeld/actions/runs/44256323755), separate author-only auxiliary branch `support/pr44-offline-pyvista-review` **NOT** under review and NOT merged.
- Original runtime ZIP artifact **14406007331**, name `pr44-offline-pyvista-b99f832cc48c81984b8c830ada065cf9614ebf46`, whole ZIP SHA256 **`2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295`**, 3,241,942 bytes, 14 entries. GitHub Actions artifact link: https://github.com/physicsvigilante/emfeeld/actions/runs/44256323755/artifacts/14406007331
- The *identical original ZIP* may be supplied as `PR44_Offline_PyVista_Runtime.zip` in your new chat. SHA256 check it before extraction. Check ZIP CRC/safe paths and the five wheel SHA256 against its `manifest.json`/the runtime record.
- Five pinned wheels: PyVista0.48.4, scooby0.12.1, cyclopts5.5.2, rich-rst2.2.0, docstring-parser0.18.0. The archive **does not** supply VTK, NumPy or the rest of the environment. Reviewer’s isolated environment must have VTK9.6.2 and compatible NumPy/matplotlib/Pillow/etc. Never install on the owner's Windows/Conda.
- Safely extract outside the candidate source and saved evidence, then in a *fresh* interpreter:

```sh
python -m pip install --disable-pip-version-check --no-index --no-deps \
  --find-links "$RUNTIME/wheels" --target "$OVERLAY" \
  -r "$RUNTIME/requirements-overlay.txt"
export PYTHONPATH="$OVERLAY:$PINNED_SOURCE/src"
export PYVISTA_OFF_SCREEN=true VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow
export LIBGL_ALWAYS_SOFTWARE=1 MPLBACKEND=Agg
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
python -c 'import pyvista, vtk; print(pyvista.__version__, vtk.vtkVersion.GetVTKVersion(), pyvista.__file__)'
```

Author tested offline dependency availability and a basic real-widget screenshot smoke only. A longer author test attempt timed out: neither is independent reviewer evidence or an R2 PASS.

## Targeted reviewer-owned real graphics tests (R2-B01)

Write and actually execute tests against the **unmodified production** `CavityLesson` plus real `pyvista.Plotter`/`vtk` objects, not surrogates. Prefer small bounded scenes, separate processes/test groups, single numerical-library threads, fresh output paths and original logs.

1. Four visible/enabled slider widget representations in the correct renderer; verify **initial authored model remains bit-for-bit unchanged** by widget initialization.
2. Trigger **actual VTK interaction events** for offset, polar, azimuth and isolated-Q preset and registered **G/N/C/L keyboard events**. Verify model/control/label synchronization and grounded/isolated-Q semantics.
3. Verify camera unchanged when toggling cutaway, cutaway only affects rendered geometry (not fields/induced totals), actual production **`pv.Arrow` glyph vertices** remain wholly outside metal at admitted near-wall offsets for both signs and arbitrary orientations, and curves terminate in the correct physical regions.
4. After modifying a live controller, **capture new real PNG** and fresh `report.json`/state arrays/`lesson.json`/camera/settings/hash receipts. Independently inspect actual PNG content and verify it matches the changed controller, with source input retained separately. Test failed screenshot/output and protected sealed-root aliases without modifying historical evidence.
5. Preserve first failed cases and harness corrections; record interpreter version, actual import paths, source Git identity, original bundle hashes, commands and completed exit codes. If runtime fails or times out, do not invent success.

After actually executing reviewer-owned tests, publish `projects/emfeeld/pr-44/reviews/review-02-chat-b.md` and explicitly state **this is a NEW reviewer conversation/context continuing the independent evaluation from the published original review-01**. Reference review-01 but never as your own prior execution. Scoped PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE. **Do not merge.** Original review-01, source, report and wheel ZIP remain unchanged.

## Scope limits

Even successful programmatic widgets and snapshots do **not** prove real manual Windows mouse usability, JEE student/teacher acceptance, genuinely unseen teacher-question comprehension, whole-book solving, arbitrary conductor geometries, general Maxwell dynamics or a universal numerical error bound. Those remain separate evaluation goals.
