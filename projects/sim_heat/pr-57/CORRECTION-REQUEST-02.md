# SIM_HEAT PR57 — CORRECTION-REQUEST-02: focused R1 independent re-review of Host-header hardening

**Source PR:** [physicsvigilante/sim_heat draft #57](https://github.com/physicsvigilante/sim_heat/pull/57), **still open, draft and unmerged**.

| Pin | Exact value |
|---|---|
| Base merged `main` | `20f5605d28f22d4a7dc86ad478a4cf44347157d4` |
| Original reviewed source | `e8a9696c8f14bc59c2d3918e65c987a8c4230bf0`, tree `b59f6aabec9c3cca5c0c2fd52d429a0df04b208f` |
| Independent original review | [Chat B review-01](reviews/review-01-chat-b.md), blob `790f60343603c6840c6b9302d19b802d432e21ef`, **SCOPED PASS (R1), two MINOR follow-ups** |
| **Corrected HEAD — NEW review target** | **`a663c4c8c37494c1db6ef5fcaf32da0d4ba4fcba`** |
| **Corrected Git tree** | **`0c44961b473d23737b0c9f3b3f2cd3db65b9f264`** |
| Corrective diff vs old reviewed HEAD | **3 modified files only:** `tools/authoring_workbench.py`, `tests/test_authoring_workbench.py`, `docs/LOCAL_AUTHORING_WORKBENCH.md`; no other files |
| Full base diff | Still exactly five original PR57 ADDED paths; all prior H1/physics/evidence/native/viewer sources unmodified |
| Independent deliverable | **New `projects/sim_heat/pr-57/reviews/review-02-chat-b.md`** by separate-context Chat B |
| Risk class | **Focused R1** HTTP entry hardening and privacy guidance; escalate to R2 only if real physical/result/evidence semantics changed |
| Merge/native authority | **NONE**. Do not merge, deploy, query/install/build/launch OpenModelica, regenerate original/frozen references or integrate historical C1 work. |

Read [original independent review](reviews/review-01-chat-b.md), [Chat A disposition](responses/response-01-chat-a.md), source `AGENTS.md`, central `PROTOCOL.md` / `REVIEW-RISK-POLICY.md` / `REVIEW-TEMPLATE.md`, and exact three-file code diff before testing.

## Finding F-01 — independent reproduction and exact correction

Old reviewed source allowed a duplicated Host header where **the first was valid** and the second hostile. Chat B independently reproduced `200 OK` and admitted source JSON. Chat A built a **real raw socket HTTP/1.1 test first**, and before implementing the fix observed three failures: valid+evil GET 200, duplicate-valid GET 200, valid+evil HEAD 200. Retain this first failure record; the original source was not retroactively passed.

Now `PreviewHandler._route` gets **all** HTTP `Host` occurrences via `self.headers.get_all('Host', [])`, requires **exactly one** string matching actual bound `127.0.0.1:<port>`, and sends HTTP **421** before returning any resource otherwise. The raw-wire test covers: valid singular control 200 and correct admitted JSON; valid+evil GET 421; evil+valid GET 421; duplicate valid+valid GET 421; valid+evil HEAD 421; missing Host 421; no source-data leak on refusal. The same code path handles GET and HEAD. All old raw model/study/download, port/path/Host, POST/PUT/PATCH/DELETE refusal tests remain.

**Independent tasks:** Personally reproduce raw two-Host behavior on corrected source (both orders), including same duplicate Host and HEAD. Probe header capitalization, whitespace, missing host, incorrect local port and no data leak if feasible. Confirm one valid Host still serves the actual admitted `studyId`/source SHA and the server still binds only loopback. Avoid mistaking a lack of remote public bind for strong protection from other processes on the same host. Check no change to native, H1 admission, output labels, or external reader fallback.

## Finding F-02 — privacy documentation and local help

The trusted-local-machine warning now appears **both in the standalone guide and the HTTP-served local help page**: other processes on the same computer can read in-memory admitted source/provenance if they know the port, no authentication for local processes; users must avoid secrets/sensitive information, shared/untrusted computers, and stop the server with Ctrl+C. The new test checks that the help page exposes the warning. This is a description of the existing bounded deployment model, not a new authentication feature.

**Independent tasks:** Check the guidance explicitly and verify HTTP response contents. Ensure it does not claim private-from-local-processes or origin/source authenticity. Confirm that source-only inspector imported JSON is display-schema checked, not trusted or native-qualified.

## Exact-head CI and evidence

All new GitHub CI checks completed **SUCCESS**:
- [Branch push run **44312686935**](https://github.com/physicsvigilante/sim_heat/actions/runs/44312686935), actual corrected source HEAD/tree, artifact [**14431216832**](https://github.com/physicsvigilante/sim_heat/actions/runs/44312686935/artifacts/14431216832), **13,841,352 bytes**, SHA256 **`53a201c4561bbca3668409fddbf850381ff5ad4551c91622653678651238d0c5`**, **56 unique CRC-valid ZIP members**.
- [PR run **44312700673**](https://github.com/physicsvigilante/sim_heat/actions/runs/44312700673), GitHub synthetic merge HEAD **`d99773ed095a1b2809be60992eecd619109d7ffb`**, first parent current main, second parent corrected candidate, **same complete tree `0c44961...`** as source. Artifact [**14431251686**](https://github.com/physicsvigilante/sim_heat/actions/runs/44312700673/artifacts/14431251686), **13,841,327 bytes**, SHA256 **`0be4a67e13d723a153f1aabfff9c7d83a94f527c7c43f9285c233869d397f6c1`**, **56 unique CRC-valid ZIP members**.
- [Audit-core run **44312700604**](https://github.com/physicsvigilante/sim_heat/actions/runs/44312700604), **SUCCESS**; artifact **14431975359**, **5,874,260 bytes**, SHA256 **`6404d2e6dd46d9ecbe28ca12f39f78c3524baa00befc902929fa2f6ea078bd0a`**, **33 unique CRC-valid members**.

Both workbench CI runs report **300 unique unit test PASS, one optional SKIP**: H1 152, analytical 4, adapter 62 pass/one skip, product **40** (33 prior + seven workbench), Node 42. Six original historical native diagnostic archive case replays D1, D2, DEV_BRIDGE, TEACH_RING4, S1, D2_K2 all **`BYTE_IDENTICAL`** and `nativeExecutedByReplay=false`; original D2/D2_K2 comparison and TEACH_SPLIT3 *source-only* JSON regenerated byte-identically. Hosted actual HTTP Chromium existing explorer/source-preview/docs and D1 desktop, steady S1 mobile, TEACH_SPLIT3 desktop local workbench (admission/refusal, security routes) **PASS**. Counts overlap between runs and personal tests; do not sum.

Chat A personally downloaded/rehashed all three ZIPs, checked all unique names/CRCs, reconstructed the **complete Git source trees** from both full `source.tar` snapshots to **exact `0c44961...`**, inspected exact checkout/scope/file diff and six-case archive/Browser logs. Developer personally ran the **full 300 unit tests locally**, renderer parity and saved comparison/source-only payload byte comparisons, and verified the raw-Host three initial fail cases then the corrected PASS. The old and new reviewer local Chromium HTTP navigation may be blocked by `ERR_BLOCKED_BY_ADMINISTRATOR`; hosted real HTTP browser PASS is separate evidence. No new native simulator operation.

## Required final judgment

Review only the two minor corrections and relevant regression/preservation surfaces, with separate judgments for source interpretation (unchanged), numerical/native coverage (not qualified), source-only status integrity, HTTP privacy, teacher usability limits and evidence preservation. Make a **new independent Chat B report** at `projects/sim_heat/pr-57/reviews/review-02-chat-b.md` with exact corrected HEAD/tree, personally executed/adversarial probes, evidence provenance, any remaining limitations and **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** verdict. Preserve original review-01 and all older source/CI records. A scoped pass **never grants merge/native permission**; PR57 must remain draft/unmerged without an explicit separate owner merge approval.
