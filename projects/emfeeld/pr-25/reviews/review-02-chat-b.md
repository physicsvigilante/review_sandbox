# EM Fields PR #25 — independent Chat B focused R1 re-review 02

**Verdict: PASS (scoped F1/F2 correction; not production merge approval).**  
**Date:** 2026-11-16, Asia/Kolkata  
**Reviewer:** Chat B, separate ChatGPT conversation, GPT-6; independently authored and executed adversarial checks on downloaded pinned source. This is independent conversation context, not a different human or certified physics evaluator.  
**Source:** [physicsvigilante/emfeeld PR #25](https://github.com/physicsvigilante/emfeeld/pull/25), OPEN / DRAFT / UNMERGED when checked.  
**Exactly reviewed corrected head:** a56b4680a90647ad4af03a52a0b9053807d10a7b  
**Canonical Git tree:** ce20aa49d978c94150edbbf017d8fae1e2f6f896  
**Qualified base:** bf6a18399c604136dd363ad94d40557dbe2c2543, tree e7ddc4c6c44106bf3113f7c1e176b21490a7cf5c  
**GitHub merge preview:** 7b04fc27b6a4e0efaf74045734389af416ec9223, same exact corrected tree, parents base and head.  
**Historical failing head:** 4fe896ff6bb98d21a090bc16a84fe26145f9f5e7. [Original review-01](review-01-chat-b.md) remains CHANGES REQUESTED for that old head. Its original negative attempts are NOT rewritten or reclassified.  
**Classification:** Focused R1 evidence/presentation wiring correction; no changed physical law, integrator, numerical threshold, model_runs presenter, existing store engine, or renderer. **No source files, source PR, original saved artifacts, or old review were modified.**

## Exact identity and provenance

I downloaded the **original** exact-head [source snapshot artifact 14238767336](https://github.com/physicsvigilante/emfeeld/actions/runs/43896101372), verified ZIP SHA256 **adb773b583db0f94d61c75c230cb98574378e6ca53d444650ef86e6a5a0e8c4a** and clean CRC, verified contained original tested-source.tar SHA256 **d92de608f8aa2e9e66a99fe9164f2dc3fda6e516396635095c52a6be02503725**, and independently added its **346 tracked files** into a disposable Git index. Git write-tree gave **ce20aa49d978c94150edbbf017d8fae1e2f6f896**. GitHub Git-object reads independently confirmed head/tree, merge-preview/tree and parents. GitHub original-to-corrected comparison reports two commits and **only three modified paths**: README.md (+20), src/emfeeld/scenario_ensembles.py (+40/-10), tests/test_scenario_ensembles.py (+110/-2).

The reviewer read the full current prompt, FOLLOW-UP-02, old review-01, author response, author archive audit, Issue #24, central PROTOCOL/RISK-POLICY/AGENTS, source AGENTS, and relevant native-model, scenario-ensemble and viewer code/contracts. The author response is contextual evidence, not my verdict.

## F1 — BLOCKER on historical source: foreign sealed evidence screenshot corruption

**Corrected: PASS in novel reviewer-owned executions.** Relevant source: [scenario_ensembles.py, screenshot admission near line 488](https://github.com/physicsvigilante/emfeeld/blob/a56b4680a90647ad4af03a52a0b9053807d10a7b/src/emfeeld/scenario_ensembles.py#L488-L512), before [view_ensemble presenter call near line 557](https://github.com/physicsvigilante/emfeeld/blob/a56b4680a90647ad4af03a52a0b9053807d10a7b/src/emfeeld/scenario_ensembles.py#L514-L565).

Independent setup: staged **two genuinely different sealed native experiments**, E1 (electric line + uniform-field model) and T1 (shell + point model), from the original Linux release. They have different model roots, stores, original template runs, accepted child native runs, ensemble seals and saved comparisons. A third separately sealed G1 case tested read-only partial-comparison behavior. Before tests, original native-run and ensemble inspectors accepted the unchanged studies; all file paths and SHA256 bytes for all three studies were snapshotted.

With valid E1 fresh baseline selected, I invoked the **real scenario_ensembles CLI parser/selector** through an external runpy wrapper that intercepted only the final model_runs.present_run function and recorded invocations. Each of the following *fresh proposed screenshot paths* was refused with a nonzero input-error exit **before even entering the intercepted presenter**: under T1 parent native template; under T1 accepted member native run; under T1 baseline native run; under T1 sealed ensemble; under T1 original model store; under T1 sealed comparison; under a distinct pending/unsealed ensemble marker; and through symlinked parents into foreign native template, model store and nested member run. A preexisting screenshot directory was also refused. **All eleven refusals** left their requested screenshot paths absent (except the deliberately preexisting directory, which remained unchanged), created no protected-root files, and left every original E1/T1/G1 path-and-byte inventory exactly unchanged. The original T1/E1/G1 read-only inspectors continued to accept their respectively complete/complete/partial states.

A fresh external destination **was admitted and delegated** to the correct E1 saved baseline without modifying protected inputs. An additional reviewer execution used the **unchanged real model_runs.present_run and real receipt-writing logic**, substituting a minimal plotter ONLY because this environment lacks PyVista. It actually created screenshot and presentation receipt in a fresh external directory reached through an ordinary benign symlinked parent; verified frame hash, original native integrity SHA, exact revision reference and no changes to the sealed ensemble/store/template. **That locally generated PNG is a graphics mock, explicitly NOT real PyVista evidence.** The independently audited original CI E1/G1 PNGs below are real PyVista captures.

The boundary is an ordinary resolved-path, recognizable-evidence-root protection, not a guarantee against malicious concurrent writers, filesystem races, arbitrary hidden protected roots or an adversary able to rewrite/reseal all integrity records.

## F2 — MAJOR on historical source: member literally named baseline

**Corrected: PASS in novel reviewer-owned executions.** Relevant source: [new native run-ID namespace near line 39](https://github.com/physicsvigilante/emfeeld/blob/a56b4680a90647ad4af03a52a0b9053807d10a7b/src/emfeeld/scenario_ensembles.py#L39-L43), [view selector and source-bound receipt near lines 529–564](https://github.com/physicsvigilante/emfeeld/blob/a56b4680a90647ad4af03a52a0b9053807d10a7b/src/emfeeld/scenario_ensembles.py#L529-L564).

I independently constructed **a new accepted four-member E1 native ensemble** from a newly imported pristine source/store and original sealed template; two additional members had independently authored distinct line-source positions, strengths and stable physical IDs. Its third (index 3, nonfirst) member was literally named **baseline**. All four member V3 revisions, native computations and comparisons completed, with distinct physical revision references. The actual CLI entrypoint/parser was invoked with both separate selectors; only the final unavailable graphical presenter was instrumented, so these executions test real run generation, CLI selection, exact saved-run inspection, provenance receipt and delegations, not offscreen visualization.

| Property | --baseline | --member baseline |
|---|---|---|
| Reported selection | baseline | member:baseline |
| selection_kind | fresh_baseline | member |
| member_id | null | baseline |
| Saved run_path | baseline | member-03/run |
| Recorded run_id | ensemble-R1-review-four-baseline | ensemble-R1-review-four-m-baseline |
| Exact revision SHA256 | 07b093eca8c8109ef41ad35a077340310416fed33fb9c9455b6361de355caba0 | bec45668e7574fa1c194c89226da5e6f2d014ba4f0fd1373ca969c3bcdb4e769 |
| Original native integrity.json SHA256 | 5ea0268a8c4c267c137978f51279c6a104b91faeddcfe9cdb64d232cffb32fd9 | dfec1275563f06da5fda3ca2e4af424c1a8105d4eb3963155a4c205d275fa796 |

For **each** selection, the CLI receipt's saved path, run ID, exact revision object and run_integrity_sha256 matched the independently read original run.json and integrity.json. The two references, run seals, run IDs and labels were all distinct; all original saved study bytes remained unchanged. Maximum 25-character ensemble and member IDs yield a **62-character** newly generated native ID, accepted by the existing 64-character identifier grammar; the baseline/member namespaces remain disjoint.

**Backward compatibility was executed against real old-source-saved data:** I downloaded old-head source snapshot artifact 14235101355 (original ZIP SHA256 **c23454c0d0993202bf4b717fb4524f5b8fc56849a32ca131b9228d720d77596f**) and separately executed its unmodified old source to construct a complete four-member ensemble with a third member literally named baseline. The two old native run.json entries really do both contain **ensemble-R1-review-four-baseline**, reproducing the historical ID collision. The corrected selector, without rewriting/migrating old evidence, returned distinct selection_kind, member_id, run_path, exact reference and original integrity-seal hashes. **All 169 historical study files stayed byte-identical** in the reviewer read-only view experiment; both original native IDs remained exactly as saved.

This supports unambiguous **receipts**, not an assertion that the historical renderer's title embedded distinct run IDs. Old native run IDs were intentionally not retroactively changed.

## Nearby controls — independently exercised

The reviewer additionally observed all of the following without a new source defect:

- **G1 honest partial:** saved G1 ensemble comparison remains partial because a baseline body is genuinely absent, while selected hypothesis-B's native trajectory is complete and its saved sample index 2 is viewable. The return reports ensemble_status=partial, selection_kind=member and exact member-02/run, with no fabricated comparison completeness.
- **Unviewable native states:** newly authored rejected V3 member and a separately accepted-but-native-partial member refused presentation; the separate accepted complete sibling remained independently viewable.
- **Read-only evidence:** mutated/re-signed ensemble completion summary, original accepted and rejected store proposal.json byte changes (including whitespace-only), original template run.json byte change, and a stale unrelated T1 template all refused before presenter invocation. No new screenshot output was made. The inherited store decision.json parsed-equality boundary was not widened or mislabeled as a regression.
- **Selections and sampling:** missing/unknown/conflicting selectors refuse; static T1 nonzero sample rejects; trajectory E1 out-of-range sample (999) was also rejected by **actual unmocked model_runs.present_run** before screenshot directory creation.
- **Legacy and PR #23:** normal inspect returned its sealed result; invalid run/inspect flag combinations and missing run output refused without writes; an authored raw JSON 1e400 nested analysis value and a static-mode/trajectory-observation contradiction both failed before output or revision creation.
- **Normal external path:** legitimate external screenshot parent symlink admitted through unchanged native receipt path; symlinks into protected parent paths refused.

**Source-test replay, separately identified:** I ran the exact pinned source's existing focused tests with CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, pytest 9.0.2, warnings-as-errors, and no PyVista: **62 passed in 4.54 seconds**. These 62 are the *author's regression definitions*, NOT an extra set of independently authored cases. A separate attempt to rerun the whole 1,464-test local suite reached roughly 24% before the execution time limit and did **not** complete; this is **not** reported as a full reviewer pass or a failed assertion. Hosted CI's full-suite results remain attributed to CI/author qualification.

## Independently inspected original Linux/Windows native release evidence

These are independently downloaded **original ZIP bytes**, not copied screenshots from a narrative or image mocks.

| Release | Original artifact | ZIP SHA256 (reviewer matched) | Result |
|---|---|---|---|
| Linux Ubuntu 24.04 | [14239164323](https://github.com/physicsvigilante/emfeeld/actions/runs/43896101641/artifacts/14239164323) | 46f5580399c9333aff41523915f88f98f41dee06a799d182609d54375c76bb2a | PASS |
| Windows Server 2022 | [14240032272](https://github.com/physicsvigilante/emfeeld/actions/runs/43896101641/artifacts/14240032272) | e16ae19f7a48f6c7181217952ebfd4768cb0d7c5b53d99fb609d0ca2cae04d8d | PASS |

For **each original ZIP separately**, my read-only script verified 2,157 unique entries, no ZIP CRC errors, **33 actual saved inventories** (21 run/ensemble/comparison roots and 12 nested native), **12 original complete native runs**, **60 original run-input SHA bindings**, **six sealed comparison request bindings**, and **six exact accepted original model-store proposal hashes**. I executed the pinned source's real read-only inspectors against E1/G1/T1 from each archive: E1 and T1 complete, G1 honestly partial. Each OS has **32 ok comparison observations and two typed unavailable, code=unknown_operand**, specifically absent G1 baseline bodies, not silently reassigned by position.

I opened the original real-PyVista E1/G1 images, and independently decoded and hashed the exact four original archived PNG files (each 1200 × 850 and over 2,300 unique RGB colors). Each **presentation.json.frame_sha256 matches the exact original PNG**, and each **run_integrity_sha256, run_id and full revision reference matches the intended saved native run**, with recorded sample index 0 and recorded time 0.0 s.

| Original image | Verified PNG SHA256 |
|---|---|
| Linux E1 fresh baseline | 8ca503af4673d9d547b4ce919140a3afd1d6638f3112fbe02ac1fe62132b2b8f |
| Linux G1 hypothesis-B | 2a2eab68ef0e3bf8daf1c80591e3dc100c4e22f84e6cdad19dc495efa2c057ac |
| Windows E1 fresh baseline | 364b2018f3db54ee5a3d7c5d4d28891ff985f96e7c041d4c4cbac3bb3794013a |
| Windows G1 hypothesis-B | 1999ff1a8ec200c2eccf70163db1554bc41213c6efed96112f2d3969a440d0d2 |

Visible labels differentiate electric potential in **V** from gravitational potential in **J/kg**; slides show fixed 0-sample views, trajectory paths, a source-specific potential reference and disclaimers on schematic particle markers, truncated infinite geometry, display-time versus physical time, no collisions/backreaction. These are source-recorded offscreen **state** views, not reintegration, a physical inter-hypothesis transition, independent numerical derivation of every scene, teacher acceptance, or proof of manual Windows pointer/slider behavior.

Exact-head CI metadata was also checked directly: [Linux/Windows clean-install run 43896101641](https://github.com/physicsvigilante/emfeeld/actions/runs/43896101641) SUCCESS for both jobs **at the requested head**, [separate real-PyVista run 43896101195](https://github.com/physicsvigilante/emfeeld/actions/runs/43896101195) SUCCESS at the head, and [source snapshot 43896101372](https://github.com/physicsvigilante/emfeeld/actions/runs/43896101372) SUCCESS at the head. Per-job **1,464 headless + 18 historical behavioral + 33 real-PyVista** and the 62 focused replay counts come from the **hosted/author logs**, not my independent full-suite execution. The frozen historical whole-file guard was deselected on current source, as documented.

## New review attempts and first-attempt preservation

I did not reuse author-owned test cases as the whole independent review. My tests construct distinct disposable actual E1/T1/G1 saved experiments, an independently modified four-member physical E1 ensemble, a genuine **old-source-built** four-member collision case, changed sealed manifests, store proposal bytes, native partial/rejection cases, and external CLI/receipt checks. Reported test attempts:

1. **First external harness v1 preserved unchanged**: script SHA256 **786aabed5d05d8b24179cc43513e8fdf8d676cd720c7001a81ad849b4a1bb196**, original stdout SHA256 **02141c4fee6db10834e79f1d33d99166441980913f317dfc93ad1813f209cc66**. Initial foreign-seal refusals **passed**, but the harness wrongly expected a deliberately preexisting screenshot directory to be absent. Its attempted CLI presenter monkeypatch via a second sitecustomize module was not loaded because this execution environment already had a higher-priority sitecustomize; later positive commands reached real PyVista and failed with **ModuleNotFoundError: pyvista**. Execution was time-limited before the full suite finished. These are **reviewer harness/environment errors**, not source regressions; the first log was retained, never silently turned green.
2. **Corrected external harness v2**, with a direct CLI parser/runpy wrapper intercepting *only* the final presentation call, retained unchanged: script SHA256 **ddcbc3a9747c1ea6fbd368cadee88d4607f0ab2600eb95814a51a7e3d832cdc7**, stdout SHA256 **80737ebfea9dee20b83ae86142c1f8f42b609ad9590afd0c2dcf917a2c0fa116**. Its **18 completed named independent checks passed** (including F1 eleven refusals and external admission, F2 new and historical four-member identity, G1 partial and native refusal cases); runner time limit interrupted later cases. Do not count those later cases from this run.
3. **Split independent remainder v3** executed **10/10 named checks PASS**, including re-signed ensemble, accepted original proposal byte tamper, template tamper, stale template, selectors, samples, old commands and PR #23 preflight guards. Script SHA256 **bef7b98ac315253fa29dbdc59a12095fb003dc4bc07db5d4787e3f704726358f**; JSON results SHA256 **0581754b1bea2a57d10216a399ea02fab8b0de80a0fb5b32e17a819d23b5355d**.
4. **Additional independent single checks PASS:** changed original **rejected** proposal.json bytes refused with no renderer or screenshot; real native presenter/receipt generation with benign external symlinked parent and mocked graphics PASS, original sealed files untouched. Archived release auditor separately passed all enumerated checks on both original ZIPs. The local presenter's substitute 48×36 PNG is never confused with real archived 1200×850 PyVista screenshots.
5. **Original review-01 remains untouched and historically CHANGES REQUESTED.** Its first F1 corrupted foreign evidence on old source and its F2 duplicate old ID were genuine old-source defects. This report is a **new PASS on new head only**. The older reviewer’s overly broad store decision.json raw-whitespace expectation remains characterized as an inherited parsed-JSON boundary, not a demonstrated new PR #25 regression.

## Separate scope judgments

| Dimension | Finding | Basis and boundary |
|---|---|---|
| Source interpretation fidelity | NOT RE-QUALIFIED | No interpretation/physics-source changes in scoped correction; original scenario assumptions remain illustrative |
| Physical/numerical correctness | NO NEW REGRESSION OBSERVED / NOT INDEPENDENTLY CERTIFIED | New/replayed native cases and archive native seals pass; no new physics laws or independent numerical derivation of full system |
| Native simulation and measurement coverage | PASS for targeted preserved cases | Actual fresh E1 four-member native calculation, G1 honest partial and invalid/partial/refused variants, 12 sealed original runs/OS |
| Evidence integrity and source provenance | **PASS for F1/F2** | Reviewer-owned protected-root write refusal, exact identities and hashes, historical IDs, original ZIP/PNG native receipts |
| Teacher-facing usefulness | UNKNOWN | Single saved-scenario viewing demonstrated; no classroom user testing or manual desktop pointer evaluation |
| Textbook-answer completeness | NOT APPLICABLE | No textbook-answer generation in this bounded selector change |

## Final disposition and release advice

**PASS — the independently demonstrated old F1 blocker and F2 major issue are corrected on exactly a56b4680a90647ad4af03a52a0b9053807d10a7b / tree ce20aa49d978c94150edbbf017d8fae1e2f6f896. No remaining material R1 correction defect was demonstrated.** The preserved first harness failures are explained rather than erased, the original historical review remains negative on its old head, and the current CI/original-release visual evidence is not misrepresented as a locally run real-PyVista test.

**Residual limitations:** reviewer environment lacks PyVista (so direct live real-PyVista positive is independently verified from immutable CI images/receipts, not rerendered here); local full 1,464-test attempt did not finish; no guarantee against hostile concurrent path writers or full malicious re-sealing; no manual Windows pointer/slider or teacher certification; historic identical run IDs remain intentionally unchanged. None requires changing this bounded correction under Issue #24's scoped R1 gate. Escalate on a newly demonstrated source regression or any change to physical/evidence semantics.

**Do not merge based only on this report.** Leave source PR #25 unchanged until Chat A verifies the unchanged exact head, owner approval and qualified CI; after any authorized merge, run the separate fresh post-merge main qualification. This review is published solely to the central review_sandbox and grants no production merge permission.
