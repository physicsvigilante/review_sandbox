# SIM_HEAT PR69 — CORRECTION-REQUEST-03: bounded N8 precision-width re-review

**Review ONE new report-evidence guard, not the independently reviewed N7 physical solver, whole-system dynamics, or native execution.** Verdict SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE.

## Frozen identities

- [Draft PR69](https://github.com/physicsvigilante/sim_heat/pull/69) corrected HEAD **3e7a8434880cc197d54cd02377e4bd69c15d1717**, full tree **e3693bc9fe1764d4bb0535bbdc09f4367c519b4b**; base PR68 reviewed-in-scope still-draft HEAD **4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128**. PR synthetic checkout 18e881c422f8e62c2da4f205f3a585717bb9bad3 has the identical tree.
- Original independent [review-01](reviews/review-01-chat-b.md), blob dc5aaf725ae64e2ffa36e0e3feabfeb2af8fa55e, CHANGES REQUESTED on original cccbc8dc source.
- [Review-02](reviews/review-02-chat-b.md), blob **32d03320b141473227b4c852d2c29e17b91c9d0d**, CHANGES REQUESTED on OLD corrected HEAD **23172ce2cd7a18466d2bf176b83064e6cd49bac1**. It confirmed that original native/owner flag and rod label forgeries were blocked but identified a fully coordinated 110 K published-band forgery contradicting a declared 1e-6 K max.
- [Chat A response-02](responses/response-02-chat-a.md) gives exact chronology. Old reviewed source to corrected source changes only 3 N8 files; the N7 numerical method and all old Modelica/native/C1 evidence stay unchanged.

## Independent reviewer challenge

Review-02's exact area_chain physics: hot 410 K, cold 300 K, area rod conductances G_A=1 and G_B=2 W/K, exact true junction J=1010/3 K. Construct the forged N7 report with **J interval [300,410] K**, updating ALL three interval aliases, both rod heat flow interval labels (A [0,110] W, B [0,220] W), the three node outward ledgers (Hot [0,110], Cold [-220,0], J [-110,220]), and hot/cold boundary supplies. Keep true source, midpoint proof, zero residual/barrier and false native/certificate flags unchanged. This mathematically conservative 110 K-wide report claims an N7 limit of 1/1000000 K.

At the OLD unchanged checker, the [tests-only RED 44573545550](https://github.com/physicsvigilante/sim_heat/actions/runs/44573545550), HEAD c4881ce3a808ce793e18e04c3826e6711d0a242e, genuinely observed **CornerRefusal NOT raised**, specifically for the fully coordinated test. New N8 code now checks the published width EXACTLY before PASS using the already required rational proof max; the fully coordinated forged report must refuse with **width-specific** CornerRefusal, not a mismatched alias/rod/boundary record. Try width slightly over 1e-6 K if useful.

Verify legitimate N7 reports remain admissible: 4-junction/16-circular-corner case, area-chain exact singleton, original T1-T known-body circular edge with zero junction uncertainty and real Pi heat-flow width, valid source rod orientation reversal and **zero-junction** case whose proof has NO maximum-width field. No tolerance widening or numeric-source changes.

## Hosted evidence and stop

- [PUSH 44574129126](https://github.com/physicsvigilante/sim_heat/actions/runs/44574129126) and [PR 44574147295](https://github.com/physicsvigilante/sim_heat/actions/runs/44574147295) both SUCCESS at CURRENT HEAD, each **18 N8 + 283 inherited =301 distinct OFFLINE PASS**, docs parity, original 7 physical 100x failures and 8 native blockers preserved. Push/PR are repeated coverage, not 602 cases. ZIP digests are GitHub metadata (see response-02), not independently rehashed by developer.
- Corrected HEAD and PR synthetic have matching whole Git tree; exactly three N8-only changed files vs review-02, no original physical model, Modelica, runner, archives or N7 method modified.

Write **one NEW independent Chat B report** at physicsvigilante/review_sandbox/projects/sim_heat/pr-69/reviews/review-03-chat-b.md. Preserve reviews-01 and -02 unchanged; distinguish personally tested APIs from hosted CI or source-inspection predictions. **No OpenModelica install/version/build/launch, native certification, original C1 rewrite, owner manifest, any PR merge or deployment.** PR69 and PR70 are separate DRAFT source lines; PR70 audit still needs its own review.
