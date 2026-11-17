# conductor_sim PR #72 — Independent targeted R2 re-review #02 (Chat B)

**Outcome: CHANGES-REQUESTED — NEW F-04 SOURCE-PROVENANCE BLOCKER.** The three original issues F-01/F-02/F-03 are independently reproduced as **corrected** on this precise source. However, a new exact-built-in `dataclasses.replace` attack on M31a physical-hypothesis provenance is **accepted by the corrected M31b typed result and its detached JSON export**, while the trusted M24a event-run receipt remains unmodified. Keep production PR #72 **DRAFT, OPEN, UNMERGED**. This is **not** a physics-law or solver defect, and is **not** evidence of malicious end users; it is an actual integrity-contract hole in the authoring/result boundary.

| Item | Exact independent observation |
|---|---|
| Production source | [physicsvigilante/conductor_sim PR #72](https://github.com/physicsvigilante/conductor_sim/pull/72) |
| Live source HEAD, independently checked twice | `72c5f9ffc133da1db79b11c6ba878f95fb8d90c8` |
| Independently checked Git commit tree | `6033283cf38345abd2f2cace5cd7999997509984` (432 entries, no `AGENTS.md`) |
| Source base/main | `ec4f4f10ae6392335c8078cd7ecb0bc575addf04` |
| Two corrective commits | `b9d038251407cf48e86a0be768ae44488dc4cf6e`, `72c5f9ffc133da1db79b11c6ba878f95fb8d90c8` |
| Exact corrective comparison | [Old reviewed head → corrected HEAD](https://github.com/physicsvigilante/conductor_sim/compare/7c177e7da153992d963c966091c76ed12faab5a0...72c5f9ffc133da1db79b11c6ba878f95fb8d90c8) — three files: `src/conductor_sim/coupled_event_family.py`, `tests/test_m31b_coupled_event_family.py`, `docs/m31b.md` |
| Reviewer | Chat B, separate ChatGPT GPT-6 conversation; not human certification or proof of different model weights |
| Date | 2026-11-17 IST |
| Risk and scope | Targeted R2 review of observation issuance, native status/physical-failure boundaries, event provenance, and preserved physics |
| Production code changes by reviewer | **None**; source PR status not changed |
| Independent native execution | **Yes**, first-attempt newly authored Chat B Python 3.12 tests via review_sandbox GitHub Actions |
| Reviewer probe file | [review-02-chat-b-probes.py](../reviews/review-02-chat-b-probes.py), original independent commit `8a04f16fe437b5d2a6337d4faa4ec5c7bf15cf9e` |
| Reviewer native workflow | [Run #44020279830](https://github.com/physicsvigilante/review_sandbox/actions/runs/44020279830), first attempt, exact literal production HEAD/tree both verified, package installed |
| Native evidence | [Artifact #14300088305](https://github.com/physicsvigilante/review_sandbox/actions/runs/44020279830/artifacts/14300088305), containing `review02-results.json`, `review02-native.log` and SHA256 manifest; **GitHub-reported ZIP SHA256** `c47e93e2667b4924534c66b054d1dc0ef55a715757aa78dc02abb405d80fd803`; reviewer inspected GitHub job logs, did not independently download/re-hash artifact ZIP |
| Live outcome | Source PR **open, draft, unmerged**, HEAD matches exact review pin; production CI 18/18 SUCCESS |
| Historical report | [Review #01](review-01-chat-b.md) **CHANGES-REQUESTED** on old SHA remains unmodified |

## Findings

### F-01 — RESOLVED for ordinary typed-root tampering tested

**Source:** [`coupled_event_family.py` lines 113–149, 219–229, 339–341](https://github.com/physicsvigilante/conductor_sim/blob/72c5f9ffc133da1db79b11c6ba878f95fb8d90c8/src/conductor_sim/coupled_event_family.py#L113-L149).

An original real native rod child root was relabeled **+0.030 s**, including both bracket endpoints, retaining the original native position/velocity and all physical fields. Newly authored independent native tests at literal source HEAD observed:

- Direct unsealed `CoupledEventRun(...)`: **REJECTED** with `ValueError: coupled event differs from runner-issued observation receipt`.
- `dataclasses.replace(authentic, children=(tampered_child,))`: **REJECTED**.
- Direct constructor **explicitly retaining original authentic `_observation_digest` and `_issuer`**: **REJECTED**.
- Post-construction `object.__setattr__` replacement followed by `as_dict()`: **REJECTED**, because export revalidates receipt.

The receipt snapshots the original `EventRun.as_dict()` and actual parent/child native payloads (including roots, brackets, saved trajectory samples), statuses and reasons, and revalidates the hash. This closes original F-01 in the declared ordinary same-process dataclass copying scope. The object token and digest are **not cryptographic attestation** against deliberate arbitrary manipulation of module-private internals.

### F-02 — RESOLVED for false parent/child refusals, including authentic refusal retained

**Source:** [`coupled_event_family.py` lines 121–135, 169–218, 308–335](https://github.com/physicsvigilante/conductor_sim/blob/72c5f9ffc133da1db79b11c6ba878f95fb8d90c8/src/conductor_sim/coupled_event_family.py#L121-L135).

Independent native tests relabeled a genuinely successful structural-parent event as `event_run=None,status='rejected-event-study'`; the same attack was made on a genuinely successful child. Both were **REJECTED** using `dataclasses.replace`, and both were **REJECTED** by explicit direct construction with the original issuer and original digest. Authentic numerical parent/child pairing remained `one-resolved-pair`.

A separate independently executed `terminal-refusal` structural source-world case **genuinely refused** M24a parent event qualification (`UnsupportedProblem: initial release departs beyond the stop surface`); the admissible coupled child independently returned `complete` with real `EventRun`. The event shift correctly stayed `unpaired`. No fabricated observation or suppressed successful child occurred. Thus the original F-02 is resolved in this scope.

### F-03 — RESOLVED for injected unsolved M31a child; successful sibling not suppressed

**Source:** [`coupled_event_family.py` lines 201–218 and 327–335](https://github.com/physicsvigilante/conductor_sim/blob/72c5f9ffc133da1db79b11c6ba878f95fb8d90c8/src/conductor_sim/coupled_event_family.py#L201-L218).

Independent deterministic native test created a valid physical two-child family and **test-injected** `scenario!=None,trajectory=None,status='integration-failed'` for the first M31a child, leaving the second child valid. The physical parent/source scenario identity was retained. M31b called `_observe` **exactly twice** (once for the structural parent and once for the *successful sibling*), **never** for the failed child. Exported failed-child physical/event statuses were both `integration-failed`, with `event_run=None`, and `unpaired` event-time comparison. The valid sibling had `complete` native event evidence. Attempting to inject a complete event into the failed child at the typed constructor was **REJECTED**.

This validates the status boundary; it **does not** demonstrate that the RK solver itself actually fails for any production physical problem.

### F-04 — NEW BLOCKER: the receipt does not bind declared M31a physical hypothesis or plan identity to the native observation

**Source and cause:**

- [`coupled_event_family.py` lines 113–138](https://github.com/physicsvigilante/conductor_sim/blob/72c5f9ffc133da1db79b11c6ba878f95fb8d90c8/src/conductor_sim/coupled_event_family.py#L113-L138): receipt snapshots **original event, parent/child native results, status/reason, case_id and revision IDs**, but **not the actual authoring `CoupledPhysicalPlan` or the authored edits**.
- [`coupled_event_family.py` lines 151–159 and 192–225](https://github.com/physicsvigilante/conductor_sim/blob/72c5f9ffc133da1db79b11c6ba878f95fb8d90c8/src/conductor_sim/coupled_event_family.py#L151-L225): result verifies the reattached physical family's plan *by object identity*, then rechecks existing `CoupledPhysicalRun.__post_init__` against that **same substituted** plan.
- [`coupled_physical_family.py` lines 212–269](https://github.com/physicsvigilante/conductor_sim/blob/72c5f9ffc133da1db79b11c6ba878f95fb8d90c8/src/conductor_sim/coupled_physical_family.py#L212-L269): M31a validates child hypothesis identity, scenario lineage, native trajectory/spec binding and exact parent/child sample comparisons **but does not independently prove that the recorded edit values generated the already-returned child scenario**.
- [`coupled_event_family.py` lines 275–295](https://github.com/physicsvigilante/conductor_sim/blob/72c5f9ffc133da1db79b11c6ba878f95fb8d90c8/src/conductor_sim/coupled_event_family.py#L275-L295): `physical_model_family.as_dict()` exports the asserted edits and `plan_id` without binding them into the observation receipt.

**New independently executed exact-built-in repro, result: ACCEPTED by constructor AND detached export, without altering receipt/token or any native event-run object.** Given an authentic `run_coupled_event_family(event_example('added-mass'))` result:

1. Its authentic child is generated by an atomic hypothesis changing **`field:Enew.field_v_m=(150.,0.,0.)` V/m and `test-particle.mass_kg=2e-5` kg**.
2. Using **only `dataclasses.replace` and exact original built-in dataclasses**, create a new hypothesis with `field:Enew.field_v_m=(175.,0.,0.)` V/m and `test-particle.mass_kg=3e-5` kg. Construct a consistent replacement `CoupledPhysicalPlan`, `CoupledPhysicalRun`, `CoupledPhysicalEntry`, `CoupledEventPlan` and `CoupledChildEvent`, reusing all genuine existing source scenarios and numerical trajectories. **Neither `_issuer` nor `_observation_digest` is modified.**
3. `dataclasses.replace(original_CoupledEventRun, plan=...,physical_family=...,children=...)` **SUCCEEDS**. `result.as_dict()` **SUCCEEDS**. The export declares the newly forged `175 V/m` and `3e-5 kg` authored edits, while the **unchanged genuine revised scenario** continues to contain `150 V/m` and `2e-5 kg`. The receipt remains accepted.
4. A separate simpler `dataclasses.replace` with only a new `plan_id='review02:foreign-plan'` similarly **SUCCEEDS**, relabeling top-level exported identity.

**Independently observed workflow lines:** `F04_HYPOTHESIS_PROVENANCE_REBIND ACCEPTED_UNEXPECTEDLY`, `F04_PLAN_ID_REBIND ACCEPTED_UNEXPECTEDLY`. These are ***positive, executed integrity bypasses***, not just predicted code-reading concerns. The first affects the physical meaning of the teacher-authored experiment; the second affects identity/provenance. This is a **major/blocking evidence-fidelity defect** even though native physics and event timestamps remain unmodified.

**Smallest correction:** expand the trusted runner-issued observation snapshot to bind a canonical **complete `CoupledPhysicalPlan`** (including actual atomic `edits`, plan ID, hypotheses and their declared source branch) and verified relationships to the actual child scenarios/physical family; recheck the identical original immutable runner-issued content at typed result construction and export. Alternatively implement another minimal trustworthy identity/provenance binding to the original `CoupledPhysicalRun`/plan that rejects coherent dataclass copy substitutions. Do not simply compute a new digest from a replacement, and do not treat a checksum available to arbitrary module internals as cryptographic. Add a regression reproducing **both** accepted F-04 attacks, at construction and detached export. No numerical solver or physical law needs modification.

## Tests and independent evidence

**Personally authored and executed as Chat B** (review hub workflow, first attempt, source HEAD/tree checked prior to editable installation):

| Probe | First-attempt observed result |
|---|---|
| Genuine native rod parent/child M24a event, complete same-direction unique pairing | PASS |
| Shifted root/bracket: direct constructor, copied seal and explicitly reused old digest/issuer | ALL REJECTED |
| Mutation after construction followed by detached export | REJECTED |
| False parent refusal, false child refusal, plus explicit old-seal constructor attempts | ALL REJECTED |
| Authentic parent event-study refusal while coupled child succeeds | PASS |
| Injected M31a `integration-failed` child, `_observe` call accounting, valid sibling retained, forged child event refused | PASS |
| New native two-property gravity + y-field downward detector against independent uniform-acceleration analytic SI root | PASS |
| F-04 mismatched authored physical edits with original native physics and unchanged receipt | **ACCEPTED — NEW BLOCKER** |
| F-04 plan-ID substitution with original native events and unchanged receipt | **ACCEPTED — provenance gap** |

The first-attempt GitHub Actions job deliberately exited **1** because the script reports both unguarded attacks as failures. It was **not** an install/fixture failure. All intended F-01/F-02/F-03 and analytic-case checks completed before the two F-04 attacks. The first attempt and its evidence are retained unchanged.

**Novel reviewer analytic case:** original Chat B authored two-property gravity + electric field with signed detector y = −0.003 m. Reference `t=sqrt(0.006/|a_y|)`:

- structural parent: `a_y=-1.995 m/s²`, reference **0.05484084971070818 s**, native **0.05484084701538087 s**, error **2.69532731e-9 s**;
- coupled child: `a_y=-3.125 m/s²`, reference **0.04381780460041329 s**, native **0.04381780624389649 s**, error **1.64348320e-9 s**;
- both sign −1, exactly one resolved root each, native `duration`, correct immediate-parent SHA, source-preserving hypothesis and `one-resolved-pair` comparison.

This is a **real independently triggered new native execution** of a reviewer-authored physical scenario; no production field/RK callback is used for the analytic reference. Its absolute errors are within the independently asserted 1e-7 s tolerance.

**Separately inspected developer-generated evidence, NOT personally rerun by this reviewer:**

- All **18/18 live exact-candidate-head workflows** independently fetched from GitHub Actions API, all `completed/success`. The 18 include historical old gates; do not overclaim that each is a new M31b scenario.
- [PR Python run #44017950729](https://github.com/physicsvigilante/conductor_sim/actions/runs/44017950729), 3.10 and 3.12 jobs successful, **1,909 passed + 97 real-FEMM-only skipped + 16 warnings** per interpreter according to supplied/current developer records. PR Python uses synthetic merge checkout, not literal head.
- [Literal direct-source-push Python #44017943727](https://github.com/physicsvigilante/conductor_sim/actions/runs/44017943727), Python 3.10/3.12 success at literal corrected source. The current reviewer separately queried completion status; per-test counts rely on developer reports unless independently retrieved from logs.
- [Real FEMM 5 #44017950852](https://github.com/physicsvigilante/conductor_sim/actions/runs/44017950852), SUCCESS, historical **97 real-FEMM cases** reported by developer. No new M31b-specific FEMM observable inferred.
- [Historical real Chromium #44017950667](https://github.com/physicsvigilante/conductor_sim/actions/runs/44017950667), SUCCESS; not new M31b UI.
- [Native Coulomb/rod+DOP853 #44017950861](https://github.com/physicsvigilante/conductor_sim/actions/runs/44017950861), SUCCESS. Developer's existing native (parent 0.5529332747459412 s, child 0.4985157885551453 s) versus separate implementation DOP853 (parent 0.5529332751693772 s, child 0.4985157889191854 s), as previously reviewed/recorded; reviewer did **not** re-run or redownload its artifacts here.
- Developer's corrected review01 replays [#44017981135](https://github.com/physicsvigilante/review_sandbox/actions/runs/44017981135) are separate developer-controlled evidence; **not** substitute for newly executed reviewer probes above.
- Prior review #01 independent Coulomb analytic+SciPy assessment and original-failure reproduction preserved and not relabeled.

**Review limitation:** No local `conductor_sim` install in this reviewer container because direct GitHub clone failed due to outbound DNS; actual reviewer-authored Python was executed in GitHub Actions on exact source SHA/tree and reported from its logs. The new workflow has a deliberately negative status because F-04 was confirmed. No browser screenshot or FEMM solver was independently run in this context; corrected source does not edit their algorithms.

## Separate scope judgments

| Dimension | Assessment | Basis |
|---|---|---|
| Source interpretation fidelity | **FAIL — report integrity** | F-04 allows authored 150 V/m, 2e-5 kg model to be exported as a different 175 V/m, 3e-5 kg hypothesis |
| Physical / numerical correctness | **PASS in bounded tested native examples** | Corrected code does not change physical equations; reviewer native uniform-acceleration event case agrees to ~1–3 ns, real rod pairing intact |
| Native simulation and observable coverage | **PASS for targeted F-01/F-02/F-03, qualified elsewhere** | Actual newly triggered native tests, genuine parent refusal and valid child, controlled failed physical child with sibling, retained guard/two-root/terminal/unresolved developer tests |
| Evidence integrity and provenance | **FAIL (blocker)** | Native event receipt protects event result, not coherence of claimed M31a plan/hypothesis and true simulated child |
| Teacher-facing usefulness | **Useful bounded engine, release blocked** | Same-source-world event comparison works, but a misdeclared hypothesis can mislead teachers |
| Textbook-answer completeness | **Not applicable** | This feature is an exploratory composed physical/event engine rather than textbook answer solver |

## Release advice

**CHANGES-REQUESTED.** Exact current production HEAD remains draft/unmerged with all 18 developer CI green, but the new **independently demonstrated F-04 provenance bypass** blocks release. Keep PR #72 draft. The implementer should issue the **smallest correction binding physical plan/hypothesis/source identity to the trusted runner-issued receipt**, add the explicit original `dataclasses.replace` attack as a regression, rerun current-source CI and request **targeted re-review #03** at a NEW pinned HEAD/tree. No wholesale Coulomb/rod/ODE/Chromium/FEMM redesign or duplicated physics audit is indicated. Do not merge, approve, mark ready, or edit original negative review #01.

A separate ChatGPT context provides useful adversarial evidence, but is not independent human physics certification or proof of different model weights.
