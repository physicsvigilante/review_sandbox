# SIM_HEAT PR #69 — independent Chat B R2 review-01

**Verdict: CHANGES REQUESTED — new N8 offline source/rational cross-verifier only.** The independent corner/residual/barrier mathematics checks out within its admitted domain, but N8 currently accepts materially inconsistent **untrusted N7 report metadata**. This is an evidence-semantics blocker, not a demonstrated error in the previously scoped-passed N7 mathematical solver, not a native qualification decision, and not permission to merge.

- **Reviewer / date:** Chat B, independent conversation context (GPT-6), 2026-11-19 (Asia/Kolkata). Independent context is not independent human certification.
- **Source PR:** [SIM_HEAT #69](https://github.com/physicsvigilante/sim_heat/pull/69), DRAFT/unmerged; exact head [`cccbc8dca8acc65e17054babbb9e5558063c0d4b`](https://github.com/physicsvigilante/sim_heat/commit/cccbc8dca8acc65e17054babbb9e5558063c0d4b).
- **Base:** already scope-reviewed, still-DRAFT [PR68](https://github.com/physicsvigilante/sim_heat/pull/68) commit `4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128`. Full source tree **`80b8894e100b1ba55b5c90bfe0dd0da96080f13b`**, independently fetched from the Git commit API. Synthetic PR checkout `9a7af14405d455358ede6fab9b7fa132a9b26928` has the same tree, with parents [base, head].
- **Scope checked:** central PR69 REQUEST, reviewer prompt, status, central PROTOCOL / RISK-POLICY / AGENTS; SIM_HEAT AGENTS, H1 contract / offline amendment / C1 freeze, prior independent PR68 review, exact four added N8 files, the unchanged N7 public report contract, relevant N4 admission and T1 facts, plus hosted workflow logs.
- **Diff provenance:** GitHub base-to-head comparison is exactly four **added** paths, no changes to N1–N7, source Modelica, native runner, C1 or frozen references: `qualification/h1_n8/corner_replay.py` (blob `76f4f36ffad2abec345a15bc24740a63a7d31142`); `qualification/h1_n8/README.md` (`07a9bcd29eecc6f566f5b661c2b4f3cabe88e934`); `qualification/h1_n8/tests/test_corner_replay.py` (`9bdd1bacbb28b624fca7819e1a636d3eb6fef488`); `.github/workflows/h1-n8-corner-crosscheck-ci.yml` (`b79d9e3c2dca952b586c6a63525d3fb95c7b8b2b`).
- **Execution provenance:** Personally executed a fresh **separately written** Python Fraction/Machin/Gaussian-elimination calculation (the pinned N8/N7 modules were **not** imported or run locally), plus a 110-digit mpmath check of the independently derived Pi interval. Personally inspected the GitHub API run records and decoded job logs. No OpenModelica install/query/build/launch, no native tests, no source edits or merges, no artifact ZIP download/re-hash.

## Blocking findings

### N8-F01 — HIGH / evidence authority: N8 can PASS a forged N7 certification/native claim

In the pinned [`corner_replay.py` lines 176–204](https://github.com/physicsvigilante/sim_heat/blob/cccbc8dca8acc65e17054babbb9e5558063c0d4b/qualification/h1_n8/corner_replay.py#L176-L204), the initial untrusted-`reported` gate requires `referenceAccuracyCertified`, `nativeQualified`, `nativeExecuted` and `timeTrajectoryComputed` to be false. Other relevant N7 authority fields are **never read as constraints** by the checker. Examples include `independentlyCertifiedReference`, `allGrid77Plus8Plus5Certified`, `referenceBundleWritten`, `ownerApprovedExpectedReferenceManifestVerified`, `sourceInterpretationIndependentlyAuthenticated`, `runtimeReady`, `initialValueProblemSolved` and `proof.proofIsIndependentNativeCertificate`. All are false in genuine [N7 output](https://github.com/physicsvigilante/sim_heat/blob/cccbc8dca8acc65e17054babbb9e5558063c0d4b/qualification/h1_n7/verified_junctions.py#L265-L320).

**Reproducer to add as regression** (source-inspection-predicted bypass, **not** misrepresented as a local execution of the checked-in module):

```python
fake = deepcopy(valid_n7_report)
fake["independentlyCertifiedReference"] = True
fake["allGrid77Plus8Plus5Certified"] = True
fake["proof"]["proofIsIndependentNativeCertificate"] = True
# n8.replay(raw, expected_sha256=pin,
#           body_node_temperatures=temps, reported=fake)
# No predicate examines these mutations: the unchanged mathematical data
# can still yield OFFLINE_..._CROSSCHECK_PASS.
```

This matters because N8 expressly accepts a claimed **untrusted** report and returns a `PASS` status. Its *own* hard-coded false flags prevent N8 from directly becoming a native certificate, but do **not** make a falsely promoted underlying report trustworthy. The developer test `test_native_and_source_trust_forgery_refuses` probes only the subset of three already-gated flags.

**Required correction:** Define and validate the N7 evidence/status semantics appropriate to the cross-check, including all native, independent-certificate, trajectory, owner/source authority and proof-native fields that must remain false; reject missing or promoted critical fields. Add negative mutations for at least one currently unchecked top-level and one nested proof flag. Do not claim actual owner-source authentication on the strength of a caller-provided SHA.

### N8-F02 — HIGH / signed physical evidence: rod orientation and conductance labels are not checked

N8 independently reconstructs source edge orientation and rational conductance intervals, but the report comparison at [lines 279–282](https://github.com/physicsvigilante/sim_heat/blob/cccbc8dca8acc65e17054babbb9e5558063c0d4b/qualification/h1_n8/corner_replay.py#L279-L282) reads **only** `reported["rodHeatFlows"][name]["heatFlowWExactPhysicalEnclosure"]`. It never compares that rod record's `fromNode`, `toNode`, `positiveFromTo`, `orientation`, or `conductanceWPerKExactPhysicalInterval` to independently reconstructed source facts. The set-of-rod-name inventory check at lines 195–197 does not remedy this.

**Reproducer to add as regression** (source-inspection-predicted bypass; not a personally executed N8 call):

```python
fake = deepcopy(valid_n7_report)
rod = fake["rodHeatFlows"]["ArcX_J4"]  # true source direction: X -> J4
rod["fromNode"], rod["toNode"] = "J4", "X"
rod["conductanceWPerKExactPhysicalInterval"] = ["0", "0"]
# Leave rod["heatFlowWExactPhysicalEnclosure"] intact.
# The checked 16 signed q values still fit the untouched numeric interval,
# so current N8 predicates do not reject the false direction or G claim.
```

The resulting record contradicts `q_from_to=G*(T_from-T_to)` and positive `G` even though N8 would report a successful physical flow comparison. This is a **new N8 coverage/evidence-integrity defect**, not proof that the unchanged N7 API itself emits bad labels.

**Required correction:** For each rod name, match the report's endpoints, orientation semantics and exact conductance interval to N8's independent source-derived record, in addition to checking signed heat-flow interval containment. Add regressions mutating direction alone and G label alone. As a secondary hardening step, check the report's assumed-body/fixed-source Kelvin metadata and duplicate row/node enclosure fields for consistency with the same independently reconstructed source; those are currently outside N8's verified field set. Avoid treating an N8 `PASS` as validation of fields it never reads.

## Independently corroborated mathematics (PASS within source-only scope; does not waive blockers)

1. **Exact decimal / Pi:** An independently written 40-term alternating arctan implementation yields rigorous `Pi = 16 atan(1/5) - 4 atan(1/239)` bounds of width approximately **4.77600323798 × 10^-58**. A separate 110-digit mpmath comparison places Pi strictly inside; ordinary binary64 equality is insufficient to check this tiny interval. The source decimal `k=800,d=0.1,L=3` gives `k*d²/(4*L)=2/3` **exactly**, hence `G=2Pi/3`, not a fabricated rounded conductivity.
2. **Four-junction challenge / 16 independent corners:** Independently reconstructed the prior Chat B challenge from original source-style rational conductances: 4 unknowns, 11 edges, 4 circular uncertain edges, parallel H–J1, J1–J2–J3 loop, separate anchored J4 island and isolated body I. Implemented a separate exact rational **Gaussian** linear solver and assembled each of all `2^4=16` independent G endpoint combinations (a conservative superset of physically correlated common Pi). All 16 solved with exact zero linear residual; all satisfy the separately reconstructed midpoint source residual inequality, signed `A(G)v >= r`, and full rational `x0 ± v` containment. Midpoint K approximately J1 **376.640520647068**, J2 **340.757515496605**, J3 **349.205429433345**, J4 **348.958296834357**. Maximum corner-to-centre deviation approximately **3.308 × 10^-57 K**; widest comparison interval approximately **3.359 × 10^-56 K**; minimum signed comparison slack approximately **6.555 × 10^-59 W**.
3. **Negative gradient:** The uncertain J1–J2 circular conductor has `v_J1 - v_J2 < 0`; its J1 row minimum correctly uses **G_hi**, while nonnegative gradients use **G_lo**. Re-derivation included known neighbours with barrier value zero. N8 source [lines 228–244](https://github.com/physicsvigilante/sim_heat/blob/cccbc8dca8acc65e17054babbb9e5558063c0d4b/qualification/h1_n8/corner_replay.py#L228-L244) follows that rule and requires exact independent equality of the residual and signed lower row. Exact midpoint verification [lines 209–226](https://github.com/physicsvigilante/sim_heat/blob/cccbc8dca8acc65e17054babbb9e5558063c0d4b/qualification/h1_n8/corner_replay.py#L209-L226) and whole-envelope containment [lines 245–259](https://github.com/physicsvigilante/sim_heat/blob/cccbc8dca8acc65e17054babbb9e5558063c0d4b/qualification/h1_n8/corner_replay.py#L245-L259) address genuine hazards beyond merely sampling corners.
4. **Original T1-T special case:** Recomputed the original area-only junction matrix from pinned `reference-facts.json`, excluding circular T06 because its endpoints are two **known** body nodes B/P. For assumed R=337, B=303, P=318 K: `J_Lower=8453032705655/25123167961` K; `J_Upper=8454784897015/25123167961` K, each a singleton. T06 has signed negative B→P heat flow and a nonzero Pi-dependent interval of width approximately **1.563 × 10^-58 W**. This source-only result is not a native trajectory.

These are reviewer-executed, **separately implemented** numerical checks, not personally executed `n8.replay` acceptance tests. The static bypass findings above are justified by complete pinned source control-flow inspection; new N8 runtime regressions are still needed.

## Hosted CI and frozen evidence (personally retrieved; hosted, NOT reviewer-local runs)

- [First RED PUSH 44543508873](https://github.com/physicsvigilante/sim_heat/actions/runs/44543508873), SHA `75b5fde01641d8e4d3287e2dc1920ca2d41083d6`: **9 N8 tests, 1 failure**, `AssertionError: CornerRefusal not raised`; previous forged J3 residual was already zero. This is an invalid test mutation, not an observed N7 proof failure. The original failure remains preserved.
- [Corrected exact-HEAD PUSH 44543998302](https://github.com/physicsvigilante/sim_heat/actions/runs/44543998302), `head_sha=cccbc8dc...`, **SUCCESS**; [PR 44544420069](https://github.com/physicsvigilante/sim_heat/actions/runs/44544420069), same PR head and tree-identical synthetic checkout, **SUCCESS**. Personally fetched their job logs: both have **11 N8 + 13 N7 + 13 N6 + 11 N5 + 15 N4 + 12 N3 + 16 N2 + 17 N1 interval + 34 plan + 152 H1 = 294 distinct OFFLINE tests**, all groups OK; documentation HTML/Markdown parity PASS. This is **294 repeated in each run, not 588 independent test cases**.
- The workflow explicitly asserts old source identities and historical **seven physical 100× refusals / eight native blockers**, but this is hosted regression evidence, not personally repeated native physics. GitHub reported push artifact `14540060661` digest `sha256:740cc34afea3655c679f5cc8c00178ab40ecbfcf7a3920de74e36970a7bb7f69` and PR artifact `14539274214` digest `sha256:bf806f6ceec9176631ce0ca6bc074f17d34ba86a18e0a9fd43b5220c8a1ae63b`; ZIP contents/CRC were **not** downloaded and independently rehashed here.

## Separate review dimensions

| Dimension | Verdict |
|---|---|
| Source physical facts and law arithmetic | **PASS within caller-pinned source**; not independent owner/source authority |
| Exact mathematical corner / midpoint / signed universal barrier checks | **PASS on independently reconstructed 16-corner challenge**; no newly observed N7 mathematical defect |
| Untrusted report signed-flow and authority verification | **CHANGES REQUESTED** (N8-F01, N8-F02) |
| Native simulation, real trajectories, all-grid reference accuracy | **NOT EXECUTED / NOT CLAIMED** |
| Evidence integrity | Exact head/tree/diff and hosted CI independently inspected; **artifact bytes not rehashed**, unsafe report metadata acceptance must be fixed |
| Teaching effectiveness / unfamiliar native composition | **NOT TESTED**; source-only graph is not native or held-out transfer proof |

## Required next gate; strict stop

Fix **N8 only** for N8-F01/F02, add adversarial regressions demonstrating the current false acceptance becomes a refusal, publish a **new exact source SHA** and current-head PUSH/PR offline CI, then seek **targeted R2 re-review** of those affected evidence contracts. Preserve this report and the first RED, do not rewrite prior N7 independent review or unfreeze source evidence. Do not promote N8/PR69 merely because its existing 294 offline tests are green.

**Still held:** PRs #59/#60/#62–#69 remain DRAFT/unmerged; original seven 100× physical-reference failures, eight N1 native blockers, and first-author private scorer UNSEALED remain unchanged. No OpenModelica version query/install/build/launch, external source/owner seal, reference promotion, time-grid certificate, historical C1 rewriting, source merge or deployment.

**Signed:** Chat B — independent R2 report pinned to `cccbc8dca8acc65e17054babbb9e5558063c0d4b`; central review-file publication only.
