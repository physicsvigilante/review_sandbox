# Opticsim PR #88 — final independent R2 **design** review status

**State: CHAT B R2 DESIGN-ONLY PASS at revised exact head; Stage 1 diagnostic implementation NOT YET AUTHORIZED OR TESTED; mandatory Stage 2 NOT AUTHORIZED.** The original v1 design received CHANGES-REQUESTED. The revised v2 design was independently accepted at the design level only. PR #88 is research/doc/workflow-only and remains **draft and unmerged**.

## Frozen source and CI identities

- [Source draft PR #88](https://github.com/physicsvigilante/opticsim/pull/88), base/current `main` `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`; pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`, Node 24.19.0.
- Original independently reviewed v1 proposal head `28c4aa94bbbf6b5a63a8bef433c80186e08a3d35` — [Chat B review-01](reviews/review-01-chat-b.md) **CHANGES-REQUESTED (DESIGN ONLY)**, three high-severity blockers B1–B3 and two major issues B4–B5. Historical report is unchanged.
- **Revised exact design head reviewed by Chat B review-02: `391047a5467f8e27f7b2162074900e8387945b9f`.** [Pinned proposal](https://github.com/physicsvigilante/opticsim/blob/391047a5467f8e27f7b2162074900e8387945b9f/docs/NATIVE-FINITE-FORWARD-QUALIFICATION-PROPOSAL.md); [exact v1→v2 diff](https://github.com/physicsvigilante/opticsim/compare/28c4aa94bbbf6b5a63a8bef433c80186e08a3d35...391047a5467f8e27f7b2162074900e8387945b9f) one commit, **one markdown file +60/−22 lines**. Full PR contains four research/docs/temporary-CI files; **no production `src/`, native, schema, numerical threshold, browser or results implementation**.
- On the revised head **11/11 GitHub Actions workflows passed**, [unified run 43757031446](https://github.com/physicsvigilante/opticsim/actions/runs/43757031446). This is existing software/research CI, **not** Stage 1 or Stage 2 executable qualification evidence. Chat B inspected workflow summaries only, not raw CI logs, newly executed native/Chrome tests or artifact ZIPs for this review.

## Independent design review lineage

1. **[Chat B review-01](reviews/review-01-chat-b.md): CHANGES-REQUESTED (DESIGN ONLY)** for original head `28c4aa94...`. Mandatory v9 suppression before proven observer neutrality, absent native-incident-point correspondence, incomplete public-data withholding matrix, unvalidated 128 cap and source/observer coverage were challenged.
2. **[Developer response — Chat A](responses/response-01-chat-a.md)** authored design v2 corrections and [targeted follow-up-02](FOLLOW-UP-02.md). It is **not** an independent review.
3. **[Chat B review-02](reviews/review-02-chat-b.md): PASS — DESIGN ONLY** for revised head `391047a5...`. All B1–B5 explicitly resolved **as design contracts**, with actual implementation prerequisites retained. No production bugs, new native capabilities or numerical fixes were certified.
4. **[Chat A response to review-02](responses/response-02-chat-a.md)** records the developer's disposition without falsely converting a design pass into engineering evidence.

## Accepted *design* boundary and release gates

- **Stage 0 remains the already-authored research and test-only shadow**, with no change to current canonical v9 results.
- **Stage 1, requiring separate owner authorization and fresh implementation:** **opt-in, bounded, noncertifying** diagnostic of actual native finite-Glass intersection geometry for validated v9 scenes only. It cannot alter native ray propagation, existing measurement qualification, canonical numerical thresholds, current source schemas, or claim physical correctness; an observed mismatch triggers a conspicuous **not certified by this diagnostic** advisory, not silent promotion or mandatory withholding.
- **Stage 2, not authorized:** possible **mandatory** v9 native-measurement gate would need a new owner policy decision and separately reviewed exact-head evidence proving complete public qualification consistency. Stage 1 approval or a Stage 1 clean diagnostic would **not** authorize Stage 2.

**Implementation prerequisites carried forward from Chat B**: a unique owning per-native-instance callback, exact original call/input/return/newRays identity and exception propagation even on snapshot failure; bounded scalar capture with post-run BigInt; complete source/Glass/**all-detector** ID-to-instance handler ownership and missing-start/zero-hit negative controls; exact forward, native cutoff and finite-edge `u` plus independently justified **computed intersection `P*` versus native reported incident-point** agreement (otherwise `unknown`); both actual and computed endpoint/vertex uncertainty; 128/129 capture overflow negative and no silent clipping; 1–4 actual sources, 0–2 actual detectors, full Fresnel on/off, truncated/warned native controls; source, meter and signed power invariance; real Chrome responsiveness/time/memory and honest advisory UI; A→B→A delayed native/audit callback isolation.

**No new implementation is present.** A future Stage 1 code PR needs actual native/browser tests, all 11 workflows on its own exact head, fresh independent Chat B R2 **implementation** review and separate owner-authorized merge. A Stage 2 mandatory policy would require additional design/evidence authorization, not be slipped into Stage 1.

## Historical research evidence that remains untouched

- [PR #87](https://github.com/physicsvigilante/opticsim/pull/87) documents actual finite-glass forward-hit discrepancies in one completed native near-critical run; this is a **binary64 represented-line inconsistency**, not a full physical ray solution.
- PR #88 original [research CI 43753292106](https://github.com/physicsvigilante/opticsim/actions/runs/43753292106) completed **24 synthetic v9 scenes, 64 native executions** (48 paired and 16 critical repeats), **55 checked finite-edge callbacks plus one unknown**, while current canonical results remained unaltered; prior Chat A rehashed research artifact [14177321360](https://github.com/physicsvigilante/opticsim/actions/runs/43753292106/artifacts/14177321360), SHA256 `5a1ceda61fe4d33158049ccc8705f46d79dea8f51ee45739182a8715d2e896e1`.
- Three previous strict-parity research workflow runs [43752308258](https://github.com/physicsvigilante/opticsim/actions/runs/43752308258), [43752585277](https://github.com/physicsvigilante/opticsim/actions/runs/43752585277), [43752839859](https://github.com/physicsvigilante/opticsim/actions/runs/43752839859) **FAILED**. The unchanged ordinary native simulation itself displayed exact-critical run-to-run variability. Those failures remain, and **observer neutrality remains unproven**. The design reviewer did not run additional tests in review-02.

## Next action

**Owner decision whether to authorize only Stage 1 diagnostic implementation** on a new implementation branch from production `main`. Retain PR #87/#88 as draft/unmerged historical research. Do not merge their disposable research workflows. No further same-SHA broad design review is necessary. No deployment.
