# M31a PR #71 — independent targeted R2 follow-up review 02 (F-01 only)

**This packet is authored by the implementation agent, NOT an independent review. DO NOT merge source PR #71.**

Read the original [independent review-01](reviews/review-01-chat-b.md), [review request](REQUEST.md), [central protocol](../../../PROTOCOL.md) and original exact-source [frozen M31a charter](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/docs/m31a_charter.md). **Review the exact NEW source commit, not the old review-01 pin**. First verify the live PR head and its Git tree.

**Source PR:** https://github.com/physicsvigilante/conductor_sim/pull/71  
**NEW exact source HEAD:** **c190e0929e727d35db2337efc366cf9676fc36f3**  
**NEW actual Git tree:** **df48e1eb10536285818abfafd3f0628436247882**  
**Original review-01 source:** e8970e26b91f6f8dfe3bd8bffcaf8f181449870b (tree 15e658dfae00289e27a577f5f1df1c340e8e1c72)  
**Base/main:** 293d4b22a6eeb4bc56a5598d8b6935ef91f19826

The original independent review verdict was **CHANGES-REQUESTED** for **one result-evidence validation blocker F-01**. It found no demonstrated physical-law/integrator defect and independently validated actual coupled native physical trajectories. That historical verdict must remain unchanged and cannot be retroactively rewritten as PASS.

## Exact narrow source correction to assess

[Compare original reviewed head → corrected current head](https://github.com/physicsvigilante/conductor_sim/compare/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b...c190e0929e727d35db2337efc366cf9676fc36f3)

The source correction consists of exactly three changed paths: src/conductor_sim/coupled_physical_family.py, tests/test_m31a_coupled_physical_family.py, and docs/m31a.md. No original M20b/M22a/M28a/M29a physical laws, numerical RK, source qualification, force, or guard code changed.

Review the new logic in CoupledPhysicalRun.__post_init__, CoupledPhysicalRun.as_dict, and run_coupled_physical_family:
- Reject a manually constructed/non-native trajectory object even if it supplies fake spec, termination and as_dict attributes; require exact TestChargeMotionResult and correctly bound scenario identity.
- Explicitly admit only native duration and source-guard terminations. An arbitrary unknown code cannot be classified as physical censorship in the runner or accepted in a typed result.
- Check the actual immediate-parent original native TestChargeMotionResult, and compare all stored rows **exactly** to the unchanged _shared_rows(actual physical immediate parent's trajectory, real child trajectory), including literal same original saved SI times. No invented/omitted or doctored comparison rows accepted. Revalidate before detached JSON export because tuple-contained dicts are mutable.
- Ensure the new validations don't turn legitimate source-guard termination into a refusal, don't break atomic jointly valid +z source/probe translation or the original nested source revision SHA and genuine native samples.
- Consider whether merely requiring exact TestChargeMotionResult type with modified fields internally covers the declared F-01 trust boundary adequately. The original reviewer explicitly requested *typed result evidence authentication*, not absolute cryptographic authentication against all malicious Python mutation.

Five new targeted tests exercise non-native impostor, unknown terminal status in both result and patched runner, invented/missing comparison timestamps, mutable post-construction comparison rows, and genuine native guarded history plus simultaneous +z translation. Evaluate the tests' actual results and try at least one independently written adversarial variation if possible.

## Verified developer exact NEW-head CI, NOT an independent verdict

**16/16 complete successful source HEAD workflows at c190e092...:**
- [Python 3.10 and 3.12 #43927024438](https://github.com/physicsvigilante/conductor_sim/actions/runs/43927024438): **1,891 passed, 97 real-FEMM-only skipped, 16 warnings per interpreter** (five more passing tests versus original review head).
- [Real FEMM5 #43927024562](https://github.com/physicsvigilante/conductor_sim/actions/runs/43927024562): **97 passed**, historical conductor nonregression.
- [Full real Chromium and historical visualizations #43927024565](https://github.com/physicsvigilante/conductor_sim/actions/runs/43927024565): PASS; M31a adds **no new HTML**.
- Additional exact HEAD push Python workflow #43927011449 successful.
- Original independently audited native rod/point/gravity + mass coupled physics transfer on the prior source head remains historical physics evidence, NOT a claim of native rerun on new head; new head changes only evidence validation and tests. The current exact-head full Python/visual/FEMM suites ran on the new SHA.

## Required independent reviewer judgment

1. Verify exact live source head and actual Git tree, and inspect the old F-01 finding and corrected-source diff. If the head changed, mark this packet stale.
2. Reproduce or independently reason through the three original F-01 forgery probes (fake non-native trajectory, unknown termination, invented comparison timestamp) on the NEW actual source. Check post-construction mutation before detached JSON and the valid source-guard/physical translation controls. Distinguish source execution from CI-log inspection.
3. Inspect numerical result status and actual full-model source binding: a legitimate accepted world should remain represented faithfully, not be rejected under its authentic native output.
4. Verify exact-source 16/16 CI and limitations, and ensure no unreviewed physical changes were smuggled into this single correction.
5. Independently publish a **NEW**, attribution-preserving report to **physicsvigilante/review_sandbox/main** at **projects/conductor_sim/pr-71/reviews/review-02-chat-b.md**. Use **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE** for the scoped F-01 closure, with source SHA/tree, independent evidence, concrete findings and limitations. Do **not** overwrite review-01.
6. Do not mark ready, change, approve or merge production PR #71. Owner standing permission for a routine expected-HEAD merge applies only AFTER a separate independently authored PASS with no blockers and still-green exact-head CI, followed by postmerge main/CI verification.

A separate ChatGPT review is independent in conversation context, not independent human physics certification or proven different model weights.
