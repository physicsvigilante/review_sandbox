# SIM_HEAT H1-C1-F0 — PR #29 independent R2 review status

**Status: `awaiting-independent-review`** of original first-author model/study and historical frozen F0 offline acceptance. **No independent Chat B verdict yet; no C1 native simulation, no full scientific qualification, no fully blind author selection, and no production merge.** This historical candidate PR is **NOT TO BE MERGED** even after a scoped R2 PASS; a future separate C1 reference/native/acceptance record must preserve F0 and original first author outputs.

| Field | Pinned result |
| --- | --- |
| Source PR | [#29](https://github.com/physicsvigilante/sim_heat/pull/29), **draft/open/unmerged**, against historical F0 base, **not** main |
| Original F0 implementation source | **`dd8c9432abe97563414bb3ed809e61e673473812`**, tree `551904dc91ce5d70cc6dfc72b2115e8ae497fa22` |
| **Exact review candidate source HEAD** | **`74a8031651f9742c35e18fca499f3bd7866ab15b`** |
| Candidate Git tree | `06a1d6bb4a1f701caf4c43e3241e8cc38420d065` |
| Changed paths | **5 added**: original author task comment, original first model, study, notes and one frozen offline-only workflow. No original F0 production files changed |
| Public author freeze packet | Historical [PR #9 commit `ea954eee...`](https://github.com/physicsvigilante/sim_heat/commit/ea954eee9b416498874419b9c8e5503f94821be8): `START_HERE.md`, `AUTHOR_CONTRACT.md` unchanged |
| Original Stage 1 TASK | [Issue #26 comment 6919450031](https://github.com/physicsvigilante/sim_heat/issues/26#issuecomment-6919450031), created **2026-11-16 14:36:47 UTC**, SHA-256 **`3fe63b96b731af7af1b4d2a081684446e62e2a70d6c692ce9c39495c52836e4c`**, captured before Stage 2 invitation |
| First Stage 2 author submission | [Issue #26 comment 6919854838](https://github.com/physicsvigilante/sim_heat/issues/26#issuecomment-6919854838), created **2026-11-16 14:52:33 UTC**; SHA-256 **`e69eb7f0fe4a926062d7bd901ca31d43f60aa25e7207cf35e17a48f468d63122`**, captured before first offline test |
| Model SHA-256 | `9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435` (matches original study value) |
| Study SHA-256 | `b235d4242728c44dd994e09db3ffd92d197398dde3fe6c8f006a801981997fdc` |
| Author notes SHA-256 | `eac5f720bb744d572a0ff7219825856e140f17f29fac0c3aff0218de15d69d0a` |
| Frozen source case | Two finite buffers, two fixed baths, four rods (including two parallel bridges), four ideal nodes, eight connects, **9** public K/W/J requests |
| Exact HEAD offline CI | [43896919308](https://github.com/physicsvigilante/sim_heat/actions/runs/43896919308) — **SUCCESS** at exact candidate source |
| Original offline evidence ZIP | [Artifact 14239267614](https://github.com/physicsvigilante/sim_heat/actions/runs/43896919308/artifacts/14239267614), original whole-ZIP SHA-256 **`05a290ac04cecfa3634a773a140e4ae8accfbd5a1058bd48c175a86d86176d38`**, **10,002 bytes**, 8 members, CRC PASS |
| Frozen offline tests | **149/149 PASS**; first unchanged author study CLI **exit 0**, `admitted=true`, `nativeExecuted=false`, 4 nodes, 1 network, **9/9 `not_computed`** public requests |
| Frozen first admission result SHA | `5aaa3d0c09711a04d6cdaaa416f9d7cffe30753b06353e551602c10da9db1f0d` |
| Actual OpenModelica calls / native runs | **0**. No native MAT, native-qualified report or compiled-result values |
| Prospective modal grid | **Same-author checking only**: slowest τ≈362.12180065 s; five-τ stop≈1810.60900325 s, minimum even N≈3780; original provisional 1800/3600 is untouched but does not meet planned C1 modal grid |
| Author independence | Separate authoring ChatGPT conversation, **author disclosed previous H1 design/review exposure** and selected/wrote task/model as one role; fully blind author selection not established |
| R2 outcome | **Pending Chat B** at `reviews/review-01-chat-b.md` |
| Merge | **Never merge historical F0 candidate PR**; review is source/authoring evidence only, not production integration |
| Reference / native status | No sealed independently certified checking reference; no bounded C1 native run plan; no final H1-C1 transfer PASS |

## Independent review question and preservation

Independently compare the *original first TASK* and **unaltered first model/study/notes** with original issue timestamps and captured source SHA, and verify the authored graph is materially different from exposed developer fixtures (especially DEV_BRIDGE and Ring4). Check eight connections and two parallel rods including `RodCircular` diameter, nine requests/provenance and F0 grammar, while explicitly disclosing the author's prior exposure.

Separately verify the original frozen F0 parser/runner source against the current historical PR base. Modern `main` has an H1 MAT-v4 schema/metadata change after F0; it is **not** silently substituted. A success here proves only **first authored case offline admission**; no physical/numerical truth is certified by the parser. Evaluator checking-only matrix calculations and grid predictions are not independent reference accuracy evidence.

## Reviewer handoff

[REQUEST.md](REQUEST.md) contains exact original task/model/study SHA, source branch and CI artifact, original author-exposure disclosures, mathematical checks and R2 questions. [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md) is the ready-to-paste second-ChatGPT prompt. Follow central [PROTOCOL.md](../../../PROTOCOL.md), [REVIEW-RISK-POLICY.md](../../../REVIEW-RISK-POLICY.md) and [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md).

**Next:** Independent-in-context Chat B reviews exact **`74a8031651f9742c35e18fca499f3bd7866ab15b`** and commits **new** `projects/sim_heat/pr-29/reviews/review-01-chat-b.md` directly to central hub. Owner can say **“review done”** to Chat A, which will retrieve findings and then plan separate reference-accuracy and bounded C1 native follow-up. No native execution or merge of PR #29 without a distinct later scope and validation. Original first task and first author files stay unchanged.
