# SIM_HEAT PR64 — Chat A correction response to independent R2 review-01

**Disposition: accepted all five findings F-01–F-05.** This is a developer response, NOT Chat B approval, native qualification, owner merge permission or a new reference implementation.

## Authenticated chronology

Independent [review-01](../reviews/review-01-chat-b.md), Git blob 113b917d8761881e345d5344919317a8654a4a00, returned CHANGES REQUESTED on OLD HEAD f0d863e8e1dcc44e89d1ab7e1a2f377d89d9714f (tree 99136556b49e20ff3e310b6bde408101528e6b14). Keep this original report unchanged.

Tests-only commit [5bed795e](https://github.com/physicsvigilante/sim_heat/commit/5bed795eb375dead19c3859a4fc83b8262637b4b) was published BEFORE editing the design/checker. Its [push CI 44493281732](https://github.com/physicsvigilante/sim_heat/actions/runs/44493281732) and [PR CI 44493291650](https://github.com/physicsvigilante/sim_heat/actions/runs/44493291650) genuinely FAILED: 12 N3 tests attempted, 5 failures and 3 errors across missing normative sections, wrong status, exponent overflow, and repeated plan reads. Logs remain historical negative evidence.

Corrected [HEAD 0cf27524](https://github.com/physicsvigilante/sim_heat/commit/0cf275241e718fbcd2b2d2c1f7761565c7c06a92), entire tree 4f253f1959797362d68ad4e153552b776ff82f33, directly follows tests-only HEAD. Only four N3-only files changed after independent review: MIGRATION-CONTRACT.md, migration-plan.json, check_migration_plan.py, and tests/test_migration_plan.py. Full draft PR64 remains the same five additions stacked on still-draft PR63 HEAD 6baba681ae1680e2fcae1ea8efbf0953afcb031b. No original model, physical facts, H1 production code, runner, references, C1 archive, PR63 comparator or PR62 interval math was modified. Synthetic PR merge 3203990a3bab985ddf1c58223adbf7e5d1da56f0 has the same whole Git tree and ordered parents [PR63 base, corrected PR64 head].

## F-01: prospectively authenticated approval, not a self-chosen seal

A future expected-manifest contract is now normative: owner approval by authenticated GitHub account physicsvigilante, separate R2 code/certificate review, a protected content-addressed approval revision in review_sandbox, detached Ed25519 signature over RFC8785/JCS canonical bytes, and owner public-key trust root pinned in the independently reviewed runner release rather than supplied by the caller. A separate approval envelope binds Git commit, manifest hash/path, GitHub server approval event/time, reviewer-report blob, owner signature/key and attempt lease. The signed manifest must cover source HEAD/tree, original model/study/facts, three study and bundle SHA+semantic seals, code/dependency closure, full numerical certificate, local allowance/time/quadrature policies, host/OMC/MSL/image, approved branch/workflow and single-use budgets.

Prospective future preflight must authenticate approval *before any checking preparation or OMC operation*, require trusted server approval timing earlier than workflow creation and any output, atomically claim an externally protected append-only one-use attempt ledger before the first OMC action, recheck before each case, and refuse post-output self-resealing, caller-chosen keys, stale/unprotected approvals and crossed cases. **No key, protected approval commit, attested host, approved manifest, lease or native permission exists in PR64.** Their fields stay explicitly NULL/FALSE. A digest alone is not external authorization.

## F-02: versioned runner/bundle compatibility and mandatory refusal matrix

The future exhaustive dispatch distinguishes unchanged legacy h1.reference.prepare/legacy with sim_heat.reference_bundle/2 (never accepted for N1), PR62 source-only candidate schema (diagnostic only), and proposed *unimplemented* sim_heat.h1_n3.physical_interval_reference_v1 with sim_heat.h1_n3.reference_bundle/1. Unknown/missing versions, mixed schemas, old fallback and altered per-case identities REFUSE. Future new bundles require exact code and source identity, independent certificate, all 77 exports/eight requests/five integrals, units/owner/scales/time/quadrature and distinct study IDs; both the domain-separated semantic SHA and full canonical serialized SHA must equal externally pre-approved expectations before any OMC. The normative futureRefusalMatrix contains 24 pre-OMC refusals.

Certificate requirements preserve source-exact Pi/rational physics, reference error <=1/100 of each unchanged own-output allowance, 64-ULP static native/0.64-ULP reference precision, K/W/J local policy, signed flows and full primary/tight 2401 plus dense 4801 samples. A post-freeze unfamiliar admitted H1 composition must pass without core checker/runner/solver edits before generalized authorability is claimed. The new general checker, serializing adapter, native-runner version dispatch, three externally signed bundles, independent certificate and real host **are NOT implemented** here.

## F-03–F-05 mechanical corrections

- F-03: document literal corrected to DESIGN_VERIFIED_NATIVE_BLOCKED, matching actual receipt.
- F-04: parse_float explicitly rejects exponent overflow 1e309, -1e309 and nested signed variants as DesignRefusal; duplicate-key, NaN/Infinity-token rejection remains.
- F-05: CLI check() consumes ONE hash-pinned and same-bytes-parsed plan snapshot; public audit(caller_plan) separately reloads and refuses mutated in-memory arguments. A scratch-file change after first read is tested. PLAN_BLOB was updated to new Git blob 357a7cd92576b04bbb256ad2728633ebf92149af.

## Exact-head evidence and restricted meaning

[PUSH 44494218732](https://github.com/physicsvigilante/sim_heat/actions/runs/44494218732) and [PR 44494231401](https://github.com/physicsvigilante/sim_heat/actions/runs/44494231401) completed SUCCESS at corrected HEAD. Both decoded logs show **12 N3 + 16 N2 + 17 N1 interval + 34 plan + 152 H1 = 231 distinct offline tests per run**, all five new regressions PASS, docs parity PASS. GitHub-reported artifact IDs/digests: push 14514187477 / sha256:1c0c5ce4324c1e2f66c05b52f307111d8ca3a85d8a6dc762ddea9ac1a0df21; PR 14514242292 / sha256:b474747ea67e38d07f3d73bd945c505663d0a9c943683ef884291877d9cc445d. These are API-reported digests, NOT personally rehashed ZIPs or independent scientific certificates.

**Next:** exactly one targeted Chat B R2 correction review-02 on corrected HEAD, published as new reviews/review-02-chat-b.md. Old review-01 remains CHANGES REQUESTED for old HEAD. PR64/63/62/60/59 all stay draft/unmerged; seven original old checking-centre physical 100x refusals, eight actual native readiness blockers and UNSEALED original author scorer remain. No OpenModelica install/query/build/launch, native bundle, host, runner change, historical C1 update, merge or deployment.
