# SIM_HEAT PR #55 — independent Chat B focused R1 review, cycle 05

## Verdict: **SCOPED PASS — CI-only current-base correction; NOT MERGE READY**

**No demonstrated blocking defect in the reviewed CI correction.** The current source-preview workflow compares the GitHub PR synthetic merge against its *actual checked-out first parent*, verifies its second parent is the authored PR head, and preserves the exact original fourteen added paths and protected-source refusal. This resolves the observed stale PR-event-base mismatch without modifying the earlier R2-approved source-preview implementation or any physics, original diagnostic/reference data or qualification meaning.

This is **not** an R2 re-review, native physics qualification, production-merge recommendation, status-check waiver, teacher trial or authorization to merge PR55/PR54. PR55 stays draft/unmerged pending separate owner decision and current check-policy verification.

## Identity, scope and authority

| Item | Independently verified |
|---|---|
| Project | [physicsvigilante/sim_heat](https://github.com/physicsvigilante/sim_heat), [draft PR #55](https://github.com/physicsvigilante/sim_heat/pull/55) |
| Exactly reviewed source HEAD | **47edc006c459d403a16c54ffd63a33f6a6956999** |
| Exactly reviewed source Git tree | **da5b2ed60dacc2ee2e01d14baf366a3eb89f610e** |
| Preceding independently R2-reviewed source | 1383a06d20422182cdae643337d6ddbdd6fcc5ec, tree 9d1216afcd3f6ba5978a6e4cf0fa79ca69ad5c9d; [review-04 SCOPED PASS](review-04-chat-b.md) remains unchanged |
| Source HEAD parent | d693189585b76c5f5d00bdfd45a5bddf6f7eca33 (first attempted CI-only correction, not a passed PR-run) |
| Prior original main | 0278b79b4da1c3196edca7903189713e0482f3f6 |
| Current main at review | **7a80bd9c85d67b3a2e353d2a0702c8c5594c20dc** (PR56 integrated) |
| Actual checked-out PR synthetic merge | **ff3b421d60642427432e7477153263940f6b1729**, tree **2f1da9c596cf44af963dbcefc3ab78d3d780ef3c** |
| Synthetic merge parents, ordered | **HEAD^1 = 7a80bd9c85d67b3a2e353d2a0702c8c5594c20dc; HEAD^2 = 47edc006c459d403a16c54ffd63a33f6a6956999** |
| Reviewer | Chat B, separate ChatGPT conversation, GPT-6; 2026-11-18 |
| Risk | Focused **R1** workflow applicability / evidence protection |
| Production source edited by reviewer | **No**. Only this new central review report is authored/committed. |

Read and followed [REVIEWER-PROMPT-05](../REVIEWER-PROMPT-05.md), [CI-APPLICABILITY-REQUEST-05](../CI-APPLICABILITY-REQUEST-05.md), central [PROTOCOL](../../../../PROTOCOL.md), [REVIEW-RISK-POLICY](../../../../REVIEW-RISK-POLICY.md), [REVIEW-TEMPLATE](../../../../REVIEW-TEMPLATE.md), pinned SIM_HEAT AGENTS.md, the prior review-04 scope, actual source workflow and GitHub commit/run objects. Independent means a fresh reviewer context and adversarial checks, **not** a separate human/domain expert or blind source interpretation.

## Findings

### F-05-01 — current-base PR merge-parent correction: **PASS (no blocker)**

The [R2-reviewed source → current source compare](https://github.com/physicsvigilante/sim_heat/compare/1383a06d20422182cdae643337d6ddbdd6fcc5ec...47edc006c459d403a16c54ffd63a33f6a6956999) has **two CI-only commits; exactly one modified file**, [`.github/workflows/source-preview-ci.yml`](https://github.com/physicsvigilante/sim_heat/blob/47edc006c459d403a16c54ffd63a33f6a6956999/.github/workflows/source-preview-ci.yml#L45-L93), net +15/-2 lines. No source-preview builder/parser/provenance/viewer implementation, Modelica components, native controller, reference thresholds, original archive, qualification source or historical C1 code changed.

The PR branch push retains the **pinned old-base** source diff against 0278b79..., and GitHub compare establishes actual old-base ancestry (ahead four, behind zero). On a pull_request checkout the shell uses `git rev-parse HEAD^1` for the scope base and `git rev-parse HEAD^2` for the candidate, then asserts second-parent equality with GitHub's event PR head SHA. In both modes, the **same** scope base is used for the strict `git diff --name-status` allowlist and `git diff --exit-code` protected-path test. `set -euo pipefail`, `fetch-depth: 0`, and the commit-existence check make missing parents/failed assertions fail rather than silently selecting a guessed fallback.

The actual [GitHub merge commit object](https://github.com/physicsvigilante/sim_heat/commit/ff3b421d60642427432e7477153263940f6b1729) independently confirms the ordered parents above. The [current main → merge compare](https://github.com/physicsvigilante/sim_heat/compare/7a80bd9c85d67b3a2e353d2a0702c8c5594c20dc...ff3b421d60642427432e7477153263940f6b1729) has exactly **14 ADDED paths and no modified/deleted path**, matching the original strict workflow literal set, including both source tests and all source-preview files. The [old main → candidate HEAD compare](https://github.com/physicsvigilante/sim_heat/compare/0278b79b4da1c3196edca7903189713e0482f3f6...47edc006c459d403a16c54ffd63a33f6a6956999) is also exactly those fourteen ADDED paths. The unrelated PR56 changes (`.github/workflows/product-entry-ci.yml` and `tests/test_product_ci_scope.py`) are present **in main**, not counted as PR55 changes.

The original protected paths remain explicit: `viewer/network`, `qualification`, `tools/h1_native_batch.py`, `h1/model.py`, `h1/study.py`, `h1/policy.py`, `h1/reference.py`, `h1/verification.py`. Any extra changed path/status also breaks the exhaustive 14-row equality. No exception, glob expansion of the allowed set, new native job or bypass was introduced.

**Adversarial probes personally executed:** In a separate temporary local Git fixture (placeholder source contents, **not** a claim of replaying the production repository), I constructed old main, PR56's two-file main advance, a branch with the exact 14 allowed additions and a two-parent synthetic merge. The corrected-base diff admitted fourteen while the stale old-base comparison yielded sixteen and refused. The original push baseline admitted fourteen. A wrong second-parent expected SHA failed the actual shell equality test; a single-parent commit lacked HEAD^2 and failed in PR mode. Deliberately modifying `h1/model.py` caused **both** the allowlist and protected-diff checks to fail. These are negative control checks of the guard structure, not a second hosted Actions run or a malicious PR submission. **No blocking defect demonstrated.**

For future base advances, re-run CI against the new synthetic merge before considering integration; first-parent identity applies to the checked-out merge snapshot, not an eternal assertion that main cannot move later.

### F-05-02 — historical failed first attempt correctly preserved: **PASS**

The **first** proposed CI-only commit d693189... used the event `pull_request.base.sha`. [PR run 44287156069](https://github.com/physicsvigilante/sim_heat/actions/runs/44287156069) actually **FAILED** (job 134742651832). The checked-out synthetic merge was **f8dd555ee111b77a86fbcb2aea3d0c8957963de9**, tree 37387e53bde220d18eb57f05d05927636864f359, with first parent **new main 7a80bd9...** and second parent **d693189...**. GitHub's event base field was still **old main 0278b79...**. Directly downloaded the retained failed artifact **14418428881** (873 bytes, SHA-256 **74ffd8c4615c9f2efd1a756b61b72bd305032181414d2babde13e53b7765c95b**, CRC valid): its `scope-base-sha.txt` is old main and its `source-diff.txt` has **16 changes**, including PR56's modified product workflow and added scope test. The job log shows the exact allowlist AssertionError and exit code 1; archive replay/browser steps were **SKIPPED**. It must remain **FAILURE**, not be retroactively marked a pass. Its prior push run [44287147849](https://github.com/physicsvigilante/sim_heat/actions/runs/44287147849) separately passed for the branch's old-base scope.

Crucially, even the **new** successful PR run's event payload still reports the old base SHA; the corrected workflow derives the checked-out parent's SHA instead. The earlier unrelated product-entry [failed candidate run 44272592968](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592968) also remains historical failure, not erased by PR56's later integration.

### F-05-03 — current exact-head CI and preservation: **PASS within hosted evidence class**

I directly inspected GitHub workflow-run/job metadata and logs, downloaded both complete current Actions artifacts, verified ZIP SHA-256, file counts, unique names and CRC, and inspected the retained internal receipts, test logs, replay JSON, original/browser logs and source-preview screenshots.

| Evidence | Push at exact branch HEAD | PR at checked-out synthetic merge |
|---|---|---|
| Workflow | [44287688196](https://github.com/physicsvigilante/sim_heat/actions/runs/44287688196), job 134744484823, **SUCCESS** | [44287695317](https://github.com/physicsvigilante/sim_heat/actions/runs/44287695317), job 134744509723, **SUCCESS** |
| Artifact | [14418494274](https://github.com/physicsvigilante/sim_heat/actions/runs/44287688196/artifacts/14418494274), **8,339,486 bytes**, SHA-256 d4d984a0e47a1740e748034c5cdafef778dff433f79095803519654ac938444d | [14419742707](https://github.com/physicsvigilante/sim_heat/actions/runs/44287695317/artifacts/14419742707), **8,339,586 bytes**, SHA-256 1989f20ecdc73cc657d8149a86efbd9143f84423c93e66e459dcc92d537c7d02 |
| ZIP integrity | **47 unique entries, 47 CRC-valid** | **47 unique entries, 47 CRC-valid** |
| Internal head/tree | **47edc006... / da5b2ed...** | **ff3b421d... / 2f1da9c...** |
| Internal scope base | **0278b79...** (old pinned lineage) | **7a80bd9...** (new main) |
| Actual `source-diff.txt` | Exact **14 A** entries | Exact **14 A** entries |
| Hosted test results | **281 PASS, 1 optional SKIP** | **284 PASS, 1 optional SKIP** |
| Replay/compares/browser | All pipeline stages **SUCCESS** | All pipeline stages **SUCCESS** |

Both totals count H1 **152**, analytical **4**, adapter **62 pass / one optional skip**, and Node **42**; product/source tests were **21** on push and **24** on PR because PR56's **three pre-existing main tests** are on the synthetic merge. These two runs overlap; **do not add their passes**. [Audit-core PR run 44287695288](https://github.com/physicsvigilante/sim_heat/actions/runs/44287695288), job 134744509328, is separately **SUCCESS**. GitHub lists three completed successful check runs against current source HEAD. No current check in that observed set is red; that observation does not certify all repository branch-protection/ruleset policy.

**Six original archived diagnostic replays:** Directly read **both** artifact `archive-replay.json` receipts; they are identical and record `BYTE_IDENTICAL` / `nativeExecutedByReplay=false` for **D1, D2, DEV_BRIDGE, TEACH_RING4, S1, D2_K2**. Downloaded and personally hashed/CRC-checked **all five original archive ZIPs** (D1/D2 share one archive). Their SHA-256 values exactly match the six-case receipts: 14152886226 = 8fc38b9e..., 14155084346 = f16975a2..., 14204656273 = 82b4a87b..., 14215520616 = 0bc1433b..., 14153251022 = dc32a0a3.... I **did not independently execute** the six-case replay builder; its byte-identical derived preview claims are inspected GitHub-hosted replay output, corroborated by original archive identities rather than a new personal run.

Both current artifacts contain identical regenerated `compare-replayed.json` (SHA-256 **34f6abac6948fd5c70b3b91d13a72336c5d768ce235f0108f26c57731ef134c3**) and `preview-replayed.json` (SHA-256 **15011d101a38d46fb2b86cc7ee41ec6448ff4b47fd36419e0cc1c903b73d4ac3**). The successful CI script compares these bytes to the existing tracked comparison and new source-only preview respectively; no original reference is regenerated. The admitted preview has `authored_source_only`, `nativeExecuted=false`, `nativeQualified=false`, `sourceFidelityQualified=false`, and **all four TEACH_SPLIT3 requests remain `not_computed`**. Original archived cases remain `diagnostic_only/nativeQualified=false`; this does not upgrade them.

**Browser:** Hosted real localhost Chromium passes on both runs for historical D1/D2/bridge/S1/Ring4 and reversals, existing product entry/navigation, source-preview desktop/mobile, H1-admitted component/node name collision, whole-component and model provenance, alternate topologies, invalid mode/provenance refusal with stale UI clearing, and asynchronous import races. I inspected logs and the actual source-preview desktop/mobile, provenance-collision and refusal screenshots inside the artifact; **I did not personally launch Chromium**. The server log has incidental `/favicon.ico` 404 responses, so browser success means successful page assertions/no page JavaScript errors, **not literally zero HTTP errors**.

## Independent evidence boundaries and separate judgments

**Personally done:** Read pinned GitHub code/commit objects and compare-file sets; independently matched both ordered merge parents with the current main and source branch; inspected all three current check runs, earlier failure, exact jobs/logs, two current ZIPs and the failed-attempt ZIP; verified artifact hashes, unique names and CRC; checked all five original archive ZIP hashes/CRC against six archived-case receipts; inspected source-only request/provenance flags and browser screenshot/log evidence; ran isolated Git parent/allowlist/protected-code negative probes. No tool installed/executed OpenModelica or modified the source repo.

**Hosted only, not personally rerun:** Full Python/Node CI suites, archived preview reproduction, tracked byte comparisons, source admission and real-HTTP browser interaction. No fresh live native trace, frozen reference generation, teacher evaluation or independent numerical/physical acceptance occurred.

| Dimension | Cycle-05 conclusion | Basis |
|---|---|---|
| Source interpretation fidelity | **UNCHANGED / not re-reviewed** | Only CI workflow changed since prior R2-approved source |
| Physical/numerical correctness | **NOT ASSESSED** | No physics/source semantic change or new native evidence |
| Native simulation/observable coverage | **NO NEW CLAIM** | Original diagnostic archive replay only; four source requests not computed |
| Evidence integrity / CI provenance | **SCOPED PASS** | Exact parent/base/diff, artifact fingerprints, six archive receipts, original hashes and failures checked |
| Teacher-facing usefulness | **UNCHANGED / not re-reviewed** | No viewer behavior or authored content changed |
| Textbook-answer completeness | **NOT IN SCOPE** | Developer-authored illustrative TEACH_SPLIT3; no calculated answers |

## Disposition and stop

**No demonstrated new defect requiring a production correction for this narrow R1 workflow change.** The historical first attempt remains failed, the old-head CHANGES REQUESTED reviews 01/02/03 remain authoritative for their own old SHA, and review-04's corrected source-only SCOPED PASS remains untouched. PR56 is merged to main; [PR55](https://github.com/physicsvigilante/sim_heat/pull/55) and [PR54](https://github.com/physicsvigilante/sim_heat/pull/54) remain open **draft, unmerged**.

**Smallest next gate:** retain this pinned review and artifact references; prior to any separate owner-authorized PR55 integration, confirm the current main/PR merge snapshot and applicable required GitHub status checks are still current. If main moves, obtain fresh appropriate CI. Do not use this pass to merge, run OpenModelica, promote original diagnostics, regenerate frozen references, integrate C1 or deploy.
