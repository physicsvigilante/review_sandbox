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
