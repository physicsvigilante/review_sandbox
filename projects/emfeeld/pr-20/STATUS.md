# EM Fields PR #20 — merged, post-merge release qualification pending

**MERGED on standing owner authorization; fresh main-branch qualification IN PROGRESS (2026-11-16, Asia/Kolkata).** Do not call this release fully qualified until both fresh workflows pass. The owner's instruction to continue building autonomously supersedes routine merge-approval requests for reviewed, bounded changes, but does **not** waive independent R2 review, unaddressed blocker gates or materially changed physical scope.

## Exact approved reviewed source and merge

- [Source PR #20](https://github.com/physicsvigilante/emfeeld/pull/20) is **merged**. **Merge commit f0fc993dae1831432ca43b651a12e64fa0b2fdd5** is main, with canonical Git tree **a9cee83857195f0c2d4c36d4741559094fad64bd**, identical to independently reviewed exact source head **fb16a233fb73d7e749e08029c848b4b99c5158a7** and CI preview checkout **fedcba18a8b5713e0a0666c5bb213484220da7f9**. Merge parents: formerly qualified main **1b7d5c652bb635723746b3c6ce77baee536b997e** and that exact review-passed source commit.
- [Chat B review 03](reviews/review-03-chat-b.md) is **scoped R2 PASS**, blob **b2afd7ad8db4b841ec87addf172f18724554fb2d**, covering R2-NEW-01 and bounded F-01/F-02/F-03 regression protections at exact source head/tree. [Chat A disposition](responses/response-03-chat-a.md) accepts this bounded conclusion. Original independent [review 01](reviews/review-01-chat-b.md), blob **3ecb837b03bd6c1644f289a50fa5b33794212fb5**, and [review 02](reviews/review-02-chat-b.md), blob **9cbe288105c0b31f4848ec71f1bd34bbcb6316a0**, remain historically **changes-requested** on their prior SHAs. Neither report or failed attempt is altered.
- Frozen design-only PR #19 is separate; its exact document bytes are present in merged PR #20. Do not count this implementation merge as approval for expanded physical laws, solver or classroom evaluation.

## Pre-merge evidence

- [Exact-head Linux/Windows full clean-install CI #43846152822](https://github.com/physicsvigilante/emfeeld/actions/runs/43846152822) **PASSED both OSs**: per OS 1,402 headless + 18 historical behavioral + 33 real-PyVista = 1,453 suite-memberships; the 60 separately rerun focused tests were already part of the headless definitions. The unchanged obsolete whole-file freeze assertion remained deselected.
- [Separate real-PyVista #43846152829](https://github.com/physicsvigilante/emfeeld/actions/runs/43846152829) **PASSED**, including real rendering and slider-event checks.
- The original pre-merge Linux/Windows release ZIPs were downloaded, SHA256/CRC-checked and had source/native inventory and E1/G1/T1 reference evidence audited. Original first failures and Chat B negative cases remain preserved in exact-bound records.

## Fresh post-merge qualification — PENDING

- [Fresh merged-main Linux/Windows workflow #43853253048](https://github.com/physicsvigilante/emfeeld/actions/runs/43853253048): **IN PROGRESS**.
- [Fresh merged-main real-PyVista workflow #43853253096](https://github.com/physicsvigilante/emfeeld/actions/runs/43853253096): **IN PROGRESS**.
- Both are triggered by exact merged-main commit **f0fc993dae1831432ca43b651a12e64fa0b2fdd5**; qualifying the source PR head before merge does not substitute for merged-main checks.

**Next:** confirm full Linux/Windows and rendering job outcomes, independently check published artifacts and saved source-native run inventories, then create an append-only `MERGE-REPORT.md` and reconcile final STATUS. Do not call release complete before then. All physical laws and numerical tolerances are unchanged; this feature compares distinct independently simulated scenarios rather than modeling the transition. Unkeyed hashes are not hostile-writer authentication, and independent-context ChatGPT review is not human physics certification. Local Conda/user studies and paused classroom evaluation remain untouched.
