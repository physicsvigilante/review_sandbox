# SIM_HEAT PR54 — correction/integration request 02: current docs + source-only preview, focused R1

**Source:** [physicsvigilante/sim_heat draft PR #54](https://github.com/physicsvigilante/sim_heat/pull/54). **NOT merged. No native execution or source-result qualification is authorized.**

## Frozen source identities

| Field | Exact identity |
|---|---|
| **Current PR54 HEAD** | **`6cc3637a8f4009bfb37cafa8ed27edbd049d2d9e`** |
| **Current source Git tree** | **`e354dcf1f64e3e552850422336db237a7e3de556`** |
| Current `main` base | **`13260a62eb36d58802878c4d3dfb534ad1621f91`**, tree `2f1da9c596cf44af963dbcefc3ab78d3d780ef3c` |
| PR54 original independently reviewed HEAD/tree | `8f6ef1d0f8d0ebd938620c5694bc11856a5c9e7e` / `89db0700884d1f528c00715c5bb1b888d1378f1c`; [original Chat B review-01](reviews/review-01-chat-b.md) **SCOPED PASS on OLD HEAD only** |
| Current PR54 source commit parents | Original PR54 head `8f6ef1d...` + now-merged main `13260a62...` (an integration commit ON PR54 branch, not a main merge) |
| Actual hosted PR synthetic merge | `d838e8d0293f895377b0babecc5d20404fbbba05`, ordered parents current main `13260a62...` and current PR54 head `6cc3637...`, **same complete tree `e354dcf...`** |
| Current-main-to-head diff | **Exactly 11 paths**, 5 modified/6 added; NO existing physics/H1/qualification/viewer changes |
| Risk | **Focused R1**: navigation/evidence-claim presentation and CI applicability, with escalation only for demonstrated changed scientific/provenance meaning |
| New independent deliverable | **NEW** `projects/sim_heat/pr-54/reviews/review-02-chat-b.md`, authored solely by independent Chat B |
| Native/merge authority | **None. PR54 draft/unmerged, no OMC/Modelica native calls, no frozen reference regeneration.** |

## Why this new exact head exists

Owner explicitly approved prior [PR55](https://github.com/physicsvigilante/sim_heat/pull/55) integration, which merged to main at `13260a62...`; previously [PR56](https://github.com/physicsvigilante/sim_heat/pull/56) integrated a product-only CI trigger narrowing. The **original PR54** teacher-documentation candidate was reviewed R1 at its old SHA, but now conflicts with the merged product-entry CI file and was missing the newly available source-only viewer in navigation/capability inventory.

Developer merged the **new main into PR54's DRAFT branch only**, reconciled the shared workflow, added the explicit source-only navigation and updated canonical Markdown/HTML as one coherent teacher-facing candidate. The original review-01 was not edited. This new source head needs focused independent review before owner considers any main merge. The broader R2 evidence for unchanged source-preview implementation remains in [PR55 review-04](../pr-55/reviews/review-04-chat-b.md); the subsequent PR55 CI-only review-05 is [here](../pr-55/reviews/review-05-chat-b.md). No need to repeat physics review absent evidence of changed physics or provenance semantics.

## Exact changed scope (11 paths relative current main)

- `index.html` (modified): three distinct start actions—six-case archived explorer, saved conductivity comparison, and generic **source-only H1 inspector**—plus four evidence-category cards and truthful status labels.
- `docs/CAPABILITIES.md` (modified canonical) and generated `docs/CAPABILITIES.html` (added): one single-source current registry with **admitted authored-source previews** clearly separate from archived native diagnostics (`diagnostic_only/nativeQualified=false`), H1 analytical checking references and historically uncomputed C1 source views. TEACH_SPLIT3 is source-only, NOT a seventh native archive. Real table navigation and original source links.
- `docs/AUTHORING.md`, generated `docs/AUTHORING.html` (both added): current H1 admission guide and exact scratch D1 edit/refusal walkthrough; now links correct `python -B -m h1.source_preview ... --root ... --out ...` from admitted H1 studies and generic source viewer. Original old H1 contract still labeled **historical/proposed**, not rewritten. Source-only requests stay `not_computed`, no native execution.
- `tools/render_product_docs.py` (added): bounded Markdown→static HTML renderer for exactly two trusted canonical docs; generated pages have canonical SHA-256 metadata and `--check` detects drift. No runtime JS/code execution/upload surface.
- `tests/test_product_entry.py` (modified), `tests/test_product_docs.py`, `tests/browser_product_docs.py` (added): original catalog/evidence invariants, rendered exact HTML/source links, scratch-only real H1 CLI four-call walkthrough, desktop/mobile local HTTP clicks: root→source-only inspector→capability registry→original native JSON→current authoring guide→original study JSON.
- `.github/workflows/product-entry-ci.yml` and `tests/test_product_ci_scope.py` (modified): reconcile PR56's narrowed product-only triggers/protected-source refusal with PR54's generated docs parity/browser tests and PR55's new source-preview tests. Product candidate strict exact **11-path diff allowlist** and current-base `h1 experiments qualification viewer` protected-source guard; PR synthetic merge uses verified `HEAD^1` and `HEAD^2` rather than stale event base; branch push uses actual merge-base, main push uses prior parent, baseline checks exact pinned current main. Does not invoke OpenModelica. Tests still reject product-only H1 changes and unrelated source-preview-only triggers.

**Scientific preservation:** all original `h1/`, `experiments/`, `qualification/`, `viewer/`, original six `viewer/network/data` JSON/catalog/comparison, native runner, numerical references and frozen C1 history **unchanged relative to current merged main**. Existing PR55 source-only viewer remains exactly its separately reviewed production code; new PR54 only adds navigation and documentation.

## Exact-head hosted CI — all successful

[Branch-push **44296676358**](https://github.com/physicsvigilante/sim_heat/actions/runs/44296676358): **both matrix jobs SUCCESS**, including actual candidate head `6cc3637...` and exact-main baseline `13260a62...`.

[Pull-request **44296685585**](https://github.com/physicsvigilante/sim_heat/actions/runs/44296685585): **both matrix jobs SUCCESS**, candidate checkout synthetic merge `d838e8d...` with Git tree **identical** to current branch head, baseline exact main `13260a62...`. [Audit-core **44296685871**](https://github.com/physicsvigilante/sim_heat/actions/runs/44296685871) **SUCCESS** at current head.

- Candidate source: **293 unique unit tests PASS, one existing optional unittest SKIP** (152 H1 +4 analytical +62 adapter +42 Node +33 product). Baseline 284 overlapping PASS/one optional SKIP; **do not add totals**.
- Both candidate and baseline original SIX historical native diagnostic case bundles replay **BYTE_IDENTICAL**, `nativeExecutedByReplay=false`, published conductivity comparison byte-identical, and TEACH_SPLIT3 source-only JSON regenerated byte-identically; no native simulator was installed/invoked.
- Existing historical explorer, root entry, source-only inspector including admitted collision/provenance/refusal/race tests and new generated-docs desktop/mobile actual HTTP browser checks all **PASS**. The new docs parity check PASS. A harmless favicon HTTP 404 is not a JavaScript page error.
- Candidate branch artifact [**14423269966**](https://github.com/physicsvigilante/sim_heat/actions/runs/44296676358/artifacts/14423269966), **13,043,669 bytes**, SHA-256 `5e4abd75563959c22c8ca5c7d40f43079a68867747e9ba0128fbf18158621dec`, **54 unique CRC-valid members**.
- Candidate PR artifact [**14423632234**](https://github.com/physicsvigilante/sim_heat/actions/runs/44296685585/artifacts/14423632234), **13,043,678 bytes**, SHA-256 `2608d8d39012171f886308935f758d5200ebd1ccc2abd6f72bf0301edb34c564`, **54 unique CRC-valid members**.
- Exact main PR baseline [**14423793111**](https://github.com/physicsvigilante/sim_heat/actions/runs/44296685585/artifacts/14423793111), **9,726,201 bytes**, SHA-256 `1599005429d081596fc5967d490cb7d404a82935075c688ed51057634ac6ebf5`, **47 unique CRC-valid members**.
- Chat A personally downloaded/rehashed/CRC-checked these artifacts, compared actual head/tree/scope-base/11-path source diffs, archive and browser logs, and **independently reconstructed complete Git trees from the hosted `source.tar`**: current candidate `e354dcf...`, baseline `2f1da9c...`, exact matches to GitHub. Chat A personally reran **all 33 product tests** and renderer `--check` on byte-verified full candidate source with Python3.13.5: PASS. Full inherited suites, original ZIP replays and actual HTTP Chromium are **hosted** executions inspected by Chat A, not personally rerun.

## Focused independent R1 questions

1. Is the new start page and registry faithful to **four distinct evidence categories**? Archived native diagnostics are not promoted, source-only TEACH_SPLIT3 remains `not_computed`, analytical checker data is not native output and C1 original failures remain unchanged. The source-only inspector is not shown as an apparatus diagram or authenticating arbitrary imported JSON.
2. Confirm Markdown/HTML SHA/parity, link safety, original full H1 authoring/refusal walkthrough fidelity and no native invocation. Verify the explicit historical-contract label remains truthful. Check browser source-only path and docs tables at desktop/mobile, keyboard where supported; no source-only field turns into a computed value.
3. Check actual **11-path-only** diff/current base and that all previously approved physics/archives/native/qualification files are unchanged; PR55/56 remain integrated on main, and no historical C1 stack was added.
4. Check CI trigger inclusions/exclusions, **exact PR synthetic merge parent** (not stale event base), push current-main merge-base and current main push previous-base, preserved strict protected-source rejection and 11-path allowlist. Verify the 33 current product tests and all original six archive replay/real HTTP source-viewer regressions truly run and failure-propagate. Catch any actual capability/evidence semantics drift; escalate only if material.
5. Independently exercise a negative protected-source diff and/or a source-only import refuse if feasible, and distinguish tests personally executed from hosted CI. Reviewer may find issues; no desired verdict is prescribed.

Do not falsely say original PR54 R1 approval applies to this new source; it was pinned to `8f6ef...`. Do not assert browser imported-source authentication, teacher classroom usability, numeric native correctness or answer completeness. The historical C1 precision/seal failures, nine uncomputed original C1 requests and all six historical `diagnostic_only/nativeQualified=false` statuses remain untouched.

## Stop / report

Chat B independently writes a **NEW** `projects/sim_heat/pr-54/reviews/review-02-chat-b.md` with exact new head/tree, test attribution, concrete findings and one verdict **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. Do not modify original [review-01](reviews/review-01-chat-b.md) or source code. No production merge of PR54 without **new separate explicit owner approval**, no deployment, OpenModelica query/install/build/launch, C1 historical integration, frozen-reference regeneration, or native-status promotion.
