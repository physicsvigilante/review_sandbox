# PR #81 · Windows offline study admission

Request an independent R2 review of the offline admission and qualification claims on [PR #81](https://github.com/physicsvigilante/sim_heat/pull/81). Base `6904ec8219be0ddb8ec1635a9d000ddda80307c9`, [source head 538fbb097f81d3c66b458fa7cf99bd35a9ed7aac](https://github.com/physicsvigilante/sim_heat/commit/538fbb097f81d3c66b458fa7cf99bd35a9ed7aac), Git tree `664d64151d09c9cd5cb092ece44dd71876974559`. [Full delta](https://github.com/physicsvigilante/sim_heat/compare/6904ec8219be0ddb8ec1635a9d000ddda80307c9...538fbb097f81d3c66b458fa7cf99bd35a9ed7aac)

## Evidence

The [first Windows run](https://github.com/physicsvigilante/sim_heat/actions/runs/44845390162) failed at `99389140a2993bc8c0db6e4f99b24a5a839959de` on two spellings of the same temp root. Inspect the [successor Windows run](https://github.com/physicsvigilante/sim_heat/actions/runs/44846214173) at the corrected head, including checkout identity and test logs. This workflow exposes the job log and uploads no separate evidence archive. The [original local qualification record](https://github.com/physicsvigilante/sim_heat/blob/538fbb097f81d3c66b458fa7cf99bd35a9ed7aac/qualification/h1_windows_study/OFFLINE-RECORD.md) and its 334/338 full-suite result describe the earlier loader at the source revision named in that record. The successor has a different loader hash and six focused local checks. The broader suite result has not been reattributed to the successor.

## Questions for Chat B

- Exercise the public loader with nested parent revisions and equivalent Windows root spellings. Independently probe authored separators, paths outside the root and link handling as tools allow. Check whether input or revision identities can change, whether valid paths are refused, and whether the corrected comparison preserves containment.
- Verify the N1 manifest and original input bytes against the reviewed base. Inspect the candidate loader pin, original T study admission, binding to the reference facts and the historical checker's exact refusal. Check whether the CI and record support their stated scope.
- Identify evidence gaps separately from confirmed defects. The seven legacy reference failures and eight native-readiness blockers remain open. Use offline checks only. Keep the original reports and both source PRs intact. No OpenModelica installation, query, build or execution.

Report the exact head, commands and limitations with a scoped verdict. Publish your own new `projects/sim_heat/pr-81/reviews/review-01-chat-b.md` in the review hub. No source merge is authorized.
