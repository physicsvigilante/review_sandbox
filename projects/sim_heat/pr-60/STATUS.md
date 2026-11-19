# SIM_HEAT PR60 — targeted design review accepted; numerical readiness still blocked

**Current state:** `REVIEW02_SCOPED_PASS_PRE_NATIVE_DESIGN; CHAT_A_ACCEPTED; F01_SPECIFICATION_RESOLVED; SEVEN_STATIC_PRECISION_REFUSALS_RETAINED; EIGHT_EXECUTION_BLOCKERS_RETAINED; EXACT_HEAD_OFFLINE_CI_PASS; EXECUTION_NOT_READY; NATIVE_CALLS_ZERO; DRAFT_UNMERGED`.

## Exact source and review disposition

[PR60](https://github.com/physicsvigilante/sim_heat/pull/60), branch `planning/h1-n1-t1t`, remains open, draft and unmerged at **HEAD `58ca02b293f2afbd931ab7ad1832fc4e34df1574`**, complete Git tree **`c31fe1a37a598f30fa5859227a3ccbc5abf5c470`**. Main remains `f52613c39c539b2d4543a9838e5658d526fca10e`, tree `0c44961b473d23737b0c9f3b3f2cd3db65b9f264`. Successful PR synthetic checkout `0c6f885043a2cdc813f2e82991bedbef822716a2` has the identical candidate tree and ordered baseline/candidate parents.

Independent [Chat B review-02](reviews/review-02-chat-b.md), original blob **`2c86cc80cc13acce598fa1537b8d53b3a52a0e1a`**, returns **SCOPED PASS for F-01 arithmetic-target DESIGN only** at this exact corrected HEAD. [Chat A response-02](responses/response-02-chat-a.md) accepts it. The original [review-01](reviews/review-01-chat-b.md), blob `8d0712c75c56f7fa13b7bb80f7bebe63964b8abb`, remains CHANGES REQUESTED on old HEAD `469ab08f4b0fbe3144110bae41b57d29695447bb`; no reviewer report was rewritten or extended retrospectively.

One correction changed five N1 plan/check/test/workflow files. Full PR still consists of twelve additions, with no existing H1/physics/numerical/viewer/native/reference/C1 modifications. Original T1-T model/study/notes and all physical inputs remain byte-identical. Evidence-only PR59 remains separate, draft and unmerged; duplicate PR61 remains closed without merge. No source change or merge occurred in this review-disposition step.

## What passed, and what did not

**F-01 specification is resolved:** Physical target P is exact source-decimal mathematics with independently bounded Pi. The mandatory certificate still requires `max(abs(v_ref-Plo), abs(v_ref-Phi)) <= epsilon/100`. Representation target R records declared RN-even binary64 literal/intermediate arithmetic separately. Agreement with R cannot replace physical accuracy, erase R-to-P discrepancy, or establish an unobserved Modelica compiler's behavior.

The unchanged static native allowance remains **64 ULP**, giving the reference certificate a **0.64 ULP** budget. There are no exemptions, broadened tolerances or output-fitted targets. All 77 native exports, eight public requests and full-grid dynamic/integral obligations remain.

**Seven actual static precision refusals remain:** `T02.G`, `T06.A`, `T06.G`, `T07.G`, `T08.G`, `T10.G`, `T_Plug.C`. Chat B independently reproduced all fourteen physical/representation checks using exact fractions, a separately written 45-term rational Pi enclosure and binary64 expression probes. The eight-blocker readiness list still includes `STATIC_CHECKING_CENTRES_FAIL_PHYSICAL_100X_BOUND`; the constant probe correctly reports `REFUSED_UNCHANGED_CHECKING_CENTRES`. A passing refusal regression is not a passing physical-reference certificate.

Correctly rounded physical-centre witnesses remain **non-adopted examples** only. They do not replace reference values, historical seals, native fields or a full trajectory certificate. Any future adoption needs a new prospective checking implementation/version, independent numerical evidence and actual runner re-preparation binding. No manual edits of existing reference bundles are permitted.

## Existing exact-head checks and attribution

[Push 44376836623](https://github.com/physicsvigilante/sim_heat/actions/runs/44376836623), [PR 44376848205](https://github.com/physicsvigilante/sim_heat/actions/runs/44376848205), and [audit 44376847910](https://github.com/physicsvigilante/sim_heat/actions/runs/44376847910) remain completed SUCCESS, rechecked for this disposition. Each plan suite has **34 focused tests + 152 inherited H1 tests = 186 distinct passes**, plus docs parity; overlapping local/push/PR totals are not additive. Eight blockers, false execution/certification flags and zero native calls remain asserted.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| Push 14460713898 | 1,457,976 | `d372964c84a6986b7d56219eb64b4126e5c62f705eb0ba99b1a77f66e0af5818` |
| PR 14461696589 | 1,457,978 | `2f45c1ae60ac2e75814a3eb4c9a82f74f5faee84e4cd5410d2e97c7644e12928` |
| Audit 14462475448 | 5,874,377 | `30baefd86bebfd19489971f7902cb4ecc15f14f13fd705123e37862264032305` |

Prior Chat A verification recorded 10/10/33 unique CRC-valid entries, exact source.tar Git trees, six original archived cases BYTE_IDENTICAL and hosted browser PASS. Chat B personally verified arithmetic, pinned source and provider metadata/logs, **not** ZIP downloads, repository unit reruns, independent archive replay or Chromium. This disposition did not rerun those tests or rehash the artifacts. Full earlier evidence remains in [response-01](responses/response-01-chat-a.md), [correction request](CORRECTION-REQUEST-02.md), and the [previous status pinned before this disposition](https://github.com/physicsvigilante/review_sandbox/blob/c101b3b84cc7c07c3ffc2eecd4bab5ab433831a0/projects/sim_heat/pr-60/STATUS.md).

## Next substantive work and stop

**No third review is needed for this unchanged specification.** Next work is implementation and evidence: a newly versioned physical-reference checker that clears the seven static refusals without relaxing accuracy, full dynamic/integral certification, prospective runner/reference binding and new N1-only seals, the primary-only exact-common-time companion comparator, and authenticated runtime/containment/single-use controls. Review the genuinely changed critical code/evidence together within the existing bounded R2 scope; do not restart whole-project or per-constant reviews.

The optional maximum-finite binary64 property test suggested by the reviewer is future hardening, not a new present design blocker. Original source horizon 0–2400 s and proposed primary/tight/dense studies remain unchanged. A future ceiling of **3 version queries / 3 builds / 3 launches / zero retries** is NOT current permission. **Actual native counts remain zero; `nativeExecutionReady=false`, `referenceAccuracyCertified=false`, `nativeQualified=false`.** Final runtime identities, manifests, reference replay and a separate explicit owner native authorization are still required.

No OpenModelica install/version query/build/launch, native-runner invocation, frozen-reference regeneration, historical C1 integration, diagnostic promotion, deployment or production merge authorized/performed. H1-T1 remains UNSEALED after the private-key loss; original source requests remain `not_computed`; six historical archives remain `diagnostic_only/nativeQualified=false` and original C1 precision/seal failures remain historical failures.
