# Opticsim PR #151 — independent R1 review request: real native sampled-arrival witness

**NEW SOURCE / DO NOT MERGE.** This review covers an optional physically specified native verification workflow for a separately, independently reviewed *conditional analytical* observer-position query. A native sample reaching a finite detector is **not** a real eye, perceived image, native inverse ray search, general route, continuous irradiance or unsampled accuracy certificate. Do not inherit review clearance of the parent feature automatically.

## Exact source scope and identity

- [Draft Opticsim PR #151](https://github.com/physicsvigilante/opticsim/pull/151), base exactly the **frozen, independently reviewed PR #150 source head** `0fb738f69b3257113c73dbf9d1f2917037daa5cc`.
- Candidate HEAD **`e078f1208b40514ed7d5f853b1c7520e36341431`**, source Git tree **`cb4e3d41e4e9a60ac8ee9027ffae58049c1a5d1c`**.
- Temporary [CI-only PR #152](https://github.com/physicsvigilante/opticsim/pull/152) is main-target solely to trigger standard workflows. Its synthetic merge **`c619a5c2defa0b401e7641026062d9b34ae36934`** has an **identical Git tree** `cb4e3d41e4e9a60ac8ee9027ffae58049c1a5d1c` and parents [production main `d3509e82fb65d81aabe336666851f8f2962623f4`, exact candidate HEAD]. Verify both Git commit objects rather than relying on green checks. Close #152 **unmerged** after evidence; never treat it as a production release proposal.
- Diff against frozen #150 is four additions only: `scripts/jee-observer-native-witness.mjs`, `test/jee-observer-native-witness-v1.test.mjs`, `examples/jee-observer-native-witness-v1.json`, `docs/JEE-OBSERVER-NATIVE-WITNESS-V1.md`. No modification to existing `src/`, pinned PhyDemo, canonical scene schema, adapter, browser or original reviewed #150 source.
- [Chat B's #150 R1 review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-150/reviews/review-01-chat-b.md) cleared only the separate analytical conditional result, explicitly noting that native actual arrival needed another evidence gate. This PR **is** that new gate and must be independently assessed.

## What a user must explicitly author

The request format is `opticsim-observer-native-witness-v1` with two strict parts. [Concrete example](https://github.com/physicsvigilante/opticsim/blob/e078f1208b40514ed7d5f853b1c7520e36341431/examples/jee-observer-native-witness-v1.json).

- `analyticalQuery`: the unchanged reviewed typed one-plane source-position / observer-position geometry, explicit source S, observer O, plane P+normal from source to observer side, indices and mm/cm/m unit. This analytical result always has `native.status:not-run`.
- `physicalVerification`: source brightness in [0.01,1], explicit native `partialReflection` boolean, chosen versioned numerical `runPolicy` preview-v1 or dense-v1, detector alignment `tangent-to-interface` and finite `lengthMm` [1,200], explicit Euclidean `arrivalToleranceMm` [1e-7,1], and chosen dimensionless unit-vector `directionTolerance` [1e-9,1e-3]. The detector center O and tangent alignment convention are declared, not an eye or an unrequested observer artifact. The runPolicy's specific sampling, depth and processed-ray limit are retained from existing canonical policy.

The tool must **reject** missing/invalid physics rather than silently selecting brightness, Fresnel-off, detector, numerical limits or a ray route. The existing analytical query must succeed conditionally **before any native scene is authored**. When `numerically-unstable` (the prior y≈9000 world-rounding or 135-degree ingress-grazing counterexamples), there must be no native ray and no scene. A canonical v5 refusal (e.g. finite detector endpoints beyond coordinate bounds) remains `physical-scene-refused`, not a fabricated native run.

## Native propagation and evidence contract

The runner then creates an explicit, fully valid canonical v5 scene of:
1. One real `point-source` with `single-ray` direction from the conditional analytical calculation, explicit source brightness and the declared S.
2. One native `PlaneGlass` at the author's infinite boundary with exactly stated indices and `partialReflection` policy.
3. One passive finite `Detector` at the declared O, tangent to the plane, explicit full length.

The native PhyDemo solver freely propagates the ray. The analytical predicted interface crossing **is not** given to native as a forced path, and the adapter's planar event does not expose a directly observed interface `pointMm`. This does **not** mean PhyDemo discovered the inverse shooting direction.

The runner requests exactly these regular canonical observables: `source-emissions`, `interface-interactions`, `interface-first-event`, `detector-crossings`, and opt-in `detector-hit-events`. It requires complete/successful native execution, exact canonical scene SHA match with qualified readings, one native emitted ray, one interface incident/transmitted event with correctly declared index orientation, one complete count-matched native detector crossing, methods `native-observation` and `native-hit-event-observation`, matching first native refracted direction, and actual hit coordinates and incoming direction.

The result `verified-sampled-arrival` is allowed **only** for the measured hit whose Euclidean position error to O is within the **author-selected** `arrivalToleranceMm`, both actual transmitted-branch/native detector incoming-direction and analytic direction mismatch are within declared `directionTolerance`, and native incident/refraction angle error <=1e-5 degrees. Report actual native hit coordinates, error magnitudes, methods, Fresnel warnings and selected tolerances. This result is evidence about **one sampled native ray**, not a universal guarantee about any other geometry, human perception, continuous light or image formation.

Inspect status handling carefully: `analysis-unqualified`, `physical-scene-refused`, `native-incomplete`, `native-evidence-unavailable`, `native-error`, `native-infrastructure-error`, and `measured-miss` must not leak measured values when native evidence is absent or stale. A complete run with **zero genuine crossings** needs honest wording distinct from absence of evidence; check whether the current generic `native-evidence-unavailable` label is sufficient or merits a correction. Also scrutinize whether `verified-sampled-arrival` can be inferred from a fabricated or stale result without qualified native provenance, whether event-count and ray isolation actually establish the intended narrow source-to-hit relation, and whether any test-only executor injection affects production output.

## Builder evidence and independent physical checks

- Optical/native/browser [run #44305042852](https://github.com/physicsvigilante/opticsim/actions/runs/44305042852) is at candidate head; job `134804300861` completed SUCCESS, with **809/809 Node tests**, including new real-native and negative tests.
- The logged `JEE_OBSERVER_NATIVE_WITNESS` reports **real pinned PhyDemo** completed, actual native detector hit `(100.00000000000001,40)` mm for analytical S=(-60,0)→O=(100,40), indices 1.5→1 and declared 20-mm detector, arrival error `1.4210854715202004e-14 mm`, `nativeImageDetected:false`.
- New tests cover mirrored y=±40 true native crossings; the exact old 135-degree grazing and y≈9000 world-rounding controls refusing native authoring; invalid finite detector geometry; old stale SHA and deliberately incomplete depth-0 suppression; injected infrastructure faults; input rejection/hash/no-overwrite and Fresnel-off warning retention.
- GitHub Actions standard workflow suite may complete after the source review request was drafted. **Review every final workflow status** and the exact source/merge tree; no 11/11 claim is accepted until all results are verified. The builder native-run evidence is **not reviewer-independent PhyDemo or Chrome execution**.

## Requested independent reviewer verdict

Independently inspect all four new files and relevant unchanged authoring/contract/observables/adapter + pinned simulator source behavior. Recompute the target Snell geometry and actual recorded hit from the decoded CI log; verify metadata, numerical policy, completeness and hash gates, method provenance, rejection behavior, and the distinction between actual native observer-centered detector hit versus mathematical image/crossing. Challenge the zero-hit case, native warnings and user-selected tolerance semantics.

Publish independent findings at **`projects/opticsim/pr-151/reviews/review-01-chat-b.md`** with exact SHA/tree, evidence provenance, P0/P1/nonblocking issues, and verdict **CLEARED FOR OWNER DECISION / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. Do not alter PR #150 source, merge any PR, assert universal native reachability or release. Production main, held PRs #141/#143/#144/#148/#150, historical changes-requested #145/#146, and branch-protection issue #123 retain independent gates.
