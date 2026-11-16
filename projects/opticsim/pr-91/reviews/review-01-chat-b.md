# Chat B independent R2 research-evidence review — Opticsim PR #91

**Verdict: PASS — FOR R2 RESEARCH EVIDENCE ONLY, NOT FOR PRODUCTION MERGE, PHYSICS CERTIFICATION OR STAGE-2 POLICY.**

**Reviewed source:** [Opticsim draft PR #91](https://github.com/physicsvigilante/opticsim/pull/91), exact head **6e374baf284ebab48d836260f1d96ef022508d40**; base/main **50dd0f4d9530d0a61bb4c7064c4326a8ac0ce518**; pinned native PhyDemo **811f508d2b070898c241a568b0c167dcb8645251**. Reviewed 2026-11-16. Source PR remains **DRAFT/UNMERGED**. This is a separately performed Chat B audit of the original bytes, not a relabeling of Chat A's Python checker.

## 1. What I actually did

- Read the hub protocol, risk policy, R2 request, exact-head AGENTS.md, both research scripts (run.mjs and exact-check.py), methodology, temporary workflow extension and relevant finite-hit/native-face implementation. Checked the pinned GitHub base-to-head comparison: **four changed files only** — research runner, exact-checker, methodology README and a disposable unified CI extension. **No production src/ or pinned native engine change.**
- Retrieved the **original** GitHub Actions ZIP [artifact 14216289446](https://github.com/physicsvigilante/opticsim/actions/runs/43849271999/artifacts/14216289446); independently SHA-256 hashed the ZIP and the three raw members before analyzing their JSON.
- Independently reconstructed the five scene hashes using Node JSON serialization, verified all 132 recorded native projections' SHA-256 fingerprints, and re-generated the 120-trial Fisher–Yates schedule from the stated xorshift32 seed. Inspected every row's schedule, frozen input hash, status, native processed and interface counts, available detector results and ON/OFF advisory; recalculated distributions without trusting the top-level summaries.
- **Independently recomputed all 40 SHADOW finite-line intersections** from raw native binary64 p1/p2/incident and the original authored polygon edges using a *separate integer-lattice algorithm*: read IEEE-754 sign/mantissa/exponent bits, map every coordinate to a shared power-of-two integer lattice, use integer cross-product determinants to derive exact rational t/u, then use integer comparisons for finiteness, forward direction, native cutoff and exact incident-point agreement. I did **not** execute or import Chat A's Python exact-check.py or the Opticsim JS audit function. Compared all 40 statuses/reasons and all available exact rational numerators/denominators to the original exact-reference.json.
- Independently calculated critical-incidence, transmitted-angle and TIR scalar controls. Inspected original GitHub CI run/job metadata and the first failed Chrome job log, plus the exact-head unified successful job log.
- **Did not rerun the pinned native engine, Node 24 test suite, browser, or 132 fresh-process trials** in this review environment. “New reviewer computations” refer to offline audit of independently downloaded original evidence; native-execution results and original CI were inspected, not executed anew. No Opticsim source, original ZIP, historical failure, PR state or source measurements were modified.

## 2. Evidence identity and original CI

Original ZIP SHA-256: **f0743e9301491227062ff9c8dd4f2391aab06e9f03a8ffc76247ed3cb4bcf8e9**.

| Original ZIP member | Verified SHA-256 |
| --- | --- |
| inputs.json | 32c7670fa8223324c691a059dda378f8a1a92e976e6a10f293960c5e4578e387 |
| report.json | 5d9c19789e527095e1e03efc48b348188d4cbc7f5a29b739934e6180401e8de2 |
| exact-reference.json | 306917c62e0a35722e84c74d79f02faed0698eeb7ff5b3185d069d70f612ae55 |

The archived report's source.commit is **29406503a5e53f0e52e1023d9495fe037bf0477c**. I verified via GitHub that this is the **synthetic pull-request merge-test commit**, with parents base **50dd0f4...** and exact research head **6e374baf...**; the associated workflow head_sha is the requested research head. It does **not** indicate a substituted source revision.

The exact-head [unified CI run 43849271999](https://github.com/physicsvigilante/opticsim/actions/runs/43849271999) passed on its first attempt; its log reports **766/766 Node tests, 120 ordinary native trials, 12 distinct SHADOW native trials, and the separate Chat A-authored 40/40 Python geometry checks**. All **11 distinct workflows** ultimately have successful conclusions.

**Preserved negative result:** [Planar browser workflow run 43849271747, attempt 1](https://github.com/physicsvigilante/opticsim/actions/runs/43849271747/attempts/1) **failed**, even though its 766 Node tests and planar native acceptance passed. The failing step was the Chrome browser startup: absent **DevToolsActivePort** before timeout. The **failed job alone** was rerun as [attempt 2](https://github.com/physicsvigilante/opticsim/actions/runs/43849271747/attempts/2), which passed at the **same head SHA**. Final 11/11 green is **not** first-attempt 11/11 green. No code alteration to obtain that rerun is visible.

The recorded full research ZIP is retained unmodified. The [separate access-controlled original archive](https://chatgpt.com/space/page_90379210155c8191b623a517b3b4b) is linked by the author, but I verified the original GitHub Actions artifact directly; I did not authenticate to the auxiliary Page archive.

## 3. Fixed scenes and randomized protocol

All five **fully authored v9 polygon-dielectric scenes** serialize to their saved hashes; all trial scene hashes match their parent. Original scene SHA-256 values:

| Case | Verified serialized scene SHA-256 |
| --- | --- |
| normal-with-detector | f47dae1a62b20b44e6725fc2f1666ab8b7effc480670bb3bef9873ed90d07c9f |
| far-below-five | e8bd9693e44cb124e0c0776f1635eb51f363c88cd47d400a1fb5c8534fcfa1c1 |
| critical-translated | 1bd5a3aaabe3f9f5cb2d45a2c296b70d78e4c7504975559a8a25c2bcd254f023 |
| critical-rotated37 | 0cb737c0670d19464771962c8c92451a05aeefc45a47dba6026094d8a78a9b7a |
| far-above-five | 613dc7d2c7389e40b18815c3a4ef50e59c27d9cbadc2dda9632eb0dd079f7760 |

Independent xorshift32/Fisher–Yates replay with **seed 0x90a112** matches **every ordered schedule slot and ordinal**: each case has **six blocks**, exactly **two OFF and two ON** randomly ordered in each block (12 per mode per case). The code invokes one child Node process per trial via execFileSync, and all 132 archived rows state new OS process. Direct OS process IDs were not archived/independently monitored; process independence is supported by the runner source plus original CI completion, not separately witnessed.

The final **12 SHADOW** rows are separately scheduled (four each for normal, translated critical and rotated critical), are **not randomized OFF/ON** and are not legitimate causal comparators. No change to optical values within a case was found, and no runner setup exceptions or missing trials were found.

## 4. Ordinary OFF/ON native evidence — recomputed from all 120 raw rows

**Exactly 106 genuine completed / 14 genuine failed.** Those 14 failures are **not** missing data or harmless setup failures: all occur in the translated exact-critical case and carry the native interface error “G1: native interface emitted nonfinite or indeterminate encounter evidence.”

| Synthetic scene | 12 OFF records | 12 ON records | Native measurements / advisory |
| --- | --- | --- | --- |
| Normal, actual detector | 12 completed, 2 Glass hits each | 12 completed, 2 hits each | Each mode: 4 processed, detector D1 one crossing, signed **relative** power **−0.5**; ON 12 checked |
| Critical −5° | 12 completed, 1 Glass hit each | Same | 2 processed; ON 12 unknown |
| Critical, translated | **5 completed / 7 failed**; 3 hits when completed, 4 when failed | **5 completed / 7 failed**; same hit counts | 4/5 processed respectively; ON 5 inconsistent, 7 suppressed |
| Critical, rotated 37° | 12 completed; hit counts **4:9, 6:3** | 12 completed; hit counts **4:6, 5:3, 6:3** | 5/7 vs 5/6/7 processed; ON 12 inconsistent |
| Critical +5° | 12 completed, 3 hits each | Same | 4 processed; ON 12 unknown |

The originally archived ON and OFF **projected native-result hashes** match in the stable cases and share the same translated-critical state frequencies. The rotated distribution differs. **Neither equality nor difference of separate-run distributions proves observer neutrality, interference or causality.** These are different ray objects and native runs, notwithstanding the balanced design.

**Nonblocking reporting defect (F-01):** The top-level field **genuineNativeStates** in run.mjs is calculated from **all 132 rows**, including 12 SHADOW rows; its saved tally **117 completed / 15 failed** is **not** the genuine OFF/ON total. The genuine-only result is **106/14**, correctly recoverable from individual records and per-case ordinary summaries. This is a **misnamed/pooled presentation aggregate** and must never be quoted as the ordinary-trial outcome. In any future revised runner, compute that field from ordinary rows or rename it to allNativeStates; **do not rewrite the original ZIP or silently change these first-attempt data**. The contamination does not enter the per-mode frequencies above or invalidate the archived row-level evidence, but it warrants explicit correction before reusing the field.

## 5. Independent scalar optical controls

For high-index to low-index transfer, inside **n=1.6**, outside **n=1.3**: critical angle **asin(1.3/1.6) = 54.34091230386124°**. Both frozen far-control scenes have a first interaction on the actual finite **face-34**, from **inside**, with correct y-up authored to native y-down conversion.

- At **49.34091230386124°** (critical −5°), expected transmitted first event, with independently calculated refraction angle **69.01292800507566°**; archived native first-event angle **69.01292800507557°**. All 24 OFF/ON rows agree with transmission.
- At **59.34091230386124°** (critical +5°), expected total internal reflection; all 24 OFF/ON rows report TIR.
- Normal-incidence control shows transmission and one detector crossing of **−0.5 signed relative power** across every OFF/ON run. **Only** the normal case has a detector: no detector-power conclusion is available for the critical scenes.

No unique native branch is adjudicated at the mathematically exact critical boundary; far-angle scalar controls do not certify full multiple-bounce ray trajectories or Fresnel power.

## 6. Independent original-binary64 SHADOW audit

The research SHADOW mode installs **one extra native-calling Glass.onRayIncident wrapper before the existing Stage-1 owner**, snapshots original raw p1/p2/incident scalars and calls its saved original via **one** apply invocation. The owning observer still runs; code and recorded callback/interface counts show no missing calls in these 12 runs. Its cap is **128** callbacks per trial, but only **40** were captured in total, with **no capture exceptions or cap overflow**. SHADOW outcome is **11 completed / 1 failed**. Its wrapper can alter numerically sensitive execution: **do not pool it with ordinary ON or OFF or infer identical ray history**.

I reconstructed native y-down edges by negating authored polygon y coordinates and confirmed **every archived nativeFaceVertices point** equals the frozen v9 source polygon's ordered edges. Every reported hit was grounded within **1e−5 mm** of exactly one finite source edge; largest measured distance was approximately **5.08e−13 mm**. The face is reconstructed from the compiler contract and frozen scene; a second, independent per-execution native Glass.path dump was not preserved.

For each of the **40 actual original scalar captures**, my distinct bit-decoding/integer-determinant computation agrees with the archived checker on **classification and exact available rational t/u numerators and denominators**, with **zero disagreements**:

| Exact represented-geometry classification | Count | Appropriate interpretation |
| --- | ---: | --- |
| Exact finite-forward and exact incident-point agreement | **8** | Checks the represented event only |
| Finite-forward geometry but supplied point differs; no validated point-error envelope | **21** | **UNKNOWN**, not a proven error or pass |
| Exact represented intersection is nonforward | **10** | **INCONSISTENT** for recorded binary64 ray/face |
| Reported native hit within 0.01 mm of a vertex | **1** | **UNKNOWN** corner ambiguity |

More specifically, the **four translated-critical nonforward** records (ordinals 125–128, hit index 2) have **exact t=0**. The **six rotated-critical nonforward** records include negative t values of approximately **−4.2871e−7** and **−2.8951e−7** (e.g. ordinal 129, hit 3: **−635731093954651/1482881382794735452609**). These are real comparisons against **represented** ray endpoints, not proof of a unique physical cause; very small endpoint perturbations can matter near exact critical incidence.

The single near-vertex case is **ordinal 125, hit 3**, about **8.74e−5 mm** from the vertex, correctly left ambiguous under the 0.01 mm guard. The minimum computed nondegenerate ray–edge crossing sine among the other samples was approximately **5.96e−8**, above the current sqrt(binary64 epsilon) heuristic (**1.49e−8**), but this heuristic is **not** a validated geometric uncertainty/error bound. No claim about sensitivity under upstream rounding or universally reliable incident-point agreement follows from these checks.

**Important attribution limit:** all 40 raw per-hit coordinate snapshots came **only** from SHADOW, not from genuine OFF/ON records. Thus, the exact 10 SHADOW contradictions **cannot be asserted to occur on every ordinary ON run**, nor can their incidence be used for a treatment-effect estimate. The 40/40 agreement between Chat A's two implementations was not itself independent review; the independently authored integer-lattice recheck above is what this report adds.

## 7. Sufficiency by evidence dimension

| Dimension | R2 research-only assessment |
| --- | --- |
| **Interpretation fidelity** | Synthetic authored scenes and physical parameters are retained exactly; **no** held-out original textbook-question interpretation or answer accuracy tested |
| **Represented finite-forward ray geometry** | **Supported for the 40 preserved SHADOW observations**, including explicit unknowns and contradictions; does **not** certify default ON/OFF events or ideal native physics |
| **Native execution status / coverage** | Complete 132-record audit, with real **106/14 ordinary** outcomes and **11/1 shadow**, plus first-event controls; failed cases remain failed |
| **Evidence integrity / reproducibility** | ZIP and three files rehashed, all five scene hashes and 132 native projection hashes verified; seeded schedule replayed and 40 exact rational calculations independently repeated. No fresh native replay or independently captured process IDs in this review |
| **Teaching usefulness** | The opt-in diagnostic may help identify suspect demonstrations, but its correctness, classroom usability, image formation, and textbook-answer completeness remain **unproven** |

**Verdict rationale:** There is sufficient original, pinned and independently rechecked numerical evidence to accept the **bounded descriptive R2 research finding**, including **10 represented nonforward SHADOW intersections**, the OFF/ON run variability and the explicitly incomplete outcomes. The misleading pooled **genuineNativeStates** field is a concrete **nonblocking reporting defect**, not evidence that the per-mode comparison was pooled. There is **insufficient evidence** for any causal observer-effect, production native geometry fix, universal threshold, automatic measurement withholding, Fresnel/Watt/illumination/image claim, or claim of source-authentic teaching success.

## 8. Smallest next verification and release hold

If future work seeks evidence for *ordinary* Stage-1 numerical behavior, acquire original per-hit binary64 coordinates **within the existing single owning Stage-1 observer** in a separately identified research-only trace, without adding a second native-calling wrapper, and compare its complete projected native outputs and input hashes against existing genuine ON behavior. Label any added capture as a **new experimental profile**, and preserve this first original ZIP. That alone still cannot establish causality; a separate, controlled counterfactual design and conditioning/error-bound study are needed before stronger claims. Correct F-01 only in new future reports/source, not by modifying original artifact bytes.

**No source edits, native algorithm changes, Stage-1 canonical measurement changes, Stage-2 mandatory withholding, workflow-to-main merge, or source PR #91 merge are authorized by this PASS.** Keep PR #91 **DRAFT/UNMERGED**; its research-only workflow extension is disposable. Any production physics, measurement or withholding proposal needs its own owner decision, pinned evidence, R2 review and release gate.
