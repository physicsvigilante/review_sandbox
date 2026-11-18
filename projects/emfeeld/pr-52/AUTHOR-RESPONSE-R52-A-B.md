# PR52 — author response to R2-01/R52-A and R2-02/R52-B

**Author correction implemented; independent follow-up still required. No merge or release.**

## Review assessment and source pins

The original [independent review](reviews/review-01-chat-b.md), blob `69959528c981d1b0ec8a83b52ddcf417f017a9e8`, and [supplementary independent recheck](reviews/review-01-chat-b-independent-recheck-20261118.md), blob `d50b377532da99888d61904c8f375f89eb879e8e`, both requested changes for two bounded renderer-neutral contracts. Their original findings, independent positive tests, first reviewer harness failures and limitations remain unchanged.

- Reviewed head: `3ea61a4d79d211009fb0b038fa56b7cef1e1e38c`; tree `49afa15dbd3c1e9b15d0a41719eea7bdabd0540a`.
- Corrected head: **`43980b952e533483a36fedac2e95eab3df980f82`**; tree **`f161a608853e5e180c459d68454e48c8fb734c39`**.
- Released base/main remains `6bfeb2c314841ef861d7d66b67c894a6295b705e`.
- Current CI preview `d9e98328143b9a85c37bd77b5e36eeb256b86d85` has the same corrected tree and directly verified ordered parents [released base, corrected head]. It is not an actual-main merge.

Four paths differ from the reviewed source: `visualization.py`, its contract, and two added headless/real-PyVista regression files. There are400 tracked files;396 of the398 previously reviewed files are byte-identical. No field law, solver, general PyVista adapter, playback controller, old test, existing workflow, Gauss/cavity lesson or historical evidence was modified. PR51 dipole source and PR53 browser source are separate and untouched.

## R52-A: extreme finite field direction normalization

### Original author reproduction

With the existing strict parser, uniform gravitational field `(1e200,0,0)` produced343 correct finite nonzero physical samples but343 false zero direction vectors, with an overflow warning. `(1e-200,0,0)` produced343 finite nonzero physical samples but no arrows. An additional `(1e-160,-1e-160,1e-160)` case exposed inaccurate directions from partially underflowed squared components, rather than only complete omission. These outputs and original failing tests are retained.

### Correction

Validity is now based on finite components and at least one nonzero component. Normal-scale vectors use the unchanged legacy norm/division arithmetic to preserve existing rendering. For extreme scales only, directions are formed by dividing by the largest absolute component before normalization; no unrepresentable physical norm is needed. The safe arithmetic branch bounds derive from float64 range, not a physical cutoff or solver tolerance. Tiny unrepresentable component ratios may round, while the largest component and direction remain nonzero. Exactly zero or undefined fields still have no arrow.

**Raw SI field and potential values are not rescaled or modified.** Only schematic unit-direction calculation is corrected. Tests include mixed-sign nonaxial fields, smallest represented subnormal components, a vector whose magnitude exceeds float64 although its components are finite, mixed zero/undefined samples and exact normal-scale parity. Two actual-PyVista tests show that both extreme axis-aligned fields produce exactly the same real direction-glyph mesh as a unit field, while their physical values remain different and intact. This is not arbitrary-scale accuracy certification of every analytic source or renderer scalar mapper.

## R52-B: malformed recorded positions at the standalone builder

### Original author reproduction

A real trajectory coherently truncated to two samples for a five-sample scene was accepted. The exported snapshot claimed five frames, and `frame(4)` raised raw `IndexError`. This reproduces the independent finding without replacing the real trajectory with a mock.

### Correction and deliberately bounded contract

The standalone builder validates and detaches **all supplied position arrays before any field sampling**. Each must be real, finite and exactly `(scene.samples,3)`. Missing attributes, malformed shapes, invalid values and noniterable recording containers yield typed `ValueError`, not a returned snapshot with inaccessible frames. Solver-produced positions receive the same shape/finiteness guard before return. Valid recordings are copied without integration or interpolation.

The existing builder's position-only records remain supported. This guard does not claim to authenticate trajectories or certify particle count, timestamps, velocities, energies or initial conditions. The unchanged general `make_plotter(..., recorded=...)` still uses the existing stronger `study.validate_recorded` guard for those full-scene checks. Its existing behavior is preserved; no broader recorded-study or authoring schema was introduced.

## Exact corrected-source local verification

Environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, pytest9.0.2, PyVista0.48.4, VTK9.6.2; Linux software EGL. The existing optional viewer package and four supporting pure-Python wheels were hash-checked from the original PR44 offline archive and installed with `--no-index --no-deps --target` into an isolated container overlay. No owner's-computer installation or new product dependency.

Commands used corrected `src` plus that overlay, `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`, `PYVISTA_OFF_SCREEN=true`, `VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow`, `LIBGL_ALWAYS_SOFTWARE=1`, and `MPLBACKEND=Agg`:

- `python -W error -m pytest -q tests`: **1,857 passed**,132.07s.
- `python -W error -m pytest -q pilots/authorability_v1/test_pilot.py -k 'not test_all_available_parent_files_remain_frozen'`: **18 passed,1 preexisting obsolete guard deselected**.
- `python -W error -m pytest -q viewer_tests`: **56 actual-PyVista tests passed**,162.32s.
- Focused selection:37 passed, including24 new headless cases,11 existing data cases and2 new real-PyVista cases. These overlap the full suites.
- The first new24-case headless run on reviewed source had **21 failures and3 passes**, retained unmodified. Those parametrized failures concern the two identified root defects, not21 independent defects. No old test assertion or tolerance was relaxed.
- Additional same-author direction challenges:306 finite nonzero vectors spanning float64 exponents and branch boundaries agreed with separately expressed scalar `math.hypot` references within the stated roundoff comparison. This is not an independent reviewer verdict or global numerical proof.

## Same-host rendering preservation

Invoked unchanged production `tools/qualify_viewer.py` capture functions separately against the exact reviewed source and corrected source, using the same actual PyVista/VTK environment. No mock renderer or fabricated Git HEAD was used. **Nine cases passed on each source;47 mesh signatures and17 screenshot PNGs were exactly equal.** Native VTK slider events and physical marker positions remain part of those captures. Before and after images, raw JSON reports and comparison receipts are retained. The author visually inspected the electric-composition, gravitational-orbit and oblique-line/plane contact sheet. No manual Windows or classroom claim follows.

## Fresh hosted qualification — source audit complete; OS gate tracked separately

New workflows on corrected head: full OS44373152024; source44373152018; viewer44373151963; Gauss44373152053; cavity44373151974. Their final statuses and original OS archives must be checked separately; passed local tests do not substitute for hosted completion.

The original new source ZIP artifact **14459362685** was downloaded and read-only audited: whole SHA256 **`12d3a4092cc12ed2aca2e8f75ad9ed996ecb74309eae7e920d0abf6144b874b3`**, TAR SHA256 **`c0de48dd4e584ca2d5692577cd2fb230a98be0729292b3c141e1506a7474775d`**. CRC/safe paths,400 original Git blob hashes and all400 local tested file bytes matched; local `git write-tree` and remote preview both give `f161a608...`. Later hosted completion belongs in an additive report, not a retroactive rewrite of this checkpoint.

## Remaining gate

Request only a bounded independent follow-up on the two corrected data contracts, native glyph consumption and preserved recorded playback. Prior positive independent architecture/physics tests remain attributed to their original review. Do not call these author fixes an independent PASS. Keep PR52 draft; after accepted follow-up, use guarded exact-head integration and new actual-main release checks. PR51's separate R2-01 follow-up is already PASS on its unchanged accepted head; do not request a redundant wholesale dipole review. PR53 remains an isolated draft, not merged into this correction.