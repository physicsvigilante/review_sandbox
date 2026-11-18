## Follow-on PR #52 — literal integer metadata correction, new independent R2 pending

After [Chat B PR51 review-01 CHANGES REQUESTED](reviews/review-01-chat-b.md) and [Chat A acceptance](responses/response-01-chat-a.md), a separate [DRAFT SIM_HEAT correction PR52](https://github.com/physicsvigilante/sim_heat/pull/52) was opened at new source `e78ec2ccb2f8f97bbc1b282ec6bbe2847c1e1603`, tree `2ad10a1679d528f88030494f0349171502ef8e0f`, immediately on reviewed PR51 HEAD. It fixes **all six** case/provenance integer fields (`canonicalSamples`, `samples`, `duplicateRowsCollapsed` in steady and campaign), including Boolean and matching-float refusal, with nine independent test-only negative/positive methods. **Exact-head [CI #44232637466](https://github.com/physicsvigilante/sim_heat/actions/runs/44232637466) SUCCESS**: 249 genuine hosted OFFLINE passes, 1 historical optional skip, six original published bundles byte-identical, full viewer Chromium smoke PASS, original data unmodified, zero OMC. Its downloadable artifact #14396095895 has **34/34 CRC** and full SHA `2c22dd3db778942227acec29364819e73bd0a0822b006a7b5cc9bfc4a1555d36`. An intermediate fixture-cleanup workflow #44232475551 **FAILED**, retained. [New PR52 R2 review request](../pr-52/REQUEST.md) awaits independent Chat B; PR51 remains CHANGES REQUESTED at old SHA and both PRs remain DRAFT/unmerged. No native release authority gained and original frozen C1 numerical/reproduction FAILs unchanged.

---

## Independent R2 review-01 COMPLETE — CHANGES REQUESTED (MAJOR F-01 strict-type gap)

Independent [Chat B review-01](reviews/review-01-chat-b.md), reviewer-authored blob `0765d1226a74b2b5f181e3ccddd0bc2bc00c8768`, returned **CHANGES REQUESTED** on exact reviewed PR51 HEAD `52d693a748ad3709c99215bac0a5840a236937a6` (tree `7dcbb52c40f5b431ccdfe5dd4d2329fa21463829`). [Chat A response](responses/response-01-chat-a.md) **ACCEPTS** independent F-01: the original steady and campaign archived-result adapters fail to enforce literal `int` on three separate JSON metadata fields: case `canonicalSamples`, MAT/CSV provenance `samples`, and `duplicateRowsCollapsed`. `True`/floating-point equal counts can pass otherwise unchanged checks. This is a bounded internal schema-integrity defect **NOT** evidence of corrupted actual original GitHub archives or native scientific qualification. The reviewer reproduced 8 incorrect-type acceptances with repacked synthetic/test-only copies and explicitly verified original authentic archive replays remain unchanged.

The originally reviewed source/CI result remains 240 HOSTED OFFLINE unit passes, one optional skipped; six original diagnostic bundles byte-identical; hosted browser PASS — all **historical**, not a complete cross-adapter R2 PASS. **No new original F0 physical law, runner, checking reference, native output, externally authenticated owner release or production merge is authorized.** Fix in a **NEW exact-head scoped successor PR52**, with typed `type(x) is int` checks on both adapters and negative tests plus unchanged original archive replay, then targeted independent R2. PR51 remains draft/unmerged. All 11 genuinely missing C1 native gates and F0/PR32 historical FAILs persist.

---

# SIM_HEAT PR51 — active-main audit corrections, independent R2 pending

**Status: IMPLEMENTED + EXACT-HEAD CI PASSED; awaiting independent R2. Draft/unmerged; no native execution authorization.**

[Source PR51](https://github.com/physicsvigilante/sim_heat/pull/51) is based directly on active `main`, not the historical C1 experiment chain.

- Head: `52d693a748ad3709c99215bac0a5840a236937a6`.
- Tree: `7dcbb52c40f5b431ccdfe5dd4d2329fa21463829`.
- Main base: `c06fb5395781482bd6bbe055d10bc10cdf3bba8d`.
- Branch: `audit/2026-11-17-core-corrections`.
- Scope: exactly 11 paths, seven modified/four added; shared JSON parser, generated junction-ID collisions, archive/report type and consistency checks, reproduction tool, capability docs and dedicated offline CI.

No physical component equations, original Modelica/studies, reference specifications, numerical tolerances, native runner, historical execution plans or six published diagnostic data bundles were changed. Shared parser source changes prospectively: old source-pinned plans must refuse it, and do. Test-only scratch pins are not historical or live native plans.

## Verified evidence

[Exact-head push CI #44148890246](https://github.com/physicsvigilante/sim_heat/actions/runs/44148890246), job `134271418151`, completed SUCCESS. [Artifact #14358266358](https://github.com/physicsvigilante/sim_heat/actions/runs/44148890246/artifacts/14358266358): 5,873,728 bytes; SHA-256 `c0acc90ef3153625e4f480201d12a6ab43d79bfff433d2cd546fe1d22d746282`. Chat A downloaded/rehashed it and checked 33 unique CRC-valid members, matching head/tree/diff receipts, actual logs, archive replay and selected screenshots.

**Hosted unit tests: 240 passed, 1 optional skipped, zero failures.** Breakdown: H1 152; arithmetic 4; adapter suite 54 collected/53 passed/1 skipped; Node 31 passed. The skipped original-campaign mutation method was separately run locally with its authentic archive supplied and passed; it remains a hosted skip, not a hosted pass.

**Original archive replay: six of six published bundles BYTE_IDENTICAL** (D1, D2, DEV_BRIDGE, S1, TEACH_RING4, D2_K2). Saved comparison index also unchanged. Replaying original data does not rerun Modelica or independently qualify numerical accuracy.

**Hosted full explorer Chromium smoke: PASS**, including six-case switching, transient/steady controls, saved-time/keyboard/playback, CSV/refusal/import-race behavior, saved comparison, desktop/mobile screenshots. Developer-local localhost navigation was blocked by the environment and was not counted as a pass; the hosted normal localhost test subsequently succeeded. This is not cross-browser/accessibility/classroom certification. Twenty-one hosted PNG screenshots are retained.

**New OpenModelica operations: zero.** Synthetic repacked test archives are explicitly not native evidence. Ordinary D1/S1 checking-fixture preparation is separate from the untouched adopted C1 reference. Existing recorded main cases remain diagnostic-only and `nativeQualified=false`.

## Separate review lineage and next gate

PR50's [final evidence-corrected independent review](../pr-50/reviews/review-01-chat-b.md) scoped-PASSED the standalone C1 schematic visual fix; original PR49 remains CHANGES REQUESTED at its old head. That visual correction is **not included** in PR51 and its independent PASS does not approve main parser/provenance changes.

This candidate needs one coherent **R2** on the actual changed main behaviors. [REQUEST](REQUEST.md) and [reviewer prompt](REVIEWER-PROMPT-01.md) are ready. Chat B alone must create NEW `reviews/review-01-chat-b.md` with an independent verdict; no such verdict is asserted here.

After findings are resolved, production integration requires explicit owner approval and post-merge verification. Do not merge the historical C1 stack, promote diagnostic results, erase scientific failures, repin old execution plans or launch a native attempt. Consolidation of the working explorer and one bounded author-to-result workflow remain the forward direction, not more mock safeguard layers.
