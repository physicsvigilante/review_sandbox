# Independent Chat B review — SIM_HEAT PR70 (R2)

**Verdict: CHANGES REQUESTED — one narrow, reproducible typed-snapshot defect.** The other four maintenance corrections appear sound within their stated boundaries. This is a review of source/provenance and plan-loader maintenance, **not** approval of a new physics law, PR69, native execution, a physical-reference certificate, or a merge.

## Exact subject and scope

- Source: [physicsvigilante/sim_heat PR70](https://github.com/physicsvigilante/sim_heat/pull/70), **draft/unmerged** when checked.
- Reviewed HEAD: `3f718ce0f1bb3fbc75162f99862796e32d2b0752`; tree: `d9bd26ff57b22be20fce9c39ad855b0fa8fe4862`.
- Actual base main: `f52613c39c539b2d4543a9838e5658d526fca10e`; tree: `0c44961b473d23737b0c9f3b3f2cd3db65b9f264`.
- GitHub's exact-head synthetic checkout: `e2646ec13347b10583110197f5b96f7f655599b2`, with ordered parents [base main, reviewed HEAD] and the **same** candidate tree.
- Reviewed the 11 changed paths against the base plus relevant full source, tests, workflows, original plan-refusal tests, archive replay adapter, central protocol/risk policy, `AGENTS.md`, H1 contract, offline amendment and C1 freeze. No Modelica, numerical policies, original case sources, native archives or historical plans appear in this PR diff.

## Finding R2-01 — typed snapshot comparator admits an altered topology set (review blocker, bounded)

**Location:** [`h1/study.py` at the reviewed HEAD](https://github.com/physicsvigilante/sim_heat/blob/3f718ce0f1bb3fbc75162f99862796e32d2b0752/h1/study.py), `_same_typed` and `verified_snapshot`.

The new comparison recursively handles dataclasses, exact `dict`, `list` and `tuple`, but leaves `frozenset` to ordinary Python equality. `Topology.anchored_nodes` is a `frozenset[int]`. Python considers integer 1 equal to boolean `True` within sets, so a post-admission change of member **type** is accepted even though the comparator explicitly promises no bool/int coercion and claims exact typed source/derived comparison.

**Independently reproduced against the artifact-extracted exact candidate tree:**

```python
from dataclasses import replace
from pathlib import Path
from h1.study import load_study, verified_snapshot, _same_typed
from h1.source_preview import build_source_preview

root = Path("h1/cases").resolve()
s = load_study(root/"D1"/"study.json", root)
bad = replace(s, topology=replace(
    s.topology, anchored_nodes=frozenset({0, True})
))
# Original anchored_nodes: frozenset({0, 1})
assert _same_typed(bad, s) is True      # should be False
assert verified_snapshot(bad)           # should refuse
assert build_source_preview(bad)["status"] == "admitted_source_only"
```

Control probes on the same source: an unchanged `deepcopy` was admitted; a nested `dict` subclass and a boolean replacement in `topology.node_of` were both refused with `identity`.

**Impact is narrower than preview forgery.** The preview builder uses the freshly reloaded study, not the altered caller's topology, and `anchored_nodes` is not emitted as a source-preview value. I did **not** reproduce a wrong mass, heat flow, source hash, or native result. However, the claimed rule that *any* changed typed derived topology must refuse is false. As exact typed revalidation is the evidence-critical purpose of A19-03, this requires a targeted correction before declaring the scope fully passed.

**Required correction:** compare `frozenset` membership using exact element types, not Python's coercing equality (or implement a general recursive type-aware unordered comparison). Add a negative regression using the reproduction above and a positive unchanged-copy control. Retain the already demonstrated refusal for mutated mass, provenance, requests, `node_of`, and disk source; preserve cross-folder `D2_K2` revisions and byte-identical canonical TEACH_SPLIT3. Publish a **new source SHA** and exact-head focused/full offline CI. Re-review only this change and its preserved evidence; no fresh OMC run or broad physics re-review is required.

## Other five-correction checks

| Correction | Independent assessment |
|---|---|
| A19-01 direct-script import | **Supported.** Root insertion precedes `h1` imports only in direct-script mode; `python -I .../tools/authoring_workbench.py --help` passed from an unrelated temporary working directory. Existing route allowlist, Host, loopback and write refusals were inspected and remain unchanged. |
| A19-02 Windows boundary | **Supported with platform limit.** `.as_posix()` is the correct filesystem-to-portable-descriptor conversion; PureWindowsPath regression passed. Actual native Windows execution was not performed. Traversal, path confinement and no-symlink checks remain in `checked_path`. |
| A19-03 snapshot | **Partially supported, blocked as above.** Source is reloaded under the original stored case root, full `Study` state is compared, detached fresh state is used for output, and material source/provenance/request/physical/topology mutations fail in the existing tests. `frozenset` type equality is an exception to the specified strict rule. |
| A19-04 plan read | **Supported.** `load_plan` reads raw bytes once, verifies bounded length and SHA-256 on that buffer, and parses that same decoded buffer. Its scratch-file replacement regression passed. `check_host`, `prepare`, `execute`, per-case budgets and native invocation code were not changed. The loader hash does not itself confer trusted native authority. |
| A19-05 recurring CI | **Supported for this PR.** Original-branch-only all-added-file and protected-diff checks are conditional on the historical branch names, with `SOURCE_BRANCH` supplied as environment data rather than interpolated into executable code. Maintenance still validates actual PR checkout parents and executes the existing unit/JS/replay/browser steps. The new test runs the embedded Python guard for original versus maintenance branches; the protected-diff shell conditional was verified by inspection. Future maintenance coverage still depends on workflow path filters and should not be overstated as an unconditional universal gate. |
| New `tools/check_project.py` | **Supported within offline scope.** All six default suites ran successfully from an unrelated invocation context, recording failures/blocks as nonzero and `nativeQualificationGranted: false`. It makes no direct OMC invocation or native grant; archive and browser switches are optional. Tests invoked by this helper are source-controlled, not an independent sandbox/security boundary. |

## Independent execution and provenance distinctions

**Personally executed on the reviewed source (not merely inferred from CI):**

1. Downloaded GitHub artifact **14551734124**; ZIP SHA-256 `d72bdafd5fdab6f0c9a5c6e3c7993e443fe62258517dead85e34875e1f4b9887`; its 56 ZIP members passed CRC. Safely extracted `source.tar`; `git write-tree` of its 262 original files produced **exactly** `d9bd26ff57b22be20fce9c39ad855b0fa8fe4862`. The artifact records synthetic checkout `e2646ec...`, candidate-identical tree and base `f52613c...`, also checked through GitHub's commit API.
2. Executed `python -B -m unittest tests.test_audit_regressions tests.test_audit_ci_scope -v`: **12 passed**. Executed `python -B tools/check_project.py --out <new outside-repository folder>`: **313 collected / 312 passed / 1 optional adapter skip** (H1 152, analytical 4, adapters 63 with one skip, product 52, JS 42); documentation parity passed. No OMC query/build/launch.
3. Independently downloaded and checked the five original archive ZIPs, including their CRCs and whole ZIP SHA-256:
   - 14152886226: `8fc38b9e2f040b48ab5cbeab34e8698b7c99c4d462a1e31e8bc33b0395185379`
   - 14155084346: `f16975a25eea79f61f7819fb9e704ab04a33630044a51a0d062b8399c1c9ce38`
   - 14204656273: `82b4a87b66e0022d582da931253649b3829f6633119a57081c02dc253dc5dbd9`
   - 14215520616: `0bc1433be66df2827f8907d100ca264f6a721fe8ad40644b962500b97fa9b8b2`
   - 14153251022: `dc32a0a36a27f031ce7a13da83ebdd26a3dd6ac1d14612fa597b36cb439f4843`
   Offline `replay_published_archives.py` returned **BYTE_IDENTICAL** for D1, D2, DEV_BRIDGE, S1, TEACH_RING4 and D2_K2. The replay did not execute archived binaries.
4. Personally reproduced Finding R2-01 and its controls, separately from the author's 12 regressions.

**Observed hosted evidence, not personally rerun locally:** GitHub Actions run **44566839120** (source preview), **44566839405** (audit core), **44566839372** (workbench) all show success, correct PR head and passing job steps. Read their job logs: full offline suites, archived replay, actual HTTP Chromium explorer/source-preview/docs/workbench interactions and refusal checks were run by CI. The source-preview ZIP's hash cited by Chat A was not separately recomputed in this chat. No independent local HTTP browser run was performed; the author's earlier local browser failures remain environment-blocked and should not be relabeled.

The author's reported fail-first baseline (7 failures + 1 error among ten affected code tests), the separate PR69 **147/147** frozen-snapshot qualifications and the rehash of the other new CI ZIP are **developer evidence**, not tests performed by this reviewer.

## Explicit residual limits and stop

The strict physical source-interpretation/reference readiness gate, historical **seven** strict physical-reference failures, **eight** native blockers, and unsealed external scorer are unchanged. Provenance links and even a byte-perfect preview cannot prove the original interpretation of a textbook figure. Old execution plans remain pinned to old code and appropriately refuse this successor; temporary test-fixture repins are not historical plan edits. Product authoring, the mathematical draft stack, legacy native runner and teaching viewer are not yet one qualified end-to-end runtime. No fresh OpenModelica qualification, deployment, original case rewriting, PR69 decision or merge is authorized here.

**Disposition:** Request a one-file typed-comparator hardening plus a focused regression, new commit and exact-head CI; preserve all original archived replays. This is **not** a request to re-open the general architecture. PR70 should remain draft pending targeted re-review and separate owner approval.