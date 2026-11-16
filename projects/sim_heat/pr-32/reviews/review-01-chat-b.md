# SIM_HEAT PR #32 — independent Chat B R2 review (reference reproducibility)

**Outcome: PASS — STRICTLY SCOPED to the accurate forensic capture and scientific assessment of an actually FAILED reproducibility experiment.** The original PR #31 checking-reference seal is **NOT bitwise reproduced** by the two new host environments. The cross-host/reference-certification gate remains **FAIL / HOLD**. The exact-head diagnostic CI's success is a **diagnostic success only**. This verdict does **not** authorize a reference-identity exception, native F-02 execution, production merge, or any tolerance change.

## Identification and review boundary

- **Project:** physicsvigilante/sim_heat; [draft source PR #32](https://github.com/physicsvigilante/sim_heat/pull/32), historical F0 experiment, not production main.
- **Exactly reviewed source HEAD:** [502a6e8c392d8b8cfb8a4361cddcae4fafff6f01](https://github.com/physicsvigilante/sim_heat/commit/502a6e8c392d8b8cfb8a4361cddcae4fafff6f01); **source tree** ef08c7029975c7e3c224c6a13d9c5663986604b8.
- **Immediate reviewed base:** d857c8e807612026ecdf624277b4ace3977fefe3 (PR #31); original F0 implementation dd8c9432abe97563414bb3ed809e61e673473812.
- **Reviewer/date:** Chat B, separate ChatGPT conversation (GPT-6), 2026-11-16 UTC. Separate context is not proof of distinct model weights, independent human adjudication, or authenticated laboratory hardware.
- **Risk/scope:** R2; offline reference reproducibility, archived integrity, physical/numerical error bounds, provenance and gate interpretation. No OpenModelica, native MAT output, full project rerun, or browser/classroom evaluation.
- **Source modifications:** NONE. This newly authored central review report is the only requested GitHub write. No historical reference, task, source, evidence, PR, or tolerance was modified.

Read the [central protocol](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md), [R2 policy](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md), review template, original F0 task and [frozen authoring contract](https://github.com/physicsvigilante/sim_heat/blob/ea954eee9b416498874419b9c8e5503f94821be8/qualification/h1_c1/AUTHOR_CONTRACT.md), PR #31 independent Chat B review, and the exact-head added code/workflows. No AGENTS.md exists in the complete exact-head source tree; none was substituted from floating main.

## Findings

### F-01 — VERIFIED PASS (scope/integrity): exact-head addition-only change and original 80× failure preserved

GitHub base-to-HEAD comparison shows **seven added paths, 995 inserted lines and zero modifications/deletions**: two offline workflows, two comparators/diagnostics, one provenance collector, and two scope/findings documents. The original F0 code, first-authored model/study, source task, V2 preparer, H1 verification/runner, old native plan, checking specification, and historical failures are unchanged. Independently compared complete archived source SHA manifests: **117 of 117 common PR #31 files are unchanged** at the failed two-host ancestor; its four additional paths are additions. The remaining three files were added later through the exact reviewed head. Both host jobs also recorded 14/14 original F0 frozen-pin checks; the original preparer explicitly checks the 23 native-plan source hashes (those pin checks ran in CI, not as a separate local 23-file rehash).

Directly downloaded the [original F0 artifact #14238243398](https://github.com/physicsvigilante/sim_heat/actions/runs/43895266125/artifacts/14238243398): ZIP SHA-256 **754e35a1143c2d0f08b38f826a2104a58e1c345a7ac1491b18dad7cb03354107**, valid CRCs. Saved bundle raw SHA **770a5422727f3678a07e9dfa201ad88dd85669ad9f01b045b84dad059b433276**; independently recomputed canonical seal **d76c98f37a0629b56d977c960d1e75694e1121832a9d5281f68bb972d31a365b**. Its stored hotLead.G is 0.44999999999999996 W/K, giving an independently recalculated reference-error/native-allowance fraction **0.0125**, hence **80× rather than required ≥100×**: ORIGINAL **FAIL**, not retroactively repaired.

The PR #31 V2 bundle separately stores 0.45 W/K, with fraction **0.003125** and **320×** static margin, under the same allowance. The unchanged coldLead.G = 0.39999999999999997 W/K has **0.009375** error/allowance (**106.6667×**), close to the 0.01 strict cutoff. This is a frozen-reference sensitivity worth retaining in future gates, not grounds to adjust tolerances.

### F-02 — VERIFIED NEGATIVE (major evidence finding): two hosts reproduce one another, NOT the PR #31 archive

Directly downloaded GitHub's **original saved artifacts**; all whole ZIP SHA-256 values match the recorded values and all ZIP entries pass CRC:

| Artifact | Archived CI run, source | Independently verified ZIP SHA-256 |
|---|---|---|
| [PR #31 original V2 #14249313720](https://github.com/physicsvigilante/sim_heat/actions/runs/43915934653/artifacts/14249313720) | #43915934653, d857c8e… | d9259837e0e03c70989b50b2c9dcbf13aca260da4d1cb0ae000b2a23ef65732e |
| [Ubuntu 22.04 #14254152610](https://github.com/physicsvigilante/sim_heat/actions/runs/43921113470/artifacts/14254152610) | #43921113470, 86cbe18… | d5dbad4b0da3a700e8ad8f22b4b61f0618485b1d46289f739151c71f416737c4 |
| [Ubuntu 24.04 #14254052553](https://github.com/physicsvigilante/sim_heat/actions/runs/43921113470/artifacts/14254052553) | #43921113470, 86cbe18… | 8821f29d1f63764a4cb03e4598eda60e70a2bd0b7e2ea91936613aefaf05a4b7 |
| [Original cross-host refusal #14252364840](https://github.com/physicsvigilante/sim_heat/actions/runs/43921113470/artifacts/14252364840) | #43921113470, 86cbe18… | 516824ae5432d5d484d13a285dcc81f842226a7e022f9793de1d23fd1c3c2401 |
| [Initial forensic #14255040340](https://github.com/physicsvigilante/sim_heat/actions/runs/43921830450/artifacts/14255040340) | #43921830450, f91a7b8… | 892df4986191246bf9d37dd3326bd3de28db5181ae9ede08f5ddcecb809c6f75 |
| [Final exact-head forensic #14253809455](https://github.com/physicsvigilante/sim_heat/actions/runs/43922852455/artifacts/14253809455) | #43922852455, 502a6e8… | 448e3096f809fd773ef1ebf9d6e3f62510abbe375e6e2caa6652d60394d2616c |

Independently hashed and recalculated canonical JSON (all top-level fields except the seal, sorted keys/compact separators):

- **Previously reviewed PR #31 V2:** raw SHA 0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368; canonical seal **d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9**; F0-reprepared parent **d76c98f37…**.
- **All four fresh-process V2 bundles** (two processes per Ubuntu version), including both in-process repeats: same raw SHA **456b82081aa97b59f55e86830ddabfc36f14fd74991542e350a2266e0f9962f5**, valid canonical seal **c30e8783d39c7b0198c1adf0273ac84568f698f08287f02bf79eeed224830b07**, new F0-reprepared parent **e92e1a00d9c45d4bb91f458f3750ba189f117fcdecd8b56c693e0fc57476d2cb**.
- **Between the two newly hosted bundles:** 0 differing JSON leaves, zero raw-byte difference. **Between either new hosted bundle and the reviewed original V2:** 112,049 differing JSON leaves and distinct raw/canonical identities. Never alias, reseal, or accept one as the other.

GitHub run #43921113470 is independently confirmed **completed/FAILURE**. All three relevant jobs failed their **intended original-seal assertion**, while retaining full bundles, reports and refusal receipts; no new candidate was accepted. The standalone comparator records the reason on both hosts: “V2 seal not equal to original independently reviewed candidate.” The exact-head #43922852455 is **completed/SUCCESS only for forensic capture** and explicitly reports status CAPTURED_REVIEWED_V2_SEAL_DRIFT__CERTIFICATION_HOLD, referenceCertifiableByThisReport=false, nativeExecuted=false and nativeQualified=false. A green diagnostic **must never be used as a passing bitwise/certification gate**.

### F-03 — VERIFIED PASS (numerical/physics, sampled only): independently checked strict 100× budgets

I independently parsed the **original complete saved JSON** and counted each differing leaf; no project comparison code was imported. The 112,049 leaf differences break down as: **83,077 samples across 26/37 columns; 13,445 samples across 4/4 integral histories; 15,485 quadrature-allowance leaves; 5 derived ordinary allowances; 5 scales; 31 method-metadata leaves; and 1 seal**. The physical specification and its independently recomputed fingerprint **3afcfddb28ddbf9f9266548504bb43fc2f5420e90d10cb4acbf87334c6e3ab4c**, time grid, units, owners and temporal policy are identical. The unchanged task is the two thermal buffers (125 and 180 J/K), hot/cold baths, and four correctly oriented rods (0.45, 1, π/10, 0.4 W/K). No changed physical law/source or unit convention explains the changed fingerprint.

**Independent computation, not copied diagnostic flags:** From the pinned original Stage-1 physical SI facts I independently implemented a separate **85-decimal-digit two-scalar modal-coefficient analytical solution** of the coupled energy balances, with analytical heat-flow integrals, not the repository's matrix spectral-projector code. I compared **every 37×4001 = 148,037 saved scalar** and **every 4×4001 = 16,004 saved integral** against the physically derived values for **each of the two distinct saved V2 identities**, using the unchanged reference limit = original native allowance/100 for scalars and (0.001 J + 0.000001×integral scale)/100 for integrals. All passed.

- Max *true reference error / native allowance* was **0.009375** for **both** V2 identities, at coldLead.G; limit **0.01**. The two independently derived decay rates are approximately -0.002761501788087817373 and -0.020874879364556124572 s⁻¹. No tolerance changes.
- Max *true integral error / existing strict 100× integral budget* was **9.802944218813159e-5** for archived PR #31 and **1.0303071512813997e-4** for the newer host result; limit **1**. These are sampled, finite-grid checks, not interval proofs or native observations.
- Independently compared all **148,037 old-vs-new scalar values** using min(old allowance, new allowance): maximum drift/native allowance **2.406978427913137e-7** (rightBuffer.dU, index 3875; absolute **9.822542779147625e-10 J**); limit for a strict 100× *reference* budget = **0.01**.
- Independently compared all **16,004 old-vs-new integral values** using the conservative min of the two existing integral-history scales: maximum drift/existing 100× integral budget **8.823332004711584e-5** (leftBuffer.Q_in, index 3913; absolute **5.02222974319011e-9 J**); limit **1**.

The conservative between-reference comparison is useful to quantify drift but **does not by itself prove either reference correct**; the independently evaluated physical solution above, and the separate saved PR #31/new-host high-precision reports, supply stronger bounded accuracy evidence. Both V2 identities are numerically defensible as **distinct** checking-only artifacts. The old F0 identity is *not* within strict 100×.

### F-04 — VERIFIED PASS (provenance with limitations): captures actual loaded runtime, not a proven drift cause

Read the **original** host runtime.json, wheel manifests, installed WHEEL/RECORD identities, process logs and original GitHub job-step results. Both used Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0 and threadpoolctl 3.6.0; the four wheel archive digest/filename manifest lines match exactly between hosts (manifest SHA **0069c38244c1ac061c85549441d7483bbe9a49f5905fbb394f10e5b1848ce5e0**). Local-install-from-download and pip-check succeeded per original job logs; the actual downloaded *wheel archive bytes* were not independently downloaded again in this review.

The loaded runtime capture reports **NumPy and SciPy OpenBLAS 0.3.30**, Haswell dispatch, pthreads and four threads for both. Ubuntu **22.04.5**, hosted image **20261111.360.2**, reported CPU **AMD EPYC 7763**, differs from Ubuntu **24.04.5**, hosted image **20261111.370.1**, CPU **AMD EPYC 9V74**. Host labels/CPU data are recorded runner claims, not hardware attestation. Original reviewed PR #31 lacked equivalent actual loaded BLAS/CPU data. **The cause of PR #31-versus-new float64 drift remains unknown**; neither the OS nor BLAS can be singled out causally from these artifacts.

The fresh-process comparator's original saved receipts include four negative mutation cases: lower-neighbor static G, a modified dynamic temperature, a changed flow integral, and widened allowance. All four changed bundle seals; the first three independently failed the source's high-precision checker; allowance widening was correctly only seal-tested (high-precision result not claimed). These **CI-observed controls** were not separately rerun with the repository code by Chat B. Relevant entrypoints explicitly refuse optimized Python; original jobs used non-optimized **python -B**. Individual diagnostic workflow shell assertions would still be weakened by an unsupported **-O** invocation, so treat this as a pinned-CI property, not a general assertion-independent security guarantee. No demonstrated defect under the tested invocation.

### F-05 — MAJOR OUTSTANDING GATE (not a defect in this diagnostic): generator reproducibility is NOT established

New hosted outputs match across these tested two OS images/processes, but **both differ from the pre-existing independently reviewed original**. The older unexplained failed prior-seal attempt had no alternative saved digest; this experiment does not reconstruct it or establish root cause. The failed two-host job is correctly red. A bitwise-deterministic V2 *generator* is therefore not currently certified. Any gate that explicitly promises “regenerate the reviewed SHA on arbitrary approved hosts” remains unfulfilled. Evidence of very small numerical drift does **not** license replacing the approved archived identity, silently rewriting checker pins, or accepting a modified reference.

This is a **certification/release HOLD**, not grounds to label the deliberately negative forensic experiment as an implementation failure. Preserve PR #32 as draft/unmerged and maintain all original results.

## Forward scientific disposition — one immutable fixture vs deterministic generator

**Recommendation: Option A is scientifically defensible and the smaller next step, conditional on a separate explicit owner/independent R2 disposition.** A verified numerical *reference artifact* need not have a bitwise-portable numerical *generator* to be a rigorous frozen checking comparator. The already archived, independently checked **PR #31 V2 bundle** can be proposed as the **sole immutable, SHA-pinned checking input**. Its mathematical evidence, physical provenance and numerical tolerance checks are strong at the sampled times. This decision would **narrow the claim from deterministic regeneration to faithful consumption of an exact saved artifact**; it must *not* reclassify failed regenerations as passes.

Prerequisites before any certification/consumption: (1) owner explicitly approves a revised, narrowly scoped immutable-fixture reference contract after independent review, retaining the full failed-bitwise record; (2) preserve the original archived PR #31 bytes **durably beyond GitHub Actions' 90-day retention** and authenticate both raw SHA and canonical seal, source/spec fingerprint, provenance, schema, 4001-grid, 37 channels, units/owners, 4 integral histories and unchanged allowances on every load; (3) the checker/any eventual new native plan must bind to **that exact already-verified reference**, not rerun the drift-prone preparer or accept either identity interchangeably; (4) retain the strict frozen 100× proof, the original F0 80× FAIL, no tolerance waiver and the coldLead.G narrow-margin warning; (5) separately review/authorize a new F-02 native one-shot source/host/plan, then assess actual native traces against the sealed reference. No such policy, canonical-fixture promotion, durable storage or native gate is approved by this review.

**Option B (new deterministic generator) is necessary only if the owner requires bitwise reproducible generation of the reference as a contractual feature**, e.g. reproducible builds/portability instead of immutable-fixture consumption. Then a deliberately specified arithmetic/serialization/rounding pipeline, newly versioned reference lineage and fresh independent physical checking and cross-host R2 evidence would be required. Pinning package versions and observing two matching hosts here does not prove that property; a cosmetic seal normalization/rounding shortcut is unacceptable. Do not delete or overwrite either historical reference.

## Independently performed work vs inspected evidence

**Personally performed offline:** downloaded and SHA-256/CRC-checked the actual seven listed artifact ZIPs; independently recomputed old F0, PR #31 V2, and both new-host canonical reference seals, their raw hashes and repeat identities; independently diffed complete JSON trees and all 148,037+16,004 old/new numerical points; independently solved the two-thermal-buffer system at 85-digit precision for **both** V2 reference identities over their entire 4001-point saved grids; verified exact rational/IEEE-754 static margins; compared archived source manifests and exact GitHub PR/commit diff. Reviewer-side scripts were local-only and not written into SIM_HEAT.

**Inspected original CI rather than rerun:** actual hosted operating-system packages/BLAS and provenance recordings, 14 original pin checks, original preparer's 23 source pin assertions, four original mutation controls, exact GitHub job-step outcomes, archived self-reports and workflows. No virtual environment/wheel install, new checking-reference preparation, model compiler query, OpenModelica build, native launch, or physical measurement was performed in this review.

## Separate scope judgments

| Dimension | Scoped judgment | Basis |
|---|---|---|
| Original source interpretation fidelity | **PASS, unchanged** | Original Stage-1 SI givens, two-body/four-rod topology and orientations match unchanged spec; 7-path addition-only diff |
| Physical/numerical checking correctness | **PASS, at saved 4001 samples only** | Independently recomputed all 37 channels and four integral histories on both V2 identities under frozen strict 100× budgets |
| Archived identity/integrity | **PASS for individually distinguished archives** | Actual downloaded ZIP SHA/CRC, raw bundle SHA, recalculated canonical seals; original 80× F0 failure preserved |
| Bitwise generation of previously reviewed V2 | **FAIL / HOLD** | New host bundles equal each other, but differ from PR #31 V2 raw/canonical identity |
| Evidence/provenance and forensic scope | **PASS with limits** | Actual OS/BLAS/wheel records and proper fail-closed two-host outcome; prior-runtime root cause unresolved |
| Native simulation and nine public observations | **NOT TESTED / HOLD** | Zero OMC calls/builds/launches; original nine requests remain not_computed in saved original admission |
| Teacher-facing usefulness | **UNKNOWN** | Original task has meaningful sign-reversal teaching intent, but no native curves or classroom assessment |
| Textbook-answer completeness | **NOT APPLICABLE** | Original independent illustrative task, not a textbook-answer audit |

## Release advice

**Scoped PASS for PR #32's archived negative forensic evidence and quantitative interpretation at exact SHA 502a6e8…. NO PASS for cross-host regeneration of the PR #31 seal, reference promotion, F-02 native, or merge.** Keep the historical PRs draft/unmerged. The smallest next action is a separately reviewed, owner-authorized **immutable-checking-fixture policy/retention/consumer-pinning decision** (Option A), or a separate explicitly deterministic generator milestone only if that stronger property is required. A successful diagnostic job must not be reused as a reference-certification or native release check.
