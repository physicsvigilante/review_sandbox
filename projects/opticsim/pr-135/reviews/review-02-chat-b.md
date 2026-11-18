# Chat B — second-pass independent physics review: Opticsim PR #135 (R2)

**Date:** 2026-11-18  
**Verdict: CLEARED FOR OWNER DECISION — RESEARCH ONLY.**

The R1 P1 preregistration blocker is corrected: the final test-only source contains **actual pinned-native paired equal-index tests for both 1.0→1.0 and 1.5→1.5**, with two separately emitted ±0.5° rays per medium configuration and measured 5 mm detector crossings. I recomputed the backintersections **from the archived native hit coordinates and outgoing unit vectors**, rather than accepting the analytical predictions or the postprocessor's reported depths. R1's mixed-order and warning-retention recommendations have also been addressed within the bounded research scope. All **11 final-source builder workflows completed successfully**; Node v24.19.0 records **802/802 passed**, including all 12 new B research tests. This clearance is solely for the owner to decide what to do with **research evidence**. **It authorizes no merge, production B feature, eye/pupil/physical image claim, or native accuracy certificate.**

## 1. Reviewed identity, scope, and preserved R1 evidence

| Item | Independently verified GitHub object / result |
| --- | --- |
| PR | [physicsvigilante/opticsim #135](https://github.com/physicsvigilante/opticsim/pull/135), still **open, draft, unmerged** at final recheck |
| Production baseline | `d3509e82fb65d81aabe336666851f8f2962623f4`, tree `45ff3bcd9093a527652f13f76c3cc0b02826642f` |
| **Reviewed R2 HEAD** | **`d6aff4e388aef982c3fc1b88039d4ac6951b4fca`** |
| **R2 HEAD Git tree** | **`afc157ed2976e937dbe9de942b05ffd205e6a083`** |
| Tested PR merge | `10b8b07e782626eff81f7bdbc5d9ec71ecf8bf44`; independently fetched Git object has **the same tree** `afc157ed2976e937dbe9de942b05ffd205e6a083` and parents `d3509e8...` + `d6aff4e...` |
| R2 HEAD's parent | Original R1-reviewed HEAD `58001725e8fd97cbfeb00ee9eaff705a864ecae5`, tree `ff0c6e46ea97b650c5e7e58680f180c458a437c1` |
| Diff against source baseline | Three commits ahead, zero behind; **exactly one added file**, `test/jee-finite-detector-window-feasibility.test.mjs`, **559 added lines, zero deleted**, blob `1a57c562bdf8eb00ebbc5e21569cc2cd179f9876` |
| R2 correction commit | One existing research test file changed; added equal-index tests, mixed-component-order pair and raw warning-retention test; no production optics, `src/`, scene/schema, native pin, browser UI, workflow or other tracked files |
| Native pin | `811f508d2b070898c241a568b0c167dcb8645251` in archived setup/build output and test document provenance |

I fetched and read the full 559-line final research test, its R2 commit diff, issue [#134](https://github.com/physicsvigilante/opticsim/issues/134), the [full R2 request](../REQUEST-02.md), and the preserved [Chat B R1 report](review-01-chat-b.md). GitHub's native job checkout log explicitly shows checkout of `10b8b07e...`; I independently compared the Git commit objects to ensure this checkout is tree-identical to the intended HEAD. I did not substitute the synthetic merge SHA for the authored HEAD.

The archived R1 report remains present (blob `dbca6f99f93fe310a61abc8122fc0259c0635fb5`), with its original **CHANGES REQUESTED** verdict and the original `58001725...` source identity. The earlier R1 CI evidence also remains queryable: **11/11 successful, one attempt each**, including [native run #44235111520](https://github.com/physicsvigilante/opticsim/actions/runs/44235111520) and [browser run #44235111578](https://github.com/physicsvigilante/opticsim/actions/runs/44235111578). R2 does not retroactively clear R1.

## 2. Actual native equal-index detector evidence and independent geometry

The actual final-source native log is from [workflow #44238752532, job #134581162269](https://github.com/physicsvigilante/opticsim/actions/runs/44238752532/job/134581162269). I retrieved and parsed the **379,045-character / 1,152-line** builder log, including **83 structured research entries**. The fixture is one v5 `S1` single-ray source at `(-120,0)` mm, one normal `I1` plane at `x=0`, and one **actual finite 5 mm** `D1` segment centered at `(40,0)` mm, y endpoints `[-2.5,+2.5]` mm. Each run separately emits `-0.5°` or `+0.5°`; `partialReflection:true`, `rayDensity:0.2`, `maxRayDepth:8`, `processedRayLimit:10000`. Each logged native result is `completed`, `executionPassed=true`, with zero truncation, undefined behavior, or warnings; **one emission, one interface interaction, one transmitted branch, and one native detector hit** per run.

| Native fixture | Negative scene SHA-256 | Positive scene SHA-256 |
| --- | --- | --- |
| 1.0→1.0 | `5477ab66fe9be029c58b9e4ea9a1b742bce3c5b2ddae5ca9e3793dd03544fb9d` | `92c926079ce9f7b5debf3a9e7cd31168cf923448c7220b83e466773f85c8e9f4` |
| 1.5→1.5 | `56e414615a95dbe41202f1cf2176a681be5dd5efc87dc5ebfb35cab38f75fb41` | `14d112cb0bf7764a145229e63ba13f3612d38c10310024d8e3d16baad7fe2dfb` |
| Original 1.5→1 | `4007c919f63cdbd4a1d0ff6f57ec5ac438fa6295eee4ac1f4bdca70d19e6ccf0` | `37fb3a4da5b1f87ecf794e3f148b07cbe7bc6351efb802f73da2b6bf351569f3` |

For **both equal-index pairs**, the archived native `detector-hit-events` data are:

- Negative: `p₋=(40,-1.396298846521404)` mm; `u₋=(0.9999619230641713,-0.008726535498373877)`; detector `distanceFromP1Mm=1.103701153478596`.
- Positive: `p₊=(40,+1.396298846521404)` mm; `u₊=(0.9999619230641713,+0.008726535498373877)`; `distanceFromP1Mm=3.896298846521404`.
- Both outgoing unit vectors match the **actual native transmitted first-event branch directions**; reported indices are genuinely `1→1` or `1.5→1.5` respectively. Actual transmitted relative power is 1, with **zero reflected branches**. Reflections were inspected, not assumed absent.

For independent reconstruction, I solved `p₋+s₋u₋ = p₊+s₊u₊` using these *logged* values, with determinant `u₋×u₊ = 0.017452406437283397`. This gives **`s₋=s₊=-160.00609254171871 mm`**, **`(x,y)=(-120.0000000000008, ≈0) mm`**, normal source-side depth **`120.0000000000008 mm`**. Minimum endpoint clearance is **`1.103701153478596 mm`** for each hit. The independent scalar reference `160·tan(0.5°)=1.3962988465214 mm` agrees, but was **never supplied to native propagation**. The tiny algebraic two-line residual is not an optics error estimate.

The retained **1.5→1 baseline** is also independently reconstructed from the archived hits:

- `p₋=(40,-1.5708611274685678)`, `p₊=(40,+1.5708611274685678)` mm.
- `u₋=(0.9999143248553549,-0.013089803247560816)`, `u₊=(0.9999143248553549,+0.013089803247560816)`; both exactly match native transmitted branches. Native outgoing angle `±0.7500118999902209°`, with one transmitted (relative power ≈0.96) **and one reflected** branch (relative power ≈0.04) per run; one detector hit each.
- Independent determinant `0.02617736355354841`; `s₋=s₊=-120.00647357027965 mm`; intersection **`(-79.99619199829817,0) mm`**, normal source-side depth **`79.99619199829817 mm`**; endpoint clearance **`0.9291388725314322 mm`**.

This independently verifies the physically expected **distinction between the no-index-contrast 120 mm control and the 1.5→1 ≈80 mm backprojection**. It is *only* geometric extrapolation of measured outgoing lines from **separate** native runs, not a native backward-propagated ray, observer, pupil, image formation or simultaneous view.

## 3. R1 correction disposition and remaining refusal behavior

**R1 F1 / P1: RESOLVED for this research gate.** The final test file executes both actual equal-index media, four separate ±0.5° native runs, with genuine 5 mm crossings, branch/hit-direction checks, finite-endpoint clearance, nonparallel backward intersections and correct source-side depths. The 12 new research tests all pass in pinned native builder CI. No solver path is manufactured.

**R1 F2 / P2: RESOLVED.** The new mixed-order test pairs native `S1,I1,D1` on the negative-angle run with `D1,I1,S1` on the positive-angle run. Its canonical SHA pair is `4007c919...` and `2b40920342cda7757f9e151f7f49c7ab338a82caf9dbad89cf4ca11b824e668e`; the test compares canonicalized **whole** physics+simulation with only explicit emission `directionDeg` removed and component order sorted. These are distinct native calls; both produce one true detector crossing and independently the ≈79.996192 mm intersection. Callback order does not establish source lineage.

**R1 F3 / P2: RESOLVED for valid paired-run native suppression and finite misses, with a stated synthetic limit.** `provenance()` now preserves each execution's `rawNativeWarnings` alongside each requested observable's status and warnings, with separate invocation label, canonical SHA and native status. `derivePair()` collects both valid pair records *before* returning `suppressed/null` on incomplete/stale execution or `unavailable/null` on a finite detector miss. The actual full native Fresnel-off runs are `completed` but their readouts are **`qualified`** with the per-run `omits Fresnel` caution. A valid two-hit pair remains **`qualified`**, not silently promoted to available. The actual shifted-window Fresnel-off miss has native crossing counts `[0,1]`, returns null/unavailable, and preserves both distinct qualified warning records.

The new *suppressed* warning test uses two actual `maxRayDepth=0` native incomplete results (their original raw native warning arrays are **empty**), then **clones and injects `SYNTHETIC_RESEARCH_WARNING_PROVENANCE_CONTROL`** into the first execution's metadata. The resulting passing assertion tests provenance plumbing with two suppressed records; this is **SYNTHETIC WARNING INJECTION FOR METADATA PIPELINE ONLY, NOT A WARNING EMITTED BY PHYDEMO**. There is no claim to have observed an organic warning on that incomplete run.

Other retained bounded controls in final source and builder logs: shortened detector `[0,0]`, shifted detector `[0,1]`, far-off detector `[0,0]`; reversed/rotated/transformed/cm/m scenes; mismatched source, indices, finite-window length and placement, Fresnel policy, numerical depth budget, extra plane, duplicate/single inputs, stale/missing opt-in capture; native TIR and near-critical finite-window misses; measured near-parallel rejection and synthetic antiparallel algebra control. Opt-in recording reports unchanged canonical hash and original native meter keys/values. No unobserved ray line is constructed.

## 4. Ranked findings and limitations

### P0 — No critical defect identified

No evidence of altered production optics, forged native crossing, wrong outgoing refraction sign, missing target tree/merge identity or failed final-source builder CI in this bounded review.

### P1 — No unresolved research-acceptance blocker

R1's specifically preregistered **equal-index native case** is now present and verified from actual event data. Research-only acceptance is complete for the declared #134 test matrix, subject to owner decision.

### P2 — Nonblocking evidence and production-admission boundaries

1. **Noncertifying conditioning remains the original F4 caveat.** `MIN_LINE_SINE=1e-4`, `MIN_ENDPOINT_CLEARANCE_MM=0.05`, and `MAX_EXTENSION_SCENE_RATIO=10` are explicit *test-local* heuristics. The logged ±`1e-4 mm` / ±`1e-6 rad` synthetic post-native perturbations shift the derived point at most `0.0015291726268600314 mm` in this fixture. Neither that value nor a near-zero algebraic line residual bounds native accuracy, detector-edge error or physical imaging uncertainty. A separately reviewed error and conditioning contract is required before any production B design.
2. **Warning-preservation guarantee is scoped.** Both records and warnings are retained for *in-scope, same-family pairs* reaching native readout inspection, including incomplete/stale and finite-window-miss nulls. Very early preflight refusals (duplicate input, wrong component scope, mismatched apparatus/scene hashes) return typed null reasons **before** building the per-run `evidence` array; their evidence can therefore be empty. The preregistered contract requires typed refusal there, not universal preservation of invalid-pair evidence. Do not generalize the new warning test into an all-refusals provenance guarantee.

### P3 — Interpretive and test hygiene notes

- The suppressed warning test labels its second run `complete-other`, but the source explicitly sets `maxRayDepth=0` for **both** runs and both native statuses are `incomplete`. Rename the label when next touching this test to avoid misreading the fixture; this is not a physics failure or research blocker.
- A 5 mm finite detector is **not a literal eye or pupil** and a two-line backintersection is not a uniquely localized perceived image. Native detector event lists do not imply continuous irradiance, simultaneous observation, full ray lineage, or scene-wide visibility.
- The scope does **not** license production observer/image/eye claims, public schema or authoring changes, browser UI additions, changes to held #133/#129, or release against main protection issue [#123](https://github.com/physicsvigilante/opticsim/issues/123). All require independent subsequent contracts, physical validation, native regression and owner approval.

## 5. Final-source builder CI and Chrome verification

I queried GitHub Actions run metadata **by the exact R2 authored head SHA**, retrieved final native and browser job-step statuses, and read the actual native and browser logs. Every one of the following **11 workflows** has `status=completed`, `conclusion=success`, `run_attempt=1`, `event=pull_request`, and `head_sha=d6aff4e...`:

| Workflow | GitHub run | Conclusion |
| --- | --- | --- |
| Plane-mirror angular inverse checks | [44238752532](https://github.com/physicsvigilante/opticsim/actions/runs/44238752532) | SUCCESS |
| Original refraction problem pair | [44238752589](https://github.com/physicsvigilante/opticsim/actions/runs/44238752589) | SUCCESS |
| Curved mirror checks | [44238752961](https://github.com/physicsvigilante/opticsim/actions/runs/44238752961) | SUCCESS |
| Parameter experiment checks | [44238752568](https://github.com/physicsvigilante/opticsim/actions/runs/44238752568) | SUCCESS |
| Numerical ray reliability diagnostics | [44238752579](https://github.com/physicsvigilante/opticsim/actions/runs/44238752579) | SUCCESS |
| Deterministic planar angular query checks | [44238752512](https://github.com/physicsvigilante/opticsim/actions/runs/44238752512) | SUCCESS |
| Planar refraction checks | [44238752526](https://github.com/physicsvigilante/opticsim/actions/runs/44238752526) | SUCCESS |
| Quasi-static source motion checks | [44238752610](https://github.com/physicsvigilante/opticsim/actions/runs/44238752610) | SUCCESS |
| Qualified authoring checks | [44238752541](https://github.com/physicsvigilante/opticsim/actions/runs/44238752541) | SUCCESS |
| Optical composition checks | [44238753014](https://github.com/physicsvigilante/opticsim/actions/runs/44238753014) | SUCCESS |
| Unified problem workflow checks | [44238753032](https://github.com/physicsvigilante/opticsim/actions/runs/44238753032) | SUCCESS |

The [native job's actual checkout](https://github.com/physicsvigilante/opticsim/actions/runs/44238752532/job/134581162269) states `HEAD is now at 10b8b07`, Node `v24.19.0`, pinned native PhyDemo `811f508...`, and **802 tests, 802 pass, zero fail/skipped/cancelled**. All **12** `B research:` test cases have an explicit passing line. The [optical composition job #134581163573](https://github.com/physicsvigilante/opticsim/actions/runs/44238753014/job/134581163573) also checked out the matching merge, used Node 24 and the same native pin; its existing browser steps succeeded, including **Chrome 157.0.8103.50 — browser acceptance 27 checks / 15 screenshots**, plus **hosted demo smoke 5 checks / 1 screenshot**. Existing optics controls remained successful. These are unchanged browser regressions, not a new B observer demo.

## 6. Independent-versus-builder evidence boundary and gate consequence

**Independently performed in this review:** read R2/R1/#134 and final test-only source, compared actual Git commit objects and base-to-head diff, inspected Actions run/job statuses, parsed archived real native and Chrome logs, extracted native event/hit/direction/count/reflection identities, and separately solved the two-line geometric intersections with the **logged** numeric coordinates/directions for both equal-index cases, the 1.5→1 baseline, and the mixed-order pair. I also verified archived R1 source and old CI records remain accessible.

**Not independently executed:** PhyDemo engine; Node 24 test suite; Chrome/browser regression; a fresh clone/install/build; or a new local native experiment. The **802/802** and **11/11** results are **builder GitHub CI evidence inspected by an independent reviewer**, not 11 independent physics replications.

**Gate consequence:** The corrected exact-tree PR has the evidence required for the owner to decide the disposition of **bounded research-only candidate B finite-window feasibility**. **Keep PR #135 draft and unmerged unless the owner separately authorizes a change.** A future production B observable, physical observer/pupil model, image claim, quantitative native error policy, or browser affordance must undergo distinct design, native and implementation review. Held #133/#129 and protected-main #123 remain independent.
