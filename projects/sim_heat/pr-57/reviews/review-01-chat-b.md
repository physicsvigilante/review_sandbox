# Independent Chat B R1 — SIM_HEAT PR #57

**Verdict: SCOPED PASS (focused R1), with one minor HTTP hardening finding and explicitly bounded evidence.** No blocker or changed physics, numerical, native, or qualification semantics demonstrated. This review is **not** a merge, deployment, classroom-validation, source-authenticity, or native-execution approval.

| Field | Independently reviewed identity |
|---|---|
| Source PR | [physicsvigilante/sim_heat#57](https://github.com/physicsvigilante/sim_heat/pull/57), draft/unmerged |
| Source base | `20f5605d28f22d4a7dc86ad478a4cf44347157d4` |
| **Exactly reviewed source HEAD** | **`e8a9696c8f14bc59c2d3918e65c987a8c4230bf0`** |
| **Git tree** | **`b59f6aabec9c3cca5c0c2fd52d429a0df04b208f`** |
| PR synthetic merge | `b9c6ca0383bf3a09048ead4d6b4c75734b0e9e83`; verified identical tree and ordered parents base + source HEAD |
| Reviewer | Independent-context Chat B, GPT-6; not a human or different-model-family attestation |
| Date/time | 2026-11-18 13:06 UTC |
| Class / scope | R1; local-only H1 source-admission glue, read-only HTTP surface, identity, real browser evidence, archive preservation |
| Source repository edits | **None**. All personal tests ran against extracted CI source in a separate temporary working area; no source PR/branch modified |
| Review hub edit | This **new** review report only |
| Native authority | None; **no OpenModelica invoked, installed, queried, built or run** |

## Source and CI identity

- Read pinned `AGENTS.md`, current H1 authoring/source-preview contracts, all five new files, relevant unchanged `h1/study.py`, `h1/source_preview.py`, and existing viewer `app.mjs`/`core.mjs`. The candidate diff is **exactly five added paths**: `.github/workflows/authoring-workbench-ci.yml`, `docs/LOCAL_AUTHORING_WORKBENCH.md`, `tools/authoring_workbench.py`, `tests/test_authoring_workbench.py`, `tests/browser_authoring_workbench.py`. No protected H1 parser, physical model, numerical evaluator, native runner, existing viewer, diagnostic catalog or frozen C1 path changed. Independently computed the five Git blob SHA-1s from the retained source tar and matched the corresponding pinned GitHub file blobs.
- Independently checked the GitHub Git-commit API: source HEAD's tree is `b59f6a...` and the PR synthetic merge has **the same tree**, with parents `20f5605...` and `e8a9696...`.
- Inspected [push CI 44305567524](https://github.com/physicsvigilante/sim_heat/actions/runs/44305567524) (job `134806109848`), [PR CI 44305754947](https://github.com/physicsvigilante/sim_heat/actions/runs/44305754947) (job `134806764112`) and [audit-core CI 44305754916](https://github.com/physicsvigilante/sim_heat/actions/runs/44305754916) (job `134806767959`): all concluded success. Downloaded and independently ZIP-tested **PR artifact 14428272787**: 13,840,382 bytes, SHA-256 `7ab64ea80770b3fa7e7787a7cb10b7eadf28de94051a2b1d3d5a2cf273e79e66`, **56 unique entries, all CRC-valid**. Its `head-sha.txt`, `head-tree.txt`, `scope-base-sha.txt`, `source-diff.txt` match the verified synthetic merge/tree/base and five-file scope. Push run log reports artifact SHA-256 `b68aca2e56f81afbea3ddd771db6ff699d0ba9a285b0c125e366fd50af75e6b6`; unlike the PR artifact, that ZIP was not independently downloaded/rehashed here.
- Inspected PR artifact test logs: **152 H1 passed; 4 analytical passed; 63 adapter tests with 1 existing optional skip; 39 product passed (including 6 new workbench tests); 42 Node passed**. Thus **299 unique unit passes and one skip** per run, not totals added across runs. Product HTML `--check`, saved D2/D2_K2 comparison and TEACH_SPLIT3 source-only output parity passed in CI. Analytical reference checks are **not native measurements**.
- The PR artifact's real-HTTP **hosted** Chromium log reports PASS on D1 desktop, steady S1 mobile, TEACH_SPLIT3 desktop, read-only/refusal requests and forged-import state clearing. Personally inspected retained `loopback/d1-desktop.png`, `loopback/steady-mobile.png`, `loopback/split3-desktop.png` and corresponding refused screenshots: source IDs, `not_computed`, unqualified metadata and cleared graph on forged import are visibly consistent. The separate existing explorer/source-preview/docs browser logs also passed. These are **hosted CI executions and artifact observations**, not my own successful local Chromium navigation.

## Findings

### F-01 — MINOR / HTTP Host validation: duplicate Host headers not refused

**Location:** [`tools/authoring_workbench.py:92-96`](https://github.com/physicsvigilante/sim_heat/blob/e8a9696c8f14bc59c2d3918e65c987a8c4230bf0/tools/authoring_workbench.py#L92-L96).

**Independently reproduced, real loopback HTTP:** for an admitted D1 server, submit a raw HTTP/1.1 `GET /viewer/source_preview/data/TEACH_SPLIT3.json` with two headers, first `Host: 127.0.0.1:<actual-port>`, second `Host: evil.invalid`. **Observed 200 OK with the admitted JSON.** Reversing their order gives **421**. The current `self.headers.get('Host')` checks only the first parsed value. A singular wrong Host correctly gives 421.

**Expected:** a strict Host allowlist should require **exactly one** Host header whose value equals the current `127.0.0.1:port`. **Fix/regression:** check `self.headers.get_all('Host', [])` count equals one, then exact equality; unit-test duplicate hosts in both orders, with a raw-socket request or equivalent. **Severity rationale:** no external-network bind, CORS grant, write path or demonstrated cross-origin exfiltration; a malicious local process able to send duplicate Host can already send the valid singular Host. Therefore this is a **real but nonblocking defense-in-depth defect** for the documented local-trusted-machine scope; do not call the current check an absolute strict-single-Host guarantee.

### F-02 — MINOR / privacy boundary documentation, not a demonstrated implementation defect

**Location:** [`docs/LOCAL_AUTHORING_WORKBENCH.md`](https://github.com/physicsvigilante/sim_heat/blob/e8a9696c8f14bc59c2d3918e65c987a8c4230bf0/docs/LOCAL_AUTHORING_WORKBENCH.md) and [`tools/authoring_workbench.py:129-139`](https://github.com/physicsvigilante/sim_heat/blob/e8a9696c8f14bc59c2d3918e65c987a8c4230bf0/tools/authoring_workbench.py#L129-L139).

The service is **loopback-only, not authenticated or private from other processes on the same machine**. An ordinary local client can GET the in-memory authored source/provenance JSON once it knows the port; this is inherent to the stated local HTTP design, not a network-reachability bypass. Recommend one explicit teacher-facing sentence: do not include secrets in source/provenance notes; on shared or untrusted machines, stop the session after inspection. A remote public-server threat model would need a separate security design/review. No R1 blocker on the declared trusted-local-use contract.

**No blocker/major code defect demonstrated** in admission ordering, path sandbox, no-write routes, source-only labeling, original archived diagnostics or standard hosted-browser refusals. Source hashes demonstrate internal bytes/descriptor consistency, **not independent author or textbook-source authenticity**; the documentation acknowledges this.

## Independently executed evidence (non-native)

1. **Six new workbench Python unit tests: PASS (6/6)** against the extracted exact-tree source. They exercise D1/S1/TEACH_SPLIT3, local HTTP allowlist, forbidden methods, wrong Host, stale hash, invalid public request and outside-root refusal.
2. **Fresh Chat B-authored model `CHATB_BRANCH2`** (not an existing H1 case, not the developer's reported scratch chain): two fixed boundaries `hot=345 K`, `cold=280 K`; bodies `core(m=0.7,c=480,T_initial=300)` and `load(m=1.2,c=780,T_initial=295)`; rods `feed` (area, k=160,L=0.4,A=0.00025), `splitA` (circular, k=43,L=0.18,d=0.01), `splitB` (area, k=81,L=0.28,A=0.00011), `bridge` (circular, k=210,L=0.33,d=0.008), `drain` (area, k=95,L=0.15,A=0.00018). Connect `hot→feed→` ownerless ideal junction; junction branches through `splitA→core` and `splitB→load`; `core→bridge→load→drain→cold`. Original scalar slots each carry a separate truthful `illustrative` attribution, plus a `@model` adopted-assumption record. A provenance note deliberately contains literal HTML-looking `<img src=x onerror=alert(1)>`; viewer code renders notes via text nodes/`textContent` rather than HTML.
3. **Novel admission: PASS**, using unchanged `create_server`: 9 components, 5 rods, **5 logical nodes including the ownerless junction**, transient mode, and **four `not_computed` requests** (`temperature(core.port)`, `heatFlow(splitB)`, `energyChange(load)`, `temperatureDifference(hot.port,cold.port)`). Actual model SHA-256 `108f542850b91b09138b14e25babfeb81042a0ccf2c566bc3a919a7e61a762a7`; actual study SHA-256 `94df3399f2e74dd612aaefaf5f3e794786f9813e004d621544e27432474abe98`. HTTP JSON exactly equaled the admitted payload and preserved both SHA values, typed source fields, `nativeExecuted=false`, `nativeQualified=false`, `authored_source_only`.
4. **Novel renderer-core transfer: PASS** with unchanged `viewer/source_preview/core.mjs` in Node: `admitPreview` accepted the new in-memory source payload, `layoutNodes` mapped five nodes, `core.m` retained `0.7 kg` source input and `splitB.k` retained `81 W/(m K)`; all four requests remained `not_computed`. This is **not** a successful local Chromium render of the novel network.
5. **Adversarial real HTTP against novel session: PASS** for the intended contract: singular evil/wrong-port Host **421**; absolute URI, encoded traversal, raw `model.mo`, raw `study.json`, invented ZIP route and query-string path **404**; POST/PUT/PATCH/DELETE **405**; HEAD **200 without body**; OPTIONS **501 (no operation)**. Bind address was `127.0.0.1`, `Cache-Control: no-store`, CSP/CORP/nosniff present, and no `Access-Control-Allow-Origin`. Apart from F-01, no forbidden source data was returned.
6. **Pre-socket refusal: PASS** on the novel scratch case. Independently patched the workbench's `ThreadingHTTPServer` constructor to raise if invoked; stale model digest (`identity`), unknown observation (`request`), missing `feed.L` provenance (`provenance`), and a missing rod endpoint after a corresponding model rehash (`connection`) all raised `Refusal` **without touching the server constructor**. Only disposable authored files were rewritten by the reviewer to prepare the separate negative cases; the source checkout was not changed.
7. **Original six published diagnostics: independently replayed all six without native execution.** Downloaded original artifact ZIPs `14152886226`, `14155084346`, `14204656273`, `14215520616`, `14153251022`; executed the unchanged read-only `viewer/network/tools/replay_published_archives.py` against them. D1, D2, DEV_BRIDGE, TEACH_RING4, S1, D2_K2 each returned **`BYTE_IDENTICAL`**, with `nativeExecutedByReplay=false`. My six-row receipt matches the hosted PR artifact receipt exactly. Independently read the six catalog payloads: every one remains `evidenceKind=historical_native_diagnostic`, `nativeQualified=false`, `publicRequestStatus=diagnostic_only`; published catalog SHA-256s match the replay outputs. The TEACH_SPLIT3 source-only fixture separately still has `nativeExecuted=false`, `nativeQualified=false` and four `not_computed` requests. No old C1 80x/100x, seal, or external-author result was requalified or rewritten.
8. **Failed test attempts preserved:** my direct local Chromium run failed at its first `page.goto` with `net::ERR_BLOCKED_BY_ADMINISTRATOR`, before browser assertions. It is **not a local browser pass**; hosted real-HTTP Chromium plus inspected retained screenshots provide the browser evidence. Separately, the initial reviewer-only scratch probe reached a faulty final assertion `any(bool)` and raised `TypeError` **after** its product checks had passed; I corrected only the disposable reviewer harness and reran to completion (PASS). Neither failure was a SIM_HEAT source failure or omitted from this review.

## Separate scope judgments

| Dimension | R1 judgment | Basis / boundary |
|---|---|---|
| Source interpretation fidelity | **PASS for admitted-source representation; source truth UNVERIFIED** | H1 validated exact scratch bytes, inputs, attribution links and logical connections; no independent textbook fact authentication |
| Physical/numerical correctness | **NOT RE-ADJUDICATED** | No physical/numerical code changed; hosted analytical checks passed, but these are not newly measured physics |
| Native simulation / observable coverage | **NOT RUN / NOT EXPANDED** | Fresh network requests remain `not_computed`; archived native results only replayed as published diagnostics |
| Evidence integrity and provenance | **SCOPED PASS** | Pinned tree and 5-file diff, retained exact CI artifact, independent six-case byte-identical replay, correct qualification limits |
| Teacher-facing usefulness | **SCOPED PASS** | Genuine one-command admission/source inspection and novel composition transfer, real hosted standard-case Chromium; no blind teacher trial or novel local browser render |
| Textbook-answer completeness | **NOT APPLICABLE** | This PR adds no numerical answer pathway |

## Release advice / remaining gates

**SCOPED PASS for the declared R1 local-only source workbench**, not a general-purpose HTTP service or validated source-to-simulation pipeline. Recommend a small follow-up regression for duplicate Host headers (F-01) and a one-sentence trusted-local-machine privacy warning (F-02). Neither requires modifying physics, historical frozen evidence, or previous review results. The local Chromium limitation and absence of blind teacher/LLM authoring/native qualification remain explicitly **unknown**, not inferred successes. No R2 escalation is warranted **for this exact five-file diff**; if admission semantics, native controls, physics meanings or evidence-qualification flags change later, reassess risk at R2.

**Leave PR57 draft/unmerged until the owner separately approves.** Do not merge, deploy, run OpenModelica, regenerate historical references, integrate original C1 work, or promote any archived diagnostic to qualified evidence.

*Independence statement:* This is a fresh separate-context Chat B review of pinned source and downloaded execution artifacts. It does not establish independent human adjudication or distinct model weights.
