# Independent Chat B R2 numerical research/evidence review — Opticsim PR #97

**VERDICT: PASS — FOR BOUNDED NUMERICAL RESEARCH/EVIDENCE ONLY.** This is **not** an approval of native optical physics, a numerical tolerance or point-error envelope, observer causation, a production release, Stage-1 or Stage-2 policy changes, or the disposable workflow. **KEEP PR #97 DRAFT AND UNMERGED.**

**Date:** 2026-11-16. **Source:** [draft Opticsim PR #97](https://github.com/physicsvigilante/opticsim/pull/97), exact source head **760473cafceb70c055bb7c13b138a16c5e4d7620**, base/main **50dd0f4d9530d0a61bb4c7064c4326a8ac0ce518**, pinned PhyDemo **811f508d2b070898c241a568b0c167dcb8645251**. Scope: central [request](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-97/REQUEST.md), [protocol](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md), [risk policy](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md), and earlier [independent PR96 research review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-96/reviews/review-01-chat-b.md).

## 1. Independent work and limits

I used the connected GitHub account to download the **three original GitHub Actions ZIP archives** (PR96 original plus both PR97 originals), not Chat A's private Pages replicas, and computed whole-ZIP and every-member SHA-256 in a separate local container. I inspected the complete original five-file PR97 change, the prior frozen protocol, production/native observer source, pinned upstream geometry, job-step outcomes, exact-head workflows and prior review boundaries.

I implemented **a new integer/dyadic binary64 finite-segment audit** over all 44 original corrected-run TAP-archive callbacks: decode IEEE-754 signs/exponents/mantissas, form a per-event common power-of-two integer coordinate lattice, calculate exact cross products, rational ray t and edge u, exact point comparison and exact squared-cutoff test. The program does **not** import or execute Opticsim's JavaScript audit or the developer's Python Fraction audit. A separate new Node reconstruction of pinned PhyDemo's *global-coordinate binary64* determinant and forward/finite-segment/cutoff predicates independently checks the recorded rounded native point. Node also recomputed all **96/96 native-result fingerprints** from the two original JSON reports; all match.

**Execution boundary:** I did **not** rerun PhyDemo, Chrome, or the 96 original Node subprocesses. Native execution facts are those retained in original CI reports, GitHub job steps, and intact artifacts. This is an independent **offline original-byte and numerical replay**, not independent new native execution or recovery of any pre-JSON in-memory signed-zero bits.

## 2. Source freeze and preregistration

GitHub reports the protocol commit [c32c2e1](https://github.com/physicsvigilante/opticsim/commit/c32c2e1ffbe849a54416df2ce25775cc746ea39d) at **2026-11-16 13:34:32 UTC**; the first PR97 research workflow began **13:39:33 UTC**. Frozen protocol blob **c3fbe3752af228f817a2fd816a8f596a564f88e5** remains identical at reviewed head. It fixed **two** original PR96 nominal-critical synthetic cases, six balanced randomized blocks per case, four modes, seed **0x9700A55**, and **48 separate fresh-process positions**.

GitHub's [PR #97 diff](https://github.com/physicsvigilante/opticsim/pull/97/files) contains **exactly five added research-only files, 585 additions and zero deletions**: a disposable workflow, preregistration PROTOCOL.md, README.md, run.mjs and exact-check.py. No production **src/**, vendor PhyDemo, scene schema, Stage-1 canonical measurement, Stage-2 withholding, UI, cutoff or native ray algorithm changed. The [first trial head](https://github.com/physicsvigilante/opticsim/commit/9df7bea7d5b18ec63a0cc2f82c0c83d5163d6a3b) to [corrected head](https://github.com/physicsvigilante/opticsim/commit/760473cafceb70c055bb7c13b138a16c5e4d7620) GitHub comparison changes **one line only**, the test Python default input directory. The source runner, scheduled cases, protocol and native setup did not change after the first observations.

All six original PR96 serialized documents rehash to their saved scene hashes. The **two selected** originals are:

| Case | Verified original serialized scene SHA-256 |
| --- | --- |
| critical-shift-neg | 4389fecfe80ad01fa7cb160f22319327ccf9e30bb35c211012cc15599ff422c6 |
| critical-tilt-p14-shift | a47cb0aee2da8693fa4934bf17e0d26f8f96ee2b4fccce039f706ed6f60328b1 |

The original **19,205-byte** PR96 inputs.json SHA-256 is **caa07af040d0a71b50ea6b69470aa55a545b04d52195994913123a902b434df3**. Its bytes are equal to **both** PR97 archives' original source member and **both** newly copied trial inputs.json members. No source physical case was rebuilt.

## 3. Original ZIP and member verification

Every reported value below was independently rehashed from the exact downloaded ZIP bytes.

| Original artifact ZIP | Bytes | SHA-256 |
| --- | ---: | --- |
| [PR96 14229080814](https://github.com/physicsvigilante/opticsim/actions/runs/43872962563/artifacts/14229080814) | 12,217 | 467b548edbcdfc8cf4aecdab416d134d3ac703572a4e0330a4379fcb28df9929 |
| [PR97 first 14229538642](https://github.com/physicsvigilante/opticsim/actions/runs/43877888781/artifacts/14229538642) | 21,080 | d4929a2d837a6f2d42df17be150145e37bfe312297eea41f36713de7022071c3 |
| [PR97 corrected 14230677949](https://github.com/physicsvigilante/opticsim/actions/runs/43878097648/artifacts/14230677949) | 23,246 | a6bae60306f4a0730f4cae021b86a46b534d65736de2cb381f24c507d3eaa22e |

**Independently verified original individual member hashes** (duplicated original PR96 members are byte-identical in the two PR97 ZIPs):

| Member | Bytes | SHA-256 |
| --- | ---: | --- |
| PR96 inputs.json / each PR97 source and copied inputs.json | 19,205 | caa07af040d0a71b50ea6b69470aa55a545b04d52195994913123a902b434df3 |
| Original PR96 report.json / each PR97 source-pr96-original/report.json | 120,930 | 9324aabab62a2ab0e3636c30dec2154e590daf7c90304e8aeafa564e41250698 |
| Original PR96 exact-reference.json / each PR97 source-pr96-original/exact-reference.json | 23,826 | 497d2e568ca851dd98941be38ccd54b7473953b56405b653771f784633808f12 |
| First PR97 research report.json | 153,711 | 9fd6e67bc28a6c3a463ee0eb75f2c68e12bc923a54d3c05c350504c19b4a93af |
| Corrected PR97 research report.json | 154,974 | 7826d3983853e769cf42375fdb58f3623f93265c51ab71be89985651e27253a3 |
| Corrected PR97 exact-reference.json | 30,058 | 4bfcd144c10baa2c6d1bbfeabea372a15869b3bfef79713fdb76295882bc3142 |

The corrected exact-reference.json cites **7826d398...** as its input report digest, matching my direct hash. The first PR97 archive **does not contain a completed Python exact-reference**. GitHub's [original first job](https://github.com/physicsvigilante/opticsim/actions/runs/43877888781) confirms step 8 (48 native process trials) **SUCCESS**, step 9 (Python audit) **FAILURE**, and always-upload step 10 **SUCCESS**. This is an **overall failed workflow**, not an absence of genuine native trials. Corrected [run 43878097648](https://github.com/physicsvigilante/opticsim/actions/runs/43878097648) shows all three steps SUCCESS. GitHub lists exactly **12/12 success-conclusion workflows associated with head 760473c**, including 11 ordinary checks and the one disposable research action. For pull_request actions, the recorded GITHUB_SHA inside the JSON is GitHub's test-merge checkout (corrected run **3da728a0f0c4e23fd80b7be860adf044f492d9cc**), not a claim that production main merged this draft.

## 4. Forty-eight scheduled original positions in EACH run

I independently regenerated xorshift32 and Fisher–Yates from **0x9700A55**, using two fixed case IDs × six blocks × four disjoint modes. **All 48/48 original positions, case IDs, blocks, slots, scene hashes and row ordinals match in BOTH reports.** Both have 48 records, zero missing/runner-level error rows, zero callback faults, zero truncation and no warnings. Each report says its subprocesses are fresh Node OS processes, consistent with [run.mjs](https://github.com/physicsvigilante/opticsim/blob/760473cafceb70c055bb7c13b138a16c5e4d7620/evaluation/repeated-critical-profile-controls-v1/run.mjs) spawning a separate Node child for each scheduled slot.

Every failed row in both original reports retains the diagnostic error **“G1: native interface emitted nonfinite or indeterminate encounter evidence”**; its Stage-1 advisory (if enabled) is **suppressed**. Ordinary OFF has no requested Stage-1 diagnostic, though it retains the normal application observer. No failed native row was relabelled completed.

Each cell below is **completed / failed** with six scheduled trials:

| Original case | Profile | First run | Corrected run |
| --- | --- | ---: | ---: |
| critical-shift-neg | ordinary-off | 3 / 3 | 5 / 1 |
| critical-shift-neg | ordinary-on | 2 / 4 | 5 / 1 |
| critical-shift-neg | tap-blackhole | 4 / 2 | 3 / 3 |
| critical-shift-neg | tap-archive | 2 / 4 | 0 / 6 |
| critical-tilt-p14-shift | ordinary-off | 3 / 3 | 5 / 1 |
| critical-tilt-p14-shift | ordinary-on | 3 / 3 | 2 / 4 |
| critical-tilt-p14-shift | tap-blackhole | 4 / 2 | 1 / 5 |
| critical-tilt-p14-shift | tap-archive | 5 / 1 | 4 / 2 |
| **ALL (48 per run)** | **all profiles** | **26 / 22** | **25 / 23** |

Per-profile combined denominators: **first** OFF 6/6, ON 5/7, blackhole 8/4, archive 7/5; **corrected** OFF 10/2, ON 7/5, blackhole 4/8, archive 4/8. The first original TAP-archive recorded **41** callbacks; corrected TAP-archive recorded **44**.

**Direct original-report cross-run comparison:** all 48 positions have identical schedule and original scene SHA, but **21/48 changed completed/failed native state**, exactly at **1, 3, 5, 8, 9, 10, 11, 12, 16, 21, 26, 30, 31, 35, 36, 38, 40, 41, 45, 46, 48**. These same **21 positions** changed native-result fingerprints and Glass meter projections; the other 27 did not. Recomputed native-result JSON.stringify SHA-256 agrees with **96/96 stored fingerprints**. Similar aggregate totals **conceal** substantial within-slot variability. These are **different fresh executions**, not the same optical event reobserved or a causal matched-pair intervention.

## 5. Hot-path control integrity

Inspected the original single native-calling wrapper in [src/planar-media.js](https://github.com/physicsvigilante/opticsim/blob/760473cafceb70c055bb7c13b138a16c5e4d7620/src/planar-media.js), its Stage-1 [native diagnostic](https://github.com/physicsvigilante/opticsim/blob/760473cafceb70c055bb7c13b138a16c5e4d7620/src/native-finite-hit-diagnostic.js), and both TAP branches in [run.mjs](https://github.com/physicsvigilante/opticsim/blob/760473cafceb70c055bb7c13b138a16c5e4d7620/evaluation/repeated-critical-profile-controls-v1/run.mjs). The interface observer calls finiteDiagnostic.beforeIncident, then calls the original Glass.onRayIncident **once** via original.apply(this,args). PR97 adds one **diagnostic-method** wrapper, with identical **per-callback** p1/p2/incident scalar copy, array push, cap (128) and original diagnostic delegation for both TAP modes. No extra native-calling Glass wrapper is installed. The wrapper does change synchronous callback work and cannot be considered neutral.

Both TAP profiles execute postterminal baseline predicate mapping; **blackhole discards raw coordinates from its report**, whereas archive persists them. The original records show callbacks equal the actual Glass interaction meter in every TAP trial, captured length equals min(callbacks,cap), no faults and no over-cap samples. First blackhole / archive callback totals **40 / 41**, corrected **44 / 44**. **Same code per callback does not imply equal total callback counts across differing native runs.** Neither execution elapsed times nor observer neutrality nor causal differences have been established; ordinary OFF/ON use another native-calling workflow, so these are four deliberately distinct observational profiles.

## 6. Forty-four independent exact represented-binary64 checks

For each **actual** corrected-run archived callback, I used the saved native p1, p2, incident (native **y-down**) and mapped each original authored finite face (authored **y-up**) to native y-down; a proximity test identifies the unique incident-near finite face (maximum residual ~**4.419e−8 mm**, below the existing **1e−5 mm** classification guard). This face is an inferred match to recorded native point, **not an independently logged Glass face index**. I evaluated source-specified near-vertex and conditioning guards, exact integer signed ray t/edge u determinants, finite edge, forward sign, exact represented cutoff and computed intersection versus archived point. UNKNOWN remains UNKNOWN.

| Recorded event classification | Count | Distinct full serialized binary64 signatures |
| --- | ---: | ---: |
| EXACT_INTERSECTION_NOT_FORWARD (inconsistent) | **12** | **2** |
| NATIVE_INCIDENT_POINT_AGREEMENT_UNBOUNDED (UNKNOWN) | **24** | **4** |
| REPORTED_HIT_AT_OR_NEAR_VERTEX (UNKNOWN) | **8** | **2** |
| **Total** | **44** | **8** |

**All 44/44 independent reason/status pairs agree** with original Opticsim JS classifications. The corrected original same-author Python report separately agrees; this is not itself new native measurement evidence. **32/44 callbacks originate in eight eventually FAILED native TAP-archive trials**; their advisory is suppressed and no callback from a failed run is a qualified physical reading. Only **12 callbacks** came from four completed TAP-archive processes. Eight duplicate-heavy signatures are not 44 independent optical configurations. The signatures reflect **serialized JSON binary64 representations**, not proof of in-memory negative-zero sign bits.

The **two distinct nonforward signatures**, both on inferred **face-12**, each occur **six times**, all at zero-based callback index **2**:

1. **critical-shift-neg**, trial ordinals **2, 8, 10, 13, 18, 23**. Exact represented line has **t = 0** (not a strictly forward ray). The independently reproduced pinned native rounded intersection is **(1153.1213249443667, 740)**; its rounded positive travel is ~**0.0004001264 mm**, passing the native rounded forward, finite-segment and >1e−6 mm step gates.
2. **critical-tilt-p14-shift**, ordinals **25, 32, 34, 39, 42, 46**. Exact represented line has **t ≈ −5.61257408e−7** (backwards). Pinned native rounded intersection is **(1559.5026128439306, 269.40019693191533)**; its rounded apparent forward travel is ~**0.0000371431 mm**, again passing all three native rounded gates.

A **separate Node implementation** of the exact [pinned PhyDemo geometry.js linesIntersection](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/geometry.js) global-coordinate arithmetic order and native rounded-point acceptance predicates reproduces **44/44 recorded incident points and 44/44 rounded finite/forward/step-gate outcomes** from saved JSON. This reconciles the **12 represented-dyadic nonforward** statements with the **rounded binary64** native acceptance. It supports a precise *represented-line versus rounded-point numerical inconsistency*, not an ideal critical-angle Snell/TIR branch, a safe rounding tolerance, full native path proof or unique causal root.

## 7. Additional independently identified research confound: native RNG is not fixed

**Finding R-01 — important interpretation limitation, not a retrospective alteration of the archived evidence.** The test's deterministic seed **0x9700A55 controls only experiment schedule order**, **not PhyDemo's native random numbers**. Opticsim's [src/adapter.js compile](https://github.com/physicsvigilante/opticsim/blob/760473cafceb70c055bb7c13b138a16c5e4d7620/src/adapter.js) does **not set native randomSeed**. Pinned PhyDemo [Scene.js](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/Scene.js) defaults randomSeed to null and seeds the generator from the current time on scene load. Its [Glass.js getIncidentData](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/sceneObjs/glass/Glass.js) calls scene.rng() to perturb the auxiliary inside/outside test ray by a small amount.

Thus **the same authored physical case and deterministic schedule are not the same controlled native RNG stream across fresh processes**. Random inside/outside disambiguation is a plausible contributor to changed native success/failure patterns; I did **not** experimentally isolate or establish its contribution. This does **not** negate the original observations or the independent dyadic contradiction for recorded scalars, but **materially limits any attribution solely to observer overhead, scheduler, or floating-point arithmetic**. Treat this as a **blocker for stronger mechanism/causal/stability claims**, not a failure to report the bounded exploratory trial honestly.

## 8. Scientific boundaries, next rigorous test and merge hold

**Bounded research PASS:** I find no demonstrated integrity blocker in the frozen protocol, unchanged original cases, original-archive authenticity, all native success/failure denominators, independent integer/dyadic classification, or faithful presentation of research-only limits. The documented native failure cases are **real trial failures**; the first Python-audit failed workflow stays **FAILED**. The corrected archive and head-specific 12/12 CI checks are genuine software/evidence-integrity checks, **not optical correctness approvals**.

**Limits requiring explicit retention:** no independent PhyDemo rerun or uninstrumented same-event counterfactual; runtime native RNG is unpinned; 44 events represent only eight distinct binary64 signatures; near-vertex and point-agreement categories remain UNKNOWN; no universally justified incident-point-error envelope, exact mathematical critical branch, physically certified path/image, Watts measurement, classroom interpretation validation, observer-neutral timing match or approved Stage-2 withholding. Neither different profile frequencies nor matching fingerprints proves causality or physics.

**Smallest defensible next test:** on a **new independently preregistered test-only research branch**, select **one** existing original critical case, keep its source document and inputs.json bytes unchanged, and run **six balanced four-mode blocks (24 fresh processes)** with an **explicit single fixed PhyDemo native randomSeed logged per run**. Hash the test-only compiled native scene/config separately, retain every native status/fingerprint/callback and original source hash, and run a separate independent exact-dyadic check. Compare within-mode repeatability and across-mode results under a controlled RNG stream. This would isolate a major current confound **without** authorizing production physics changes or proving observer causation. Leave both original PR97 ZIPs and their failed/successful statuses immutable.

**FINAL GATE: PASS — R2 NUMERICAL RESEARCH/EVIDENCE ONLY. DO NOT MERGE PR #97 OR ITS DISPOSABLE WORKFLOW.** Source PR and all original artifacts are unchanged by this review. No change to production optics, PhyDemo, source physics, thresholds, Stage-1 canonical results, Stage-2 policy or public deployment is approved. This is a newly authored append-only Chat B report, not an adoption of Chat A's developer findings.
