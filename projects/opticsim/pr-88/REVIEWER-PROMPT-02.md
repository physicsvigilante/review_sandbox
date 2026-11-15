# Paste into separate Chat B — targeted R2 design re-review of Opticsim PR #88 (round 2)

You are **Chat B**, reviewing only the revised PRE-IMPLEMENTATION numerical reliability **design**, not production code and not a textbook-answer engine.

**Central review hub:** https://github.com/physicsvigilante/review_sandbox
**Review request:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-88/FOLLOW-UP-02.md
**Original Chat B review-01 (CHANGES REQUESTED):** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-88/reviews/review-01-chat-b.md
**Chat A developer response:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-88/responses/response-01-chat-a.md
**Source draft PR:** https://github.com/physicsvigilante/opticsim/pull/88
**EXACT revised design SHA:** `391047a5467f8e27f7b2162074900e8387945b9f`
**Original design SHA:** `28c4aa94bbbf6b5a63a8bef433c80186e08a3d35`
**Main production base:** `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`
**Pinned revised proposal:** https://github.com/physicsvigilante/opticsim/blob/391047a5467f8e27f7b2162074900e8387945b9f/docs/NATIVE-FINITE-FORWARD-QUALIFICATION-PROPOSAL.md
**One-file v1→v2 diff:** https://github.com/physicsvigilante/opticsim/compare/28c4aa94bbbf6b5a63a8bef433c80186e08a3d35...391047a5467f8e27f7b2162074900e8387945b9f

1. Independently read central `PROTOCOL.md`, `REVIEW-RISK-POLICY.md`, pinned source `AGENTS.md`, original review-01 and the **new follow-up request**. Check Chat A's claimed B1–B5 changes against the exact source diff, not on trust.
2. **Priority B1:** challenge the change from unjustified **mandatory v9 suppression** to diagnostic-only research first and any later separately owner-approved policy. A read-only observer is not automatically behavior-neutral at unstable exact-critical numerical geometry. Probe whether a single owner, exactly-once native delegation, scalar snapshots, and postrun BigInt are sufficient *design-level safeguards* without overstating evidence.
3. **Priority B2:** independently reason about the false incident-point example: vertical edge (10,0)→(10,10), ray (0,5)→(1,5), falsely reported hit (10,7). Check that forward finite `t/u` checks **plus independent computed point agreement**, unknown on unjustified error bounds, and computed endpoint/vertex guards correctly avoid false clean or false bug accusations.
4. **Priority B3:** challenge all of the Stage-2-only completed/inconsistent/unknown/stopped/stale/no-request checker/CLI/result/coverage/browser/export/A→B→A matrix, distinguishing actual native completion from **trusted measurement fitness**. Ask whether a Stage-1 advisory diagnostic must explicitly refuse to call canonical v9 numeric values independently certified.
5. Review B4–B5 for actual remaining contradictions: 128/129 limit, 1–4 sources, 0–2 detectors, Fresnel branches and browser BigInt budgets; installed and invoked source, Glass, and detector handlers, including zero-hit with a missing source. Preserve **all historical first failed CI runs**; no new physics change or ray patch.
6. **Write a NEW report as Chat B**, not Chat A, to `physicsvigilante/review_sandbox` at `projects/opticsim/pr-88/reviews/review-02-chat-b.md` (or review PR). Verdict `pass`, `changes-requested`, or `insufficient-evidence` must be stated as **DESIGN ONLY** for exact revised SHA. Clearly distinguish tests actually run from proposed tests, do not invent native/Chrome evidence and do not merge any source PR.
7. Return the new review's GitHub URL. A design pass will **not** authorize Stage 1 diagnostic code, Stage 2 mandatory qualification or a production merge; separate owner approval and implementation-level R2 are required.

After the review is saved, the owner can return to the Chat A conversation and say **“Review complete.”**