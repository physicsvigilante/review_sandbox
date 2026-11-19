# Ready-to-paste Chat B — SIM_HEAT PR69 narrow N8 width correction R2 review-03

You are independent Chat B. Review the latest N8 OFFLINE checking-only correction: a forged N7/1 report must not PASS when its published temperature interval is wider than its own maximumPermittedEnclosureWidthK. Review-02 requested this fix; earlier certification and rod-direction defects were already corrected.

**Draft source PR69:** https://github.com/physicsvigilante/sim_heat/pull/69
**EXACT corrected HEAD:** 3e7a8434880cc197d54cd02377e4bd69c15d1717
**Full Git tree:** e3693bc9fe1764d4bb0535bbdc09f4367c519b4b
**Old review-02 CHANGES REQUESTED HEAD:** 23172ce2cd7a18466d2bf176b83064e6cd49bac1
**Fail-first test-only RED HEAD:** c4881ce3a808ce793e18e04c3826e6711d0a242e
**Reviewed-in-scope still-draft PR68 base:** 4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128

**READ FULL REQUEST FIRST:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-69/CORRECTION-REQUEST-03.md

Inspect the exact N8-only old-to-new diff and Chat A response-02. Reproduce the coordinated Chat B 110-K-width forged area-chain report: H=410 K, C=300 K, G_A=1, G_B=2 W/K, true J=1010/3 K. Synchronize junction aliases, both rod heat-flow intervals and every node/boundary ledger, leaving N7 proof maximum exactly 1e-6 K. The new checker must REFUSE due specifically to published-width violation, not alias mismatch. Test the true singleton, valid zero-unknown proof without maximum-width field, original T1 circular known-body edge and unfamiliar four-junction 16-corner source graph. Do not re-review unchanged N7 physics absent a concrete new bug.

Tests-only [RED CI 44573545550](https://github.com/physicsvigilante/sim_heat/actions/runs/44573545550) failed exactly at missing refusal before code change. [Corrected PUSH 44574129126](https://github.com/physicsvigilante/sim_heat/actions/runs/44574129126) and [PR 44574147295](https://github.com/physicsvigilante/sim_heat/actions/runs/44574147295) are both SUCCESS, **301 DISTINCT offline tests per workflow**, docs parity, original seven/eight holds. Attribute independently executed probes separately from hosted evidence.

**Write ONE new independent report directly to:**
physicsvigilante/review_sandbox/projects/sim_heat/pr-69/reviews/review-03-chat-b.md

Verdict SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE at exact corrected HEAD. Preserve independent reviews #01/#02 unchanged. No OpenModelica install/query/build/launch, no original source/physical reference promotion, native certificate, C1 history rewrite, PR merge or deployment. PR70's separate main-based project audit review is still pending. After publishing, owner may say "review done" to Chat A.
