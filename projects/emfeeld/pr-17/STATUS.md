# EM Fields PR #17 — final central R2 review and release status

**MERGED WITH EXPLICIT OWNER APPROVAL; POST-MERGE FULLY QUALIFIED (2026-11-16 UTC).** Exact merged-main commit **1b7d5c652bb635723746b3c6ce77baee536b997e**, canonical Git tree **339224f69e5c671dea83678cdb00845887ce27b4**, identical to independently reviewed source head **62121252c6526c53c29440dcd8f41b6109f70e04**. [Source PR #17](https://github.com/physicsvigilante/emfeeld/pull/17) is closed/merged.

**[Final append-only merge and post-merge qualification report](MERGE-REPORT.md)** records the exact source and merge parentage, owner authorization, Linux/Windows jobs, original ZIP SHA-256/CRC and saved-run inventories, E1/G1/T1 references and residual limitations.

## Independent-context R2 history — retained

- Original [REQUEST.md](REQUEST.md) and [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md) remain pinned to the exact pre-merge candidate; original independent [Chat B review 01](reviews/review-01-chat-b.md) reports **scoped PASS**, no demonstrated blocker/major defect, and retains Git blob **5f6ecd63e2f0dc5df51abb1db355a5cb976c8755** unchanged.
- [Chat A response 01](responses/response-01-chat-a.md) separately triages informational/minor F-01–F-04 without altering Chat B's report or relabeling historical failures. Chat B independently reran 199 tests and performed reviewer-authored adversarial and analytic/RK4 checks, but its attempted full local headless run was incomplete; hosted CI supplies full-suite evidence.
- The owner explicitly authorized merging PR #17 after reviewing the scoped pass. The exact reviewed head was rechecked, converted from draft to ready and merged without source variation. Fresh main-branch CI passed afterward.

## Fresh post-merge verification — green

- [Merged-main Linux + Windows clean-install release workflow #43820500320](https://github.com/physicsvigilante/emfeeld/actions/runs/43820500320) **SUCCESS both OSs** at merge commit **1b7d5c652bb635723746b3c6ce77baee536b997e**. Per OS: **1,342 headless + 18 historical behavioral + 33 real-PyVista = 1,393 suite-membership tests**. The unchanged obsolete whole-file freeze guard was explicitly deselected. The 34 extra focused atomic executions are already among the 1,342 headless tests.
- [Separate merged-main real-PyVista workflow #43820500338](https://github.com/physicsvigilante/emfeeld/actions/runs/43820500338) **SUCCESS**, with 1,342 cumulative tests and real renderer/slider qualification.
- Linux ZIP artifact **14204053864**, SHA-256 **938443ff04644297fb0fc693ea725c1a5c510929ad3c1e2d9d8e565c2a4b5a9f**; Windows ZIP artifact **14204677732**, SHA-256 **c87679f4df03d51456319b668789f9d8f1434911a6a81e672bdfe051bcc90a2b**. Both original ZIPs downloaded and SHA/CRC checked: **1,629 entries each**, no CRC/duplicate-name errors, exact merge checkout pin. Both passed **seven top-level run inventories, six nested native inventories, run input/reference hashes**, and E1/G1/T1 results: three accepted atomic revisions, six complete runs, one deliberate refusal, **36 static checks and seven trajectories per OS**.

## Scope and next gate

**PR #17 release is complete within its bounded physical and evidence contract.** This is independent-context GPT review, not independent human physics certification. Local locks and SHA receipts do not establish distributed/crash-safe transactions or hostile-writer authenticity. Test particles remain nonrelativistic and independent; no conductor/mixed-domain/many-body physics was added. Offscreen rendering is not manual Windows mouse interaction or classroom teaching validation. No saved user model stores or local Conda environment were changed; teaching evaluation remains paused.

Any next physical/evidence feature requires a separate scope and risk class, current-source CI, proportionate independent-context review, and a **new explicit owner merge approval**. This release does not authorize future source changes or installation.
