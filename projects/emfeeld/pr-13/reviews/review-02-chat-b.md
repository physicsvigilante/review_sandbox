# EM Fields PR #13 — independent R2 targeted follow-up review 02 (Chat B)

- **Project / source repo:** [physicsvigilante/emfeeld](https://github.com/physicsvigilante/emfeeld).
- **Source PR:** [#13](https://github.com/physicsvigilante/emfeeld/pull/13), draft and unmerged at review.
- **Base SHA:** `c67d1115ad6fc982f29fe113583430e676938902`.
- **Previously reviewed SHA (review 01; preserved):** `766633a60679208f534c5d299578b100d2d29eea`; [original report](review-01-chat-b.md) remains `changes-requested` for that older commit.
- **Exactly reviewed corrected head SHA:** **`e7c772af39c6271cd7a033ec2a006d617a51b442`**.
- **Corrected tree SHA:** **`ea4efcc21e101be8ceb11cbae5c14924e45d172b`**.
- **Correction diff:** [pinned old-to-corrected comparison](https://github.com/physicsvigilante/emfeeld/compare/766633a60679208f534c5d299578b100d2d29eea...e7c772af39c6271cd7a033ec2a006d617a51b442).
- **Reviewer:** Chat B, separate ChatGPT conversation (GPT-6); not an independent human examiner or demonstrably a different model family.
- **Date:** 2026-11-15 UTC.
- **Scope / risk:** **R2 targeted re-review of F-01–F-04 only** under [FOLLOW-UP-02](../FOLLOW-UP-02.md). Did not reopen original physical laws, solver, viewer or general E1/G1/T1 interpretation.
- **Source PR files changed by reviewer?** No. Local test harness and disposable artifact copies only; no source commits, PR changes, CI reruns or merges.
- **Outcome: `pass` (strictly scoped to the four R2 corrections at this exact source SHA).**

## Verdict

**No demonstrated remaining defect in F-01, F-02, F-03 or F-04.** The new guards reject the originally demonstrated counterexamples without breaking representative valid controls. This is **not** approval of unrelated parts of PR #13, a claim of cryptographic provenance, or permission to merge. Owner acceptance remains a separate gate.

## Findings — four previously open issues

### F-01 — RESOLVED — nonzero scalar ratio underflow

- **Corrected source:** [`src/emfeeld/derived_observations.py:25-34,121-151`](https://github.com/physicsvigilante/emfeeld/blob/e7c772af39c6271cd7a033ec2a006d617a51b442/src/emfeeld/derived_observations.py#L121-L151).
- **Independent execution, expected versus actual:** `5e-324 / 1e308` and `-5e-324 / 1e308` both return **`unavailable/numeric_range`**, not a successful fabricated zero; a valid 3-vector field-magnitude case with the same extreme ratio also refuses. `0.0 / 1e308` returns successful zero; `5e-324 / 1.0` remains successful with nonzero subnormal output; `-5e-324 / -1.0` remains positive subnormal; `1e-320/1e-320` is 1.0; signed potential `-3/6` is -0.5. Division overflow and zero denominators refuse with `numeric_range` and `zero_denominator`, respectively.
- **Why resolved:** New guard `av != 0.0 and value == 0.0` plus nonfinite check occurs after division. No successful fabricated zero was observed for the tested finite nonzero operands.
- **Limitation:** Does not certify relative accuracy of a representable subnormal or recover information already rounded away before the saved float64 operand was formed. That is not the original finding.

### F-02 — RESOLVED — contradictory complete status after re-sealing

- **Corrected source:** [`src/emfeeld/derived_observations.py:226-266`](https://github.com/physicsvigilante/emfeeld/blob/e7c772af39c6271cd7a033ec2a006d617a51b442/src/emfeeld/derived_observations.py#L226-L266), [CLI `269-286`](https://github.com/physicsvigilante/emfeeld/blob/e7c772af39c6271cd7a033ec2a006d617a51b442/src/emfeeld/derived_observations.py#L269-L286).
- **Independent execution on BOTH downloaded Linux/Windows release artifacts:** The genuine `derived-001/G1/result` has `partial` status with `G1-invalid-time = unavailable/different_saved_times`. Copied its saved derived result, changed *only* `result.json.status` to `complete`, and regenerated *only the disposable copy's* unkeyed `integrity.json` with production `_inventory`. Against the untouched `sweep-G1/sweep/baseline`, `inspect(copy,using=native)` now raises **`RevisionError.code == 'derived_integrity'`**. The real CLI returns **exit 2**, diagnostic `derived completion contradicts saved observation outcomes`, and no successful JSON on stdout. Intact G1 inspects as **`partial`** and its CLI returns exit **1** (expected partial outcome), not an integrity error. Both operating-system artifacts independently reproduced this.
- **Why resolved:** Reinspection recomputes all derived item outcomes and aggregate completion, validates source-run/packet linkage, complete sealed source execution, exact result metadata and duplicate source IDs. A self-consistently rehashed but internally contradictory completion is now refused.
- **Limitation:** SHA-256 inventory is **not keyed authentication**. A writer who can rewrite both source evidence and inventory can forge mutually consistent values; this review tests internal semantic consistency, not hostile-writer identity.

### F-03 — RESOLVED — invalid physical magnitudes and vector inconsistency

- **Corrected source:** [`src/emfeeld/derived_observations.py:75-106`](https://github.com/physicsvigilante/emfeeld/blob/e7c772af39c6271cd7a033ec2a006d617a51b442/src/emfeeld/derived_observations.py#L75-L106).
- **Independent direct controls:** Negative `field` and `force` magnitudes, including `-5e-324`, and negative saved `speed` / `kinetic_energy` all become **`unavailable/operand_unavailable`** with `negative_nonnegative_observable` reason. Inconsistent magnitudes (e.g. vector `[3,0,0]` with magnitude `4`), zero-vector/nonzero-magnitude, subnormal-vector/zero-magnitude, malformed vectors and overflowing 3-vector norm also refuse. `[3,4,0]` with magnitude 5 succeeds; an approximately `5e-13` relative deviation is allowed, while `2e-12` is refused, consistent with `rel_tol=1e-12, abs_tol=0`.
- **Real native negative controls, independently repeated for BOTH CI artifacts:** Copied the intact G1 native run, changed `native/result.json` observation `field_0.magnitude` to `-2.5`, and regenerated only that disposable run copy's `model_runs._inventory`. Deriving from the original G1 request then produces `partial`: the affected field ratio is **`unavailable/operand_unavailable`**, valid body distance remains `ok`, and the deliberate mismatched-time item remains `unavailable/different_saved_times`. The genuine native and derived inputs remain hash-unchanged and inspect successfully.
- **Valid controls:** Positive field/force vector norms, native E1/G1/T1 derived results from both OS artifacts, positive saved kinetic energy and signed potential-difference ratios remain accepted. In particular a signed potential difference ratio `-5/2` yields `-2.5`.
- **Limitation:** A physically plausible but fabricated fully re-sealed vector and scalar can still pass; the added check is an invariant, not independent reconstruction of the field law. The altered G1 value is a reviewer-controlled **copy**, not an original solver error.

### F-04 — RESOLVED — malformed saved time and sample identity

- **Corrected source:** [`src/emfeeld/derived_observations.py:25-34,109-118,132-135,164-178`](https://github.com/physicsvigilante/emfeeld/blob/e7c772af39c6271cd7a033ec2a006d617a51b442/src/emfeeld/derived_observations.py#L109-L118).
- **Independent execution:** Both trajectory-ratio and position-separation paths return **`unavailable/invalid_saved_time`**, without traceback, for `time_s=10**500`, `NaN`, `+/-Infinity`, boolean, `None`, strings and **absent `time_s`**. They likewise reject missing sample index and sample index `True`, `False`, negative, float or string. Sample-index mismatch and actual-time mismatch return **`unavailable/different_saved_times`**; identical valid time and nonnegative integer index succeed.
- **Why resolved:** `_valid_saved_sample` invokes `_number`, which traps float-conversion `OverflowError` and rejects nonfinite and nonnumeric saved values. It requires an actual nonnegative Python `int` index rather than accepting `bool`.
- **Limitation:** No claim is made that all numeric input serialization formats preserve arbitrary mathematical precision; the checked contract is finite float64-compatible saved observations and exact saved identity comparisons.

## Tests and independent evidence

### Independently executed in Chat B's separate Linux container

- **Environment:** CPython **3.13.5**, NumPy **2.3.5**, SciPy **1.17.0**, pytest **9.0.2**. No dependencies installed and no fresh native EM integration, Windows execution or PyVista rendering run locally.
- Downloaded the exact corrected-head source snapshot from [source-snapshot CI run 43729059276](https://github.com/physicsvigilante/emfeeld/actions/runs/43729059276), artifact **14167258280**: ZIP SHA256 **`b3bc1aa6f635b84f2ac3a5a7df98f4c89a30157f532d770dd6e448f13f6337ab`**, full ZIP CRC valid; enclosed `tested-source.tar` SHA256 **`17b6f0ee60fd598114c1972c1760279048f56da08e4124043572ed4d4fdaed70`**. Independently matched **all 325 blob SHA1 hashes** against the accompanying Git tree file and recomputed the extracted source's actual Git tree **`ea4efcc21e101be8ceb11cbae5c14924e45d172b`**. GitHub commit metadata separately confirms corrected head `e7c772a...` and CI merge-preview checkout `7474ba9...` have precisely this **same tree**, so the reviewed checkout is not a floating branch. Production module blob SHA1 **`bef80a292f4402a4aed2869fdae0965db1a5ad9b`** matches GitHub's SHA-pinned file.
- **Existing tests rerun independently:** `PYTHONPATH=src python -m pytest -q -W error tests/test_derived_observations.py` → **46 passed**, 7.77 s.
- **Novel/repeated adversarial checks written by this reviewer:** `PYTHONPATH=src python -m pytest -q -W error --tb=short ../test_chat_b_r2.py` → **83 passed**, 7.79 s. Final local harness SHA256 **`f70de43d63a4bd0fcfdfdd6bd87794a7c932ccd7a6ff5ffb7faf22e89cd05d7b`**. Initial 76 cases also passed before adding seven missing-metadata, boundary-tolerance and positive-energy controls. These invoke the **actual extracted production Python functions**, not a reimplementation or Chat A's claimed results.
- **Native saved-output reinspection (no resimulation):** Original E1/G1/T1 results independently re-inspected using real sealed baseline runs from each OS archive. Linux: E1 ratio `1.201106296660619`, G1 field ratio `0.8318483227835429`, G1 separation `2.686918279985713 m`, T1 ratios `11.781609195402293` and `0.36585365853658547`. Windows differs only at last roundoff digits for E1/G1 field ratio; all outcomes and G1 partial status agree. These measurements were **not** rederived from independently run new physical trajectories in this follow-up.
- Both independently downloaded [release CI run 43729059256](https://github.com/physicsvigilante/emfeeld/actions/runs/43729059256) ZIPs have valid CRC for **1,250 entries each**, with checked SHA256:
  - **Linux** job **132857250809**, artifact **14167811270**, ZIP **`b1f32f099f2f5b9494327d7df41cd2fd8014973e0adc4f65c2fffec5a639ed57`**.
  - **Windows** job **132857250864**, artifact **14167972595**, ZIP **`131af51d9599b02a07fa58f122198314cb4fbca74f39b9173062d2f8448285a9`**.
  - Each artifact `head-sha.txt` is `7474ba9b6d0880b6c871987134b82d6b8122b322` (same exact corrected tree). Directly inspected both original G1 partial reports, archived developer challenge copies and native-sealed baselines.

### CI observations (NOT tests independently rerun on those hosted OS runners)

Read the actual Linux and Windows GitHub Actions job logs and artifacts, not only the developer's response. Both job conclusions are **success**. Each records **1,265 headless passed**, **18 historical behavior passed / 1 intentionally deselected obsolete all-file freeze assertion**, **33 real-PyVista passed**, and a **repeat of the same 46 derived-focused tests** (not 46 additional unique test definitions). E1/G1/T1 reference qualification succeeded with G1 correctly partial; archived re-sealed negative controls have the expected refusal statuses. Separate [real-PyVista workflow run 43729059279](https://github.com/physicsvigilante/emfeeld/actions/runs/43729059279) also reports success. These are CI executions, **not** independent reviewer execution on Windows or of the renderer.

## Separate scope judgments

| Dimension | Scoped assessment | Basis |
|---|---|---|
| Source interpretation fidelity | **Not re-assessed** | No new textbook interpretation; follow-up intentionally restricted to F-01–F-04. |
| Physical/numerical correctness | **Pass (four corrected boundaries)** | Independent float64 underflow, signedness, norm, saved-time and legitimate-value checks; no new law evaluated. |
| Native simulation / observable coverage | **Pass for saved derived evidence; broader unknown** | E1/G1/T1 reinspection and disposable G1 re-sealed tests on both OS artifacts, not fresh native integrations. |
| Evidence integrity and provenance | **Pass for bounded deterministic semantics; no authentication claim** | Full exact-tree identity, verified CI archives, complete-source checks, conflicting-status refusal. Inventories remain unkeyed. |
| Teacher-facing usefulness | **Not assessed** | No teacher sessions or interactive viewer test by Chat B. |
| Textbook-answer completeness | **Not assessed** | Outside the narrow follow-up. |

## Remaining limitations and release advice

There is **no demonstrated open correction blocker within these four findings**. Native input trust still relies on externally controlled, unkeyed inventories; numerical subnormal outcomes do not gain a rigorous relative error bound; same-author CI reference checks are not a new independent human physics certification. The corrected source was tested via an identical-tree merge-preview snapshot rather than rerunning the entire native solver independently. None of those boundaries contradicts the scoped contract.

**Recommendation:** mark F-01–F-04 resolved **for commit `e7c772af39c6271cd7a033ec2a006d617a51b442` only**, retain original review-01 unchanged as historical evidence, and allow the owner to perform separate release/merge approval. **Do not merge on this review alone; do not carry this verdict to a newer source commit without new verification.**
