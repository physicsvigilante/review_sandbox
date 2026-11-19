# SIM_HEAT PR70 — CORRECTION-REQUEST-02: typed set/frozenset source snapshot R2-01

**Verdict requested:** SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE for the ONE corrected evidence-critical strict-type snapshot comparison defect, not a broad physics/native audit and not a merge authorization.

## Frozen source and independent history

- Original [independent Chat B review-01](reviews/review-01-chat-b.md), reviewer-authored blob **be9904ffb34aff2a0164c19241ada21821e2e2c4**: **CHANGES REQUESTED** at OLD source PR70 head **3f718ce0f1bb3fbc75162f99862796e32d2b0752**, complete tree **d9bd26ff57b22be20fce9c39ad855b0fa8fe4862**. Preserve that exact historical verdict and its independent original artifacts.
- Current [DRAFT PR70](https://github.com/physicsvigilante/sim_heat/pull/70), still main-based on **f52613c39c539b2d4543a9838e5658d526fca10e**, exact corrected HEAD **c2bd9ce63a6d725fdcd63d2d5d7c5416c7843739**, complete tree **3e71e670a8af88ef9661b29125407a2c9fe4139d**. Current synthetic PR checkout **8643bf65443faf1fca3add0368e953572e8981f3** has identical tree and ordered parents [main base, current corrected head].
- Old reviewed HEAD→new HEAD changes ONLY h1/study.py and tests/test_audit_regressions.py. Source comparator gets 15 new lines handling exact-type set/frozenset members; two new reviewer-targeted regressions, one import edit. No original H1 Modelica/runner/native archive, C1, N1–N8 qualification stack, physical laws/error thresholds, old study and frozen reference changed.
- [Chat A response-01](responses/response-01-chat-a.md) details the test-only RED and correction/CI.

## Reproduction and correction scope

In original source, \`Study.topology.anchored_nodes=frozenset({0,1})\` could be replaced post-admission with \`frozenset({0,True})\`, and Python set equality returned True despite the changed member type. Previous \`_same_typed\` compared exact dataclass/list/dict/tuple types but used native set equality, so \`verified_snapshot\` did not refuse. This is contract/provenance failure, not demonstrated falsification of a displayed physical measurement; source preview rebuilt from fresh source.

- Test-only HEAD **649e3d3b05f2276ab34d969dc1bf856f8b1e2869**. [PUSH CI 44582420338](https://github.com/physicsvigilante/sim_heat/actions/runs/44582420338) and [PUSH CI 44582420385](https://github.com/physicsvigilante/sim_heat/actions/runs/44582420385) actually executed the two new product regressions on the unchanged comparator and **FAILED 2 of 54 product tests**, with \`AssertionError: True is not false\`. Audit-core 44582420316 succeeded because it did not run the new product test suite. Do not attribute a false failure to audit-core.
- Corrected code matches every member in an equal-sized exact built-in set/frozenset **one-to-one using the same recursive exact-type comparator**. Positive unchanged integer-member sets and full source previews remain admitted. Review must challenge bool/int collision in nested Topology and direct sets/frozensets, possible ordering effects and dataclass type differences. Ensure \`verified_snapshot\` refuses changed member type with \`identity\` and \`build_source_preview\` does not accept the mutated caller. Check unaffected mass/provenance/request/disk mutation refusal, TEACH_SPLIT3 canonical bytes and sibling-folder D2_K2 revision.

## Exact-head CI evidence

- [Core project audit 44582867852](https://github.com/physicsvigilante/sim_heat/actions/runs/44582867852): SUCCESS.
- [Source preview 44582868025](https://github.com/physicsvigilante/sim_heat/actions/runs/44582868025): SUCCESS.
- [Authoring workbench 44582867906](https://github.com/physicsvigilante/sim_heat/actions/runs/44582867906): SUCCESS.
- Source-preview/workbench hosted logs: **152 H1 +4 analytical +63 adapters (1 optional skip) +54 product +42 JavaScript =315 collected; 314 PASS and 1 OPTIONAL SKIP** per workflow, docs parity. Six archived diagnostic cases replayed with historical bytes; real HTTP Chromium source inspection, docs and workbench refusals exercised. Zero native calls, no OMC installation/version/build/launch.
- Artifact identities and reported SHA256 for all 3 runs in [Chat A response-01](responses/response-01-chat-a.md). Developer did not independently rehash new hosted ZIPs. The source SHA and PR synthetic tree have identical Git-tree identities independently verified in GitHub objects.

**Review output:** publish ONE NEW report at \`physicsvigilante/review_sandbox/projects/sim_heat/pr-70/reviews/review-02-chat-b.md\`, state SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE pinned to new head. Differentiate reviewer-local executed probes from hosted CI, and preserve review-01. Do not change source from Chat B.

**Strict holds:** PR70 and earlier source PRs DRAFT/UNMERGED; no current native OpenModelica execution, no new sealed owner source/reference authority, no reference-bundle promotion, no C1 history rewrite or deployment. Seven old static physical 100x checking-centre failures, eight native execution blockers and private scorer UNSEALED persist. This review does not cover pending broader native qualification or integration.
