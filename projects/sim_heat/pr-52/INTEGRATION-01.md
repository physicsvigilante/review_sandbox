# PR51 + PR52 — owner-approved integration and post-merge verification

Recorded by Chat A on 2026-11-18. This is a developer integration receipt, not a new independent review.

## Authority and immutable review mapping

The owner replied **“approved and keep working”** to the explicit proposal to integrate the corrected PR51+52 candidate into main with post-merge verification, no native execution and no historical C1-stack merge. Approval was recorded on source [PR52 comment 6969052557](https://github.com/physicsvigilante/sim_heat/pull/52#issuecomment-6969052557) and [PR51 integration comment 6969096309](https://github.com/physicsvigilante/sim_heat/pull/51#issuecomment-6969096309).

Original PR51 review remains CHANGES REQUESTED at `52d693a748ad3709c99215bac0a5840a236937a6`. Independent PR52 report blob `410347813b523ef43ee8082cc236d0631ec6b7b2` remains SCOPED PASS at `e78ec2ccb2f8f97bbc1b282ec6bbe2847c1e1603`, tree `2ad10a1679d528f88030494f0349171502ef8e0f`. No reviewer file was edited or retroactively promoted.

## Executed merges

1. PR52 merged into the PR51 audit branch at **`618835ab96ce2886a7f6889cb8793365595b5bbb`**. Its complete Git tree equals the reviewed PR52 tree exactly.
2. After fresh successful integration CI, corrected PR51 merged into main at **`4162c3d47016150076b226ebe2585073a785547a`**. Its complete Git tree again equals **`2ad10a1679d528f88030494f0349171502ef8e0f`**.

Both merge API calls supplied the expected source head; main's pre-merge base was `c06fb5395781482bd6bbe055d10bc10cdf3bba8d`. Combined change is fourteen paths. The defective old PR51 head was not merged by itself. PR50 and the historical C1 stack were excluded.

## Fresh integration and post-merge evidence

### Integrated audit branch

[Run 44237530254](https://github.com/physicsvigilante/sim_heat/actions/runs/44237530254), job `134577160232`, SUCCESS at `618835ab…`. Artifact **14398026681**, **5,873,987 bytes**, **33 distinct CRC-valid members**, SHA-256:

`9a4043a268e692a0b0ab18eeadbba1a7482e9ce821ad20288427eb91a3773caa`

Chat A downloaded and rehashed the ZIP, checked all CRCs, actual head/tree, fourteen-path diff, unit logs, six BYTE_IDENTICAL original archive replay records and browser PASS. Unit total **249 passed, one optional skipped**, zero failures. Comparison bytes unchanged.

### Automatic main workflows

All three push workflows on exact main `4162c3d…` completed SUCCESS, as verified from GitHub run metadata:
- [44237857837](https://github.com/physicsvigilante/sim_heat/actions/runs/44237857837), generic explorer;
- [44237853722](https://github.com/physicsvigilante/sim_heat/actions/runs/44237853722), H1 offline integration;
- [44237853601](https://github.com/physicsvigilante/sim_heat/actions/runs/44237853601), original viewer.

Their suites overlap; these are not additional unique scientific validations.

### Complete exact-main archive replay after merge

The next product candidate's [CI run 44238734097](https://github.com/physicsvigilante/sim_heat/actions/runs/44238734097) includes a **separate baseline job `134581100335` checking out exact merged main `4162c3d…`**. It completed SUCCESS: **249 passed, one optional skipped; all six original bundles BYTE_IDENTICAL; comparison unchanged; full explorer Chromium smoke PASS**.

Baseline artifact **14398721933**, **5,873,775 bytes**, **33 distinct CRC-valid members**, SHA-256:

`27fc39b8971cc7525ae5cf2e97750c68a37d468435d91291cfd2738f0c15b0cd`

Chat A downloaded/rehashed/CRC-checked it and inspected logs and replay. `head-sha.txt` is `4162c3d47016150076b226ebe2585073a785547a`, `head-tree.txt` is the reviewed `2ad10a…` tree, and `source-diff.txt` is empty. The workflow event/artifact name contains the later product candidate SHA; **that is not the baseline's actual checkout**. New navigation tests are intentionally skipped in this baseline because those files are not yet on main, distinct from the existing optional unittest skip.

These were hosted executions inspected by Chat A, not a claimed local full-suite rerun. No new native execution occurred.

## Result and continuation

**Corrective integration is complete and post-merge verified.** The six original results remain diagnostic-only and nativeQualified=false. Source identity/integrity checking is not arbitrary-archive authentication. Original C1 scientific failures, frozen references and uncomputed native requests remain unchanged.

Continued product work is now [draft PR53](https://github.com/physicsvigilante/sim_heat/pull/53): static explorer entry, current capability registry and navigation tests, separately based on this merged main. Its focused R1 presentation review is not a reopening of the unchanged physics audit and does not authorize merging that new candidate. No OpenModelica query/build/launch, native runner, frozen-reference regeneration, historical C1 merge or deployment was performed.