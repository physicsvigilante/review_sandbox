# Independent Codex review 03 — v27 historical evidence and replay

**CLEARED FOR OWNER DECISION.** Codex, independent reviewer, 21 November 2026. Reviewed PR #195 head `7eb3cc8f3b66d450328fa7cbff329e779b4182cc`, Git tree `1ad8e1094315d8666d1fd4ac968d9e8c5e42856a`. The remaining verification issue from review 02 is resolved on this head. I found no release blocker in the scoped change.

## Independent reproduction

I used the public v27 baseline package and the genuine `native-evidence.json` from the archived original CI run. I separately ran the original executor and core from `e7e2d199b6be25265decb6f7ec7826a3477ab24f`. The resulting summary matched the archived summary by deep equality. Both match the scene hash and upstream PhyDemo pin, and both lack the later endpoint verification. I also ran the corrected public checker against the original core, and rebuilt and ran the current core for positive controls.

| Boundary | Independently observed result |
| --- | --- |
| Current checker, original core | Incomplete, executionPassed false, diagnostics null and observations null. |
| Requested measurements, historical summary | All seven suppressed with null values. |
| Browser execution projection, saved scenario, notebook export | Each refused the unverified v27 evidence. The original input-only portable package could still be opened. |
| Comparison of current and historical snapshots | Current evidence accepted, historical evidence rejected. Every comparison withheld. |
| Two-entry notebook replay, one current and one historical | One qualified and one incomplete, overall `partial-native-incomplete`. The incomplete row had no current native summary, its qualified results were null, and no comparison was performed. |
| Two-sample Beam-width sweep, historical 40 mm and current 20 mm | One completed and one failed sample retained. Plotted crossing values were null and 8. The historical raw report was absent from the sanitized execution passed to the sample callback, and observations were null. |
| Two current notebook entries | Both qualified, with seven qualified requested measurements each. |

I repeated the negative replay, comparison, and sweep checks using the genuine archived envelope, the newly reproduced legacy envelope, and the current checker's incomplete result from the older core. No previous detector total was promoted to a current measurement. The current snapshot and notebook checks accepted verified evidence. Existing focused tests also cover complete current runs with unavailable hit positions above the retention limit.

## Source, frozen evidence and tests

The change from `6a6b4ea4a9d81f3e1dbda3d3ba4b602c5f34a8cd` adds a schema-27 evidence predicate and applies it at native checking and summary-consuming boundaries. I compared both Git trees. The optical admission and runtime endpoint audit, adapter, upstream pin, historical evaluation files, research protocol and fixtures are byte-identical across this delta. Review 02's independent optical and browser results apply to those unchanged components.

I recomputed the historical records from Git blob bytes. The original transfer freeze SHA-256 remains `02c843efbdf786ce6d5a2c21f8539f3f839dce62ade0afc707e7edfbf822137e`. The reserved input remains `8e8deca8af9919cb56906c2491eb2ac2e8de50f833e30134272b1a074213c756`. The eleven-case protocol remains `398ea13f95cf9a0d6339b33466c4fc7688960a439fcb7f8386a4ad2f09a833f7`. Both historical-to-current links for the two intentionally changed consumers matched their recorded SHA-256 values.

| Consumer | Prior source SHA-256 | Reviewed source SHA-256 |
| --- | --- | --- |
| exploration.js | `855f1b3dc786852f881e75c761e191515b6fefe87bdbb82dcca3711481e02dab` | `eadaec97de4f2a7f4780d40694bc1cce2f5a8798be62ac611097060f043f6f5d` |
| scenario-comparison.js | `7852e615d59b88ed7eba1ba9bc15e450cdfa49eda7b04f5ee2398df334452bbf` | `df3e8b88c40964191bae567ae3e48ec876ba64f817ef44ef02a1e30852ff58ed` |

I rebuilt the headless bundle using Node 24.19.0 and pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`. All **33 focused tests passed**, spanning v27, notebook export/replay, sweep snapshots and historical detector transfer. An initial Windows Git archive had CRLF conversions and failed one historical file-hash assertion. I restored the isolated export from Git blob bytes, rebuilt and reran both the focused tests and independent controls successfully. No tracked project source or frozen record was edited.

I verified eleven successful workflows for the exact source head and read the optical job log showing 1,145 Node passes. The full-suite count is CI evidence. My local work on this delta covered the summary and replay paths above. Owner release authorization and post-merge verification are separate.

[Reviewed delta](https://github.com/physicsvigilante/opticsim/compare/6a6b4ea4a9d81f3e1dbda3d3ba4b602c5f34a8cd...7eb3cc8f3b66d450328fa7cbff329e779b4182cc) · [Review 02](https://github.com/physicsvigilante/review_sandbox/blob/f0ff592afcd047ef98fed67c571a8925c0858d78/projects/opticsim/pr-195/reviews/review-02-codex.md) · [Exact-head optical CI](https://github.com/physicsvigilante/opticsim/actions/runs/44843207328/job/136656470106)
