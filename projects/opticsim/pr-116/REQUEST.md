# Opticsim PR #116 — R2 physics review request: bounded multi-element native depth (v17)

**Status: prepared for independent review once final source-CI is verified. No Chat B verdict received. DO NOT MERGE.**

## Source and dependencies

- Source [draft PR #116](https://github.com/physicsvigilante/opticsim/pull/116), new `feature/native-two-thick-lens-mirror-v17` branch based on previously R2-cleared but owner-held v16 `94ea1a184e025065fe28da49691a3f39dc916296` [PR #113](https://github.com/physicsvigilante/opticsim/pull/113). Source head is under active CI corrections at request creation; **independent reviewer must inspect final exact source HEAD and its Git tree**. The source PR temporarily targets main solely to activate existing workflow triggers, then must be retargeted to the unreleased v16 dependency.
- v16 depends on reviewed but unreleased v15 [PR #110](https://github.com/physicsvigilante/opticsim/pull/110) and v14 [PR #107](https://github.com/physicsvigilante/opticsim/pull/107); all remain DRAFT/UNMERGED and require independent owner merge authorization.
- Pinned native PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`; it must not change. No new solver, fake ray route, modified brightness threshold or native cutoff.

## Proposed new v17 scope

A new **isolated** schema and adapter v17 model `native-two-thick-lens-mirror-tracing` explicitly accepts **exactly two independent finite stationary nonrotated biconvex native SphericalLens** objects, **one finite native Mirror**, **1–4 explicitly directed native SingleRay sources**, and **0–2 passive detectors**. Each lens retains individual front/back spherical radii, finite aperture, positive rim, material index and Fresnel flag, sharing exactly one explicit exterior index. Complete bodies separated by >=0.01 mm in x. The mirror's *full finite segment*, including both endpoints, stays >=0.01 mm horizontally outside EACH lens full x envelope; the existing v4 optical mirror/source and detector validators remain. Sources, detectors and lens geometry are enforced by the entire unchanged v15 two-lens validator on a **read-only validation-only subset**; the canonical/native object lists remain intact. No extra optics, third thick lens, nested media, image calculation, wave/ray ancestry or guarantee of return.

## Explicit native simulation policy — core review risk

Source [test-only PR #115](https://github.com/physicsvigilante/opticsim/pull/115) previously established that a true `D1→L1→L1→L2→L2→M1→L2→L2→L1→L1→D1` return requires more native ray depth than prior public v15/v16 `maxRayDepth:8`. That prior test used native JSON AFTER canonical validation, not an admitted public arrangement. The actual pinned depth sweep showed depth 8/9/10 incomplete with truncation 0.5 in the synthetic fixture; 11/12/16 completed with zero truncation.

The v17 contract now adds a **new explicitly named `native-deep-v17`** authoring policy (rayDensity=0.2, `maxRayDepth:16`, processedRayLimit=10000), selected by default **only for new v17 authoring when no policy is supplied**. If v17 explicitly requests the historical `preview-v1`, its depth=8 and incomplete run must remain unqualified. All earlier v1–v16 canonical documents remain capped at depth 8, including v15 and v16 optical scenes; no older save may be upgraded silently. The v17 native max-depth ceiling is 16, not an automatic dynamic expansion, and its larger budget does not guarantee a complete Fresnel tree or image.

Review whether `src/authoring.js`, `src/contract.js`, `src/composition-profiles.js`, `src/two-thick-lens-mirror-composition.js`, `src/adapter.js`, `src/observables.js` actually enforce these policy/geometry/isolation claims without modifying the pinned native engine. Incomplete ray depth, weak Fresnel branches, undefined behavior, corner ambiguity, stopped runs, stale exact scene hashes and export/reopen must continue to suppress requested measurements.

## Validation and source CI

Synthetic fixture `examples/native-two-thick-lens-mirror-v17.json`: source S1 (−200,0) pointing 0°; L1 (0,0) Rfront=Rback=100 mm, aperture 100, thickness 30, ninside=1.5; L2 (150,0) same geometry, ninside=1.3; both outside n=1; finite M1 mirror at (300,0), tangent +90°, length 400; detector D1 at (−100,0), tangent +90°, length 400; Fresnel off. The new contract requests per-lens actual face counts, mirror reflections and detector crossings; no path is supplied.

New `test/native-two-thick-lens-mirror-v17.test.mjs` includes native 11-event return and independent local face Snell geometry, authentic missed finite mirror, object-list reversal, off-axis ray, independent two-source scene, cm/mm authored units, version-sensitive policies, old v15/v16 saved depth rejection, geometry/material/refusal controls, stale-scene/qualified export, explicit preview depth-8 incompleteness and full-Fresnel truncation. The new `scripts/native-two-thick-lens-mirror-browser.mjs` must exercise actual Chrome edits to both lenses/mirror, return/miss, invalid overlap with stale-result withholding, qualified export/reopen, ray miss, and UI disclosure of depth 16. Historic UI source hash provenance is appended as a separate v17 file rather than revising original frozen evidence.

**At the time of this request, the final candidate CI must be separately verified.** An initial source HEAD had failed historical negative tests that assumed newly authorable v17 apparatus must still be rejected; they were updated to verify **new authoring is v17-allowed while historical saved v15/v16 formats are still forbidden**, without editing the previously reviewed production code or old golden inputs. Another v17 test explicitly supplying the v17-only policy while choosing a v15/v16 model was corrected to require refusal until the deep policy is removed. All initial failed runs must stay visible, and the reviewer must examine final exact-head CI rather than count a previous successful run.

Adversarial review should inspect 0.009/0.011-mm geometry gaps, two-source reflection/detector event merging, reverse rays, light entering between lenses, unexpected TIR/rim corner re-hits, non-air shared index, full Fresnel weak-branch cutoff at depth16, processed-ray/16-depth boundary and whether the simulator detects an incomplete run rather than invent a complete ray path. Success in a single fixture is not evidence of a universal minimum depth.

## Independent output required

A **separate-context Chat B** should write `physicsvigilante/review_sandbox/projects/opticsim/pr-116/reviews/review-01-chat-b.md`, identifying final reviewed source HEAD and tree, independent finite geometry/Snell/Fresnel calculations, actual source-CI pinned-native/Chrome metadata, severity-ranked findings, residual numerical/physical limitations and a clear verdict **CLEARED FOR OWNER DECISION**, **INSUFFICIENT EVIDENCE**, or **CHANGES REQUESTED**. If the review environment lacks Node>=24.19 and the pinned native checkout, independently compute physical references and disclose source-CI-only native observations; do not claim an independent native execution. No human expert certification or textbook-answer completeness is implied.

**Do not merge PR #116 or its unreleased v14/v15/v16 dependencies. Independent review and distinct owner authorization are separate release gates.**
