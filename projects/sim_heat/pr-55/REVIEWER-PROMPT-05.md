# Chat B — SIM_HEAT PR55 CI-only review cycle 05

**Do not re-review the old physics/source-preview R2 findings; Chat B review-04 already returned SCOPED PASS on the unchanged implementation at `1383a06d...`.** This request covers ONLY the added base-relative CI-workflow changes since then.

Source PR: https://github.com/physicsvigilante/sim_heat/pull/55, still draft/unmerged.

**Latest HEAD:** `47edc006c459d403a16c54ffd63a33f6a6956999`.
**Latest Git tree:** `da5b2ed60dacc2ee2e01d14baf366a3eb89f610e`.
**Old R2-accepted source:** `1383a06d20422182cdae643337d6ddbdd6fcc5ec`, tree `9d1216afcd3f6ba5978a6e4cf0fa79ca69ad5c9d`. **Diff: exactly one changed file, `.github/workflows/source-preview-ci.yml`.**
**Main now:** `7a80bd9c85d67b3a2e353d2a0702c8c5594c20dc` (owner-approved PR56 integration).

**Read full focused R1 request:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-55/CI-APPLICABILITY-REQUEST-05.md

Verify the strict exact original 14 source-preview additions and protected-source refusal remain intact, now using actual checked-out GitHub PR synthetic merge first parent `HEAD^1` for current main while asserting second parent `HEAD^2` equals the PR's authored source HEAD. Branch push preserves original old main lineage. **Important:** the first attempt used `github.event.pull_request.base.sha` and genuinely FAILED at [PR CI 44287156069](https://github.com/physicsvigilante/sim_heat/actions/runs/44287156069): GitHub's PR event base reported OLD main despite new synthetic merge parent. Keep that failure.

Inspect actual completed:
- [push CI 44287688196](https://github.com/physicsvigilante/sim_heat/actions/runs/44287688196), artifact [14418494274](https://github.com/physicsvigilante/sim_heat/actions/runs/44287688196/artifacts/14418494274), SHA256 `d4d984a0e47a1740e748034c5cdafef778dff433f79095803519654ac938444d`, **281 tests passed/one skipped**, six original native diagnostic archive bundles byte-identical, original comparison and source-only preview unchanged, real Chromium PASS.
- [PR CI 44287695317](https://github.com/physicsvigilante/sim_heat/actions/runs/44287695317), actual synthetic merge `ff3b421d60642427432e7477153263940f6b1729`, first parent new main `7a80bd9...`, second parent candidate `47edc006...`, artifact [14419742707](https://github.com/physicsvigilante/sim_heat/actions/runs/44287695317/artifacts/14419742707), SHA256 `1989f20ecdc73cc657d8149a86efbd9143f84423c93e66e459dcc92d537c7d02`, **284 tests passed/one skipped** (plus PR56's 3 already-on-main tests), all six original archives byte-identical, original comparison and source preview unchanged, real Chromium PASS. Both source-preview ZIPs had **47 distinct CRC-valid entries**.
- [audit-core CI 44287695288](https://github.com/physicsvigilante/sim_heat/actions/runs/44287695288) SUCCESS.

The exact allowed source-preview 14-path diff is unchanged on both push and PR synthetic merge; guarded original physics/reference/archived viewer paths must remain protected. Independently probe negative protected-source changes and wrong merge-parent scenarios if possible. Preserve current source-only `not_computed` boundaries; no new native or scientific qualification.

Publish **your own NEW independent review** to:
`physicsvigilante/review_sandbox/projects/sim_heat/pr-55/reviews/review-05-chat-b.md`.
Prior review-01/02/03 are CHANGES REQUESTED on original OLD source. Review-04 is R2 SCOPED PASS on corrected source; leave all unchanged. No PR55/PR54 merge, OpenModelica installation/query/build/launch, frozen-reference regeneration, historical C1 integration, diagnostic promotion or deployment. A scoped CI review pass does not authorize merging.
