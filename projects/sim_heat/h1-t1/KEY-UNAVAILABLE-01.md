# H1-T1 — original evaluator-key custody failure, first report

**Disposition:** `ORIGINAL_SELECTOR_KEY_UNAVAILABLE; PRECOMMITMENT_UNVERIFIABLE; SEALED_BLIND_SCORING_ON_HOLD; FIRST_AUTHOR_ATTEMPT_PRESERVED; NO_H1_VALIDATION; NO_NATIVE`.

**This is a process/evidence integrity failure, not a demonstrated physical-model failure or numerical-solver failure.** Do not call it a key reveal or a valid precommitted scorer. Do not generate a substitute key, backdate a scoring rubric, alter the locked tasks, or edit the author's original attempt.

## Immutable report evidence

| Field | Captured value |
|---|---|
| GitHub issue | [H1-T1 Issue #58](https://github.com/physicsvigilante/sim_heat/issues/58) |
| **Selector's issue report** | [Comment **6982883843**](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6982883843) |
| GitHub posting account | `physicsvigilante`; text attributes original key custody to separate-context selector Chat B |
| GitHub created_at (UTC) | **2026-11-18T15:21:27Z** |
| GitHub updated_at (UTC) at capture | **2026-11-18T15:21:27Z** (equal to created_at) |
| **Original complete report body SHA-256** | **`2123c5e51db849c1189df3b6f31551c5453c1bb8736a970b5724d505750df340`** |
| Body size | **1,303 UTF-8 bytes**; 1,301 JavaScript UTF-16 code units |
| Verbatim immutable snapshot | [`intake/KEY_UNAVAILABLE_COMMENT_6982883843.raw.md`](intake/KEY_UNAVAILABLE_COMMENT_6982883843.raw.md) |
| Snapshot Git blob SHA-1 | `c801f8bc53f16f900a24bffd25e36403dbcc7dd2` |
| Snapshot creation commit | `cd19469b1a07aac7de68ab09b4b7baa7de2b7cd9` |
| Original selector's **pre-author SHA-256 key commitment** | `49cc3397ae5bbbabff823e674491d9d44d8341bbd8b9556694c86f5ffffb6319` |
| Actual key/raw bytes/salt received | **NONE** |
| Original task set | [Comment `6981681502`](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6981681502), [exact task lock](TASK-LOCK-01.md) |
| Original author first attempt | [Comment `6982616288`](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6982616288), [exact first-attempt lock](FIRST-ATTEMPT-LOCK-01.md) |

Chat A retrieved the original key-unavailable comment from GitHub's exact issue-comment API, saved the **entire body verbatim**, and fetched the committed snapshot to compare it equal to the live GitHub original. The body SHA-256 was computed only after a digest implementation passed known `""`, `"abc"` and Unicode test vectors. GitHub issue comment `created_at == updated_at` at capture. No scientific/author files were read, rewritten or validated in this custody operation. GitHub issue comments remain editable, so the committed raw snapshot and digest are the historical record.

## What was reported, without repairing history

The selector's exact report is headed **`H1-T1 EVALUATOR_KEY_V1_UNAVAILABLE — SELECTOR REVEAL ATTEMPT`**. It states that its **original** private `EVALUATOR_KEY_V1` UTF-8 raw file, original random salt and exact byte formatting are unavailable from the accessible selector conversation/Library/session; the published digest alone cannot reconstruct those bytes. The selector did **not** generate a replacement, invent a matching hash, run H1, execute OpenModelica, score a model or falsely present a new key as precommitted.

Accordingly, the originally promised **salted scorer-key commitment has NOT been opened or independently verified**. This is `UNSEALED / NOT VERIFIABLE`, not `HASH_MATCH`, and not a basis for asserting fully precommitted blind-scoring success. A fresh key after the original author attempt has been exposed cannot retroactively close this first-attempt key custody gap.

**Already secured evidence remains valid on its own terms:** selector's task-only comment was independently selected in a separate context and snapshotted before the author submission; the full original author first attempt was snapshotted before this key-reveal failure. These facts support a source-first-attempt *artifact sequence*, but do not prove the missing private scoring key or all resulting model claims.

## Safe next paths; do not conflate

**Path A — exact original-key recovery (preferred if genuinely possible):** the same original selector context may locate and produce the **unchanged** original raw key UTF-8 bytes and random salt through a reliable preserved artifact. Chat A must first capture those original bytes and verify SHA-256 equals `49cc3397...` **before** any precommitted blind scoring or H1 admission. A new reconstructed key, altered whitespace or guess is not acceptable. Do not repeatedly pressure the selector to regenerate a matching-looking key.

**Path B — explicitly downgraded unsealed evaluation (salvage, separate classification):** if original bytes cannot be recovered, a separately authorized bounded `H1-T1-UNSEALED` diagnostic can compare the already-locked public task specifications against the already-captured original model/study/refusal, and run the pinned **offline-only** H1 admission and source inspector in read-only/scratch conditions. Clearly report **`PRECOMMITTED_SCORER_UNAVAILABLE`** and no original private-key verification; treat all post-submission source-interpretation adjudication as *retrospective, not precommitted*. A new independent scorer/rubric can be useful for checking model fidelity but cannot be presented as the originally promised hidden, pre-author key. Preserve raw first attempts and record any extraction/normalization/hash assistance as derived, never as an original unassisted pass. One consolidated evidence review suffices after this diagnostic. **This path is not automatically activated by the original protocol; a transparent owner decision is needed to change the scoring claim.**

Neither path authorizes fresh native simulation or changed physics/evidence semantics. The historical frozen H1-C1-F0 80× reference precision and cross-host seal failures and uncomputed outputs remain unchanged. All six original archived native diagnostic cases retain `diagnostic_only/nativeQualified=false`. No OpenModelica install/version/build/launch, native runner, original reference regeneration, deployment or integration merge occurred.

## Avoid recurrence without extra review bureaucracy

For future selector-gated tests, **verify the key can survive a conversation/session boundary BEFORE authoring starts**. Store an access-controlled (or properly encrypted, cryptographically authenticated) *exact-byte escrow copy* of the original key, along with its SHA-256 commitment and a separately kept decryption secret, before publishing the task set. A hidden key known only to an ephemeral unpersisted file/session is not reliable custody. Another option is to use public, pre-pinned rubric criteria and task facts instead of a private key when the experiment does not require a genuinely concealed precommitted scoring key. This is a process correction, **not a physics change**, and need not create a separate code PR or a sequence of repetitive reviews.
