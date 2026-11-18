# SIM_HEAT PR54 — focused R1: rendered product documentation and tested admission walkthrough

**Source:** [draft PR54](https://github.com/physicsvigilante/sim_heat/pull/54). **No merge, deployment or native execution authorization.** Read central [PROTOCOL](../../../PROTOCOL.md), [risk policy](../../../REVIEW-RISK-POLICY.md), [review template](../../../REVIEW-TEMPLATE.md) and exact-source `AGENTS.md`.

| Identity | Exact value |
|---|---|
| Candidate head | `8f6ef1d0f8d0ebd938620c5694bc11856a5c9e7e` |
| Candidate tree | `89db0700884d1f528c00715c5bb1b888d1378f1c` |
| Parent / merged PR53 main | `0278b79b4da1c3196edca7903189713e0482f3f6` |
| Parent tree | `c73f86e58be8b9eb55756432aae064f00719487f` |
| Branch | `product/authoring-guide` |
| Risk | Focused R1, documentation/navigation and faithful presentation of existing behavior |
| Independent deliverable | NEW `projects/sim_heat/pr-54/reviews/review-01-chat-b.md` |

## Reason and bounded change

PR53's [independent R1 report](../pr-53/reviews/review-01-chat-b.md), unchanged blob `95c6a05f7c66dbefaf57f3d3a8b7f8d59c759226`, SCOPED-PASSED its original head with two nonblocking follow-ups: F-01 did not establish browser-readable Markdown registry/navigation; F-02 recommended a historical proposed contract without clarifying its lifecycle label. PR53 has since been owner-approved, merged and [post-merge verified](../pr-53/INTEGRATION-01.md). This new candidate implements the follow-ups and gives authors current instructions; it does not reopen the unchanged physics audit.

Exactly **ten paths: four modified, six added**:

- Modified: `.github/workflows/product-entry-ci.yml`, `index.html`, `docs/CAPABILITIES.md`, `tests/test_product_entry.py`.
- Added: `docs/AUTHORING.md`, `docs/AUTHORING.html`, `docs/CAPABILITIES.html`, `tools/render_product_docs.py`, `tests/test_product_docs.py`, `tests/browser_product_docs.py`.

Protected source/data paths `h1`, `experiments`, `qualification`, `viewer` and the historical H1 implementation contract/offline amendment are unchanged. No changed engine, admitted grammar, numerical tolerance, physical model, original reference, native runner or published case/catalog/comparison bytes. CI enforces this and Chat A compared complete extracted snapshots.

## Review these actual behaviors

### Canonical content and usable static navigation

`CAPABILITIES.md` stays canonical; only the two source-link/label lines change. `AUTHORING.md` is the new current guide. The bounded, standard-library renderer converts only these trusted documents to committed static HTML, records the canonical file SHA, escapes raw HTML, permits relative/HTTPS links, and maps only the two generated-doc links from `.md` to `.html`. No runtime scripts, remote assets, Markdown service or user-upload surface. `--check` must refuse stale/missing output without silently rewriting it.

Check text, table, source-link and code-block fidelity; unsupported/unsafe markup handling relevant to the two inputs; duplicate/invalid heading/table/fence behavior; deterministic regeneration; readable desktop/mobile layout and table focus/scrolling. Historical/source-file links intentionally open original files, explicitly disclosed; this is not a promise to render all repository Markdown. The root registry link must actually navigate to HTML, not merely return HTTP 200.

### Current authoring guidance without rewriting history

The guide labels the older contract a historical foundation design record and preserves its original header. Check every important claim against pinned `h1/__main__.py`, `h1/study.py`, `h1/model.py`, `h1/policy.py` and D1/S1/D2_K2 source examples. It documents only supported constructors/fields/ports, public requests, provenance, analysis bounds and structured refusals. It distinguishes model identity/source checks from source fidelity, numerical acceptance and native permission. Admission outputs `nativeExecuted=false` and public readings `not_computed`; internal export names are not new public request operations.

### Execute the published walkthrough, not an unrelated example

The single fenced Python block in `AUTHORING.md` creates a temporary D1 copy. Four actual `python -B -m h1` calls exercise: unchanged valid control; illustrative model edit with stale SHA refused as `identity`; updated NEW scratch digest/attribution admitted with all requests `not_computed`; unknown target refused in the request report. It checks return codes/statuses and preserves original files, and cleans up the temporary directory. No original/native plan is repinned, no reference is generated, no solver/native operation occurs.

Tests extract and execute the exact block with subprocess restrictions. Independently inspect/run it where tools permit and distinguish complete actual CLI execution from reexpression. This is an existing-composition editing exercise, not the unfamiliar composition end-to-end milestone and not a source-only visualizer.

## Exact-head hosted evidence

[Push CI **44245470832**](https://github.com/physicsvigilante/sim_heat/actions/runs/44245470832) succeeded, with distinct actual checkouts:

| Job | Actual source | Unit outcome | Other outcomes |
|---|---|---|---|
| Candidate **134603246408** | `8f6ef1d0...` | **266 passed, one optional skip** | Six original bundles BYTE_IDENTICAL, comparison unchanged, full existing explorer/entry smoke, generated-page parity and real HTTP documentation navigation PASS |
| Postmerge baseline **134603246932** | merged main `0278b79b...` | **257 passed, one optional skip** | Six original bundles BYTE_IDENTICAL, comparison unchanged, full explorer and entry HTTP smoke PASS |

Candidate breakdown: H1 152 + arithmetic 4 + adapter 62 PASS/1 SKIP + Node 31 + product 17 = **266 PASS**. Product 17 is eight inherited plus nine new methods. Do not add overlapping candidate/baseline totals. Baseline intentionally skips successor-only generated documentation step; that is separate from the existing optional unittest skip.

The new actual-HTTP browser smoke navigates from root into rendered registry and guide, checks headings/tables/statuses/no page overflow/static markup, focuses a table region, clicks original D1 bundle/study JSON links, checks their response and visible content, and cross-navigates from registry to guide at 1440×1000 and 390×844. Four new screenshots retained. Existing entry/explorer suites separately exercise their established routes/interactions. No JS page errors; favicon 404 remains harmless HTTP behavior, not a claim of zero network errors or accessibility certification.

## Original artifacts and executable source snapshots

| Artifact | Size / unique CRC-valid members / PNGs | Whole ZIP SHA-256 |
|---|---|---|
| [Candidate **14400973503**](https://github.com/physicsvigilante/sim_heat/actions/runs/44245470832/artifacts/14400973503) | 10,639,019 bytes / 45 / 27 | `b26c9ed5e828f01e8d873208146f8982a7613186a8c447d172fb0c3352c45757` |
| [Baseline **14401083576**](https://github.com/physicsvigilante/sim_heat/actions/runs/44245470832/artifacts/14401083576) | 7,815,278 bytes / 38 / 23 | `c4ffaf855f28dad9535cae2a0036d24027035cecc70bc2ef043b8714556cddfb` |

Chat A personally downloaded and hashed both, checked ZIP uniqueness/CRC, actual head/tree/source diff, all suite summaries, replay receipts and comparison bytes. Each includes **complete `source.tar`** from the actual checkout. Safely extract to a separate directory; reject unexpected paths/member types. Chat A reconstructed each complete Git tree locally and obtained exactly `89db070...` for candidate and `c73f86e...` for baseline, verifying all original source bytes and modes. This provides a complete source option even when direct cloning is blocked. Do not execute archived native binaries.

Baseline artifact name/event SHA contains `8f6ef1d0...` but `head-sha.txt` is **0278b79b...**; baseline diff is empty. The source receipts, not the event name, identify the checkout.

## Developer-personal checks and first-attempt limitation

Before push: Python/YAML syntax, renderer parity, seven locally runnable new unit tests; exact HTML Chromium `page.set_content` probes at widths 320/390/1440. First harness reused a page and failed a later viewport focus assertion; fresh-page-per-viewport harness then passed all six document/viewport probes. Preserve this harness failure/correction; it is not a demonstrated production defect and the first run is not retrospectively counted as all-pass.

After verified complete source reconstruction, Chat A personally ran **all 17 product tests on exact candidate source** under Python 3.13.5: passed, including the four real admission CLI invocations in the exact guide block, original-byte checks and temporary cleanup. Renderer `--check` passed and source remained unchanged. The complete inherited suites, six-original replay and actual browser HTTP runs were hosted executions inspected by Chat A, not local executions. Selected retained registry/mobile and authoring/desktop screenshots were visually inspected. This is not a teacher study, cross-browser qualification or new numerical certification.

## Independent deliverable and boundaries

Write your own NEW report with **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, exact head/tree, concrete findings, personally executed versus inspected evidence and preserved limitations. Focus on F-01/F-02 correction, current guidance accuracy, renderer parity, walkthrough preservation and navigation. Escalate to R2 only for a real changed source-interpretation/physical/result/provenance meaning, not merely because new documents mention existing physics.

Do not edit old reports, original examples, frozen references or historical failures. Six published cases remain `diagnostic_only/nativeQualified=false`; C1 native readings remain uncomputed. No OpenModelica query/install/build/launch, native runner, frozen-reference regeneration/adoption, production merge, historical-stack merge or deployment is authorized. A review pass does not authorize any of them. The full unfamiliar author-to-native workflow remains future work.
