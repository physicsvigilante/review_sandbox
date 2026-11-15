# Chat B independent R2 review — SIM_HEAT H2-02, PR #14

- **Project / source repo:** SIM_HEAT / [physicsvigilante/sim_heat](https://github.com/physicsvigilante/sim_heat).
- **Source PR and base SHA:** [PR #14](https://github.com/physicsvigilante/sim_heat/pull/14); base **a33a0d79da405ff4c7191b9bfb94e096b10e2a9f**.
- **Exactly reviewed head SHA:** **281c5a45b536b698ea2b6896710e3cc49e20698b**; not floating branch HEAD.
- **Reviewed source tree / diff:** request-pinned tree **5ed4a1c0ac34a5fe5f463aafb1433abfa557c999**; [pinned commit](https://github.com/physicsvigilante/sim_heat/commit/281c5a45b536b698ea2b6896710e3cc49e20698b), [PR diff](https://github.com/physicsvigilante/sim_heat/pull/14/files). Fourteen added files, 842 additions, zero deletions; no edits to H1 engine, original viewer, Modelica library, experiments or native policy.
- **Reviewer:** Chat B, separate ChatGPT conversation, GPT-6; independent *context*, not verified independent model weights or human subject-matter adjudication.
- **Date/time:** **2026-11-16, approximately 00:10–00:40 IST** (2026-11-15 UTC).
- **Scope/risk:** **R2**, generic H1 native-evidence adapter, saved-trajectory contract and teacher-facing data-only topology viewer; D1, D2, DEV_BRIDGE; source/provenance, K/J/W ownership, signed flow, refusals and UI. No new physical law or solver accepted here.
- **Were source files changed during review?** **No.** Only an isolated local scratch reproduction was prepared; no source PR writes, merge, native launches or dependency installs. Rechecked PR remained draft, open, unmerged at exact head.
- **CI runs / artifacts actually inspected:** author CI [43745347155](https://github.com/physicsvigilante/sim_heat/actions/runs/43745347155), downloaded artifact **14173792995** (ZIP SHA-256 **d0283eea89e5e4b4a413c767ac2560768f695876b83f4cd0216049523a0c62e8**), including logs, head marker and screenshots D1/D2/bridge/mobile/refusal. Downloaded original native artifact **14152886226** (SHA-256 **8fc38b9e2f040b48ab5cbeab34e8698b7c99c4d462a1e31e8bc33b0395185379**) and **14155084346** (SHA-256 **f16975a25eea79f61f7819fb9e704ab04a33630044a51a0d062b8399c1c9ce38**). All three ZIP CRC checks passed.
- **Outcome: changes-requested** (scoped). **Three substantive evidence-presentation defects**, plus one smaller reversal-label defect. **No demonstrated numerical or source-topology defect in the three shipped original archives/bundles.** Source PR should remain draft.

## Findings

### F-01 — BLOCKER — refused case leaves prior evidence visible

**Location:** [viewer/network/app.mjs lines 9, 25, 29–30](https://github.com/physicsvigilante/sim_heat/blob/281c5a45b536b698ea2b6896710e3cc49e20698b/viewer/network/app.mjs#L9).

**Independent reproduction:** Load accepted D2, record the body J readouts, then select D1 with its case response deliberately replaced by mismatched JSON bytes (unchanged catalog digest). The source digest correctly refuses and disables controls; *however*, the prior D2 energy/temperature-related labels and values and the D2 model provenance remain in the page. The value in '#current-value' becomes a dash, but '#energy-readouts', '#time-label', '#graph-count', '#reversal-note', '#model-id' and other evidence-bearing fields are not cleared. **I executed the byte-identical pinned app.mjs/core.mjs in a minimal Node DOM harness and confirmed that previous D2 J values and D2 model identity persist after refusal.** The author's own CI **refusal.png** also visibly contains old bridge energies and boundary powers behind a case-digest refusal; the CI browser assertion only checks the main value and disabled slider.

**Expected:** A rejected new case displays *no prior observations as current evidence*; explicit empty/refused placeholders for all quantitative panels and provenance. **Observed:** stale signed W and J readouts survive a refused source. This contradicts the explicit refusal/clear-state acceptance requirement.

**Evidence/confidence:** Confirmed source execution (DOM harness, not a real browser), corroborated by the author's real Chromium screenshot. **Correction:** make error/pending-case transitions atomically clear all evidence-bearing nodes, previous selection and observation labels, charts, readouts, times, direction, legend, reversal, provenance/import status; add a real-browser regression asserting absence of old J/W/K readouts and old source identity after a tampered catalog case.

### F-02 — BLOCKER — valid CSV import can be assigned to a different selected case

**Location:** [viewer/network/app.mjs lines 29–32](https://github.com/physicsvigilante/sim_heat/blob/281c5a45b536b698ea2b6896710e3cc49e20698b/viewer/network/app.mjs#L29).

**Independent reproduction:** Load D1; start importing its *authentic* 223,471-byte archived normalized.csv. Hold the asynchronous WebCrypto SHA operation, select D2 successfully, then release the D1 hash. The import callback does not capture/check a case identity or request generation after its awaits. The correct D1 CSV passes the D1 hash, then **updateRows(D1_rows, …)** applies those rows under **current = D2**, advertising **1,001 verified samples for D2**. D2 cold/hot energy fields become **NaN J** because those fields are absent from the D1 rows. The old D1 rod values may also be presented under D2's model and source labels.

**Expected:** An import belongs exclusively to the bundle and selection active when import began; switching cases cancels/discards its pending result. **Observed:** cross-case evidence contamination. **I reproduced this with the exact pinned app.mjs/core.mjs and exact original D1 CSV in a controlled Node DOM harness, pausing just the full-CSV digest; this is NOT a separate Chromium run.** The source's async lifecycle and observed wrong-case readouts establish the defect.

**Correction:** capture the immutable case ID/object and a monotonically increasing selection token before the first await; invalidate pending imports on case switch/refusal and test the token *after* parse and before any DOM/state update. Avoid stale success/error status from an old import. Add a controlled delayed-digest desktop browser regression that switches D1 → D2 during D1 import and checks D2 remains at its own 21-point preview with no D1 rows or NaN.

### F-03 — MAJOR — schema accepts false topology/channel ownership, despite valid suffixes

**Location:** [viewer/network/core.mjs lines 59–86](https://github.com/physicsvigilante/sim_heat/blob/281c5a45b536b698ea2b6896710e3cc49e20698b/viewer/network/core.mjs#L59), contrasted with the correct model-derived ownership in [viewer/network/tools/build_case.py](https://github.com/physicsvigilante/sim_heat/blob/281c5a45b536b698ea2b6896710e3cc49e20698b/viewer/network/tools/build_case.py).

**Independent repro with schema-valid, deliberately altered copies of the actual bundles:**

1. Change the D1 edge to **from=body, to=reservoir** without altering native flow data or node.ports. validateCase **accepts** it, although D1 model connects **rod.port_a to reservoir** and **rod.port_b to body**. It now labels original positive **+12 W** as **body → reservoir**, the reverse of native meaning.
2. In D2, exchange the cold/hot node temperature and energy field strings, leaving both valid '.T' / '.dU' columns. validateCase **accepts** cold.temperature=hot.T and cold.energy=hot.dU; it would label the cold body's initial **293.15 K** as **353.15 K**.
3. In the bridge, exchange heated/cooled boundary power field strings. validateCase **accepts** cooled.power=heated.Q_to_network, falsely attributing an initial **+13 W** source power to cooled rather than the actual **−10.8 W** absorbed at cooled.

**Expected:** enforce graph edge port_a/port_b membership, unique/consistent ownership of each port, node temperatures/energy/boundary power bound to their actual named owner, and junction sensor to one of its actual rod endpoints. **Observed:** only identifier existence, field suffixes and column inclusion are validated; arbitrary node.ports strings/ownership are not reconciled.

**Limit/importance:** The **three shipped hashes and adapter-generated graphs are correct**; an altered file cannot pass the current tracked catalog digest unless the catalog is repinned. The defect is in the claimed **general case schema / next data-authored case** and any accidentally misauthored/reviewed successor bundle, *not* in the original D1/D2/bridge demonstration. **Correction:** extend validateCase with explicit rod endpoint-to-node port membership, port uniqueness and owner-bound channel identity checks; regression against a recomputed-catalog-digest wrong-port/wrong-owner case, not only an unknown node ID.

### F-04 — MINOR — a zero touch is reported as a genuine signed reversal

**Location:** [viewer/network/core.mjs lines 124–129](https://github.com/physicsvigilante/sim_heat/blob/281c5a45b536b698ea2b6896710e3cc49e20698b/viewer/network/core.mjs#L124), used by [app.mjs lines 27, 31](https://github.com/physicsvigilante/sim_heat/blob/281c5a45b536b698ea2b6896710e3cc49e20698b/viewer/network/app.mjs#L27).

**Independent reproduction:** firstSignChange with valid saved values at t=0,1,2 of **+1 W, 0 W, +1 W** returns **{from:0,to:1,index:1}**, even though no opposite signed value was observed. The test's '[positive,zero,positive]' is synthetic and is **not** asserted to occur in the three archived runs. The real bridge **does** have a legitimate **−0.0096537564 → +0.0058078818 W** crossing between 1720–1730 s; the existing bridge result remains valid.

**Correction:** report observed reversal only when supported by *opposite nonzero* sampled signs (allow bracket across intervening zero sample(s) without inferring exact crossing time). Distinguish 'reached zero' from 'reversed'; regress +/0/+, −/0/−, +/0/− and −/+.

## Tests and independent evidence

### Checks performed by Chat B — NOT merely reported CI results

1. **Pinned source and unchanged diff:** fetched exact commit files and base/PR changed-path list. Independently reconstructed the exact viewer source locally: git blob IDs matched the GitHub-pinned **core.mjs 216255e5…**, **app.mjs eca7b610…**, **index.html 194c7947…**, **D1 01fbcaf0…**, **D2 d20089a1…**, **bridge b4d18123…**, **index 15e12a67…**. No source repo modification.
2. **Original archives:** downloaded and SHA-256/CRC checked both original native ZIPs and CI ZIP (digests above). Read original attempt.json, verification.json, model.mo, study.json, normalized.csv, raw model_res.mat, mat_provenance.json and build/simulation return codes. Exact model/study/MAT/CSV hashes and diagnostic status agree for all three; attempts are **checks_passed, diagnostic_only, nativeQualified=false**. Read archived 'channelIsIndependentMeasurement' as a **MAT alias/provenance classification**, *not* proof of independent sensor measurement.
3. **Native raw MAT against CSV — independent SciPy decode:** all **1002 / 1002 / 2002 raw rows** (including the identical terminal duplicate) matched the original MAT timestamp grid exactly. Comparing original numeric MAT rows, sign-negated aliases and constant parameter tables against every exported CSV channel gave **maximum absolute difference 0** across **12 + 14 + 42 = 68 non-time columns**. This checks CSV against the archived MAT, not whether the archived MAT reflects a separately authenticated run.
4. **Independent native-to-bundle reconstruction:** using a separate union-find on archived Modelica connect statements and a new Python CSV/JSON reconstruction (not importing production build_case.py) produced **exact matching SHA-256** for D1 **49c605d5…**, D2 **c0fc143d…**, bridge **07dbe098…** and exactly **21 / 21 / 23 saved preview rows**. Original full grids **1001 / 1001 / 2001**. All actual port_a → port_b directions matched: D1 reservoir→body; D2 hot→cold; bridge left→right, rejectLeft left→cooled, rejectRight right→cooled, supplyLeft heated→left, supplyRight heated→right. The only native bridge sign change across the 2001 grid samples was at 1720–1730 s. No invented sampled values or crossing time detected.
5. **Independent physical arithmetic from original full CSVs:** D1 analytic temperature max error **1.56e−5 K**, analytic flow max error **3.12e−6 W**; D2 analytic temperatures max error **2.07e−5 K**, analytic flow max error **5.52e−6 W**, worst total isolated-body energy drift **2.84e−10 J**. Bridge all five Fourier conductance checks and both body ΔU=capacity×ΔT identities had **zero residual** in the decoded numeric values; node/boundary signed-power ledgers were within **1.78e−15 W**. These are **new review calculations**, *not* a new solver qualification, fresh native launch or independent reference-source certification.
6. **Exact JavaScript contract and CSV parser run in Node 22:** **6 independent adversarial tests passed as assertions of expected observations**, including three *successful* authentic full-CSV imports (1001/1001/2001), all preview rows identical; negative byte SHA, missing terminal duplicate, nonidentical repeated terminal, missing required channel, wrong grid, false nativeQualified, unexpected fields, invalid time, missing observation, wrong endpoint ID and size/shape refusal. The **two intentional acceptance findings** were false rod/node/channel ownership and +/0/+ false reversal (tests assert source currently accepts/mislabels these).
7. **Exact app.mjs/core.mjs executed in a minimal DOM harness:** reproduced F-01 and F-02 with the original source files and real D1 CSV. This tests source state and controlled async ordering but **does not establish actual browser interaction or visual layout**.
8. **Independent Chromium attempt failed due environment policy:** Python Playwright and Chromium were available, but navigating to localhost, file:// and data: pages failed **net::ERR_BLOCKED_BY_ADMINISTRATOR**. **No Chat B real desktop/mobile browser run or screenshot is claimed.** The downloaded author's real-Chromium screenshots were visually inspected (bridge, mobile, refusal). Their bridge and mobile layouts display the correct labels/arrows; notably, refusal.png corroborates F-01 by displaying old W/J readouts after a new case digest refusal.
9. **CI evidence only, not independent tests:** pinned run 43745347155 successfully reports **151/151 H1**, **4/4 arithmetic**, **4/4 adapter**, **7/7 JS**, and passing Chromium desktop/mobile smoke. The head marker inside the downloaded artifact equals the reviewed SHA. Earlier author CI browser failures 43744485774 and 43745168791 remain historical; there is no evidence of a changed native physics tolerance. No new OpenModelica build or launch was performed for H2-02.

**Not executed independently:** production compile_case.py using the full production h1 module suite; destructive ZIP/member negative tests *through that adapter*; a real browser import/switch timing test; any new OMC build/launch; arbitrary fourth physically native-qualified assembly; C1 external authorship; classroom use. Adapter preflight guards were source-reviewed, while archived inputs and source hashes were independently cross-checked. Unperformed tests are not marked pass.

## Separate scope judgments

| Dimension | Pass / Fail / Unknown | Basis |
|---|---|---|
| Source interpretation fidelity | **Pass (bounded)** | Archived illustrative models/studies and native port graph match D1, D2 and bridge; not a fresh textbook-source adjudication |
| Physical/numerical correctness | **Pass for original diagnostic traces; Fail for adversarial viewer semantics** | Exact MAT/CSV and independent arithmetic support originals; F-03/F-04 can mislabel valid numeric data when schema-valid data are misowned |
| Native simulation and observable coverage | **Pass for archived exports; Unknown for new qualification** | 68 native MAT/CSV export channels checked; historical runs diagnostic-only, no new native launch |
| Evidence integrity and provenance | **Fail at viewer presentation boundary** | Correct archive/catalog hashes but F-01 stale refused evidence, F-02 cross-case import and F-03 insufficient owner checks |
| Teacher-facing usefulness | **Unknown for classroom value** | CI screenshots show usable desktop/mobile network exploration; refusal/race can mislead, no observed teacher trials |
| Textbook-answer completeness | **Unknown / not applicable** | H2-02 is not a symbolic answer or textbook-solution completion milestone |

## Release advice

**Changes requested. Do not merge PR #14 yet.** Preserve the good original D1/D2/bridge archives, case fingerprints, H1 code and archived CI history. Correct **F-01/F-02 evidence-state isolation**, **F-03 field/port ownership enforcement**, and **F-04 zero-contact reversal labeling** in the small generic viewer scope. Add focused Node negatives and *real Chromium* regressions (especially source-digest refusal after nonzero readouts; verified D1 CSV import while switching to D2), then run new exact-head CI and produce targeted source/evidence review. Do **not** relax numerical tolerance, rewrite original native data, invent fresh independent measurements or reopen the solver architecture.

The smallest additional owner-side proof is a browser test that (a) shows a rejected selection leaves zero previous source values visible, and (b) delays an authentic native CSV import through a case switch and rejects stale completion; plus parser tests showing a repinned wrong-port, swapped-body-field and swapped-boundary-power bundle refuses. Existing original-data integrity work needs no new native runs merely to fix viewer logic. C1 and independent native/scientific qualification remain separate gates. No source PR state was changed by Chat B.
