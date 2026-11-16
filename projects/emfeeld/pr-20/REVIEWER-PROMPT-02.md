# Reviewer prompt 02 — EM Fields PR #20 targeted R2 re-review

You are **Chat B**, independently reviewing the **correction** to the three reproduced defects in your own prior PR #20 R2 report. Read the [targeted FOLLOW-UP-02](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-20/FOLLOW-UP-02.md), the immutable [original review-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-20/reviews/review-01-chat-b.md), [Chat A's attributed response](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-20/responses/response-01-chat-a.md), plus central protocol, risk policy and review template.

Review **draft source PR #20** https://github.com/physicsvigilante/emfeeld/pull/20 at **EXACT corrected head 145b68fcab75201a6a31876e91c075c3f00b0fc8**, canonical Git tree **6f224d516f25eb7b4f8516cdcd33a596453ee0b4**, base **1b7d5c652bb635723746b3c6ce77baee536b997e**. Hosted CI preview checkout **f34acd2db9cfa76883ccd3803fed438b816d87f0** has the same tree. Do not review floating main or the older failed head **4b51a83** as the corrected implementation. Read the pinned contract and exact [two-file correction diff](https://github.com/physicsvigilante/emfeeld/compare/4b51a833c0ed5ef189becf5881064d1b516df21b...145b68fcab75201a6a31876e91c075c3f00b0fc8).

**Independently execute novel adversarial tests of F-01/F-02/F-03:**

- Reproduce your original E1 resigned-index-0 attack against immutable index requests for 2.0 s, both one-sided and both-sided. Corrected source must hard-refuse invalid_native_run **without creating comparison output**. Independently challenge direct index, exact-time, nearest-time tolerance/earlier tie, time_offset receipt, saved NPZ grid and values.
- Corrupt **unselected** recorded trajectory_sample values and field vector/magnitude receipts in copies of complete sealed runs while requesting an unrelated field vector. Complete-source preflight must hard-refuse, not disguise the result as an unavailable pair or a valid complete run. Confirm ordinary unknown_operand remains partial for truly absent data in otherwise sound runs.
- Insert a malformed numeric/string/null false-looking check.passed (e.g., integer 0) into otherwise successful native evidence and re-sign unkeyed inventories. It must not be accepted as a verified check. Investigate check receipt shape/expectation semantics and report any remaining inconsistency.

The corrected source has [fresh Linux+Windows clean-install CI #43837372118](https://github.com/physicsvigilante/emfeeld/actions/runs/43837372118) **SUCCESS both OSs**, 1,387 headless +18 historical +33 real-PyVista suite memberships per OS; [separate real-PyVista #43837372318](https://github.com/physicsvigilante/emfeeld/actions/runs/43837372318) **SUCCESS**. Raw Linux/Windows source/run archives were SHA256/CRC audited and the unchanged E1/G1/T1 native comparisons preserve 16 successful and one expected unavailable result; read details in FOLLOW-UP-02. Distinguish your own new executed tests from reading/replaying Chat A's same-author evidence; record failed first attempts rather than erasing them.

**Publish a NEW, separate, Chat B-authored review file** to:

physicsvigilante/review_sandbox/projects/emfeeld/pr-20/reviews/review-02-chat-b.md

(or a central review-only PR). Give exact reviewed source SHA/tree, corrected-scope evidence, first failures, limitations, and the scoped **pass / changes-requested / insufficient-evidence** verdict for F-01–F-03. Do not edit review-01, source PR #20, or historical output. **Do not merge PR #20.** Return the committed review URL so the owner can say “Review complete” to Chat A. Even after a scoped pass, **separate explicit owner merge approval** is mandatory.
