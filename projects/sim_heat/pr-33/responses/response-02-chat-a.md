# SIM_HEAT PR #33 — Chat A disposition of targeted Chat B review-02

**Outcome accepted: SCOPED PASS** for corrected immutable checking-reference storage/inspection integrity only.

**Independent report:** [review-02-chat-b.md](../reviews/review-02-chat-b.md).
**Reviewed exact source:** SIM_HEAT historical draft [PR #33](https://github.com/physicsvigilante/sim_heat/pull/33), HEAD `bf51e7721bca73720aa9b5f5f2de90defee821ec`, Git tree `a4c1e1cdd247cb07990db672ad4c092e93933d83`.
**Original review-01:** CHANGES REQUESTED at `b8c5152aac86fc1be32f7b98e032f108d8345c66`; remains historically correct and unchanged.

## Findings/disposition

- **F-01 complete-manifest integrity — independently RESOLVED.** The current pinned inspector checks exact original **2,167-byte manifest** SHA-256 `50467b138ed64cdb908f2c763bc777e6babf0bb04a0711568acc559112e66f84` before parsing any field. Reviewer personally rejected **15/15** altered historical/identity/retention/provenance cases, including all five former bypasses. The code-embedded literal is a checking constant under the exact reviewed commit, **not proof of authenticated owner adoption**.
- **F-02 exact compressed Git object — independently RESOLVED.** The inspector now separately pins **503,552-byte** XZ SHA-256 `fc5a7df5928c3fb8aef2ba4af516dfbd32b42c0450ebef1051ad4fd7efebd17f` before decompression, independent of editable manifest values. Reviewer directly hashed actual pinned Git bytes, recompressed original archived PR #31 JSON and tested alternate valid XZ presets 3, 7 and 9 (including same-length alternate encodings), forged manifest fields, corruption, truncation and extension. Each wrong object refused.
- **F-03 XZ decoder memory bound — independently RESOLVED.** Genuine archive decoded with `memlimit=64MiB` and the pre-existing maximum decompressed output bound; malformed objects refused before decoder. Review did **not** claim a demonstrated earlier denial-of-service exploit or general process-memory guarantee.
- **Historical preservation and no-native — confirmed unchanged.** The original first author task/model/study, frozen F0 physical and checking code, original failed F0 **80× vs 100×** accuracy reference, PR #31 separately checked V2 mathematical bundle and PR #32 cross-host bitwise regeneration FAIL are still distinct historical evidence. The previous CHANGES REQUESTED report is not overwritten. The exact reviewed PR #31 V2 scientific source bytes remain raw SHA `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368` and canonical seal `d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`.
- **Evidence/tests — confirmed:** exact-head CI [#43934967279](https://github.com/physicsvigilante/sim_heat/actions/runs/43934967279) SUCCESS, artifact ZIP 14259763856 SHA `5cc97cd2944d68d55f895fda9ee8668be74967e30f7211fe6906aea5c83aec94`, 9 candidate integrity tests, 149 frozen H1 regressions, 14 frozen source SHA pins, default unauthorized consumer refusal, zero OpenModelica. Chat B performed **34 separate novel offline adversarial checks** and independently recomputed source/blob/archive identities.

## Gate disposition

**Close F-01–F-03 for the exact reviewed candidate, no further corrective source work needed.** PR #33 remains **draft/open/unmerged**. This scoped PASS **does not** grant canonical-reference promotion, owner authentication, protected tag/retention policy, native reference consumption, a reference-bound native one-shot plan, OpenModelica launch or C1 qualification.

**Next guarded stage:** prepare a separately reviewable *proposed* Option A owner/trust-root/retention and read-only reference-consumption contract, including precise original PR31 artifact/manifest/commit identities, source/ref policy, refusal tests and a hard stop before native execution. Whether to adopt Option A is an **explicit owner decision**, not inferred from “review done” or a Chat B PASS. No source PR #28–33 historical experiment merges into production main are authorized. A complete native F-02 execution plan and its separately authorized launch are later stages.
