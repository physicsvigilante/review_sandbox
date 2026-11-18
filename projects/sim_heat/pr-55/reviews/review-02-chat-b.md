# SIM_HEAT PR #55 — additional independent Chat B R2 review (02)

## Outcome: **CHANGES REQUESTED** — source-preview scope only

This separately authored review is pinned to **source HEAD `0b15c02e5c3c60af32224e0ec5f29a2920927d5a`**, **Git tree `1be95f7dc60bd729d691e437c06f7914f0e045e4`**, and the one-commit base `0278b79b4da1c3196edca7903189713e0482f3f6`. It does not evaluate a floating branch. The candidate safely labels its default public requests `not_computed`, leaves the original C1 evidence untouched, and has successful exact-head CI. However, an accepted component identifier can collide with the viewer's generated node identity and show the wrong physical source component on selection. The preview builder also omits valid component-scoped provenance, while the viewer hides retained model-regime provenance. These are significant fidelity defects in a *generic source-inspection* feature, regardless of green CI.

**Why report 02?** `reviews/review-01-chat-b.md` was already committed before this review began. The central protocol prohibits overwriting any prior independent report. This is a separate, newly authored report; report 01 was neither replaced nor reattributed.

| Property | Independently checked identity |
|---|---|
| Source PR | [physicsvigilante/sim_heat #55](https://github.com/physicsvigilante/sim_heat/pull/55) (draft) |
| Base SHA / tree | `0278b79b4da1c3196edca7903189713e0482f3f6` / `c73f86e58be8b9eb55756432aae064f00719487f` |
| **HEAD / tree** | **`0b15c02e5c3c60af32224e0ec5f29a2920927d5a` / `1be95f7dc60bd729d691e437c06f7914f0e045e4`** |
| Base-to-head diff | [Exactly 14 additions; zero modifications/deletions](https://github.com/physicsvigilante/sim_heat/compare/0278b79b4da1c3196edca7903189713e0482f3f6...0b15c02e5c3c60af32224e0ec5f29a2920927d5a), one commit, single base parent |
| Reviewer / date | Chat B, separate GPT-6 ChatGPT conversation; 2026-11-18, approximately 08:37 UTC / 14:07 IST |
| Risk | R2: source interpretation, provenance, untrusted JSON, async UI state and evidence boundaries |
| Mutations performed | **None** to `sim_heat`, original artifacts, C1, PR54 or preexisting central reports. Only local scratch code/fixtures and this new central review file. |
| CI | [Push run 44257880331](https://github.com/physicsvigilante/sim_heat/actions/runs/44257880331), job `134643839279`, [artifact 14407310945](https://github.com/physicsvigilante/sim_heat/actions/runs/44257880331/artifacts/14407310945) |

Required reading was inspected: central REQUEST, REVIEWER-PROMPT-01, PROTOCOL, REVIEW-RISK-POLICY, REVIEW-TEMPLATE; source AGENTS.md, H1_IMPLEMENTATION_CONTRACT, H1_OFFLINE_AMENDMENT and historical C1 FREEZE. All 14 added files were read or inspected against exact-head content and the downloaded artifact. Independence means separate conversational evaluation, not a distinct human expert or a blind held-out teacher qualification.

## Findings and minimal corrections

### F-01 — MAJOR: supported component name is confused with a generated node ID

**Source:** [`viewer/source_preview/app.mjs` lines 11–24](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/viewer/source_preview/app.mjs#L11-L24), [`h1/source_preview.py` lines 37–47](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/h1/source_preview.py#L37-L47), unchanged H1 model identifier rule.

**Independent reproduction:** Start with the source-only TEACH_SPLIT3 preview; consistently rename the legal RodArea component `shortcut` to `node_0` in component ID, ports, rod, provenance targets and public request. The H1 parser's regular expression and reserved-word set permit `node_0`. The exact source-preview builder assigns `node_0` to the aluminum logical node. The exact browser schema validator **accepted** the consistently renamed payload.

In Chromium using exact-hash `app.mjs` and `core.mjs` in an offline DOM harness, activating the **aluminum node** by pointer or keyboard displayed **Component node_0 / RodArea / A=0.00011 m2 / L=0.42 m / k=160 W/(m K)**, not the aluminum node's owner/ports. Both desktop (1440×950) and mobile (390×844) reproduced it, and the picker contained **two options with the same value `node_0`**. In `choose`, component lookup precedes node lookup, while both share the same untyped selection namespace.

**Expected:** node selection inspects the node/owner/connected ports; component selection inspects the rod. **Observed:** a valid name collision substitutes physical source facts for the requested graph object. The scratch renamed JSON was verified for display-schema consistency; this reviewer did not rerun the whole H1 loader for the renamed Modelica model, so actual source admission rests on the inspected unchanged identifier/parser rules, not a claimed local Python execution.

**Smallest correction:** tag selection values by entity type (`component:<id>` vs `node:<id>`), dispatch on type, and add pointer/keyboard/picker regressions using a model with a legitimately admissible node-like component name. Do **not** narrow the frozen H1 grammar merely to avoid a UI namespace collision.

### F-02 — MAJOR: valid component-scoped provenance is dropped; model assumptions not shown

**Source:** [`h1/source_preview.py` lines 53–64 and 87–89](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/h1/source_preview.py#L53-L89), [`h1/study.py` `check_provenance`](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/h1/study.py#L84-L104), [`app.mjs` source inspector](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/viewer/source_preview/app.mjs#L11-L26).

**Reproduction from exact source:** The unchanged H1 loader explicitly allows provenance targets belonging to `set(model.components)`. Add to a scratch TEACH_SPLIT3 study the otherwise valid record:
```json
{"target":"feed","kind":"adopted_assumption","locator":"r2/component","note":"Assume lateral feed losses negligible."}
```
Existing direct slot attributions remain in place. `build_source_preview` copies a component record *only* if its target equals a specific effective slot (`feed.k` etc.) or belongs to that slot's scalar-parameter dependency chain. Target `feed` satisfies neither predicate, so the record is absent from the component payload and from `modelProvenance`. This is a deterministic source-level finding, not an assertion of a personally run loader reproduction.

Separately, the original authentic saved JSON contains an `@model` adopted-assumption record. The builder retains it in `modelProvenance`, but `app.mjs` never renders that array. I injected a distinctive model-regime note into an otherwise valid source-only payload and imported it into the same exact-code DOM harness; the marker was not present anywhere in the rendered page on either viewport.

**Expected:** preserve and inspect component-level and model-level assumptions, separately from field-specific attribution, while retaining repeated field/dependency records. **Observed:** component assumptions lost from the exported description; model assumptions not inspectable in the UI.

**Smallest correction:** export original component-target records under a component-level provenance collection and render both that collection and model-regime records. Do not falsely rewrite whole-component assumptions as slot source-givens. Add direct-slot, parameter-chain, component-target and `@model` browser/builder regression coverage, including multiple records for one source slot.

### F-03 — MINOR: imported display metadata needlessly accepts H1-inconsistent claims

**Source:** [`viewer/source_preview/core.mjs` lines 19–21, 49–65](https://github.com/physicsvigilante/sim_heat/blob/0b15c02e5c3c60af32224e0ec5f29a2920927d5a/viewer/source_preview/core.mjs#L19-L65).

**Personally executed Node probes:** Mutating TEACH_SPLIT3's `mode` to `steady` while retaining three Body instances was accepted and could be presented as a steady composition. Changing an original provenance `kind` to `native_qualified` was also accepted. The H1 loader's supported provenance-kind set excludes that string, and steady topology with Bodies is outside H1 admission. This is a **display-schema consistency issue**, not proof of a forged native result: the same validator still enforces `nativeExecuted=false`, `nativeQualified=false`, `sourceFidelityQualified=false`, and `not_computed` for all public requests.

**Smallest correction:** check supported H1 mode/component compatibility and provenance-kind enums, or explicitly label unauthenticated imported metadata without suggesting loader admission. Do not misrepresent source-preview JSON validation as host/source signature verification. A syntactically valid but forged model/study hash was also accepted by design; this is the documented origin-authentication limitation, **not** an undisclosed exploit.

## Separate evidence categories — what I actually ran vs inspected

### Personally executed / observed

1. **Downloaded exact CI artifact** through GitHub, independently hashed the local ZIP: **7,438,185 bytes**, SHA-256 `ab328892f0c5796987e091e447c1d1fb78732c7bb6c70f6378ab409aed9ed1b2`; 44 unique entries; all CRCs valid. `head-sha.txt`, `head-tree.txt` and `source-diff.txt` match GitHub commit/tree/diff.
2. Compared the downloaded CI `preview-replayed.json`'s **Git blob SHA-1 `3df3c880e7252d37956162b49970d0073b247eed`** against the exact-head GitHub blob SHA for `viewer/source_preview/data/TEACH_SPLIT3.json`: **identical bytes**. This verifies saved preview identity, distinct from native archive replay.
3. Reconstructed **unchanged exact JS bytes** into a local scratch test directory; `git hash-object` matched GitHub's source blobs: `core.mjs` = `e485427cd97cc29469c2e551a07d4dfe8550dc52`; `app.mjs` = `c6bb32c0b333f37d8bbdea3262067c89c35f029a`. The local HTML was a **minimal scratch DOM**, not the original hosted index; the code functions and CI preview JSON were exact.
4. Ran local **Node source-display probes** against that exact `core.mjs`: the original and a *synthetic* two-fixed-boundary/one-rod steady topology passed structural display validation. Forged native flags, computed request status, injected results, diagnostic promotion, missing provenance, wrong SI unit/type, boolean/nonpositive values, extra fields, dangling ports/rods and invalid request targets were refused. The synthetic second topology was **not independently admitted with H1 Python**; hosted CI separately exercises genuinely admitted D2 and S1.
5. **Browser first attempt:** local actual-HTTP Chromium navigation to a scratch localhost server failed with `net::ERR_BLOCKED_BY_ADMINISTRATOR`. Preserved as a failed navigation attempt; **not** recast as a local HTTP pass.
6. Ran an **offline Chromium DOM harness** loading the exact hashed app/core JS against a minimal HTML DOM and stubbed initial JSON fetch. Desktop and mobile both displayed the authentic CI preview with 13 interactive graph elements, four `not_computed` requests and false native flags. The F-01 collision and model-assumption omission reproduced; refusal cleared graph, requests, identity, selection and inspector. **Eight asynchronous race trials passed**: old-valid/new-invalid and old-invalid/new-valid, each with *old read last* and *new read last*, on both viewports. No JS page errors in this separate DOM harness. This is **not** a real HTTP/module-loading pass.
7. Independently tabulated the exact saved preview: **12 source components, 32 typed scalar inputs**, three Body heat capacities (154, 441, 630 J/K), seven positive rod conductances (each `kA/L`, circular `A=πd²/4`), six logical nodes, one ownerless junction, seven rods and four requests. Those hand arithmetic checks concern source-domain plausibility; they are **not native simulated temperatures, powers, energies or trajectories**.
8. Personally inspected the CI's saved full-page source browser screenshot: the graph is explicitly schematic and sometimes line-crossing, with separate source input cards, four uncomputed observations and native qualification shown as false. No physical apparatus geometry can be inferred from placement.

### Inspected hosted CI, not personally rerun

The exact-head **push** run `44257880331` (attempt 1, job `134643839279`) has all required steps successful. Read its actual downloaded suite logs: H1 **152 PASS**, analytical **4 PASS**, adapters **62 PASS / 1 optional SKIP**, product/source **19 PASS**, Node **39 PASS** = **276 passes plus one optional skip**. These are hosted executions, not an additional 276 reviewer-run tests. The browser logs state original explorer, product entry and new real-HTTP source viewer PASS. The HTTP logs contain `/favicon.ico` **404**, so “no JS page errors” is **not** “zero HTTP errors.”

CI's original-archive replay receipt reports exactly D1, D2, DEV_BRIDGE, TEACH_RING4, S1, D2_K2 as **`BYTE_IDENTICAL`**, every row with **`nativeExecutedByReplay=false`**. The source workflow includes a byte comparison of saved comparison output and regenerated source-only JSON. I directly inspected these receipts and workflow, **not** the five original diagnostic ZIP archives in this reviewer environment; do not mistake inspected CI replay for a fresh native run or a personal independent archive reconstruction.

The [exact GitHub compare](https://github.com/physicsvigilante/sim_heat/compare/0278b79b4da1c3196edca7903189713e0482f3f6...0b15c02e5c3c60af32224e0ec5f29a2920927d5a) confirms all 14 paths are added, no old sources modified, including physical library, H1 grammar/study/policy/reference, archived viewer, native runner and C1 freeze. The new workflow contains no OMC installation/query/build/launch command; its replay helper describes and performs archive decoding/checking rather than launching a compiler. Original diagnostic labels remain `diagnostic_only/nativeQualified=false`. **PR54 was separately fetched and remains open, draft, unmerged.**

## Source-fidelity checks / physical limits

The illustrative task, Modelica model, declared study and saved JSON consistently show fixed boundary `sourceHot=354.15 K`, `sourceCold=287.15 K`; Bodies `copper(0.4 kg, 385 J/(kg K), 299.15 K)`, `steel(0.9 kg, 490 J/(kg K), 311.15 K)`, `aluminum(0.7 kg, 900 J/(kg K), 291.15 K)`; seven positive area/circular rods with the task's SI inputs; and **13 authored `connect` statements**, including `copper -> shortcut -> aluminum` and the **steel -> jLeft -> ownerless junction -> jRight -> cold** branch. Orientation describes authored `port_a/port_b` connectivity, not a measured heat-flow sign.

The four public requests are `steel_temperature` (steel.port, K), `branch_flow` (shortcut, W), `aluminum_energy` (aluminum, J), and `body_to_cold` (copper.port minus sourceCold.port, K): all are `not_computed`. The 0..1000 s, 1000-interval transient analysis descriptor does not establish an executed sample series. No new OpenModelica results, reference outputs, physical geometry, textbook givens or blind-teacher success are claimed. The TEACH_SPLIT3 developer-chosen illustrative data must never be relabelled as an independent teacher trial.

## Separate scope judgments

| Dimension | Judgment | Reason |
|---|---|---|
| Source interpretation fidelity | **FAIL — generic preview** | The default case matches its authored facts, but F-01 can display wrong component facts and F-02 suppresses permitted provenance. |
| Physical/numerical correctness | **LIMITED SOURCE SANITY; NATIVE UNKNOWN** | Existing laws untouched; source SI signs/topology and derived dimension checks plausible; no new native trajectories or independently checked solution. |
| Native simulation / observation coverage | **NOT TESTED for PR55** | All four public requests remain `not_computed`; six original native *diagnostic* archives only replayed offline. |
| Evidence integrity / provenance | **CI identity/preservation PASS; attribution completeness FAIL** | Exact SHA/tree/ZIP, byte-preservation and no promotion verified at stated level; component/model provenance still incomplete in display. |
| Teacher-facing usefulness | **CONDITIONAL / not teacher-qualified** | Source graph and units can support inspection; source misselection and hidden assumptions undermine trust; no classroom outcome evidence. |
| Textbook-answer completeness | **NOT APPLICABLE** | Illustrative developer-authored source exercise, no textbook result or answer. |

## Release advice / stop conditions

**Do not approve the claimed generic source-preview milestone yet.** Fix F-01's distinct selection namespaces and F-02's component/model provenance path in a **new exact source commit**, with targeted source admission + browser tests covering name collisions and assumption visibility; disposition F-03 explicitly. Rerun exact-new-head CI including all six original archived diagnostic replays, saved comparison, source-only byte identity, and hosted real-HTTP Chromium refusal/race tests. Then request **targeted** Chat B re-review; a new full R2 is needed only if changes broaden physics, native/evidence or authoring semantics.

**Strict boundaries remain in force:** no PR55/PR54 merge, no OpenModelica invocation/install/version query/build, no native runner, no frozen-reference regeneration, no historical C1 integration or rerating of `diagnostic_only/nativeQualified=false`. This report is an independent source-preview assessment only, not an approval for native physics, production deployment, or owner merge.
