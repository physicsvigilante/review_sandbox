# PR #33 — author pre-merge compatibility preflight with released PR #32

**Outcome: AUTHOR-ONLY local combined-tree regression PASS; NOT A GITHUB MERGE OR RELEASE QUALIFICATION (2026-11-17).** Source PR #33 still open/draft/unmerged, and independent R2 review has not yet occurred.

## Construction and identities

- Current actual released `main` = PR #32 merge commit `a18c26f050f5320ce8a9d61f7169e32cd6e31f38`, source Git tree `9f59fd94a15a1f0c2759ab8662b23a36a41810da`; fully post-merge qualified separately in [PR #32 release report](../pr-32/MERGE-REPORT.md).
- Exact PR #33 candidate source head `ee54e96488e5cd9d2eb904abf65811627bfcc006`, tree `b8581afb8816052980dc03be27a3ad8acf1dd447`, initially branched from older PR #29 main `3f1ec44a54b24b9f8275a98abf81126a9386bf61`. Original source verified from the corrected-head original GitHub source TAR `b50e944c7025b1c9b748b575fd247207350d3d27b4413a9f4daf1f7123c6e914`.
- A **disposable local directory** was made from the independently reconstituted original merged-main PR #32 source TAR. Exactly the **four added PR #33 files**, with unchanged source SHA256 and no existing path collisions, were copied from the independently reconstituted corrected PR #33 exact source snapshot. No working GitHub branch, sealed saved run, user Conda environment, PR #29/32 input or source record was mutated.
- `git write-tree` of this uncommitted local 356-file composition = **`0a446f52f443ecafbe4fee3625a246737aa84b80`**. This is a **predicted combined tree** from the two precisely identified sources, not yet an actual GitHub merge commit or CI source preview. GitHub's final actual integration must independently verify the composite tree and all source blobs before any release claim.

## Executed compatibility qualification in the local review container

- `PYTHONPATH=src python -m pytest -q -W error tests/test_physics_demonstration.py tests/test_teacher_transfer_pilot_v1.py tests/test_scenario_ensembles.py` -> **113 passed**. Includes both PR #32 physical demonstration tests and PR #33 transfer/legacy ensemble tests.
- `PYTHONPATH=src python -m pytest -q -W error tests` -> **1,515 PASSED in 108.89 s** (exit 0). Original captured full log SHA256 `1004da348a36d75e617351feee79e96d6ddfb8ffc39e992b0901420097a442ad`, first and only completed full local run on this combined source. Earlier PR #33 source-specific 109 focused and 1,511 headless original CI tests are separate inputs, **not additive test counts**.
- This composite does not change the preexisting physics engine or native comparison code. No modified numerical tolerance, fixture SHA, original PR #29 ZIP, original PR #32 demonstration packet, viewer implementation or historical review report. Both source-specific original CI suites have independently passed previously at their own distinct trees.

## Remaining gates

The exact frozen PR #33 candidate `ee54e96...` **still requires one independent-context R2 evidence/interpretation review** using [REQUEST.md](REQUEST.md) and [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md). A reviewer PASS on that old-base source and local 1,515-test overlay are **not** automatic final combined GitHub qualification. If approved to integrate, Chat A must fetch live `main`, verify it has not moved, require correct source identity and full merged-tree compatibility, use a guarded GitHub merge, and separately qualify fresh **actual main-push** Linux/Windows/real-PyVista and original release artifacts, preserving original hashes and honest unavailable G1 results.

Teacher usefulness, blind interpretation accuracy, manual Windows desktop interaction, human physics certification and hostile fully re-sealed hash authenticity remain unestablished.
