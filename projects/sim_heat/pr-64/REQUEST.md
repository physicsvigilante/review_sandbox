# SIM_HEAT PR #64 — R2 independent review request: versioned reference migration design, OFFLINE ONLY

**Review objective:** assess the sufficiency and fail-closed integrity of a NEW bounded **design contract** for future H1-N1 checking-reference migration. This is **NOT** a review of implemented new numerical checking values, a runner upgrade, native simulation or permission to merge. Issue **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, precisely separating the reviewed design from still-unimplemented prerequisites.

## Frozen identities

- [DRAFT source PR64](https://github.com/physicsvigilante/sim_heat/pull/64): HEAD **`f0d863e8e1dcc44e89d1ab7e1a2f377d89d9714f`**, complete Git tree **`99136556b49e20ff3e310b6bde408101528e6b14`**.
- Stacked base independently reviewed but STILL DRAFT/UNMERGED [PR63](https://github.com/physicsvigilante/sim_heat/pull/63): HEAD **`6baba681ae1680e2fcae1ea8efbf0953afcb031b`**, base tree **`27b6ce015d5ba8229ee5990d3fa1e90352fe3f45`**. Source PR62/PR60/PR59 are also draft/unmerged; production main untouched.
- Synthetic PR checkout commit **`6e973b5e0c1677567c1d1267754c8d253cdea495`** has identical whole tree `99136556...` and ordered parents PR63 base then PR64 HEAD. The diff against PR63 is **exactly five additions**; no old `h1/`, `tools/`, C1, authored T1-T, PR62/PR63 code or historical reference changes.
- New files: `qualification/h1_n3/MIGRATION-CONTRACT.md`, `qualification/h1_n3/migration-plan.json`, `qualification/h1_n3/check_migration_plan.py`, `qualification/h1_n3/tests/test_migration_plan.py`, `.github/workflows/h1-n3-design-ci.yml`.
- Machine plan's Git blob ID is **`2203449ddd3282ddfc71699097f3fe320d2c7c54`**. Checker validates the same raw JSON bytes it parses and independently checks pinned Git-blob content of the current PR62 interval generator, PR63 comparator and unchanged legacy H1 reference, policy, temporal, verifier and native runner. Original source model, study and public facts retain separately pinned original SHA-256 values.

## What the design must preserve and must not claim

PR62's source-only 2,401/4,801 mathematical trace candidates are pinned as **historical data identities**, not regenerated or independently certified by N3. PR63's 77 exports plus eight public observation primary-only comparator was reviewed with synthetic legacy bundles; neither makes the old native runner use new checking values. The unchanged `tools/h1_native_batch.py` still calls `h1.reference.prepare(spec)`, so the old checking centres remain self-prepared. **Seven old source-exact physical 100× failures and all eight native blockers remain.** An N3 verified plan cannot in itself fix that.

Future versioned checking code should be a **general reusable H1 graph capability**, not a hidden one-apparatus solver. Explicitly new-version numerical/certificate implementation, all 77+8+5 at every grid sample with independent physical error <= epsilon/100, original 64-ULP native/static 0.64-ULP reference policy, new N1-only primary/tight/dense study/reference identities, double clean replay on an authorized host, actual code + host/OMC/MSL source manifests, and an **externally committed expected SHA and semantic seal BEFORE any native output** are required. Future runner re-preparation must select only a preauthorized checking version and match trusted expected bytes/seals; self-selected/resealed references and unknown-version fallback must refuse. These steps are DESIGN requirements only; none has been implemented here.

The validator currently checks that a design plan cannot claim new checking implementation, migration, host attestation, trusted seals, native/merge authority or results, and that all original source pins/legacy blocker labels persist. It observes the old runner via AST without importing it, reading version, executing it or creating native plans. It always emits `sim_heat.h1_n3.design_check_receipt/1` with `status=DESIGN_VERIFIED_NATIVE_BLOCKED`, `referenceMigrated=false`, `nativeCalls=0`, `nativeExecuted=false`, `nativeQualified=false`. Do **not** treat this self-verification as scientific proof or operational authorization.

## Developer and hosted evidence (not independent review)

- [Exact HEAD PUSH CI **44487658247**](https://github.com/physicsvigilante/sim_heat/actions/runs/44487658247) **SUCCESS**, artifact `14511526776`, GitHub-reported ZIP SHA256 `8209da1658727bbb2c29abe773b94473b840e1b7627c4873bae2ff769d005ee6`.
- [Exact HEAD PR synthetic CI **44488030925**](https://github.com/physicsvigilante/sim_heat/actions/runs/44488030925) **SUCCESS**, artifact `14510929241`, GitHub-reported ZIP SHA256 `c73e42cecc5156b65f76a3d583b62c3616bce248d411594bdbbe87a53437069a`.
- Both decoded hosted job logs: **7 new N3 design tests +16 inherited N2 comparator +17 inherited N1 interval +34 N1 plan +152 H1 =226 distinct PASS per run**, docs parity PASS, original N1 plan checker refuses old seven physical-100× values and retains eight blockers/zero native calls. These two runs overlap. ZIP SHA metadata has **not been separately downloaded and independently re-hashed by Chat A in this milestone**.
- Negative mutations cover fake future reference SHA/seal, external host claims, bundle edits, old-centre fallback, invented native authorization, stale scope/runner/study/trace, original SHA and Git blob drift, duplicate/nonfinite JSON and scratch output overwrite. Tests are developer-authored evidence, not separate Chat B proof.

## Reviewer instructions and STOP

Read the exact source contract and its five-file diff, central `PROTOCOL.md` and `REVIEW-RISK-POLICY.md`, the existing `AGENTS.md` and H1-N1 `PLAN.md`/`REFERENCE-CONTRACT.md`. Test source-data/JSON integrity guards and negative cases personally when possible; distinguish observed evidence from claims. Challenge the **design's compatibility with generic future H1 authorability** and the externally anchored pre-output seal/runner re-preparation trust boundary. Flag any missing unambiguous condition rather than approving a future checker that is not built. Do not redo previously accepted PR62 input guards or PR63 comparator numerical checks unless the new plan has invalidated them.

Publish exactly one independent report at `physicsvigilante/review_sandbox/projects/sim_heat/pr-64/reviews/review-01-chat-b.md`. Never write a Chat B report from Chat A. If a design issue is found, fix in new source SHA, run current-head CI and narrow re-review. Do not merge any PR or enable native workflows based on this design review.

**STOP:** NO OpenModelica installation/version query/build/launch, native result, old reference adoption/regeneration, C1/archive edit, recovered original secret scorer claim, deploy or PR64/63/62/60/59 merge. All eight N1 native gates remain closed.
