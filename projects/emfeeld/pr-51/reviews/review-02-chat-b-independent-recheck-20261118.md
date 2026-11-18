# Supplementary independent R2-01 recheck — EMFEELD PR51

**Date:** 2026-11-18. **Verdict: PASS — R2-01 preset-display/provenance/receipt correction ONLY.** This supplements but does **not overwrite** the preexisting `review-02-chat-b.md`; original independent `review-01-chat-b.md` remains historically CHANGES REQUESTED. No merge or Issue50 closure.

**Pinned sources:** draft PR51 corrected head `68f1b170d90e257082f23ce33d427b037a962435`/tree `9072602daaf0ab45d23162ac5597e3b02f25b0c2`; earlier reviewed head `f7cdf370fa44c40e6b5cb6d0c3ff580a7a364e52`/tree `00592c7cc15d5013b4702951ff0db9baa7376b25`. Reconstructed both exact trees, verified 404 source blobs and the five-path patch; physical `dipole_lesson.py` source byte-identical (`fee338771ff4745322561d51b538e3506cabdaac41b56d00f54f4e396af58e8d`).

## Independent real-PyVista VTK results

- **20 fresh real production screenshots** (840×560 and 1440×960) with native VTK slider `EndInteractionEvent` and actual registered keyboard B/1/3/V/T/O/reset callbacks. New E angles polar 41.375°, azimuth −128.625°, then 137.625°/33.75° with translated/modified geometry were used, rather than simply reusing the author's 75°/40° reproduction. Current-state production JSON + raw NPZ + screenshot SHA receipts were checked, with native actor/glyph and VTK annotation bounds assertions.
- For known parallel/antiparallel presets, residual **nonzero physical torque** and actual `not_equilibrium` remain, while only roundoff-origin large torque/rotation cues are suppressed. A **freshly instantiated state with the identical represented coordinates** has the exact same signed torque but retains torque and rotation-cue meshes because it lacks preset provenance. E.g. independent key1 and new authored state both retain `[9.294851926564675e-25,-6.620785079313314e-25,5.545448396153663e-26] N m`. Known-preset PNG SHA `33eba871ce4745e9d6d5f1ae4f21e7b063ec3cd96514eb3c36c1d37f326063fe`; independent authored same-pose SHA `eb7da390bfdec896a8be235b0ec0279dffa95bf07049ed6ee80d3107e6c12c1e`.
- Truly authored tiny signed torques as small as **±1e-50 N m** remain visible; there is no global torque-zero snap. Prediction hides derived cue/readout; live provenance mismatch restores the true cue. Zero charge/field, cardinal exact cases, work reference, invalid-control refusal and lifecycle changes verified.
- **Nine new reviewer-authored non-graphics groups** passed, including 16 preset cases at eight other new non-cardinal directions, ten provenance invalidation modes and persistence, robust near-roundoff display guard checks and 150 states against the unchanged physical law. Existing author tests separately rerun: 72 focused headless + six real PyVista (not counted as new reviewer tests).

## Independently audited original artifacts

Original dedicated dipole artifact `14447351668` SHA-256 `eda4d63032f0e046d618c13d1246d9b7ed27546e35b06f0c7e0dc4452944209d`: 133 safe/unique/CRC-clean ZIP entries, 15 manifests/239 matching references, 14 exact analytic physics/work scene replays and screenshot/NPZ receipts, 504 module hashes and 404 nested source files matched. Original Ubuntu `14448007611` and Windows `14449036014` archives were independently downloaded/checked: each 2,186 members, 173 manifests/1,750 references (one known intentionally corrupt refusal fixture), 82×36 module receipts. Hosted exact-head test logs show 1,894 headless+18 historical/one deselected+68 real PyVista per OS. These remain author/hosted execution, not independent full Windows test runs.

## Gate and evidence

**R2-01 correction PASS in this bounded scope.** Keep PR51 draft and Issue50 open until owner-directed guarded exact-head integration and fresh actual-main CI/archive qualification. Manual Windows, DPI and human teacher/JEE validity are not claimed. Original reviewer-only first failed expectation preserved in the evidence archive. No product files modified.

**Full reviewer-generated evidence:** owner-facing `EMFEELD_PR51_R2_01_Independent_Recheck_Evidence.zip`, SHA-256 `30889434b9ad8159a368b28b76ec44fa5d2509d83919bf3efb3c77ce3ef2c47f` (180 files: new scripts, first and corrected logs, independent fresh real screenshot/current-state receipts and NPZ arrays, source and original-archive audit results). Original source/CI ZIPs not repacked.
