# Paste into Chat B — targeted Opticsim R2 design re-review (PR #81, round 2)

You are Chat B in a separate ChatGPT conversation, reviewing **only the corrections to the pre-implementation design**. The original Chat B [review-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-81/reviews/review-01-chat-b.md) concluded **CHANGES-REQUESTED**, not a production defect; retain it unchanged.

**Review hub:** https://github.com/physicsvigilante/review_sandbox
**Targeted request:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-81/FOLLOW-UP-02.md
**Developer response:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-81/responses/response-01-chat-a.md
**Source draft PR:** https://github.com/physicsvigilante/opticsim/pull/81
**EXACT revised design head:** `d814455cf823907551cbc7914d1f8b3b508efcab`
**First reviewed head:** `df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7`
**Production base:** `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`
**Exact change diff:** https://github.com/physicsvigilante/opticsim/compare/df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7...d814455cf823907551cbc7914d1f8b3b508efcab

1. Read central `PROTOCOL.md`, `REVIEW-RISK-POLICY.md`, the first Chat B report, the follow-up request, and **pinned revised proposal**. Check the developer response against actual diff, not on trust.
2. **Prioritize F-01/F-02/F-03:** zero-hit lost source coverage with **zero** downstream incident callbacks; exactly-once atomic native callback/return/child references and legacy measurements; graph private until all gates and A→B→A run-epoch isolation. Probe for any remaining conceptual false-positive or leak.
3. Check F-04–F-07 only for concrete contradictions: warning/approximation precedence, injected guard-cap tests (not physically claimed ordinary scenes), 1-interface/1–2 SingleRay/1–2 detector exact allowlist, identity versus near-critical physics and teacher-facing limitations. Do not ask for an unrelated general ray-history engine.
4. **Write a new review report as Chat B** to `physicsvigilante/review_sandbox` at `projects/opticsim/pr-81/reviews/review-02-chat-b.md`. Do **not** edit review-01 or source PR #81, or merge anything. Outcome `pass`, `changes-requested`, or `insufficient-evidence` applies **to design only**. Record reviewed head and whether actual tests were run.
5. Provide the new report's GitHub URL. A design pass does not certify an unimplemented feature; implementation requires separate approval, CI and future independent R2 review.

After Chat B's report is saved, the owner can say **“Review complete”** back in the Chat A conversation.