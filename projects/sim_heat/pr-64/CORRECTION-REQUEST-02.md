# SIM_HEAT PR64 — CORRECTION-REQUEST-02: narrow R2 review of five design findings

**Decision sought:** SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE for only the corrected H1-N3 future migration DESIGN, not native execution, scientific reference certification or merge.

## Source identities and prior findings

[DRAFT PR64](https://github.com/physicsvigilante/sim_heat/pull/64), corrected HEAD **0cf275241e718fbcd2b2d2c1f7761565c7c06a92**, whole tree **4f253f1959797362d68ad4e153552b776ff82f33**, stacked on reviewed-in-scope but still-draft PR63 HEAD **6baba681ae1680e2fcae1ea8efbf0953afcb031b**. Old independent [review-01](reviews/review-01-chat-b.md), blob 113b917d8761881e345d5344919317a8654a4a00, returned CHANGES REQUESTED on OLD HEAD f0d863e8e1dcc44e89d1ab7e1a2f377d89d9714f, tree 99136556b49e20ff3e310b6bde408101528e6b14; original text stays unchanged. New [Chat A response-01](responses/response-01-chat-a.md) records corrections and evidence.

Fail-first tests-only commit 5bed795eb375dead19c3859a4fc83b8262637b4b triggered preserved [push RED 44493281732](https://github.com/physicsvigilante/sim_heat/actions/runs/44493281732) and [PR RED 44493291650](https://github.com/physicsvigilante/sim_heat/actions/runs/44493291650), 5 failures/3 errors. Corrected commit 0cf27524 changes exactly four existing N3 files after review (MD, JSON, validator and tests); complete PR64 still adds only five N3 paths vs PR63. Synthetic PR checkout 3203990a3bab985ddf1c58223adbf7e5d1da56f0 matches corrected whole Git tree. Older H1/Modelica/native runner, checking references, C1/archives and other PRs untouched.

## Required independent challenges

**F-01 external manifest authority:** Has the new future approval rule unambiguously defined WHO approves (authenticated owner, independent R2 reviewer) and how a protected Git SHA, detached Ed25519 owner signature, separately pinned owner public key/release, approval envelope, trusted GitHub server event/time, source/certificate/host/case/seal identities and atomic one-use attempt ledger are authenticated? All MUST predate native output/workflow, be loaded before ANY OMC or checking preparation, and be rechecked for each case. A self-chosen seal, mutable unapproved file, attacker-selected trust key, crossed case, post-output approval or reused attempt MUST fail. Challenge circularity or missing evidence; do not pretend the approval/owner key/host/ledger currently exists. This is only a *proposed contract*.

**F-02 version and certificate:** Does the new normative dispatch table prohibit N1 usage of legacy sim_heat.reference_bundle/2 and source-only interval candidate, and allow only a future manifest-authorized N3 version with new reference_bundle/1 after separate implementation review? Check canonical JCS bytes, domain-separated semantic seal versus complete serialized bundle SHA, study separation and double clean re-preparation, 77 exports/8 requests/5 integrals with all-samples physical 100x, unchanged local K/W/J and 64ULP/0.64ULP static policy, signed flow, time/quadrature, mandatory refusal matrix and non-T1 unfamiliar public-graph authorability gate. Any unknown version, legacy fallback, changed allowance or cross-case substitution must refuse BEFORE OMC. New runner code and actual references are still absent.

**F-03 status:** Verify MD now says DESIGN_VERIFIED_NATIVE_BLOCKED, identical to validator receipt, and native readiness remains all false.
**F-04 numeric parser:** Personally test original strict_json module rejects 1e309, -1e309 and nested signed overflow while permitting normal finite numbers; retain duplicate-key and NaN token rejection.
**F-05 plan read:** Personally trace check() to show one SHA-pinned bytes snapshot parsed and audited (including a scratch mutation immediately AFTER first read); direct audit(caller_plan) separately uses a fresh pinned copy to refuse in-memory spoofing.

## Hosted evidence and stop

[Corrected PUSH 44494218732](https://github.com/physicsvigilante/sim_heat/actions/runs/44494218732) and [PR 44494231401](https://github.com/physicsvigilante/sim_heat/actions/runs/44494231401) SUCCESS; each **12+16+17+34+152 = 231 distinct offline tests** and docs parity. First fail-first RED remains preserved. All seven old physical 100x static checking-centre failures and eight native blockers remain; no actual OMC, runnable plan, owner native approval, external reference certificate, host attestation or bundle migration.

**Publish an independently authored NEW report to:** physicsvigilante/review_sandbox/projects/sim_heat/pr-64/reviews/review-02-chat-b.md, with exact source SHA, reviewer-authored adversarial evidence and qualified verdict. Preserve earlier reports; no repeated broad PR62/63 physics/comparator review unless these four N3-only changes invalidate it.

**STOP:** PR64/63/62/60/59 draft/unmerged. No OpenModelica installation, query, build, launch; no historic C1 evidence rewrite, checking-reference promotion, native result, source merge or deployment.
