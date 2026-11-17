# Chat B — Independent source-integration review of Opticsim PR #122

**Date:** 2026-11-17  
**Verdict: INTEGRATION CLEARED FOR OWNER DECISION**  
**Boundary:** A targeted *integration* verdict only. **No PR may be merged or released on this verdict.** v18 PR #120 still requires its independent R2 physics review; footprint PR #118 is separately owner-held. PR #122 is a disposable research integration and must remain draft/unmerged absent an entirely separate owner decision.

## Reviewer independence and evidence limits

This is an independent source-level review of the GitHub objects, exact source/CI logs and the published physical fixture, with independent scalar geometry calculations. **I did not clone/build or independently run pinned PhyDemo, Node, or Chrome in my own runtime.** Native and Chrome execution claims below are explicitly **builder GitHub Actions CI evidence inspected by this reviewer**, not reviewer-native replication. The numerical geometry below is recalculated from physical inputs and the documented endpoint convention, not read from JS output as an oracle. This review does not certify two-thick-lens optical physics, ray-tracer internals, physical point-spread functions, images or continuous irradiance.

## Exact source identity and ancestry — independently checked

- [Research PR #122](https://github.com/physicsvigilante/opticsim/pull/122) remains **open, draft, unmerged**, currently based on `feature/native-thick-lens-aperture-v18`.
- Exact HEAD: `70cf502d19e243e4a8d7d1e0795f008c101c582d`.
- Exact HEAD Git tree, independently fetched from the Git commit object: `df9282da11ff416d0033cdf7e09509ba8dc24bc9`.
- [v18 source PR #120](https://github.com/physicsvigilante/opticsim/pull/120) prerequisite: `1c566103842cc6c4841aa97360cc893b0ed710c4`. Git compare confirms the integration source is **9 commits ahead, 0 behind**, with this prerequisite as merge base; the integration branch was not constructed by merging the unreleased #118 branch.
- [Footprint source PR #118](https://github.com/physicsvigilante/opticsim/pull/118): `7d44e52d2c4c5db30d91e4e87970b706c18a90f6`, independently main-based.
- Temporary synthetic main-target CI merge `1ec478b5a84dcae89a23e613103f7b98f9bc1f6c`: the Git commit object's tree is **also exactly** `df9282da11ff416d0033cdf7e09509ba8dc24bc9`. Tree identity is verified, not inferred from the PR description.

### Full 20-path diff and held-source footprint

I inspected the entire 20-file diff inventory, with detailed code inspection of the four shared paths (`README.md`, `src/app.js`, `src/observables.js`, `test/detector-hit-transfer.test.mjs`), the new cross-feature tests, measurement implementation, CLI/browser scripts, evidence/result rendering, provenance pins, and unchanged UI completion gates.

**All twelve #118-changed paths outside the four overlapping paths have Git blob SHAs identical to exact #118**, including `.github/workflows/unified-workflow.yml`, `scripts/author-scene.mjs`, `src/native-observations.js`, `src/detector-directional-footprint.js`, `src/evidence-panel.js`, `src/result-preview.js`, the standalone footprint tests, CLI/browser acceptance programs, the footprint contract, and its independent post-freeze fixture. The remaining integration-only changes are the dedicated research doc, four native cross-feature tests, a separate combined-viewer pin, and the correction to the research copy of the v18 source-pin test.

The v18 `src/adapter.js`, `src/contract.js`, `src/thick-lens-aperture-composition.js`, physical v18 fixture, original v18 source pin, and `upstream-pin.json` retain the **exact v18 Git blobs**. The `src/qualified-ui.js` Git blob is also unchanged. The complete diff contains no edit to the pinned PhyDemo runtime, native ray propagation, source sampling, v18 validators, event callback/collector, component authoring, or numerical limits.

## Integration behavior and fail-closed gates

1. **Opt-in only, browser:** `src/app.js` sets `captureRequestedDetectorHits` for either `detector-hit-events` or `detector-directional-footprint` before applying a valid qualified scene, and restores the previous flag on a failed apply. `src/qualified-ui.js` snapshots only a completed current session and uses revision/sequence checks to prevent stale asynchronous results from replacing the current display.
2. **Opt-in only, CLI:** `scripts/run-problem.mjs` passes the actual native request list into `evaluateDocument`. The latter enables the existing hit-event capture for either request kind; `snapshotNativeObservations` adds `detectorHitEventsById` only when either kind was requested. The five ordinary observation keys are unchanged without opt-in.
3. **Read-only derived measurement:** `src/observables.js` validates component type, exact scene SHA, completed execution, native event status, observed hit count versus original crossing count, and array length before calling `directionalDetectorFootprint`. The new function accepts at most 32 events, rechecks finite/on-segment point coordinates, unit incoming direction, 0.01 mm endpoint separation, and a non-grazing detector-normal direction. It uses centered-residual unweighted population RMS. Inconsistent or overflowed event lists withhold **only** the new derived footprint while preserving qualified legacy crossing counts when the native run is complete.
4. **No invented zero-width miss:** Both empty direction groups retain `count:0` but `null` for extrema, mean distance/point, span and RMS. A one-hit group's computed RMS=0 is explicitly identified as a sampled statistic, not a physical zero-width image.
5. **Incomplete/stale suppression:** An incomplete/stopped/failed run or mismatched scene SHA suppresses requested results before either old or new native values are used. The v18 depth-8 cross-integration test checks that both new footprint and old count/absorption results are suppressed. The presentation layer classifies the derived value as a *native sampled readout*, not a conditional image or PSF.

No material integration-code defect was reproduced through this inspection. The only physical assertion supported here is that the sample geometry and measured native CI outputs agree in the tested synthetic arrangement.

## Independent physical-fixture calculation (not derived from JS result values)

From the exact held v18 fixture `examples/native-thick-lens-aperture-v18.json` and the unchanged `mirrorEndpoints` convention:

- Source `S1=(-200,0)` mm emits a single ray at 0°, or **u=(+1,0)**. The aligned lenses (`L1` at x=0, `L2` at x=150) are symmetric about y=0; their on-axis surface normals do not deflect this central ray. The vertical mirror at x=300 returns it along **u=(-1,0)**. These direction predictions rely on the explicit on-axis symmetric fixture, not any inferred general two-lens image.
- Detector `D1` has centre `(-100,0)` mm, angle 90°, full length 400 mm. Hence **p1=(-100,-200), p2=(-100,+200)** mm; **t=(0,+1)** and the left/positive normal **n=(-1,0)** (floating-point trigonometry can add negligible residuals).
- For the first rightward crossing, **u·n=-1**: it belongs to **towardNegativeNormal**. For the leftward return, **u·n=+1**: it belongs to **towardPositiveNormal**. Both axial intersections are `(-100,0)` mm, and the along-detector distance `s=(P-p1)·t=200` mm.
- Therefore each group has **N=1, mean s=200 mm, mean point (-100,0) mm, min=max=200 mm, span=0, sampled population RMS=0**. This is *not* a physical spot-width measurement. Before/after original native counts should remain **D1 crossings=2; A1 absorptions=0**. GitHub native CI reports those same values.
- Aperture `A1` at x=-150 has vertical full length 100 and a centred transparent opening length 20. At opening centre y=0, the gap is **[-10,+10]** mm and the initial y=0 ray passes. Moving **only the aperture centre to y=+30** gives total y span **[-20,80]** mm, clear gap **[20,40]** mm and opaque arms **[-20,20]** and **[40,80]** mm. The first rightward y=0 ray strikes the lower opaque arm at **(-150,0)** before reaching detector x=-100 or either lens. Thus **A1 absorption=1, D1 native crossings=0**, and the two groups each have **N=0 with null mean, extrema, span and RMS**, not fabricated zero-width optical measurements.
- A depth-8 truncated propagation is a *completeness gate*, not a detector miss. It must suppress all requested measured values rather than return partial counts or inferred zeros.

## Exact-source CI, real Chrome and first failure — inspected, not rerun here

- I fetched GitHub Actions workflows associated with exact HEAD `70cf502d…`: **all 11/11 were completed successfully**, rather than taking the PR description's assertion at face value.
- [Unified workflow 44101713146](https://github.com/physicsvigilante/opticsim/actions/runs/44101713146), exact-head job `134103165146`, logged **865 tests, 865 passes, 0 failures** on Node **v24.19.0**. Its four new native integration tests passed: two-direction return, genuine aperture-blocked miss, **footprint-only** event capture, and depth-8 result withholding. It also logged **5 real public CLI footprint acceptance cases** (including >32 overflow and incomplete full Fresnel on standalone source fixtures) and **7 real-Chrome footprint checks with 4 screenshots** (using a planar fixture, not the two-lens v18 fixture).
- [Planar/refraction 44101713121](https://github.com/physicsvigilante/opticsim/actions/runs/44101713121), job `134103168197`, logged **13 passing real-Chrome v18 native aperture checks**. Those are browser v18 physics checks, *not* a combined v18-footprint browser request.
- [Optical composition 44101713483](https://github.com/physicsvigilante/opticsim/actions/runs/44101713483), job `134103167049`, independently included the four new integration cases in its successful Node suite.
- **Preserved failure:** The immediately preceding [failed unified run 44101334751](https://github.com/physicsvigilante/opticsim/actions/runs/44101334751), job `134101807976` on `d8d99142f1b277932141f9631a23e91052a3c702`, logged **864 pass / 1 fail / 865 tests**. The sole failed test was `v18 browser provenance is append-only…`: the old standalone v18 viewer blob expectation `cfbea455df3f7ea7a30002d0139730c25b235d32` did not match the combined current viewer `1a61bbe1460b30d16f37d29b83a1e0f0c98bfb66`. The research-only correction preserves the standalone v18 pin and checks a **new third pin** instead; the later exact-head suite passed. This initial failure must not be erased from the historical record.

### Historical source pin lineage

I inspected the original R1 freeze, post-exposure viewer records (v14, v15, v16, v17, v18), separate footprint record and new combined record. The original reserved `src/app.js` **SHA-256** remains `aad952e4c0b90a6812c21cd5f4ac92f35b52caf59f733d814deef3d32f43faf4`. The recorded v14 → v15 → v16 → v17 **SHA-256** candidate chain is `2d9a4bc6…` → `d34a9a0d…` → `0df07545…` → `1d6aec64…`, with corresponding predecessor links preserved.

Separately, I fetched the actual `src/app.js` **Git blob SHA-1** at the historical refs, confirming:
- main base `d3509e82…`: **`d8037fddf08e7536811bed961a4f8c0c59ece285`**;
- v17 source `9157c7a9…`: **`9d447af4c8fc59ec1e8fdcfbcec0c4d739fc477f`**;
- v18 source `1c566103…`: **`cfbea455df3f7ea7a30002d0139730c25b235d32`**;
- separate footprint source `7d44e52d…`: **`3b611f940f68e6814b9cc0577e4c063ac2dc7c28`**;
- combined research HEAD: **`1a61bbe1460b30d16f37d29b83a1e0f0c98bfb66`**.

The new combined pin references both correct source-parent blobs and its actual candidate blob; `test/fixtures/detector-hit-transfer-freeze.json` remains the exact same Git blob as v18 (`d7aee36a9047330f1227b992dc75cf0b491ba7da`). GitHub exact-head CI passed the SHA-256 freeze assertions. I did **not** independently rehash every earlier historical v14–v17 file's SHA-256; their archived provenance records and testing chain were examined and are unchanged by the 20-file integration diff. Neither old R1 evidence nor the #118/v18 original source was retrospectively relabelled as blind integrated evidence.

## Ranked reproducible findings and corrections

**F1 — P2 / nonblocking residual coverage: missing *combined v18* full-Fresnel withholding case.**  
The v18 standalone test exercises Fresnel-on incompleteness for old observables and the #118 standalone plate tests Fresnel-on withholding for the footprint. The four new `test/v18-footprint-integration.test.mjs` cases exercise depth-8 truncation **but not v18 L1+L2 full-Fresnel while the footprint is requested**. Reproduce the coverage hole by checking that file's four tests. Recommended follow-up: from the exact v18 fixture, set `partialReflection=true` for both lenses, request only the footprint plus original detector counts/absorption, and assert complete withholding if the native trace is incomplete. This is a missing combined test, **not evidence of a currently failing implementation**.

**F2 — P2 / nonblocking residual coverage: no v18-specific >32-hit overflow test.**  
The standalone directional-footprint native suite and public CLI exercise genuine >32 hits and verify the footprint is unavailable while the original count remains accessible; the v18 cross-feature tests do not apply that condition with both thick lenses, mirror and aperture present. A future test should first determine whether an admitted v18 authoring arrangement can genuinely yield >32 native detector callbacks, and if so validate the complete native overflow behavior; if not, test the measurement boundary with an explicit count/overflow sentinel without pretending the arrangement is natively authorable. The existing code and standalone native tests do support fail-closed overflow, so this is **not an observed clipping defect**.

**F3 — P3 / nonblocking residual coverage: no combined v18 + footprint real-Chrome scenario.**  
The footprint Chrome workflow exercises planar material changes, export/reopen, miss, and incomplete Fresnel; the separate v18 Chrome workflow exercises v18 aperture controls. Neither runs a qualified browser bundle with **v18 two lenses + mirror + aperture and a footprint-only request**. Add such a scenario, edit A1 from y=0 to y=30, and check UI freshness, signed group counts, null statistics and stale-result suppression. Source inspection of `app.js` + `qualified-ui.js` and separate Chrome coverage makes this a **targeted confidence gap**, not a reproduced stale UI failure.

**F4 — P3 / optional wording drift:** The newly added README paragraph still says the draft footprint is “pending exact-head CI” even though the held #118 and this exact combined research HEAD have already passed CI. Update that wording if the text is carried into a future release candidate; preserve release/independent-review holds.

**No P0/P1 integration blocker identified.** Do not claim the three untested combined edge cases are passed merely because adjacent standalone tests pass.

## Decision

**INTEGRATION CLEARED FOR OWNER DECISION** at **exact HEAD `70cf502d19e243e4a8d7d1e0795f008c101c582d` and tree `df9282da11ff416d0033cdf7e09509ba8dc24bc9`**, for the bounded integration question only. The native event-capture opt-in and derived signed statistics appear correctly composed with v18 in the tested fixture; CI/source provenance was directly inspected and independent analytic detector/aperture geometry supports the expected results. F1–F3 remain explicit targeted edge-test follow-ups, and F4 is editorial.

This verdict is **not** separate independent native PhyDemo or Chrome re-execution, does **not** replace PR #120's pending R2 optical physics review, and is **not authorization to merge PR #122, #118, #120 or any previously held PR**. The research PR should remain disposable and unmerged; any future combined release requires its own reviewed candidate and explicit owner approval.
