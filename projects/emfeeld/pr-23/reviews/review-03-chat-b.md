# EM Fields PR #23 — third targeted independent Chat B R2 review (review-03)

**Scoped verdict: PASS** for the remaining **R2-01 static-analysis / trajectory-observation preflight blocker**, with representative **R2-02 and R2-03 regressions PASS**. Reviewed exact source commit **`7bbdea64a81c2e3bea2b24c59a2d5866afdda707`**, canonical Git tree **`e7ddc4c6c44106bf3113f7c1e176b21490a7cf5c`**, on **2026-11-16 (Asia/Kolkata)**. This is a *narrow, independently executed corrective review*, not a new full physics review, a human certification, or authorization to merge. Source PR #23 was observed **OPEN, DRAFT, UNMERGED**.

The earlier independently authored [review-01](review-01-chat-b.md) (**CHANGES REQUESTED**, source `38773a5...`, blob `e2ceb284c7183b91dcbd24ee2c9eb6b97ffcd814`) and [review-02](review-02-chat-b.md) (**CHANGES REQUESTED**, source `5738fec0...`, blob `f50bea4768ce4b7707e5f3068d4cbb2ccadd38ed`) retain their original verdicts on their original source commits. Both original blob SHAs were checked before publication; neither review was edited.

## Identity, source and review boundaries

- Request: [FOLLOW-UP-03](../FOLLOW-UP-03.md); [reviewer prompt 03](../REVIEWER-PROMPT-03.md); [source PR #23](https://github.com/physicsvigilante/emfeeld/pull/23); central [protocol](../../../../PROTOCOL.md) and [R2 risk policy](../../../../REVIEW-RISK-POLICY.md).
- GitHub Git-commit object independently reports exact `7bbdea64...` tree `e7ddc4c6...`. The draft PR's current head matched; base is qualified `f0fc993dae1831432ca43b651a12e64fa0b2fdd5`. Merge-preview `12b75e59b3343c4583a5764484774bbf3b9b11dc` has that **same tree** and parents exactly qualified base + reviewed head.
- [Diff from review-02 head to reviewed head](https://github.com/physicsvigilante/emfeeld/compare/5738fec0d22deb59d0f146dc75b8a9b33db64486...7bbdea64a81c2e3bea2b24c59a2d5866afdda707): **two commits, two paths only**: `src/emfeeld/scenario_ensembles.py` (+8 lines) and `tests/test_scenario_ensembles.py` (+44 lines); no deleted code. No changed physics law, integrator, solver thresholds, existing V3 store or viewer implementation.
- I downloaded the **original** [source snapshot workflow #43871642044](https://github.com/physicsvigilante/emfeeld/actions/runs/43871642044) artifact **14227622960**. Original ZIP SHA256 **`16ff2509ad223fc7f8eedf046768f7efbfbc9e7ecce11da26c524909038f2b43`**, CRC clean. Inner `tested-source.tar` SHA256 **`7e8cf776546f6afb21a36f77e398029163919e84d188065ad6644943f29f73f3`**. Extracted **346 tracked Git files**, initialized a disposable Git index, and independently reproduced the exact canonical tree with `git add -A; git write-tree`: **`e7ddc4c6c44106bf3113f7c1e176b21490a7cf5c`**. Source files were not patched.
- Inspected corrected `_native_grammar`, `validate_spec`, `run_ensemble`, `inspect_ensemble`, the unchanged `model_runs.lower`, native observation grammar and prior reviewer reports. The new guard checks for `trajectory_sample` or `trajectory_event` under `analysis.mode != 'trajectory'` *inside* `validate_spec`, before output creation or `ModelStore.revise`.

## Independently authored and executed tests

**Environment:** disposable Linux container, CPython **3.13.5**, NumPy **2.3.5**, SciPy **1.17.0**, pytest **9.0.2**. No pip/Conda installs, user-machine changes, GitHub source writes or saved-study edits. The reviewer code was stored **outside** the 346-file extracted source. Existing fixture utilities were used **only** for normal parent import/configuration and construction of literal valid V3 edits; tests did **not** call the author's ensemble `_spec`, `_member`, `_native_root`, `_run`, or the author's regression test functions.

Independent fixture: two prescribed solid-sphere electric sources, one named test particle `probe`, an immutable sealed native parent run, and two genuinely valid sibling V3 charge-change proposals sharing that parent. Independent world-coordinate field and ordered potential-difference observations used `[0.41,-0.18,0.33]` and `[3.1,0.49,-0.3]` m. The second sibling was intentionally malformed in primary negative cases to prove the first sibling cannot consume an identity. For every expected preflight refusal, the entire model-store and original native-run file inventories were compared **path-for-path and byte-for-byte**, plus no ensemble output, no proposals and exactly one root revision.

**First-attempt preservation, including reviewer harness error:**

| Reviewer-owned execution | Outcome | Log SHA256 |
|---|---|---|
| First batch (27 cases) | **9 passed / 18 failed** because my fixture's *ensemble ID was 26 characters*, over the 25-character limit; the failures were at unrelated ID validation, **not** evidence that the R2-01 guard failed | `f65f9e81e69a9f71ba20b86e38cecedfa44371e7e95fe0c9180786adadbe9bb0` |
| Corrected **reviewer fixture only**, identical 27 cases | **27 passed / 0 failed**; source unchanged | `c7bde80076714037fd296c16238d5e4f10d19153fc6f3a26ece24570af578d19` |
| Final reviewer suite, adding two native plane-crossing controls | **29 passed / 0 failed**, `-W error`; source unchanged | `768e58213aff5e84d71d25f9e85287f232df35c9050e279c26863f2b5f021f08` |

The mistaken original first log was **not replaced**. The original first-harness and corrected second-harness snapshots, final reviewer script, first/second/final logs, native characterization and source manifest were bundled in this conversation's reviewer evidence ZIP, SHA256 **`bd1beea2e9c3b414a5a612d742a6a07ef87c78043ae3a733842e9112bc94d1eb`**. Final reviewer script SHA256 **`4affe8eb6132b6d9ae90031ed3f9c0e3667434698ab91221d1ebe421ca75227c`**.

Reproduction after extraction of the pinned source archive and placement of `reviewer03_tests.py` outside its tree:

```bash
PYTHONPATH=source/src:source/tests:. python -m pytest -q -W error -ra reviewer03_tests.py
```

### R2-01 — PASS: original cross-field blocker independently closed

- Under **static** member-2 analysis, fully valid `trajectory_sample` **position index 0**, **velocity index 0**, and fully specified plane `trajectory_event` requests with `either` and `positive` directions each raised **`RevisionError(code='unsupported_analysis')` before output/revision publication**. I first independently lowered the same observations against the real parent with a genuine trajectory analysis to verify they were valid syntax: this is **not** a dummy-grid out-of-range false positive. A second physically crossing plane event, at **y=0.201 m**, was also refused under static mode.
- An additional case put **both** motion request types in member 1; another placed the bad static member in a **three-member** ensemble. All were rejected before sibling attempts. Original store/template bytes remained exactly equal, proposal-directory count **0**, revision count **1**, and ensemble output directory **absent**. The previously consumed proposal IDs remained available: correcting the spec and rerunning with the *same IDs* produced two accepted, complete sibling results.
- Positive native controls: valid **trajectory** analysis with index-0 and index-10 motion samples produced complete, inspectable sibling runs. A real plane event at **y=0.201 m** returned **`ok` in both siblings**, with independently checked event time inside the modeled interval and saved y-coordinate at the authored plane, and a complete ensemble. An event at **y=0.243 m** appropriately produced a **`no_event`/partial** native outcome for a non-crossing physical trajectory, rather than artificial completion or global grammar failure. A static field-only ensemble remained complete.
- **Physical errors remain per member**, not global schema failures: (a) a syntactically valid but physically stale named `presentation.entity_order` left member 1 complete, member 2's V3 revision **accepted** and its native run **rejected/partial**; (b) a truly invalid physical property in member-2's V3 edit produced a **rejected second proposal** and left the first member complete; (c) an actually missing named particle `ghost` under *valid trajectory mode* was admitted as syntax, then its accepted sibling's native run honestly **rejected/partial**. All corresponding complete/partial ensembles passed deterministic `inspect_ensemble` without rewriting source evidence.
- Four further independent malformed/duplicate grammar or ID combinations were preflight-refused with no writes.

**Conclusion:** The exact previously reproduced R2-01 static/motion grammar contradiction no longer reserves either sibling or publishes a partial result, and representative legitimate member-level physical failures are not erroneously elevated into global preflight rejection.

### R2-02 — PASS within five independent numeric-token probes

Injected the literal JSON numeric token **`1e400`** (not a non-JSON `Infinity` token) at five separately authored nested locations: second-member V3 value, second-member field coordinate, first-member expectation `rtol`, second-member presentation camera component, and second-member trajectory event accuracy `time_atol_s` with a valid trajectory analysis. All five yielded a hard finite-input preflight exception, no ensemble output, zero proposal reservations, one original root revision and byte-identical store/template inventories. The guard is at the new ensemble boundary; no claim is made that legacy shared JSON decoding changed.

### R2-03 — PASS within four independent stored-byte drift probes

Created one **accepted** member and one physically **rejected** member, with a sealed **partial** ensemble that initially inspected successfully. For each member separately, altered **only** the original store `proposals/<sha256(proposal_id)>/proposal.json` by (1) appended whitespace preserving parsed JSON meaning and (2) a semantic JSON change. In all **four** cases, unchanged original `decision.proposal_sha256` no longer matched stored raw bytes; `inspect_ensemble` raised **`RevisionError(code='ensemble_integrity')`**. Read-only inspection did not change store or output inventories; restoring the *exact* original proposal bytes restored inspection without changing the sealed ensemble.

## Exact-head CI and separate author-controlled evidence

Independently queried GitHub workflow/job metadata and original job logs for this **exact head**:

- [Linux/Windows clean-install #43871642152](https://github.com/physicsvigilante/emfeeld/actions/runs/43871642152): **SUCCESS** on Ubuntu 24.04 and Windows 2022. Each job's original log recorded **1,435 headless passed**, **18 historical behavioral passed (one obsolete whole-file freeze test deselected)**, **33 real-PyVista tests passed**, and a **33-pass focused ensemble re-run** already contained in the headless suite. These are **1,486 suite memberships per OS**, not 1,486 distinct new reviewer tests.
- [Separate real-PyVista #43871641853](https://github.com/physicsvigilante/emfeeld/actions/runs/43871641853): **SUCCESS**, with original log recording **1,435 passed** plus successful offscreen render/slider-event steps. It does not establish manual Windows pointer operation.
- [Source snapshot #43871642044](https://github.com/physicsvigilante/emfeeld/actions/runs/43871642044): **SUCCESS** and independently extracted/reconstructed tree as described above.
- I separately reran the **existing 33 author-written focused test definitions** on the pinned source with `-W error`: **33 passed**, log SHA256 **`b1bf4bf9142953638127e8a89bfd0c80008b437f107f2f2e35c4a33e0eacf789`**. These remain explicitly **author-defined**, not part of the 29 novel tests.
- The original Linux/Windows release ZIP integrity, native E1/G1/T1 source/reference checks and 32 fulfilled/two intentionally unavailable saved comparisons are described in [FOLLOW-UP-03](../FOLLOW-UP-03.md) as **author/hosted evidence**. I did **not** independently re-download or re-audit both full release ZIPs in this narrow review, and do not re-label author references as new independent numerical verification.

## Residual limitations and disposition

This review was limited to the repaired cross-field R2-01 preflight, representative R2-02/R2-03 boundaries, nearby member-level behavior, source identity and current CI provenance. It does **not** re-qualify every numerical law, every possible native packet, all 1,435 headless test definitions independently, full Linux/Windows archived scientific receipts, manual Windows viewer interaction or classroom outcomes. An accepted V3 revision is not proof of numerical success; a legitimate event `no_event` remains an honest partial outcome. Checksums are unkeyed evidence, not adversarial cryptographic authentication. Structural local locks are not distributed, crash-safe ACID transactions. Two hypothetical prescribed scenarios are not a physical time transition.

**Final scoped verdict: PASS** on the exact reviewed commit **`7bbdea64a81c2e3bea2b24c59a2d5866afdda707`** / tree **`e7ddc4c6c44106bf3113f7c1e176b21490a7cf5c`**. **R2-01 = PASS** for corrected static/motion preflight; **R2-02 = PASS** on overflow regressions; **R2-03 = PASS** on accepted/rejected stored-proposal-byte regressions. No remaining blocker was reproduced within the specified correction scope.

**No source PR, source branch, source files, existing review reports, merge, CI attempt or saved model was changed by this reviewer.** The owner/source implementer must separately observe all source-specific merge gates, review identity freshness, owner approval and post-merge qualification; this central report is **not** a GitHub required status check or an automatic merge instruction.
