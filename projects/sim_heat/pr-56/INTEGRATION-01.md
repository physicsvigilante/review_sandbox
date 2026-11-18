# SIM_HEAT PR56 — owner-directed merge and post-merge verification

Developer integration receipt, 2026-11-18. **Not a new independent review or a release/native qualification.**

## Bounded authority and immutable evidence

The owner replied **“continue”** directly after Chat A's specific proposal: **controlled PR56 integration and post-merge verification**, PR54/PR55 excluded, no native execution. Chat A recorded this bounded interpretation in [source PR56 comment](https://github.com/physicsvigilante/sim_heat/pull/56#issuecomment-6975499636) before changing source; not blanket permission to merge another PR or deploy/execute native code.

Independent [Chat B R1 review-01](reviews/review-01-chat-b.md), original Git blob `3daf82e9743f7c4def217aee9206e2ad6aed98f8`, is SCOPED PASS at reviewed HEAD **`21eac064f98d76f12a31f03daf3bad3470cfbf96`**, tree **`0b789438b4aa1d0ecf6cbc6d38030eb540b97d48`**. [Chat A response](responses/response-01-chat-a.md) accepted its narrow CI-only scope. Neither reviewer report nor original scientific archives were rewritten.

## Actual merge

Source [PR56](https://github.com/physicsvigilante/sim_heat/pull/56) was explicitly marked ready and merged by GitHub API with **expected head SHA**, without force/status bypass, at **`7a80bd9c85d67b3a2e353d2a0702c8c5594c20dc`**. GitHub commit API independently confirms:
- Parent 1: original main `0278b79b4da1c3196edca7903189713e0482f3f6`.
- Parent 2: exact reviewed PR56 head `21eac064f98d76f12a31f03daf3bad3470cfbf96`.
- Complete resulting tree: **`0b789438b4aa1d0ecf6cbc6d38030eb540b97d48`**, **identical to reviewed PR56 tree**.

The merge changed only the existing product-entry CI workflow and added three focused trigger/guard tests. No H1 law, interpretation, numerical policies, viewer engine, native runner, original C1 case, archived diagnostic JSON/catalog/comparison or frozen reference changed.

## CI attribution

- Premerge [product workflow 44278285853](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285853): SUCCESS in candidate and baseline matrix. Actual candidate synthetic merge tree exactly `0b789438...`; **260 candidate unit PASS, one optional skip**; all six original native diagnostic archives **BYTE_IDENTICAL**, original D2/D2_K2 comparison byte-identical, full explorer and product-entry desktop/mobile/keyboard HTTP Chromium smoke PASS.
- Premerge [audit core 44278285564](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285564): SUCCESS.
- Postmerge GitHub automatic [H2 H1 offline 44283426197](https://github.com/physicsvigilante/sim_heat/actions/runs/44283426197): completed **SUCCESS** at exact merged main `7a80bd9...`. This is an H1 offline job, **not a second full product-browser/original-archive rerun**. Earlier full product CI was at an **identical source tree**, so that evidence remains scoped but overlapping, not new native scientific proof.
- Original [PR55 product-entry CI failure 44272592968](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592968) remains a genuine historic failed candidate, not retroactively replaced by a green status.
- GitHub branch metadata before merge returned `protected=false` and required-status `enforcement_level=off`, `contexts=[]`; public rulesets `[]`. The detailed protection endpoint remained integration-forbidden (403), so this is not a claim of an exhaustive organizational policy audit.

## Next branches and fixed-base caveats

Both [PR55](https://github.com/physicsvigilante/sim_heat/pull/55) (independently R2 scoped-passed corrected source at `1383a06...`) and [PR54](https://github.com/physicsvigilante/sim_heat/pull/54) remain **draft/unmerged**; PR56 merge did not authorize them. PR55's dedicated source-preview CI contained an exact 14-path allowlist against **fixed former main `0278b79...`**, which is invalid on a synthetic PR55 merge after PR56's two-file main advance. Chat A has begun a *separate CI-only PR55 workflow correction*; new exact-head checks and focused independent review are required. The first prospective PR55 workflow-only candidate at `d693189...` had a **real failed PR CI run 44287156069** because GitHub event `pull_request.base.sha` retained stale original main despite synthetic merge first parent being new main `7a80bd9...`. This failure must stay visible. Subsequent corrected head `47edc006...` uses actual synthetic merge first parent and validates second parent against PR head; verification pending at this receipt's creation. Do not promote a pending run to pass.
  
PR54 also edits the product-entry workflow, adding generated HTML documentation parity and browser navigation tests, so any future integration must **combine** its docs checks with PR56's tighter triggers and current-base protected-source guard rather than overwrite them. Require exact-new-head CI/review and separately explicit owner approval for both PR54 and PR55.

All six published cases remain `diagnostic_only/nativeQualified=false`, four TEACH_SPLIT3 requests `not_computed`. **No OpenModelica version query/install/build/launch, fresh native run, frozen/adopted reference generation, historical C1 branch merge, deployment or new qualification occurred.**
