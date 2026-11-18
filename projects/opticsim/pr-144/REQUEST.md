# Independent R1 review request — Opticsim PR #144, typed planar apparent-depth query v1

**NEW STANDALONE ENGINE CODE. DRAFT; DO NOT MERGE.** This is NOT a continuation of the test-only research review for PR #143, and prior approval cannot clear this new source. Review exact source physics, hard validation and evidence provenance before any release decision.

## Exact tree and ancestry (verify via Git objects)

- [PR #144](https://github.com/physicsvigilante/opticsim/pull/144), draft, main-based.
- Head: `aea25a9b480260e2498229d80f7f6cbe3d4ac574`.
- Source Git tree: `e1fe378b7070ef6be53f34faa798e75774f877a5`.
- True base production main: `d3509e82fb65d81aabe336666851f8f2962623f4`.
- Exact source-CI synthetic merge: `186141dae6c56ae631be4b9e3e0839f6db0a5653`, same tree `e1fe378b7070ef6be53f34faa798e75774f877a5`, parents main and HEAD. Check commit objects, do not rely on status badge.
- Four added files; **no** changes to existing canonical scene schema, PhyDemo pin or vendor, native adapter, existing v1–v13 authoring/observables, browser or held v14–v19 branches:
  1. `src/planar-apparent-depth-query.js` — new exported typed calculation.
  2. `scripts/planar-apparent-depth-query.mjs` — new JSON CLI with original-input SHA256 preservation.
  3. `test/jee-apparent-depth-query-v1.test.mjs` — analytical and actual native *test-only* regression.
  4. `docs/JEE-PLANAR-APPARENT-DEPTH-QUERY-V1.md` — complete bounded contract.

## Prior reviewed evidence, but not source approval

[Chat B review of research PR #143](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-143/reviews/review-01-chat-b.md) independently cleared the **test-only native feasibility**, finding the real native hit positions and refracted directions consistent with exact finite-angle Snell law. Reviewer recommended a distinct typed contract, conservative fail-closed numerical statuses, strict provenance boundaries and no native image claim. PR #144 is a **new code path** and requires its own independent inspection.

## Authored query and physics

Exactly this minimal JSON is supported; arbitrary scene data, implied material indices, reflection settings and detector/observer positions cannot be silently assumed:

```json
{
  "format": "opticsim-planar-apparent-depth-query-v1",
  "lengthUnit": "mm",
  "source": {"x": -60, "y": 0},
  "interface": {
    "x": 0, "y": 0, "normalDeg": 0,
    "sourceIndex": 1.5, "observerIndex": 1
  },
  "observation": {"kind": "finite-incidence-angle", "incidentAngleDeg": 5}
}
```

The explicit normal points from the source negative medium to observer positive medium. World is x-right/y-up. `incidentAngleDeg` is **signed angle from the normal on the source side**, not an observer location inferred from a diagram. Exact one-plane ideal model: source depth `d=-dot(source-planePoint,n)>0`; angle `r=asin(ns/no * sin(i))` for a physically propagating transmitted ray; source-normal interface foot `F`; ideal crossing `Q=F+d tan(i)t`, with CCW tangent `t`. The conditional axis intercept is `A=F-d_app*n`, `d_app=d tan|i|/tan|r| = d(no/ns)cos(r)/cos(i)`. It is **not a real virtual image detection**, and the source/plane normal must be fully stated.

Output `status:'conditional', resultKind:'conditional-axis-intercept'` with apparent depth, axis-intercept point, predicted crossing, signed angles and separately named paraxial limit. A separate explicit `observation:{kind:'paraxial-limit'}` yields `d_paraxial=d(no/ns)` with `resultKind:'paraxial-limit'`, not inferred from one axial ray. For `i=0`, single-ray result is `not-identifiable` with `value:null`; `0<|i|<1e-6°` or near input grazing returns `numerically-unstable`. Shared `classifySnellTransmission` conservative `2e-12` ratio band is used for near-critical ambiguity; definite TIR returns `TIR-no-transmission` and no value. An out-of-domain mathematical projection also withholds output.

Indices [1,4]; mm/cm/m converted to mm and both authored points within ±10000 mm. Source must be at least 0.01 mm on **negative** side; opposite source side/unknown normal is rejected, not silently reversed. Extra keys, missing indices or angle, nonfinite data and contradictory paraxial/finite options reject before computing a value.

**No hidden native simulation:** the CLI and calculation always report `native:{status:'not-run',observations:null,nativeImageDetected:false}`. No native rays, source brightness, Fresnel settings, ray pairing or observer position are invented. Native-hit-unavailable/incomplete-or-stale statuses are deliberately excluded from a v1 function which never runs the native simulator. In *tests only*, independently authored complete v5 PhyDemo scenes with explicit brightness/partialReflection:false verify real hit positions and interface vectors, and stale/incomplete native results are suppressed using the existing native evaluator.

## Builder CI (not independent rerun)

- **11/11 standard workflows SUCCESS** at exact source head via tree-identical synthetic PR merge.
- Optical composition [run #44277301999](https://github.com/physicsvigilante/opticsim/actions/runs/44277301999) plus planar-angular [run #44277302418](https://github.com/physicsvigilante/opticsim/actions/runs/44277302418).
- **800/800 Node tests** on this source, including 10 new named tests for finite-angle, signed symmetry, rotation/translation, units, exact/near axis, critical/TIR, schema refusal, native hit method/approximation/provenance, stale/incomplete suppression and no-overwrite CLI evidence.
- Existing native/browser workflows passed. **This is builder-CI evidence, not independent PhyDemo or Chrome re-execution.**

## Reviewer checklist (independent analysis; source is untrusted)

1. Verify precise SHA/tree, main ancestry, no historical changed files, and actual CI logs.
2. Independently recalculate signed-plane geometry for 0°, 90°, 180° normals and lateral-offset source; exact/limit depths for 1.5→1 and 1→1.5, signed angles, and Snell critical/TIR. Check whether output could imply a unique real image or observer.
3. Audit malformed/unknown fields, source-side/order validation, unit scaling and 0.01-mm inclusive clearance, numerical bands, out-of-domain/near-grazing, equal-index physics, possible NaN/Infinity, and mutation/provenance of inputs.
4. Inspect CLI: original bytes/hash, independent output paths, rejection state, no falsely labelled native observation, and bounded filesystem writes. Verify any exposure of a qualified PhyDemo scene or native execution would require additional explicit data.
5. Read actual test assertions and native log provenance: narrow single-source/one-ray controls must not be promoted to full parentage attribution or reconstructed observer/image claims. Check stale/incomplete and approximated Fresnel warnings.
6. Rank real errors P0/P1, other nonblocking notes and decide **CLEARED FOR OWNER DECISION / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** on this new code. If clear, keep new source draft until owner separately authorizes a release; note potential later integration with reviewed but held v14–v19 and branch-protection issue #123.

Publish `projects/opticsim/pr-144/reviews/review-01-chat-b.md` with exact source identity, independent numerical checks, evidence limits and one verdict. **Do not modify Opticsim source, approve a pull request as a builder, merge, alter old reviews or claim release.**
