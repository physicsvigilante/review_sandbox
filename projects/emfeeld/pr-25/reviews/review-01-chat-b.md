# Review 01 — Chat B independent focused R1 review of EM Fields PR #25

**Verdict: CHANGES REQUESTED** — source head **4fe896ff6bb98d21a090bc16a84fe26145f9f5e7**. Two reproducible identity/presentation problems remain within the explicitly requested R1 review scope. This is a separate-context reviewer report, **not source merge approval**, not a new physics-law audit, and not a Windows manual interaction certification.

**Review date:** 2026-11-16 (Asia/Kolkata). **Source:** [emfeeld PR #25](https://github.com/physicsvigilante/emfeeld/pull/25); [Issue #24](https://github.com/physicsvigilante/emfeeld/issues/24). **Handoff:** [request](../REQUEST.md), [current prompt 02](../REVIEWER-PROMPT-02.md), [author ZIP audit](../AUTHOR-ARCHIVE-AUDIT-01.md). Prompt 01's pending-Windows statements are historical; Windows subsequently completed successfully.

## 1. Exact frozen provenance and method

- Qualified source base **bf6a18399c604136dd363ad94d40557dbe2c2543**, Git tree **e7ddc4c6c44106bf3113f7c1e176b21490a7cf5c**.
- Reviewed PR head **4fe896ff6bb98d21a090bc16a84fe26145f9f5e7**, canonical Git tree **4df3703346ec7cba1ab74fcd6daa40796a535bf3**.
- CI merge-preview **75f818bdb199ad97ae036bd1dea380f03d7e71f6**: independently fetched Git commit; parents are the exact base then head above; its tree is also **4df3703346ec7cba1ab74fcd6daa40796a535bf3**.
- Independently downloaded the **original** source snapshot artifact **14235101355** from [workflow 43886746421](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746421). Raw ZIP SHA-256 **c23454c0d0993202bf4b717fb4524f5b8fc56849a32ca131b9228d720d77596f**. Extracted the original tested-source.tar and rebuilt an isolated Git index from all **346 tracked files**: git write-tree independently returned the exact **4df3703346ec7cba1ab74fcd6daa40796a535bf3**. Four changed code/documentation/CI paths were identified; no old solver, model_runs renderer or native inspect source was changed by PR #25.
- Direct GitHub API check of [Linux/Windows workflow 43886746384](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746384): completed/success on both Ubuntu 24.04 job **133366826330** and Windows 2022 job **133366825905**. [Separate real-PyVista workflow 43886746161](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746161), job **133366824764**, also completed/success. The source snapshot workflow completed/success. Each run is bound to the pinned head and base. The author's counts (1,456 headless, 18 current historical, 33 real-PyVista per OS, plus a 54-case focused rerun already included in headless) are **author/CI evidence**, not extra independently authored reviewer tests.
- Reviewer local runtime: Linux, Python **3.13.5**, NumPy **2.3.5**, SciPy **1.17.0**, pytest **9.0.2**. The original pinned source was imported from the extracted tar. **PyVista unavailable locally**; graphical construction in the failure reproducer was explicitly stubbed, while original Linux and Windows real-PyVista screenshots were inspected independently from GitHub artifacts. No source branch, saved experiment or user-local install was modified.

## 2. Findings requiring correction

### F1 — BLOCKER: screenshot destination can corrupt unrelated sealed evidence

**Observed production path, not hypothetical.** The new [view_ensemble screenshot check, lines 515–522](https://github.com/physicsvigilante/emfeeld/blob/4fe896ff6bb98d21a090bc16a84fe26145f9f5e7/src/emfeeld/scenario_ensembles.py#L515-L522) rejects existing destinations and destinations beneath only the supplied ensemble, store and parent template. It **accepts a fresh directory inside a different, unrelated existing sealed native run**. [model_runs.present_run lines 255–283](https://github.com/physicsvigilante/emfeeld/blob/4fe896ff6bb98d21a090bc16a84fe26145f9f5e7/src/emfeeld/model_runs.py#L255-L283) then creates that directory and writes the PNG and presentation receipt.

**Independent reproduction:**
1. Use the original Linux release artifact's valid **scenario-ensembles/E1/{ensemble,store,parent-template}** to select the E1 baseline.
2. Copy the separately sealed **scenario-ensembles/T1/parent-template** to a disposable directory named foreign; first confirm model_runs.inspect_run(foreign) succeeds.
3. Pass screenshot_output = foreign / "injected-presentation" to scenario_ensembles.view_ensemble(E1_ensemble, store_path=E1_store, using=E1_template, baseline=True).
4. With a stubbed make_plotter only (the real view_ensemble and model_runs.present_run logic unchanged), outcome is **complete**, the native presentation code writes foreign/injected-presentation/frame.png and presentation.json, and subsequent model_runs.inspect_run(foreign) fails **run_integrity: run file inventory or exact bytes changed**. No original foreign files were overwritten: the violation is the two unsealed new files inside a previously sealed run. Original archives were preserved; only the disposable copy was modified.
5. A separate refusal-expectation test confirms this failure occurs *before* any permissible renderer call: the new view selector calls the renderer rather than rejecting this preexisting evidence directory.

**Why this matters:** Issue #24 expressly requires fresh screenshot outputs outside **previously saved evidence**, not just outside the three current inputs. Any other valid saved run is at risk. Rendering itself need not contain any physics error to break that run's seal. An external screenshot path and protected paths through direct/symlinked parents were separately tested successfully.

**Required correction:** Strengthen screenshot destination admission before model_runs.present_run. Reject destinations whose resolved ancestor is any recognizable existing sealed run, ensemble, model store or protected evidence root (including unrelated roots and parent symlink aliases); keep legitimate fresh external paths usable. Add a negative regression with two independent sealed runs and an unaffected-source inventory check. Document the remaining filesystem race/TOCTOU limit; do not claim distributed or hostile-writer ACID.

### F2 — MAJOR: baseline-named member receives identical reported selector and run_id as the fresh baseline

**Observed on a newly executed, valid four-member ensemble.** A member literally named **baseline** is valid under Issue #24 and was deliberately placed at third member index, unrelated to its proposal/revision ID. The new selector correctly opens different native run directories and different exact revision references:

| Invocation | Actual native path | Saved revision ID | Reported selection | Reported run_id |
|---|---|---|---|---|
| --baseline | baseline | root | baseline | ensemble-four-member-review-baseline |
| --member baseline | member-03/run | variant-3 | baseline | ensemble-four-member-review-baseline |

The first three columns distinguish the underlying physical runs correctly. **But the selector label and recorded run_id collide**, undermining unambiguous reporting/provenance for precisely the edge case called out in the acceptance criteria. The inherited [_run_id generator, lines 39–40](https://github.com/physicsvigilante/emfeeld/blob/4fe896ff6bb98d21a090bc16a84fe26145f9f5e7/src/emfeeld/scenario_ensembles.py#L39-L40) gives both variants the same run_id. The new [view result, lines 498–535](https://github.com/physicsvigilante/emfeeld/blob/4fe896ff6bb98d21a090bc16a84fe26145f9f5e7/src/emfeeld/scenario_ensembles.py#L498-L535) gives both variants the same selection field. Two different reference hashes/path bindings prevented the *wrong run* being shown; do not misstate this as a physics retargeting error.

**Required correction:** Return an explicit discriminator (for example, selection_kind = fresh_baseline vs member, plus member_id where applicable) alongside exact native reference/path identity. Ensure **newly generated** saved runs have noncolliding run identifiers for these legal selections, or establish and document an equivalently unambiguous source-bound identifier contract. Preserve historical sealed files unchanged rather than retroactively renaming prior run IDs. Add a reviewer-meaningful CLI regression that checks **both** path/reference correctness and identification, not just distinct selected paths.

## 3. Independently executed positive and negative tests

The new test logic is reviewer-owned and located **outside the extracted source repository**, so it is not a self-review of the author's 21 additions. Test snapshots compare every file path and full-file SHA-256 in the original ensemble, model store and parent native template before and after each view/refusal. All intentional mutations were confined to disposable copies.

- **Four-member native construction and binding:** created four accepted V3 members with non-positional IDs, including a member named baseline; inspected sealed output and verified baseline plus all four native path/reference selections, no input writes. Correct target selection PASS; the distinct-run-identity assertion later revealed F2.
- **Partial comparison:** on **both original Linux and Windows G1** archives, inspect_ensemble returned aggregate partial while hypothesis-B native run was complete with comparison partial. Selecting B with saved sample index 2 delegated exactly to member-02/run, preserved exact run_id and revision reference, and wrote no inputs. PASS.
- **Refusal/read-only:** independent accepted and rejected V3 store proposal **original byte** whitespace tampering, ensemble/parent template whitespace changes, a re-signed contradictory ensemble summary, absent/duplicate/unknown selectors, negative/noninteger sample indices, rejected V3 and accepted-but-native-incomplete members, stale unrelated template, and guessed member subpaths refused before presentation. Independent sibling remained viewable. PASS for the stated exact proposal-byte contract.
- **Screenshot boundaries:** direct paths inside the current ensemble/store/template, existing destination, existing symlink and parent symlink into the ensemble all refused; genuinely fresh external destinations, including an external symlink parent, delegated correctly. PASS. A path under an **unrelated sealed native run failed**, F1.
- **Native sampling:** the actual existing model_runs.present_run rejected out-of-range trajectory samples and a nonzero static sample before invoking a fake make_plotter; new view wrapper did the same for a G1 out-of-range sample. PASS. No locally fabricated PyVista screenshot was treated as actual rendering.
- **Old commands and PR #23 guards:** CLI inspect returned the original deterministic report, inspect --output and view-only flags on inspect/run refused, and run with missing output refused without file changes. A new raw JSON 1e400 numeric preflight case and static/trajectory mixed grammar case refused before any revision/output write. PASS.
- **Existing pinned author-test replay, separately labeled:** PYTHONPATH=src:tests pytest -q tests/test_scenario_ensembles.py → **54 passed in 5.49 s**. The 54 definitions include the existing PR #23 guards and author's PR #25 tests; they are **not** new reviewer-owned definitions.

**Preserved attempt sequence:**
1. Original reviewer suite: **26 passed / 2 failed**. First negative: unrelated sealed evidence screenshot not refused (F1). Second negative: expected a whitespace-only mutation of *stored decision.json* to fail inspection. This second expectation was too broad for the explicitly qualified raw-proposal-byte contract and is corrected below; the failure is preserved here, not deleted. Original script SHA-256 **b75c11715a2d17845324798c0cd5200663e8f1ab1ed2ac5dfd8be41a41efb2ac**, original log SHA-256 **fb2c663c0b028bdd3f0a975f218b401b1b9f24770e1a22e7a30087ceab9819f6**.
2. Second suite recorded the inherited stored-decision boundary as a passing characterization rather than a refusal requirement: **27 passed / 1 failed**, with the F1 failure unchanged. Script SHA-256 **4e74a3910ab41c05bf0eb65b324cd198d072fcc643bc29565def93c0d7c63681**, log SHA-256 **3044125f70a9a0c87cd96908694a709261c3886535ebd1462ca7e74f58953091**.
3. Expanded third suite added true CLI baseline/member baseline identity and stale-reference/symlink/sampling challenges: **30 passed / 2 failed** — F1 plus newly exposed F2. Script SHA-256 **aba84d6bb0e45193899c7588c34463df4398f956d8599c6ef1dbef1f90b57bd0**, log SHA-256 **98b85e9a8e5312402f4061272b37ff1cc35fce21c58987d499ededf9f677a358**. A separate run of the remaining tests gives **30 passed / 2 deselected**, not a sign-off shortcut. Both failing source cases remain open.
4. Independent disposable-copy F1 end-to-end evidence: return status complete; events make_plotter → plot.show → plot.screenshot → plot.close; two new screenshot/receipt files in foreign sealed T1 run; subsequent original run inspector → run_integrity. Reproducer log SHA-256 **4223b546e96c41a15943b7b4b7b1d9f2fc7b378c3a60d71da2e469a7921cdb5b**.
5. F2 standalone identity trace: paths baseline versus member-03/run; differing revision IDs root versus variant-3; **equal selection labels and equal run_id**. Log SHA-256 **6b247f98ebdeb5071a5e7b4c6a511f024262db21091dc0822184152c6a6a9ffa**.

### Inherited boundary, not counted as a new PR #25 blocker

The original store's **decision.json** is compared as parsed JSON with the per-ensemble decision, not by exact original decision-file bytes. Whitespace-only modification to the store decision.json can therefore leave a valid inspect result. This behavior exists in the **qualified base's unchanged inspect_ensemble**, whereas the original accepted/rejected **proposal.json bytes** are explicitly SHA-256-bound and our independent whitespace tampering of those original proposal bytes was correctly refused. The reviewer's first strict-decision-raw-byte expectation was overbroad relative to this R1 contract. Record stronger store decision-byte attestation as an optional separate hardening/design decision, not as a falsely proven new selector regression.

## 4. Original Linux/Windows artifact and actual PyVista evidence audit

Original downloaded release ZIPs were independently hashed and CRC-tested:

| OS | GitHub artifact | Original ZIP SHA-256 | Independent archive/seal results |
|---|---|---|---|
| Linux | [14236425127](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746384/artifacts/14236425127) | 573b23020f3b2d5471152242352a017b18e05761cb6afdbb7ad7fea714ca44ec | 2,157 unique CRC-clean entries; 21 matching full-tree top-level manifests, 12 matching native manifests, 12 saved native runs and 60 input hash bindings |
| Windows | [14235259284](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746384/artifacts/14235259284) | 6182044d7b103ba4e8e0f46e1c9501228977d760259508cd08f295bfc7417ad8 | Same independent counts/checks |

Also executed the exact source **inspect_ensemble** on each of the six archived OS × E1/G1/T1 cases: E1 and T1 complete, G1 honestly partial. Independently counted six cross-comparison results per OS: **32 ok / 2 unavailable**. No unavailable body was retargeted as a different positional index.

**Actual original real-PyVista captures inspected, not mock output:** Linux and Windows E1 fresh baseline plus G1 accepted sibling hypothesis-B. Each is **1200×850**, visibly nonblank with over 2,300 unique RGB colors, and source-labelled as electric potential **V** or gravitational potential **J/kg** as applicable. E1 shows its line/uniform field, test particle and recorded curve; G1 shows a sphere/point configuration and recorded particle paths. Saved PNG SHA-256 matches presentation.json.frame_sha256; presentation.json.run_integrity_sha256 matches the bytes of the **corresponding original native run/integrity.json**; saved run_id and model revision reference match run.json and the command log; sample_index **0**, time_s **0.0**. G1 member is not falsely called a complete comparison. The four archived PNG SHA-256 values are:

- Linux E1: **8ca503af4673d9d547b4ce919140a3afd1d6638f3112fbe02ac1fe62132b2b8f**; Linux G1: **e1d683d0dd49d9b87d1766258888e749815054b612de6af2a493ca0fae6b72d9**.
- Windows E1: **364b2018f3db54ee5a3d7c5d4d28891ff985f96e7c041d4c4cbac3bb3794013a**; Windows G1: **cff5f498218f3e9bf13c8625748e00a0421512aae3c754e86acaadf45ba123ca**.

These captures depict **saved-state presentation only**, not re-integration or a physical transition; the screenshots are not teacher acceptance. Linux/Windows **offscreen** execution does not establish manual Windows mouse/keyboard/slider interaction.

## 5. Disposition and next gate

**CHANGES REQUESTED on the exact head above.** F1 is a directly demonstrated sealed-evidence integrity violation; F2 is a directly demonstrated selector/provenance ambiguity on a supported legal member ID. Neither is evidence of changed physical laws or incorrect original native fields/trajectories. Fix both with narrow regressions, fresh head SHA/tree and appropriate current-head Linux/Windows/real-PyVista qualification. Preserve first attempts and historical source artifacts unchanged. The implementer may provide a focused response with reproduction/correction evidence; further review should be scoped to the corrected behavior and affected regressions, escalating only if evidence/physics semantics change. The PR must remain unmerged until corrections and the separate owner/source merge gates are satisfied.

**Not established here:** independent live PyVista rendering from this reviewer environment; manual Windows pointer qualification; classroom usefulness; human physics certification; resistance to malicious full hash re-sealing, concurrent writers or filesystem races. No source PR, central prior review, user installation or saved model was modified by this review.
