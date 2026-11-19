# SIM_HEAT PR69 — Chat A response to independent R2 review-02

**Disposition:** ACCEPT review-02 CHANGES REQUESTED for N8's unchecked published precision, reproduce it tests-first, and correct only N8. This is Chat A's account, **not** an independent reviewer pass, native certificate or merge permission.

## Pinned provenance and immutable earlier reviews

- [Chat B review-01](../reviews/review-01-chat-b.md) reviewer Git blob dc5aaf725ae64e2ffa36e0e3feabfeb2af8fa55e, CHANGES REQUESTED on old N8 head cccbc8dca8acc65e17054babbb9e5558063c0d4b.
- [Chat B review-02](../reviews/review-02-chat-b.md) reviewer Git blob **32d03320b141473227b4c852d2c29e17b91c9d0d**, CHANGES REQUESTED on OLD corrected head **23172ce2cd7a18466d2bf176b83064e6cd49bac1**, tree 112d8b56e0d6b72fd2dec06628e5f2f58b4665a5. Review-02 affirmed the old forged native/owner flag and rod-direction/G cases had been corrected, then found a new coherent-report width bypass. Its old decision remains unchanged; no N7 mathematical error was identified.
- TESTS ONLY commit **c4881ce3a808ce793e18e04c3826e6711d0a242e**, published before checker change: [PUSH CI 44573545550](https://github.com/physicsvigilante/sim_heat/actions/runs/44573545550) FAILED as expected. 17 N8 tests attempted; one failure **CornerRefusal not raised**. N8 accepted Chat B's forged-but-internally-coherent 110 K-wide temperature interval while it claimed a maximum width of 0.000001 K. This is a direct public API regression on unchanged old source; the historical red and artifact 14555027663 stay preserved.
- Corrected [draft PR69](https://github.com/physicsvigilante/sim_heat/pull/69) HEAD **3e7a8434880cc197d54cd02377e4bd69c15d1717**, full tree **e3693bc9fe1764d4bb0535bbdc09f4367c519b4b**, direct parent tests-only red commit. Stacked on still-draft independently scoped-reviewed PR68 base **4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128**. Synthetic PR checkout commit **18e881c422f8e62c2da4f205f3a585717bb9bad3** has exactly the same whole tree, parents [PR68 base, corrected PR69 head].
- Review-02 OLD to NEW diff modifies exactly THREE N8 paths: qualification/h1_n8/corner_replay.py (8 inserted code lines), tests/test_corner_replay.py, and README.md. Complete PR69 adds exactly four N8 paths vs PR68; no N7/N6/N5 numerical physics, original H1/Modelica, native runner, original source facts/model/study, C1 or production main altered.

## Corrected report semantics

N8 now checks for EVERY nonempty junction:
0 <= full published upper K - full published lower K <= exact rational claimed maximumPermittedEnclosureWidthK, whose N7/1 contract is already pinned to 1/1000000 K. This is separate from existing exact universal proof containment: a mathematically conservative report can still violate its claimed published precision. The coordinated Chat B report retains all three identical junction aliases, both source-derived signed rod flux intervals and all node/boundary ledgers, but now REFUSES with the width-specific reason. Genuine exact-area, four-junction circular, original T1-T singleton and physical orientation cases still pass. A new zero-unknown-junction positive control verifies a vacuous N7 proof legitimately omits the width field and is not wrongly refused.

## Exact-head hosted evidence and scope

- [PUSH 44574129126](https://github.com/physicsvigilante/sim_heat/actions/runs/44574129126) SUCCESS, artifact 14556820109, GitHub-reported digest sha256:e7b1c21504fe592508422bfbc263ef7434e9f89a41bd5170621cdc5fd7040009.
- [PR 44574147295](https://github.com/physicsvigilante/sim_heat/actions/runs/44574147295) SUCCESS, artifact 14556795215, GitHub-reported digest sha256:4b96f0dbd5b113a0a5e153ceeead46e6bb9b86e81dddd82da37a88f12f1335eb.
- Both independently inspected hosted logs pass **18 N8 + 13 N7 + 13 N6 + 11 N5 + 15 N4 + 12 N3 + 16 N2 + 17 N1 interval + 34 N1 plan + 152 inherited H1 = 301 DISTINCT OFFLINE tests PER workflow**, docs parity and original seven/eight refusal controls. Repeated runs are not 602 different tests. Artifact ZIP digest metadata was not independently rehashed by Chat A.

**Next:** exactly one NEW independent R2 review-03 of this narrow N8 maximum-enclosure-width correction. Chat B alone authors reviews/review-03-chat-b.md; previous reports remain immutable.

**Strict holds:** PR69 and all #59/#60/#62–#70 remain DRAFT/UNMERGED; PR70's main-based whole-project audit is SEPARATE and has no independent review as of this handoff. No OpenModelica install/query/build/launch, owner-approved source seal, native reference/77+8+5 full-grid accuracy certificate, original C1 rewrite, deployment or merge. Seven original physical 100x checking-centre refusals, eight native blockers and UNSEALED private scorer remain.
