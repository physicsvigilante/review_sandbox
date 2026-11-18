# SIM_HEAT PR #57 — independent Chat B R1 correction review 02

**Verdict: SCOPED PASS (R1) for the corrected duplicate-Host refusal and local-machine privacy guidance.** The two prior MINOR findings are resolved within the stated trusted-local-source-inspection contract. No new blocker, physical/numerical semantic change, or historical evidence promotion was demonstrated. This verdict is **not owner authorization to merge, deploy, perform native execution, or qualify diagnostic evidence**.

| Field | Pinned identity / scope |
|---|---|
| Source | [physicsvigilante/sim_heat PR #57](https://github.com/physicsvigilante/sim_heat/pull/57), verified **draft, open, unmerged** |
| Base main | 20f5605d28f22d4a7dc86ad478a4cf44347157d4 |
| Old head reviewed in immutable [review-01](review-01-chat-b.md) | e8a9696c8f14bc59c2d3918e65c987a8c4230bf0 |
| **Exactly reviewed corrected HEAD** | **a663c4c8c37494c1db6ef5fcaf32da0d4ba4fcba** |
| **Corrected Git tree** | **0c44961b473d23737b0c9f3b3f2cd3db65b9f264** |
| Synthetic PR merge | d99773ed095a1b2809be60992eecd619109d7ffb, tree identical to corrected source; parents are pinned main then corrected HEAD |
| Reviewer / date | Separate-context Chat B (GPT-6), 2026-11-18 |
| Risk / task | Focused R1 re-review of duplicate Host headers, raw HTTP regression, privacy guidance, exact-head CI and archive preservation |
| Source edits / native operations by this review | **None.** No OpenModelica query, installation, compilation, simulation, reference regeneration or native-runner execution |
| Review-hub edit | This new review-02 report only; original review-01 remains historically bound to the old head |

## Scope and exact correction

I read the central [correction request](../CORRECTION-REQUEST-02.md), [reviewer prompt](../REVIEWER-PROMPT-02.md), original [review-01](review-01-chat-b.md) (Git blob 790f60343603c6840c6b9302d19b802d432e21ef), [developer disposition](../responses/response-01-chat-a.md), source and review-hub AGENTS.md, and central PROTOCOL.md, REVIEW-RISK-POLICY.md and REVIEW-TEMPLATE.md.

Independently queried GitHub's exact commits/trees and compared old head to new head: **one corrective commit; exactly three modified files**: tools/authoring_workbench.py (+3/-1), tests/test_authoring_workbench.py (+45), docs/LOCAL_AUTHORING_WORKBENCH.md (+2). Full base-to-HEAD diff remains **exactly five added files**, with no modifications to existing h1/, experiments/, qualification/, viewer/, native runner, archived originals or frozen C1 evidence. Inspected complete corrected workbench source, new tests, guide, browser smoke and CI workflow; inspected the unchanged h1/source_preview.py source-only status creation and archive replay script. This is a bounded HTTP/doc correction, not a novel physical source-admission or solver implementation.

## F-01 — RESOLVED / prior MINOR duplicate Host vulnerability

**Code:** [corrected tools/authoring_workbench.py around lines 93–100](https://github.com/physicsvigilante/sim_heat/blob/a663c4c8c37494c1db6ef5fcaf32da0d4ba4fcba/tools/authoring_workbench.py#L93-L100); [raw regression test](https://github.com/physicsvigilante/sim_heat/blob/a663c4c8c37494c1db6ef5fcaf32da0d4ba4fcba/tests/test_authoring_workbench.py#L99-L139).

The original reviewer **actually reproduced** valid-then-evil duplicate Host returning HTTP 200 plus admitted JSON at **old** HEAD; reversed order returned 421. Chat A records that the newly written raw-wire regression **first failed three cases on old code**: valid+evil GET, duplicate-valid GET and valid+evil HEAD, each erroneously giving 200. Those failures are **historical failures, not passes**; I did not rerun old head in this cycle.

The corrected handler uses case-insensitive parsed-header collection via self.headers.get_all('Host', []) and refuses unless there is **exactly one** header whose normalized value equals the server's actual 127.0.0.1:port. Refusal is HTTP 421, using a fixed non-source body, **before** any path dispatch or resource lookup. GET and HEAD share the route guard; HEAD sends no body. One correctly formed singular Host still serves the actual admission payload. Binding remains hardcoded to IPv4 loopback, with only snapshotted allowlisted resources.

**Independent personally executed bounded adversarial check:** A disposable Python 3.13.5 HTTP server using a manually transcribed copy of the corrected PreviewHandler routing/response logic and a clearly synthetic in-memory source JSON was exercised by **16 raw TCP HTTP/1.1 requests**, all PASS on the completed second harness run. Probes included single-valid GET/HEAD (200, correct sentinel for GET), valid+evil and evil+valid GET (421), valid+valid GET and HEAD (421), valid+evil HEAD (421), missing Host GET/HEAD (421), mixed-case duplicate header names (421), mixed-case single name (200), wrong port and localhost hostname (421), trailing-space Host (421), repeated leading HTTP header whitespace (parsed as a single correct Host, 200), and triple Host (421). All 421 GETs returned only the fixed 'Invalid Host' text and no source JSON; all HEAD responses had empty bodies. Leading optional whitespace accepted after standard Python header parsing is not a duplicate-Host bypass. **Boundary:** this is an isolated standard-library behavior check, **not an execution of the full pinned SIM_HEAT module or a real admitted H1 model**, so hosted pinned CI below is the actual source-integration evidence.

**First attempt provenance:** My initial disposable probe harness incorrectly asserted that a rejected **HEAD** must carry the explanatory body; it failed after the first five valid controls when HEAD correctly returned an empty body. I corrected only that reviewer harness expectation and reran all sixteen cases to pass. This is a reviewer-test mistake, **not a SIM_HEAT defect**. The separate developer pre-fix three-failure regression record remains acknowledged and unchanged.

**Regression coverage:** the actual corrected source test creates the real H1 D1 loopback server and sends duplicate raw header bytes, both orders, duplicate-valid, duplicate HEAD and missing Host, with a valid singular control; source JSON is excluded from refused bodies. Both pinned hosted workbench CI logs explicitly show test_duplicate_host_headers_refused_in_both_orders **ok**. I found no remaining demonstrated F-01 defect in the declared local-only R1 scope.

## F-02 — RESOLVED / prior MINOR privacy guidance

**Guide:** [docs/LOCAL_AUTHORING_WORKBENCH.md](https://github.com/physicsvigilante/sim_heat/blob/a663c4c8c37494c1db6ef5fcaf32da0d4ba4fcba/docs/LOCAL_AUTHORING_WORKBENCH.md). **Served help:** corrected HELP constant in [tools/authoring_workbench.py](https://github.com/physicsvigilante/sim_heat/blob/a663c4c8c37494c1db6ef5fcaf32da0d4ba4fcba/tools/authoring_workbench.py#L34-L43).

Both surfaces explain that another process on the **same machine** can fetch the admitted in-memory source preview/provenance when it knows the session port. The guide explicitly states there is **no authentication between local processes**; the help page conveys the same consequence as 'Any process on this computer ... can read'. Both tell teachers to omit secrets from models/provenance, avoid shared or untrusted machines and stop the server with Ctrl+C. The fixed help asset is in the route allowlist; the source test checks the served /index.html bytes for the warning and Ctrl+C. This review directly inspected the pinned HELP literal and the matching test, **not a full checkout-hosted HTTP help fetch**. Language does not claim source custody, textbook authentication, private-from-local-processes behavior or fitness as a public server. Browser-imported JSON remains merely display-schema validated and is not native-qualified.

**Residual documented limit, not a newly discovered defect:** any local process that knows the port and sends the valid singular Host can read the payload. Duplicate-Host refusal is defense in depth, not local authentication. Do not expand this R1 result into a general remote-web-service security claim.

## Exact-head CI and preservation evidence

I independently inspected GitHub run metadata, job steps and text logs plus GitHub artifact-list metadata (not merely the PR description):

| Hosted run | Checked identity | Result / relevant evidence |
|---|---|---|
| [Push 44312686935](https://github.com/physicsvigilante/sim_heat/actions/runs/44312686935) | push, source HEAD a663c4c8… | **SUCCESS**; job 134830622239, artifact 14431216832; size 13,841,352 bytes, GitHub SHA-256 53a201c4561bbca3668409fddbf850381ff5ad4551c91622653678651238d0c5 |
| [PR 44312700673](https://github.com/physicsvigilante/sim_heat/actions/runs/44312700673) | PR head a663c4c8…, synthetic checkout d99773ed… with **same tree** | **SUCCESS**; job 134830670253, artifact 14431251686; size 13,841,327 bytes, GitHub SHA-256 0be4a67e13d723a153f1aabfff9c7d83a94f527c7c43f9285c233869d397f6c1 |
| [Audit-core 44312700604](https://github.com/physicsvigilante/sim_heat/actions/runs/44312700604) | PR head a663c4c8… | **SUCCESS**; job 134830671172, artifact 14431975359; size 5,874,260 bytes, GitHub SHA-256 6404d2e6dd46d9ecbe28ca12f39f78c3524baa00befc902929fa2f6ea078bd0a |

Each workbench job log confirms **H1 152 pass, analytical 4 pass, adapter 62 pass/1 optional skip, product 40 pass (including all 7 workbench tests), Node 42 pass**: 300 unique passes and one skip per run, not 600 additive passes. The corrected raw regression is explicitly reported as passing on both runs. Existing source-preview/documentation parity checks succeeded, including byte comparison of saved D2/D2_K2 comparison index and TEACH_SPLIT3 source-only JSON. Real-HTTP Chromium existing explorer/source/docs and D1 desktop, S1 mobile, TEACH_SPLIT3 desktop local-workbench smoke steps passed in **hosted CI**, not in a personally executed browser session.

**Six original archived diagnostics:** The unchanged viewer/network/tools/replay_published_archives.py enumerates **D1, D2, DEV_BRIDGE, TEACH_RING4, S1, D2_K2** from the five original ZIP artifact IDs 14152886226, 14155084346, 14204656273, 14215520616, 14153251022. For each, it requires the original full-ZIP SHA match and a **byte-identical** regenerated diagnostic preview, raises on mismatch, and only then emits status BYTE_IDENTICAL with nativeExecutedByReplay=false. Both workbench CI logs show this entire command completed successfully and its receipt was retained as archive-replay.json. Existing original archive assets/readers/catalogs are outside the five-file diff. Thus the successful **hosted replay gate** supports six-case byte preservation; it is **not a new native run**. Source-only h1/source_preview.py still sets evidenceKind=authored_source_only, nativeExecuted=false, nativeQualified=false, sourceFidelityQualified=false, publicRequestStatus=not_computed and individual request statuses not_computed; that file was unchanged.

**Evidence limit:** This environment could read source, GitHub job logs, artifact-list sizes and SHA-256 metadata but could **not download the binary artifact ZIPs** for an independent byte/CRC audit or personally replay the original archives. Consequently the developer's claim that each ZIP has 56 distinct CRC-valid members and the actual six-row saved receipt contents are **developer/hosted evidence, not my independent ZIP verification**. The GitHub artifact API independently corroborates the listed hashes/sizes, and the successfully completed fail-closed replay step supports the six case assertions. No false claim of personally downloading/re-hashing artifacts or personally running hosted Chromium is made.

## Separate scope judgments

| Dimension | Judgment | Basis and limit |
|---|---|---|
| Source interpretation fidelity | **SCOPED PASS; external source truth unverified** | Same H1 load_study and source builder, corrected Host-only guard; exact bytes/statuses unchanged in source scope; attribution is not independently authenticated |
| Physical/numerical correctness | **NOT RE-ADJUDICATED** | No physics/solver/numeric path changed, analytical CI passed; no new independent physical measurements |
| Native simulation / observable coverage | **NOT RUN / NOT QUALIFIED** | Workbench performs source-only admission, requests stay not_computed; six original archives remain diagnostic_only/nativeQualified=false |
| Evidence integrity / provenance | **SCOPED PASS with bounded ZIP-inspection caveat** | Pinned exact commits/tree, unchanged protected code and archives, successful hosted six-case fail-closed replay, artifact metadata; no personal ZIP rehash |
| HTTP refusal/privacy | **SCOPED PASS** | Actual CI raw-wire regression, inspected exact guard and guide/help, 16 isolated raw HTTP probes; same-machine unauthenticated visibility explicitly remains |
| Teacher-facing usefulness | **SCOPED PASS for documented source inspection only** | Hosted D1/S1/TEACH_SPLIT3 browser paths pass; no blind LLM/teacher authoring acceptance or public-server guarantee |
| Textbook-answer completeness | **NOT APPLICABLE** | No computed-answer pathway added |

## Release advice

**SCOPED PASS for PR57 corrected R1 HTTP/privacy findings only; no R2 escalation indicated for this three-file fix.** Leave existing review-01 and its first-failure history unchanged. Retain the complete hosted archive receipt/artifacts for a later reviewer with binary access if independent rehash is demanded; this is a transparent evidence limit rather than an observed source blocker. No further source change is required for F-01/F-02 based on the evidence inspected.

**Keep source PR #57 draft and unmerged until separate, explicit owner merge approval.** Do not deploy as an authenticated public service, run or install OpenModelica, regenerate original/frozen references, invoke a native runner, merge historical C1 material, rewrite original diagnostic archives, or promote any archived diagnostic to qualified evidence. This separate-context LLM review does not attest human evaluation or distinct model weights.
