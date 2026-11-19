# EMFEELD PR52 — independent R52-A/R52-B correction follow-up (review 02)

**Date:** 2026-11-19  
**Verdict: PASS — strictly scoped to the two corrected renderer-neutral data-boundary contracts (R52-A and R52-B).** Not a release, merge, full hosted-archive, blind-JEE, or Windows human-interaction approval.

## Pinned identity, provenance and diff

- Draft [PR52](https://github.com/physicsvigilante/emfeeld/pull/52): current head `43980b952e533483a36fedac2e95eab3df980f82`, Git tree `f161a608853e5e180c459d68454e48c8fb734c39`, base/main `6bfeb2c314841ef861d7d66b67c894a6295b705e`. GitHub independently showed PR open/draft with that exact head and base on review.
- Previous independent-review head `3ea61a4d79d211009fb0b038fa56b7cef1e1e38c`, tree `49afa15dbd3c1e9b15d0a41719eea7bdabd0540a`. Its original [review](review-01-chat-b.md) and [supplementary recheck](review-01-chat-b-independent-recheck-20261118.md) remain **CHANGES REQUESTED as historical records**; this report does not overwrite or reinterpret their first failures.
- Independently verified packet ZIP CRC and every SHA256SUMS entry; original source ZIP SHA256 `12d3a4092cc12ed2aca2e8f75ad9ed996ecb74309eae7e920d0abf6144b874b3` and nested TAR SHA256 `c0de48dd4e584ca2d5692577cd2fb230a98be0729292b3c141e1506a7474775d`.
- Checked **all 400 original source Git blobs**, reconstructed the exact corrected Git tree, and matched each of the four separately packaged changed files to that tree. In a **separate isolated copy**, reversed the exact supplied correction patch and reconstructed the previous **398-file** tree exactly. No candidate-source tracked file was edited.
- A GitHub commit comparison independently shows **one commit/four paths only**: `src/emfeeld/visualization.py`, `docs/RENDERER_NEUTRAL_VISUALIZATION_V1.md`, new `tests/test_visualization_boundary_regressions.py`, new `viewer_tests/test_visualization_boundaries_runtime.py`. No field law, solver, existing PyVista renderer/playback module, specialized lesson, existing test, or schema version changed.

## First defects independently re-created, then corrected

Using the two fully reconstructed exact trees, the reviewer executed the *same separate minimal probe*:

| Input / boundary | Previously reviewed tree | Corrected tree |
| --- | --- | --- |
| Uniform gravity `(1e200,0,0)` | 343 finite nonzero raw samples but **343 false zero-unit arrows**; overflow warning | 343 finite nonzero raw samples and **343 proper nonzero arrows**; no warning |
| Uniform gravity `(1e-200,0,0)` | 343 finite nonzero raw samples but **zero arrows** | 343 matching nonzero unit arrows; no warning |
| Real trajectory coherently shortened to two positions for five scene samples | Builder accepts; reported five frames; `frame(4)` crashes with raw `IndexError` | **Early typed `ValueError`** before snapshot return |

These reproduce the original **two root defects**, not 21 unrelated bugs. The first failures in the original reports remain preserved.

## Independent R52-A challenge: PASS

Reviewer-authored tests use an **independent scalar `math.hypot` reference**, not repeated calls to the production helper. New checks include: mixed-sign non-axial directions; components in the `1e308` range whose mathematical magnitude exceeds finite float64; tiny subnormals; partial squared-norm underflow; ratios spanning hundreds of decimal orders; normal-range exact arithmetic; and inputs on both sides of the `sqrt(float64 tiny)` and `sqrt(float64 max)/2` branch boundaries.

- **15 separate strict authored uniform-field inputs** each preserved all 343 raw SI vector samples, their source-model potentials, origin identities, 343 finite unit directions, field/potential units, schema version, JSON content and schematic/not-field-line roles.
- An additional independently constructed **343-row mixed field sampler**, including 338 nonzero finite rows, zero and nonfinite rows, was checked against per-row independent scalar references. Valid origins stayed paired with direction rows; invalid/zero rows were omitted and undefined raw components serialized to JSON `null` rather than being silently converted to physical zero.
- Two **actual PyVista 0.48.4 / VTK 9.6.2 glyph renders** for new mixed-sign extreme/subnormal fields produced finite, oriented real arrow meshes matching independent oracle-generated VTK glyphs; visible nonblank 1200×850 screenshots and unchanged source raw arrays were verified. These were not fake or mocked renderers.
- Source inspection confirms ordinary-range legacy norm/division is retained; scaling is restricted to **schematic direction computation** outside its numerically safe region. There is no physical magnitude rescaling, new source cutoff, field-law adjustment, or physics tolerance.

R52-A is accepted for its documented representable-input presentation contract, **not** certification of arbitrary-scale analytic physics or every downstream VTK scalar coloring behavior.

## Independent R52-B challenge: PASS

- **16 varied invalid second records after a valid first path** (missing/non-numeric data, wrong counts/dimensions, bool/complex/string/object arrays, NaN and infinity) produced typed early `ValueError` before a forbidden field sampler or reintegration could be called. A genuine saved `Trajectory` shortened coherently across its physical fields was likewise refused before sampling.
- Valid real trajectories and position-only records preserved **every saved frame** without reintegration or interpolation, with detached read-only position arrays (mutating source arrays did not alter the snapshot). Multiple valid paths and static/empty recordings remained supported; invalid frame indices were rejected.
- Genuine native VTK slider `EndInteractionEvent` playback through **all seven saved indices**, including last-frame and reverse-order seeking, moved the marker to the correct recorded positions without consulting a solver.
- The bounded builder validates only the **position arrays needed for portable frames**. It does not claim full timestamp, velocity, energy, particle-count, provenance or initial-condition certification. The unchanged higher-level `make_plotter(..., recorded=...)` still invokes the stronger `study.validate_recorded` contract.

## Independent preservation and execution results

In an isolated Linux/Python 3.13.5 runtime with NumPy 2.3.5, SciPy 1.17.0, actual PyVista 0.48.4/VTK 9.6.2, software EGL and warnings treated as errors:

- **37/37 new reviewer-authored tests passed.** The *first* reviewer harness had **16 failures/21 passes**, caused solely by two reviewer mistakes: comparing shapes `(343,3)` and `(3,)` without tiling, and sending NumPy scalar types to an intentionally strict JSON-number parser. Only reviewer code was corrected; original failure output is retained.
- **40/40 selected existing author tests passed** (data, new boundary regression, actual boundary PyVista and existing renderer tests); these are *not* counted as independent test design.
- Three ordinary scenes (**electric_sphere, line_plane_fields, ideal_sun**) were independently rendered on the reviewed and corrected trees, with **16 exact VTK mesh signature matches and five exactly equal pixel-array capture hashes**, including genuine native last-frame slider events in moving scenes. This is a reviewer before/after check, independent of the author's nine-scene preservation claims.
- Independently read-only audited the supplied **original Ubuntu ZIP** (`14460747180`): CRC, safe unique 2,186 entries, 173 integrity manifests, 1,750 hash references, **1,749 matching** and exactly one intentionally corrupt refusal fixture `derived-001/G1/review-challenge-resealed-native/native/result.json`. The negative fixture was **not repaired, relabeled valid, or treated as an unexplained release failure**.

At this follow-up, GitHub Actions returned **success** for both Ubuntu and Windows jobs in run `44373152024`; it listed the newly completed Windows original archive **`14461791503`** and Ubuntu archive `14460747180`. **The original Windows archive was not downloaded or independently byte-audited in this review**. This updates the earlier *at-packaging* Windows-pending observation without pretending to have completed its archive gate. Author full-suite numbers (1,857 headless, 18 historical with one obsolete guard deselected, 56 graphics) remain attributed to the author/hosted runs, not reviewer reruns.

## Decision, scope and remaining gates

**PASS** for **R52-A / R2-01** and **R52-B / R2-02** at the pinned head only. No remaining correction blocker found in these two boundaries. Both original CHANGES REQUESTED reports, including reviewer harness mistakes, remain historically intact. No candidate file, PR, issue, or branch was modified by the independent reviewer; no merge was made.

This does **not** approve PR53/Three.js, reopen PR51's already separately reviewed dipole change, certify all rendering inputs, certify manual Windows behavior, solve blind JEE problems, or approve a production release. Owner-directed guarded integration and fresh actual-main CI plus original archive audits remain later gates.

**Reviewer evidence:** `PR52_Independent_Boundary_Followup_Evidence.zip`, SHA256 **`64bb3261d53bf3c16d6c2292d53c1e2030d22b907ddcea6c997718a1fa786684`** (25 entries, 10 independently captured PNGs, first-failure/final logs, new tests, old/new probes, native preservation signatures and Ubuntu audit); supplied separately in the reviewer conversation, without repacking original archives.
