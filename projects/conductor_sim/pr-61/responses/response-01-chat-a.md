# M26a PR #61 — Chat A disposition of independent review-01

**Author: Chat A (implementer), not Chat B.** Original separately authored [review-01](../reviews/review-01-chat-b.md) is preserved verbatim. Reviewer outcome was **CHANGES-REQUESTED** at source head `e0ea76e80aca4b05cea7f16a12549c13670108d2`, tree `98b5b18fe3dedb6e0d3fb744c3732e812bb188fc`.

## F-01 — major, confirmed and corrected in new candidate

Chat B reproduced that two generations retain live Python parents but the detached `DrivenReassembly.as_dict()` only included the previous driven assembly digest. The exported final record could not recover the initial DrivenModel's model ID and provenance. This *is* a real mismatch with the stated complete audit-export contract, not a physics/integrator defect.

**Correction:** [source module](https://github.com/physicsvigilante/conductor_sim/blob/1683e7a20b059096e3bca98abe7f55a6e982696a/src/conductor_sim/driven_reassembly.py) now exports `parent_driven_assembly` recursively (null for a root parent). The embedded parent record's `revision_id` is retained in `parent_driven_assembly_revision_id`. Each generation retains actual parent/child driven models, provenance, original M22a base audit and physical changes. As with M22a, ancestry is limited to 16 structural steps. `as_dict()` hashes its built record once rather than redundantly rebuilding the recursive parent chain.

**Regression:** New three-generation `test_review_f01_multigeneration_export_contains_original_driven_model` checks that a final detached JSON alone recovers the root DrivenModel ID and provenance, verifies each parent-child ledger link and recomputes all export digests. It also checks parent purity and record detachment.

## F-02 — minor, namespace ambiguity clarified and tested

Chat B correctly reproduced that an authored source ID may textually equal a `DrivenModel.model_id`. This is **intentional typed namespaces**, not an illicit physical-component collision. A model ID names a model record, a scenario ID names a scenario record, a `NamedSource.source_id` names a physical source, and the typed record keys disambiguate them. Physical component IDs (fixed sources, drag, scheduled field, reserved roles) must remain distinct, and retired source IDs cannot be reused inside retained ancestry. No source physics is changed by a model record's name.

**Clarification:** [M26a technical docs](https://github.com/physicsvigilante/conductor_sim/blob/1683e7a20b059096e3bca98abe7f55a6e982696a/docs/m26a.md) explicitly define the namespaces and interpret frozen charter N3 as forbidding aliases within the *physical component* namespace. Frozen original charter and both reviewed source/evidence records remain intact.

**Regression:** New `test_review_f02_separate_model_scenario_and_physical_component_namespaces` documents same-text model/scenario/source IDs being valid and real physical role collisions remaining refusals.

## Scope, verification and merge gate

No existing electrostatic field, force, ODE integrator, event, numerical tolerance, schedule semantics or viewer was edited. New source commits since reviewed head modified only `driven_reassembly.py`, `test_m26a_driven_reassembly.py` and `m26a.md`. Full existing CI and the new Chromium test must pass **on the new exact head**, not be inherited from the older reviewed commit. The original reviewer’s independent three-phase physics calculations and ZIP/source integrity checks remain historically valid for the earlier head, not a claim of new-source re-execution.

**New correction head:** `1683e7a20b059096e3bca98abe7f55a6e982696a`; tree `b6d0e919e6f927099277303489923b241ca124e4`. **New-head CI pending as of this record.** Do not call the correction accepted before full CI and a targeted separate Chat B re-review of only F-01/F-02 and their boundary regressions. The source PR remains draft/unmerged and will require explicit separate owner merge approval.