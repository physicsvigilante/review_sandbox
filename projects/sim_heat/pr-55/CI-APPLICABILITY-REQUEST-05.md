# SIM_HEAT PR55 — CI applicability review request 05 (focused R1)

**This request reviews ONLY the CI-workflow difference after an independent R2 PASS of the source-preview implementation. It is NOT a fresh physics review or permission to merge.**

| Pin | Verified identity |
|---|---|
| Source PR | [physicsvigilante/sim_heat #55](https://github.com/physicsvigilante/sim_heat/pull/55), open draft, unmerged |
| Base main NOW | **`7a80bd9c85d67b3a2e353d2a0702c8c5594c20dc`** (integrated reviewed PR56 CI trigger correction) |
| Source-preview R2-reviewed HEAD | **`1383a06d20422182cdae643337d6ddbdd6fcc5ec`**, tree **`9d1216afcd3f6ba5978a6e4cf0fa79ca69ad5c9d`** — independent Chat B [review-04](reviews/review-04-chat-b.md) SCOPED PASS, source-only F-01/F-02/F-03 |
| New CI-only HEAD | **`47edc006c459d403a16c54ffd63a33f6a6956999`**, tree **`da5b2ed60dacc2ee2e01d14baf366a3eb89f610e`** |
| Diff [R2-approved → current](https://github.com/physicsvigilante/sim_heat/compare/1383a06d20422182cdae643337d6ddbdd6fcc5ec...47edc006c459d403a16c54ffd63a33f6a6956999) | **Exactly one modified file**: `.github/workflows/source-preview-ci.yml`; two successive developer correction commits, 15 lines added/2 deleted net from R2-approved tree |
| Required independent reviewer report | NEW `projects/sim_heat/pr-55/reviews/review-05-chat-b.md` (review-01/02/03/04 immutable) |
| Review risk | **Focused R1 workflow applicability/protected-source integrity**, escalate only for a demonstrated changed evidence/qualification/physics contract |
| Native authority | **None. No OpenModelica query/install/build/launch**, native runner, original frozen-reference regeneration, release or deployment |

## Why change the already-reviewed PR55 workflow?

Independent Chat B [PR56 R1 review-01](../pr-56/reviews/review-01-chat-b.md) warned: PR55's dedicated source-preview CI checked its exact **14 PR-owned source-only additions** against a *fixed old main* `0278b79b...`. After owner's explicit PR56-only merge, main advanced to `7a80bd9...` with two extra files belonging to PR56. The synthetic PR55 merge contains all 16 changes relative to old main and the old diff gate would reject a **legitimate new main**.

The first prospective CI-only commit `d693189585b76c5f5d00bdfd45a5bddf6f7eca33` attempted to use `github.event.pull_request.base.sha`. A real [PR CI run **44287156069**](https://github.com/physicsvigilante/sim_heat/actions/runs/44287156069) **FAILED**, because the event base SHA remained stale at `0278b79...` **even though the checked-out PR synthetic merge commit `f8dd555...` had actual first parent `7a80bd9...`**. Its diff still listed 16 changes. This failed attempt is immutable historical evidence, not a pass. The same intermediate commit's [branch-push workflow 44287147849](https://github.com/physicsvigilante/sim_heat/actions/runs/44287147849) passed (old ancestry was correct there). Do not conceal or rewrite either outcome.

The **current corrected commit `47edc006...`** uses these controls in the existing source-preview workflow:
- **On PR synthetic merge**: `scope_base="$(git rev-parse HEAD^1)"` (actual checkout first parent), `candidate_parent="$(git rev-parse HEAD^2)"`, and assert the second parent equals `github.event.pull_request.head.sha`. Refuse nonmerge/mismatched candidates rather than making unsupported base guesses.
- **On the source-preview branch push**: keep original pinned lineage `0278b79...`, so the 14 original additions are still the complete candidate source diff.
- Save actual selected base as `scope-base-sha.txt`; compute both the **exact existing 14-path source-preview allowlist** and the original **protected physics/reference/archived viewer diff guard** against the same `"$scope_base"`. No allowlist widening and no protected-path exception.
- All inherited H1, analytical, viewer/adapter, Node, new source-preview, six original archive replays, source-only payload exact identity, comparison byte identity and real Chromium browser steps remain unchanged. No native runner or evidence-status change.

## Exact current-head GitHub hosted verification

[**Current push run 44287688196**](https://github.com/physicsvigilante/sim_heat/actions/runs/44287688196), job PASS on actual branch head, artifacts [14418494274](https://github.com/physicsvigilante/sim_heat/actions/runs/44287688196/artifacts/14418494274) **8,339,486 bytes**, SHA-256 **`d4d984a0e47a1740e748034c5cdafef778dff433f79095803519654ac938444d`**, 47 unique CRC-valid ZIP members. Internal `head-sha.txt=47edc...`, tree `da5b2...`, `scope-base-sha.txt=0278b79...`; 14-path diff exactly accepted. H1 152 + arithmetic 4 + adapter 62 + product 21 + Node 42 = **281 PASS, 1 existing optional SKIP**. Six original diagnostic bundles `BYTE_IDENTICAL`, `nativeExecutedByReplay=false`, comparison/source-only JSON exact, desktop/mobile existing and source-browser PASS.

[**Current PR run 44287695317**](https://github.com/physicsvigilante/sim_heat/actions/runs/44287695317) PASS on **actual synthetic merge SHA `ff3b421d60642427432e7477153263940f6b1729`**, Git tree **`2f1da9c596cf44af963dbcefc3ab78d3d780ef3c`**, parent 1 `7a80bd9...` and parent 2 `47edc...`. Artifact [14419742707](https://github.com/physicsvigilante/sim_heat/actions/runs/44287695317/artifacts/14419742707) **8,339,586 bytes**, SHA-256 **`1989f20ecdc73cc657d8149a86efbd9143f84423c93e66e459dcc92d537c7d02`**, 47 unique CRC-valid ZIP members. It records **`scope-base-sha.txt=7a80bd9...`** and the same exact original 14 paths; product suite now **24 PASS** (21 PR55 + 3 already on main from PR56), so **284 PASS, one optional SKIP**, other counts unchanged. All six original bundles replay **BYTE_IDENTICAL**, saved comparison/source-only preview exact, real localhost original/TEACH_SPLIT3/S1/D2/collision/provenance/refusal/races Chromium PASS. Tests overlap with push source; do not add totals.

[**Audit-core run 44287695288**](https://github.com/physicsvigilante/sim_heat/actions/runs/44287695288) PASS at current PR. First failed run 44287156069 is NOT reclassified as green; original unrelated product-workflow failure [44272592968](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592968) remains an independent earlier historical failure. CI artifacts were downloaded/rehashed/CRC-checked by Chat A and all head/tree/base/diff/archive/browser log receipts inspected. This is GitHub-hosted execution, **not** a claimed developer-local live HTTP rerun or new native computation.

**Local developer regression:** full source reconstructed at exact previous corrected PR55 tree `9d1216...`, one workflow file changed; local `git write-tree` **`da5b2ed...`**, exactly new GitHub commit tree and blob SHA. A simulated union of PR56's two main files with PR55's 14 owned additions produces **exactly 14 candidate-only differences relative to updated main**, not 16, with protected H1/qualification/data files unchanged. A deliberately changed `h1/model.py` is detected by protected-diff comparison. Initial test fixture counted untracked `__pycache__` files and failed; a second fixture using **tracked Git files** instead passed. Retain this first harness error (not a production-source bug). YAML parsed. GitHub PR-base field was observed stale despite synthetic merge's correct first parent; this is the actual reason for the second commit.

## Independent review tasks

1. **Independently verify exact source** HEAD/tree; compare to R2-approved `1383a06...`: only CI file changed. Confirm no code modifications to the H1 parser, source preview/provenance, Modelica physical components, archived native results, original references/checking thresholds, old viewer or frozen C1.
2. Verify GitHub PR run **actually** checked out synthetic merge first-parent **new main** and second-parent **new source head**; do not substitute PR event `base.sha` if stale. Reproduce mismatch from failed 44287156069 and success from 44287695317 with exact diff lists. Assert changed unrelated PR56 files are excluded, while the original PR55 14 additions remain mandatory and any protected edit is still refused. Push branch must still verify old reviewed lineage.
3. Confirm original 6 archive replays, saved D2/D2_K2 comparison, source-only case `not_computed` statuses and actual Chromium refusal/race smoke remain consistent. Distinguish personally rerun checks from inspected hosted CI.
4. Evaluate GitHub action script safety, no undesired branch/merge guessing or bypass on unexpected checkout, and edge case of future nested branches/status. Review PROTOCOL/REVIEW-RISK-POLICY/AGENTS. Only **R1 scope** is requested; don't repeat old R2 physics review without changed physics or evidence semantics.
5. If found, report concrete CI blocking issues and smallest regression, not future hypothetical overengineering. Confirm PR54 remains independently reviewed **draft/unmerged**, and PR56 already integrated on main. Do not claim PR55 release ready or merge approval.

## Required output and stop

Independent Chat B must commit a **NEW** report `projects/sim_heat/pr-55/reviews/review-05-chat-b.md`; never edit prior review-01/02/03 (old-head CHANGES REQUESTED) or review-04 (corrected-head source-only SCOPED PASS). Report exact new commit/tree/merge-ref, personal vs hosted probes, original failures, source/evidence/teacher boundaries, and one verdict **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** on this **CI-only change**.

Even if R1 passes, **PR55 stays draft/unmerged until separately owner-approved integration and current branch-protection/required-status checks**. Original six data remain `diagnostic_only/nativeQualified=false`; TEACH_SPLIT3's four requests `not_computed`, not new native results. No OpenModelica operation, frozen reference regeneration, historical C1 integration or deploy.
