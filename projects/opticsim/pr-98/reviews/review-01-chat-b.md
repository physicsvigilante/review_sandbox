# Opticsim PR #98 — independent Chat B R2 numerical research/evidence review 01

**Verdict: PASS — bounded NUMERICAL RESEARCH/EVIDENCE ONLY.** This is **not** a production-physics, native-engine, observer-neutrality, browser, measurement, Stage-2, or merge approval. **Keep [PR #98](https://github.com/physicsvigilante/opticsim/pull/98) DRAFT and UNMERGED**, including its disposable research workflow. This is a separate Chat B assessment, not an adoption of the developer's exact-reference result.

**Reviewed exact source:** Opticsim HEAD **477db82058dde2aba4627a51c8d991e24dce6015**, production base/main **50dd0f4d9530d0a61bb4c7064c4326a8ac0ce518**, pinned upstream PhyDemo **811f508d2b070898c241a568b0c167dcb8645251**. Read the [central request](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-98/REQUEST.md), [protocol](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md), [risk policy](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md), prior [PR97 independent report](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-97/reviews/review-01-chat-b.md), relevant source contracts, and original archived records.

## 1. Source, frozen protocol, and RNG pathway

- GitHub's exact PR diff shows **five new files, 631 added lines, zero deletions**: evaluation/fixed-native-rng-v1/PROTOCOL.md, run.mjs, exact-check.py, README.md and .github/workflows/research-fixed-native-rng-onecase.yml. **No modifications** to production src/, vendor, authored schemas/scenes, numerical thresholds, Stage-1/Stage-2, browser, or measurement logic. The protocol commit [6e6d3a7](https://github.com/physicsvigilante/opticsim/commit/6e6d3a7ed66b04473b0c1e0fceac557a99468168) is an ancestor (the reviewed head is six commits ahead); commit time **2026-11-16 14:24:28 UTC**, earlier than reviewed native trial log at **14:30:07 UTC**. The evidence establishes ordering of the reviewed execution, not a global proof that no unreported local test ever occurred.
- Independently read pinned [Scene.js](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/Scene.js): serializable randomSeed defaults null; loadJSON copies supplied scene properties, then executes seedrandom(this.randomSeed) if nonempty **before constructing scene objects** (otherwise time-based seeding). Pinned [Glass.js](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/sceneObjs/glass/Glass.js) getIncidentData consumes two scene.rng() values for auxiliary inside/outside perturbations. Thus the earlier PR97 schedule-only RNG control was materially incomplete.
- Original [src/adapter.js at base](https://github.com/physicsvigilante/opticsim/blob/50dd0f4d9530d0a61bb4c7064c4326a8ac0ce518/src/adapter.js) does not add randomSeed. [PR98 run.mjs](https://github.com/physicsvigilante/opticsim/blob/477db82058dde2aba4627a51c8d991e24dce6015/evaluation/fixed-native-rng-v1/run.mjs) calls original core.compile(source), **copies** its native config, attaches only randomSeed = opticsim-fixed-native-seed-v1-20261116, and calls unmodified core.loadNative; it asserts the loaded scene's seed and does not explicitly sample scene.rng() before simulation. It uses the same seeded test-only core.Session construction for **all four profiles**, including OFF/ON. Therefore these ordinary seeded profiles **are not byte-identical public evaluateDocument invocations**. No assertion is made about uninstrumented RNG consumption in every upstream constructor or elimination of all engine randomness.
- The baseline [src/planar-media.js](https://github.com/physicsvigilante/opticsim/blob/50dd0f4d9530d0a61bb4c7064c4326a8ac0ce518/src/planar-media.js) invokes the original Glass.onRayIncident **once**, forwarding identical native args. In the two TAP modes, run.mjs wraps only the Stage-1 finiteDiagnostic.beforeIncident method, makes the same capped p1/p2/incident scalar copies, and calls the original diagnostic once. Archive retains scalar arrays only after terminal; blackhole discards them. This matches intended hot-path operations per callback, **not proven equal timing/observer neutrality**.

## 2. Original GitHub artifacts: independently downloaded and hashed

I downloaded original [PR96 Actions artifact 14229080814](https://github.com/physicsvigilante/opticsim/actions/runs/43872962563/artifacts/14229080814) and original [PR98 Actions artifact 14234576916](https://github.com/physicsvigilante/opticsim/actions/runs/43886295485/artifacts/14234576916), not a developer-retyped summary or private Page archive. Both ZIPs passed CRC testing. SHA-256:

- **PR96 original ZIP:** 12,217 bytes; **467b548edbcdfc8cf4aecdab416d134d3ac703572a4e0330a4379fcb28df9929**.
- **PR98 original ZIP:** 20,665 bytes; **e79f5dd396c67bd513a484e0b6fb8082b08da2ed82c237eb1eaf688e88150ab2**.

Every one of PR98's **six original ZIP members** was independently rehashed (size in bytes):

| Original archive member | Size | SHA-256 |
|---|---:|---|
| source-pr96-original/inputs.json | 19,205 | caa07af040d0a71b50ea6b69470aa55a545b04d52195994913123a902b434df3 |
| source-pr96-original/report.json | 120,930 | 9324aabab62a2ab0e3636c30dec2154e590daf7c90304e8aeafa564e41250698 |
| source-pr96-original/exact-reference.json | 23,826 | 497d2e568ca851dd98941be38ccd54b7473953b56405b653771f784633808f12 |
| llm-authoring/fixed-native-rng-v1/inputs.json | 19,205 | caa07af040d0a71b50ea6b69470aa55a545b04d52195994913123a902b434df3 |
| llm-authoring/fixed-native-rng-v1/report.json | 93,213 | b9ea7eb4366fddfd3dcdaf9e8ac6f475e04804bec54b696fbd93eda3814511f2 |
| llm-authoring/fixed-native-rng-v1/exact-reference.json | 16,024 | 820cb342ad72b0f0a5db79aa78fc37d4b6d938b6dab27987a574096b7880a56d |

The **three inherited PR96 member byte strings** also matched the separately downloaded original PR96 ZIP exactly; PR98's copied inputs.json matched the original PR96 inputs.json byte-for-byte. Independently serialized the chosen original critical-shift-neg schema-v9 physical document with the canonical JSON pretty-print/newline, reproducing **scene-save SHA-256 4389fecfe80ad01fa7cb160f22319327ccf9e30bb35c211012cc15599ff422c6**. No authored scene retune is evident.

## 3. Independent schedule and all original native outcomes

Using a newly implemented unsigned xorshift32 + integer-space Fisher–Yates shuffle with **schedule seed 0x9800A55** (different from the native string seed), I reconstructed all **24/24** block/slot/mode/ordinal assignments in the original research report. Six block mode orders (OFF=seeded-off, ON=seeded-on, BH=seeded-tap-blackhole, AR=seeded-tap-archive):

1. AR / BH / ON / OFF
2. BH / OFF / AR / ON
3. OFF / ON / AR / BH
4. OFF / AR / ON / BH
5. AR / BH / OFF / ON
6. AR / ON / BH / OFF

All **24/24 native records are genuinely marked FAILED**, six in **each** mode, never completed; each original native result independently rehashes with SHA-256 fingerprint **d5a678236ef9f67a49063a3e91f990004699587edeb8971a4efcdd0aeff600d0**. All have **G1: native interface emitted nonfinite or indeterminate encounter evidence**, four Glass interactions, one invalid observation, processed=5, emitted=1, zero native warnings/truncation, and identical first Glass event (reported TIR from inside at face-34). The first event is **not** a qualified optical outcome because the entire run failed. ON/BH/AR Stage-1 advisory is suppressed with reason NATIVE_RUN_NOT_COMPLETE; OFF has none. No runner-level missing rows or errors; both TAP variants show 4 actual callbacks per trial, 4 captured per trial under cap 128, zero capture faults, and callback meter equality. The six archive TAP trials retain 24 original scalar callbacks; the six blackhole TAP trials persist no raw coordinates.

Across **all 24** recorded configurations, the **unseeded compiled native hash** is exactly **e74e1452bd26402a94b9e0748be38ce8a0720274e5910b68bc65634a72bec1b7** and the **seeded test-native hash** is exactly **24006e61e74d527d74a8acec4b5ec25a4e543f2a384a5e90ab1d50f97c49a109**; observed scene.randomSeed = opticsim-fixed-native-seed-v1-20261116 for every row, and all source hashes agree. This is consistency across **original logged configurations and inspected source**; I did not independently rebuild the pinned native binary to recompute its compiled config bytes.

## 4. Independent exact finite-face numerical audit

I wrote and executed a **separate local Python integer-lattice algorithm**, not importing Chat A's Python Fraction checker or Opticsim's JS audit. It lifts each serialized binary64 number via as_integer_ratio() to a **common power-of-two integer lattice** per hit, computes **integer cross-product determinants**, signed exact ray t and finite-face u, compares exact forward/cutoff inequalities by cross multiplication, and compares the exact constructed hit with the archived binary64 point *without an invented position tolerance*. Float computations are used only for the documented finite-face residual (1e-5 mm), vertex clearance (0.01 mm), and near-parallel conditioning (sqrt binary64 epsilon) guards.

Independently grounded all four stored face segments for **all six archive processes** to original PR96 polygon coordinates (authored **y-up**, recorded native rays and hits **y-down**). Each archived point has a unique sufficiently near finite face. I separately implemented pinned PhyDemo's **binary64 global-coordinate linesIntersection calculation order** and its rounded on-ray, finite-segment and step-greater-than-cutoff gates, reproducing **24/24 saved incident coordinates and 24/24 native rounded gate acceptances**.

| Independent integer-lattice result | Archived callbacks | Distinct full serialized binary64 signatures |
|---|---:|---:|
| EXACT_INTERSECTION_NOT_FORWARD (inconsistent) | **6** | **1** |
| NATIVE_INCIDENT_POINT_AGREEMENT_UNBOUNDED (UNKNOWN) | **12** | **2** |
| REPORTED_HIT_AT_OR_NEAR_VERTEX (UNKNOWN) | **6** | **1** |
| **TOTAL** | **24** | **4** |

All **24/24** independently determined status/reason pairs agree with original JS recorded classifications; zero disagreements. The source's same-author exact-reference file is consistent too, but was **not** used as the numerical oracle.

**Specific adversarial example:** all six archive runs' zero-based callback **2**, inferred face-12, have **exact represented t=0** (not strictly forward), while the pinned **rounded** intersection is **(1153.1213249443667, 740)** with apparent forward travel ≈ **0.0004001264 mm**, passing native rounded on-ray, finite-face, and **1e-6 mm** minimum travel gates. This is a precise *represented binary64 line versus rounded native intersection* discrepancy; it does **not** identify a unique failure cause or ideal critical-angle truth. Native supplied point mismatch for 12 other callbacks remains UNKNOWN absent a calibrated error envelope; all six near-vertex callbacks remain UNKNOWN. **All 24 callbacks came from six FAILED native trials**, not independent accepted optical rays. Repeated identical JSON signatures do not establish original in-memory signed-zero bits.

## 5. Exact-head CI — 11/12, NOT 12/12

Queried GitHub's workflow runs by exact HEAD. There are **12 concluded workflows: 11 SUCCESS, one FAILURE**. Research-integrity workflow [43886295485](https://github.com/physicsvigilante/opticsim/actions/runs/43886295485) succeeded on Node v24.19.0 and completed original native execution, the same-author Python check, and artifact upload. **That successful research workflow does not reclassify 24 FAILED native processes as successful optical simulations.**

Unchanged curved-mirror workflow [43886295178](https://github.com/physicsvigilante/opticsim/actions/runs/43886295178) **FAILED on both attempt 1 and attempt 2**. I inspected both GitHub jobs and original job logs; npm tests, curved-mirror native integration acceptance and build all succeeded on both attempts. The real-browser step failed both times with **“Error: No Chrome/Chromium available; browser evidence cannot be claimed”** (first at 14:30:38 UTC; rerun at 14:33:00 UTC). With no curved-mirror/browser/production changes in this five-file PR, this is **a runner/browser-availability gate failure**, not a demonstrated numerical regression from PR98; nevertheless real-browser verification remains **NOT PASSED** and exact-head source CI is **NOT GREEN**. No silent Chrome workaround, browser-pass claim, or production-merge authority follows.

## 6. Interpretation, residual limitations, and smallest next test

**Supported bounded finding:** for **this one unchanged source scene**, **this single fixed native seed**, **this exact pinned engine**, and the **common test-only seeded Session path**, the archived fresh-process results have stable **FAILED** status, same native fingerprint and four Glass callbacks across all four observation profiles. Fixed native seed meaningfully controls one identified confound left by PR97, but the current test cannot prove the seed *caused* PR97's 21/48 status switches, observer neutrality, time-matched profiles, general determinism across machines, perfect RNG control, valid physical critical branch, correct full ray route, safe geometric tolerance, or canonical measurement acceptance. The failure reason is an original native interface observation error and must stay visible. All failed-run Stage-1 measurements remain withheld; mandatory Stage-2 withholding is unchanged.

**Execution distinction:** I directly downloaded and hashed the two original archives, reconstructed the schedule, source-hash-checked the authored scene, recomputed original native projections/fingerprints and finite-face geometry with independently written numerical code, reconstructed rounded native gates, and inspected pinned source plus actual CI attempt logs. **I did not install or run a fresh Node 24/PhyDemo simulation or an independent browser**, and did not instrument internal RNG calls; native execution evidence comes from the original Actions logs/artifacts.

**Smallest defensible next experiment:** preregister **one second different native seed** on the **same untouched original source case** using the existing shared test-only path, a balanced four-profile schedule and original-process reporting. Keep the original PR96 and PR98 archives immutable; compare native status/fingerprint and face callbacks by seed. Any changed behavior would establish seed-sensitive observations for this case, **not** observer causality or correct physics. Separately repair/requalify Chrome availability for the existing curved-mirror browser gate as a **CI-infrastructure task**, without changing numerical thresholds or treating the failed workflow as green.

**FINAL GATE: PASS — independent R2 NUMERICAL RESEARCH/EVIDENCE ONLY. HOLD PR #98 DRAFT/UNMERGED.** No production optics, PhyDemo, native cutoff, authoring schema, measurements, Stage-1/Stage-2, browser workflow, release gate, or source-PR state has been modified by this review.
