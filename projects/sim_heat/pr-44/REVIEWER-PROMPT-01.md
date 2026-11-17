# Chat B — SIM_HEAT PR #44 read-only artifact intake FIREWALL R2

Continue as independent Chat B reviewer for historical [draft SIM_HEAT PR #44](https://github.com/physicsvigilante/sim_heat/pull/44).

**Review exact source HEAD `331a04c34d465516ffb0ecbb580a334032fa7de2`**, Git tree `fa139f1421c0c763600d1dc3650d152b3157e543`, immediate independently reviewed PR43 base `4e220a152e702c06b07320850f5caacff1091bb3`.

Read the full central packet:
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-44/REQUEST.md

This PR adds FOUR source/test/scope/CI paths only, implementing an **ALWAYS-BLOCKED READ-ONLY inventory of untrusted local native-looking files**. Even **all nine** expected filenames present, with forged owner-signed/native PASS claims, must NEVER become native evidence or satisfy a real owner/host/CAS gate. The program only hashes bounded local bytes and strictly parses JSON for form; it NEVER decodes `model_res.mat` or computes the nine public native readings. Upstream PR41 audit still requires **11 native-release safeguards MISSING**.

Independently inspect/test: absent/partial/full fake file sets, forged owner/native claims, synthetic MAT/CSV bytes, duplicate JSON keys/NaN/oversized/extra `build.mos`/symlink/unsafe labels, no MAT decoder/reference regeneration/native runner/external provider. Reproduce PR43 F-06: forged fake `status`/`fakeCounts` may look well-shaped, but local inventory can NEVER authenticate that receipt. Confirm all outputs `releaseBlocked=true`, `nativeQualified=false`, `nativePublicRequestsStillNotComputed=9`, and no native authority.

Verify exact-head [CI #44062963378](https://github.com/physicsvigilante/sim_heat/actions/runs/44062963378) and [artifact #14319136950](https://github.com/physicsvigilante/sim_heat/actions/runs/44062963378/artifacts/14319136950), **27,322 bytes**, ZIP SHA-256 `a76e171341f5002ff2654bd109952ba20911debfac0bdf78711761866be6152c`, **41/41 CRC valid**, **329/329 OFFLINE tests**. Confirm frozen first-author Modelica/study, owner-approved exact saved PR31 V2 scientific reference raw SHA/seal and historic F0 80×/100× accuracy FAIL and PR32 bitwise regeneration FAIL are preserved.

Commit a NEW independent `projects/sim_heat/pr-44/reviews/review-01-chat-b.md` in `physicsvigilante/review_sandbox` with **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, findings and personally tested vs CI-inspected evidence. A scoped PASS may endorse **only DENIAL/inventory behavior**, not a real native-result verifier, physical qualification, signed owner release, global one-shot lock, executable native plan or production merge.

Do not edit frozen model/physics/approved reference, merge historical PRs, install/query/build/launch OpenModelica, adopt alternate PR32 reference, weaken tolerances or grant owner-native permission. Before real work the owner must separately explicitly authorize the exact named version-query/build/single-launch budget and an independently reviewed trusted source/host/adapter/atomic store.