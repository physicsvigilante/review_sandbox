# SIM_HEAT PR54 — owner-directed teacher workflow merge and exact-main verification

Developer integration receipt, 2026-11-18. This records a GitHub merge and test evidence; it is **not an independent review, physical/numerical qualification, classroom study or authorization for native execution**.

## Authority and reviewed candidate

The owner replied **“continue. keep going”** directly to Chat A's preceding single bounded request to approve merging PR54 with post-merge verification and **no native execution**. Chat A interpreted that instruction as approval **for PR54 only**, recorded the interpretation *before* changing source in [PR54 comment 6978393723](https://github.com/physicsvigilante/sim_heat/pull/54#issuecomment-6978393723). It is not approval for later source merges, deployment, OpenModelica version queries/builds/launches, C1 stack integration, or frozen-reference changes.

Independent [Chat B review-02](reviews/review-02-chat-b.md), original blob `60be108e0c5543ed9b9e66b2f317150871fd0688`, **R1 SCOPED PASS** at source HEAD `6cc3637a8f4009bfb37cafa8ed27edbd049d2d9e`, Git tree **`e354dcf1f64e3e552850422336db237a7e3de556`**, current base prior main `13260a62eb36d58802878c4d3dfb534ad1621f91` tree `2f1da9c596cf44af963dbcefc3ab78d3d780ef3c`. Earlier [review-01](reviews/review-01-chat-b.md) SCOPED PASS remains unchanged and pinned only to its older head `8f6ef1d...`. [Chat A response-02](responses/response-02-chat-a.md) accepted the current-head bounded verdict. Candidate was exactly 11 product/docs/CI paths relative to prior main; H1/experiments/qualification/viewer and all native evidence bytes unchanged.

## Executed merge

[Source PR54](https://github.com/physicsvigilante/sim_heat/pull/54) was marked ready then merged by GitHub's normal merge API with strict expected head `6cc3637...`; no force/status bypass. Exact new main commit:

**`20f5605d28f22d4a7dc86ad478a4cf44347157d4`**

Direct GitHub commit data confirms parents (1) prior main `13260a62eb36d58802878c4d3dfb534ad1621f91`, (2) exact reviewed source HEAD `6cc3637a8f4009bfb37cafa8ed27edbd049d2d9e`. The complete merged-main Git tree remains **`e354dcf1f64e3e552850422336db237a7e3de556`**, exactly independently reviewed and exactly equal to premerge successful PR synthetic-merge tree `d838e8d...`. No unrelated file was folded into reviewed source.

## Tests, original preserved evidence, attribution

Full product browser/source and archive validation was successful on the **identical tree** in reviewed [PR run 44296685585](https://github.com/physicsvigilante/sim_heat/actions/runs/44296685585), and was run again **on exact merged main** by automatic [push CI 44303088073](https://github.com/physicsvigilante/sim_heat/actions/runs/44303088073), with **both candidate exact main and historical baseline matrix jobs SUCCESS**:
- Candidate `134797552313` actual checkout `20f5605...`, tree `e354dcf...`, **293 unique unit PASS + one optional skip** (152 H1, 4 analytical, 62 adapter, 42 Node and 33 product), original six case bundles `BYTE_IDENTICAL`, `nativeExecutedByReplay=false`, conductivity comparison and source-only TEACH_SPLIT3 preview byte-identical. Explorer, root entry, source-preview authored collision/provenance/refusal/import races, and rendered registry/authoring guide real-HTTP Chromium desktop/mobile links PASS; documentation drift/parity PASS. Native runner not invoked.
- Baseline `134797551657` actual checkout prior main `13260a62...`, tree `2f1da9c...`, SUCCESS; **284 PASS + one optional skip**, original six archives BYTE_IDENTICAL, comparisons unchanged. Baseline does not run candidate-only rendered-docs browser step. Counts overlap; do not sum.
- Postmerge [H2 H1 offline 44303087072](https://github.com/physicsvigilante/sim_heat/actions/runs/44303087072), job `134797546664`, **SUCCESS** at exact main `20f5605...` and 152 H1+4 analytical checks. No new native result.

Chat A downloaded/rehashed/CRC-checked full postmerge artifacts and verified all their Git checkout receipts:
- [candidate artifact 14426842783](https://github.com/physicsvigilante/sim_heat/actions/runs/44303088073/artifacts/14426842783): **13,043,647 bytes**, SHA256 **`8f2405431a5d5b52a2852707ee12d4e52d61884b8a24a83cc7efa706f76b344c`**, **54 unique CRC-valid ZIP members**, internal head `20f5605...`, tree `e354dcf...`, scope base `13260a62...`.
- [baseline artifact 14426943418](https://github.com/physicsvigilante/sim_heat/actions/runs/44303088073/artifacts/14426943418): **9,726,202 bytes**, SHA256 **`174c737f6c315987341990d87eade50464ad93d91c01eaa838d16f4359675e67`**, **47 unique CRC-valid members**, internal head `13260a62...` and tree `2f1da9c...`.
- [H1 artifact 14425649344](https://github.com/physicsvigilante/sim_heat/actions/runs/44303087072/artifacts/14425649344): **652,158 bytes**, SHA256 **`8c524cfe04bb2a4713b7f84d7dc7ab75e1184e2241fea061e2ecbfe17133b8f9`**, **9 unique CRC-valid members**, internal head `20f5605...`.

Earlier local exact-source 33 product tests, renderer parity and Chat B independent offline six-case replay retain their separate evidence attribution. Source and tests here are **offline checking and archived playback**, not OpenModelica simulations.

## New capabilities and boundaries

Current `main` now has one navigable start page with (1) original six-case archived diagnostic explorer, (2) saved D2/D2_K2 comparison, and (3) generic H1 *authored-source-only* inspector, alongside a browser-readable canonical capability registry and current, source-backed authoring/refusal guide. Source-only preview requests remain `not_computed` and never supply predicted temperatures/flows. All six original native diagnostics retain `diagnostic_only/nativeQualified=false`. The original frozen C1 precision (80× vs required >=100×) and reference seal failures remain preserved, with nine native public requests uncomputed.

A newly supported combination of the existing H1 domain can be drafted and admitted without writing a custom apparatus-specific solver/viewer; **not** general thermodynamics, a physics calculation, authenticated authoring or complete author-to-native transfer. Teacher usefulness has not been demonstrated in a real classroom.

**PR54 integration and post-merge verification complete.** No additional source merges, native OpenModelica operations, frozen/adopted reference regeneration, historical C1 branch integration, deployment, numerical qualification or status promotion occurred.
