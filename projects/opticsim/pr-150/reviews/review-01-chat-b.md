# Independent R1 — Opticsim PR #150: source-position / observer-position planar refraction

**Review date:** 2026-11-18  
**Reviewer:** Chat B (independent GitHub object/source inspection, CI log verification, separately implemented Python binary64 reference and 80-digit mpmath scalar calculations).  
**Verdict: CLEARED FOR OWNER DECISION.** No P0 or P1 defect found in the **stated narrow, conditional, analytical-only v1 contract**. This is **not** a native observer-hit accuracy certificate, PhyDemo rerun, release approval, merge authorization, or retroactive clearance of held PRs. PR #150 remains draft/unmerged and requires a separate owner decision.

## 1. Exact identity, ancestry, scope — verified from Git objects

| Item | Independent observation |
|---|---|
| [Opticsim PR #150](https://github.com/physicsvigilante/opticsim/pull/150) | Open, draft, unmerged at review |
| Source HEAD | `0fb738f69b3257113c73dbf9d1f2917037daa5cc` |
| Source tree | `8cd6b5df7cceaf68d04deca4926eb91245986216` |
| True production main base | `d3509e82fb65d81aabe336666851f8f2962623f4` |
| Base tree | `45ff3bcd9093a527652f13f76c3cc0b02826642f` |
| Synthetic CI merge | `4ff6dd2ff4b8cf85a2ecc59c3836cca1df2ffcfc` |
| Synthetic merge tree | `8cd6b5df7cceaf68d04deca4926eb91245986216` — matches source |
| Synthetic merge ordered parents | `[d3509e82fb65d81aabe336666851f8f2962623f4, 0fb738f69b3257113c73dbf9d1f2917037daa5cc]` |
| Compare production main → PR HEAD | 5 ahead, 0 behind; merge-base is production main |

Verified using actual [source Git commit object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/0fb738f69b3257113c73dbf9d1f2917037daa5cc), [synthetic merge Git commit object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/4ff6dd2ff4b8cf85a2ecc59c3836cca1df2ffcfc), [source tree](https://api.github.com/repos/physicsvigilante/opticsim/git/trees/8cd6b5df7cceaf68d04deca4926eb91245986216?recursive=1) and GitHub compare, not simply the PR description. Recursive tree response was not truncated. Exactly **four additions; no modified/deleted existing file**:

- `src/planar-observer-point-query.js` (blob `19697ec4223a08dbb4b334d84ff164b745ff2c1c`), 188 lines.
- `scripts/planar-observer-point-query.mjs` (blob `0456ae2e7b8125dcc30bd6879ffaa0d836c62339`), 68 lines.
- `test/jee-observer-point-query-v1.test.mjs` (blob `46d571c7f31d6f49b749101ddf5f0d700582f9ac`), 244 lines.
- `docs/JEE-OBSERVER-POINT-QUERY-V1.md` (blob `b4734f042d728ad0310eb93441a341717fdbe399`), 62 lines.

Read all four, plus relevant unchanged base versions of `src/planar-media.js`, `src/angular-math.js`, `src/observables.js`, `src/qualified-utils.js`, and `scripts/authoring-evidence.mjs`. The production native adapter, pinned PhyDemo, canonical schema and browser were not changed by this PR. Prior test-only #148 and held explicit-angle #144 are different gates.

## 2. Independently assessed physics

Let n be the oriented normal from the source side to observer side; t its counterclockwise tangent. Source and observer normal clearances `ds`, `do` are positive. The input admits only one infinite plane with a source on the negative side and observer on the positive side. Let `span = uo - us` and let `v` be the source-foot-to-crossing tangent displacement. The implemented equation is:

    F(v) = ns*v/hypot(ds,v) - no*(span-v)/hypot(do,span-v) = 0.

With strictly positive `ds`, `do`, `ns`, `no`,

    F'(v) = ns*ds^2/(ds^2+v^2)^(3/2) + no*do^2/(do^2+(span-v)^2)^(3/2) > 0.

Thus the ordered bracket from 0 to `span` (reversed when `span<0`) has one ideal stationary transmitted path, with the source/observer normal signs handled correctly. It is an endpoint-conditioned interface problem: not an arbitrary prescribed incident ray. A separate forward total-internal-reflection refusal is therefore not required for the ideal endpoint-conditioned solution, though physical TIR still applies in forward-angle problems.

Independently solved the example with 80-digit mpmath bisection and separate binary64 reference geometry, not by reading back asserted test constants:

| Case / computed observable | Independent result |
|---|---:|
| `S=(-60,0)`, `O=(100,40)`, plane x=0, 1.5→1: Q | `(0, 11.24615577120923)` mm |
| Incident / source heading | `+10.616108941304953°` |
| Refracted angle | `+16.041977708350927°` |
| Conditional backward-axis apparent depth | `39.11183381854949` mm |
| Separate paraxial depth | `40` mm |
| Observer tangent reflected to -40 mm | Q y=`-11.24615577120923` mm, signed angles reversed, same depth |
| Equal indices 1→1 | apparent depth = `60` mm |
| Reverse indices 1→1.5 | apparent depth = `92.53084858393252` mm |
| Rotations 90° / 180° | transformed world Q and direction; same apparent depth |

The finite-angle backward extrapolation intersects the source-normal axis at depth `v*do/(span-v)` and is **not** a demonstrated image. For exact axial `span=0`, the path and crossing are determined while **one ray cannot identify image depth**: null depth/point is correct, independently of the separately labelled 40-mm paraxial comparison. Rejecting very small nonzero axial tangent offsets as `NEAR_AXIAL_INFERENCE` is conservative and consistent with the published v1 contract.

## 3. Numerical refusals and physical/numerical distinction

Inspected [source lines 79–187](https://github.com/physicsvigilante/opticsim/blob/0fb738f69b3257113c73dbf9d1f2917037daa5cc/src/planar-observer-point-query.js#L79-L187) and [tests 47–180](https://github.com/physicsvigilante/opticsim/blob/0fb738f69b3257113c73dbf9d1f2917037daa5cc/test/jee-observer-point-query-v1.test.mjs#L47-L180). Verified the admission order: bounded input; 110-iteration **local v** bisection; local residual; reconstructed Q and separate world Snell residual; ingress and exit cosine cutoff; exact-axial/near-axial distinction; representable apparent point; conditional payload only after these gates.

Independent *Python binary64 arithmetic with analogous operation ordering* reproduces the intended negative-control classes; these are not claims of direct execution of the checked-in JavaScript:

| Case | Independent reference observation | Expected implemented refusal |
|---|---|---|
| y≈9000, `S=(-.02,9000), O=(.02,9000.01)`, 1.5→1, plane x=0 | local Snell residual ≈ `5.55e-17`; reconstructed-world residual ≈ `-4.15e-11` | `WORLD_COORDINATE_ROUNDING` |
| #146 R2 ingress geometry, normal 135°, 1→2 | incoming normal cosine ≈ `3.70747e-7`; represented-world residual ≈ `3.46e-14` | `NEAR_GRAZING_INGRESS` |
| Mirrored negative tangent of previous case | incoming normal cosine ≈ `3.70747e-7`; represented-world residual ≈ `-1.59e-14` | `NEAR_GRAZING_INGRESS` |
| `S=(-60,0), O=(100,9000)`, normal 0°, 1.5→1 | outgoing normal cosine ≈ `0.01117705665` | `NEAR_GRAZING_EXIT` |

The known R2 incoming-grazing failure is now covered on **both** tangent signs; high-world-coordinate cancellation withholds rather than invents Q/heading; the two normal-cosine guards are separate. `0.02` is an **arbitrary conservative numerical admission rule**, not a physical critical-angle threshold, and the local/world residual tests are **not a rigorous native forward-ray positional error bound**. The [docs](https://github.com/physicsvigilante/opticsim/blob/0fb738f69b3257113c73dbf9d1f2917037daa5cc/docs/JEE-OBSERVER-POINT-QUERY-V1.md) and result limitations state this explicitly. No overclaim of achieved native arrival was found in the public contract.

Coordinate units, closed fields, finite input, ±10000-mm coordinates after conversion, opposite-side 0.01-mm clearance, [1,4] indices, and [-180,180] normal angle are checked explicitly. An invalid request throws (CLI rejects), while valid but numerically unqualified input returns `numerically-unstable` with `value:null`. Conditional calculations do not silently reverse the normal or material indices.

## 4. Native and CLI provenance boundary

- [Source result](https://github.com/physicsvigilante/opticsim/blob/0fb738f69b3257113c73dbf9d1f2917037daa5cc/src/planar-observer-point-query.js#L42-L59) always states `native.status:'not-run'`, `observations:null`, `nativeImageDetected:false` and an unassessed source-question interpretation. The returned Q is a **predicted mathematical interface crossing**, not native interface `pointMm`; the apparent point is not an observed image.
- [CLI implementation](https://github.com/physicsvigilante/opticsim/blob/0fb738f69b3257113c73dbf9d1f2917037daa5cc/scripts/planar-observer-point-query.mjs#L14-L64) hashes original JSON bytes, records exact preserved input and uses fresh exclusive output. It never authors native brightness, Fresnel assumptions, a detector, or a scene. Invalid JSON/shape yields rejection with no analytical result. The pre-existing evidence helper prevents ordinary overwrite/symlink ancestor escape, while expressly **not** claiming tamper-proof storage.
- The [test-only native cross-check](https://github.com/physicsvigilante/opticsim/blob/0fb738f69b3257113c73dbf9d1f2917037daa5cc/test/jee-observer-point-query-v1.test.mjs#L182-L223) separately authors full canonical v5 scenes with one explicit single ray, a planar interface, Fresnel-off `partialReflection:false`, and a finite detector. It checks actual moderate-angle native detector hit location/direction, first interface transmission and a Fresnel-omission warning. This evidence cannot be attributed to the public analytical query or generalized to all bounded inputs.
- Inspected unchanged `src/observables.js`: completed, hash-matched, execution-passed native evidence gates the readings; stale/incomplete results suppress measurements. The new regressions cover both refusals. Single-ray isolation is **not** general multi-source optical ancestry.

## 5. CI provenance — builder execution, independently verified logs

GitHub Actions API for the exact PR HEAD returns **11/11 workflow conclusions SUCCESS**, all `pull_request` on SHA `0fb738f69b3257113c73dbf9d1f2917037daa5cc`. These include [Optical composition #44300152212](https://github.com/physicsvigilante/opticsim/actions/runs/44300152212) and [Planar angular #44300152211](https://github.com/physicsvigilante/opticsim/actions/runs/44300152211). Read native job lists and decoded logs, not just the PR status summary.

Specifically, [planar-angular job 134787468431](https://github.com/physicsvigilante/opticsim/actions/runs/44300152211/job/134787468431) prints **`tests 800`, `pass 800`, `fail 0`, `skipped 0`** and named source-observer cases including real **test-only** native observer reach, strict query, and CLI evidence tests. Optical-composition job **134787468547** also runs Node tests, build and separately named browser/native acceptance steps successfully. Source and synthetic merge trees match by inspected Git objects.

**Provenance limit:** These are **builder CI runs**, not my independent Node / PhyDemo / Chrome execution. My separate work was read-only Git object/source inspection and independent scalar/reference numerical computation. I did not execute PhyDemo, Chrome, install dependencies or modify Opticsim.

## 6. Severity findings and recommended follow-up

**P0: none found. P1: none found within the documented analytical-only contract.** The previously identified incoming-grazing failure is suppressed. No mathematical sign, Snell-root, index-orientation, false native-source attribution, stale-observation or rejected-input defect was identified in the inspected changes.

**NB-1 — Forward-ray arrival remains an uncertified property (nonblocking only under the present honest labeling).** Local and reconstructed-world Snell residual checks plus two `0.02` normal-cosine guards do **not** prove that a rounded degree heading, converted into an independently authored native scene, will meet a given observer-position tolerance for every admitted bounded geometry. Preserve the *predicted/conditional* wording, `native:not-run`, and the current absence of promised achieved hits. If future UI/API claims verified arrival, make a separately qualified forward propagation/positional-error or actual native-hit check a **new required gate** rather than extending this R1 conclusion.

**NB-2 — Separate ray solvability from axis-inference withholding in a future version.** Very near but nonzero axial spans or out-of-domain axis intercepts currently withhold the entire result, including an otherwise potentially useful ray prediction. This is conservative and explicitly documented, not a blocker. A future typed per-field status could make pedagogical display more informative without inventing an apparent depth.

**NB-3 — Expand independent native coverage before a stronger guarantee.** The actual native comparison covers ±40-mm moderate-angle examples, not near-boundary/oblique-normal/wide-world-coordinate/near-grazing observer hits. Add oblique rotated normals, asymmetric signed spans, property-based floating cases, and optional per-case native detector-hit distance evidence if expanding the contract. Tests already guard the critical scalar counterexamples; broad native accuracy should not be inferred from them.

**NB-4 — Evidence integrity is appropriately bounded.** SHA-256 and exclusive writes check ordinary original-byte identity/non-overwrite, not adversarial immutability. Keep this qualification in publication material and never call it tamper-proof.

## 7. Final disposition

**CLEARED FOR OWNER DECISION** on the exact SHA/tree above, as a self-contained, explicitly limited analytical JEE observer-position query. No requested P0/P1 source correction blocks the *scoped R1 gate*. This verdict is conditional on retaining the present public distinctions: `conditional` mathematical prediction ≠ native achieved hit; apparent-axis extrapolation ≠ physical image; valid but numerically withheld ≠ invalid authored geometry; test-only native cross-check ≠ production native integration.

**Do not merge or release on the strength of this review alone.** Leave PR #150 draft/unmerged pending separate owner judgment; do not treat #148 test-only clearance, #144 explicit-angle review, other held PRs, or branch-protection issue #123 as resolved by this finding.
