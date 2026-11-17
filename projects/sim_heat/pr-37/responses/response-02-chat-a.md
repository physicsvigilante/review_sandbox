# SIM_HEAT PR #37 — Chat A disposition of independent targeted R2 review-02

**Independent reviewer report:** [review-02-chat-b.md](../reviews/review-02-chat-b.md), original Git blob `cebd8e8955c044133889bf8c56ef51679674b3c3`.
**Disposition: ACCEPT SCOPED PASS for corrected OFFLINE staged-input readback at exact source `2f2b8d5008f51b9972897058328aed8cbcbfbbce`, tree `de397fe3af9bb3385c4ef55354e49c33571dc99b`.** Original [review-01 CHANGES REQUESTED](../reviews/review-01-chat-b.md) remains valid at source `d1d6a32252b41dabad832668de642ecaf475a2a3`. No source PR merge or native authorization follows.

## Findings

- **F-01 — CLOSE within offline stage scope:** state and manifest now reject duplicate JSON keys at all nesting levels, `NaN/Infinity/-Infinity`, malformed/unbounded metadata, and numeric substitutes for literal false permission/history flags. Independent reviewer replayed actual on-disk stage, including 8 duplicate-key and 3 nonfinite attacks; all refused.
- **F-02 — CLOSE:** readback authenticates disabled preview against independent original Git blob `2c01301d1c493f33c9eb4bfb9778190adbb6d0bc` and raw SHA-256 `7e03896563ae8b4762b56bb8807612a93cddb759145a23fa94326363ea706326`. Coordinated replacement of plan bytes and staged manifest SHA now refuses, without invoking a native runner or regenerating scientific reference.
- **F-03 — CLOSE for local provenance only:** original label stored in state and manifest, requested readback label must match; staging parent and leaf symlinks refuse. Residual confirmed by Chat B: changing the directory label **and both editable JSON labels together** can still pass. Local mutable scratch metadata is not a signed global attempt identity or a trustworthy native across-run reservation. Future protected atomic ledger remains mandatory.
- **F-04 — CLOSE named numeric type checks:** source pin counts in stage and disabled plan require literal JSON integers, rejecting `23.0`/`true`; state `0` cannot substitute JSON false. Existing strict launch-budget and grid types preserved.

## Independent evidence and scope

Current-head [CI #44028343008](https://github.com/physicsvigilante/sim_heat/actions/runs/44028343008) completed SUCCESS, [artifact #14304102592](https://github.com/physicsvigilante/sim_heat/actions/runs/44028343008/artifacts/14304102592), whole ZIP SHA-256 `256da986efc326fe806185dd36cf42ba5c652c268efef7d28ec2351dafa53191`, 35/35 CRC. All **217 offline** tests passed: 24 staging, 16 disabled-preview/type, 11 owner checking-only consumer, 8 binding, 9 archive, 149 frozen H1. Original model/study/library and exact PR31 4,409,800-byte saved V2 JSON raw SHA `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368`, canonical seal `d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`, all matched direct independent source/artifact checks. The reviewer performed 22 additional locally replayed negative attacks; those are **predicate replays**, distinguished from real source-executed hosted CI.

No F-01–F-04 blocker remains **for this offline staging contract**. Frozen original F0 static accuracy (80× vs ≥100×) stays **FAIL**, as does PR32 cross-host bitwise regeneration of the originally reviewed PR31 seal. Original first author source/evidence and every historical result are unchanged. Nine requested actual native observations remain **not_computed**.

## Next bounded development milestone and stop gates

Continue only to a new, separately scoped **pre-native adapter/one-shot safety design** with exact immutable input binding, no reference regeneration and fail-closed simulated/negative tests. Do not use the old `h1_native_batch.py::prepare` to regenerate the checking reference. Do not launch or query OpenModelica, count a simulation, claim a host/compiler version, adopt a new seal, alter frozen source, or merge historical PRs.

Before any *real* native attempt: establish owner-authenticated protected/durable scientific release root and backup, independently reviewed reference-bound native adapter and exact source/plan, actual OMC/MSL/host/toolchain evidence, durable atomic across-run one-shot reservation that retains failures, independent pre-native R2, and **separate explicit owner approval for the specific OMC version/build/launch budget**. After any authorized run, independently review native trace integrity, full outputs, integrals and nine requests. PR #37 stays draft/unmerged.

**Status:** independent PR37 corrected readback **SCOPED PASS**, native F02 **HOLD**.
