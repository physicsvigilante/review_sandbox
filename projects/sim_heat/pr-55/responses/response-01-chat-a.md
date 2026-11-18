# SIM_HEAT PR55 — Chat A disposition of independent R2 review-01: CHANGES REQUESTED

Date: 2026-11-18. This is **Chat A's developer disposition**, NOT a Chat B independent verdict or authority to merge/native execute.

## Original review preserved

Original independent [Chat B review-01](../reviews/review-01-chat-b.md), Git blob originally committed to `review_sandbox`, returned **CHANGES REQUESTED** on the **old exact head `0b15c02e5c3c60af32224e0ec5f29a2920927d5a`**, tree `1be95f7dc60bd729d691e437c06f7914f0e045e4`. Source was correct for default TEACH_SPLIT3 and six original archived diagnostic case preservation, but the generic preview had the defects below. Neither the original report nor its source SHA was rewritten or reclassified to PASS.

| Finding | Developer disposition | New, bounded corrective implementation |
|---|---|---|
| F-01 — MAJOR | **ACCEPT, reproduced from admitted H1 scratch model** | Allow component named `node_0` but use typed selection `component:node_0` versus `node:node_0` in picker and pointer/keyboard graph interaction. Never change the H1 grammar or authored public IDs. |
| F-02 — MAJOR | **ACCEPT, reproduced component assumption loss** | Retain original component-targeted provenance as distinct `componentProvenance` records, not fabricated scalar source facts; separately display existing `@model` assumptions. Preserve direct-slot, parameter-dependency, repeated and original-order notes. Refusal clears assumptions too. |
| F-03 — MINOR | **ACCEPT as bounded display-schema consistency** | Require H1-compatible steady/transient component envelope and exactly the six documented provenance-kind labels in input, component and model provenance. Still only a display consistency check—not authentication or a physical solver. |

## New corrected source identity and local tests

**New unreviewed corrective commit** `1383a06d20422182cdae643337d6ddbdd6fcc5ec`, Git tree **`9d1216afcd3f6ba5978a6e4cf0fa79ca69ad5c9d`**, direct parent original reviewed `0b15c02e5c3c60af32224e0ec5f29a2920927d5a`, still base `main` `0278b79b4da1c3196edca7903189713e0482f3f6`.

Exactly **10 modified source-preview paths**, all among the original 14 added files: `h1/source_preview.py`; `viewer/source_preview/{app.mjs,core.mjs,index.html,core.test.mjs,data/TEACH_SPLIT3.json,README.md}`; `tests/{test_source_preview.py,browser_source_preview.py}`; `docs/ADMITTED_SOURCE_PREVIEW.md`. No other paths changed. All GitHub blob identities matched byte-verified local source; GitHub's new tree equals the actual local `git write-tree`.

Developer personally ran on exact reconstructed source: H1 **152 pass**; arithmetic **4 pass**; viewer/adapter **62 pass, one optional skip**; product **21 pass**; Node **42 pass** = **281 unique tests passed, one optional skipped**, zero failures. Saved conductivity comparison and new source-only preview regeneration byte-identical. The new Python regressions use an actually admitted scratch Modelica/study where rod `node_0` and generated graph node `node_0` coexist, and distinct component/`@model` provenance markers. New Node tests reject unsupported kinds/cross-mode inputs. Developer's separate exact-HTML Chromium DOM tests at 1440/390 px passed typed selection and visible assumptions; local HTTP navigation remained **blocked** by environment policy, not counted as local HTTP PASS.

## New exact-head hosted evidence and caveat

[Push source-preview CI 44272584312](https://github.com/physicsvigilante/sim_heat/actions/runs/44272584312), exact head `1383a06...`, **SUCCESS**. [PR source-preview run 44272593014](https://github.com/physicsvigilante/sim_heat/actions/runs/44272593014) **SUCCESS**. Hosted suite **281 PASS, one optional skip**; original D1/D2/DEV_BRIDGE/TEACH_RING4/S1/D2_K2 native diagnostic archive replays **six BYTE_IDENTICAL**, `nativeExecutedByReplay=false`; original D2/D2_K2 comparison byte-identical; new source preview byte-identical to its tracked source-only JSON. Actual-HTTP Chromium original explorer/product navigation and new source-preview desktop/mobile smoke **PASS**, including typed node/rod click, keyboard, picker, component/model provenance, mode/kind refusals, stale-state clearing and old/new import ordering.

[Source-preview artifact 14413740683](https://github.com/physicsvigilante/sim_heat/actions/runs/44272584312/artifacts/14413740683): **8,339,309 bytes**, SHA-256 **`b6289d0b729706f52065b230b1f62b7a6f76252adb49279f34fd2ecb24e3e078`**, independently downloaded/rehashed by Chat A; **46 unique entries, 46/46 CRC valid**. Internal head/tree/diff receipts match current commit. These full suite, archive and browser executions are **hosted, inspected by Chat A**, not fresh local browser-over-HTTP or personal original-ZIP archive runs. The favicon 404 is an HTTP request failure, not a JS page error.

**Keep unrelated CI failure visible:** [product-entry CI run 44272592968](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592968) has a **genuine FAILED candidate job** at PR merge-ref `a74eb1aa...`, because its existing product-only `git diff --exit-code ... -- h1 experiments qualification viewer` assertion rejects the new H1 source-preview files. It was triggered by the broad `tests/**` PR path filter. Its exact old-main baseline job succeeded. This is a separate workflow **scope conflict**, not a source-preview functional-test failure. Do not call the entire GitHub check suite green. Source-specific R2 CI and separate audit-core [44272592956](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592956) succeeded. Before any merge, obtain an explicit disposition of the extra red required check under the repo policy; do not silently waive it. Avoid broadening this physics/provenance correction by rewriting an unrelated workflow.

## Next gate and preservation

**Targeted independent R2 re-review required** on corrected commit/tree, with [CORRECTION-REQUEST-02](../CORRECTION-REQUEST-02.md) and [REVIEWER-PROMPT-02](../REVIEWER-PROMPT-02.md). Only independent Chat B may author the NEW `reviews/review-02-chat-b.md`; old review stays CHANGES REQUESTED. Review accepted claims narrowly: three fixed surfaces, actual valid H1 scratch cases, real browser refusal/selection/regime presentation, exact-head CI, original bundle preservation and CI-scope caveat. New code is **not yet reviewed**.

Both PR55 and separate PR54 remain draft/unmerged. No OpenModelica installation/version/build/launch, native runner, regenerated frozen/adopted reference, deployment, native qualification, historical C1 merge or original-data reclassification occurred. TEACH_SPLIT3 remains source-only; all authored public observations are `not_computed`.
