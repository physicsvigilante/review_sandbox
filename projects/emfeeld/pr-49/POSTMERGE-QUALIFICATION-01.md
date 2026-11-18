# PR49 — actual-main qualification checkpoint01

18 November 2026. **Three actual-main workflows and their new original artifacts have passed author audit. Full Linux/Windows release qualification is still PENDING at this checkpoint.** This report does not reuse premerge ZIPs as main-push evidence.

## Source identity

Actual merge `6bfeb2c314841ef861d7d66b67c894a6295b705e`; source tree `4da6b80f53d78b2394c8516b9463e442fffb50fe`, identical to independently reviewed candidate `9963c09d169a04cea488886db5f04c0de4074886`. [Integration record](MERGE-REPORT.md) retains ordered-parent, expected-head and review assessment details. All three new source TARs below have actual merge SHA in their Git archive pax header and contain394 files byte-identical to the reviewed source. Local Git reconstruction returned the reviewed tree. Their TAR SHA256 is `99861139d1f993ed792cec765bc4e1c4c6cc8a6b88f99cde434cea1aa7d0618c`.

## Completed new main-push runs and original ZIPs

| Workflow | Run | Original artifact | ZIP bytes | ZIP SHA256 |
|---|---:|---:|---:|---|
| Gauss lesson/usability |44310514516|14429738484|14,448,764|`5f511008ea6c0b205300351b1caee6a0337d5be52e96e032f0c55f5b11f7845a`|
| Conductor cavity |44310514570|14430291674|13,463,967|`196498ab95d8c2b7e17ef37972213ce9f0071448ad1ba2b85a6a8d1338fbbc89`|
| Existing viewer |44310514531|14429981956|14,177,453|`b90e01bcf4cceca5dc81b194a7ff94ffc4a420aa010ea40157e343921d5de932`|

Connected GitHub job reads confirmed each completed/success, including artifact upload and cleanup. Artifact metadata ties each to main/actual merge. Original ZIPs were downloaded, whole-hashed against server metadata, CRC-tested, checked for unique safe member paths and absence of symlinks, then audited without modifying original bytes.

### Gauss lesson and small-window scenes

114 ZIP members; **127 focused tests passed**,14 scenes (eight original plus six usability); all92 scene-manifest references match. Fourteen implementation receipt sets each match all34 package modules. Original input bytes, current lesson hashes, screenshot hashes/dimensions, execution/flux availability and stored arrays are consistent. At unavailable boundaries, exact flux is null and electric-field arrays are absent. In available scenes the retained E dot n equals the dot product of stored E and outward normals.

Read-only local replay against exact source reproduced all14 archived physics dictionaries **exactly** in this environment (zero observed differences), after normalizing Python tuples to their JSON-array representation. The audit code allows explicitly recorded float64 cross-host roundoff, but none was needed here; no production tolerance was changed. The sampling caution was separately recomputed from original signed error, all prescribed charge magnitudes and the archived epsilon0. Its visibility follows prediction/shape/availability rules; it remains explicitly not an accuracy certificate.

The actual new six-scene usability sheet and eight-scene legacy Gauss sheet were visually inspected. At840x560, numeric panels, caution, controls and footer/colorbar have separate visible areas. The original boundary scenes are plain/unavailable without stale field coloring/arrows; ordinary cube scenes do not retain a sphere warning. The two supported window sizes are represented, not all DPI/window combinations.

### Conductor lesson

49 ZIP members; **71 focused tests passed**,six complete scenes; all36 scene-manifest references and six sets of34 source-module receipts match. Current-state/original-input and PNG hashes verified; the new six-scene contact sheet was visually inspected. This is regression evidence for unchanged conductor code, not new conductor physics.

### Existing viewer

22 ZIP members; **1,822 headless tests passed**,nine runtime cases PASS,17 PNG receipts matched exact PNG bytes and nonblank images. Report commit equals actual merge; nested/flat geometry equality is retained. All17 thumbnails were inspected as a contact sheet. This is author inspection of hosted renders, not manual Windows operation or a fresh independent review.

Focused counts overlap larger suites; do not add them as unique tests. Original reports correctly retain independent-review/human/teacher fields as not evaluated by those CI runs.

## Retained audit-harness first failure

The first local Gauss archive audit compared an in-memory tuple of face-name strings with the JSON list and mistakenly routed the unequal containers through numerical subtraction. NumPy raised UFuncNoLoopError. The original script and failure log are retained. The correction was confined to the audit helper: normalize the local measurement dictionary through JSON serialization before comparison. The complete corrected audit passed without changing product source, artifacts, tolerance or physics. This was not a candidate defect.

## Outstanding gate

Full Linux/Windows workflow **44310514548** remains in progress. At the last job read, Ubuntu had passed current headless/historical/graphics and was executing native evidence workflows; Windows had passed headless/historical and was executing graphics. Final completion of both full jobs, including downstream evidence and uploads, plus the new original Ubuntu/Windows ZIP audits are still required.

**Issue48 remains open; PR49 is merged but not yet fully release-qualified.** The separate focused reviewer PASS remains unchanged. No independent teacher trial, manual Windows mouse/keyboard acceptance, unseen-JEE or arbitrary-scale validation is asserted.
