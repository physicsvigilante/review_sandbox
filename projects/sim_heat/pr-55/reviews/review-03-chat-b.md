# SIM_HEAT PR #55 — independent Chat B R2 review 03

**Verdict: CHANGES REQUESTED** (source-preview R2; no native or merge approval).

The pinned default TEACH_SPLIT3 source preview accurately carries its declared physical inputs, connection graph, source identities, and four `not_computed` requests. Exact-head source-preview CI passed and the original diagnostic archives have unchanged recorded bytes. However, a valid-looking component/node identifier collision misidentifies selected physical facts in the browser, and the preview builder discards permitted component-level provenance. Model-level regime assumptions are retained as JSON but never shown. These are significant defects for a **generic teacher-facing authored-source inspector**, notwithstanding the successful existing tests.

This is a *second independently executed review*, not a rewrite or adoption of earlier reviewer reports. The requested `review-01-chat-b.md` and `review-02-chat-b.md` already existed when publication was attempted. Per [PROTOCOL.md](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md), prior reports were **not overwritten**; this is the new uniquely named `review-03-chat-b.md`.

## Pinned identity, scope and authority

| Item | Independently checked |
|---|---|
| Source PR | [physicsvigilante/sim_heat #55](https://github.com/physicsvigilante/sim_heat/pull/55), open draft, unmerged when checked |
| Base | `0278b79b4da1c3196edca7903189713e0482f3f6` |
| **Exact head** | **`0b15c02e5c3c60af32224e0ec5f29a2920927d5a`** |
| **Git tree** | **`1be95f7dc60bd729d691e437c06f7914f0e045e4`** |
| Parent/tree verification | Direct GitHub Git-commit API response: exactly that tree and exactly that base parent |
| Changed paths | [Base-to-head comparison](https://github.com/physicsvigilante/sim_heat/compare/0278b79b4da1c3196edca7903189713e0482f3f6...0b15c02e5c3c60af32224e0ec5f29a2920927d5a): **14 additions, zero modifications/deletions** |
| Risk | R2 — source interpretation, provenance/evidence, imported JSON, viewer concurrency |
| Reviewer/date | Chat B, distinct ChatGPT conversation, GPT-6; 2026-11-18 UTC. Independence is context separation, not verified different model weights or human adjudication |
| Source edits | **None.** Local scratch copies and probes only. No source PR, frozen reference, historical C1, or other review report modified |
| Exact-head hosted CI | [run 44257880331](https://github.com/physicsvigilante/sim_heat/actions/runs/44257880331), successful *push* run, job `134643839279`, [artifact 14407310945](https://github.com/physicsvigilante/sim_heat/actions/runs/44257880331/artifacts/14407310945) |
| Separate PR54 | [PR #54](https://github.com/physicsvigilante/sim_heat/pull/54) remains open, draft, unmerged; head `8f6ef1d0f8d0ebd938620c5694bc11856a5c9e7e`, not incorporated here |

Read the complete central REQUEST and reviewer prompt, PROTOCOL, REVIEW-RISK-POLICY, REVIEW-TEMPLATE, `AGENTS.md`, `docs/H1_IMPLEMENTATION_CONTRACT.md`, `docs/H1_OFFLINE_AMENDMENT.md`, and `qualification/h1_c1/FREEZE.md`; inspected all 14 additions at the pinned ref, plus H1's unchanged source/provenance admission paths. Do not interpret this report as a fresh H1 native, C1, or teacher qualification.

## Findings

### F-01 — MAJOR / source-selection fidelity: component IDs collide with generated graph node IDs

**Source:** [`h1/source_preview.py:37-47`](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/h1/source_preview.py#L37-L47); [`viewer/source_preview/app.mjs:11-24`](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/viewer/source_preview/app.mjs#L11-L24).

**Reproduction:** Rename the default case's rod `shortcut` to `node_0`, consistently updating that identifier's ports, requests and provenance; in a model/study test also recompute the scratch model hash. `node_0` is a legal public Modelica component name under the unchanged `h1/model.py` identifier/RESERVED rules. Its separate generated node `node_0` is the aluminum node. The resulting structurally consistent preview passes the **unchanged, exact-blob** `admitPreview`. In independently executed Chromium DOM at **1440×950 and 390×844**, activating the graph control labelled **“Inspect source node aluminum”** by pointer or Enter selects the **RodArea component `node_0`**, showing `A=0.00011 m2`, `L=0.42 m`, `k=160 W/(m K)`, rather than the aluminum node's role, owner and incident ports. The picker contains two `value="node_0"` options. Thus another object's authored physical facts are presented as the selected graph object.

**Expected:** The node and rod remain independently selectable and show their respective source identities. **Observed:** A shared untyped selection key makes `choose()` prefer the component. This is a browser DOM reproduction using an imported, structurally admitted altered preview; I did **not** run the full Python H1 loader on this altered scratch model. The unchanged H1 syntax and validator logic independently establish why such a component name is admitted. Confidence: high.

**Smallest correction:** Namespace selection keys (`component:<id>`, `node:<id>`) or pass typed selection objects; never prohibit formerly legal H1 names to hide a viewer bug. Add an actual `load_study`→preview→Chromium regression for a rod named `node_0`, including pointer, keyboard and picker selection. Do not change the underlying physics graph.

### F-02 — MAJOR / provenance fidelity: admitted component-level records are omitted; model assumptions are hidden

**Source:** [`h1/study.py:84-100`](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/h1/study.py#L84-L100); [`h1/source_preview.py:53-64,87-89`](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/h1/source_preview.py#L53-L89); [`app.mjs:11-26`](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/viewer/source_preview/app.mjs#L11-L26).

The unchanged H1 `check_provenance` explicitly admits any existing component ID as an original record target. For an independently authored additional assumption record, e.g.:

```json
{"target":"feed","kind":"adopted_assumption","locator":"review/component","note":"Feed heat loss neglected for this model"}
```

the builder's `affected` list contains **only** exact numeric field targets (`feed.k`/`feed.L`/`feed.d`) and dependent bound-parameter names; the permitted bare component target `feed` never qualifies and is silently lost from the source-preview output. No extra-component provenance field exists to retain it. This is a high-confidence **source-logic finding**, not a claimed independent end-to-end `load_study` execution. The retained study hash cannot replace missing content.

Separately, source `modelProvenance` records are exported but not rendered by the page. I inserted a distinct model-regime marker into an admitted-shape imported source payload and executed Chromium DOM tests at both viewports: the source is accepted, but its model assumption is absent from all visible page/inspector text. **Observed in the browser.**

**Expected:** Preserve original record target/kind/locator/note and show valid **component** and **@model** assumptions as such; do not mislabel them as per-slot source facts. **Smallest correction:** Add typed, separately presented component provenance and a model-regime section; keep the existing many-to-one parameter/slot attribution and repeated original records. New regressions should use the real H1 loader for direct-slot, scalar-chain, component, and model targets and assert both emitted JSON and inspector visibility.

### F-03 — MINOR / untrusted JSON display consistency: mode and provenance enums are weak

**Source:** [`viewer/source_preview/core.mjs:19-21,48-65`](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/viewer/source_preview/core.mjs#L19-L65).

My independent Node probes changed the default preview to `mode="steady"` while retaining its three bodies: `admitPreview` **accepts** and labels this as steady, although the H1 study loader refuses bodies in steady mode. A separately mutated `sourceProvenance[0].kind="native_qualified"` is also accepted as arbitrary nonempty text despite H1's six-kind enum. These are potential misleading source-status labels, **not** actual solver or qualification promotions: the preview still refuses `nativeExecuted=true`, `nativeQualified=true`, `publicRequestStatus="diagnostic_only"`, and computed requests. The browser intentionally does not authenticate independently uploaded source or re-run H1 parsing.

**Correction/disposition:** Either enforce the cheap H1 mode/topology and provenance-kind invariants on imported display data, or visibly distinguish untrusted display-only metadata from H1-admitted source assertions. Test both changes without inventing a second physics solver.

### F-04 — INFORMATIONAL / other inherited workflow is red on a PR merge ref

The dedicated **exact-head push** source-preview workflow is green. A separate [product-entry workflow run 44258286511](https://github.com/physicsvigilante/sim_heat/actions/runs/44258286511) on the **PR merge ref** `c15c2598e6968996507b7e69f89c399fb6392d5a` failed because its candidate job applies `git diff --exit-code 4162c3d... HEAD -- h1 experiments qualification viewer`: this PR *intentionally adds* `h1`/`experiments`/`viewer` files, so that workflow's unchanged-postmerge scope guard exits 1 **before** its suites. Its fixed `postmerge-baseline` matrix leg passed. Do not describe **all** workflows on PR55 as green, nor confuse this guard with a source-preview test failure. Owner can explicitly disposition the unrelated guard/trigger separately; it does not negate the pinned source-preview CI success.

## Independent tests and hosted evidence (strictly separated)

### Personally executed, no OpenModelica

1. Downloaded the complete [exact-head source-preview artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44257880331/artifacts/14407310945) and independently checked **7,438,185 bytes**, **SHA-256 `ab328892f0c5796987e091e447c1d1fb78732c7bb6c70f6378ab409aed9ed1b2`**, **44 unique ZIP members and no bad CRC**. Its `head-sha.txt`, `head-tree.txt`, and `source-diff.txt` agree with the API and the 14-addition-only change.
2. Reconstructed **exact Git blobs** for `core.mjs` (`e485427cd97cc29469c2e551a07d4dfe8550dc52`), `app.mjs` (`c6bb32c0b333f37d8bbdea3262067c89c35f029a`), original `model.mo` (`13a62a86dd19f932505435000e69f62dba2ee840`), and source JSON (`3df3c880e7252d37956162b49970d0073b247eed`). No source code changes were used in the probes.
3. A separately coded oracle compared the **12 component identities/types and 32 SI source inputs** against the TEACH_SPLIT3 task and exact authored model. Independently unioned the **13 authored connect statements** into the same **six logical nodes** (three bodies, two maintained boundaries, one ownerless junction `jLeft.port_b`–`jRight.port_a`). Checked all seven authored rod endpoint orientations, the copper–aluminum shortcut, four operation/target/unit mappings, and **four `not_computed` statuses**. No predicted temperatures, powers, histories, rod geometry, or computed native values occur in the source payload.
4. Executed 19 independent Node admissions/refusals against the **exact original `core.mjs`** and saved source JSON: normal source, forged native flags, `diagnostic_only`, computed requests, extra results, unknown ports, bad requests, missing provenance, typed-unit mistakes, boolean/zero/infinite inputs; these refusals passed. Repeated valid attribution records remain accepted. The same probes observed F-01's identity collision and F-03's cross-mode/kind acceptance.
5. Chromium DOM at 1440×950 and 390×844 executed the original **byte-verified core/app functions** and imported source JSON. Default four-request display, native forgery refusal with complete prior graph/requests/details/identity/selection clearing, **both** old-valid/new-invalid and old-invalid/new-valid delayed import completion orderings all passed; no JS page errors. Independently reproduced F-01 pointer/Enter misselection, duplicate picker values, and F-02 hidden model assumption. An additional **H1-supported-shape**, isolated single-body preview displayed without changing viewer code; HTML/event-handler text in a provenance note remained inert text. This local alternative was **not** authenticated through an actual H1 loader; hosted CI separately exercises genuine D2.
6. **First local browser attempt failed:** actual localhost `page.goto` returned `net::ERR_BLOCKED_BY_ADMINISTRATOR`. That log was retained. The successful local follow-up was an **offline DOM harness**, using a minimal HTML DOM, stubbed default JSON fetch, and a classic-script wrapper at the ES-module import/top-level-await boundary; core/app function bodies were unchanged and original blob identities checked. **Do not call the local probe an actual HTTP/site-deployment PASS.** The hosted CI run below is separately real HTTP.

### Inspected hosted CI, not personally re-executed

- [Run 44257880331](https://github.com/physicsvigilante/sim_heat/actions/runs/44257880331) shows exact pinned SHA, a successful job with fail-fast shell and strict allowed diff guard, protected-path diff, existing comparison `cmp`, new source-only preview `cmp`, original-archive read-only replay, and real-HTTP Chromium checks.
- Log summaries/artifact: H1 **152 pass**; analytical **4 pass**; adapter **62 pass and one optional skip**; product **19 pass**; Node **39 pass** = **276 passes, one optional skip**. These are *hosted* passes, not another 276 tests independently run here. Real HTTP Chromium source-only, existing explorer and product-entry browser logs say PASS; the source server log also has a nonblocking `/favicon.ico` **404**, so “no page errors” is not “zero HTTP errors.”
- The downloaded `archive-replay.json` names **all six originals** as `BYTE_IDENTICAL` with `nativeExecutedByReplay=false`: D1 `49c605d5...`; D2 `c0fc143d...`; DEV_BRIDGE `07dbe098...`; TEACH_RING4 `b4f46b29...`; S1 `eacab37b...`; D2_K2 `a057e076...`. The existing compare-index rebuild passed byte comparison. This is **inspected hosted archive replay evidence**, not a claim that I separately downloaded and rehashed the five historical artifact archives or invoked their native executables. The 14-addition diff independently establishes that the existing catalog, diagnostic bundles, frozen references, physical library, runner and C1 files were not modified in this PR.
- Source-only TEACH_SPLIT3 regeneration and its comparison to saved JSON passed at exact head. A source-only replay is not a new native archive replay or numerical/reference qualification.
- I did **not** execute the full H1 loader, original six archive replays, numerical reference preparation, physical runtime, native runner, or OpenModelica. No installed dependencies, source commits, or historical records were changed.

## Separate judgments

| Dimension | Assessment | Reason |
|---|---|---|
| Source interpretation fidelity | **Default PASS; generic inspector FAIL** | Default source values/topology/requests match, but F-01 selects another object's physical facts and F-02 loses legal assumption records |
| Physical/numerical correctness | **Source physical contract consistent; native numerical behavior UNKNOWN** | H1 components/ports and units inspected; no new trajectory/reference or native run |
| Native simulation and observation coverage | **NOT QUALIFIED / UNKNOWN** | All four requests correctly `not_computed`; diagnostic archives remain `nativeQualified=false` |
| Evidence integrity / provenance | **Historical preservation PASS; provenance presentation FAIL** | Verified tree, CI artifact digest/CRC and unchanged archives by hosted replay; F-02 omission |
| Teacher-facing usefulness | **PARTIAL** | Helpful topology/source-only inspection, but misleading selection and hidden assumptions prevent generic sign-off |
| Textbook answer completeness / blind authoring | **NOT CLAIMED** | Developer-authored illustrative TEACH_SPLIT3; not a held-out teacher, textbook, or classroom validation |

## Smallest correction and next gate

Keep **PR55 draft/unmerged**, PR54 separate. Fix F-01 and F-02 in **a new source SHA** with admitted-model plus desktop/mobile selection and provenance regressions; explicitly decide F-03. Repeat exact-new-head source CI, original six archive-preservation checks, and real-HTTP Chromium refusal/race tests. Perform a **targeted independent re-review** against the new commit; do not relabel this old-sha report. There is **no authorization** here for a source merge, deployment, OpenModelica version query/install/build/launch, native operation, C1 integration, frozen/adopted reference regeneration, or promotion of `diagnostic_only/nativeQualified=false` data.
