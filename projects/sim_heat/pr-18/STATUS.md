# SIM_HEAT H3 Ring4 PR #18 — independent R2 review status

**Status: `awaiting-independent-review`.** Development, a separately approved one-shot native run, fifth generic viewer case and exact-HEAD CI are complete. **No Chat B independent findings, R2 verdict, owner merge permission or production merge is claimed.**

| Field | Exact value / current result |
| --- | --- |
| Project / source | `sim_heat` / `physicsvigilante/sim_heat` |
| Source PR | [#18](https://github.com/physicsvigilante/sim_heat/pull/18), **draft, open, unmerged** |
| Source base | `a6f0881236201e3ad7b9dd27d8fd0974c7972f56` |
| **Review candidate HEAD** | **`cea658c11fde5da7309aca18a6b4885858252c13`** |
| Review candidate Git tree | `888d2c256ecbb0b1e9313341f08f58f9642db485` |
| Review class | **R2**, native evidence and generic ZIP-ingest semantics |
| First source/task identity | `experiments/teacher_ring4/TASK.md` commit `a87d19308899b7f320d5d3632112f5b605d8f279` before model and study |
| Original Modelica model SHA-256 | `3a4771b5e6254a72a2d96e8a432b5151db8af51c1ef1d49b9553bb0e9c56e5a8` |
| Original study SHA-256 | `812e27fb83643d8ddf052181610f3d1353efbdef4e482a9374f263dd92b7f1fd` |
| New checking reference SHA-256 | `f5a7b10337cd62ff79ce77896b63135b71a2b2e39ee355ace46acf4ede55217b`; same-author checking only |
| Original failed native attempt | [43843168327](https://github.com/physicsvigilante/sim_heat/actions/runs/43843168327) — **FAIL** offline, **0** native builds/launches |
| Original failed offline correction | [43844072956](https://github.com/physicsvigilante/sim_heat/actions/runs/43844072956) — **FAIL**, source pin drift of historical test fixed by complete test restoration |
| Corrected offline author CI | [43844642166](https://github.com/physicsvigilante/sim_heat/actions/runs/43844642166) — PASS |
| Corrected successor offline-only preflight | [43845057752](https://github.com/physicsvigilante/sim_heat/actions/runs/43845057752) — PASS, **0 native commands** |
| Actual successful new native run | [43845664024](https://github.com/physicsvigilante/sim_heat/actions/runs/43845664024) at `39b2067c9b6ea5f903dc4c360a78241b24df7c09`, **one** version query/build/launch |
| Native archive | [Artifact 14215520616](https://github.com/physicsvigilante/sim_heat/actions/runs/43845664024/artifacts/14215520616), ZIP SHA-256 `0bc1433be66df2827f8907d100ca264f6a721fe8ad40644b962500b97fa9b8b2` |
| Native result | 2001 true physical-time samples (0–24000 s); 126/126 diagnostic checks, 15 public requests diagnostic-only |
| Native acceptance | `diagnostic_checks_passed_not_native_qualified`, `nativeQualified=false` |
| New fifth bundle | `viewer/network/data/TEACH_RING4.json`, SHA-256 `b4f46b2953409980ea5d5ed1b41cafaf5a7504003da44038d9d51286bb6e8a34` |
| Four signed native reversals | `ringDA` 336–348, `ringAB` 756–768, `ringCD` 1956–1968, `ringBC` 3984–3996 seconds, **saved-sample brackets only** |
| Final exact-head author CI | [43848622423](https://github.com/physicsvigilante/sim_heat/actions/runs/43848622423) — **SUCCESS**, 151 H1 / 4 analytic / 14 adapter / 18 JS / real Chromium desktop/mobile |
| Final author CI artifact | [14215443752](https://github.com/physicsvigilante/sim_heat/actions/runs/43848622423/artifacts/14215443752), ZIP SHA-256 `7974a2b7778ca05c146bb6c2b593fba485424d2228848bfccfd4bd5983a1a8bf` |
| Independent Review 01 | **Awaiting Chat B** at `reviews/review-01-chat-b.md` |
| Owner merge approval | **Not granted; development/native successor approval is not merge approval** |
| Post-merge CI | Not applicable; source PR is unmerged |

## Important preserved distinctions

This is a teacher-style **illustrative new combination** of existing bodies/rods/bath components, not a literal textbook numeric example or a held-out independent H1-C1 model. Early refused tests and all failed/cancelled intermediate source-branch CI are preserved. The one-shot native workflow stays only on its experimental branch. The final PR does **not** alter H1 physical laws, reference/checker/runner, stored native evidence, numerical tolerances, original four viewer case files, viewer renderer or public schema. The only production adapter change is a generic nested/root source ZIP reader, which must be independently adversarially reviewed because it changes evidence ingestion.

The original native output is diagnostic evidence, not independently measured heat transfer or a full H1/R3/C1 qualification. Same-author references and the independent-in-code-context test do not substitute for genuinely separate authoring or independent human checking. Any future new trusted artifact requires separate GitHub run/commit/artifact/whole-ZIP hash verification; consistent self-pinned metadata is not external attestation.

## Reviewer handoff

- [REQUEST.md](REQUEST.md) — exact source/CI/native and adversarial R2 scope.
- [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md) — short ready-to-paste Chat B prompt.
- [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md), [PROTOCOL.md](../../../PROTOCOL.md), [REVIEW-RISK-POLICY.md](../../../REVIEW-RISK-POLICY.md) — independent reporting and risk policy.

**Next:** User pastes the prompt into Chat B. Reviewer examines exact `cea658c11fde5da7309aca18a6b4885858252c13`, commits **new** `review-01-chat-b.md` directly to this hub, and returns the committed link. Owner may simply say **“Review complete”** here; Chat A will retrieve the independently authored report directly from GitHub and address confirmed findings. **PR #18 remains draft/unmerged until scoped R2 clearance and separate explicit owner merge approval.**
