# SIM_HEAT H3 Ring4 PR #18 — independent R2 review status

**Status: `independent-r2-pass-awaiting-owner-merge-approval`.** Chat B independently authored [Review 01](reviews/review-01-chat-b.md), Git blob `6df99ca2bb42a0e42ca8e1f1e738f5d7373d79d1`, **scoped R2 PASS** at the exact unchanged source HEAD `cea658c11fde5da7309aca18a6b4885858252c13`. One **nonblocking MINOR** F-01 concerns unsafe-looking *ignored outer ZIP member names* outside the selected native attempt directory; F-02 records the explicitly bounded external GitHub attestation trust limit. **PR #18 remains draft/open/unmerged; owner merge approval has NOT been granted.**

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
| Independent Review 01 | **SCOPED R2 PASS** — [Review 01](reviews/review-01-chat-b.md), exact HEAD `cea658c11fde5da7309aca18a6b4885858252c13`, Git blob `6df99ca2bb42a0e42ca8e1f1e738f5d7373d79d1` |
| Owner merge approval | **Not granted; awaiting separate explicit owner decision after R2 PASS** |
| Post-merge CI | Not applicable; source PR is unmerged |

## Important preserved distinctions

This is a teacher-style **illustrative new combination** of existing bodies/rods/bath components, not a literal textbook numeric example or a held-out independent H1-C1 model. Early refused tests and all failed/cancelled intermediate source-branch CI are preserved. The one-shot native workflow stays only on its experimental branch. The final PR does **not** alter H1 physical laws, reference/checker/runner, stored native evidence, numerical tolerances, original four viewer case files, viewer renderer or public schema. The only production adapter change is the generic nested/root source ZIP reader. It received independent targeted R2 review. Chat B found a **nonblocking MINOR**: traversal-looking names on *ignored unrelated outer ZIP members* can pass the selected-attempt read-only validation, while actual native attempt members remain checked and the **entire original ZIP** is source-hash-pinned; no extraction or new native result is involved. If revisited later, separately harden all outer member names and add a synthetic negative regression without altering this already reviewed head. The reviewer also reminded that a self-repinned ZIP is not independently authenticated by the adapter.

The original native output is diagnostic evidence, not independently measured heat transfer or a full H1/R3/C1 qualification. Same-author references and the independent-in-code-context test do not substitute for genuinely separate authoring or independent human checking. Any future new trusted artifact requires separate GitHub run/commit/artifact/whole-ZIP hash verification; consistent self-pinned metadata is not external attestation.

## Completed independent review and remaining owner gate

- [REQUEST.md](REQUEST.md), [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md): original source-pinned R2 review handoff.
- [Chat B Review 01](reviews/review-01-chat-b.md): **SCOPED PASS** at the exact reviewed source `cea658c11fde5da7309aca18a6b4885858252c13` and Git tree `888d2c256ecbb0b1e9313341f08f58f9642db485`. Review independently downloaded and SHA/CRC-checked both native and viewer CI artifacts, reconciled 88 original native manifest hashes, verified all **54 native MAT/CSV variables**, independently solved the 4-state linear energy-balance model at **2,001** saved times, checked 126/126 diagnostic records and 15 public observations, and reconstructed the 29-point fifth viewer bundle byte-for-byte.
- Native numeric limits: reviewer's independently derived matrix exponential differed from saved native temperatures by at most approximately **1.35423×10⁻⁵ K** and from signed rod power by **4.063×10⁻⁶ W** across the 2,001 saved instants. No full independent scientific qualification or arbitrary-case validation is claimed. Four reversals are *saved sample brackets*, not exact crossings.
- Reviewer F-01: **MINOR / nonblocking**. An unrelated ignored outer ZIP filename such as `../ignored.txt` is not refused by the selected-attempt archive reader; there is no extraction and the original authentic whole ZIP remains hash-pinned. The reviewer used an isolated literal-port test, not a claimed production-level exploit. Optional future small guard + synthetic regression can address it separately without another full physics review.
- Reviewer F-02: **QUESTION / documented trust boundary**. The adapter validates the caller-pinned original source archive and its internal evidence, but does not independently authenticate arbitrary repinned GitHub run/commit identities. Every later native artifact requires separate trusted run/artifact/commit/ZIP-digest checks.
- Original failed attempts, the independent-review report and `diagnostic_only` / `nativeQualified=false` statuses remain immutable. No H1 laws, source model/study, historical H1-C1-F0 baseline or original four viewer bundles were changed by the review.
- [Exact-head CI 43848622423](https://github.com/physicsvigilante/sim_heat/actions/runs/43848622423) **completed/success**, 151 H1, 4 analytic, 14 adapter, 18 Node, desktop/mobile real Chromium. GitHub PR #18 still has the **identical reviewed head**, is mergeable and draft; `main` is still the base merge commit `a6f0881236201e3ad7b9dd27d8fd0974c7972f56`.

**Next:** Ask owner for **separate explicit approval to merge SIM_HEAT PR #18**. If approved, verify exact reviewed SHA and CI, mark draft ready, use an expected-head guard for merge, check main matches the merge SHA, verify post-merge CI and update this central status. A scoped PASS alone is not merge authorization. No native solver launch is needed to merge the already tested viewer case.

Released scope remains a developmental, fixed teacher-style system, *not* a blind H1-C1 transfer, independent sensor measurement, full H1/R3 qualification, unrestricted symbolic/inverse/Modelica authoring, or proven classroom efficacy.
