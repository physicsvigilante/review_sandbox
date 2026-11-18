# SIM_HEAT PR54 — implemented, tested, focused R1 pending

**Status: `IMPLEMENTED; EXACT-HEAD-CI-PASS; AWAITING-FOCUSED-INDEPENDENT-R1; DRAFT-UNMERGED; NO-NATIVE-AUTHORIZATION`.**

[Source PR54](https://github.com/physicsvigilante/sim_heat/pull/54): exact head **`8f6ef1d0f8d0ebd938620c5694bc11856a5c9e7e`**, tree **`89db0700884d1f528c00715c5bb1b888d1378f1c`**, parent/base main **`0278b79b4da1c3196edca7903189713e0482f3f6`**. Ten paths, four modified/six added. No independent verdict or source merge approval yet.

## Product change

Implements PR53's nonblocking F-01/F-02 follow-ups in a separate candidate: canonical capability Markdown now has a generated static HTML view with actual browser navigation; the historical H1 contract is explicitly labeled historical; a current source-backed authoring guide documents existing admission behavior. The exact guide walkthrough makes temporary D1 copies, exercises valid admission, a stale-hash refusal, an attributed illustrative edit, and an unknown observation refusal through four real H1 CLI calls. No native values are computed. An existing-composition scratch exercise is not unfamiliar author-to-native qualification.

The historical contract, offline amendment and complete `h1`, `experiments`, `qualification`, `viewer` paths remain unchanged. Published native diagnostic data is not reclassified. The bounded renderer adds no runtime scripts or external assets; committed HTML is checked against its Markdown source.

## Verified evidence

[Run **44245470832**](https://github.com/physicsvigilante/sim_heat/actions/runs/44245470832), push, completed successfully:

| Job | Actual checkout | Unit results | Other checks |
|---|---|---|---|
| Candidate134603246408 | `8f6ef1d0...` | **266 passed, one optional skip** | Six BYTE_IDENTICAL original bundles, unchanged comparison, full explorer/entry browser, generated parity and new real HTTP registry/guide/source-link navigation PASS |
| Baseline134603246932 | exact merged main `0278b79b...` | **257 passed, one optional skip** | Six original bundles and comparison unchanged; full explorer/entry browser PASS |

Candidate 17 product tests include eight inherited plus nine new methods. Totals overlap across jobs; do not add. Baseline intentionally skips the successor-only generated-document step, separately from the optional unittest skip. Event/artifact names use candidate SHA; actual checkout receipts establish the baseline identity.

| Artifact | Bytes / unique CRC-valid members / PNGs | Whole ZIP SHA-256 |
|---|---|---|
| Candidate14400973503 | 10,639,019 / 45 / 27 | `b26c9ed5e828f01e8d873208146f8982a7613186a8c447d172fb0c3352c45757` |
| Baseline14401083576 | 7,815,278 / 38 / 23 | `c4ffaf855f28dad9535cae2a0036d24027035cecc70bc2ef043b8714556cddfb` |

Chat A downloaded/rehashed/CRC-checked both, inspected logs/replay/head/tree/diff and comparison bytes, safely extracted complete source.tar snapshots and reconstructed exact Git trees locally. Candidate tree89db and baseline treec73 both matched GitHub. Protected paths were directly compared unchanged. Selected retained registry/mobile and guide/desktop screenshots were visually inspected.

**Personally executed developer tests:** initial seven locally available new tests and exact-HTML Chromium `page.set_content` at320/390/1440; after verified complete source reconstruction, **all 17 product tests passed locally on exact candidate bytes under Python3.13.5**, including all four real admission CLI calls. Renderer `--check` passed; originals/source unchanged. Full inherited suites, original-archive replay and actual HTTP browser runs remain hosted execution inspected by Chat A, not local reruns.

First static browser harness reused a page with old focus and failed a later viewport assertion; fresh-page-per-viewport harness passed all six document/viewport probes. This retained harness error is not a demonstrated page defect or a retroactively passing first attempt. No teacher study, accessibility/cross-browser certification, zero-HTTP-error or independent scientific qualification is claimed.

## Review and preservation

[REQUEST](REQUEST.md) and [reviewer prompt](REVIEWER-PROMPT-01.md) are ready. Chat B alone must author NEW `reviews/review-01-chat-b.md`. Focused R1 covers renderer/content/link parity, truthful current guidance versus pinned implementation, scratch-only CLI walkthrough/cleanup, browser navigation and preservation. Escalate only for demonstrated changed physical/evidence semantics.

PR53 is already [integrated and post-merge verified](../pr-53/INTEGRATION-01.md). Its original review blob `95c6a05f7c66dbefaf57f3d3a8b7f8d59c759226` and findings remain unchanged, not a blanket verdict on this successor. No OpenModelica query/install/build/launch, native runner, frozen-reference regeneration/adoption, deployment or historical C1-stack integration occurred. This new candidate remains draft/unmerged; six archived outputs retain `diagnostic_only/nativeQualified=false`, and C1 failures/uncomputed native requests remain historical facts.
