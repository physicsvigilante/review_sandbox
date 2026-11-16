# Independent R2 follow-up review 02 — conductor_sim M31a PR #71 (F-01 only)

**Verdict: CHANGES-REQUESTED (one residual, narrowly scoped comparison-evidence validation blocker).**

- **Reviewer:** Chat B, separate ChatGPT conversation, GPT-6. Independent context, not independent human physics certification or proof of different model weights.
- **Review date:** 2026-11-16/17 IST.
- **Source repository / PR:** https://github.com/physicsvigilante/conductor_sim/pull/71 — DRAFT, OPEN, UNMERGED at review close.
- **Base/main:** 293d4b22a6eeb4bc56a5598d8b6935ef91f19826.
- **Exactly reviewed NEW source HEAD:** c190e0929e727d35db2337efc366cf9676fc36f3.
- **Verified actual Git tree (Git commit API):** df48e1eb10536285818abfafd3f0628436247882.
- **Previously independently reviewed source HEAD:** e8970e26b91f6f8dfe3bd8bffcaf8f181449870b, tree 15e658dfae00289e27a577f5f1df1c340e8e1c72.
- **Original separate report, immutable:** [review-01-chat-b.md](review-01-chat-b.md), CHANGES-REQUESTED for F-01.
- **Handoff / charter:** [REVIEWER-PROMPT-02](../REVIEWER-PROMPT-02.md), [REQUEST](../REQUEST.md), [central PROTOCOL](../../../../PROTOCOL.md), [frozen M31a charter](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/docs/m31a_charter.md).

This report assesses **only the correction to F-01**, without relitigating the original physical-law review and without rewriting review-01. No edits, tests, approvals, or merges were made to the production source repository.

## Source identity and correction scope

Queried the live PR and independently obtained its Git commit object; both match the new exact source SHA above. Git's actual commit tree matches df48e1eb... . The prior independently reviewed HEAD is the **immediate parent** of this one new commit. The explicit GitHub compare reports **exactly three paths**, all additive in this correction:

1. [src/conductor_sim/coupled_physical_family.py](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/src/conductor_sim/coupled_physical_family.py) — 21 inserted lines.
2. [tests/test_m31a_coupled_physical_family.py](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/tests/test_m31a_coupled_physical_family.py) — 93 inserted lines, five new tests.
3. [docs/m31a.md](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/docs/m31a.md) — 11 inserted lines clarifying evidence scope.

No source field, force, RK integrator, physical qualifier, source-reassembly, numerical controller or existing M20b/M22a/M28a/M29a implementation changed between the two review pins. A root AGENTS.md lookup at the pinned source ref returned 404; the frozen charter and source/domain contracts were used.

## F-01 correction: effective portions

**1. Non-native impostor trajectory — FIXED for declared type boundary.** The public CoupledPhysicalRun now requires the exact built-in PrescribedScenario and TestChargeMotionResult types ([source L214-L230](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/src/conductor_sim/coupled_physical_family.py#L214-L230)). The runner also requires native result type and exact candidate-spec identity ([L317-L328](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/src/conductor_sim/coupled_physical_family.py#L317-L328)). An arbitrary object with fake spec, termination and as_dict attributes can no longer be accepted. This is *typed evidence authentication*, not cryptographic attestation against deliberately modified internals of a real TestChargeMotionResult.

**2. Unknown termination — FIXED.** Both runner and typed result admit only duration and source-guard. The former maps to complete, the latter maps to censored; other codes fail rather than silently relabeling numerical uncertainty as physical censorship. The unchanged native prescribed-motion solver maps existing surface-/charge-guard events to source-guard ([prescribed_motion.py L349-L357](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/src/conductor_sim/prescribed_motion.py#L349-L357)).

**3. Native parent binding and ordinary comparison tampering — SUBSTANTIALLY FIXED.** For an accepted coupled child, CoupledPhysicalRun now checks the exact immediate-parent native TestChargeMotionResult type, exact expected-parent spec identity and recognized parent termination ([L231-L236](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/src/conductor_sim/coupled_physical_family.py#L231-L236)). It recomputes the comparison row tuple from unchanged M28a _shared_rows(actual immediate parent, child) and rejects ordinary invented, omitted, reordered or modified rows ([L237-L238](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/src/conductor_sim/coupled_physical_family.py#L237-L238); [M28a L158-L173](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/src/conductor_sim/trajectory_sweep.py#L158-L173)). Pre-export __post_init__ repeats this check ([L240-L243](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/src/conductor_sim/coupled_physical_family.py#L240-L243)).

**4. Genuine native controls — PASS by observed exact-source CI.** The five new focused tests include the original three F-01 counterexamples, mutation after construction, actual source-guard censoring and jointly valid +z source/probe translation ([tests L349-L430](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/tests/test_m31a_coupled_physical_family.py#L349-L430)). The test file shows 15 passing test dots in exact-head CI; valid guard termination and jointly translated complete model are retained. This is evidence **from CI execution**, not a fresh reviewer-run native integration.

## Remaining new finding F-01-R — BLOCKER: Python equality is not exact typed comparison evidence

**Location:** [CoupledPhysicalRun.__post_init__, source L191-L194 and L237-L243](https://github.com/physicsvigilante/conductor_sim/blob/c190e0929e727d35db2337efc366cf9676fc36f3/src/conductor_sim/coupled_physical_family.py#L191-L243). It requires a built-in tuple for comparisons but does not validate the concrete type or serializable value of each comparison row. It then uses ordinary Python tuple/dict equality for “exact” rows. CoupledPhysicalEntry.as_dict serializes the user-provided comparison rows, and CoupledPhysicalRun.as_dict passes them through JSON.

**Adversarial variation independent of the developer's five tests:** A valid native run has a parent/child comparison at exact time 0.0. Replace **only** the first stored time_s value with built-in Python False. Python considers False == 0.0, so two otherwise identical ordinary dicts and tuples compare equal. The new validation accepts the altered row **even though detached JSON exports a Boolean false rather than the literal numeric saved SI timestamp 0.0**. Pre-export revalidation repeats the same equality and therefore also misses it. This changes the type and evidence representation without touching any native TestChargeMotionResult or solving any new model.

Suggested full-source regression (not claimed as run against installed conductor_sim in this reviewer environment):

~~~python
from dataclasses import replace
run = _actual_complete_coupled_family()  # fixture in the M31a tests
good = run.entries[0]
assert good.comparisons[0]["time_s"] == 0.0
bad_first = dict(good.comparisons[0])
bad_first["time_s"] = False
bad = replace(good, comparisons=(bad_first, *good.comparisons[1:]))
forged = CoupledPhysicalRun(run.plan, run.structural_run, (bad,))
assert forged.as_dict()["entries"][0]["exact_time_comparisons"][0]["time_s"] is False
# Desired after correction: CoupledPhysicalRun must reject this instead.
~~~

**Independently EXECUTED micro-reproduction:** In the reviewer Python runtime, tested equivalent plain tuples of dicts, confirmed that the Boolean-falsified row compares equal to the genuine numeric row, and confirmed Python's JSON encoder emits false in place of 0.0. This execution tests the exact equality/serialization semantics used by the pinned source. It is **not** an installation/execution of the entire source package, so the full-source regression above remains a code-path-predicted outcome.

A second independently executed semantic probe used a float subclass overriding equality, allowing an actual stored time of 9999.0 to compare equal to 0.0 and serialize as 9999.0. That requires deliberately adversarial custom Python and is not needed to establish the blocker: the built-in Boolean case alone demonstrates that the “exact typed saved SI timestamp” claim is false. The latter illustrates why simply rejecting Boolean scalars is not the entire answer if arbitrary comparison-row objects remain accepted.

**Required bounded correction:** Enforce type-faithful, canonical comparison rows, not ordinary cross-type Python equality of user-supplied objects. A defensible small fix is to compare the **fully JSON-normalized** stored rows (strictly finite, built-in JSON primitives) to the JSON-normalized recomputed native _shared_rows, and/or enforce exact row dictionaries with exact numeric/tuple value types before equality. If comparisons are export-only, deriving exported comparison rows directly from the native parent and child instead of trusting mutable stored row objects is another suitable design, provided constructor mutations are still refused as required by the typed-result contract. Preserve the exact existing time-matching algorithm and no-interpolation semantics.

Add a targeted regression for Boolean 0.0 substitution both at result construction and by post-construction mutation before as_dict; a custom equality numeric/dict subclass is a useful second case. Do **not** change actual physical laws, native integration, source qualification, parent lineage or frozen historical evidence. Rerun exact new-head CI and request another narrowly scoped independent check.

**Severity/rationale:** This is **not** a physical-law defect or evidence of forged results from the genuine native runner. It is a residual **public typed result / detached-evidence validation bypass** of the original F-01 class, using only a built-in Python bool (not cryptographic attack, OS tampering or malicious mutation of an internal native solver object). The source charter explicitly excludes Boolean physical authoring values and calls for authentic typed result evidence; the new contract claims literal numeric saved SI timestamps. Accordingly F-01 is not fully closed.

## Verified CI and provenance limits

Queried the **live GitHub Actions runs API filtered by exact new HEAD**: **16 of 16** runs report completed/success, all with head_sha c190e0929e727d35db2337efc366cf9676fc36f3. Inspected the actual job steps and log outputs:

- [Python PR workflow #43927024438](https://github.com/physicsvigilante/conductor_sim/actions/runs/43927024438), Python **3.10 and 3.12**: each **1,891 passed, 97 skipped, 16 warnings**. Full M31a test-file progress is 15 dots. The **97 skips** are real-FEMM-only in the standard Python matrix, not silent claims of real solver coverage.
- [Python push workflow #43927011449](https://github.com/physicsvigilante/conductor_sim/actions/runs/43927011449) also succeeded at this exact source head. Its Python 3.10 log independently repeats **1,891 passed, 97 skipped, 16 warnings**.
- [Real FEMM 5 workflow #43927024562](https://github.com/physicsvigilante/conductor_sim/actions/runs/43927024562): real-FEMM job log states **97 passed** and historical FEMM integration, not a novel FEMM-specific M31a trace.
- [Visualization workflow #43927024565](https://github.com/physicsvigilante/conductor_sim/actions/runs/43927024565): historical real-Chromium and source checks succeeded; its Python non-FEMM test job states **1,891 passed, 97 deselected, 16 warnings**. No M31a-specific HTML is claimed.

**Important checkout distinction:** The PR-triggered Python, FEMM and Chromium log checkout lines identify GitHub's synthetic PR merge commit **e74787830ccb53c2283bc5ea0567f35dde7ec5ba** (merge of c190e092... into unchanged base 293d4b22...), while the additional successful **push-triggered** Python job ran at the direct new source ref. GitHub run metadata reports the same PR head SHA for the PR jobs. Do not misdescribe a PR merge-checkout artifact as a literal source-HEAD commit artifact.

The prior independent review-01's standalone physics recalculation against **404 retained genuine native states** (finite tilted rod, signed points, gravity, reassembled new point and coupled revisions; separate closed-form field and SciPy DOP853) remains **historical evidence tied to the original source head**. This re-review did not redo those calculations or execute native conductor_sim on the new head; the new commit changed comparison validation/tests/docs only and the new-head CI tested retained genuine guard and translation controls. No proof of exact ODE error bounds, full adversarial Python-object immunity, or new renderer is inferred.

## Required next action and release gate

**CHANGES-REQUESTED: F-01-R only.** Close the residual type/serialization fidelity gap in exact comparison rows with one bounded fix and additional negative tests. Keep the historical review-01 verdict unchanged, and do not claim this review as PASS or merge authority. PR #71 must remain **DRAFT / UNMERGED** until a new independent targeted PASS on the corrected new SHA/tree and still-green exact-head CI; the owner/implementer then manages the separate expected-head release gate and postmerge verification. No GitHub source PR approval, ready-state transition or merge was performed by this reviewer.
