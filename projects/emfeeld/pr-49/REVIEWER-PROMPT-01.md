# PR #49 — focused independent presentation review

You are a separate-context reviewer of `physicsvigilante/emfeeld` PR49 / Issue48. Do not treat Chat A's tests or this handoff as your own verdict. This is a bounded follow-up to independently reviewed/released PR47, not a request to repeat its entire unchanged physics review. Do not merge, modify candidate source, mark the PR ready or edit old evidence.

## Pin and authenticate

- Candidate HEAD: `9963c09d169a04cea488886db5f04c0de4074886`.
- Candidate Git tree: `4da6b80f53d78b2394c8516b9463e442fffb50fe`.
- Qualified base/main: `f6a078354ec2a657ca010c5c92ea578a0f55a2ad`, tree `65935bb395552d3dfb466a6e48d03230f18b6b66`.
- CI preview: `7635a3e96079f54167dbbb14f96299e8397555a1`; verify same tree and ordered [base,head] parents.
- Original source workflow44302715755/artifact14427545169; whole ZIP SHA256 `7ae28db3a740cd3aeb1feefd31f5a53600773aa130cde6be6858c943376aa4a7`; source TAR SHA256 `375c61cbdea9c9fb2f9595fdc475f46f898143f55f22b75f421ed19646c7222e`.
- Original Gauss workflow44302715942/artifact14426857273; whole ZIP SHA256 `3dd97ba302defcfe9131b51fbb101afe83b3b25b2c7cb864cd490bdea732e195`.

Read the repository AGENTS, Issue48, current PR49 metadata/diff, relevant lesson contract, and author qualification records in this directory. Authenticate original ZIPs against live GitHub metadata, verify safe paths/CRC and reconstruct the394-file tree. Six changed paths: viewer, lesson workflow, contract, two added test files and a new scene script. All numerical physics modules and old tests should be byte-identical; verify this rather than assuming it.

`AUTHOR-QUALIFICATION-01.md` has complete local results and an explicitly pending Windows checkpoint. Read any later completion addendum and current workflow state; do not promote a pending report to a pass. Full hosted workflow44302715851 is distinct from the focused lesson workflow. Viewer44302715977 and cavity44302715844 are additional regression gates, not independent reviews.

## Review the affected behavior only

1. **Meaning of the caution.** Independently check the display rule against raw production results: abs(sample-minus-exact)>0.01*sum(abs(all prescribed charges))/epsilon_0. It is not a solver tolerance, measurement acceptance criterion, rigorous bound or accuracy certificate. Challenge near-inside/outside sources, both signs, zero net enclosed charge, all-zero charges and symmetric cancellation. Absence of a warning does not establish resolved local samples. Ensure no values are normalized or boundary status altered.
2. **Live state transitions.** Exercise actual PyVista/VTK slider/key events, not a surrogate controller: warning appears for large discrepancy, can remain after refinement, hides for prediction, clears for boundary/unavailable and cube states, and reappears appropriately. Exact, sampled and signed error values must remain distinct. Check0.9999 versus1.0001 coordinates are visibly distinct.
3. **Real rendering and resize.** Capture fresh production screenshots at840x560 and1440x960, including a changed state. Use native render-window resizing without a physical redraw; verify annotations update without changing physical state, mesh/probe data, flux or camera. Inspect the readout, caution, sliders, colorbar/footer and axes. The defined minimum is840x560; do not assert arbitrary viewport, DPI or manual Windows usability. Check long-but-admitted displayed numbers or multiple charges as an additional challenge rather than testing only the default.
4. **Current-state evidence.** A new snapshot must retain original authored bytes separately, record the current window/control/caution state, bind the actual PNG and stored samples, and preserve numerical status. Boundary capture may execute successfully while flux remains unavailable/null. Check a prediction-state capture and one protected-output refusal. The added display metadata must not upgrade physical/teacher acceptance.
5. **Scope classification.** Author proposes R1 bounded presentation with focused review. Escalate any demonstrated numerical/admission/evidence-semantic change. Do not demand a second wholesale solid-angle physics review when its code is unchanged; do not dismiss a real affected-path defect because the patch is called UI.

## Runtime and commands

Use the exact source extracted from the original ZIP. Normal installation uses the repository's existing declared dependencies, not new software on the owner's machine. The optional preserved PR44 overlay contains five original pure-Python wheels (PyVista0.48.4 and supporting packages), SHA256 `2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295`. It is **not a complete standalone runtime**: compatible Python/NumPy/SciPy/VTK and software OpenGL must already exist or be installed in an isolated reviewer environment. Verify wheel hashes before offline installation; do not substitute reconstructed VTK objects and call them production PyVista.

Suggested environment: PYTEST_DISABLE_PLUGIN_AUTOLOAD=1; PYVISTA_OFF_SCREEN=true; VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow; LIBGL_ALWAYS_SOFTWARE=1; MPLBACKEND=Agg; source/src plus any isolated overlay on PYTHONPATH.

Authored regressions (rerunning is useful but not reviewer-owned new cases):

```
python -W error -m pytest -q tests/test_gauss_lesson_presentation.py
python -W error -m pytest -q viewer_tests/test_gauss_usability.py
python -W error tools/qualify_gauss_usability.py --output NEW_DIRECTORY
```

Add your own affected-path challenges and at least one fresh changed-state image/receipt. Author local full graphics initially hit240s after48 progress passes, then a distinct complete51-test run passed in242.43s. A short reviewer wall limit is not a source failure, but an unfinished run is not a pass. Use focused work and retain timeouts honestly. All focused counts overlap the full suites.

## Preserve failures and report accurately

The author initially used the wrong scalar-bar lookup key, corrected before candidate commit, and then corrected a clipped-line/axes layout prototype. A separate author cross-host audit initially demanded bitwise numeric identity; it found roundoff-scale differences with unchanged physical source. The corrected audit records those differences, not adjusted source hashes or relaxed production tolerances. Your own first failures, harness corrections, unavailable checks and screenshots must remain attributable to you.

Write `projects/emfeeld/pr-49/reviews/review-01-chat-b.md` in `physicsvigilante/review_sandbox`, with exact source pins, independent cases/commands, completed versus incomplete results, new screenshot/input/state hashes, any source changes since pin, and a **scoped PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** verdict. Provide reproducible blockers separately from nonblocking suggestions. Author CI counts are not your own checks. Do not certify teacher usefulness, human Windows operation or new physics. Guarded integration and fresh actual-main release/original archive audits remain Chat A's later work under owner direction.