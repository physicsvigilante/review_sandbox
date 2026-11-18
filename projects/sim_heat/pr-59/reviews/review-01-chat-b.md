# SIM_HEAT PR #59 — Chat B consolidated independent evidence review

**Outcome: SCOPED PASS — H1-T1-UNSEALED retrospective PUBLIC-task source fidelity, unchanged first-attempt H1 offline admission, source-only presentation, and honest unsupported-law refusal ONLY.** This is **not** verified precommitted hidden-key/blind scoring, a native/physical numerical qualification, an authenticated textbook case, or approval to merge PR #59.

| Identity / boundary | Reviewed value |
| --- | --- |
| Source | [physicsvigilante/sim_heat PR #59](https://github.com/physicsvigilante/sim_heat/pull/59), draft and unmerged at review |
| **Exact source HEAD** | `7234a53a5022441a912eb09240138e9c6c5945d8` |
| **Exact source Git tree** | `6405d89cfcc6f2b899975cafb56310f13fe20ea1` |
| Pinned baseline | `f52613c39c539b2d4543a9838e5658d526fca10e`, tree `0c44961b473d23737b0c9f3b3f2cd3db65b9f264` |
| PR synthetic merge (CI only) | `1036ade7d3ab7845fbae50b2d0d5003edbf563e0`, same tree, parents baseline then reviewed HEAD |
| Reviewer | Fresh separate-conversation Chat B, GPT-6; not independent model weights or human subject-matter adjudication |
| Date | 2026-11-18 UTC |
| Scope / risk | Focused R2 **evidence/source-fidelity** review; no production H1 change; no OpenModelica/native execution authorized |
| Source files modified by reviewer | **None**; read-only inspection, offline validation and local scratch extraction only |

**Disposition:** No demonstrated source, topology, request, admission, evidence-identity or qualification-boundary defect in this precise UNSEALED scope. The lost private key is a **material and permanent limitation of this trial's original claimed scoring method**, not a condition that green CI can cure. Keep the source PR draft/unmerged.

## F-01 — Critical scope boundary: original scorer key cannot be verified (major limitation; not a new code defect)

The original selector published a salted private-key SHA-256 commitment `49cc3397ae5bbbabff823e674491d9d44d8341bbd8b9556694c86f5ffffb6319` before the author's submission. The [selector's later report](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6982883843) states the **actual private key bytes and salt were unavailable**; the commitment was **never opened or verified**. No alternative key can restore the original blinded precommitment. The [owner's downgraded authorization](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/h1-t1/UNSEALED-AUTHORIZATION-01.md) allows only *retrospective comparison to the already locked PUBLIC task*, then source-only H1 checks. Accordingly, the result must always be labeled **H1-T1-UNSEALED / retrospective public-task evaluation**. Do not score or publish it as a successful precommitted hidden-key trial.

The public tasks were selector-invented illustrative cases, not externally authenticated JEE textbook exercises. Selector and author used different GPT-6 conversations, disclosed earlier general SIM_HEAT exposure, and used shared underlying model-family training; independent human creation, independent weights and total absence of prior exposure cannot be proven. Source hashes authenticate *the captured records*, not the truth of source attribution or the author's private process.

## F-02 — First-attempt chronology and exact source identity (PASS; independently checked)

I fetched the three **original GitHub issue comments** through the issue-comment API and independently recomputed SHA-256 over each complete UTF-8 body (SHA-256 checked against standard known vectors). The comment timestamps, byte lengths and digests match:

| Record | Created UTC | UTF-8 bytes | Whole-body SHA-256 |
| --- | --- | ---: | --- |
| [Original fixed selector tasks, `6981681502`](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6981681502) | 14:36:12 | 10,233 | `8f45ad3d4a763952e25d60658ae4d8eeae37fd266bd372b3cd80fb19b81fa2a2` |
| [Original FIRST_ATTEMPT_V1, `6982616288`](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6982616288) | 15:11:39 | 31,793 | `fa96e40b24fe3b039e823a78f54546bdf0ed2400e0f3b1b9519bbeb764e3c893` |
| [Original unavailable-key disclosure, `6982883843`](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6982883843) | 15:21:27 | 1,303 | `2123c5e51db849c1189df3b6f31551c5453c1bb8736a970b5724d505750df340` |

The pre-evaluation [task lock](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/h1-t1/TASK-LOCK-01.md), [first-attempt lock](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/h1-t1/FIRST-ATTEMPT-LOCK-01.md) and [retrospective fidelity record](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/h1-t1/PUBLIC-TASK-FIDELITY-01.md) describe the intended capture-before-evaluation sequence. The original issue comment's `created_at == updated_at` and matching locked body support this chronology, but editable GitHub comments alone are not immutable originals; the committed raw snapshots are the stable identities. The fidelity report was recorded before the trial H1 admission as described; this does **not** make its rubric precommitted.

I independently extracted **all seven** labeled Markdown code fences from the original author comment (S model/study/notes; T model/study/notes; X refusal). Each current PR case file matches the fenced text **plus exactly one terminal LF**, and every resulting Git blob SHA matches `DERIVATION.json`. This is openly **derived file packaging**, not a set of independently uploaded original files. All seven blobs are **identical at first evidence HEAD** `7adddca2c3f52ffc1d52daa0f460ad8d206f35f8` **and corrected HEAD**; no authored physical parameter, connection, study request or note was repaired. The author's unchanged study hashes match the LF-derived model contents:

| Case | Derived `model.mo` SHA-256 | Derived `study.json` SHA-256 |
| --- | --- | --- |
| S | `26113226ae046634c36e0acd51cdeb84f6ce9c500dbaaa86f31e5d34fbfce2a7` | `582cd7f82051b098bbd674aff920fb9a954366f5d27b275ffc73c40bcd0f672e` |
| T | `2c60e40f1ad8d85f46968f03712d23e8cd6b9c656cf6099a38a97d198d0873ae` | `12ad51f59d2bd6c6561d4059f68b4263e7d4e39cdf5493f353a7affee6929d2a` |

## F-03 — Independent physical/source-fidelity comparison: S and T (PASS, source-level only)

I compared the **original selector's tables** against the **original author's Modelica and study JSON**, separately from H1 parsing. A new independent port union-find over every written `connect(...)` checked the **complete sorted port-equivalence partitions**, not only element counts. For all rod rows I checked `k`, `L`, `A` or **circular diameter `d`**, the exact rod class, the **declared port_a/port_b node**, and signed request orientation. I also checked every maintained-temperature and finite-body field, component identities, all study requests and operand order, all physical-slot provenance targets, and the model regime note. No mismatch, extra owner, junction storage, phantom rod, missing or duplicate source slot, or direct body-body short was found.

**T1-S — three-thermostat guarded heat spreader:** exactly 3 boundaries `S_Hot=386 K`, `S_Cold=294 K`, `S_Guard=326 K`; 7 `RodArea` plus circular `S08(d=0.018 m)`; **11 components, 13 connects, 19 distinct ports, 6 exact ideal nodes** `H,C,G,J_North,J_South,J_Center`, including 3 distinct ownerless junctions. The complete 8/8 rod endpoint partitions match the locked topology. **27/27 scalar source fields** have exact `illustrative` provenance; one `@model` adopted-assumption record. Steady mode has `analysis={}`. All **6/6** public request IDs, operators and targets match, including `S06.port_a - S_Cold.port` and `S04.port_a - S_Guard.port`, with ordered/positive-a-to-b flow semantics retained. The novel cross-link/branches do not require extra production components.

**T1-T — two-feed three-block thermal lattice:** exactly 2 boundaries `T_Warm=367 K`, `T_Cool=289 K`; bodies `T_Ridge=(0.32 kg,460 J/(kg K),337 K)`, `T_Collar=(0.24,830,303)`, `T_Plug=(0.41,390,318)`; 9 `RodArea` plus circular `T06(d=0.016 m)`; **15 components, 18 connects, 25 distinct ports, 7 exact ideal nodes** `W,K,R,B,P,J_Upper,J_Lower`. Both ownerless junctions are storage-free and separate from body/boundary-owned nodes; complete 10/10 rod port partitions match. **41/41 scalar source fields** have exact `illustrative` provenance plus one model-regime note. All **8/8** public operations and targets match: 3 body temperatures (K), 2 relative body energies (J), oriented flows `T06` and `T10` (W), and `T03.port_a - T_Cool.port` (K). Transient `startTime=0`, `stopTime=2400 s`, `intervals=2400` (permissible even grid), `dassl`, `tolerance=1e-8` are **provisional analysis metadata**, not qualified time histories.

These graphs use the existing constant-property, lumped, 1-D Fourier conduction/finite-capacity/maintained-temperature semantics. Ideal junctions are equal-temperature, zero-storage equivalence classes; a rod's two ends are **not** collapsed into one ideal node. Material values and geometry are selector-provided *illustrative inputs*, not inferred properties or measurements. This verifies **physical model specification fidelity**, **not** that all real devices would satisfy the simplifying assumptions or that a native solution is accurate.

## F-04 — Original strict H1 offline admission (PASS; personally rerun without native solver)

I extracted the exact source tree from the corrected PR artifact into a **scratch directory**, then directly reran unchanged `python -B -m h1` on the two original LF-derived studies and `python -B -m h1.source_preview` on their admitted output. Both admissions exited **0**, `admitted=true`, `nativeExecuted=false`; S **6/6** and T **8/8** requested observations have `status=not_computed`. Independently regenerated source-preview JSON SHA-256 matches both the first failed-run and corrected hosted artifacts:

| Case | Logical nodes / rods / components | Source-preview SHA-256 | Result claims |
| --- | --- | --- | --- |
| S | 6 / 8 / 11 | `273664023af75d60f44bfb8b26fbcb00686e2f0a0e6ad6ed2b5717b529a1d912` | six `not_computed`; no native |
| T | 7 / 10 / 15 | `68ff037229a4969e379de5542121dd8f9349177d94a9676b7526e81463af0267` | eight `not_computed`; no native |

The preview source metadata is `evidenceKind=authored_source_only`, `nativeExecuted=false`, `nativeQualified=false`, `sourceFidelityQualified=false`; units are W/K for S and J/K/W for T. `scaledJunctionCondition` is an **offline preflight/conditioning diagnostic**, not a thermal measurement. Strict parser admission tests supported grammar and limits, **not** solver output or source authentication. No OpenModelica command was run.

I also independently ran inherited **152/152 H1 Python tests**, **11/11 generic JS source-preview tests** and documentation parity `--check`: **PASS** on the extracted exact candidate tree. This is repeat offline regression coverage, not a new native experiment.

## F-05 — Historical browser failure correctly preserved; narrow correction verified (PASS; failure remains FAILED)

[First push run **44340634456**](https://github.com/physicsvigilante/sim_heat/actions/runs/44340634456), job `134929302926`, on first evidence head `7adddca2...`, **FAILED**. GitHub job logs show the **source verification, 152 H1 tests, 11 JS tests and both original S/T admission/preview steps had passed** before a *new evaluator-only* Chromium test timed out waiting 30 seconds for `payload.studyId` in `#graph-title`. The unchanged production viewer titles the graph with **`modelName`** and displays the separate **`studyId`** in `#identity`. This was a **bad browser test assertion**, not evidence of a Modelica admission defect or a valid first browser pass. The irrelevant favicon 404 is not the failure cause.

The only change between first and final evidence heads is [`experiments/h1_t1_unsealed/browser_smoke.py`](https://github.com/physicsvigilante/sim_heat/blob/7234a53a5022441a912eb09240138e9c6c5945d8/experiments/h1_t1_unsealed/browser_smoke.py): assert actual `modelName` in heading and actual distinct `studyId` in identity details. [Exact one-file correction diff](https://github.com/physicsvigilante/sim_heat/compare/7adddca2c3f52ffc1d52daa0f460ad8d206f35f8...7234a53a5022441a912eb09240138e9c6c5945d8). No authored S/T/X file or production viewer changed. The first red run remains historical evidence; it is **not retroactively green**.

[Corrected push **44341730779**](https://github.com/physicsvigilante/sim_heat/actions/runs/44341730779) and [PR **44341747546**](https://github.com/physicsvigilante/sim_heat/actions/runs/44341747546) are **SUCCESS** at exact reviewed tree (PR job via same-tree synthetic merge); the hosted real-HTTP Chromium S desktop and T mobile browser receipt reports `actualHttpChromiumPass=["S","T"]`. I personally inspected both preserved source-only screenshots and forged-import refusal screenshots. They show source identities, SI values, provenance, topology, requested `not_computed` statuses, and a visible refusal/error when `nativeQualified=true` is forged; the browser assertions also require graph and request state to be cleared on refusal. These are **hosted actual-browser executions**, not a browser success I reproduced locally: my separate local Chromium attempt was blocked **at page navigation** by the tool environment (`net::ERR_BLOCKED_BY_ADMINISTRATOR` on local HTTP), before any app assertion. That environment block is not proof of an application bug, and no local browser PASS is claimed.

**Minor viewer-use limitation (nonblocking, pre-existing):** On a narrow mobile viewport the graph is wider than the screen and is within an intentionally horizontally scrollable labeled region. The captured T screenshot does not show the whole graph at once; this is not missing source topology or an indication of physically positioned apparatus geometry. Browser layout/diagram and rod ordering do not independently verify real-world distance, branch direction of heat flow, animation, or solved state.

## F-06 — Artifact, CI and historical evidence integrity (PASS with explicit authentication boundary)

I downloaded and independently checked **all four actual GitHub Action artifact ZIP bytes**, their SHA-256, distinct entries and CRC (none corrupt), then reconstructed the complete Git tree of each included `source.tar` from its Git objects; these agree with the claimed first and current source trees. I directly read each S/T admission JSON, source-preview payload, outcomes receipt, CI job logs, and corrected browser receipts:

| Run / artifact | Outcome | ZIP bytes; independent ZIP SHA-256 | ZIP entries; pinned tree |
| --- | --- | --- | --- |
| [Failed push 44340634456 / 14443931228](https://github.com/physicsvigilante/sim_heat/actions/runs/44340634456) | **FAIL** browser assertion after S/T admission | 1,440,541; `d43d1e4789d7100d61aec3f3f304ad5e290842b5116d3fe68edda3510e807370` | 22 unique CRC-valid; `ec3520e22a4f3b258c8cf0e883815f8dfbe6dcfc` |
| [Corrected push 44341730779 / 14444456298](https://github.com/physicsvigilante/sim_heat/actions/runs/44341730779) | **PASS** | 2,539,538; `5580023fd2174280e306cfa21cdf4b7cb1c229c37810bb81041be24a6ac4465c` | 27 unique CRC-valid; `6405d89cfcc6f2b899975cafb56310f13fe20ea1` |
| [Corrected PR 44341747546 / 14443453508](https://github.com/physicsvigilante/sim_heat/actions/runs/44341747546) | **PASS** | 2,539,541; `5170bd1907e4e87b94e7eaa74607284a46067f5231e320b7c771779c95694dcf` | 27 unique CRC-valid; same candidate tree |
| [Audit core 44341747559 / 14445465031](https://github.com/physicsvigilante/sim_heat/actions/runs/44341747559) | **PASS** | 5,874,350; `cfdb30bbe61dac82a3a8355d77f4a279f5abe2af487e89692f5255eb17b62b4b` | 33 unique CRC-valid; same candidate tree |

All three evidence artifacts' S/T source-preview JSONs have byte-identical hashes, including across the **failed** and corrected runs: this is important evidence the later browser fix did **not** silently change a first-attempt model, admission or generated preview. The GitHub compare identifies **exactly eleven added evidence/CI paths**, no modifications/deletions of existing `h1/`, viewer, physics, runner, reference, C1 or diagnostic-source files. The synthetic merge has the documented two parents and **same exact candidate tree**.

I inspected audit-core artifact `archive-replay.json`: it records **six original archived cases**, `D1,D2,DEV_BRIDGE,TEACH_RING4,S1,D2_K2`, each `status=BYTE_IDENTICAL` and `nativeExecutedByReplay=false`. This confirms the **hosted archive-replay receipt and preserving CI status**; I did **not** personally rerun archive replay against every original upstream ZIP or execute native physics. Existing six diagnostic-only statuses remain nonqualified, and the prior H1-C1 reference precision shortfall (80× versus 100×) and saved seal mismatch, along with its nine native-uncomputed observations, are **not** repaired or promoted by PR #59. The audit cannot authenticate new simulated temperatures or flows.

## F-07 — Unsupported T1-X radiation: honest refusal (PASS)

I inspected the original seventh code fence, [`X/REFUSAL.md`](https://github.com/physicsvigilante/sim_heat/blob/7234a53a5022441a912eb09240138e9c6c5945d8/experiments/h1_t1_unsealed/X/REFUSAL.md). It preserves the selector's illustrative vacuum-bead parameters (radius 0.035 m, mass 0.19 kg, heat capacity coefficient 420 J/(kg K), initial 470 K, black enclosure 295 K, emissivity 0.82 and specified Stefan–Boltzmann constant), the required initial radiative loss and 300-s temperature questions, and the absence of any conducting medium. It correctly identifies the missing nonlinear gray-body law `P = ε σ (4πr²)(T_bead⁴ − T_wall⁴)` and coupled body-energy balance; those equations are **symbolic explanations, not computed results**. It explicitly refuses to substitute a conductive `RodArea`/`RodCircular` across vacuum, provides **no X model/study**, and gives **no numerical answer**. No H1 radiation component, emissivity port or radiative enclosure law exists in this admitted public grammar. This is correct unsupported-law boundary behavior; an X H1 admission must **not** be demanded.

## Independent tests vs hosted-only evidence

**Personally performed:** direct GitHub comment-body rehash/chronology, seven exact-LF code-fence/package comparisons and Git blob equality across heads, independent complete S/T rod/port equivalence and scalar/provenance/request comparisons, GitHub compare/PR/CI step/log inspection, four artifact download/byte-SHA/CRC/entries and tar-to-Git-tree reconstruction, firsthand reading of source-preview outputs and screenshots, scratch rerun of both pinned H1 CLI admissions/previews with exact output SHA identities, 152 Python tests, 11 JS tests and docs parity. All used read-only repository material/local ephemeral files; neither GitHub source repository nor frozen inputs were edited.

**Hosted CI inspected, not personally rerun:** real-HTTP Chromium S desktop/T mobile and forged native-qualified refusal, audit-core replay against original archived native ZIPs, entire hosted audit matrix. **Local attempted but blocked:** Chromium navigation by sandbox URL policy; no local visual test was passed. **Not run:** OpenModelica installation/query/build/launch, native reference/numeric computation, result qualification, external textbook verification, classroom/teacher study, production merge.

## Separate scope judgments

| Dimension | Judgment | Basis and boundary |
| --- | --- | --- |
| Original S/T first-attempt public-task **source fidelity** | **PASS** | Exact numbers, full signed port incidence, public requests, SI and illustrative source attribution checked independently |
| Original X unsupported-law recognition | **PASS** | Radiation correctly refused without fictional rod, source model or answers |
| Strict H1 **offline admission** | **PASS** | S and T exit 0 on original extracted files; 6/8 observations remain `not_computed` |
| Generic **source-only visual presentation and negative guard** | **PASS (hosted browser evidence)** | Source graph/metadata shown; forged `nativeQualified` rejected/cleared; reviewer-local browser navigation blocked |
| Evidence identity / original first-attempt preservation | **PASS** | Original comments/body digests, LF derivation, Git blobs, source tree, CI/archive hashes and historical failure preserved |
| Originally **precommitted hidden-key scoring** | **NOT VERIFIED — UNSEALED** | Private salt/key lost; original commitment cannot be opened; no retrospective substitute permitted |
| **Physical/numerical correctness of solved values** | **UNKNOWN / NOT TESTED** | No native solved temperatures, fluxes, energy histories, independent reference or convergence; source-only statuses |
| **Native simulation / qualification** | **NOT DEMONSTRATED** | `nativeExecuted=false` for new cases; historical archived diagnostic replay does not execute native |
| Teacher-facing educational usefulness | **LIMITED SOURCE INSPECTION SHOWN; effectiveness UNKNOWN** | Good traceable schematic nodes/fields; no measured learning or accurate apparatus geometry |
| JEE textbook-answer completeness | **NOT APPLICABLE / NOT ESTABLISHED** | Selector-invented illustrative problems; no source authentication or computed answers |

## Required disposition / release advice

**SCOPED PASS** for this exact unsealed, source-only retrospective evidence package; no correction to original author files or to the production H1 library is supported by this review. Keep the original key custody failure prominently attached to every trial result. Do not rebrand the attempt as sealed-blind evaluation, general arbitrary-model authoring reliability, physical/numerical result qualification, or textbook-answer completeness. Preserve the first failed browser CI red and the subsequently corrected exact-head green tests separately.

**Do not merge PR #59.** Its status is evidence-only draft and this review is **not** source-merge approval. Any next claim about numeric heat results or native generality would require separately owner-authorized native work and genuine independent reference/verification; that is outside the current review. No new production test or third authoring correction is required for this scoped verdict.