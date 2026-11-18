# SIM_HEAT PR53 — focused R1: explorer entry and capability/evidence registry

**Source:** [draft PR53](https://github.com/physicsvigilante/sim_heat/pull/53), branch `product/explorer-entry`, target main. Implementation and exact-head push CI complete; independent review pending. No merge or native execution authorization.

| Identity | Exact value |
|---|---|
| Head | `86c8c146ec025ca62a4484a7e20eb76b5530f29d` |
| Tree | `c73f86e58be8b9eb55756432aae064f00719487f` |
| Base main | `4162c3d47016150076b226ebe2585073a785547a` |
| Base tree | `2ad10a1679d528f88030494f0349171502ef8e0f` |
| Diff | One commit, six paths: five added, README modified |
| Risk | **R1, focused independent review required because existing evidence is newly presented** |
| Reviewer output | NEW `projects/sim_heat/pr-53/reviews/review-01-chat-b.md` |

Read central [protocol](../../../PROTOCOL.md), [risk policy](../../../REVIEW-RISK-POLICY.md), [template](../../../REVIEW-TEMPLATE.md), pinned source `AGENTS.md`, and the exact source. Chat A must not author Chat B's report. Give SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE, with personal versus hosted evidence clearly attributed.

## Why this change

The audit recommended consolidating the useful explorer rather than extending mock authorization demonstrations. The owner-approved PR51+52 corrections are now merged and post-merge verified; see [integration receipt](../pr-52/INTEGRATION-01.md). This candidate supplies the first product-consolidation increment, not a new solver or a completed author-to-native workflow.

## Six-file scope

- New `index.html`: static root start page; primary link to the unchanged generic explorer, second link to the saved comparison, evidence-category cards, a practical inspection path and local-server instructions. Responsive layout, skip link and keyboard navigation. No scripts, forms, frames, external resources or native invocation.
- Modified `README.md`: makes root startup primary while retaining the original direct viewer route; links the current registry; preserves limitations, C1 history and explicit native authorization boundary.
- New `docs/CAPABILITIES.md`: current capability/evidence registry, original source links and six-case inventory. Archived native diagnostics, analytical checking data and expected-only source views remain separate. No new result or numerical-qualification claim.
- New `tests/test_product_entry.py`: eight standard-library tests for destinations/IDs, explicit evidence categories/statuses, static local page, link resolution, exact catalog inventory, existing bundle hashes/statuses, and plain/encoded parent-path escape in its link-checking helper. This helper is a test utility, not a new production input-security boundary.
- New `tests/browser_product_entry.py`: actual localhost Chromium navigation on desktop/mobile; keyboard entry to the existing explorer; ready comparison view; registry HTTP request; no horizontal page overflow or page errors. Existing full explorer smoke remains separate.
- New `.github/workflows/product-entry-ci.yml`: two explicitly distinct checkouts: exact merged-main baseline and new candidate. Full existing tests, original archive replay and explorer smoke on each; new navigation tests only on candidate. Actual checkout receipts disambiguate workflow-event SHA from baseline source SHA.

**No changes anywhere in `h1/`, `experiments/`, `qualification/` or `viewer/`.** Their complete Git subtree identities match base; CI also asserts empty diffs there. Original model/studies, physics, decoder/checker/reference, numerical thresholds, runner, native plans, archived data, catalogs, comparison and every existing viewer file remain unchanged. The dated audit and original reports remain historical records.

Risk is R1 because this is bounded navigation/presentation of unchanged claims, not a physical/numerical/provenance contract change. Independently examine that classification; escalate if the actual content alters evidence meaning.

## Exact-head hosted evidence

[Push run **44238734097**](https://github.com/physicsvigilante/sim_heat/actions/runs/44238734097) completed SUCCESS, attempt 1, event head `86c8c146…`.

| Job | Actual checkout | Tests / evidence |
|---|---|---|
| `134581099995`, candidate | `86c8c146ec025ca62a4484a7e20eb76b5530f29d` | **257 passed, one optional skipped**: H1 152 + arithmetic 4 + adapters 62 pass/1 skip + Node 31 + entry 8. Six original bundle replays byte-identical; saved comparison unchanged; existing explorer smoke and new real-HTTP navigation smoke PASS. |
| `134581100335`, postmerge baseline | `4162c3d47016150076b226ebe2585073a785547a` | **249 passed, one optional skipped**; six original bundles byte-identical; comparison unchanged; existing explorer smoke PASS. New navigation step intentionally skipped because it is absent on baseline. |

Do not combine overlapping job totals. The baseline's intentional workflow-step skip is not the one optional unittest skip. The existing optional original-campaign mutation method remains skipped; genuine original campaign data is replayed separately.

### Artifacts personally downloaded and checked by Chat A

| Artifact | Size / entries | Whole ZIP SHA-256 |
|---|---|---|
| Candidate **14398477224** | **6,454,848 bytes; 38 unique CRC-valid members; 23 PNGs** | `6e8ce7d23eda335e12083d60098974953d3f212a38a746897a2e5e023f573347` |
| Baseline **14398721933** | **5,873,775 bytes; 33 unique CRC-valid members** | `27fc39b8971cc7525ae5cf2e97750c68a37d468435d91291cfd2738f0c15b0cd` |

Chat A verified metadata digest/size against downloaded bytes, CRCs/unique entries, `head-sha.txt`, `head-tree.txt`, source diffs, actual unit/browser logs, six `BYTE_IDENTICAL`/`nativeExecutedByReplay=false` records and new source hashes. Candidate diff is exactly six paths; baseline diff empty. Candidate's `entry-sources.sha256` matches the locally authored files. Desktop hosted screenshot was visually inspected; local desktop/mobile HTML screenshots were also inspected.

Artifact names and GitHub artifact metadata refer to the **candidate workflow event**. The baseline job explicitly checks out main; its internal head receipt and checkout step must be inspected before attributing evidence. It is not candidate evidence relabeled as main.

Developer-local execution was limited to syntax/YAML parsing and exact HTML through Chromium `page.set_content` for layout/keyboard behavior. Direct Git clone was unavailable; there was no local complete repository, eight-test-suite, six-archive or HTTP-route rerun. Full source executions and actual HTTP navigation occurred on hosted CI, then were downloaded/inspected. No claim of independent review, broad accessibility certification, cross-browser coverage or teacher trial follows.

## Focused review tasks

1. Verify exact six-path diff and unchanged engine/evidence/viewer subtrees. Check the startup commands and old direct routes remain usable. Inspect existing source docs/catalog before accepting the registry's claims.
2. Check that a reader can distinguish real archived diagnostics from separate calculated checking data and C1 expected-only/uncomputed information. No native qualification, arbitrary CSV authentication, apparatus geometry, live solver, teacher study or completed author-to-native workflow should be implied.
3. Inspect/test local links, skip-link and keyboard flow, desktop/mobile layout, actual entry into a ready explorer/comparison, and test adequacy. Treat tests as evidence with limits, not proof of every usability property.
4. Verify candidate and baseline actual checkout identities and hosted artifacts. Independently execute focused probes where possible, distinguishing source execution, reexpression and inspected hosted results.
5. Publish your own NEW report at the specified path. Review only changed navigation/presentation/testing and preservation unless an actual semantic defect requires escalation; do not reopen an unchanged whole-project physics audit.

## Boundaries and next stage

Both archived case modes remain `diagnostic_only`, `nativeQualified=false`; this is not new native execution or independent numerical qualification. C1 frozen failures/reference custody and nine uncomputed native requests remain unchanged. The next product milestone is still one unfamiliar supported composition end-to-end, with separately reviewed and explicitly authorized native execution.

Do not merge, deploy, edit original evidence, install/query/build/launch OpenModelica, invoke the native runner, regenerate frozen C1 references, or merge historical C1 branches. A positive focused review supports only this candidate; production integration remains a separate owner decision.