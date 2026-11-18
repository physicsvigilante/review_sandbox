# SIM_HEAT PR #56 — Chat B focused independent R1 review

**Verdict: SCOPED PASS on the exact pinned correction; NOT a merge authorization.**

- **Project / repository:** SIM_HEAT, https://github.com/physicsvigilante/sim_heat
- **Source PR:** https://github.com/physicsvigilante/sim_heat/pull/56 (draft, open, unmerged when inspected)
- **Exact reviewed HEAD:** 21eac064f98d76f12a31f03daf3bad3470cfbf96
- **Exact reviewed Git tree:** 0b789438b4aa1d0ecf6cbc6d38030eb540b97d48
- **Actual PR base main:** 0278b79b4da1c3196edca7903189713e0482f3f6; tree c73f86e58be8b9eb55756432aae064f00719487f
- **GitHub hosted PR merge checkout:** 1818ed1c4c6deaf586dfe14bc71ba74918dddba3; verified Git API parents = base main + exact candidate; **merge tree equals candidate tree** 0b789438b4aa1d0ecf6cbc6d38030eb540b97d48
- **Exact code changes:** modified .github/workflows/product-entry-ci.yml; added tests/test_product_ci_scope.py; no other paths (GitHub base-to-head compare, one commit ahead and zero behind).
- **Reviewer:** Independent Chat B, separate ChatGPT conversation, GPT-6. Independence is contextual, not a claim of distinct model weights or human adjudication.
- **Date:** 2026-11-18 (Asia/Kolkata)
- **Risk / scope:** R1, narrowly bounded product-entry trigger/guard wiring, with escalation if any qualification or evidence gate weakens.
- **Source changes by reviewer:** None. Only this new independent central review report was requested.
- **Pinned source diff:** https://github.com/physicsvigilante/sim_heat/commit/21eac064f98d76f12a31f03daf3bad3470cfbf96
- **Review authorities:** central PR56 REQUEST and REVIEWER-PROMPT-01, PROTOCOL, REVIEW-RISK-POLICY, REVIEW-TEMPLATE; pinned source AGENTS; PR55 Chat B review-04; inspected the actual current workflow and source-preview workflow at PR55's corrected head.

## Executive conclusion

The correction fixes the demonstrated *applicability* defect without weakening the product-only candidate's protected-source refusal. PR trigger paths now cover the enumerated product entry, docs, renderer and product tests, not broad tests/** and not the source-preview-only paths. The candidate guard compares the synthetic PR merge checkout against **github.event.pull_request.base.sha**, while the postmerge-baseline job continues to compare its old pinned source to itself. A real protected H1/experiment/qualification/viewer modification remains an error when a product-triggered candidate runs.

**No demonstrated blocking defect was identified in PR56's two changed paths.** This scope judgment is independent of any future decision to merge PR56, PR55 or PR54. The historical PR55 product-entry red is not erased, and PR55's own fixed old-base allowlist is a separate forward integration concern.

## Findings

### F-01 — PASS (trigger correction; no blocking defect)
- **Category:** CI applicability / test coverage.
- **Location:** .github/workflows/product-entry-ci.yml, PR pull_request.paths (approximately lines 4–21); tests/test_product_ci_scope.py, positive/negative trigger checks (approximately lines 25–53).
- **Observed:** The old tests/** trigger is gone. Included: index.html, README.md, capability and authoring MD/HTML files, tools/render_product_docs.py, tests/test_product_*.py, tests/browser_product_*.py and the product CI workflow. Excluded: tests/test_source_preview.py, tests/browser_source_preview.py, viewer/source_preview/**, H1/experiment/qualification-only paths.
- **Independent probe:** 13 representative positive filenames and 10 unrelated/source-preview filenames were checked against the reviewed pattern strings; all yielded intended results. These probes used a separately authored local fixture, not a self-certifying rerun of the newly added test code.
- **Limit:** Python fnmatchcase, also used in the new committed test, is not an exact implementation of GitHub's glob engine, especially for hypothetical nested path matching. The currently enumerated patterns/tests are flat filenames and revealed no concrete coverage defect. If product tests become nested later, add a GitHub-minimatch-equivalent check. **Minor future-test-hardening advice, not a current blocker.**

### F-02 — PASS (strict actual-PR-base protected-source guard)
- **Category:** CI physical/evidence boundary; potential guard bypass.
- **Location:** .github/workflows/product-entry-ci.yml, checkout/scope calculation/guard (approximately lines 36–76); tests/test_product_ci_scope.py Git fixture (approximately lines 54–93).
- **Observed:** The hosted candidate job visibly interpolated PR base 0278b79b4da1c3196edca7903189713e0482f3f6. The downloaded candidate artifact's scope-base-sha.txt is exactly that SHA; source-diff.txt contains only M .github/workflows/product-entry-ci.yml and A tests/test_product_ci_scope.py. GitHub independently reports the same two-file base-to-HEAD diff. The strict command still runs for candidate: git diff --exit-code "$scope_base" HEAD -- h1 experiments qualification viewer.
- **Independent local Git fixture:** Historical baseline A had an older H1 file; current base B had a legitimately integrated H1 edit; product-only candidate C edited README/workflow/test. A-to-C guard returned 1 (old false rejection), while B-to-C returned 0 (correct admission). Four separate negative follow-up commits from C changed h1, experiments, qualification and viewer individually: B-to-each guard returned 1 for **all four**. The test used temporary local Git commits and no production source or Modelica runtime.
- **Baseline:** The downloaded postmerge-baseline receipt reports checkout 4162c3d47016150076b226ebe2585073a785547a, an identical scope base, and an empty source diff. The historical baseline is not silently replaced with a moving PR base.
- **Residual scope:** The PR path filter intentionally does not schedule this product workflow for a source-preview-only PR. The dedicated source-preview workflow/audit are the relevant suites for that scope. Whether GitHub's *required-check policy* handles path-skipped workflows correctly remains an external governance question, not a passed check.

### F-03 — MAJOR FORWARD INTEGRATION CAVEAT (not a PR56 code defect)
- **Category:** PR55 integration order and old-base allowlist.
- **Location:** PR55 corrected head 1383a06d20422182cdae643337d6ddbdd6fcc5ec, .github/workflows/source-preview-ci.yml, "Exact source identity, protected-code comparison and full offline suites".
- **Observed:** The source-preview workflow checks the name/status diff from fixed main SHA 0278b79b4da1c3196edca7903189713e0482f3f6 against an **exact set of 14 newly added PR55 source-preview paths**. If PR56 is approved and merged first, a future PR55 synthetic merge will also contain PR56's M .github/workflows/product-entry-ci.yml and A tests/test_product_ci_scope.py relative to that fixed base. The resulting 16-row old-base diff cannot equal the 14-entry allowlist. Independently checked the set inequality as a conditional fixture; not a claim that this future CI run has already occurred.
- **Required before PR55 integration:** After any main advance, revise PR55's own source-preview CI to compare against its then-current PR base, preserving the exact PR55-owned-path constraints and protected-code refusal, and rerun its exact-new-head PR checks; obtain appropriately scoped re-review. Do not edit or merge PR55 under this PR56 review. Integrating PR55 first also does not retroactively clear its genuinely failed product-entry run. Owner must choose order and required-check disposition.

### F-04 — OPEN GOVERNANCE QUESTION (not an assertion of bypass)
- **Category:** Required CI statuses and path-filtered workflow behavior.
- **Observed:** GitHub branch-protection required-status-checks endpoint returned **403 Resource not accessible by integration** during this review. Public rulesets endpoint returned [] but does not establish a complete required-check inventory. Therefore the reviewer **cannot certify** all required checks, exemptions, or a future mergeable status policy. A skipped path-filtered workflow may leave a required check pending; it must not be treated as green.
- **Next control:** Owner/admin should inspect actual branch protection and required-check names before approving any integration. Record a scoped governance decision; do not silently waive a red/pending required check.

## Evidence inspected and personally executed

| Evidence | Exact observation | Execution provenance |
|---|---|---|
| GitHub PR56 and Git commit APIs | HEAD 21eac064...; candidate and hosted merge trees identical 0b789438...; GitHub merge parents match exact base and candidate; two-file compare | Reviewer independently queried GitHub |
| Product-entry PR workflow [44278285853](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285853) | **SUCCESS**. Candidate job 134711947163 and baseline job 134711947770 both SUCCESS, including all required steps visible in job metadata and job logs | GitHub-hosted execution inspected; not reviewer-run |
| Candidate artifact [14416131352](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285853/artifacts/14416131352) | **6,455,105 bytes**, SHA-256 **a3a2398b8e0ea96cc243680609803e3c7f27001b1af8846347e214ef56561c7e**, **39/39 unique members, CRC valid**. Independently downloaded, hashed and opened receipts, suite logs, replay JSON and browser logs. | Reviewer independently downloaded/checked actual hosted artifact |
| Candidate original suites | **152 H1 PASS + 4 analytical PASS + 62 adapters PASS / one existing optional SKIP + 31 Node PASS + 11 product PASS** (8 inherited plus the 3 new CI tests) = **260 unique PASS, one optional SKIP, zero failed** | Read actual artifact logs and hosted job; not rerun as candidate source locally |
| Baseline artifact [14416545060](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285853/artifacts/14416545060) | **5,873,929 bytes**, SHA-256 **627e4424a79b03644ce9186df0a3e33a18aa580319b75fa3e6ac01be0ad2d985**, **34/34 unique CRC-valid entries**. Checkout and scope base both 4162c3d..., source diff empty. Historical suites = **249 inherited passes, one optional skip**. | Reviewer separately downloaded/hashed/inspected; not added to candidate's overlapping test total |
| Separate audit-core [44278285564](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285564) | **SUCCESS** at PR56 merge ref; hosted job logs show H1, analytical, adapters, Node, archive and explorer smoke steps completed | GitHub-hosted execution inspected |
| Original archive replays | Candidate **D1, D2, DEV_BRIDGE, TEACH_RING4, S1, D2_K2** each record **BYTE_IDENTICAL**, with nativeExecutedByReplay=false. Same six baseline receipts and original saved D2/D2_K2 compare index rebuild were retained; hosted cmp completed successfully. | Hosted replays and compare inspected, **not personally rerun** |
| Original archive inputs | Reviewer **independently downloaded all five original ZIPs**, corresponding to six cases (D1 and D2 share one). SHA-256 hashes matched the six receipts exactly, and all five ZIPs had no CRC errors or duplicate members. Artifacts 14152886226 / 14155084346 / 14204656273 / 14215520616 / 14153251022. | Reviewer download, digest/ZIP checks; not original simulator execution |
| Chromium browser coverage | Hosted full explorer and product-entry real-HTTP desktop/mobile/keyboard/route smoke **PASS**; screenshots present and CRC-valid in artifact. There is a nonblocking /favicon.ico **404**; do not describe this as zero HTTP errors. | Inspected hosted logs/screenshots inventory, **did not personally launch a browser** |
| Independent negative/positive controls | 13 positive + 10 negative path patterns PASS; current-PR-base acceptance and fixed-old-base false rejection replicated; 4/4 protected-directory alterations refused; PR55 fixed 14-path allowlist rejected conditional 16-path composite. | **Reviewer personally ran isolated Python/Git fixture**, not on candidate worktree; no OpenModelica |
| Historic red [44272592968](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592968) | Candidate job 134692657687 is **FAILURE**, with guard step exiting 1; archive/browser/product test steps skipped. Baseline job 134692657797 PASSED. | GitHub job statuses/log inspected. **The failed run remains failed.** |

Original ZIP digest details independently checked:
- Artifact 14152886226 (D1, D2): 8fc38b9e2f040b48ab5cbeab34e8698b7c99c4d462a1e31e8bc33b0395185379
- Artifact 14155084346 (DEV_BRIDGE): f16975a25eea79f61f7819fb9e704ab04a33630044a51a0d062b8399c1c9ce38
- Artifact 14204656273 (S1): 82b4a87b66e0022d582da931253649b3829f6633119a57081c02dc253dc5dbd9
- Artifact 14215520616 (TEACH_RING4): 0bc1433be66df2827f8907d100ca264f6a721fe8ad40644b962500b97fa9b8b2
- Artifact 14153251022 (D2_K2): dc32a0a36a27f031ce7a13da83ebdd26a3dd6ac1d14612fa597b36cb439f4843

**Important evidence limit:** The downloaded candidate's archive-replay.json reports all six byte-identical outputs, but the reviewer did **not** independently re-execute replay_published_archives.py or rebuild the saved compare index from source. Original archive ZIP hash checks and the two-file Git diff independently corroborate preservation; the exact replay computations remain hosted evidence, not independently repeated native experiments. The local Git guard fixture is independently authored from the pinned workflow patterns, not a direct invocation of the new repository test file. No native simulation or new physical verification was attempted.

## Separate scope judgments

| Dimension | Judgment | Basis |
|---|---|---|
| Source interpretation fidelity | Unchanged / out of PR56 scope | No source interpretation/authoring model changed; PR55's R2 scope remains separate |
| Physical/numerical correctness | Not requalified; no new physical calculation | Two CI/test paths only; inherited offline tests PASS; not a new native proof |
| Native simulation / observable coverage | No new qualification | Existing diagnostics remain diagnostic_only / nativeQualified=false; replay nativeExecutedByReplay=false |
| Evidence integrity and provenance | **SCOPED PASS** | Two-path diff, same Git trees, downloaded artifact checks and matching original archive digests; hosted six-case byte-identical receipts; no frozen-reference change |
| Teacher-facing usefulness | Unchanged | No viewer/product page code changed; existing smoke hosted PASS |
| Textbook-answer completeness | Not applicable | No new problem interpretation or solved-answer claim |

## Release and integration advice

1. **Accept scoped R1 review of PR56 at HEAD 21eac064f98d76f12a31f03daf3bad3470cfbf96.** No evidence-gate weakening or concrete trigger/guard defect found; no R2 physics re-review is warranted for these two paths alone. Re-review on any new source head according to the changed scope.
2. **No implied merge, deploy or PR55 approval.** An owner/admin must establish branch-protection required statuses (403 here), including treatment of skipped checks and the historic failed PR55 product job. Do not mark the historic red green.
3. **Address PR55 integration order explicitly.** If PR56 is merged after separate owner approval, PR55's source-preview workflow requires a bounded current-PR-base adjustment and new exact-head CI/review before PR55 could be integrated. Do not casually expand or waive its 14-path protected change contract.
4. Keep PR54 and PR55 draft/unmerged until their own owner-authorized gates are met. Do not run OpenModelica, regenerate references, rewrite original attempts, promote diagnostic evidence or integrate historical C1 work.

**Final verdict: SCOPED PASS (PR56 CI applicability correction only); PR55 future integration order and exhaustive required-status policy remain unresolved external merge gates.**
