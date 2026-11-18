# H1-T1 — selector's precommitted evaluator-key reveal (Stage 3)

**Read this in the SAME separate Chat B task-selector conversation that authored the original TASK_SET_V1.** This is a **key REVEAL**, not a second task selection, not a model-authoring request, not a new physics solution and not a review.

## The author's first attempt has now been sealed

Chat A has captured the independent author's complete original FIRST_ATTEMPT_V1 before any model validation or scoring:

- Exact GitHub author submission: https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6982616288
- GitHub author comment ID: `6982616288`, created `2026-11-18T15:11:39Z`.
- Full original body size: **31,793 UTF-8 bytes**; exact SHA-256: **`fa96e40b24fe3b039e823a78f54546bdf0ed2400e0f3b1b9519bbeb764e3c893`**.
- Git-immutable exact raw snapshot: https://github.com/physicsvigilante/review_sandbox/blob/2451994acf94fa5fe4cc90af98d78fc8537e0e15/projects/sim_heat/h1-t1/intake/FIRST_ATTEMPT_V1_COMMENT_6982616288.raw.md
- Capture evidence: https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/h1-t1/FIRST-ATTEMPT-LOCK-01.md

**You may now reveal the ORIGINAL sealed private key.** You must **not** modify or regenerate it after seeing the author's attempt. Prefer not to read the author's output until after revealing the key; its already-captured public availability is not permission to tune scoring criteria.

## Original task and precommitment

Your original public task-only comment:
https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6981681502

Your **already published pre-author salted evaluator-key SHA-256 commitment**:

`49cc3397ae5bbbabff823e674491d9d44d8341bbd8b9556694c86f5ffffb6319`

The evaluator needs the **exact original UTF-8 bytes of your private `EVALUATOR_KEY_V1` including its random salt**, not a reconstructed or corrected answer key.

## Required output: one GitHub comment, then STOP

If the original private key file is available from your selector session, read its **raw bytes**, without changing line endings, spaces, Unicode or trailing newline. Compute its byte length and SHA-256 with Python standard-library `hashlib.sha256(raw).hexdigest()`; compare with the precommit digest. Use `base64.b64encode(raw).decode('ascii')` to encode **the exact bytes**, not a Markdown copy of the decoded text. Base64 allows Chat A to reconstruct the exact original private key byte-for-byte without guessing whether a Markdown code-fence newline belongs to the file.

Publish ONE top-level comment in:
https://github.com/physicsvigilante/sim_heat/issues/58

Use this structure:

    H1-T1 EVALUATOR_KEY_V1_REVEAL — SELECTOR

    Original TASK_SET_V1 comment: 6981681502
    First author FIRST_ATTEMPT_V1 comment sealed: 6982616288
    Original key SHA-256 commitment: 49cc3397ae5bbbabff823e674491d9d44d8341bbd8b9556694c86f5ffffb6319
    Original key UTF-8 byte count: [actual byte count]
    Recomputed original key SHA-256: [actual result]
    Original key salt is present inside the encoded bytes; not changed or re-generated.
    Prior key/selector disclosures unchanged.
    
    BEGIN_EVALUATOR_KEY_V1_BASE64
    [exact base64 of complete ORIGINAL raw private key, not a new key]
    END_EVALUATOR_KEY_V1_BASE64

If you cannot read the **actual original** private key bytes or recomputed SHA-256 does not match the original commitment, **do not generate a replacement key or fudge a hash**. Instead post an explicit `H1-T1 EVALUATOR_KEY_V1_UNAVAILABLE` or `KEY_HASH_MISMATCH` report explaining exactly why. A missing/mismatched key means H1-T1's precommitted blind scorer cannot be verified; evaluator must label this as unsealed rather than treating a late new key as original.

**STOP immediately after posting**. Do not author models, evaluate S/T/X, run H1/OpenModelica, create physical references, edit prior issue comments or read the project's implementation. You are serving only as the original key custodian.

Chat A will first preserve the entire original reveal comment, then decode base64 and verify SHA-256 of the recovered raw key bytes against the **pre-author commitment**, then and only then begin source-fidelity comparison and offline H1 admission. No independent reviewer is needed merely to reveal a precommitted key; one consolidated review remains planned after the full evaluation.
