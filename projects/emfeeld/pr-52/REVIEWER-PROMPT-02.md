# PR52 — narrow independent follow-up: R52-A/R52-B

Review the two previously reported data-boundary defects, not a new general architecture project. **Do not edit candidate source, merge PRs, or overwrite either original review.** Publish the verdict at `projects/emfeeld/pr-52/reviews/review-02-chat-b.md` (or a distinctly named additional report if that path already exists).

## Exact source

Repository `physicsvigilante/emfeeld`, [draft PR52](https://github.com/physicsvigilante/emfeeld/pull/52), branch `feature/renderer-neutral-visualization-v1`.

- Corrected head **43980b952e533483a36fedac2e95eab3df980f82**; tree **f161a608853e5e180c459d68454e48c8fb734c39**.
- Previously reviewed head **3ea61a4d79d211009fb0b038fa56b7cef1e1e38c**, tree **49afa15dbd3c1e9b15d0a41719eea7bdabd0540a**.
- Qualified base/main **6bfeb2c314841ef861d7d66b67c894a6295b705e**.
- Current PR CI preview **d9e98328143b9a85c37bd77b5e36eeb256b86d85**, identical corrected tree, ordered parents [main, corrected head]. Verify independently where available; do not attribute author checks as yours.
- Four changed paths relative to reviewed source: `src/emfeeld/visualization.py`, `docs/RENDERER_NEUTRAL_VISUALIZATION_V1.md`, new `tests/test_visualization_boundary_regressions.py`, new `viewer_tests/test_visualization_boundaries_runtime.py`.400 tracked files;396 of398 reviewed files unchanged. General PyVista adapter, physical field laws, solver, playback, existing tests and specialized lessons untouched.

[Original review](reviews/review-01-chat-b.md), blob69959528c981d1b0ec8a83b52ddcf417f017a9e8, and [supplementary recheck](reviews/review-01-chat-b-independent-recheck-20261118.md), blobd50b377532da99888d61904c8f375f89eb879e8e, remain historically CHANGES REQUESTED. [Author correction response](AUTHOR-RESPONSE-R52-A-B.md) documents first failures and exact-source local qualification. It is a claim to verify, not an independent verdict.

## Required new checks

### R52-A / R2-01 — finite nonzero fields, truthful unit directions

Independently reproduce old uniform gravity `(1e200,0,0)` and `(1e-200,0,0)` failures, then verify corrected343 directions and untouched raw fields/potentials. Add **new** mixed-sign nonaxial magnitudes/directions, partially underflowed squared norms, smallest-subnormal components and finite components whose mathematical norm exceeds float64. Use independently scaled scalar `math.hypot` or another stable reference, not merely the production helper twice. Check finite nonzero vectors remain nonzero/unit, zeros/undefined remain absent, origins stay paired correctly and JSON raw values/nulls retain meaning.

Review the arithmetic branch: ordinary-range vectors retain old norm/division for exact compatibility; extreme vectors use max-component scaling only for schematic directions. The limits derive from float64 range, not physical admission or a solver tolerance. No raw source field is changed or silently rescaled. Tiny unrepresentable component ratios can round away; absence of arbitrary-scale analytic-physics certification is explicit.

Render genuine PyVista glyphs from corrected snapshots. Verify real arrow meshes have finite meaningful orientation for extreme fields, source arrays stay unchanged and ordinary configurations retain their established geometry/playback. Do not substitute a fake renderer or count author tests as newly designed reviewer cases.

### R52-B / R2-02 — standalone recorded-frame boundary

Create a real saved `Trajectory` and truncate all its fields consistently to two samples while the scene requests five. Old builder accepts and `frame(4)` crashes; corrected builder must give a typed early `ValueError`. Independently test other wrong counts, wrong dimensions, missing positions, booleans/complex/nonnumeric/nonfinite values and a valid first path followed by an invalid second path. Prove **all supplied positions are checked before field sampling**, and invalid data cannot return an apparently usable snapshot.

Valid paths must preserve every existing position and saved-frame index, remain detached/read-only and never invoke integration. Exercise last frame and empty/static recordings. Position-only records remain supported by this deliberately small presentation API. It does not certify timestamps, velocities, energies, source authenticity, particle count or authored initial conditions; the unchanged higher-level `make_plotter(..., recorded=...)` still calls stronger `study.validate_recorded`. Do not mistake this bounded contract for a claim of full study validation, or introduce a new solver requirement just to accept presentation data.

### Preservation and evidence

Inspect the exact four-path diff. Check immutable numerical modules/adapter, schema version/units/roles, null handling and earlier detached metadata behavior. Use real saved playback and native VTK events. A proportionate ordinary-scene before/after comparison is sufficient; do not unnecessarily rerun the unchanged specialized lesson reviews. Author executed nine real scene comparisons with47 identical mesh signatures and17 identical PNGs, plus1857 headless/18 historical/56 graphics locally. These are author results unless you independently reproduce them.

## Original artifacts and runtime

Source run **44373152018**, original artifact **14459362685**, ZIP SHA256 **12d3a4092cc12ed2aca2e8f75ad9ed996ecb74309eae7e920d0abf6144b874b3**. Inner `tested-source.tar` SHA256 **c0de48dd4e584ca2d5692577cd2fb230a98be0729292b3c141e1506a7474775d**. Verify all400 files/tree; reverse the supplied four-path patch in an isolated copy to recover the398-file reviewed tree.

Viewer run **44373151963**, original artifact **14461141047**, ZIP SHA256 **586eedb950f8843dce4bda9d2624de00622c07283a46da6aae359b4618248f8a**. It contains nine actual scenes/17 PNG receipts and the same original source TAR. Full Linux/Windows run **44373152024**: query current final status and both original artifact IDs; original current Ubuntu is **14460747180**, SHA256 **e51c88d23ded8857f8199a901157f6ba24f0927b82d78958b31ebfb84e6c4964**. The additive author completion report and handoff manifest provide the final Windows identity once available; never infer final success from passed individual steps.

Author environment: Python3.13.5/NumPy2.3.5/SciPy1.17.0/PyVista0.48.4/VTK9.6.2, software EGL. Optional unchanged PR44 offline pure-Python overlay ZIP SHA256 **2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295** can be installed with `--no-index --no-deps --target` into an isolated reviewer directory. It is not a complete scientific Python/VTK runtime. Do not install on the owner's PC. Use warnings-as-errors and actual PyVista; preserve environment limitations and incomplete runs honestly.

## Decision

Return **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** scoped to R52-A/R52-B and affected data/renderer behavior. Keep original first failures and reviewer harness mistakes. A passing author or hosted suite is not independent scrutiny. Preserve known intentionally corrupted refusal fixtures as invalid evidence, not unexplained archive failures.

**PR51's unchanged dipole correction already has an independent scoped PASS; no additional dipole review is requested. PR53 browser code is excluded.** After this correction is independently accepted, the author may perform owner-directed guarded integration and fresh actual-main release audits. This follow-up itself does not merge, close issues or certify human Windows interaction, teacher usefulness, blind JEE success, all renderer inputs or general physical accuracy.