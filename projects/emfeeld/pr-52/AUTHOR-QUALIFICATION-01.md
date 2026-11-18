# PR52 — author qualification and review handoff, checkpoint 01

2026-11-18. **DRAFT / UNMERGED. No independent review verdict yet.**

## Exact source

Current head `3ea61a4d79d211009fb0b038fa56b7cef1e1e38c`; tree `49afa15dbd3c1e9b15d0a41719eea7bdabd0540a`. Released base/main `6bfeb2c314841ef861d7d66b67c894a6295b705e`. Five paths relative to main: four additions and one modification (the earlier PR description's three/two count was corrected). 398 tracked files,35 package modules. No numerical physics, dynamics, authoring-schema or specialized lesson module changed.

The seam is `build_visualization(scene)` -> inert typed snapshot -> `render_pyvista(snapshot)`. Physical SI values, null/undefined samples, schematic direction glyphs and marker sizes, finite patches of infinite sources and calculated particle trajectories retain separate meanings. Existing general `make_plotter`, sampler injection, playback and camera behavior remain available. This is not a new simulation-authoring or sealed-evidence schema.

## Author-found export defect and fix

The preceding head `ba5e7a1e...` exposed frozen metadata through `vars()` inside `to_dict()`. Mutating returned units/geometry/annotations mutated the original snapshot. Three new parameterized regressions failed before correction. Current code uses detached `dataclasses.asdict()` copies. Raw arrays, physics samples and rendering were not changed. Failure and later passing logs remain in the owner-facing evidence bundle; this is author self-review, not independent scrutiny.

Current exact-source local qualification with warnings as errors: **1,833 headless,18 historical (one preexisting obsolete all-file guard deselected),54 actual-PyVista tests PASS**. The11 focused headless cases overlap the full suite. Runtime: Python3.13.5,NumPy2.3.5,SciPy1.17.0,PyVista0.48.4,VTK9.6.2/software EGL. The optional original wheel overlay was hash-checked and installed into an isolated container target only; no owner's-machine install.

## Original source authentication

Fresh source run44347108397/artifact14447215687: original ZIP SHA256 `6e49f21d6c31da35b6c324d18443ebc271b69ff69670e7fca43bf07dab3c91b5`; original TAR SHA256 `c5490d8aafbdf24f188010bb2e8bab3dac2aa053832318b3e3e65f3fe36fac04`. CRC/safe members checked. Every one of398 original source files matches the exact local tested bytes; local Git write-tree returns the declared tree. Preview marker `d73eb8c5c00bcd1d6352c049057d66c918fb2f5b`. Hashes are drift/integrity receipts, not human authorship proof.

## Prior-head CI and archives — completed, not promoted to current source

All five ba5e7a1e workflows completed SUCCESS. Full OS44339288416: each OS1830 headless+18 historical+54 graphics and downstream evidence. Both original ZIPs downloaded/audited:

- Ubuntu14442989905: `0590995f8a436af726d86762a38cc94db12b24dc30eca5bcc11bdbfd675f1ecb`.
- Windows14444452883: `05740af92d54cb383a833e44a869e92dd8f78aa40333e8f33a1df329d801fc55`.

Each2186 safe unique entries,173 inventories/1750 references:1749 match plus the one known deliberately corrupted negative `derived-001/G1/review-challenge-resealed-native/native/result.json`, not admitted as valid evidence. All82 implementation receipt sets match35 modules, including WindowsCRLF. E1 complete/G1 partial preserved.

The prior controlled same-host original-vs-refactored viewer comparison had nine geometry signatures and17 PNGs identical. Its original hosted viewer ZIP also matched all17 prior-main PNGs; four saved-trajectory geometry signatures had cross-host float64 differences between AWS/Azure. Those historical checks must not be called newly executed current-head image comparisons.

## Current hosted completion and next gate

Fresh current-head run IDs: source44347108397; full OS44347108199; viewer44347108249; Gauss44347108404; cavity44347108222. Final OS completion/new original archive audit is a separate gate; consult the later completion addendum rather than assuming this checkpoint closes it.

A focused **separate-context** architecture/physical-meaning-preservation review remains required. The author cannot supply its own independent verdict. After accepted review, guarded merge and fresh actual-main CI/archive audits remain mandatory. Main is unchanged. Browser prototype PR53 is isolated and stacked on PR52, not merged; its existence does not qualify this boundary. No manual Windows, teacher trial or general browser compatibility is certified.
