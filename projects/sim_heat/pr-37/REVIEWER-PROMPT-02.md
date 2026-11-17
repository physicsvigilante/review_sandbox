Continue as independent Chat B reviewer for SIM_HEAT.

Review **draft PR #37** at corrected exact source **`2f2b8d5008f51b9972897058328aed8cbcbfbbce`** (Git tree `de397fe3af9bb3385c4ef55354e49c33571dc99b`), not the original review-01 source `d1d6a32252b41dabad832668de642ecaf475a2a3`.

Read:
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-37/REQUEST-02.md

Read your original independent CHANGES REQUESTED report at `projects/sim_heat/pr-37/reviews/review-01-chat-b.md` and Chat A's response-01. This is a **focused R2 re-review of F-01–F-04**, not a new native simulation or physics review. The new diff changes only five F-02 offline staging, testing and scope files.

Independently reproduce on-disk:
- duplicate permission/state JSON keys (including nested SHA keys) and NaN refusal;
- coordinated disabled F-02 plan and staged-manifest hash replacement (must refuse against independent Git-blob and original SHA pins);
- copied/renamed stage label and symlinked staging parent refusal;
- `23.0`/`true` source-pin counts and numeric zero in place of JSON `false`.

Verify the original staged four scientific input hashes, V2 reference exact raw SHA/seal, no reference regeneration or native plan, and the exact-head [CI #44028343008](https://github.com/physicsvigilante/sim_heat/actions/runs/44028343008) / [artifact #14304102592](https://github.com/physicsvigilante/sim_heat/actions/runs/44028343008/artifacts/14304102592), full ZIP SHA-256 `256da986efc326fe806185dd36cf42ba5c652c268efef7d28ec2351dafa53191` (35/35 CRC; 217/217 offline tests).

Write a **new independent** `projects/sim_heat/pr-37/reviews/review-02-chat-b.md` in central review_sandbox with scoped PASS, CHANGES REQUESTED, or INSUFFICIENT EVIDENCE, independently performed checks vs CI observations, and residual trust/native gates.

Do not overwrite review-01, modify original files, merge historical PRs, waive the frozen 100× policy, substitute regenerated references or run OpenModelica. The native one-shot launch requires a separate future owner authorization.