# SIM_HEAT PR56 — independent focused CI applicability review

**Source PR:** https://github.com/physicsvigilante/sim_heat/pull/56  
**Purpose:** Resolve **CI-GATE-01** identified in [PR55 corrected-head independent R2 review-04](../pr-55/reviews/review-04-chat-b.md) while preserving both PR55's independent source-preview acceptance and the historic failed CI record.

| Property | Pinned identity |
|---|---|
| Repository | `physicsvigilante/sim_heat` |
| Risk | **R1 bounded CI wiring, independent focused review required**; escalate if any critical evidence/qualification rule is weakened |
| Original base main | `0278b79b4da1c3196edca7903189713e0482f3f6` |
| Base Git tree | `c73f86e58be8b9eb55756432aae064f00719487f` |
| PR56 HEAD | **`21eac064f98d76f12a31f03daf3bad3470cfbf96`** |
| PR56 Git tree | **`0b789438b4aa1d0ecf6cbc6d38030eb540b97d48`** |
| CI PR synthetic merge SHA | `1818ed1c4c6deaf586dfe14bc71ba74918dddba3`, **same exact Git tree** as PR56 HEAD |
| Diff | **2 paths only**: modify `.github/workflows/product-entry-ci.yml`, add `tests/test_product_ci_scope.py` |
| Requested independent reviewer output | New `projects/sim_heat/pr-56/reviews/review-01-chat-b.md` |
| Merge | **NOT AUTHORIZED**. PR56, PR55 and PR54 remain draft/unmerged. |

Read [central protocol](../../PROTOCOL.md), [risk policy](../../REVIEW-RISK-POLICY.md), [review template](../../REVIEW-TEMPLATE.md), [source AGENTS](https://github.com/physicsvigilante/sim_heat/blob/21eac064f98d76f12a31f03daf3bad3470cfbf96/AGENTS.md), exact source diff, and [PR55's scoped-pass-but-not-merge-ready review](../pr-55/reviews/review-04-chat-b.md). Do not treat developer CI notes as an independent reviewer verdict.

## Defect and narrow fix

**Historical failure:** [product-entry workflow 44272592968](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592968) genuinely failed in *candidate* job `134692657687` on PR55 corrected source; separate old baseline job `134692657797` passed. The workflow was invoked because `tests/**` matched `tests/test_source_preview.py`. It then required **zero changes under `h1 experiments qualification viewer` from fixed historical baseline `4162c3d...`**, which is incompatible with PR55's legitimate added H1/source-viewer source. The failing candidate job's later suites and browser steps were SKIPPED. It is a workflow applicability failure, not a successful product-entry regression test and not evidence that the R2 source-preview suite failed.

**PR56's prospective change**:
1. Narrow product-entry PR path triggers to `index.html`, README and capability/authoring docs, `tools/render_product_docs.py`, `tests/test_product_*.py`, `tests/browser_product_*.py` and this CI workflow. Unrelated `tests/test_source_preview.py`, `tests/browser_source_preview.py`, `viewer/source_preview/**` do not trigger product-entry CI. Their dedicated source-preview workflow already tests real source-specific behavior and product-entry navigation.
2. Preserve the **strict protected source diff guard for product-only candidates**: `git diff --exit-code "$scope_base" HEAD -- h1 experiments qualification viewer` still refuses **real modifications** to physical/qualified/viewer paths when changing product entry. Candidate scope base is the actual GitHub PR base SHA; on historical push, it uses the previously pinned source. The `postmerge-baseline` job retains fixed `4162c3d...` self-comparison and existing tests.
3. Retain record of the effective base in `scope-base-sha.txt`, original six-archive replay, H1/analytical/adapters/Node suites and existing real Chromium smoke. Three new offline regression methods exercise included/excluded globs, use of actual PR base in strict guard, and actual Git negative control (product change allowed; `h1` edit refused). No solver, physical law or evidence status changed.

## Exact-head hosted verification (inspect actual CI, not PR prose)

[**Product-entry PR CI 44278285853**](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285853) **SUCCESS**:

- **Candidate job 134711947163**, actual checkout PR synthetic merge `1818ed1c4c6deaf586dfe14bc71ba74918dddba3`. Its Git commit tree independently equals exact HEAD tree `0b789438...` and parent pair is current main `0278b79...` + candidate `21eac...`. Candidate receipt `scope-base-sha.txt` equals `0278b79...`; `source-diff.txt` = **one workflow modification and one added test only**.
- **Candidate unique unit passes: 260 PASS, one existing optional test SKIP**, zero fails: H1 152 + analytical 4 + adapters 62 pass/one skip + Node 31 + product 11 (eight inherited, three new). Existing explorer and product-entry desktop/mobile real-HTTP Chromium PASS. All six original published diagnostic bundles replay `BYTE_IDENTICAL` with `nativeExecutedByReplay=false`. Saved D2/D2_K2 compare index rebuilt byte-identically.
- **Baseline job 134711947770**, source `4162c3d47016150076b226ebe2585073a785547a`, PASS on its old subset (249 pass, one optional skip; new three product tests absent and candidate-only entry step skipped). Overlapping counts not additive.
- [**Artifact 14416131352**](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285853/artifacts/14416131352), candidate 6,455,105 bytes, SHA-256 **`a3a2398b8e0ea96cc243680609803e3c7f27001b1af8846347e214ef56561c7e`**, **39 distinct CRC-valid ZIP members**, downloaded and rehashed by developer. SHA/tree/base/diff, six archive receipts, original comparison, local test and browser logs inspected. A favicon HTTP 404 is not a JS page error; do not claim no HTTP errors.
- Separate [**audit-core CI 44278285564**](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285564) **SUCCESS**, archive and browser steps passed.

Local developer controls: 3/3 new tests passed, YAML parsed, entire exact base source reconstructed from the PR53 merged baseline `source.tar`, `git write-tree` returned `c73f86e58...`; applying the two changes produced local Git tree `0b789438...`, exactly matching GitHub's API tree. Both changed Git blobs independently matched local Git blob SHA-1. No OpenModelica operations.

## Review questions and boundaries

Check actual trigger-glob behavior and whether broad `tests/**` has genuinely disappeared **without excluding product-owned tests** or hiding required source-preview checks. Verify dynamic PR-base selection, pinned baseline case, preservation of strict candidate protected-path refusal (a real `h1` edit must fail). Evaluate PR merge-ref checkout/tree and compare the two files only; run independent negative probes if feasible. Verify all six archived replays and actual browser results from evidence and keep them distinct from personal reexecution.

**Important integration caveat:** PR55's dedicated `source-preview-ci.yml` still has a fixed old-base 14-additions allowlist. If main advances through a future **approved** PR56 merge, PR55's merge-ref check may see those two new CI-hygiene paths in the old-base diff and fail until the future source-preview CI scope check is made current-PR-base-relative. PR56 intentionally does **not** modify PR55's independently reviewed corrected source and does **not itself clear all possible future PR55 merge gates**. Reviewer should assess integration ordering and report whether another bounded source-preview workflow change is necessary before owner considers either integration. Do not silently waive required checks; connected GitHub branch-protection endpoint is 403, and public ruleset query showed no rulesets, so an exhaustive protected-status inventory has **not** been established.

Separately confirm [PR55](https://github.com/physicsvigilante/sim_heat/pull/55) remains draft/unmerged at reviewed corrected R2-scoped-pass HEAD `1383a06d...`, with review-01/02/03 CHANGES REQUESTED on old source and review-04 scoped PASS on corrected source; [PR54](https://github.com/physicsvigilante/sim_heat/pull/54) remains draft/unmerged. Do not modify those reviews or evidence.

## Required output and stopping point

Independent Chat B writes a **NEW** `projects/sim_heat/pr-56/reviews/review-01-chat-b.md` with exact PR56 HEAD/tree/merge-ref, personally run versus hosted tests, any findings and one **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** verdict. Focused scope, not another broad physics audit. Escalate risk if changed CI paths could weaken physics/evidence qualification. Preserve real failed workflow 44272592968 as failed historical evidence. No source PR merge, no deployment, no OpenModelica version/install/build/launch, no frozen-reference regeneration, no C1 historical integration or qualification promotion. A review pass is never merge permission.
