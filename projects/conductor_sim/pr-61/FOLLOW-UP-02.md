# conductor_sim PR #61 — targeted Chat B follow-up 02

**Request: verify F-01 and F-02 corrections only. This is NOT a new broad R2 review, merge authorization, or source edit.**

- **Original independent report:** [review-01 Chat B](reviews/review-01-chat-b.md), **changes requested** on head `e0ea76e80aca4b05cea7f16a12549c13670108d2` / tree `98b5b18fe3dedb6e0d3fb744c3732e812bb188fc`.
- **Chat A response and disposition:** [response-01](responses/response-01-chat-a.md). Original reviewer first attempts and findings are preserved.
- **Exact NEW source head to review:** **`1683e7a20b059096e3bca98abe7f55a6e982696a`**, tree **`b6d0e919e6f927099277303489923b241ca124e4`**. [Source PR #61](https://github.com/physicsvigilante/conductor_sim/pull/61) remains DRAFT, OPEN, UNMERGED. If this exact head has moved, report stale-head.
- **Comparison:** [old reviewed source → corrected source](https://github.com/physicsvigilante/conductor_sim/compare/e0ea76e80aca4b05cea7f16a12549c13670108d2...1683e7a20b059096e3bca98abe7f55a6e982696a), exactly 3 commits and **3 changed files**: `src/conductor_sim/driven_reassembly.py` (+17/-4), `tests/test_m26a_driven_reassembly.py` (+81), `docs/m26a.md` (+43). No changes to source electrostatic laws, force systems, numerical integrators, event detectors, viewer modules, FEMM, or CI workflows.
- **Risk:** R2 change to provenance/export semantics; narrow targeted re-review of corrected scope is appropriate per [review policy](../../../REVIEW-RISK-POLICY.md).

## Corrected F-01 — complete detached driven-model ancestry

The review-01 counterexample showed that live object ancestry was intact but a second-generation `as_dict()` lacked the root driven model's model ID/provenance. The new `parent_driven_assembly` field embeds the complete previous `DrivenReassembly.as_dict()` recursively; it is `null` for the first generation. `parent_driven_assembly_revision_id` equals that embedded record's digest. Each record retains full original/child DrivenModel, base M22a structural ledger, source edits, teacher origin, and exact parent revision. An already-existing bounded **16-step** structural ancestry limit still applies. The updated `as_dict()` computes its digest from the single constructed record rather than regenerating the expanding parent chain.

**Targeted check:** Construct an unfamiliar two- and preferably three-generation reassembly (source add, remove or replace, gravity change), serialize only the last `as_dict()`, and verify the root DrivenModel ID, provenance, model/ancestor revisions, actual source inventory, changes and digests are recoverable **without externally supplied parent JSON**. Check `parent_driven_assembly_revision_id == parent_driven_assembly["revision_id"]` and independently recompute the SHA-256 over each record without its own `revision_id`. Tamper with a detached copy and ensure the live model is unchanged. Flag any remaining incomplete lineage or serious data/complexity issue. Note hashes are identifiers, **not authentication or a trusted import API**.

## Clarified F-02 — separate typed record and physical-component ID namespaces

`DrivenModel.model_id` and `PrescribedScenario.scenario_id` are **record identifiers**; `NamedSource.source_id` is a **physical source identifier**. Equal strings across the model/scenario vs physical-source roles are intentionally allowed, because the typed audit ledger disambiguates them. This is explicit in M26a docs, interpreting frozen charter N3 as prohibiting collisions among **physical components and roles**, not every unrelated record identifier. Physical sources cannot alias each other, drag, scheduled applied field or reserved test-particle/medium/gravity IDs; retired physical source IDs remain unavailable in retained ancestry.

**Targeted check:** Verify cross-type same-string IDs retain distinct meanings and do not compromise source display, binding or qualified force; verify source IDs still refuse aliases with `drag:medium`, `field:scheduled` and retained physical source identities. Judge whether the documented typed-namespace policy resolves the original ambiguity or whether a concrete remaining risk merits changes. Do not call an allowed record/source textual coincidence a force-law bug without evidence.

## Fresh exact-head CI, distinct from earlier reviewed head

**All 16/16 source-specific workflows passed** for new head `1683e7a2...`:

- [Full Python 3.10/3.12 run 43739456939](https://github.com/physicsvigilante/conductor_sim/actions/runs/43739456939) and [second Python workflow 43739451857](https://github.com/physicsvigilante/conductor_sim/actions/runs/43739451857): **1,744 passed, 97 real-FEMM-dependent skips and eight warnings on each Python version**.
- [Real FEMM 5 run 43739456949](https://github.com/physicsvigilante/conductor_sim/actions/runs/43739456949): **97 passed** (historical conductor nonregression, NOT independent M26a physics proof).
- [Full visualization/Chromium run 43739457096](https://github.com/physicsvigilante/conductor_sim/actions/runs/43739457096): success; explicit M26a Chromium step passed, alongside prior viewer checks.
- [New-head visualization/source artifact 14171309142](https://github.com/physicsvigilante/conductor_sim/actions/runs/43739457096/artifacts/14171309142): GitHub-published ZIP digest `sha256:c8a30b66486a69f13eeb62da615dc16d956528c9116aba3eda75d321327ea6a7`. **Not independently rehashed by Chat A**, so treat as GitHub-reported metadata until personally checked.

The original [review-01](reviews/review-01-chat-b.md) independently checked a new three-phase exact-motion reference, 219 local regression cases, screen presentation and original artifact SHA. Those remain attributed evidence for the **older exact head**. Do not present them as fresh executions on the corrected head; the three-file corrected delta contains no physics or viewer edits.

## Requested reviewer output and merge policy

Write an **independently authored NEW append-only** `physicsvigilante/review_sandbox/projects/conductor_sim/pr-61/reviews/review-02-chat-b.md`, following [report template](../../../REVIEW-TEMPLATE.md). Preserve review-01 byte-for-byte. State exact new SHA/tree and **pass / changes-requested / insufficient-evidence**, individual verdicts for F-01 and F-02, steps personally executed vs CI inspected, any first failure and corrected retry, residual uncertainty, and whether a broader re-review is warranted. **Do not edit source, current independent reports, or merge PR #61.**

After report publication, the owner may simply tell Chat A "Review complete." Chat A will verify/triage the report. The PR requires separate explicit owner approval before any merge.