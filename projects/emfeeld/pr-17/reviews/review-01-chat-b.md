# R2 independent-context review — EM Fields Atomic Scenario Revision V1 (PR #17)

**Reviewer:** Chat B, separate-context GPT-6 ChatGPT conversation; not a separate human physicist or proof of different model weights  
**Date:** 2026-11-16 (Asia/Kolkata)  
**Project/source:** physicsvigilante/emfeeld, [source PR #17](https://github.com/physicsvigilante/emfeeld/pull/17), draft/unmerged  
**Risk/scope:** R2, bounded proposal-version-3 atomic scenario revisions, source/particle identity, construction/physical constraints, retained provenance/dependency receipts, local publish/failure boundaries, saved native evidence, E1/G1/T1 physics  
**Base SHA:** 8fe6331aefa252585b3b90f54b8ee7cbbac5e605  
**Exactly reviewed head SHA:** **62121252c6526c53c29440dcd8f41b6109f70e04**  
**Canonical reviewed source tree:** **339224f69e5c671dea83678cdb00845887ce27b4**  
**Diff:** [pinned base-to-head](https://github.com/physicsvigilante/emfeeld/compare/8fe6331aefa252585b3b90f54b8ee7cbbac5e605...62121252c6526c53c29440dcd8f41b6109f70e04)  
**CI merge-preview SHA:** 6d1c219e67cf300df7044f24690edf779270ac8f; verified source tree identical to canonical reviewed tree  
**Source files modified or source PR merged by Chat B:** **No**. Tests, injected failures and copies ran only under isolated reviewer-local temporary directories.

## Outcome: **pass** (scoped R2 implementation review; NOT merge authorization)

**No demonstrated implementation defect** was found for the frozen V3 contract in the pinned tree. A verified source snapshot, inspection of changed code and inherited guards, **199 independently rerun relevant existing tests**, **14 new reviewer-authored adversarial case groups** (including eight actual two-process contention trials), **three fresh reviewer-invoked E1/G1/T1 qualifications**, and independently written ideal-field/potential and RK4 calculations against Linux **and Windows saved traces** support this narrow conclusion.

This does **not** establish crash-safe or distributed ACID behavior, authenticated external provenance, arbitrary-model numerical certification, native Windows mouse interaction, or real teacher/classroom acceptance. Construction admission and successful native simulation remain separate. The parent/source PR must stay subject to a **distinct owner merge approval**.

## Reviewed implementation and transaction invariants

- [atomic_revisions.py lines 133–261](https://github.com/physicsvigilante/emfeeld/blob/62121252c6526c53c29440dcd8f41b6109f70e04/src/emfeeld/atomic_revisions.py#L133-L261): exact V3 envelope and member grammar, 2–4 distinct target IDs, single pinned parent, literal provenance, private final candidate, no accepted intermediate state, receipt survival/invalidation, final scene validation, locked publish.
- [model_revisions.py lines 303–328 and 389–422](https://github.com/physicsvigilante/emfeeld/blob/62121252c6526c53c29440dcd8f41b6109f70e04/src/emfeeld/model_revisions.py#L303-L328): reference/content hashes, exclusive revision directory and last-written marker; [dispatch and retained proposal decision](https://github.com/physicsvigilante/emfeeld/blob/62121252c6526c53c29440dcd8f41b6109f70e04/src/emfeeld/model_revisions.py#L389-L422).
- [structural_revisions.py lines 17–70](https://github.com/physicsvigilante/emfeeld/blob/62121252c6526c53c29440dcd8f41b6109f70e04/src/emfeeld/structural_revisions.py#L17-L70): existing *local* exclusive-writer guard; complete accepted-history scan, connected ancestry, identity reuse refusal and incomplete-history failure closure.
- [model_runs.py lines 52–119](https://github.com/physicsvigilante/emfeeld/blob/62121252c6526c53c29440dcd8f41b6109f70e04/src/emfeeld/model_runs.py#L52-L119): named source/particle lowering, old presentation refusal and stale-computed-input analysis admission; [lines 127–223](https://github.com/physicsvigilante/emfeeld/blob/62121252c6526c53c29440dcd8f41b6109f70e04/src/emfeeld/model_runs.py#L127-L223): fresh run, sealed inputs, exact mapping and read-only inspection.

The new files and narrow dispatch do not add physical laws, integrator changes, implicit source retargeting, presentation interpolation, conductor polarization or particle backreaction. All V3 expected values are checked against the same original parent, not against a sequence of unpublished intermediate states.

## Findings and explicit limitations

**F-01 — Informational/minor, interrupted publish and crash recovery.** In an *independent executed fault injection*, a reference-marker write was made to raise OSError after a revision-body file had been created. The attempt remained pending (no accepted decision/reference), its reserved directory had revision.json without reference.json, and a later atomic proposal was rejected as incomplete_history. Original accepted revision bytes were unchanged; the structural lock was released by the controlled exception. This matches [frozen contract §4(8)](https://github.com/physicsvigilante/emfeeld/blob/62121252c6526c53c29440dcd8f41b6109f70e04/docs/ATOMIC_SCENARIO_REVISIONS_V1.md#L183-L195), not a defect. **Operational requirement:** inspect/reconcile crashed or manually tampered local stores; do not silently retry/erase reserved IDs. A hard process kill, uncooperative filesystem, external adversarial writer or distributed lock race was **not executed**.

**F-02 — Informational, evidence/provenance interpretation.** Linux and Windows checkout source-byte digests in the saved run manifests differ despite identical Git tree. I initially saw Windows SHA mismatches against the Linux-extracted source. All **27** recorded Python module SHA256 values in each Windows run matched the same canonical source after LF-to-CRLF checkout-line-ending conversion; all Linux module hashes matched the extracted source directly. This is *not* evidence of divergent Python logic. Preserve both raw runtime hashes and Git blob/tree identity; never silently call them identical bytes.

**F-03 — Minor, evidence scope, no production defect.** CI's E1/G1/T1 checks are same-author, preselected fixtures. Reviewer-local independent calculations substantiate **these fixtures**, not arbitrary near-singular integrations or source interpretation truth. No native Windows desktop event manipulation or classroom trial was performed. Physics bounds and source-given-versus-illustrative provenance remain declared assumptions. A report or ZIP hash is integrity evidence, not a signature/authenticity proof.

**F-04 — Informational, original failures preserved.** Initial author CI [release run #43750725799](https://github.com/physicsvigilante/emfeeld/actions/runs/43750725799) failed on Ubuntu and Windows and [viewer run #43750725784](https://github.com/physicsvigilante/emfeeld/actions/runs/43750725784) failed during the cumulative suite: test_invalid_requests_are_rejected_without_partial_descendant expected rejected but saw no_op for a composite containing an unchanged member (1 failed, 1,336 passed in the Ubuntu failed attempt). In the **pinned later source**, V3 now raises no_op_member and records rejected, while the legacy V1 whole-proposal no_op path is unchanged. I independently tested this V3 behavior. Original logs are not reclassified as passes.

**No blocker/major findings.** Future scope expansions (distributed writers, general branch merging, symbolic or computed-origin transaction inputs, shell/plane motion, native Windows UI) would require their own authorization and review, not silent reinterpretation of this verdict.

## Reviewer-executed tests (separate from Chat A CI)

**Environment:** isolated Debian/Linux execution, CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, pytest 9.0.2; PyVista not installed locally. GitHub cannot be cloned directly here. Instead I downloaded and verified the exact-head GitHub Actions source snapshot [run #43751887494](https://github.com/physicsvigilante/emfeeld/actions/runs/43751887494), artifact **14176358700**, ZIP SHA256 **a849a7b6157048ba7e125c7ea0603991887e9b46d817fae84c4d68ed78fabe87**, inner tar SHA256 **6daacfac2f8f808fe58d1b92aec0f918c87da1fb93046102ae7b9c1b1c5fa4a1**. The snapshot declares preview HEAD 6d1c219e… and tree **339224f6…**. **All 336 file bytes** recomputed to their listed Git blob SHA-1s, with zero missing/extra/mismatched entries. The exact head commit's tree was separately checked using GitHub Git data.

Fresh execution ledger:

| Check | Independently executed outcome |
|---|---|
| 34 V3 tests, tests/test_atomic_revisions.py | **34 passed** (these definitions are also included in the 199 below; not additional distinct tests) |
| tests/test_model_revisions.py + test_structural_revisions.py + test_particle_revisions.py + test_atomic_revisions.py | **199 passed** in 13.56 s, warnings as errors |
| Reviewer-written adversarial script on actual imported ModelStore, not an implementation re-creation | **14/14 case groups passed**, including eight two-process races |
| Reviewer-invoked tools/qualify_atomic_revisions.py (without --render) | **3 accepted revisions; 6 baseline/final native runs complete; one E1 old-presentation refusal** |
| Reviewer-rerun verification/check_atomic_revision_runs.py on fresh runs | **36 field/potential checks; 7 trajectories** (same-author reference *code* invoked independently, counted separately from the reviewer-authored physics below) |
| Whole tests/ headless suite | **Incomplete:** reviewer-local attempt reached ~32% then exceeded the execution limit; **no independent full-suite pass is claimed** |
| Local PyVista and local native Windows event tests | **Not run** |

Reviewer-written adversarial cases (all actually executed on the source, under new temporary stores): (1) four mixed remove/add members including removal of both parent sources with one valid final replacement; (2) malformed fourth member preserving an unchanged accepted lineage and permitting a later distinct valid proposal; (3) canonical whole-object removal mismatch; (4) cross-role and within-proposal ID collision; (5) reuse of removed historical ID from sibling/descendant; (6) two-level computed receipt staleness and direct-literal-overwrite chain break; (7) dependent_source refusal versus overwrite of the only surviving direct receipt; (8) no-op-plus-real-change refusal; (9) negative gravitational mass and zero source radius; (10) injected failure before commit marker plus subsequent incomplete_history refusal; (11) tampered exact parent SHA; (12) fresh rejected stale-input trajectory alongside a permitted static probe; (13) fresh sealed-run native-result tamper refusal without changing the original; (14) **eight** separate simultaneous two-process competing writers, each admitting exactly one and rejecting one (store_busy or identity_conflict), with only one descendant and no residual lock.

Reviewer-authored scripts were outside the source repo and did not modify PR #17. Script identities: adversarial SHA256 **4da1a8bad6adf5b3a1fe7451173984cc1ed4c617a1bf81f3580f3033ee5d7beb**, separate-physics SHA256 **1f591c6716e273dc2822fd24f53409ce0150bf64857c9ffc032cfaf55ef34f24**. They are available as downloadable outputs in the separate Chat B conversation, not falsely described as CI artifacts.

**Reproduce core repo-owned checks** from the pinned source tree, with new empty output directories and a working scientific Python environment:

    PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -W error -p no:cacheprovider tests/test_model_revisions.py tests/test_structural_revisions.py tests/test_particle_revisions.py tests/test_atomic_revisions.py
    PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 python tools/qualify_atomic_revisions.py --output /tmp/chatb-native
    PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 python verification/check_atomic_revision_runs.py /tmp/chatb-native --report /tmp/chatb-atomic-check.json

For the key new crash case, import a two-source model using ModelStore.import_legacy; propose V3 add_source plus add_particle; wrap model_revisions.put to throw OSError **only** when writing the revision folder's reference.json; submit once; check the reserved folder has revision.json but no reference.json, proposal pending exists without decision, no accepted child reference exists, and a fresh proposal rejects with incomplete_history. For dependency chains, import a computed a.velocity_m_s receipt depending on p.charge_C and a computed a.position_m receipt depending on a.velocity_m_s. Editing p.charge_C makes *both* stale; replacing a.velocity_m_s with a literal removes that receipt but keeps dependent a.position_m stale. These are actual independently executed cases, not speculative defect claims.

## Saved evidence audited and independent numerical references

- [Exact-head hosted release run #43751887519](https://github.com/physicsvigilante/emfeeld/actions/runs/43751887519), **author CI**, Ubuntu 24.04 and Windows 2022, 1,342 headless + 18 behavioral + 33 real-PyVista distinct suite definitions per OS; 34 extra focused atomic executions duplicate definitions already in headless. [Viewer run #43751887558](https://github.com/physicsvigilante/emfeeld/actions/runs/43751887558) separately green but is **not** an independent reviewer.
- **Linux ZIP artifact 14176882398:** SHA256 **932b1689c0d34bb121a1ccaa0539ea1c9db0988ef1ebb60ce88ff5cd11865880**. **Windows ZIP artifact 14177380152:** SHA256 **e93c60adb6ec39c7f7dd95bb0bcab57edcf65bee2181e616c8aaf2714a6d6ea6**. Both downloaded in Chat B, ZIP CRC checks passed for **1,629 entries each**, and six baseline/final run-level recorded SHA256 inventories plus original input hashes per OS were recomputed and matched. Each archive contains exactly three accepted physical descendants, six complete runs and one deliberately rejected E1 old-presentation run; original revisions, preserved runs, named maps and saved source data were inspected.
- Same-author archived checker was **rerun locally** on **both** downloaded archives: 36 static and seven trajectory reference checks per OS, no failures. This is a replay of author-authored reference code, **not** independent reference authorship.
- Additionally I implemented ideal-source formulas and explicit fixed-step RK4 **afresh without importing emfeeld or the author reference module**, and checked archived Linux and Windows probe values, saved states, kinetic/potential energy arrays, identity maps and source/revision bindings. Each OS: **36 static observations + seven trajectories**. Maximum static absolute error across the two archives: **4.45e-16** in native units; maximum six-component saved-state versus independent RK4 absolute difference: **7.38e-14** (metres or metres/second by component). Fixed-step refinement independently agreed. These are numerical comparisons, not rigorous global truncation-error bounds.
- **E1:** line potential/field uses the explicitly chosen 1 m logarithmic reference radius, plus E_z=+0.15 N/C. Verified exact axial expression z(t)=0.1t+0.075t², giving z(4 s)=**1.6 m**, and the original test body's baseline-to-final terminal position displacement **3.70263609 m**. Named particle is retained and its initial properties are unchanged; its trajectory is **not** assumed unchanged.
- **G1:** used independent interior/exterior uniform-sphere acceleration/potential and the second prescribed point mass, including changed 2.0e9→2.5e9 kg source mass. Terminal position differences for retained body_1/body_2 were **0.08178450 m / 0.15513824 m** after the 5 s horizon; body_3 is separately integrated. New gravity body's omitted charge is explicitly sourced as the zero-charge parser convention, not coupled electromagnetism.
- **T1:** separately applied thin-shell constant interior potential/zero interior E and central point-source terms, including source charge edits 2e-9→3e-9 C and -5e-10→-8e-10 C. First interior probe final field **[-6.036658827, -9.054988241, -4.527494120] N/C**, potential **4.275422968 V**; no trajectories or shell motion were claimed.
- Linux/Windows observable values agreed to at worst **4.45e-16 absolute**; provenance byte hashes across their checkout-normalized .py sources were separately reconciled (F-02).

**Preserved reviewer-side audit mistakes:** My first Windows archive inventory script accidentally excluded *every* basename integrity.json, including the nested native/integrity.json required by the top-level seal; this caused a reviewer assertion failure, not a production failure. The corrected audit excludes **only** the top-level run/integrity.json, passed on all Windows runs, and is the result reported above. A first direct Linux-source-vs-Windows-run module-hash comparison also failed until normal Git checkout CRLF conversion was accounted for (F-02). Neither failed attempt was erased/relabelled. The long full-suite attempt is recorded as incomplete rather than passed.

## Separate scope judgments

| Dimension | Judgment | Basis |
|---|---|---|
| Source interpretation fidelity | **Unknown for unseen teaching sources; pass for explicitly recorded fixture-to-native mapping** | All checked named properties, source facts, declared hypotheses and preserved imported bytes map into saved requests; no new unseen textbook interpretation task |
| Physical/numerical correctness | **Pass, bounded E1/G1/T1 and tested constructed cases** | Independent analytic SI expressions, independent RK4 trajectories, energy components, fresh and archived native checks; no close-singularity general certification |
| Native simulation and observable coverage | **Pass, bounded** | Three independently invoked scenario qualifications; six complete native runs, 36 static and seven trajectory checks; old presentation explicitly refused |
| Evidence integrity and provenance | **Pass for byte and local lineage integrity; external authenticity unproven** | Exact tree/336 Git blobs, ZIP digests/CRCs, SHA256 run inventories, named mappings, source checkout EOL reconciliation, retained proposal outcomes |
| Teacher-facing usefulness | **Unknown** | No independent lesson, manual desktop interaction or classroom judgment |
| Textbook-answer completeness | **Not applicable** | Fictional illustrative/hypothetical transfer settings; no independently graded textbook-answer task |

## Release advice

**PASS only for PR #17's pinned V3 atomic-construction contract.** No requested source correction or new source commit follows from this review. Preserve the documented local-only lock, incomplete-crash forensics, singular numerical failure separation and stale receipt refusal. The smallest post-review release gate is owner review of this report and **separate explicit merge authorization**, then new main-branch CI; if the source head changes, pin the new tree and perform a proportionate re-review. Classroom use, true Windows pointer interaction, arbitrary unfamiliar physics and more ambitious transaction guarantees remain separate future qualifications.

This separate-chat LLM review provides independent **context and independently executed tests/calculations**; it is not independent human certification, and it cannot authorize production merge.
