# SIM_HEAT H1-C1-F0 PR #28 — independent pre-native R2 status

**Status: `CHANGES-REQUESTED-R2-pre-native-review`** — [independent Chat B report](reviews/review-01-chat-b.md) found F-01 major static reference accuracy deficiency (80× vs required 100×), F-02 native single-run prerequisites; [Chat A disposition](responses/response-01-chat-a.md) reproduces the issue and keeps native HOLD. ** The original separate-author task/model/study/notes have been captured in their first versions, the untouched original F0 CLI admitted the first study, a separate evaluator-assisted modal reference and original native plan were validated **offline only**, and exact-head CI is green. **Chat B R2 review is complete but NOT passed; no native build/launch, production merge, accepted C1 transfer, scientific qualification or classroom outcome is claimed.**

| Field | Exact identity / observed result |
| --- | --- |
| Source project | [physicsvigilante/sim_heat](https://github.com/physicsvigilante/sim_heat) |
| Source PR | [draft #28](https://github.com/physicsvigilante/sim_heat/pull/28) — **OPEN, UNMERGED**; compares two frozen experimental branches, **not `main`** |
| Immediate base SHA | `54df9cbe7fae64bd3923b6d86a09b76ca315edc3` — original first F0 offline validation |
| **Exact candidate HEAD** | **`baabeb3ed176f4d9fa83d6be09a58b4f21fa8319`** |
| Git source tree | `e32d8a1c2d4cd31824f82556eab505222e36f5df` |
| Original F0 source | `dd8c9432abe97563414bb3ed809e61e673473812`, tree `551904dc91ce5d70cc6dfc72b2115e8ae497fa22` |
| Review class | **R2**, novel separate-context physical composition, authoring chronology, source fidelity, reference accuracy and native plan |
| Stage 1 original | [Task-only author comment #6919450031](https://github.com/physicsvigilante/sim_heat/issues/26#issuecomment-6919450031), original SHA-256 `3fe63b96b731af7af1b4d2a081684446e62e2a70d6c692ce9c39495c52836e4c`, 2026-11-16 14:36:47 UTC |
| Task-before-model capture | Evaluator Git SHA `3a298b87863d3eb97b978a4100b83dec71200b77`; original task Git blob `2f7b1ff54cfe0baae264c8d2a5c625c09d517b4a` |
| Stage 2 original | [Model/study/notes first comment #6919854838](https://github.com/physicsvigilante/sim_heat/issues/26#issuecomment-6919854838), original SHA-256 `e69eb7f0fe4a926062d7bd901ca31d43f60aa25e7207cf35e17a48f468d63122`, 2026-11-16 14:52:33 UTC |
| First authored `model.mo` | `9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435` |
| First authored `study.json` | `b235d4242728c44dd994e09db3ffd92d197398dde3fe6c8f006a801981997fdc`; provisional 0–1800 s / 3600 intervals |
| First author `AUTHOR_NOTES.md` | `eac5f720bb744d572a0ff7219825856e140f17f29fac0c3aff0218de15d69d0a` |
| Original first source preservation | [`qualification/h1-c1-stage2-first`](https://github.com/physicsvigilante/sim_heat/tree/qualification/h1-c1-stage2-first/qualification/h1_c1/submissions/issue-26), before evaluator admission |
| Author independence | Separate ChatGPT author/selector **disclosed earlier H1 design/review summaries**; **not fully blind** or independent expert claim |
| First F0 offline CI | [43892149282](https://github.com/physicsvigilante/sim_heat/actions/runs/43892149282) — **SUCCESS**; all 14 frozen SHA pins, original first study admitted, 9 requests `not_computed`, **149/149** original F0 regression tests, **zero native** |
| First F0 offline ZIP | Artifact [14237048209](https://github.com/physicsvigilante/sim_heat/actions/runs/43892149282/artifacts/14237048209), 11,237 bytes, original ZIP SHA-256 `6467aff1922c9a2688d41741b74308922c48a0791cac31cb4be90e2b032b9247` |
| Preserved early evaluator workflow failure | [43891986377](https://github.com/physicsvigilante/sim_heat/actions/runs/43891986377) — **FAILED YAML before any job**, no validator/native; formatting-only correction afterward |
| Evaluator-assisted model | Same original model bytes, `h1/cases/H1_C1_MODAL/model.mo`, same SHA |
| Evaluator-assisted study | `b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b` — only horizon 1810.609003248995 s, grid 4000 changed from first study |
| Modal rates | Slow `0.002761501788087817...` and fast `0.02087487936455612...` s⁻¹; five slow τ≈1810.609 s; `h λfast≈0.00944906113` ≤0.01 |
| Check-only reference source | `C1_FIRST_CHECKING_REFERENCE.json`, SHA-256 `1b4b497d7427deae9e83fd712fbe9119e0c8e6599212d7762c828eca10b594c9` |
| Original sealed reference bundle | SHA-256 `770a5422727f3678a07e9dfa201ad88dd85669ad9f01b045b84dad059b433276`, 4,469,216 bytes within CI ZIP, 4001 time grid, 37 channels, `nativeQualified=false` |
| Reference seal | `d76c98f37a0629b56d977c960d1e75694e1121832a9d5281f68bb972d31a365b` |
| Same-evaluator numerical corroboration | 95-digit analytic spectral vs float64 `expm` on all 4001 points, max difference `4.547473508864641e-13 K`, **not independent certified reference accuracy** |
| One-shot original-F0 native plan | `C1_PRIMARY_NATIVE_PLAN_NOT_LAUNCHED.json`, SHA-256 `f46b2621b38427ffc098d16d91695a134b7dc4d7f913021be625ee74b8a9319a`, 23 input pins, one future version query/build/launch |
| Native execution status | **ZERO OMC queries/builds/launches**. Future experiment branch `experiment/h1-c1-f0-native-primary-once` is **not created or enabled** |
| Final exact-head CI | [43895266125](https://github.com/physicsvigilante/sim_heat/actions/runs/43895266125) — **SUCCESS** on `baabeb3ed176f4d9fa83d6be09a58b4f21fa8319`; F0 149/149, 14 frozen pins, original first/modal admission, prepared/checking ref, dry-run plan, no OMC |
| Final CI evidence | Artifact [14238243398](https://github.com/physicsvigilante/sim_heat/actions/runs/43895266125/artifacts/14238243398), 1,181,341 bytes, original full ZIP SHA-256 `754e35a1143c2d0f08b38f826a2104a58e1c345a7ac1491b18dad7cb03354107`; downloaded, ZIP CRC pass, 14 members |
| Exact source diff | **8 files added**, no original H1 physical/runner/checker/numerical source modified |
| Chat B review verdict | **CHANGES REQUESTED** — [independent report](reviews/review-01-chat-b.md) finds F-01 80×/100× strict failure and F-02 launch gates. [Chat A response](responses/response-01-chat-a.md) records HOLD and focused draft PR #30 negative regression |
| PR merge/native approval | **None; HOLD**. PR #28 remains draft/unmerged. [Draft PR #30](https://github.com/physicsvigilante/sim_heat/pull/30) is offline numerical **negative evidence**, not a policy waiver or native approval |
| Post-native validation | Not applicable; no C1 native results exist |

## Important distinctions

1. Task → Model chronology is genuinely recorded, but the author disclosed **partial prior H1 exposure**. It is **not** fully blind C1 success. Source fidelity is separate from parser success; the graph's nontrivial parallel-link topology is a proposed structural transfer assessed under disclosed exposure.
2. Frozen H1-C1-F0 source `dd8c943...` stays separate from newer main `h1/matv4.py` evidence-schema-v2; no retroactive modern-parser/runtime substitution or no-repair claim drift.
3. The author's first study (1800/3600) remains byte-identical; the evaluator's modal time grid (1810.609.../4000) and separately entered reference are **different hashed artifacts** and must be recorded as assistance, not original first author success.
4. Reference equality from two numerical methods under **one evaluator** is useful diagnostic checking, **not external physics certification**. A reference bundle is not a native result. No OpenModelica execution or real classroom behavior has been demonstrated.
5. Proposed native attempt is unexecuted; future one-shot use requires exact host/source/plan verification and separately assessed independent R2 evidence, without silently recasting any failure as a success.

## Reviewed disposition and next gate

The [independent Chat B report](reviews/review-01-chat-b.md) is **CHANGES REQUESTED**, not pending. [Chat A response](responses/response-01-chat-a.md) accepts its F-01–F-04 diagnoses and preserves originals. F-01's reference static `hotLead.G` is 80× under an existing 100× rule: **strict FAIL**. Focused draft [PR #30](https://github.com/physicsvigilante/sim_heat/pull/30) and [central request](../pr-30/REQUEST.md) add a fail-closed exact-rational regression with current-head offline [CI #43911465414](https://github.com/physicsvigilante/sim_heat/actions/runs/43911465414) SUCCESS, no original source modification and zero OMC. The original archived bundle and locally re-prepared bundle have distinct seals and may never be silently conflated.

**Next:** Chat B focused review of PR #30's accurate **negative** audit evidence, followed by separately justified 100× conforming reference/host one-shot control milestones if approved. PR #28's original R2 verdict remains CHANGES REQUESTED; no merge and **no native execution**.

