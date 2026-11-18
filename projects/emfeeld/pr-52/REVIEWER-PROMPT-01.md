# Separate-context review request — PR52 renderer-neutral visualization

Review exact **head `3ea61a4d79d211009fb0b038fa56b7cef1e1e38c`**, tree `49afa15dbd3c1e9b15d0a41719eea7bdabd0540a`, base/main `6bfeb2c314841ef861d7d66b67c894a6295b705e`. Repository physicsvigilante/emfeeld, draft PR52. Publish independent verdict/scripts/outcomes at `projects/emfeeld/pr-52/reviews/review-01-chat-b.md` in physicsvigilante/review_sandbox. Do not merge or modify product source. Author tests/reports are evidence to challenge, not your verdict.

## Bounded architecture and physical meaning

Read AGENTS.md, the exact five-path diff (four additions/one modification), `visualization.py`, the general `viewer.py`, focused tests and `RENDERER_NEUTRAL_VISUALIZATION_V1.md`. Original physics, scene authoring, numerical integration, stored studies and specialized Gauss/cavity viewers must be unchanged. PR51 is a separate branch, not this candidate. This is a data/renderer separation, not a new engine, field-line solver or universal framework.

Write new probes for electric/gravity units; source geometry/strength meanings; finite versus infinite-source extents; physical vectors versus schematic equal-length arrows; particle paths versus field lines; marker radii; x-fastest potential sampling order; NaN/null preservation; saved-time/frame identity; detached arrays/metadata; repeated rendering without reintegration; static/recorded/nested/unknown-source and missing-renderer cases. A second renderer should consume the data without PyVista/VTK or re-evaluating field laws.

Old ba5e7a1e `to_dict()` leaked frozen record dictionaries via vars(). Editing exported units, geometry roles or annotation text mutated the original. Current source uses detached copies. Three first failures and later passes are retained. Independently challenge nested export mutations and verify that no renderer-local edits change physical samples or source objects.

## Actual PyVista compatibility

Use production PyVista/VTK, not a substitute. Exercise original `make_plotter` and snapshot-consuming rendering. Check real source/arrow/path geometry, saved sample markers, slider/key events, playback shutdown, potential units/legend and camera/axes/options. Compare the exact released base and candidate in the SAME runtime for deterministic arrays/geometry/images. Historical cross-host runs showed four trajectory-signature rounding differences despite17 identical PNGs; do not conceal differences with broad tolerances or demand unexplained cross-host bitwise identity. No physics tolerance may change.

## Source and completed author evidence

Fresh source run44347108397/artifact14447215687: ZIP SHA256 `6e49f21d6c31da35b6c324d18443ebc271b69ff69670e7fca43bf07dab3c91b5`, TAR `c5490d8aafbdf24f188010bb2e8bab3dac2aa053832318b3e3e65f3fe36fac04`. **398 tracked files** reconstruct the declared tree. Preview `d73eb8c5c00bcd1d6352c049057d66c918fb2f5b`.

Current full OS44347108199, viewer44347108249, Gauss44347108404,cavity44347108222 and source all completed SUCCESS. Both OS and local suites:1833 headless+18 historical(one existing obsolete guard deselected)+54 graphics. Focused counts overlap. Original Ubuntu14446474306 SHA256 `3351d5a4471779fe28706b494b54a8f9b043f4afa31bf3416fbe65935d3c3768`; Windows14448317667 SHA256 `ddfd1b003018a74932ea09fd9b5daddd9e100ef91c592e0ea919c8dc3f4a51b3`. Read report02 and recheck live outcomes/IDs rather than trusting this prose. Source and original OS payloads were author-audited; auxiliary workflow status alone is not an independent payload audit.

Original OS archives retain the known deliberately corrupted negative `derived-001/G1/review-challenge-resealed-native/native/result.json`; it must remain a refusal, not valid evidence or a new unexplained defect. Author runtime: Python3.13.5,NumPy2.3.5,SciPy1.17.0,PyVista0.48.4,VTK9.6.2/software EGL. Optional old hashed pure-Python wheels are an overlay, not a complete runtime.

## Verdict and gate

Return PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE scoped to affected architecture, physical meaning and compatibility. Include reviewer-authored cases, actual commands/results, screenshots and reproducible blockers. Distinguish author reruns/new assertions/human validation. Preserve failures, timeouts and unexecuted limitations. Do not label dummy graphics as real PyVista or this review as a teacher/manual Windows trial.

The author cannot supply this independent verdict. Keep draft until acceptance and guarded integration; fresh actual-main CI/archive audits are later required. PR53 is an isolated stacked browser prototype, not part of PR52's merge scope. Do not merge it into the reviewed feature branch or expand this review into a broad framework. The owner-facing combined packet provides exact source ZIPs, patches, failure logs and original artifact retrieval IDs, with separate PR51 follow-up instructions.
