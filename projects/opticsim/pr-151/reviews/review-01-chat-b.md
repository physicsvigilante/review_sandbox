# Independent R1 — Opticsim PR #151: native sampled-arrival witness

**Review date:** 18 November 2026  
**Reviewer:** Chat B — independent read-only GitHub source/commit/CI-log inspection and separate 75-digit mpmath Snell calculation.  
**Verdict: CHANGES REQUESTED.** One **P1 result-truthfulness defect** was identified for a *completed native zero-crossing*. **P0: none identified.** This is not a finding of fabricated positive arrivals. The exact candidate remains **DRAFT / DO NOT MERGE**, independently of the reviewed/unmerged parent #150. No production release is authorized.

## 1. Exact source identity, ancestry and scope

| Check | Independently verified evidence |
| --- | --- |
| Source PR | [Opticsim #151](https://github.com/physicsvigilante/opticsim/pull/151), open/draft/unmerged |
| Exact candidate HEAD | `e078f1208b40514ed7d5f853b1c7520e36341431` |
| Source Git tree | `cb4e3d41e4e9a60ac8ee9027ffae58049c1a5d1c` |
| Actual comparison base | PR #150 HEAD `0fb738f69b3257113c73dbf9d1f2917037daa5cc` |
| Git comparison | Five commits ahead, zero behind, merge base exactly #150 HEAD; four added files, 591 additions, zero existing-file edits |
| Production main at evidence checkpoint | `d3509e82fb65d81aabe336666851f8f2962623f4` — separate and unmodified |
| CI-only PR | [#152](https://github.com/physicsvigilante/opticsim/pull/152), **closed unmerged**, not a production integration candidate |
| Synthetic CI merge | `c619a5c2defa0b401e7641026062d9b34ae36934` |
| Synthetic Git tree | `cb4e3d41e4e9a60ac8ee9027ffae58049c1a5d1c`, **byte-identical Git tree to candidate HEAD** |
| Ordered synthetic parents | [`d3509e82fb65d81aabe336666851f8f2962623f4`, `e078f1208b40514ed7d5f853b1c7520e36341431`] |

The [candidate Git commit object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/e078f1208b40514ed7d5f853b1c7520e36341431), [synthetic merge Git commit object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/c619a5c2defa0b401e7641026062d9b34ae36934), PR metadata and GitHub compare were inspected, not inferred from the PR description. The exact HEAD was reconfirmed before writing this review.

Four new files read completely:

1. [scripts/jee-observer-native-witness.mjs](https://github.com/physicsvigilante/opticsim/blob/e078f1208b40514ed7d5f853b1c7520e36341431/scripts/jee-observer-native-witness.mjs) — 305 lines.
2. [test/jee-observer-native-witness-v1.test.mjs](https://github.com/physicsvigilante/opticsim/blob/e078f1208b40514ed7d5f853b1c7520e36341431/test/jee-observer-native-witness-v1.test.mjs) — 207 lines.
3. [examples/jee-observer-native-witness-v1.json](https://github.com/physicsvigilante/opticsim/blob/e078f1208b40514ed7d5f853b1c7520e36341431/examples/jee-observer-native-witness-v1.json) — 28 lines.
4. [docs/JEE-OBSERVER-NATIVE-WITNESS-V1.md](https://github.com/physicsvigilante/opticsim/blob/e078f1208b40514ed7d5f853b1c7520e36341431/docs/JEE-OBSERVER-NATIVE-WITNESS-V1.md) — 51 lines.

Relevant unchanged source was also inspected: analytical source-position query; canonical scene/authoring/validation; planar normal/media adapter; detector callback capture and limits; native observation projection, scene hashing and completed-run gating; native checker; evidence directory helper. The existing `src/`, pinned native PhyDemo, canonical schema and browser were **not edited by #151**.

## 2. Independent physics calculation

For the published sample, source S = (−60,0) mm, observer O = (100,40) mm, plane x = 0, normal toward +x, source medium n₁ = 1.5 and observer medium n₂ = 1, let v be the y-coordinate of the first crossing. Fermat/Snell requires

```text
1.5*v / sqrt(60^2 + v^2) = (40 - v) / sqrt(100^2 + (40 - v)^2).
```

Separately solving this scalar equation with **75-digit mpmath** (not copying the checked-in test constants) gives:

| Observable | Independent result |
| --- | ---: |
| Predicted **mathematical** plane crossing Q | (0, 11.2461557712092301) mm |
| Incident/source heading | +10.616108941304953° |
| Transmitted/refracted angle | +16.041977708350928° |
| Expected transmitted unit vector | (0.9610594924712145, 0.2763415494111802) |
| Conditional backward-axis depth | 39.1118338185494934 mm |
| Separate paraxial depth | 40 mm |

The native CI log reports **one real detector hit** at (100.00000000000001, 40) mm and Euclidean distance to O of `1.4210854715202004e-14` mm, exactly consistent with arithmetic on the logged coordinate. This is an *actual reported native detector coordinate*; the predicted Q is **not** a native observed interface-hit coordinate. The log does not print a full raw first-event record with numeric measured angles: those gate conditions were verified in source and exercised by the success regression, **not separately remeasured by this reviewer**. I did not independently run the pinned PhyDemo simulator.

The canonical scene comprises exactly one native SingleRay at the analytically proposed heading, one PlaneGlass with source-side/observer-side indices and explicit Fresnel policy, and one finite passive Detector tangent to the plane at the stated observer coordinate. The plane compiler's native positive-normal index ratio and coordinate/sign conversions are consistent with the analytical orientation. Native propagation is *forward* and the detector event is obtained from the native callback, not from the analytical Q. **The feature is not an inverse native ray solver, source-ancestry certificate, eye, retinal model, image or continuous irradiation test.**

## 3. Source and qualification review

- **Input closure and physics:** Required closed top-level and physicalVerification records; explicit brightness [0.01,1], `partialReflection` boolean, one of two named run policies, finite tangent detector of 1–200 mm, position tolerance [1e−7,1] mm, unit-vector direction tolerance [1e−9,1e−3]. The unchanged analytical query strictly checks source/observer, length units, indices, oriented plane and numerical admission. No unrequested eye, source brightness or Fresnel choice is supplied. The inactive single-ray cone angle and camera are presentation/inactive defaults, not silently filled active optical facts.
- **Scene validation:** `prepareScene` creates an actual canonical v5 document and enforces finite detector endpoints, point-source clearance, component counts and whole-medium detector placement. Refused analytical/numerical cases create no native scene; canonical physical geometry errors become `physical-scene-refused`.
- **Native integrity:** [evaluateDocument](https://github.com/physicsvigilante/opticsim/blob/e078f1208b40514ed7d5f853b1c7520e36341431/scripts/author-scene.mjs#L30-L56) produces a digest of serialized canonical scene and reports native completion/execution status. [evaluateObservables](https://github.com/physicsvigilante/opticsim/blob/e078f1208b40514ed7d5f853b1c7520e36341431/src/observables.js#L71-L98) independently recomputes the scene hash and withholds stale/partial/failed observations. The witness matches summary/observable SHA and completed execution before considering any hit. These are trustworthy *within the local successful runner's ordinary integrity model*, not tamperproof authentication.
- **Actual measurement methods:** Existing [detector adapter](https://github.com/physicsvigilante/opticsim/blob/e078f1208b40514ed7d5f853b1c7520e36341431/src/adapter.js#L134-L184) samples native ray/incident-point inputs **before** delegating the original `Detector.onRayIncident`, checks segment alignment and endpoint margin, and count-matches whole event lists (including genuine empty lists). Interface instrumentation [records native branches](https://github.com/physicsvigilante/opticsim/blob/e078f1208b40514ed7d5f853b1c7520e36341431/src/planar-media.js#L54-L108) without forcing refraction or adding a plane-hit point for PlaneGlass.
- **Positive-gate isolation:** The witness demands one source emission, one interface interaction, one transmission with correct stated indices, exactly one count-matched detector hit, first-event and hit native-method tags, close actual detector incoming versus native transmitted branch *and* predicted outgoing unit, close Euclidean hit to O, and independently fixed 1e−5° unsigned first-native-angle consistency. Its limited apparatus topology prevents inferring any general multi-source ray ancestry. No obvious positive promotion of stale/incomplete/zero-native or analytical-only records was found.
- **Warnings and numerical policy:** Explicit `partialReflection:false` is a transmitted-only approximation and the tested accepted hit carries the Fresnel-omission warning. The user chooses a versioned native sampling/depth policy; the witness does not secretly substitute numerical parameters. `completed-with-warnings` may qualify and the warning remains reported. Native `incomplete`, `stopped`, failed and hash-mismatched execution cannot qualify.
- **Evidence:** The original JSON bytes and SHA-256 are recorded first in a fresh exclusive-write directory. Analytical evidence is written before native preparation. Prepared scene bytes precede native execution; the final report separates analytical and actual native results. Setup failures preserve existing earlier evidence where file writes succeeded. These hashes/exclusive writes are **not** proof against malicious tampering or concurrent hostile processes. The optional `executeNative` function parameter is a test-only injected executor used for negative checks, not a JSON-specified public callback in the CLI.

## 4. P1 — Completed native zero crossing is misclassified as unavailable evidence (must fix)

**Location:** [witness source lines 112–155](https://github.com/physicsvigilante/opticsim/blob/e078f1208b40514ed7d5f853b1c7520e36341431/scripts/jee-observer-native-witness.mjs#L112-L155); compare [observables lines 142–175](https://github.com/physicsvigilante/opticsim/blob/e078f1208b40514ed7d5f853b1c7520e36341431/src/observables.js#L142-L175).

On a successfully completed, fresh native trace, the existing observation layer correctly represents `detector-crossings = 0` as an **available measured integer** and `detector-hit-events = []` as a **complete, available list**. The witness nevertheless requires `crossings.value===1` and `hits.value.length===1` to pass `countMatch`; every other count returns **`native-evidence-unavailable`** with reason `UNQUALIFIED_NATIVE_SAMPLE`. The code also requires an available `interface-first-event` *before* checking whether a genuine completed run missed the plane entirely.

Thus a physically meaningful completed native negative is conflated with absent/stale/incomplete instrumentation, even when actual counts are available. A complete zero crossing may be shown in `actualReadings`, but the public top-level result, reason and status contradict its provenance. This **does not fabricate a successful hit**; it is a negative-result truthfulness and classification defect in the new witness contract. The nine added tests lack a positive qualification test for the complete-zero case.

**Required correction before R1 clearance:**

1. On completed/fresh/qualified run measurements, recognize exactly one emitted ray and an **available zero crossing with a complete/count-matched empty hit list** as an explicitly observed **no-arrival** outcome (e.g. `native-observed-no-crossing`) with null accepted hit, **not** `native-evidence-unavailable`.
2. Handle both (a) one transmitted native interface event with zero detector crossings and (b) zero native interface interactions with zero detector crossings. In (b), the first-event observation is legitimately unavailable; it must not erase the independently available zero count.
3. Keep incomplete, failed, stale, absent, inconsistent or count-mismatched readings **unavailable/suppressed**. Do not manufacture a native trajectory or infer invisibility from a single missed detector. Differentiate zero emitted rays from a qualified emitted-ray miss.
4. Add deterministic complete/hash-matched zero-crossing regressions, plus stale/incomplete/invalid-counter negative controls. Prefer an additional genuine pinned-native missed-detector fixture if one can be admitted under this narrowly constrained geometry. Re-run all gates on the **new exact HEAD** for independent re-review.

## 5. Nonblocking findings / limitations

**NB-1 — Fixed-angle mismatch reason is misleading.** At [lines 169–178](https://github.com/physicsvigilante/opticsim/blob/e078f1208b40514ed7d5f853b1c7520e36341431/scripts/jee-observer-native-witness.mjs#L169-L178), a failure of the *fixed* 1e−5° native first-event concordance gate results in `measured-miss` / `DECLARED_TOLERANCE_NOT_MET`, even if both *user-declared* positional and directional tolerances passed. This safely withholds success but misstates the reason. Prefer a dedicated native-angular-inconsistency reason and a regression showing an angle-only failure.

**NB-2 — User-selected tolerance determines meaning.** An author can explicitly accept up to 1 mm positional and 1e−3 unit-vector directional mismatch. Hence `verified-sampled-arrival` is *only* within those printed choices, not proof of exact O arrival or a universal forward-error bound. The current source/docs largely state this honestly; keep tolerances prominent in UI/results.

**NB-3 — Expand new witness coverage.** The observed true-native positive case covers moderate-angle ±40 mm using explicit Fresnel-off. Add accepted rotated-normal, reverse-index, full-Fresnel, tight/loose tolerance and boundary-adjacent cases before any claim stronger than the narrow witness. Analytical grazing/world-rounding refusals are correctly covered, but do not themselves prove every numerically admitted forward native ray must hit a finite detector.

**NB-4 — Evidence authenticity limit.** Native event source/isolation is strong for the single source–plane–detector fixture but not a path history for a general apparatus. Hashes and exclusive writes establish ordinary local match/freshness, not hostile-process provenance. No broader claim should be made.

## 6. Builder CI evidence independently inspected

GitHub Actions API returned exactly **11 workflow runs** filtered by HEAD `e078f1208b40514ed7d5f853b1c7520e36341431`: **11/11 completed SUCCESS**. Names:

1. [Optical composition checks #44305042852](https://github.com/physicsvigilante/opticsim/actions/runs/44305042852)
2. [Planar refraction checks #44305042854](https://github.com/physicsvigilante/opticsim/actions/runs/44305042854)
3. [Curved mirror checks #44305042968](https://github.com/physicsvigilante/opticsim/actions/runs/44305042968)
4. [Deterministic planar angular query checks #44305043027](https://github.com/physicsvigilante/opticsim/actions/runs/44305043027)
5. [Original refraction problem pair #44305042956](https://github.com/physicsvigilante/opticsim/actions/runs/44305042956)
6. [Quasi-static source motion checks #44305043067](https://github.com/physicsvigilante/opticsim/actions/runs/44305043067)
7. [Plane-mirror angular inverse checks #44305042960](https://github.com/physicsvigilante/opticsim/actions/runs/44305042960)
8. [Parameter experiment checks #44305042922](https://github.com/physicsvigilante/opticsim/actions/runs/44305042922)
9. [Qualified authoring checks #44305042847](https://github.com/physicsvigilante/opticsim/actions/runs/44305042847)
10. [Unified problem workflow checks #44305042849](https://github.com/physicsvigilante/opticsim/actions/runs/44305042849)
11. [Numerical ray reliability diagnostics #44305042871](https://github.com/physicsvigilante/opticsim/actions/runs/44305042871)

The decoded [optical job 134804300861](https://github.com/physicsvigilante/opticsim/actions/runs/44305042852/job/134804300861) log independently shows checkout of CI merge `c619a5c2defa0b401e7641026062d9b34ae36934` (same Git tree), `tests 809`, `pass 809`, `fail 0`, `skipped 0`, `cancelled 0`, and `JEE_OBSERVER_NATIVE_WITNESS` with native `completed`, actual hit and residual stated above. Named cases include mirrored true native hits; grazing and world-coordinate refusals before scene authoring; detector bounds; incomplete native suppression; stale hash suppression; setup failure; strict closed inputs. Native/browser acceptance and artifact steps completed successfully.

I additionally inspected decoded logs for [numerical-reliability job 134804300465](https://github.com/physicsvigilante/opticsim/actions/runs/44305042871/job/134804300465) (809/809 Node tests, numerical report acceptance pass and native numerical replay acceptance PASS) and [planar-angular job 134804301263](https://github.com/physicsvigilante/opticsim/actions/runs/44305043027/job/134804301263) (809/809, angular analysis and browser provenance acceptance). These remain **builder CI executions**, not independent reviewer reruns of PhyDemo or Chromium. The CI synthetic source and candidate source are Git-tree-identical.

## 7. Final disposition

**P0: none found. P1: one (completed native zero is presented as unavailable native evidence).**  
**Final verdict: CHANGES REQUESTED** for the exact candidate HEAD/tree above. The positive sampled-arrival evidence is credible within its explicitly narrow physical and tolerance scope, but the completed-negative outcome contract must be corrected and tested. Nonblocking diagnostic and coverage improvements are separately listed.

This verdict is an independent new source review, **not inherited clearance** from PR #150 and **not a merge or release authorization**. Keep #151 draft/unmerged; the CI-only #152 is already closed unmerged. PR #150, other held PRs and branch-protection issue #123 remain separate. Re-review the resulting **new source SHA/tree** after any corrective commit. No Opticsim code, PR, review history, or release state was modified by this review.
