# PR51 — author response to independent R2-01

2026-11-18. **Author correction implemented; independent follow-up required.** The original [review-01](reviews/review-01-chat-b.md), blob `6c0f8f1877205cea4deea6bbc73da290460df07b`, remains CHANGES REQUESTED. This response does not rewrite or close that verdict.

## Source pins and change boundary

Reviewed old head `f7cdf370fa44c40e6b5cb6d0c3ff580a7a364e52`, tree `00592c7cc15d5013b4702951ff0db9baa7376b25`.

Corrected head **`68f1b170d90e257082f23ce33d427b037a962435`**, tree **`9072602daaf0ab45d23162ac5597e3b02f25b0c2`**. Qualified base/main remains `6bfeb2c314841ef861d7d66b67c894a6295b705e`. Five correction paths: dipole viewer, contract, dedicated workflow, scene-capture script and one new graphics-test file. All numerical physics/core modules, old tests and existing evidence remain byte-identical. Total404 tracked files/36 package modules.

## Reproduction, interpretation and correction

Actual VTK E-polar75/E-azimuth40 EndInteractionEvents followed by B then1/3 reproduced the reviewer's nonzero stored torque and large schematic cue at840x560 and1440x960. Two added preset regressions failed on the original source. These failures and four before snapshots are retained.

The original cross product is correct for its represented coordinates. We did not zero it, change `measure()`, relax equilibrium classification or add a global torque threshold. Instead known key1/key3 constructions store an exact endpoint/field signature. Only while that construction still matches the live state, has the requested sign and lies within a documented coordinate-roundoff guard does the GUI suppress its misleading fixed-size torque arrow, plane and curved cue. The panel explicitly distinguishes **requested ideal alignment** from **stored rounded coordinates**, retains the numeric signed residual, and says the stored pose is not exact equilibrium. The ideal target's stable/unstable zero-torque meaning is separate.

The display guard is `8*eps*(1+(norm(r_plus)+norm(r_minus))/separation)` applied to normalized direction sine. It is construction-context presentation metadata, not a torque magnitude threshold, physical admission tolerance, proof of exact collinearity or measurement-acceptance rule. Arbitrary authored tiny signed torques—including newly authored identical rounded coordinates—retain their arrows and actual classification. Endpoint/field changes and reset invalidate provenance; charge/origin and view-only changes preserve applicable history. Zero q/E retain no-preferred-orientation semantics; exact axis cases stay exact; prediction hides the explanation.

Snapshot `display.preset_alignment` records requested target, actual stored equilibrium, residual, guard and suppression separately. No source bytes, raw torque array, energy or work are changed. Its visible/nonvisible state is tested through the production snapshot writer.

## Actual completed author execution

Full current-source local suites, warnings as errors: **1,894 headless +18 historical (one preexisting obsolete guard deselected) +68 real-PyVista PASS**. Six new graphics cases overlap the full suite. They cover both viewport sizes/native field-slider and preset-key sequences, saved NPZ torque and metadata, actual annotation bounds, prediction/reference/origin/failure/reset lifecycle, independently authored same-pose/tiny signed counterexamples and exact/zero cases.

Four before/after production captures preserve exactly equal entire physics dictionaries. Only wording/known-preset cue geometry changes. The corrected small-window image was visually inspected: retained torque values, explicit rounding explanation and separated control readouts; no full-size residual torque cue. Local14-scene capture completed. No hardware/performance/all-DPI or human Windows claim follows.

## Original fresh hosted artifacts checked

Source run44348225779/artifact14446492651, ZIP SHA256 `7b4827dd63bf165e2423612ebdd3ebf448ccb6dd891a85146d4e872699d4a669`. Original TAR SHA256 `51d7923e31131c61e1bbac88c1e64b752c542462c72e19a83e9164f447a229c7`, preview marker `a736fae575bd41b4a2f25d98a6a96afd17241a07`. All404 original source bytes match the local tested tree; local git write-tree equals9072602d.

Dedicated dipole run44348225614 completed SUCCESS: artifact14447351668, ZIP SHA256 `eda4d63032f0e046d618c13d1246d9b7ed27546e35b06f0c7e0dc4452944209d`. Original133-member ZIP passes CRC/safe uniqueness. **89 overlapping focused tests,14 actual scenes;15 inventories/239 matching hashes,504 module comparisons**. All14 saved physics/work reports replay exactly locally. Raw NPZ torque/moment/forces/energy, authored/current-state hashes and PNG hashes match. The four new native-preset scenes retain nonzero raw torque and omit only the explicitly disclosed cues.

Full current-head hosted OS workflow44348225657 and original OS archive audits are distinct completion gates; the later addendum records their final state. Prior f7cdf370 CI is historical evidence, not current-head certification. All first failures remain preserved, including original reviewer harness mistakes attributed to that reviewer rather than product defects.

## Requested follow-up

Please review **only the affected R2-01 display/provenance/receipt paths**, with new non-cardinal field/translation cases, rather than re-running a wholesale review of unchanged dipole equations. Challenge the roundoff-context criterion and provenance invalidation, wrong-sign/no-longer-aligned states, tiny genuinely authored moments, prediction, zero states and real screenshots. The separate reviewer must decide whether the blocker is resolved. Leave PR51 draft/unmerged and Issue50 open pending that verdict, guarded integration and fresh actual-main CI/archive gates. No Three.js work is mixed into this dipole correction.
