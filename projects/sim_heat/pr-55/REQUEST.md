# SIM_HEAT PR55 — independent R2 request: admitted-source preview for an unfamiliar supported composition

**Source draft PR:** https://github.com/physicsvigilante/sim_heat/pull/55

| Exact property | Verified identity |
|---|---|
| Source repo | `physicsvigilante/sim_heat` |
| Base `main` commit/tree | `0278b79b4da1c3196edca7903189713e0482f3f6` / `c73f86e58be8b9eb55756432aae064f00719487f` |
| Candidate head | `0b15c02e5c3c60af32224e0ec5f29a2920927d5a` |
| Candidate tree | `1be95f7dc60bd729d691e437c06f7914f0e045e4` |
| Source branch | `product/novel-source-preview` |
| Exact base-to-head diff | [One commit, 14 added paths](https://github.com/physicsvigilante/sim_heat/compare/0278b79b4da1c3196edca7903189713e0482f3f6...0b15c02e5c3c60af32224e0ec5f29a2920927d5a) |
| Risk | **R2:** new source-preview/admission and provenance semantics, untrusted JSON, asynchronous UI state |
| Independent reviewer deliverable | NEW `projects/sim_heat/pr-55/reviews/review-01-chat-b.md`, authored only by Chat B |
| Native authorization | **NONE. No OpenModelica query, installation, build or launch; no source merge.** |

## Review context and required reading

Read central [PROTOCOL](../../../PROTOCOL.md), [REVIEW-RISK-POLICY](../../../REVIEW-RISK-POLICY.md), [REVIEW-TEMPLATE](../../../REVIEW-TEMPLATE.md), source `AGENTS.md`, H1 implementation contract/offline amendment, and the original C1 freeze before assessing evidence or source interpretation. Historic C1 failures are immutable; do not merge, repin, adopt replacement references or make native calls.

This is the first source-only preview for an unfamiliar *combination of existing supported thermal components* in active main: `TEACH_SPLIT3`, **illustrative and developer-authored**, not a blind authoring/testbook trial. It has **three bodies, two fixed-temperature boundaries, seven rods, six logical nodes including one ownerless ideal junction, a shortcut, four public requests**. It is not a new physical law or apparatus renderer. The preview displays source values, units, input attribution, logical graph and public requests that remain `not_computed`. It does not create temperatures, trajectories, geometry, native measurements, independent host authentication or numerical qualification.

## Exact changed scope

Exactly 14 **added**, no modified/deleted files. The pre-existing `h1/model.py`, `h1/study.py`, `h1/policy.py`, model library, original cases, numerical reference/checker, native runner, `viewer/network`, six archived JSON bundles/catalog/comparison and `qualification` all remain byte-identical to the base.

- `h1/cases/TEACH_SPLIT3/model.mo`, `study.json`, `experiments/teacher_split3/TASK.md`: authored physical inputs, connections, provenance and four requested observations; task was pre-authored in developer's local evidence, **not** a held-out blind first attempt.
- `h1/source_preview.py`: `sim_heat.viewer.admitted_source/1` from successfully admitted studies. Inspect preservation of authored component values/typed units, exact connections, ownerless junctions, provenance with repeated records and parameter dependencies, original study/model identities and `not_computed` statuses. Distinguish authored values from checked derived values and from physics output.
- `viewer/source_preview/{index.html,app.mjs,core.mjs,data/TEACH_SPLIT3.json,README.md,core.test.mjs}`: generic source topology UI, untrusted imported JSON refusal, stale-state clearing, race protection. A forged native flag, unknown field, malformed/cross-mode case or reordered response must not look like native evidence or resurrect a refused source.
- `tests/test_source_preview.py`, `tests/browser_source_preview.py`, `docs/ADMITTED_SOURCE_PREVIEW.md`, `.github/workflows/source-preview-ci.yml`: new positive/refusal/adversarial checks, hosted actual HTTP Chromium and six-original-archive replay. Verify the CI is strict and does not invoke OMC or prepare an original frozen reference.

Publication package patch SHA-256: `e3f244565031f5bdd79e0da2612c47ff891bf3c4f012323d5ca38afa773109bd`. The package was actually recovered, independently locally applied, all 14 file SHA-256 values verified, and exact tree `1be95f7...` matched both local `git write-tree` and GitHub's new tree. API publication verified every Git blob SHA-1 and the exact 14-added-file diff. Do not treat these developer checks as a reviewer verdict.

## Hosted exact-head evidence (inspect independently)

[**Run 44257880331**](https://github.com/physicsvigilante/sim_heat/actions/runs/44257880331), push at exact HEAD, job **134643839279**: **SUCCESS**. Source identity/guard checks, offline tests, original archive replay, and real Chromium browser step all completed successfully.

[**Artifact 14407310945**](https://github.com/physicsvigilante/sim_heat/actions/runs/44257880331/artifacts/14407310945): **7,438,185 bytes**, complete ZIP SHA-256 **`ab328892f0c5796987e091e447c1d1fb78732c7bb6c70f6378ab409aed9ed1b2`**, **44 unique CRC-valid entries**. Developer downloaded/rehashed artifact; `head-sha.txt` and `head-tree.txt` match pinned identities, `source-diff.txt` lists exactly 14 additions. Other log/screenshot evidence is in same ZIP.

- Original H1 **152 pass**; arithmetic **4 pass**; existing viewer/adapter **62 pass, 1 optional skip**; product/source-preview **19 pass**; Node **39 pass**: **276 unit passes, 1 optional skipped, zero failures**. The developer independently executed these same suites locally after clean patch; do **not** double count them as 552 distinct tests.
- All six original archived diagnostic bundles **BYTE_IDENTICAL**: D1, D2, DEV_BRIDGE, TEACH_RING4, S1, D2_K2, with `nativeExecutedByReplay=false`. Original source catalog remains `diagnostic_only`, `nativeQualified=false`; the saved D2/D2_K2 comparison output is byte-identical. This is archived read-only replay, not fresh native simulation or independent numerical reference validation.
- Existing historical explorer browser smoke and product-entry browser smoke **PASS**. New actual localhost Chromium source-preview **PASS** on desktop and mobile: source-only statuses, 13 graph interactive elements, four uncomputed requests, secondary D2 topology, forged status refusal clearing graph/requests, and both orders of deliberately delayed imports. Source screenshots and refusal screenshots are retained.
- The new authored preview is byte-identical when regenerated from admitted study/model; no fake measurement. A harmless `/favicon.ico` 404 is present in HTTP logs, distinct from zero captured JS page errors. Reviewer must not claim no HTTP errors.
- The developer's earlier localhost browser navigation was blocked by environment policy and must not be recast as a local browser PASS. The hosted real-HTTP step passed. The reviewer should say which tests they personally run vs merely inspect.

## Independent R2 adversarial tasks

1. **Source fidelity and composability:** independently read exact authored study/model, verify physical slots, port connections, ownerless junction/shortcut, source identities, all four request definitions and statuses. Try a genuinely different supported topology (or existing D2/S1) through the same generic builder/viewer; reject apparatus-specific dispatch. Never infer geometry from layout.
2. **Provenance and identity:** test repeated provenance records and scalar-dependency attribution, omitted/duplicate/mismatched records, stale model hash, unexpected quantities, missing/extra fields, numerical/boolean type confusion and untrusted import metadata. Preserve exact authored SI inputs and distinction between source-given versus derived/checking values.
3. **Refusal and concurrency:** independently exercise wrong-type/malicious source preview input, fabricated `nativeQualified=true` or `diagnostic_only`, conflicting/stale source or requests; ensure refusal clears prior graph/values/history, never changes original files. Test old-valid/new-invalid and old-invalid/new-valid asynchronous import completion in the actual browser if possible. Record execution limits.
4. **Evidence preservation:** inspect all 14 source additions and exact changed-tree/CI receipts. Check original six native archive outputs and compare byte identities, no modification to native runner/reference/physical laws/C1, no hidden new native operation. Verify PR54 remains a **separate open draft**, not included or merged.
5. **Release boundaries:** evaluate source interpretation fidelity, physical/numerical correctness, native simulation/observable coverage, evidence/provenance integrity, teacher-facing usefulness, and textbook completeness **separately**. A source-preview pass cannot qualify physics/teacher classroom outcomes or authorize a production merge.

## Required outcome

Chat B independently creates the **NEW** file `projects/sim_heat/pr-55/reviews/review-01-chat-b.md` in `physicsvigilante/review_sandbox`, with exact head/tree, personally executed probes versus hosted evidence, first-attempt failures, concrete findings, and one verdict: **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. Do not edit developer source or existing Chat B reports. No merge/deployment, no OpenModelica operation, no frozen reference regeneration, no C1 historical branch integration. Any source correction needs a **new exact commit/CI**, with scoped re-review.
