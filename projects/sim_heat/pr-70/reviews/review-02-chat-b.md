# Independent Chat B review-02 — SIM_HEAT PR #70 (R2-01 typed snapshot correction)

**Verdict: SCOPED PASS on the corrected R2-01 set/frozenset source-integrity defect, at exact source HEAD `c2bd9ce63a6d725fdcd63d2d5d7c5416c7843739`.** This is **not** a whole-project, physical-model, native-qualification, C1, PR69, deployment or merge approval. Preserve [review-01](review-01-chat-b.md) as its historical **CHANGES REQUESTED** verdict for the older source.

## Identity and bounded scope

- Draft, unmerged [SIM_HEAT PR #70](https://github.com/physicsvigilante/sim_heat/pull/70); base main `f52613c39c539b2d4543a9838e5658d526fca10e`.
- Previous independently reviewed HEAD: `3f718ce0f1bb3fbc75162f99862796e32d2b0752`, tree `d9bd26ff57b22be20fce9c39ad855b0fa8fe4862`. Original [review-01](review-01-chat-b.md) was inspected again; blob SHA remains `be9904ffb34aff2a0164c19241ada21821e2e2c4`.
- RED tests-only HEAD `649e3d3b05f2276ab34d969dc1bf856f8b1e2869` changed **only** `tests/test_audit_regressions.py` (+30/−1) compared with old HEAD.
- Corrected HEAD `c2bd9ce63a6d725fdcd63d2d5d7c5416c7843739` changed **only** `h1/study.py` (+15) compared with RED HEAD. Thus old review→corrected HEAD changes exactly those two files; the correction does not change Modelica or other production paths.
- Independently read GitHub's commit objects: corrected source tree `3e71e670a8af88ef9661b29125407a2c9fe4139d` equals the whole tree of PR synthetic checkout `8643bf65443faf1fca3add0368e953572e8981f3`, whose ordered parents are [base main, corrected HEAD]. PR metadata still pointed to corrected HEAD and reported draft/open/unmerged at review time.

## R2-01 technical assessment

**PASS — original bool/int member collision is now refused.** The new `_same_typed` branch in [`h1/study.py`](https://github.com/physicsvigilante/sim_heat/blob/c2bd9ce63a6d725fdcd63d2d5d7c5416c7843739/h1/study.py) applies only when both containers have the same exact built-in `set` or `frozenset` type. It checks cardinality, converts actual members into a working list, and consumes exactly one recursively type-equal candidate per expected member. A candidate with an equal *value* but different Python type cannot satisfy that match. It does not rely on native set equality.

The formerly accepted counterexample is real: D1 freshly derives `Topology.anchored_nodes=frozenset({0, 1})`; a post-admission `dataclasses.replace` with `frozenset({0, True})` is natively set-equal but *not* recursively type-equal. Likewise, `frozenset({True})` vs `frozenset({1})`, `{0, True}` vs `{0, 1}`, `frozenset({False, 1})` vs `frozenset({0, 1})`, and nested tuple members refuse. A `set` vs `frozenset` substitution refuses at the outer exact-type check. Int-only copies in either iteration order still compare equal.

The matching is **one-to-one**, not merely existence-of-some-match: successful matches are removed, so one candidate cannot match two expected members. For the admitted H1 `anchored_nodes` domain (a bounded `frozenset[int]`, node limit 64), exact-type integer equality is an equivalence relation, so match order cannot change the answer. There is no need to claim an all-purpose matching algorithm for arbitrary user-defined equality hooks outside the admitted object domain.

**PASS — the API refuses before preview construction.** [`build_source_preview`](https://github.com/physicsvigilante/sim_heat/blob/c2bd9ce63a6d725fdcd63d2d5d7c5416c7843739/h1/source_preview.py) begins with `study = verified_snapshot(study)`. That function reloads the original source under the stored case root, recursively compares the complete original `Study` against freshly derived facts, and raises `Refusal('identity', ...)` on the changed topology. The negative product regression checks `verified_snapshot(wrong).code == 'identity'` and verifies that `build_source_preview(wrong)` raises `Refusal`. No preview payload is returned on that input. The preview still uses freshly reloaded source facts after success; no changed physical result was demonstrated or is claimed.

**PASS — legitimate unchanged snapshots are retained.** The positive regression tests an int-only reordered `frozenset` and successful `admitted_source_only` preview. Existing product regressions exercise unchanged D1/S1/TEACH_SPLIT3, the cross-sibling `D2_K2` revision, the canonical TEACH_SPLIT3 serialized bytes, and refusal for modified mass, provenance, request, topology `node_of`, and on-disk study content. These preexisting checks were not modified by the correction, and they passed in the exact-head hosted suites. The preview remains source-only (`nativeExecuted: false`, observations `not_computed`).

## Independent work performed vs hosted evidence

**Personally performed here:** read the original review/response/correction request, compared both commit ranges, inspected the exact corrected comparator and regression code plus the `verified_snapshot`/`build_source_preview` call chain, D1 topology construction, and source-preview refusal implementation. Independently executed the **verbatim extracted `_same_typed` function body** in an isolated Python probe (not the complete repository checkout). The probe checked synthetic nested dataclasses and explicit bool/int/outer-container/tuple negatives, unchanged copies, then enumerated **36 distinct typed set states** generated from `[False, True, 0, 1, 2, -1]`; all **2,592 ordered comparisons** across built-in sets and frozensets agreed with type-tagged member identities. This is independent comparator evidence **only**; I did not personally execute `load_study`, full source-preview integration, full test suites, a browser or archive replay in this review.

**Hosted CI inspected directly (not reviewer-local execution):**

| GitHub Actions run | Ref | Observed result |
| --- | --- | --- |
| [RED source-preview 44582420338](https://github.com/physicsvigilante/sim_heat/actions/runs/44582420338) | Tests-only `649e3d3` | **FAIL**, specifically both new tests: `test_frozenset_member_type_drift_refuses_source_preview_identity` and `test_unordered_typed_snapshot_equality_keeps_legitimate_copies`, each `AssertionError: True is not false` against old comparator. |
| [RED workbench 44582420385](https://github.com/physicsvigilante/sim_heat/actions/runs/44582420385) | Tests-only `649e3d3` | Same **two** targeted product failures; archive and browser downstream steps skipped after the failed test step. |
| [GREEN core 44582867852](https://github.com/physicsvigilante/sim_heat/actions/runs/44582867852) | Corrected `c2bd9ce` | **SUCCESS** on its selected core/offline/archive checks. This is not a separate 315-test product-suite run. |
| [GREEN source-preview 44582868025](https://github.com/physicsvigilante/sim_heat/actions/runs/44582868025) | Corrected `c2bd9ce` | **SUCCESS**; the two target regressions now show `ok`; offline suites, original archive replay and hosted HTTP Chromium interaction/refusal gates completed. |
| [GREEN workbench 44582867906](https://github.com/physicsvigilante/sim_heat/actions/runs/44582867906) | Corrected `c2bd9ce` | **SUCCESS**; target tests `ok`, offline suites, original archive replay and hosted HTTP Chromium explorer/source-preview/workbench gates completed. |

Each of the latter two product workflows ran **152 H1 + 4 analytical + 63 adapters + 54 product + 42 JavaScript = 315 tests collected, 314 passed, 1 optional adapter skipped**. Their logs show the surviving six original archive replay gate and browser checks; no native executable was launched. I did **not** independently download/re-hash the corrected workflow ZIP artifacts or re-replay archived binaries; artifact SHA metadata in Chat A's response remains developer/hosted evidence, not my independent checks.

## Nonblocking boundary observation

The generic pre-existing dictionary branch of `_same_typed` still uses native `actual.keys() == expected.keys()`. In a standalone contrived probe, `_same_typed({True: 'x'}, {1: 'x'})` returns `True`. That is a real limitation of the helper's *general-purpose* no-coercion wording, but **not a demonstrated bypass of this R2-01 correction**: the dictionaries in a freshly admitted H1 `Study` use string keys (JSON source records, model/component identifiers, port-to-node mapping and request reports), not numeric or Boolean keys. It is not a merge blocker for the specified set/frozenset defect. If a future admitted schema allows non-string dictionary keys, add recursive exact-key matching with a dedicated regression before claiming universal typed equality. The present correction neither introduces nor worsens this pre-existing gap.

## Disposition and holds

**SCOPED PASS for the R2-01 typed `set`/`frozenset` fix at exactly `c2bd9ce63a6d725fdcd63d2d5d7c5416c7843739`; no further change is required for this narrow review.** Review-01 remains the unchanged, historically accurate **CHANGES REQUESTED** assessment of `3f718ce...`; this new review supersedes its one actionable comparator objection only for the newly pinned source.

The seven old strict 100× physical-reference failures, eight native-readiness blockers and unsealed first-author scorer remain outside scope. No fresh OpenModelica operation/version/build/launch, original C1 rewrite, reference adoption, native MAT regeneration, deployment, source change, PR review submission or merge was performed. PR70 and related draft PRs are not approved for merge by this report.
