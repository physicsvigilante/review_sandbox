# SIM_HEAT PR55 — CORRECTION-REQUEST-02: focused independent R2 re-review

This is the **new** review request for the **corrected** source-preview commit; do not overwrite or retroactively pass original [review-01](reviews/review-01-chat-b.md), which returned **CHANGES REQUESTED** at `0b15c02e5c3c60af32224e0ec5f29a2920927d5a` and source tree `1be95f7dc60bd729d691e437c06f7914f0e045e4`.

[Developer response and evidence attribution](responses/response-01-chat-a.md). [Current source PR55](https://github.com/physicsvigilante/sim_heat/pull/55).

## Pin the NEW source

| Field | Exact identity |
|---|---|
| Repo/PR | `physicsvigilante/sim_heat` [#55](https://github.com/physicsvigilante/sim_heat/pull/55), draft, unmerged |
| Base `main` commit | `0278b79b4da1c3196edca7903189713e0482f3f6` |
| Original reviewed candidate | `0b15c02e5c3c60af32224e0ec5f29a2920927d5a` (CHANGES REQUESTED, do not rewrite) |
| **New corrected HEAD** | **`1383a06d20422182cdae643337d6ddbdd6fcc5ec`** |
| **New corrected Git tree** | **`9d1216afcd3f6ba5978a6e4cf0fa79ca69ad5c9d`** |
| Correction diff | [Original reviewed head → corrected head](https://github.com/physicsvigilante/sim_heat/compare/0b15c02e5c3c60af32224e0ec5f29a2920927d5a...1383a06d20422182cdae643337d6ddbdd6fcc5ec): **10 modified paths**, zero new unrelated changes |
| Review scope | **Targeted R2** — three specific Chat B defects, regression coverage, preservation, CI-scope gate |
| Required output | A NEW independently authored `projects/sim_heat/pr-55/reviews/review-02-chat-b.md` |
| Execution authority | **No native operations.** No merging PR54/PR55, no release, frozen reference change or C1 historical integration |

Read source `AGENTS.md`, H1 implementation/offline contracts, original C1 freeze and central `PROTOCOL.md`, `REVIEW-RISK-POLICY.md`, `REVIEW-TEMPLATE.md`. The original independent report is the primary defect specification. Distinguish developer assertions from personally tested results.

## Adversarial requirements: verify the corrected behavior

**F-01 original MAJOR (source identity collision):** Create a real scratch Modelica/study accepted by original `h1.study.load_study`, rename a valid rod to `node_0`, repin only scratch model SHA. Ensure the actual preview has component `node_0` and logical aluminum node `node_0` simultaneously. Confirm `component:node_0` versus `node:node_0` are distinct picker values; picker, graph click and keyboard activation of the aluminum node display node properties and ports, while rod selection shows the rod's actual authored scalar values and endpoints. Do not ban legal H1 identifiers or use an apparatus-specific fallback. Assert no false source values.

**F-02 original MAJOR (provenance completeness):** Add an admitted `feed` whole-component assumption with a unique marker and one `@model` regime assumption to a scratch study. Confirm original component record is retained in new `componentProvenance` with exact original target/kind/locator/note and visible on selecting `feed`. The model assumption must be visible in its own area; both must clear on a refused import. Neither may be converted into a `source_given` input slot. Ensure existing direct-slot and chained-parameter provenance, duplicate S1 source/unit attribution and repeated original records still pass and remain distinguishable.

**F-03 original MINOR (imported display-schema consistency):** For an otherwise valid source-only transient preview with three bodies, replace only its mode with `steady` and require browser refusal. Mutate `kind` in input, component or `@model` records to `native_qualified` and require refusal. Test valid steady S1, an independent transient composition and legitimately supported provenance labels. The imported JSON remains **untrusted**, not independently authenticated; these display checks must not claim execution or source-fidelity approval.

**Refusal and races:** Test refusal clearing graph nodes, requests, selected details, model-provenance area and identity, then a later valid import. Re-run old-valid/new-invalid and old-invalid/new-valid completion orders, and confirm latest selection wins. A negative-result bypass must not promote `nativeQualified`, `nativeExecuted`, `diagnostic_only`, computed temperatures, native flow or physical geometry.

**Source preservation:** Verify the exact ten modified paths only from the original reviewed head, the unchanged H1 physical grammar/library, historical model/study cases and references, six archived diagnostic case JSON/catalog/comparison byte hashes and all C1 frozen failures. The regenerated TEACH_SPLIT3 JSON may change as a **source-only schema payload** because `componentProvenance: []` is now represented, but not as new native evidence.

## New exact-head hosted CI and evidence (check personally)

[Push workflow **44272584312**](https://github.com/physicsvigilante/sim_heat/actions/runs/44272584312) — **SUCCESS**, exact corrected head; [PR source-preview workflow **44272593014**](https://github.com/physicsvigilante/sim_heat/actions/runs/44272593014) — **SUCCESS**, separately triggered. Archived [artifact **14413740683**](https://github.com/physicsvigilante/sim_heat/actions/runs/44272584312/artifacts/14413740683) = **8,339,309 bytes** SHA-256 `b6289d0b729706f52065b230b1f62b7a6f76252adb49279f34fd2ecb24e3e078`, **46 unique CRC-valid files**. Head/tree/diff receipts must match the exact current source.

- H1 152 + arithmetic 4 + adapter 62 + product 21 + Node 42 = **281 unique hosted unit PASSES**, one existing optional skipped test. Developer also personally ran these locally (overlapping coverage; do not add totals). Source preview regeneration and original saved conductivity comparison were byte-identical.
- All six original D1/D2/DEV_BRIDGE/TEACH_RING4/S1/D2_K2 archived **native diagnostic** output bundles replay **BYTE_IDENTICAL**, `nativeExecutedByReplay=false`. This is read-only archive reproduction, not fresh OMC evidence.
- Hosted real HTTP Chromium original explorer and new preview desktop/mobile checks **PASS** including admitted collision, component/model assumptions, inconsistent mode/provenance refusals, signed-off request statuses and both out-of-order import races. Developer local Chromium `page.set_content` probes passed; **localhost navigation was blocked locally**. Preserve this distinction and minor favicon HTTP 404; no zero-HTTP-error assertion.

**Additional CI issue to assess separately, not conceal:** [product-entry run **44272592968**](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592968) reports a **real failed candidate job**, while its separate baseline job passed. That legacy workflow is triggered by `tests/**` and asserts `git diff --exit-code` on `h1`/viewer paths for a product-doc-only change; that scope constraint rejects the source-preview additions. [Audit-core workflow 44272592956](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592956) succeeded. This is a **CI applicability/merge-gate problem**, not a demonstrated failure of the dedicated preview workflow. Independently verify the exact failed command and advise whether it requires a separate bounded CI hygiene fix before owner considers merging. Do not silently waive an actually required status check or claim all PR checks are green.

## Verdict and stop condition

The independent report must give **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** and distinguish (i) source interpretation, (ii) physical/numerical correctness, (iii) native simulation/output coverage, (iv) evidence/provenance integrity, (v) teacher usefulness, (vi) textbook completeness. TEACH_SPLIT3 is developer-authored/illustrative, NOT a blind trial. A scoped pass is **only** a corrected source-preview verdict, not owner merge permission or native qualification. Note personally executed probes versus inspected hosted logs, and preserve failures/unknowns.

Commit only your NEW report under the exact path `projects/sim_heat/pr-55/reviews/review-02-chat-b.md` in the central review repo; do not modify developer source, old review, PR54, main, frozen references or original archives. No OpenModelica query/install/build/launch and no production merge.
