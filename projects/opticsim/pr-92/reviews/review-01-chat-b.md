# Chat B independent R2 research-evidence review — Opticsim PR #92

**Verdict: PASS — FOR BOUNDED RESEARCH DATA AND REPRESENTED-BINARY64 NUMERICAL INFERENCE ONLY.** This does **not** approve a source merge, native optics correction, a validated optical critical-angle branch, observer neutrality, a new incident-point tolerance, classroom efficacy, or Stage-2 mandatory measurement withholding.

**Review date:** 2026-11-16. **Source:** [draft Opticsim PR #92](https://github.com/physicsvigilante/opticsim/pull/92), exact head **d8367c2d1bd23f3ee7c574feb45e7cc7e7793ee2**; base/main **50dd0f4d9530d0a61bb4c7064c4326a8ac0ce518**; pinned native PhyDemo **811f508d2b070898c241a568b0c167dcb8645251**. PR was checked as **draft, open and unmerged**. [Original CI](https://github.com/physicsvigilante/opticsim/actions/runs/43854663361); [original ZIP artifact](https://github.com/physicsvigilante/opticsim/actions/runs/43854663361/artifacts/14220951106); [hub request](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-92/REQUEST.md).

## 1. Independently performed work and scope

I read the hub [PROTOCOL](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md), [R2 risk policy](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md), frozen [AGENTS.md](https://github.com/physicsvigilante/opticsim/blob/d8367c2d1bd23f3ee7c574feb45e7cc7e7793ee2/AGENTS.md), request, developer report and [PR #91 Chat B review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-91/reviews/review-01-chat-b.md). I inspected PR #92's exact-head runner, Python reference, methodology, workflow extension and existing source observer/diagnostic/finite-geometry code. The base-to-head GitHub comparison has **exactly four changed files**: the new research runner, the new developer-authored Python checker, its README and twelve lines added to the temporary unified CI workflow. **No src/ or pinned native implementation changed.**

I downloaded the **original GitHub Actions artifact**, not a recreated report or Chat A's Page copy; verified archive and member bytes; parsed all five frozen complete v9 documents, 60 recorded trial rows and 87 original tapped hit captures; independently re-created the randomized schedule; and verified the saved scene and native projection hashes. I separately implemented a **new IEEE-754 sign/exponent/mantissa → common power-of-two integer-lattice → integer determinant** audit, without importing/running the developer's Python `Fraction.from_float` checker or the source JS `auditRecordedFiniteHit`. It recomputed all per-hit statuses, finite-face membership, exact t/u fractions where available, strict forward/cutoff conditions, vertex/conditioning guards and exact P* versus reported binary64 point. I also calculated elementary far-angle Snell/TIR controls and examined the source-head GitHub workflow metadata/logs.

**What I did not do:** rerun pinned PhyDemo, the 60 native OS processes, the 766 Node tests, Chrome, a new source-interpretation evaluation or a classroom test. My local Node 22 was used **only** to reproduce JSON serialization SHA-256 checks, and Python 3.13 only for independent offline calculations. The source/CI runner records use Node **24.19.0**. Fresh-process behavior is evidenced by `execFileSync(process.execPath, ... 'single' ...)` in the runner and the CI artifact; individual OS PIDs were not independently witnessed.

## 2. Artifact, exact-head CI and provenance

Original ZIP size **13,067 bytes**; independently verified SHA-256 **b6acf9c4c519d7f3826fcd501c622636ee67a937cdf41d6c0df5ded33e6db43b**.

| Exact original ZIP member | Independently rehashed SHA-256 |
| --- | --- |
| `inputs.json` (15,268 B) | `79be6692d8e107ed5fa2198abbcfe56a0fb97633aac55db573eec021ea37fc45` |
| `report.json` (222,131 B) | `bc0fee95fe8e0d61176aed8adf96081324cfa0ea1846caf1997e9fbc51570960` |
| `exact-reference.json` (60,752 B) | `9e3d386abceaa907063f0c01b3b40fc399e8a6e764da231a1959e6d24c1145ee` |

All three ZIP members match the extracted bytes. `report.provenance.inputsSha256` and `exact-reference.sourceReportSha256` correctly point to the original members. Using Node's `JSON.stringify(document,null,2)+'\\n'` and `JSON.stringify(native)` independently, **all 5 saved-scene SHA-256s and all 60 projected-native SHA-256 fingerprints matched**. Every row's case scene hash matches its own frozen input. The authored y-up polygons, source setups, native pin and case membership were inspected; these are **synthetic** cases, not five original textbook interpretations.

[Unified CI run 43854663361](https://github.com/physicsvigilante/opticsim/actions/runs/43854663361) was completed with conclusion **success** and `head_sha` equal to the exact source head. Its log reports **766/766 Node tests passed**, 60 native trials, the additional developer checker **87/87**, and the original ZIP upload ID **14220951106**. Querying the associated commit workflow runs returned **11 distinct workflows, 11 final success conclusions**. The report's `gitCheckout` **cd23c8066d8c6ccb27cba0ef9d4e723c36868bda** is GitHub's test merge commit with parents **base 50dd0f4... and head d8367c2...**; it is not an unexplained substituted research source. I did not claim to re-execute CI or to certify first-attempt results from unrelated prior workflows.

## 3. Single owning observer and experiment design

Exact-head `run.mjs` uses the existing `createNativeFiniteHitDiagnostic` and adds a wrapper **only around `finite.beforeIncident`**, copying the actual incoming native ray `p1`/`p2` and callback hit scalar values *before* delegating `original.call(this,id,ray,hit)` **once**. It does **not** assign another `Glass.onRayIncident` wrapper. The existing `observeInterfaceSet` in `src/planar-media.js` installs the sole per-instance native-calling Glass observer, invokes `finiteDiagnostic.beforeIncident` before the native mutation, and calls the pinned original `onRayIncident` via **one** `original.apply(this,args)`. The diagnostic's own `beforeIncident` only copies/counts and never calls native optics. The wrapper identity, source callbacks, detector counts, 128 cap, raw capture count, errors and terminal guards were inspected. Each of the **30 tapped rows** has callback count equal to the native Glass interaction meter, no capture faults, and **1–6** captures, all below 128. No ordinary ON row exports raw per-hit points.

**Important limit:** this verifies the static ownership/delegation pattern and matching *archived* counters, not independently instrumented native call stacks. There is still an **additional synchronous JS method wrapper and copying** on the hot path. It can perturb exact-critical execution. `ordinary-on` and `single-owner-tap` are separate executions, not identical-ray counterfactuals, and this study does not compare ordinary Stage-1 ON with unobserved bare native OFF.

I replayed xorshift32 + Fisher–Yates from **seed 0x9200a55**: all **60 scheduled case/block/slot/mode entries matched in order**, with three randomly ordered four-run blocks per case and **exactly two ordinary ON + two TAP per block**. All 60 rows match their scheduled ordinals and original case/hash; every published per-case/profile rollup and the three separately named top-level status aggregates were independently tallied.

## 4. Actual native trial states — no failed traces discarded

| Synthetic scene | Ordinary Stage-1 ON (6) | Single-owner TAP (6) | Observed Glass callback counts |
| --- | --- | --- | --- |
| Normal Glass with detector | **6 completed** | **6 completed** | 2 in every run |
| Critical −5° | **6 completed** | **6 completed** | 1 in every run |
| Translated computed critical | **3 completed / 3 failed** | **2 completed / 4 failed** | 3 completed, 4 failed |
| 37° rotated computed critical | **6 completed** | **6 completed** | 4, 5 or 6 in each profile |
| Critical +5° | **6 completed** | **6 completed** | 3 in every run |
| **All 60** | **27 completed / 3 failed** | **26 completed / 4 failed** | **53 completed / 7 failed** |

The **seven actual native failures** are row ordinals **25, 26, 28, 30, 33, 35, 36**, all translated critical. Each records the real interface error **"G1: native interface emitted nonfinite or indeterminate encounter evidence"**, 4 Glass callbacks, 5 processed rays and one invalid observer encounter. Only **3 of the 4** callbacks in each failed row have a qualified finite-face meter; the fourth is an invalid/ungrounded encounter. Their public advisory is correctly **suppressed / NATIVE_RUN_NOT_COMPLETE**, not clean. Completed translated runs have 3 callbacks and advisory **inconsistent**. All 60 checks confirmed no recorded truncation, undefined-behavior count, warnings, or setup/capture errors, but `report.errors:[]` is a **runner setup/invariant statement, not a claim that every native optical trace completed**.

**PR #91 F-01 aggregate regression: resolved in the NEW report.** The values under `ordinaryOnNativeStates` (27/3), `singleOwnerTapNativeStates` (26/4) and `allNativeStates` (53/7) arise from disjoint subsets and agree with every row and byCase rollup. The misleading `genuineNativeStates` key is absent. PR #91's separate original archived 120 OFF/ON + 12 SHADOW results and misleading historic aggregate remain untouched and must not be silently reinterpreted.

## 5. Independent all-87 original binary64 finite-hit recheck

For each **of the 87 original TAP hit records** (71 from eventually completed native runs, 16 from failed native runs), I reconstructed the four ordered **finite faces** from the corresponding saved polygon's x1/y1 ... x4/y4 and confirmed **120/120 archived authored face entries** (four per TAP trial). For intersection calculations I explicitly changed the authored **x-right/y-up** face coordinates to **native x-right/y-down**; the raw native p1, p2 and reported incident point were left in their original y-down coordinates. Every supplied hit is within **1e−5 mm of exactly one finite face**; largest independent residual was approximately **5.08423e−13 mm**.

The independently authored arithmetic reads binary64 bits directly, constructs one shared integer scale for all relevant coordinates, computes exact 2-D cross-product determinants and reduced rational t/u, compares `t > 0`, `0 ≤ u ≤ 1`, the exact represented native squared cutoff **1e−12** and exact P*–supplied-point equality using **integer comparisons**, not floating tolerances. It independently evaluates both reported and computed vertex clearance **0.01 mm**, unique segment membership **1e−5 mm**, and the conservative near-parallel sine guard **sqrt(binary64 epsilon) ≈ 1.49011612e−8**. Minimum nonvertex crossing sine in the original sample is approximately **5.96046448e−8**, so this guard does not suppress any of those samples. The near-parallel heuristic is **not** a validated incident-point uncertainty envelope.

| Independently recomputed category | Count | Evidence meaning |
| --- | ---: | --- |
| `checked`: exact finite-forward and exactly equal represented incident point | **12** | Checked **represented** values, not optical truth |
| `unknown`: represented forward geometry but P* differs from supplied native point, without an established error envelope | **56** | **Cannot certify or reject** point agreement |
| `inconsistent`: exact represented intersection is nonforward (`t ≤ 0`) | **15** | Recorded **binary64** line/finite-hit contradiction |
| `unknown`: native-reported hit within 0.01 mm of polygon vertex | **4** | Correctly withheld corner interpretation |
| **Total** | **87** | **Zero status/reason disagreements** with archived JS and Chat A Python reference |

For **all 83 nonvertex events** with archived t/u, both exact reduced numerator and denominator of **t and u** match the independently constructed integer-lattice values. There are **zero** per-hit classification, rational-parameter or face-ID mismatches; the four vertex-guarded events properly do not claim a t/u solution. All 30 tapped rows have retained original coordinates; no clean inference is drawn from failed native final states.

The **15 exact nonforward** events comprise **six translated-critical t = 0** at hit index 2 (rows 26, 28, 29, 32, 33, 36) and **nine rotated-critical negative t** events (rows 39, 40, 43, 44, 45, 46; some have two). For example, rotated row 39 hit 3 has **t = −635731093954651 / 1482881382794735452609**. **Eleven** nonforward captures came from subsequently completed native runs; **four** from failed runs whose public diagnostic remains suppressed. All four near-vertex unknowns are failed translated-critical TAP runs, hit index 3, with reported clearance approximately **8.74328e−5 mm** (well below the 0.01 mm exclusion).

These are rigorous **necessary inconsistencies between the finite intersection of the recorded represented binary64 lines and the reported native callback points**, within the specified diagnostic's geometric guards. They do **not** certify real-number critical Snell branching, a full reconstructed ray path, a validated root cause, point-error threshold or the same 15 events in ordinary ON trials. The `56 unknown` must not be relabelled either as successes or failures.

## 6. Independent first-event optics and detector controls

For explicit n_inside **1.6**, n_outside **1.3**, independently computed critical angle is **54.34091230386124°**. Across all **24 far-control rows** the first native finite-face encounter is **face-34**, from inside, with indices 1.6 → 1.3 and correct signed coordinate convention. At **49.34091230386124°** (−5°), all 12 first encounters are transmissions and the expected scalar Snell transmitted angle is **69.01292800507566°**, matching recorded within 1e−8 degree. At **59.34091230386124°** (+5°), all 12 first encounters are TIR. The 12 normal-control rows all report normal transmission and a real **D1** detector with exactly **one crossing and signed relative power −0.5**. The four critical/far scenes have **no detector**; no detector power can be inferred there.

The exact-computed-critical first-event outcomes and variable 4/5/6 downstream callbacks are **observations**, not a unique certified physical solution. Detector power here is sampled, signed, **relative** native output—not Watts, integrated Fresnel flux, continuous irradiance or image detection.

## 7. Findings, remaining risks and next narrow step

- **No R2 research-evidence blocker found.** ZIP/source evidence identity, aggregate labels, observed error semantics, single native-calling observer ownership, numerical exactness and far-angle first-event controls meet the requested bounded audit. The older PR #91 pooled-label F-01 is addressed prospectively without rewriting that archived first attempt.
- **Nonblocking terminology clarity (N-01):** the runner calls a field `nativeFaceVertices`, but its archived endpoints come from `polygonFaces` in **authored y-up** coordinates; only the ray/hit scalars are already native **y-down**. This reviewer explicitly converted the faces before every calculation. A *future test-only* version could name/declare the face coordinate frame unambiguously, without changing any original captured values or the current physical implementation.
- **Residual limits:** the 30 instrumented runs are not ordinary ON traces, the extra synchronous method work is not proven neutral, no original source/solution interpretation or held-out physics dataset was tested, and the `56 unknown` point agreements lack a justified conditioning-dependent numerical error bound. Completion is not numerical correctness; failure/suppression is real.
- **Smallest next step if stronger inference is needed:** preserve this exact original ZIP and the prior PR #90/#91 attempts; preregister a **separate research-only** study that characterizes observer/capture sensitivity and an independently justified point-disagreement uncertainty envelope, while retaining all failures and ordinary/TAP distinctions. Do not patch existing ZIPs or use this experiment to change Stage-1/Stage-2 qualification.

**Final verdict: PASS FOR THE OBSERVED R2 RESEARCH DATA ONLY. KEEP SOURCE PR #92 DRAFT AND UNMERGED.** A consequential production native numerical, ray-behavior, cutoff or Stage-2 withholding change requires a separately reviewed new source proposal, pinned genuine native evidence and explicit owner release approval. No source, vendor, historical artifact, central review request or PR state was modified by this review; this file is an independently authored append-only Chat B report.
