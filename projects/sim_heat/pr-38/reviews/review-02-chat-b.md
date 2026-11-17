# SIM_HEAT PR #38 — independent Chat B targeted R2 re-review (review-02)

**Verdict: PASS — SCOPED to correction of F-01, the literal/exact-byte integrity of the NONEXECUTABLE build-text preview manifest.** The prior CHANGES REQUESTED review remains correct for its old source SHA. This PASS is **not** native qualification, a production merge recommendation, owner approval, a compiler-query/build/launch budget, or a claim that the historical physical failures were corrected.

- **Reviewer/date:** Chat B, separate ChatGPT conversation (GPT-6), 2026-11-17. Independently reproduced tests, but this is LLM review, not independent human or owner-authenticated attestation.
- **Source:** [physicsvigilante/sim_heat draft PR #38](https://github.com/physicsvigilante/sim_heat/pull/38), historically frozen H1-C1-F0 experiment, **NEVER MERGE TO MAIN**.
- **Immediate PR base:** [2f2b8d5008f51b9972897058328aed8cbcbfbbce](https://github.com/physicsvigilante/sim_heat/commit/2f2b8d5008f51b9972897058328aed8cbcbfbbce).
- **Prior reviewed SHA/tree:** [a570e3c589457d21b6673701a2d126d7046e1c3c](https://github.com/physicsvigilante/sim_heat/commit/a570e3c589457d21b6673701a2d126d7046e1c3c) / 0f5af0d11d3c96b5b4decc3ea8dd0fae2ae201b6, [review-01](review-01-chat-b.md) **CHANGES REQUESTED**.
- **Exactly reviewed corrected head/tree:** [f87a9aa025caf5091da8fe3613734b62281ebe1c](https://github.com/physicsvigilante/sim_heat/commit/f87a9aa025caf5091da8fe3613734b62281ebe1c) / **e55d00c700665012e1e27be0f28a877348969f3f**.
- **Scoped source diff:** [old to new](https://github.com/physicsvigilante/sim_heat/compare/a570e3c589457d21b6673701a2d126d7046e1c3c...f87a9aa025caf5091da8fe3613734b62281ebe1c), 4 commits ahead, **exactly three modified paths**: qualification/h1_c1/f02/offline_build_script_preview.py (+9/-1), test_offline_build_script_preview.py (+65/-0), BUILD_TEXT_PREVIEW_SCOPE.md (+8/-0). No original Modelica model, study, thermal library, frozen H1, native runner, checker, scientific reference, preexisting stage, original numerical plan, or workflow edits. Against immediate PR base, the preview branch still adds only its original four isolated files.
- **Risk and scope:** targeted R2 evidence integrity/readback correction only. No physics calculations or native simulation.
- **Changes performed by reviewer:** a **new report only** in review_sandbox; no changes to sim_heat, old review, frozen inputs, tolerances, PR/CI or approvals; no native commands or Modelica install.

## Findings

### F-01 — original MAJOR type ambiguity: RESOLVED within the offline manifest readback scope

**Location:** [corrected source lines 120–142](https://github.com/physicsvigilante/sim_heat/blob/f87a9aa025caf5091da8fe3613734b62281ebe1c/qualification/h1_c1/f02/offline_build_script_preview.py#L120-L142); [new negative regressions](https://github.com/physicsvigilante/sim_heat/blob/f87a9aa025caf5091da8fe3613734b62281ebe1c/qualification/h1_c1/f02/test_offline_build_script_preview.py).

**Old observed failure:** the parsed dictionary-equality predicate accepted numerically equal but type-different JSON, including integer 0 / float 0.0 in place of literal false and 4000.0 in place of 4000. Original review-01 reproduced this at the predicate level and correctly requested changes at the old SHA.

**Correction examined:** the source still calls staging.strict_metadata for duplicate-key, nonfinite, top-level type and size refusals, but now independently compares **complete stored manifest raw bytes** with the deterministic expected bytes produced by encoded(contract(label,raw)); saved script bytes must also exactly match freshly derived pure formatter text. The remaining parsed-object equality is now redundant confirmation, not the sole protection. This closes F-01 even where changed dictionaries compare equal under Python semantics. It intentionally rejects changed serialization/whitespace as well as changes to JSON types, permissions, history, sample settings and references.

**Independently executed reproduction, not just test-name inspection:** I fetched and reconstructed the corrected full preview Python source, and locally checked the Git blob identity of that source **7314e9098028aac19cd136e6f0cd610ffcd04ae3**, equal to the exact pinned GitHub file blob. Using **unmodified saved CI preview script (797 bytes, SHA-256 eeb216779afc98986fc1c2649c07a036d835743a9118971a21a8f7acddad110e)** and saved manifest from the downloaded original CI ZIP, I imported the real source and called its **actual verify()** on temporary on-disk preview files.

For the isolated F-01 replay, the upstream stage verification, study loader and pure formatter were stubbed to return the saved, correctly pinned stage/script facts; the strict parser was reproduced from the inspected pinned stage source (duplicate keys and NaN refused). Thus this is **source-imported actual verifier execution with isolated upstream dependencies**, not a local full integrated staging/regeneration run. The corresponding **real full-source end-to-end staging/preview regression** is separately demonstrated by the exact-head hosted CI; I did **not** locally execute all 232 integrated tests.

- Untouched original manifest/script passed the real verifier before testing and again after restoration.
- Independently enumerated **all thirteen literal false fields** in the original saved manifest; each was separately changed to integer **0** and float **0.0** (**26/26 refused**), with script bytes held fixed. Every changed dictionary still compared equal to the original parsed dictionary under Python equality, directly reproducing the prior predicate weakness while proving the corrected verifier rejects it.
- Changed **targetIntervals integer 4000 to float 4000.0**: parsed dictionaries equal, actual verify refused (**1/1**).
- Semantically identical but differently serialized JSON: actual verify refused (**1/1**).
- Extra probes: duplicate nativeAllowed key, NaN constant, true permission, altered script text, and extra build.mos: all refused (**5/5**), with correct refusal classes/reasons.
- **Total independent local adverse checks: 33/33 REFUSED**. The source was never fed to OpenModelica; the only file modifications were within a disposable local fixture.

**Assessment:** **no remaining demonstrated F-01 defect** in exact-byte saved offline preview-manifest verification.

### F-02 — no demonstrated new non-execution defect; bounded limitations remain

The preview path calls only the unchanged [build_script pure string formatter](https://github.com/physicsvigilante/sim_heat/blob/f87a9aa025caf5091da8fe3613734b62281ebe1c/tools/h1_native_batch.py#L108-L128) to create passive text. The saved path is named unexecuted-build-script.mos.txt, **not** an executable build.mos. The preview CLI has only preview-text-only and verify-preview-only choices. It does not call frozen h1_native_batch.prepare / execute / invoke, reference.prepare, native runner, subprocess, OpenModelica, compiler query, model build, model launch or MAT decoding. Original source runner methods exist elsewhere but are not called by this preview.

**Limits:** readback checks use multiple filesystem observations rather than an atomic snapshot (stage reads, strict JSON parsing and raw read, script read, membership checks); a concurrent malicious file-swap/TOCTOU scenario is **not proven safe**. The preview has no authenticated release root, live/ref trust, host attestation, cross-run durable one-shot gate, or native launch permissions. These are acceptable **only because this is offline evidence, not a concurrent/native security boundary**. The text can be manually copied and executed elsewhere, but its presence never authorizes doing so.

### F-03 — immutable original science and negative history preserved; NOT corrected

The actual original [PR31 V2 scientific artifact #14249313720](https://github.com/physicsvigilante/sim_heat/actions/runs/43915934653/artifacts/14249313720) was independently downloaded. Whole ZIP: **2,348,945 bytes**, SHA-256 **d9259837e0e03c70989b50b2c9dcbf13aca260da4d1cb0ae000b2a23ef65732e**, **13/13 CRC valid**. Original C1_REFERENCE_V2_BUNDLE.json: **4,409,800 bytes**, raw SHA-256 **0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368**, seal **d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9**, nativeQualified=false. The repeated saved V2 bundle is byte-identical; all **37 reference channels have 4,001 samples**, as does the grid. The saved reference is input data, not a freshly computed reference or observed native measurement.

I also independently inspected PR31's F01_ORIGINAL_FAILURE_STILL_REPRODUCED.json: original hotLead.G sealed value margin **80.0×**, **strict100xPass=false**, gate HOLD_NO_NATIVE_EXECUTION. Required **≥100×** remains unmet. Historical PR32 bitwise regeneration of original V2 remains FAIL; it cannot be replaced by any alternate reference. Both histories are still marked false in the current preview and stage receipt. The nine originally requested actual native outputs remain **not_computed**.

## Provenance and CI — independently checked

**Corrected CI:** [workflow run #44032986237](https://github.com/physicsvigilante/sim_heat/actions/runs/44032986237), push, attempt 1, completed **SUCCESS**, exact corrected head f87a9aa... and tree e55d00c..., job **133869324831** success and all steps success. GitHub's own run payload, current PR ref and original saved ZIP head-sha.txt / head-tree.txt agree. Historical [run #44030612438](https://github.com/physicsvigilante/sim_heat/actions/runs/44030612438) is independently verified completed SUCCESS **only at old a570e3c... / old tree**, and does not cure its F-01.

**Original current-head ZIP [artifact #14306455880](https://github.com/physicsvigilante/sim_heat/actions/runs/44032986237/artifacts/14306455880):** I downloaded the actual archive, not a summary. Independently checked **22,116 bytes**, full ZIP SHA-256 **e74afdac7371b9ae1e8b7c5936917c35e764bc0f8f3b989619e1c37cea27e6d6**, **33/33 ZIP CRC valid**. Saved text-preview-receipt.json and text-preview-readback.json are byte-identical; status NONEXECUTABLE_BUILD_TEXT_PREVIEW_VERIFIED and all listed native/owner/one-shot flags are literal false. Only the script TXT plus NONNATIVE_BUILD_PREVIEW_MANIFEST.json reside in the preview subdirectory; no build.mos, executable, native MAT output or actual observation.

**All 232 hosted OFFLINE unit test methods PASS, verified from actual saved log count and OK marker**, not independently rerun in full locally:

| Suite | Tests | Saved log |
|---|---:|---|
| Corrected build-text preview (including F-01 on-disk cases) | 15 | OK |
| Exact immutable stage | 24 | OK |
| Existing F02 control/type | 16 | OK |
| Owner-adopted OFFLINE reference consumer | 11 | OK |
| Reference binding | 8 | OK |
| Original archive/fixture | 9 | OK |
| Frozen H1 | 149 | OK |
| **Total** | **232** | **ALL OK** |

Confirmed all seven saved CLI stderr refusals (execute, compile, build, launch, native, approve, run) report invalid choice; all seven stdout files are empty. Original F0 pin log reports **14/14 OK**. CI tracked-source SHA listing independently identifies the unchanged original Modelica model **9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435**, evaluator modal study **b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b**, and thermal library **e57955b6c32cb34321a6b1908306c4ea9a63ae259b95a5fd48c7e8d3b4da10ea**, consistent with source pins and the three-path-only old/new Git comparison. Existing staging/reference regression evidence covers the original **23** source-plan pins.

**Absence-of-native check:** inspected the exact pinned workflow and job steps/logs: read-only contents permission, checkout without persisted credentials, Python-only checking dependencies, offline stage and preview commands, disallowed CLI probes and Python unittests. No OpenModelica installation, omc --version, real compiler invocation, model build/launch, native MAT or observed native results are present in this CI path. This describes the verified workflow and evidence, **not a universal proof about events outside it**.

## Separate scope judgments

| Dimension | Scoped judgment | Basis |
|---|---|---|
| Source interpretation fidelity | PASS (unchanged, offline only) | Original model/study/library identities and source-derived text settings preserved. |
| Physical/numerical correctness | NOT QUALIFIED | No new numerical experiment; original 80×/100× failure and PR32 failure persist. |
| Native simulation/observable coverage | NOT RUN | No real OMC, built model, MAT, nine actual observations or compiler/host attestations. |
| Evidence integrity and provenance | **PASS for corrected F-01 only** | Exact manifest raw bytes, strict parser, 33 independent local refusals, 15 hosted preview tests and exact-head artifacts. No trusted release/TOCTOU guarantee. |
| Teacher-facing usefulness | NOT EVALUATED | No teaching UI/physical exploration considered. |
| Textbook-answer completeness | NOT APPLICABLE | Not a question corpus milestone. |

## Hard-stop and next gates

**Scoped PASS ends at offline nonexecuted exact build-text preview verification at f87a9aa...**. PR #38 stays draft/historical and **must never merge to production main**. This report is not native execution or a native-launch permission.

Any later native task separately requires **all** of: (1) independently owner-authenticated, protected and retained original scientific source/reference release and backup; (2) live ref/source identity trust; (3) a distinct independently reviewed **non-regenerating executable** adapter with exact source/reference pins and a named bounded plan; (4) observed actual OMC/MSL/host/compiler/runtime fingerprints and effective experiment/37-export checks; (5) atomic durable cross-run one-shot reservation/no retries and retained failure/crash/partial evidence; (6) independent pre-native R2 of that real adapter/plan; and (7) **new explicit owner approval for a specifically named compiler-version-query/build/launch budget**, followed by independent post-native trace/MAT/numerical verification. Original F0 accuracy and PR32 regeneration histories must never be relabeled.

**Final: PASS (targeted F-01 literal manifest integrity only), zero permission to invoke OpenModelica or merge historical PRs.**
