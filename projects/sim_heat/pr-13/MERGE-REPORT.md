# SIM_HEAT H2-01 PR #13 — owner-approved merge and post-merge verification

**Recorded:** 2026-11-15. **Status:** MERGED, BOTH POST-MERGE CI WORKFLOWS PASS. This is Chat A's source-release/evidence record, **not** a new Chat B review, human teacher validation, physical measurement authentication, or full native scientific qualification.

## Explicit owner authorization and exact source identity

- The owner explicitly answered **“approved”** to Chat A's single-purpose question whether to merge [SIM_HEAT PR #13 — Thermal Bridge Explorer](https://github.com/physicsvigilante/sim_heat/pull/13) into `main`. This is separate from Chat B's review verdict; no merge was inferred from reviews.
- Before merging, the source PR remained draft/unmerged and mergeable, with base `main` at `ecebc38dd3f6eaffd297bd3df97a0883e591c6ac`, head `e8449989ba55a972976ebba7e9708bc4e2351a18`, tree `c342ace7233dd112fa494be91785f79f23debeca`. The exact head had passed [original viewer CI 43736122931](https://github.com/physicsvigilante/sim_heat/actions/runs/43736122931); the independently authored [Chat B Review 01](reviews/review-01-chat-b.md) had scoped R1 PASS at exactly this head. The hub status still distinguished reviewer PASS from pending owner merge approval.
- The developer marked that draft PR ready for review as a GitHub merge prerequisite; the source head/base/mergeability were checked again before sending the **GitHub merge API** request with `expected_head_sha=e8449989ba55a972976ebba7e9708bc4e2351a18`. GitHub returned `merged=true`.
- **Final merge commit:** [`a33a0d79da405ff4c7191b9bfb94e096b10e2a9f`](https://github.com/physicsvigilante/sim_heat/commit/a33a0d79da405ff4c7191b9bfb94e096b10e2a9f), verified as current `main` and PR #13 `merge_commit_sha`.
- **Exact merge parents in order:** prior `main` `ecebc38dd3f6eaffd297bd3df97a0883e591c6ac`, and the reviewed source head `e8449989ba55a972976ebba7e9708bc4e2351a18`.
- **Final Git tree:** `c342ace7233dd112fa494be91785f79f23debeca`, byte-identical to the reviewed head's tree; **no post-review source edits occurred during the merge**. Only PR #13 was merged; previous experimental PRs and native artifacts were not merged or rewritten.

## Two independent workflow invocations on actual new main commit

Both GitHub Actions workflows were triggered by the merge's `main` push, and both completed `success`, **attempt 1**, with **head SHA exactly** `a33a0d79da405ff4c7191b9bfb94e096b10e2a9f`. They are automated author/source CI, **not** new independently performed Chat B test runs or native OpenModelica launches.

| Check | Post-merge source-run evidence |
|---|---|
| H1 offline verification | [run 43739616921](https://github.com/physicsvigilante/sim_heat/actions/runs/43739616921), **PASS**; 151/151 H1 tests + 4/4 original analytical tests; bridge offline admission and checking-only reference preparation |
| H1 evidence ZIP | [artifact 14171449614](https://github.com/physicsvigilante/sim_heat/actions/runs/43739616921/artifacts/14171449614), 647,985 bytes, original ZIP SHA-256 `224903a388338239d695d230a45b1f1f2c7bcf028de8bc9f985898db1df4849c` |
| Viewer + real Chromium | [run 43739616895](https://github.com/physicsvigilante/sim_heat/actions/runs/43739616895), **PASS**; 151/151 H1 tests + 4/4 analytical tests + **7/7 viewer tests** and real browser desktop/mobile signed-arrows, time controls, playback, SHA-refusal and screenshot checks |
| Viewer evidence ZIP | [artifact 14170889255](https://github.com/physicsvigilante/sim_heat/actions/runs/43739616895/artifacts/14170889255), 669,618 bytes, original ZIP SHA-256 `4a06e53d3e648091819c682846be2963708a6f4dc22c144241008fa1f4787f05` |

**Downloaded evidence recheck (performed by Chat A):** Both original ZIP sizes and SHA-256 digests independently recomputed to exactly the GitHub artifact records; ZIP CRC checks passed; each archive's `head-sha.txt` agrees with the merge SHA. The H1 run saved the expected test logs, dependency identities and bridge admission/reference bundle. Viewer archive saved `h1-tests.log` (151 tests, OK), `analytical-tests.log` (4 tests, OK), `viewer-tests.log` (7 tests, 0 fail), `browser.log` (desktop/mobile, arrows, reversal, time control, playback, wrong-file SHA refusal PASS), `bridge-desktop.png`, `bridge-desktop-refusal.png` and source/dependency identity records. This is integrity checking of archived CI evidence, **not proof of independently authenticated physical instrument readings**.

**No native OpenModelica compilation/launch on either post-merge job.** Network-capable package installation in CI is distinct from native heat-simulation execution and is not air-gapped.

## Review chain and outstanding limitations

- [Review 01 (Chat B, separately authored)](reviews/review-01-chat-b.md), initial reviewed head `e8449989ba55a972976ebba7e9708bc4e2351a18`, Git blob `d256b370f152493ff492c5af21b9cbb5e54273dd`, first committed at [`26b79481b6090483943177586f5fab1773692d6d`](https://github.com/physicsvigilante/review_sandbox/commit/26b79481b6090483943177586f5fab1773692d6d): **PASS strictly for focused R1 presentation scope**. Independently cross-checked all 23×12 preview numeric entries to original archived native CSV, signed rod and stored-energy relationships over all 2,001 original samples, and ran 7 separate Node controls; not a second native solver or expert classroom certification.
- [Chat A response 01](responses/response-01-chat-a.md): the sole minor F-01 suggestion is a future **explicit boundary power sign note** (“+ supplied to network; − absorbed”) rather than any confirmed wrong value or sign. It was **acknowledged/deferred**, not represented as fixed in this reviewed SHA. Chat B's real-browser navigation was blocked by an administrator policy; **no independent browser success is claimed**. Automated source CI's real Chromium tests and screenshots were green.
- The earlier viewer [failed first CI run 43735810229](https://github.com/physicsvigilante/sim_heat/actions/runs/43735810229) remains intact; subsequent successful source CI 43735933432 and final premerge CI 43736122931 retain their exact histories and hashes.
- Modelica library, native runner, original source/verification semantics and immutable historical evidence remain unchanged. Native bridge data is historically **`diagnostic_only` and `nativeQualified=false`**, not externally authenticated independent measurement. The viewer is **read-only**: 23 selected saved samples and optional byte-hash-approved import of original 2,001 canonical samples; logical network not fabricated geometry; no physical interpolation or new solver.
- Independent R3/reference-error acceptance, complete native qualification, separate-author C1, general graph authoring/visualization, teacher/classroom effectiveness and full textbook-answer coverage remain outside H2-01. This source merge does not close any of those other gates.

## Closure

**H2-01's scoped source feature is merged and both post-merge CI workflows passed.** Original reviewer report, development failure, source/run identities and data/evidence limits remain preserved. The central status is updated separately without overwriting historical reviewer findings. Future viewer changes use their own risk-based PR/CI/review process; no additional work is implied for this exact completed source feature.