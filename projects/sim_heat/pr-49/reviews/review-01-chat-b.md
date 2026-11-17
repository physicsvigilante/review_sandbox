# SIM_HEAT draft PR #49 — independent Chat B R2 review (review-01)

**VERDICT: CHANGES REQUESTED — one MAJOR source-topology *presentation* defect in the offline SVG.** The underlying Modelica connectivity, exact-source-bound JSON, nine expected-only request placements, offline/owner denials and pinned CI artifact have substantial supporting evidence. The *rendered diagram*, however, visibly disconnects the two parallel bridge rods from their junctions. This is a blocker for claiming the page faithfully *shows* the source network. It is **not** a newly demonstrated physical-model, numerical, native, or frozen-science failure.

## Review identity and boundaries

- **Project / source repository:** [physicsvigilante/sim_heat](https://github.com/physicsvigilante/sim_heat), [historical draft PR #49](https://github.com/physicsvigilante/sim_heat/pull/49).
- **Base:** `4f077d5e3f231dacae5986d66bdaf0bdbe555b83`, previous independently reviewed PR #48 topology overlay.
- **EXACT reviewed source HEAD:** `04461dd840c3249ced06c4bf0bdeecc25babe962`; **Git tree:** `55333659660daf041e8fa04bfef3ff9474924b02`. [Pinned source comparison](https://github.com/physicsvigilante/sim_heat/compare/4f077d5e3f231dacae5986d66bdaf0bdbe555b83...04461dd840c3249ced06c4bf0bdeecc25babe962).
- **Reviewer:** Chat B, GPT-6, separate ChatGPT conversation; **2026-11-17, Asia/Kolkata**. Separate conversational context, not an independent human expert or proof of different model weights.
- **Risk / scope:** R2; offline **nonphysical** source topology interpretation, SVG geometry and accessibility basics, expected request highlighting, adversarial source binding, native-evidence refusal, preservation and hosted CI receipts. Not approval of physical apparatus geometry, actual heat direction, generated Modelica outputs, browser-wide UX, owner authorization, native execution or production merge.
- **Source modifications during review:** none. No original Modelica/study/physics, frozen science, PR31 references, archived CI, branches, or source PRs were changed; no OpenModelica query/build/launch, MAT decoding, reference resealing or native plan execution.
- **Diff independently confirmed:** **8 commits ahead, 0 behind; exactly FOUR ADDED files, ZERO previously existing files modified/deleted**: `qualification/h1_c1/f02/offline_nonphysical_schematic_viewer.py`, `test_offline_nonphysical_schematic_viewer.py`, `NONPHYSICAL_SCHEMATIC_VIEWER_SCOPE.md` and `.github/workflows/h1-c1-f02-nonphysical-schematic-viewer.yml`. The original authored model and study, checking-only PR31 reference, frozen native runner/checker and historic evidence therefore do not change in this PR.
- **Central packet / protocol:** [REQUEST](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-49/REQUEST.md), [PROTOCOL](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md), [risk policy](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md).

## Findings

### F-01 — MAJOR / changes required: drawn rods do not visually attach to source junctions

**Source:** [viewer lines 112–145](https://github.com/physicsvigilante/sim_heat/blob/04461dd840c3249ced06c4bf0bdeecc25babe962/qualification/h1_c1/f02/offline_nonphysical_schematic_viewer.py#L112-L145) (layout) and [lines 340–373](https://github.com/physicsvigilante/sim_heat/blob/04461dd840c3249ced06c4bf0bdeecc25babe962/qualification/h1_c1/f02/offline_nonphysical_schematic_viewer.py#L340-L373) (rendering); [tests lines 101–118 and 221–240](https://github.com/physicsvigilante/sim_heat/blob/04461dd840c3249ced06c4bf0bdeecc25babe962/qualification/h1_c1/f02/test_offline_nonphysical_schematic_viewer.py#L221-L240).

**Independent reproduction:** I downloaded and SHA-verified the exact-head original CI ZIP, extracted its *actual* 11,149-byte `open-offline-schematic.html` and `nonphysical-schematic-contract.json`, loaded the complete HTML into an **offline Chromium/Playwright browser context** (via `page.set_content` because the execution environment blocks `file://` navigation), and inspected both the default screenshot and the `flatBridgeFlow` highlighted screenshot. Both bridge segments plainly *float* between leftBuffer and rightBuffer: they are not visibly joined to either junction. Independent geometry readback from that archived contract and SVG gives:

| Source rod | SVG line endpoints, diagram px | Node circle centers/radius | Minimum gap from EACH line endpoint to intended circle perimeter |
|---|---|---|---|
| `hotLead` | (168,218)→(346,218) | (132,218), (382,218); r=29 | 7.00 px |
| `flatBridge` | (418,174)→(596,174) | (382,218), (632,218); r=29 | **27.85 px** |
| `roundBridge` | (418,262)→(596,262) | same two buffer circles; r=29 | **27.85 px** |
| `coldLead` | (668,218)→(846,218) | (632,218), (882,218); r=29 | 7.00 px |

The code offsets bridge lanes by ±44 px from their common node line but renders **only four bare `<line>` rod segments and four `<circle>` junctions**; there are **no SVG branch-connector/stub segments or polylines** joining the parallel lanes to the buffer circles. A pure node/edge *data* graph is valid, but the *displayed circuit-like topology* shows separate floating rods instead of a connected pair of parallel thermal paths. The 7 px series-lead gap is less misleading but should also be reviewed for a deliberate visual connection convention.

**Expected:** The student-facing picture must unambiguously depict `leftBuffer` connected to `rightBuffer` through **both** distinct source parallel rods while keeping all coordinates plainly diagrammatic. **Observed:** HTML labels and selected/DOM relationships say they connect, yet the drawn strokes do not. This is a reproducible **viewer-fidelity** failure, not a claim that the original source topology or physical network is wrong.

**Required correction:** Add visibly continuous *schematic* connector/stub paths from each parallel lane into its actual source junction (and consider the series endpoint gaps). Keep the branching/layout arbitrary and explicitly nonphysical; never convert the pixels into real geometry or change signs, native-null status or immutable sources. If highlighting a bridge, its connecting stubs should remain visibly associated with the selected rod/junctions, not become ambiguous. Add a **geometry/connectivity regression** checking rendered endpoint-to-junction path continuity for all four source rods **and a pinned actual-browser screenshot/visual check**; existing tests count `<g>`, `<line>` and `<circle>` elements but do not detect disconnected strokes. Rerun the full existing offline CI at the corrected NEW source SHA, preserve prior failures and request a **targeted independent re-review** of the new SVG.

**Confidence:** High for the exact-head HTML in Chromium, independently measured from original artifact bytes and visually inspected. No underlying native physics was tested.

### F-02 — PASS (bounded) / actual Modelica source topology and request semantics

Read the exact-HEAD [authored Modelica](https://github.com/physicsvigilante/sim_heat/blob/04461dd840c3249ced06c4bf0bdeecc25babe962/h1/cases/H1_C1_MODAL/model.mo), [modal study](https://github.com/physicsvigilante/sim_heat/blob/04461dd840c3249ced06c4bf0bdeecc25babe962/h1/cases/H1_C1_MODAL/study.json), prior [source-bound topology inventory](https://github.com/physicsvigilante/sim_heat/blob/04461dd840c3249ced06c4bf0bdeecc25babe962/qualification/h1_c1/f02/offline_topology_observation_overlay.py), and new viewer. The authored eight `connect()` statements give four equivalence-class junctions: `hotBath`—`hotLead`—`leftBuffer`—two parallel `flatBridge`/`roundBridge`—`rightBuffer`—`coldLead`—`coldBath`. Original four oriented rods are source port-a→port-b: `hotLead` 03→02; `flatBridge` and `roundBridge` 02→01; `coldLead` 01→00. The viewer obtains the hot→left→right→cold *reading order* via BFS of the source-only graph; it does **not** claim this to be physical left/right space. Its x columns 132/382/632/882 and y lanes 174/218/262 are **pixels**, not meters, original rod lengths or apparatus pose.

All **nine** authored public requests correctly map to **expected** source terms and the SVG IDs: left/right temperature `leftBuffer.T`/`rightBuffer.T` (K); four oriented rod `.Q_flow` terms (W); ordered `leftBuffer.T − rightBuffer.T` (K); left/right `.dU` terms (J). The two-temperature difference is only a string/expression, not a computed subtraction. `nativeTemperature`/`nativeHeatFlow`/`nativeValue` remain null; the source positive-flow arrows do **not** claim actual direction or magnitude. The original raw model and study SHA pins recorded in the contract are `9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435` and `b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b`.

The viewer calls `source.assert_exact_source_bound(original)`, not just the source overlay's coarse shape validator; its own `assert_exact_source_bound(candidate)` validates structure then compares canonical bytes against a fresh `contract()`. Source inspection and hosted negative tests support refusal of forged coordinates/geometry, branch order/rod endpoints, request fields/signs, fake native values, changed original reference identity and missing owner gates. **I did not independently run the original Python source-mutator tests in a local source checkout**; the personally executed checks in this review were artifact/HTML/browser/geometry checks. The canonical readback is source-binding, **not authenticated owner/native provenance**.

### F-03 — PASS (bounded) / offline HTML and tested interaction; accessibility certification not claimed

The real artifact's single HTML page contains exactly **4 source node groups, 4 source rod groups, one native `<select>` with ten choices (Show All + nine original requests), a labeled output with `aria-live`, and inline CSS/JS**. The inline script is hashed into the Content Security Policy; there are no external libraries, images, requests or remote sources. Text and data attributes use HTML escaping; JavaScript uses `textContent` rather than executable HTML.

In a **personally executed** isolated, offline Chromium session: no network requests, no page errors or console errors; all nine selector values triggered JavaScript and highlighted precisely the corresponding expected `data-element` IDs; all nine summaries contained `NOT COMPUTED` with the correct expected field expression and unit; Show All reset the selection; ArrowDown from Show All selected `leftTemperature` and applied highlighting. This confirms **that browser's runtime behavior on the original HTML bytes**, not cross-browser display, independent human accessibility testing, or direct `file://` open (blocked by the browser harness administrator). F-01 remains a visual network-connection defect despite successful DOM/selector operation.

### F-04 — PASS (bounded) / exact-head evidence integrity and failed-run history

**Personally downloaded** original [artifact #14338042242](https://github.com/physicsvigilante/sim_heat/actions/runs/44104959258/artifacts/14338042242) from [successful exact-head run #44104959258](https://github.com/physicsvigilante/sim_heat/actions/runs/44104959258): **44,522 bytes**, SHA-256 **`4194d32832918a4d26689f5b853524a1f0de071f35681d137b4e0357690274e6`**, **51 unique ZIP entries, all 51 CRC-valid**. Independently extracted the **11,149-byte HTML** and verified SHA-256 **`7ef7527aac8b0cab6bbdcdbfc7a03485845b039e8ab3fd958cb66589f8ec4a9a`**. Inspected original 9,484-byte JSON contract, artifact head/tree receipts and exact four-addition diff; compared the tree to the GitHub commit API, **`55333659660daf041e8fa04bfef3ff9474924b02`**.

GitHub's final workflow metadata shows **completed SUCCESS** at precisely `04461dd840c3249ced06c4bf0bdeecc25babe962` and one successful hosted job. Independently tallied the actual **17 archived hosted offline unittest log summaries = 409/409 PASS** (20 new viewer, 19 topology, 20 dependency, 17 coverage, 24 intake, 16 stale CAS, 18 toy state, 15 release HOLD, 16 fake CAS, 12 SQLite, 15 build-text, 24 stage, 16 disabled plan, 11 offline reference consumer, 8 source binding, 9 archived reference and 149 frozen H1). These are **HOSTED tests read from receipts**, *not* 409 tests personally rerun. The ZIP's frozen F0 pin-check receipt lists 14 `OK` checks; its additional original native-plan 23 pins and PR31 archived reference identity checks were checked by hosted workflow, not independently reconstructed as a scientific reference.

The two actual previous failed workflow runs were **not waived or counted as successful**:
- [#44104466557](https://github.com/physicsvigilante/sim_heat/actions/runs/44104466557) at `1fb9988c938979e6e67103068a2f9a02bff899f9`: real Python `SyntaxError: unterminated string literal` in HTML source.
- [#44104706280](https://github.com/physicsvigilante/sim_heat/actions/runs/44104706280) at `1946495a679043abefc4cf3e74096c05800dc7af`: real SVG group-count test failure, `AssertionError: 9 != 8`, due to treating the `svg` root as a `g`.
The later pinned run separately passed after the respective corrections. I verified failure status, job-step names and failure messages from GitHub job logs.

### F-05 — PASS (preservation only) / science and native authority remain blocked

Because the PR diff is only four **additions**, it preserves frozen original F0 evidence, original source and native tools. The original reported `hotLead.G` 80× precision margin versus the mandated ≥100× **FAIL** remains a failed historical gate; the PR32 alternative cross-host reproduced seal was **not** adopted following the reported failed bitwise reproduction. The owner Option A approved only the **original saved PR31 V2 OFFLINE analytical checking** raw SHA `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368`, canonical seal `d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`. I did **not** regenerate or independently numerically revalidate this reference.

Contract `nativeObservationCount=0`; **9/9 public native values not computed**, 4/4 junction temperatures null, 4/4 rod flows null, `releaseBlocked=true`, 11 real missing owner/host/adapter/CAS/budget gates and all checked native/owner/historical-success flags false. This PR provides **zero** OpenModelica-qualified simulations and **zero** permission for a native launch, regardless of successful offline tests.

## Tests and independent evidence summary

| Evidence class | Personally executed? | Result / limit |
|---|---|---|
| Exact pinned source/compare, Python implementation, study, original model and protocol | **Read directly via GitHub** | Four added files only; source-bound logic and field mapping inspected; no source execution |
| Exact-head downloadable artifact byte/hash/ZIP integrity | **YES** | 44,522 bytes, matching ZIP SHA, 51/51 unique entries CRC-valid, 11,149-byte HTML SHA matched |
| JSON/SVG geometry audit against original artifact | **YES** | Four junctions and rods, correct data IDs, but disconnected drawn lines (F-01) |
| Offline real Chromium HTML, screenshots and interactive selector/keyboard test | **YES** | Nine correct highlights, reset, no requests/JS errors; **visible floating bridge strokes** |
| Original Python 409-method suite, frozen SHA/PR31/23-pin checks | **NO; inspected hosted log and CI evidence** | Final 409/409 hosted offline pass, not independently rerun |
| Failed intermediate workflow evidence | **Inspected GitHub run/job logs** | Two failures preserved with concrete error evidence |
| Actual native OMC/physical measurements/PR31 reference regeneration | **NO — prohibited/out of scope** | No native values, no physical release qualification |
| Real browser `file://` opening, cross-browser/assistive-tech usability | **NO** | Local-file navigation blocked in harness; no claim of accessibility certification |

## Separate scope judgments

| Dimension | Judgment | Basis |
|---|---|---|
| Source interpretation fidelity (JSON/semantic edges) | **PASS — bounded** | Independently read original 8 connects, four junctions, distinct two-rod parallel pair, nine expected-only fields |
| Faithfulness of rendered topology | **FAIL (F-01)** | Source rod segments are visually disconnected from their claimed source junctions |
| Physical/numerical correctness | **UNKNOWN / out of scope** | Original F0 failure preserved; no independent numerical qualification |
| Native simulation and observable coverage | **UNKNOWN / NOT EXECUTED** | Explicit zero native results; nine requests remain uncomputed |
| Evidence integrity and provenance | **PASS — offline CI artifact only** | Exact pinned head/tree, SHA/CRC and 409 hosted checks; two failed runs preserved; not owner authentication |
| Teacher-facing usefulness | **CHANGES REQUIRED** | Browser select and labels work; network topology drawing itself is misleading |
| Textbook-answer completeness | **NOT APPLICABLE** | No numerical answer/solution claimed |

## Release advice and smallest next action

**Keep PR #49 draft and unmerged.** Correct F-01 in **new isolated viewer code/tests only**, provide a real offline screenshot plus deterministic endpoint/connector topology regression at the new SHA, rerun exact-head offline CI and obtain a **targeted independent review of the new diagram**. The absence of new physical/numerical defects shown here does **not** authorize production merge, native OMC use, release-gate waivers, owner signature, PR32 reference adoption, or any first native one-shot budget. All 11 actual pre-native gates require their own resolution and a *separate explicit owner authorization* for any future named native version/build/launch budget.
