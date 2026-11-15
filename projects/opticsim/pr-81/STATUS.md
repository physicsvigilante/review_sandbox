# Opticsim PR #81 — R2 design-review status

**State: REVIEW-01 CHANGES REQUESTED; revised design v2 published; targeted Chat B review-02 PENDING.** Do not represent this as an independent design pass or a production implementation.

## Exact source identities

- [Source design-only PR #81](https://github.com/physicsvigilante/opticsim/pull/81): **draft, unmerged**, one documentation file only.
- Production base: `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`.
- **Original reviewed v1 head:** `df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7` — 11/11 existing GitHub workflows passed, [unified 43730335002](https://github.com/physicsvigilante/opticsim/actions/runs/43730335002); docs only.
- **Revised v2 head:** `d814455cf823907551cbc7914d1f8b3b508efcab` — [v1→v2 exact diff](https://github.com/physicsvigilante/opticsim/compare/df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7...d814455cf823907551cbc7914d1f8b3b508efcab), +46/−18 lines in the **same single proposal document**, no executable production changes.
- **Revised-head CI:** [unified workflow run 43733303726](https://github.com/physicsvigilante/opticsim/actions/runs/43733303726) completed successfully. The full eleven-workflow suite must be verified separately; initial check saw **9/11 successes and two running (planar refraction, optical composition)**. This design-only CI cannot test nonexistent functionality.

## Independent review history

- **[Review-01 — Chat B](reviews/review-01-chat-b.md)**: **CHANGES-REQUESTED (DESIGN ONLY)** on immutable original head `df783a3c...`. Three major concerns: all-source root coverage including no-hit/missing callback, observer composition/once delegation, raw graph suppression and A→B→A stale run isolation; four minor clarifications. The report is unchanged.
- **[Developer response-01 — Chat A](responses/response-01-chat-a.md)**: point-by-point design corrections to all seven findings, **proposed, not independently accepted**.
- **[Targeted review-02 request](FOLLOW-UP-02.md)** and **[reviewer prompt-02](REVIEWER-PROMPT-02.md)**: ask Chat B to assess only the revised contract and residual design risk; do not re-review all of Opticsim. **No review-02 verdict recorded yet.**

## Held boundaries and release gate

- No new `detector-ray-provenance` implementation, general native ray-history API, source-specific detector measurement, textbook answer solver or path synthesizer exists.
- No PhyDemo change, source/image interpretation change, numerical threshold modification, browser app feature, or physical authoring schema change was made. Both research PRs #79 and #80 remain draft/unmerged.
- **Next:** Chat B writes its own append-only report at `projects/opticsim/pr-81/reviews/review-02-chat-b.md` for exact revised head. The owner can say "Review complete" and Chat A will check the new review. A design-only `pass` would permit seeking a **separate implementation approval**, not a source merge. Any implemented feature would require new native/Chrome tests, exact-head 11-workflow CI and fresh full independent R2 code review before owner-authorized merge.

The central hub's R2 protocol, original source and physics-safeguard instructions remain authoritative.