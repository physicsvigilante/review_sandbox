# Separate-context review request — PR52 renderer-neutral visualization

Review exact **head3ea61a4d79d211009fb0b038fa56b7cef1e1e38c**, tree49afa15dbd3c1e9b15d0a41719eea7bdabd0540a, base/main6bfeb2c314841ef861d7d66b67c894a6295b705e. Repository physicsvigilante/emfeeld, draft PR52. Write your independent verdict/scripts/outcomes at `projects/emfeeld/pr-52/reviews/review-01-chat-b.md` in physicsvigilante/review_sandbox. Do not merge or modify product source. Author tests and reports are evidence to challenge, not your independent verdict.

## Scope

Inspect AGENTS.md, the exact five-path diff (four added/one modified), `visualization.py`, the general `viewer.py`, focused tests and `RENDERER_NEUTRAL_VISUALIZATION_V1.md`. All original physics, scene authoring, numerical integration, stored studies and specialized Gauss/cavity viewers must be unchanged. PR51 dipole is a separate branch; do not accidentally include it in this candidate. This is a small data/renderer separation, not a new physical engine, field-line solver or universal scene framework.

Independently test electric/gravity units, exact source geometry meanings, finite-vs-infinite source extents, physical vectors vs schematic equal-length arrows, calculated particle paths vs field lines, and schematic particle-marker radii. Verify x-fastest potential sampling order, NaN/null preservation, saved-time/frame identity, detached arrays/metadata and repeated rendering without reintegration. Challenge static, recorded, unknown-geometry, nested-source and missing-renderer cases. A second renderer should be able to consume the data without importing PyVista/VTK or re-evaluating field laws.

## Specific author-found defect to recheck

Old ba5e7a1e `to_dict()` leaked frozen record dictionaries through vars(). Editing export units/geometry/annotation text mutated the original snapshot. Current source uses detached dataclass copies. Three first failures and later passing cases are retained. Write your own nested export-mutation probes; do not only rerun the authored tests. Check physical arrays remain numerically identical and renderer-specific state does not contaminate source objects.

## Real rendering and existing contracts

Use real PyVista/VTK, not a stand-in. Exercise original `make_plotter` and the snapshot-consuming path. Check source/arrow/trajectory geometry, saved sample markers, actual slider/key events, playback shutdown, scalar units/legend, camera/axes and existing renderer options. Compare with the actual released base in the SAME runtime for exact arrays/geometry/image parity where deterministic. Original historical hosted runs on different machines had four trajectory-signature roundoff differences despite17 identical PNGs; do not require unexplained cross-host bitwise identity or hide real differences behind broad tolerances. No physics tolerance may be changed.

## Authenticated input and qualification references

Fresh source workflow44347108397/artifact14447215687: ZIP SHA2566e49f21d6c31da35b6c324d18443ebc271b69ff69670e7fca43bf07dab3c91b5, TARc5490d8aafbdf24f188010bb2e8bab3dac2aa053832318b3e3e65f3fe36fac04. Source403? **Correct count398 files**; reconstruct the actual declared tree, do not trust a filename or narrative count. Previewd73eb8c5c00bcd1d6352c049057d66c918fb2f5b. Full current OS run44347108199, viewer44347108249, Gauss44347108404,cavity44347108222. Read latest completion addendum/live GitHub outcomes; old ba5e7a1e passes do not certify new3ea61a4d.

Author local results:1833 headless+18 historical(one existing obsolete guard deselected)+54 graphics. Focused counts overlap. Original OS archives preserve a deliberately corrupted negative at derived-001/G1/review-challenge-resealed-native/native/result.json; do not admit it as valid evidence or count it as a new unexplained failure. Environment used Python3.13.5,NumPy2.3.5,SciPy1.17.0,PyVista0.48.4,VTK9.6.2/software EGL. Optional previously hashed offline wheels are an overlay, not a full runtime.

## Verdict

Return PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE, scoped to affected architecture, physical meaning and compatibility. Include new reviewer-owned cases, actual commands/output, screenshot receipts and any reproducible blockers. Distinguish author reruns, new assertions and independent human validation. Retain first failures, timeout/incomplete runs and platform limits. This is not a teacher trial or human Windows acceptance.

No review or release is supplied by this author request. Keep PR52 draft until independent acceptance and guarded integration. Fresh actual-main CI/archive audits are later mandatory steps. Isolated stacked PR53 is a browser proof of concept, not part of PR52's merge scope; do not merge it into the reviewed feature branch or expand this review into a broad renderer framework.
