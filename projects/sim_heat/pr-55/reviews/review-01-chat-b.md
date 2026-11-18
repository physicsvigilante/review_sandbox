# SIM_HEAT PR55 — independent Chat B R2 review 01

## Verdict: CHANGES REQUESTED

The exact candidate preserves the original evidence and correctly keeps the tested public outputs source-only. Its default TEACH_SPLIT3 payload faithfully represents the authored component values, connection graph and four uncomputed requests. However, two independently reproduced defects prevent approval of the claimed generic source-inspection path: a legal component identifier can select the wrong physical component when a graph node is activated, and valid component-level assumption/provenance records are silently discarded. Model-level assumptions are also not exposed in the UI. A smaller imported-metadata consistency gap is recorded separately.

This is **not** a failed native-physics qualification: no new native qualification was attempted or authorized. Keep the source PR draft and unmerged pending corrections, new exact-head CI and a focused re-review.

### Review identity and authority

| Property | Independently reviewed identity |
|---|---|
| Source repository / PR | [physicsvigilante/sim_heat #55](https://github.com/physicsvigilante/sim_heat/pull/55) |
| Base commit | `0278b79b4da1c3196edca7903189713e0482f3f6` |
| Base tree | `c73f86e58be8b9eb55756432aae064f00719487f` |
| **Exact reviewed head** | **`0b15c02e5c3c60af32224e0ec5f29a2920927d5a`** |
| **Exact reviewed tree** | **`1be95f7dc60bd729d691e437c06f7914f0e045e4`** |
| Diff | [One commit; exactly 14 added paths, no modifications/deletions](https://github.com/physicsvigilante/sim_heat/compare/0278b79b4da1c3196edca7903189713e0482f3f6...0b15c02e5c3c60af32224e0ec5f29a2920927d5a) |
| Reviewer | Chat B, separate ChatGPT conversation; GPT-6 Astra Pro |
| Date | 2026-11-18; final evidence checks included 08:21 UTC / 13:51 IST |
| Risk / scope | R2: source interpretation, provenance, source-only requests, imported JSON and asynchronous viewer state |
| Source changes by reviewer | **None.** Only scratch fixtures/test harnesses and this new central review report were authored. |
| CI inspected | Run `44257880331`, job `134643839279`, artifact `14407310945` |

I read the full central request/prompt, PROTOCOL, REVIEW-RISK-POLICY, REVIEW-TEMPLATE, source AGENTS, H1_IMPLEMENTATION_CONTRACT, H1_OFFLINE_AMENDMENT and original C1 FREEZE. Independence here means a separate review context, not proven different model weights, independent human subject-matter adjudication or a blind authoring trial. The developer's prior publication checks were treated as claims to verify, not a reviewer verdict.

## Findings

### F-01 — MAJOR, source fidelity / generic identity: valid component names collide with generated node selection IDs

**Locations:** [app.mjs lines 11–24](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/viewer/source_preview/app.mjs#L11-L24), especially `choose`, `openChoice` and untyped option values; [source_preview.py lines 37–47](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/h1/source_preview.py#L37-L47).

**Reproduction:** In a scratch copy of TEACH_SPLIT3, rename the rod `shortcut` to `node_0` in the model, requests and provenance targets. Recompute only that scratch study's model SHA. Run the unchanged H1 loader and source-preview builder. This is a valid H1 identifier and the actual loader admits the resulting study; it is not merely a forged JSON fixture. Load the generated preview and click, or keyboard-activate, the aluminum graph node.

**Expected:** Inspect the aluminum logical node, its owner and connected ports. A distinct selection of the rod named `node_0` should inspect that rod.

**Observed:** The aluminum graph node and the rod both use selection value `node_0`. `choose` finds the component first. Activating aluminum displays **Component `node_0`, Source kind `RodArea`, A=0.00011 m2, L=0.42 m, k=160 W/(m K)** and rod endpoints. Two picker options have the same value. Thus the selected graph object displays another object's physical source facts.

This was reproduced in the offline Chromium DOM harness at desktop and mobile sizes, first with a consistently renamed preview and then with the actual loader-generated preview. Pointer and Enter-key activation both reproduce it. The retained generated fixture has model SHA `684e63d0aa5191ba284112fe95cfc9d68c5871de84196c88fe42f42a048a8af1` and study SHA `16006bd38ce30626ec55a7d63351ebc8af7fead3403b13d70470e3b3029ad3d8`. These identities describe the scratch reproduction, not the reviewed source or any native record.

**Smallest correction:** Separate selection namespaces, for example `component:<id>` and `node:<id>`, and dispatch by the selected entity type. Preserve public component identities. Do not fix this by banning previously legal names in the frozen H1 parser. Add a regression generated from a genuinely admitted model with component names resembling generated node IDs; exercise graph click, keyboard activation and picker selection.

**Evidence/confidence:** Executed Python admission plus executed Chromium DOM behavior and inspected exact source. High confidence. Local HTTP deployment was blocked as documented below; this finding does not rely on claiming a local HTTP pass.

### F-02 — MAJOR, provenance fidelity: supported component assumptions are dropped; model assumptions are not inspectable

**Locations:** [source_preview.py lines 53–64 and 87–89](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/h1/source_preview.py#L53-L89), [app.mjs lines 11–26](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/viewer/source_preview/app.mjs#L11-L26). The unchanged [study loader](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/h1/study.py#L84-L102) permits provenance targets that are component IDs, in addition to slots, parameters and `@model`.

**Reproduction:** Append this record to a scratch copy of the original study, leaving its physical model and existing slot provenance unchanged:

```json
{"target":"feed","kind":"adopted_assumption","locator":"review/component","note":"R2_COMPONENT_ASSUMPTION: feed lateral heat loss is neglected."}
```

The exact H1 loader admits it. Call `build_source_preview` and search the serialized output for `R2_COMPONENT_ASSUMPTION`.

**Expected:** Preserve the original component-scoped assumption and make it inspectable as such, without falsely attributing it to an individual numeric slot.

**Observed:** The record is absent from the entire output. The builder only retains component records when their target matches a slot or a binding dependency; the component ID itself never enters `affected`. The original study hash is retained, but a hash cannot substitute for the omitted assumption text.

A related presentation omission was also executed: an admitted `@model` assumption with marker `R2_MODEL_REGIME_MARKER` is retained in `modelProvenance` by the builder, but no page text or inspector exposes it. `app.mjs` never renders `modelProvenance`. This matters for inspection of the constant-property, storage-free, maintained-boundary and other authored regime assumptions, even though it does not alter the underlying source model.

**Smallest correction:** Preserve component-scoped records separately from slot/dependency attribution, retaining their original target, kind, locator and note. Render component and model-regime provenance in an appropriate inspection section. Keep repeated original records and chained-parameter attribution intact; do not fabricate per-slot `source_given` records from a component assumption. Add builder and browser regressions covering direct-slot, chained-parameter, component and model targets.

**Evidence/confidence:** Executed exact loader/builder, followed by desktop/mobile DOM inspection of a generated model-regime preview. High confidence. The physical files themselves remain unchanged; the defect is in exported/displayed provenance completeness.

### F-03 — MINOR, imported display-schema consistency: cross-mode and arbitrary provenance-kind metadata are accepted

**Locations:** [core.mjs lines 19–21, 49–65](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/viewer/source_preview/core.mjs#L19-L65).

Changing only the original preview's `mode` to `steady` passes `admitPreview` and renders `TEACH_SPLIT3 · steady composition` despite its three bodies. The actual Python loader refuses the equivalent steady study. Separately, changing a provenance `kind` to `native_qualified` is accepted and the string appears in the inspector; H1 only admits its documented six provenance kinds. Both observations were executed in Node and/or the browser DOM harness.

The important qualification is that the browser is explicitly documented as a **display-schema check, not an authoring validator or origin authenticator**. Its fixed `nativeExecuted=false`, `nativeQualified=false` and `not_computed` fields remain intact in these probes. I am **not** claiming that this creates a native result or bypasses an authenticated-source check. This is a smaller consistency/presentation gap, not the principal reason for the verdict.

**Suggested bounded correction:** Enforce the inexpensive mode/component compatibility and provenance-kind enums already represented in the payload, or make unsupported imported metadata unambiguously distinct from an admitted-H1 claim. Do not add a second physics solver or imply that these checks authenticate source hashes. Add regressions for steady-with-bodies and unknown provenance kinds.

## Portable source-level reproduction of F-01 and F-02

Run this from a checkout of the pinned candidate using its existing checking dependencies. It writes only to a fresh temporary directory, does not invoke OpenModelica or a reference preparer, and retains both source-preview outputs for browser inspection:

```python
from pathlib import Path
import hashlib, json, tempfile
from h1.study import load_study
from h1.source_preview import build_source_preview, serialized

source = Path('h1/cases/TEACH_SPLIT3')
root = Path(tempfile.mkdtemp(prefix='simheat-pr55-r2-'))
model = (source / 'model.mo').read_bytes()
study_text = (source / 'study.json').read_text(encoding='utf-8')

def preview(case_name, model_bytes, doc):
    case = root / case_name
    case.mkdir()
    doc['model']['sha256'] = hashlib.sha256(model_bytes).hexdigest()
    (case / 'model.mo').write_bytes(model_bytes)
    (case / 'study.json').write_text(
        json.dumps(doc, indent=2) + '\n', encoding='utf-8')
    admitted = load_study(case / 'study.json', root)
    assert admitted.request_report['admitted']
    payload = build_source_preview(admitted)
    (root / (case_name + '-preview.json')).write_bytes(serialized(payload))
    return payload

collision = preview('COLLISION', model.replace(b'shortcut', b'node_0'),
                    json.loads(study_text.replace('shortcut', 'node_0')))
assert any(c['id'] == 'node_0' for c in collision['components'])
assert any(n['id'] == 'node_0' and n['owner'] == 'aluminum'
           for n in collision['nodes'])
# Import COLLISION-preview.json, then activate the aluminum graph node.

doc = json.loads(study_text)
doc['provenance'].append({
    'target': 'feed', 'kind': 'adopted_assumption',
    'locator': 'review/component',
    'note': 'R2_COMPONENT_ASSUMPTION: feed lateral heat loss is neglected.'})
provenance = preview('COMPONENT_NOTE', model, doc)
print('component assumption preserved:',
      b'R2_COMPONENT_ASSUMPTION' in serialized(provenance))
# Observed on the reviewed candidate: False. Expected: True.
print('Scratch evidence:', root)
```

## Independent source interpretation and genericity checks

I separately transcribed the task's values and checked all **12 component kinds and 32 typed scalar inputs**, rather than using the saved preview as its own physical oracle. The source study/model SHA-256 values are respectively `d4bb3edd13bf6fe841153a3fcd2c0ac960fa31fa94763d5e14db6d5e99737907` and `549ee4fe6b082f12f51b45c0b3e9da9c963f439c670f5f0411162e329278da4e`. Local regeneration through the exact loader and builder reproduced the published preview bytes.

The model's 13 connection statements produce six logical nodes: aluminum; copper; cold boundary; hot boundary; steel; and the ownerless junction joining `jLeft.port_b` with `jRight.port_a`. Seven rods include the copper–aluminum shortcut and the steel–junction–cold branch. Component ownership, external port identities and authored a/b orientation agree with the task. No node capacity, spatial geometry, real rod pose or measured heat-flow direction was inferred from the graph layout.

| Request | Authored operand(s) | Unit / observed status |
|---|---|---|
| `steel_temperature` | `steel.port` | K / `not_computed` |
| `branch_flow` | `shortcut` | W / `not_computed` |
| `aluminum_energy` | `aluminum` | J / `not_computed` |
| `body_to_cold` | `copper.port`, `sourceCold.port` | K / `not_computed` |

The declared 0..1000 s analysis grid is source metadata, not an executed trajectory. Input temperatures are explicitly source inputs. No private solver, apparatus-specific case dispatch, computed heat flow, energy history or reference-filled public result was found in the new builder/viewer path.

Two independently authored, different supported arrangements were admitted and displayed without editing viewer code: an isolated initialized body with zero rods, and a steady two-boundary/one-rod network using sanctioned length/area/temperature conversions. Desktop/mobile imports had the expected graph/request shapes. I also personally generated previews from the original S1 and D2 studies. S1's separate `source_given` and `unit_convention` conductivity records survived; a new two-level scalar dependency chain retained both original parameter targets and the effective slot attribution, and those records were visible in the browser.

This demonstrates useful generic machinery, not universal graph/UI qualification. F-01 and F-02 are counterexamples within the already supported domain. TEACH_SPLIT3 remains developer-authored and illustrative, **not** a held-out teacher exercise, textbook qualification or classroom study. The TASK heading's use of “independent” does not override that explicit disclosure.

## Executed local evidence versus inspected hosted evidence

### Personally executed

I used Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, Node 22.16.0, installed Playwright 1.57.0 and installed Chromium. No dependency installation or native operation was performed for this review.

The independent Python adversarial script recorded 28 assertions: 27 matched the expected behavior and one exposed the component-provenance loss. It covered the source values/topology/request mapping, byte-identical preview generation, actual admission of the collision case, chained attribution, second supported topologies, and refusals for stale hashes, missing/mismatched attribution, unknown provenance kinds, wrong quantity types, nonpositive inputs, extra study/physical fields, boolean intervals and invalid/duplicate requests. CLI probes verified that refusal preserves an existing output sentinel and that writing inside the authored case root is refused without changing the model.

The independent Node probes checked qualification/status promotion, fabricated results, wrong units, boolean/nonfinite/nonpositive inputs, missing provenance and incompatible attribution. These protections passed. Cross-mode and arbitrary-kind mutations produced the F-03 observations. Exact repeated provenance records are accepted, consistently with the current H1 loader; distinct legitimate records also remain preserved. Changing a syntactically valid hash, or claiming an otherwise unavailable bare parameter target in imported metadata, is not authenticated by this display format. I recorded that documented limitation rather than misreporting an authentication bypass.

Executed Chromium DOM tests at 1440x950 and 390x844 confirmed source-only labels, four uncomputed default requests, source-value inspection, inert rendering of an HTML/event-handler string in a note, and complete refusal clearing of graph, requests, details, identity and selection. There is no source-result history to retain. Controlled promises exercised **both completion orders** for each pair: old-valid/new-invalid, and old-invalid/new-valid. The newest selection won all four combinations at both viewport sizes. Successful DOM runs recorded zero JavaScript page errors. The initial default-fetch version guard was inspected in source; I do not claim a separately executed delayed-default-fetch test.

**Browser execution limit:** Actual localhost HTTP navigation was attempted and failed with `net::ERR_BLOCKED_BY_ADMINISTRATOR`. The later local checks used a separately labelled offline DOM harness: exact HTML with its external script tag removed, the default JSON fetch stubbed, and exact core/app code joined at the static import boundary. Production function bodies were unchanged. This is real Chromium DOM execution, **not** a local HTTP, module-loading or deployment pass. Hosted real-HTTP evidence below supplies separate coverage.

### Exact-head hosted CI independently inspected

I verified GitHub's run and job metadata, downloaded and examined [run 44257880331](https://github.com/physicsvigilante/sim_heat/actions/runs/44257880331), job `134643839279`, and [artifact 14407310945](https://github.com/physicsvigilante/sim_heat/actions/runs/44257880331/artifacts/14407310945). It is a successful **push run at the exact reviewed head/tree**, not a substituted PR merge-ref run.

The downloaded ZIP is **7,438,185 bytes**, SHA-256 **`ab328892f0c5796987e091e447c1d1fb78732c7bb6c70f6378ab409aed9ed1b2`**, with **44 unique entries and no CRC failure**. Head/tree receipts and the 14-addition diff agree with GitHub. I inspected all suite summaries: H1 152 pass; arithmetic 4 pass; adapter 62 pass plus one optional skip; product/source-preview 19 pass; Node 39 pass. Total **276 passes, one optional skip**. These are inspected hosted executions, not 276 newly executed reviewer tests, and must not be added to overlapping developer/local totals.

The workflow has failure-propagating shell settings, an exact added-path guard, protected-source comparison, byte comparisons for source preview and saved comparison, the original-archive replay and actual-HTTP Chromium steps. Its commands do not install/query/build/launch OpenModelica or regenerate an adopted physical reference. The original explorer, product-entry and new source-preview browser logs report success, including default source-only visibility, secondary D2 topology, refusal clearing and import races. I visually inspected the hosted default source screenshot and local collision evidence. Hosted HTTP logs contain `/favicon.ico` 404s; **zero page errors does not mean zero HTTP errors**.

Green CI does not cover the valid-identifier collision or component-provenance preservation counterexamples and therefore does not resolve F-01/F-02.

## Exact identity and original evidence preservation

GitHub's commit object independently confirms the requested tree and single parent. The complete base snapshot was recovered from the **baseline**, not candidate, artifact `14401083576` referenced by PR54's CI. That ZIP independently matched 7,815,278 bytes, SHA-256 `c4ffaf855f28dad9535cae2a0036d24027035cecc70bc2ef043b8714556cddfb`, 38 unique CRC-valid members and an empty baseline diff. Its actual source tree reconstructed locally to `c73f86e58be8b9eb55756432aae064f00719487f`.

Starting from that verified base, an index containing the 14 published added-file blob identities reconstructed the exact candidate tree `1be95f7dc60bd729d691e437c06f7914f0e045e4`. This is a tree-identity check, not a claim that every added file was materialized locally. All 14 files were read through pinned GitHub access; the seven added files used by the local functional probes and the unchanged model/study/policy dependency modules were separately materialized and matched to Git blob hashes before execution.

The all-additions diff excludes changes to the physical library, original cases, numerical policy, reference/checker, native runner, existing explorer, qualification and historical C1 evidence. I independently rehashed all six original saved bundles against their catalog and inspected their unchanged `diagnostic_only` / `nativeQualified=false` source metadata:

| Original bundle | SHA-256 |
|---|---|
| D1 | `49c605d5a23da7d521da6c8db186dbd2d435facb60c31289822322e20a6dfebf` |
| D2 | `c0fc143db30278898d13340faa7f60baf62185b40296767a6114e359d3c705ea` |
| DEV_BRIDGE | `07dbe0987b99c89d9a20f0a1317b3699cddbf85186dcee3ae71d6d0005c364d8` |
| TEACH_RING4 | `b4f46b2953409980ea5d5ed1b41cafaf5a7504003da44038d9d51286bb6e8a34` |
| S1 | `eacab37b499a47c094cbd642acfee269a1bea7c82d16b15b9217a8c13ef1e4e7` |
| D2_K2 | `a057e076aa31971c82509b70566892f9be60850046231104feac5d9e6365748b` |

The hosted archive replay records all six as `BYTE_IDENTICAL` with `nativeExecutedByReplay=false`; I inspected these receipts rather than claiming to have personally rerun the five original archive ZIPs. I personally compared the hosted saved-comparison replay with the original base `compare_index.json`: byte-identical. Regenerating the new source-only TEACH_SPLIT3 JSON is a different check, not an original native archive replay.

All 14 additions were inspected: the workflow; admitted-source documentation; task; TEACH_SPLIT3 model/study; builder; Python source and browser tests; viewer README, HTML, app, core, Node tests and saved JSON. No source correction was applied by Chat B.

PR54 was independently checked as **open, draft, unmerged**, on separate head `8f6ef1d0f8d0ebd938620c5694bc11856a5c9e7e`. Its candidate changes are not included in this one-parent PR55 diff. PR55 was rechecked before report publication and still points to the reviewed head as an open, unmerged draft.

## First failures, retained evidence and limits

The first local clone failed because `github.com` could not be resolved. Connector reads and downloaded artifacts supplied source access; no successful local clone is claimed. Connector-text copies were reconciled to exact blob bytes before execution, including end-of-file newline differences; this was acquisition normalization, not a production repair.

The first actual local browser navigation failed under environment policy and remains failed. The first offline DOM harness passed its initial source/refusal/race checks, then encountered a **reviewer harness error**: a bare assignment expression returning `File.prototype.text` from `page.evaluate` led to `Illegal invocation`. A separately saved v2 harness changed only that cleanup expression to an arrow-function block. The first log/results were retained, not rewritten as a pass. Subsequent defect reproductions remain failed expectations, not newly accepted production behavior. The developer's earlier reported blocked local navigation is likewise not reclassified by hosted success.

An evidence package is supplied with this review conversation: `sim_heat_pr55_chat_b_evidence.zip`, **12,011,810 bytes**, SHA-256 **`fa4337028bf13730c53ce316822a80563550663bcb71425bbb2917d53082fc52`**. It contains the hash-verified local source copies, independent scripts/scratch inputs, first-failure and successor logs, generated source-only payloads, screenshots, inspected CI files and a per-file manifest. It is supplemental; the pinned source links and reproduction above suffice to reproduce the main findings. Local absolute harness paths are documented in its README.

No full native result validation, independent transient numerical reference, teacher classroom trial, exhaustive browser accessibility audit or textbook-answer qualification was performed. No local full-suite or original-archive replay is asserted beyond the explicitly described executions.

## Separate scope judgments

| Dimension | Judgment | Basis |
|---|---|---|
| Source interpretation fidelity | **FAIL for generic approval; default case passes** | Exact default values/topology/requests verified; F-01 displays another object's facts and F-02 loses valid assumptions. |
| Physical/numerical correctness | **Source checks pass; numerical behavior UNKNOWN** | No new physical law or computed trajectory in this slice. Authored slots/connectivity checked; no new native/reference comparison performed. |
| Native simulation and observable coverage | **UNKNOWN / not qualified for TEACH_SPLIT3** | All four public requests remain uncomputed. Six original bundles remain historical diagnostics, not promoted acceptance. |
| Evidence integrity and provenance | **Preservation PASS; preview completeness FAIL** | Exact identities, artifact integrity and original bytes verified; component/model assumption handling needs correction. |
| Teacher-facing usefulness | **PARTIAL; not ready for generic sign-off** | Useful source-only inspection and second-model support, but misleading selection and hidden assumptions need repair. Classroom effectiveness is untested. |
| Textbook-answer completeness | **Not claimed / not assessed** | Developer-authored illustrative task; no numerical answer or blind textbook interpretation qualification. |

## Release advice and smallest next gate

Correct F-01 and F-02 in a **new source commit**, add direct regressions from valid admitted studies, and explicitly disposition F-03. Keep the existing parser, physical laws, original cases, frozen references and historical C1 records unchanged unless a separately justified scope requires otherwise. Run exact-new-head CI with the six original archived replays and actual-HTTP Chromium coverage, including the new selection/provenance regressions and existing refusal/race controls. A focused re-review of those corrections is sufficient unless the implementation expands physical/evidence semantics.

This report does not authorize merging, deployment, OpenModelica operations, native runner use, reference regeneration, historical C1 integration or diagnostic-to-qualified promotion. Owner approval remains a separate gate, even after a future scoped pass. PR54 remains separate and unmerged.
