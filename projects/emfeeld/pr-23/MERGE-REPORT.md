# CURRENT RELEASE DISPOSITION — POST-MERGE QUALIFIED (2026-11-16, Asia/Kolkata)

The **fresh main-push Linux/Windows CI and separate real-PyVista qualification have PASSED at the actual merge SHA** `bf6a18399c604136dd363ad94d40557dbe2c2543`. Both **original post-merge release ZIPs were downloaded and independently SHA256/CRC/native-evidence audited**: all 2,151 entries per OS were unique and CRC clean; each verified 21 sealed top-level inventories, 12 nested native inventories, 60 saved native-run input SHA256 bindings, six sealed comparisons and 32 fulfilled/two legitimately unavailable G1 measurements. The same-author 20 static/12 trajectory reference check passed per OS. Separate main PyVista workflow passed and its 17 screenshot byte hashes were verified. See **Follow-up 02** below for precise artifact IDs, SHA256, test counts and limitations. Earlier “post-merge open” sections remain unchanged as historical snapshots; their incomplete disposition is superseded here.

**Result: qualified within the explicitly automated, archive-integrity and scoped R2-review boundaries; manual Windows mouse interaction, classroom outcomes and adversarial cryptographic authenticity are not claimed.**

---

## Historical integration record and subsequent append-only updates

# EM Fields PR #23 — integration and post-merge qualification record

**Status as of 2026-11-16 (Asia/Kolkata): MERGED; POST-MERGE MAIN CI / RELEASE ARCHIVE REAUDIT NOT YET VERIFIED.** This record makes no assertion of post-merge qualification success until original run/artifact evidence has been observed. It must be updated append-only with new factual observations, preserving this initial record.

## Merge identity and audit boundary

- [Source PR #23](https://github.com/physicsvigilante/emfeeld/pull/23): GitHub reports **CLOSED / MERGED**, not draft. Merge method: merge commit. Merge SHA **`bf6a18399c604136dd363ad94d40557dbe2c2543`** ([commit](https://github.com/physicsvigilante/emfeeld/commit/bf6a18399c604136dd363ad94d40557dbe2c2543)).
- Exact accepted source head: **`7bbdea64a81c2e3bea2b24c59a2d5866afdda707`**. Source canonical tree **`e7ddc4c6c44106bf3113f7c1e176b21490a7cf5c`**. Frozen qualified main/base before merge **`f0fc993dae1831432ca43b651a12e64fa0b2fdd5`**.
- Before the guarded merge the PR was explicitly moved from draft to ready for review, then rechecked as OPEN, nondraft, mergeable, with the same head/base. GitHub's merge API was passed **expected_head_sha** equal to the exact reviewed source SHA and returned **`merged: true`** and the above merge SHA. Subsequent PR metadata independently showed **closed/merged** and the same merge commit; the commit object was fetched.
- User authorization context: standing instruction for autonomous bounded development and qualified integration, with interruptions for independent R2 review, and user's subsequent **“continue”** after the published review-03 verdict. No waiver of blockers, physics scope escalation or post-merge evidence requirements.
- Original design-only PR #22 is separate. This merge contains Bounded Scenario Ensemble V1: 2–4 independent V3 child hypotheses of an exact parent, separately authored named native runs and sealed comparisons to a *fresh* common baseline. The scenario ordering is an authored comparison, **not** a physical time transition.

## Independent review chronology, immutable historical verdicts

1. [Review 01](reviews/review-01-chat-b.md): historical **CHANGES REQUESTED** on old head `38773a546d76616fe815eb302c418281bded7c1d`; R2-01, R2-02 and R2-03 findings.
2. [Review 02](reviews/review-02-chat-b.md): historical **CHANGES REQUESTED** on old corrected head `5738fec0d22deb59d0f146dc75b8a9b33db64486`; residual R2-01 static-analysis/motion-request blocker reproduced.
3. [Review 03](reviews/review-03-chat-b.md): **scoped PASS** at merged source head `7bbdea64a81c2e3bea2b24c59a2d5866afdda707`, tree `e7ddc4c6c44106bf3113f7c1e176b21490a7cf5c`. Independent reviewer executed 29 new tests, 29 passed `-W error`: static mode + fully valid trajectory sample/event refused before *any* sibling or output write; positive trajectory and physical member-level rejections retained; representative R2-02 raw JSON overflow and R2-03 accepted/rejected stored-byte drift protected. Review 03 is scoped, not new full numerical/physical certification; reviews 01 and 02 are left unchanged.

## Pre-merge exact-head verification — previously observed success, not substituted for main CI

- [Linux/Windows clean-install #43871642152](https://github.com/physicsvigilante/emfeeld/actions/runs/43871642152): both original jobs returned completed/success on the reviewed head. Per OS **1,435 headless**, **18 historical behavioral**, **33 real-PyVista** tests. The focused 33 ensemble tests are already counted in headless, and 1,486 is a *suite-membership* sum, not extra distinct tests.
- [Real-PyVista #43871641853](https://github.com/physicsvigilante/emfeeld/actions/runs/43871641853): completed/success; offscreen and slider checks, not manual Windows interaction.
- [Exact-source snapshot #43871642044](https://github.com/physicsvigilante/emfeeld/actions/runs/43871642044): completed/success; Chat B independently reconstructed exact Git tree from 346 original source files.
- Prior author-audited Linux/Windows release ZIPs each had **2,151 CRC-clean entries**, 12 complete native runs, 60 native input hash bindings, six sealed comparisons, 21 inventories, and **32 fulfilled/two genuinely unavailable** measurements. This evidence belongs to the earlier reviewed head/merge preview, not the newly merged main commit. Do not rename these artifacts or check results as post-merge.

## Post-merge release gates — open at this record

- [ ] Identify original **main-push** clean-install Linux/Windows workflow at exact merge SHA `bf6a18399c604136dd363ad94d40557dbe2c2543`, and verify final conclusion and test-accounting logs. The available connector's `fetch_commit_workflow_runs` filters pull-request-triggered runs, so its empty response for the merge SHA **does not demonstrate** that main workflow is absent or passed.
- [ ] Identify and verify the actual post-merge real-PyVista qualification for that SHA, if triggered by main; distinguish rendered offscreen from manual desktop testing.
- [ ] Download **new** original release artifacts (if produced), check exact merged commit/tree binding, SHA256 and CRC, preserved native E1/G1/T1 evidence, input hashes and seal inventories, including the 32 fulfilled/two expected unavailable measurements. Never repurpose pre-merge artifacts as post-merge evidence.
- [ ] Append factual workflow IDs, job conclusions, artifact hashes and reconciliation outcome to this report; only then mark post-merge qualification completed. Fail closed if no accessible evidence or any test discrepancy.

## Residual limitations

No claim of distributed crash-safe ACID, cryptographic authentication against a malicious author of all unkeyed hashes, manual Windows desktop operation, classroom usefulness, broad electrodynamics or conductor response. Native V3 construction acceptance is not numerical completion; genuine missing observations remain unavailable and partial. Independent separate-chat review is not an independent human certification.

**Final integration disposition:** source **merged**, independent R2 blocker **cleared within narrow review scope**, exact-head **pre-merge CI green**, **post-merge verification outstanding**. No user's local Conda environment, sealed saved study, original reviewer reports or physics laws were changed as part of this merge record.


## Follow-up 01 — independently checked merge-tree equivalence and main-file identity (2026-11-16 Asia/Kolkata)

This follow-up is appended to the original merge report; it does **not** convert unknown post-merge job outcomes into a pass.

- GitHub compare `7bbdea64a81c2e3bea2b24c59a2d5866afdda707...bf6a18399c604136dd363ad94d40557dbe2c2543` reports **ahead_by=1, behind_by=0, files=[]**. There are **zero file changes** between the independently reviewed head and the actual merge commit, providing direct GitHub-supported evidence that the committed source trees are equivalent.
- Cross-ref fetches of six paths returned the **same exact Git blob SHA** at (a) reviewed head, (b) merge commit, and (c) GitHub's current default `main`. No changed source/test/CI bits were detected in these files:
  - `src/emfeeld/scenario_ensembles.py`: `10f688c1386c3c8cba279f082e505e711bafab27`
  - `tests/test_scenario_ensembles.py`: `5c9be0d2e1abd152b463cd75548cd78a98b9b372`
  - `tools/qualify_scenario_ensembles.py`: `d57f3ca1106e11f3ce4ca0e9a7f21d457a5594c7`
  - `verification/check_scenario_ensemble_runs.py`: `582114ae565744350697357e192037bd8995601e`
  - `.github/workflows/release-candidate.yml`: `4d7315f94fa65dfdb96f4e007ba095e09c476c1e`
  - `.github/workflows/viewer-qualification.yml`: `8c96776fd64ddc9da2e18099a4b8c678d3d91a72`
- The exact merged `.github/workflows/release-candidate.yml` declares a `push` event on `main` with `src/**` and `tests/**` path filters, which this merge modifies. The exact `.github/workflows/viewer-qualification.yml` also declares a `push` event on `main` for these paths. Thus their trigger conditions are satisfied by the merged source change. This verifies **configuration**, not the GitHub scheduler's actual run/conclusion.
- `.github/workflows/source-snapshot.yml` declares `pull_request` and `workflow_dispatch` but not `push`; a fresh main-push source-snapshot artifact is **not automatically expected**.
- The available connected GitHub `fetch_commit_workflow_runs` action explicitly filters returned runs to **pull-request-triggered** workflows. It returned no results on the new merge SHA, and `get_commit_combined_status` returned `statuses=[]`. Neither response covers GitHub Actions main-push check runs; neither is proof of absent or passing CI. Direct public web lookups for the new repository's Actions page were unavailable through this runtime. Therefore **both new push workflow conclusions and both original post-merge archive audits remain unverified.**
- The source-equivalence finding strengthens the relationship between pre-merge review/CI and merged code but **does not satisfy** the explicit fresh `main` Linux/Windows/PyVista release gate or authorize reporting the post-merge artifacts as audited.

**Current post-merge disposition is unchanged: source integration complete; fresh main CI and archived evidence gate OPEN.**


## Follow-up 02 — FINAL post-merge release qualification and original evidence ZIP audit (2026-11-16 Asia/Kolkata)

**FINAL DISPOSITION: RELEASE QUALIFIED within declared scope.** This replaces, but does not erase, the earlier "CI unavailable/unverified" factual snapshot. The source code was not modified for this qualification. The exact Git merge source/tree equivalence remains proven in Follow-up 01.

### Exact merged-main Actions runs and original logs

- **Merged SHA:** `bf6a18399c604136dd363ad94d40557dbe2c2543`. Queried original GitHub API workflow-run collection with explicit `head_sha` because the narrower connected action initially surfaced only PR-triggered runs. It returned the actual **event=push, head_sha=merge SHA, status=completed, conclusion=success** for both workflows.
- [Main release candidate clean-install #43879485356](https://github.com/physicsvigilante/emfeeld/actions/runs/43879485356), run attempt 1, completed SUCCESS: Ubuntu 24.04 job **133341223835** and Windows 2022 job **133341223401**, both Python 3.13.5. Original logs and subsequently original archived test logs report per OS **1,435 headless passed**, **18 historical behavioral passed** (plus one frozen whole-file test deliberately deselected), **33 real-PyVista tests passed**, and a separate focused **33-pass ensemble test rerun already counted inside the headless 1,435**. No multiplication of duplicate test memberships across runs.
- [Main real-PyVista #43879485317](https://github.com/physicsvigilante/emfeeld/actions/runs/43879485317), attempt 1, completed SUCCESS, Linux job **133341222495**; original log gives **1,435 passed** plus nine qualifying offscreen scene render cases and successful programmatic slider-event checks. No manual Windows pointer operation is inferred.
- The original release workflow logs include a same-author independent-expression E1/G1/T1 reference result with **20 static +12 trajectory comparisons and two expected unavailable**, not reclassified as a new independent reviewer numerical derivation.

### Original post-merge uploaded artifacts, independently downloaded and read byte-for-byte

| Artifact | GitHub ID | Original ZIP SHA256 from uploaded bytes | ZIP entries | Integrity |
|---|---:|---|---:|---|
| [Linux release ZIP](https://github.com/physicsvigilante/emfeeld/actions/runs/43879485356/artifacts/14231912437) | `14231912437` | `da900d739a0f6a44955a76d2bfffe0fa2a81fcd7f481e5dc3977a47600eabf3e` | 2,151 | all unique, CRC clean |
| [Windows release ZIP](https://github.com/physicsvigilante/emfeeld/actions/runs/43879485356/artifacts/14232926188) | `14232926188` | `2f5a4c398fa0d98ef7dfb5d0bf1cff417adc7bdadb11edbbfec6a49bbae07b57` | 2,151 | all unique, CRC clean |
| [Linux viewer ZIP](https://github.com/physicsvigilante/emfeeld/actions/runs/43879485317/artifacts/14231463772) | `14231463772` | `40f5f15dfd5fbc6573bd3a6e3041ada4a35771703869a87667a6382dd216e630` | 22 | all unique, CRC clean |

**Archive-bound evidence checks performed separately on both original OS ZIPs:**

1. Compared complete downloaded ZIP SHA256 to the original GitHub job upload-log digest and verified **all** 2,151 entries are unique with clean CRC and no path traversal. Exact archived `head-sha.txt` equals the merged SHA, not a former PR commit.
2. In each E1, G1 and T1 case, verified `ensemble/summary.json` is sealed, baseline complete and both declared sibling revision decisions **accepted**, both native runs complete. Outcome E1 **complete**, G1 **partial**, T1 **complete**. G1 partial is due solely to two unavailable requested cross-comparisons for bodies absent from baseline; not a numerical pass invented for missing data.
3. Verified **21 complete top-level SHA256 evidence inventories** and **12 nested native integrity inventories** *per operating system*, by independently hashing every referenced original archived file. Checked exactly **12 complete native runs** per OS (three original templates, three fresh baseline runs, six actual sibling runs), with their **60 raw input SHA256 bindings** to complete investigation/analysis/presentation/reference/revision bytes.
4. Cross-checked all **six sealed comparison request/result pairs** to the exact baseline and sibling `run.json` raw SHA256 and verified request/result hashes, declared pair identity and ordered saved outcomes. The exact comparison entries total **32 `ok` and two `unavailable`** per OS, both with native `unknown_operand` codes for *different* absent G1 body IDs (`body-3-absent` and `body-4-absent`).
5. Verified raw original `store/proposals/<sha256(proposal_id)>/proposal.json` bytes against the six stored `decision.proposal_sha256` values and matched archived store decision records to the sealed member decisions; request proposals match the archived store bytes semantically. No accepted child ID was silently retargeted.
6. Verified embedded test logs and same-author reference summary in each archive: headless 1,435, behavioral 18, viewer 33, focused 33 (duplicate of headless membership); source/RK4 reference 20 static, 12 trajectory, two expected unavailable. This verifies recorded results and sealed archived provenance; it is not a new independent solver run.
7. For the separate PyVista artifact, verified `report.json` binds the **same merge SHA**, reports PASS for nine source/render cases, and all **17 original 1200×850 screenshot PNG SHA256s** equal their saved `png_sha256` fields. Each image decoded and had nonblank visual content. A visual contact-sheet was reviewed in this chat; the manual desktop/Windows interaction limitation remains unchanged.

**Audit harness note:** The first read-only local audit assertion was mistakenly too specific about which G1 body was absent (`body-4` only); an initial test-log parsing pattern also omitted the legitimate `1 deselected` marker. Inspection of raw archives revealed that one G1 branch requires `body-3`, the other `body-4`. Only the *separate audit script* was corrected; original downloaded ZIPs, job logs, source commits and archived evidence were never changed. Rerunning the corrected audit passed on all three original artifacts. This is an audit-harness correction, not a source defect.

**Machine-readable independent archive audit summary:** local JSON `emfeeld-pr23-postmerge-audit.json`, SHA256 `c95f38fd98825c41ccedba0eb3e8fe4a4c3fb82efef9f99586132453fa1138bd` (available in this chat's generated files; not a GitHub required status check). ZIP digest attestations are unkeyed, not authenticity against an attacker who can replace and reseal every file.

### Final limitations and gate disposition

- **Passed:** exact merged code identity; independent Chat B R2 correction-scope pass; fresh actual `main` Linux/Windows and separate PyVista workflow conclusions; archived numerical scenario evidence status, saved hash/inventory integrity, separate current-commit native E1/G1/T1 same-author source-reference check and complete two-OS release archive read-only re-audit.
- **Still not claimed:** independent human physicist certification, separate full numerical solver verification by a new evaluator, manual Windows desktop/mouse behavior, actual classroom usefulness, conductor response, full electromagnetic dynamics, malicious-author tamper resistance, or distributed ACID guarantee. Partial G1 is the **intended honest unavailable result**.

**All requested PR #23 release gates are closed within their stated test/evidence scope.** The original central review-01 and review-02 findings and responses remain historically unchanged. Future new features must begin from the actually merged and now qualified `main` SHA, on their own branch with their own appropriate risk review.
