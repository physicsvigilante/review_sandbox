# SIM_HEAT PR #68 — independent Chat B R2 review-01

**Verdict: SCOPED PASS — N7 offline rational interval junction method ONLY.** No demonstrated blocking defect in the new exact-rational residual / positive Dirichlet-M-matrix enclosure argument. This verdict is **not** an approval of time integration, native OpenModelica execution, source authenticity, 77+8+5 accuracy, reference promotion, any stacked PR merge, or teaching effectiveness.

- **Reviewer:** Chat B, independent separate conversation, GPT-6; 2026-11-19 (Asia/Kolkata).
- **Source:** [physicsvigilante/sim_heat PR #68](https://github.com/physicsvigilante/sim_heat/pull/68), still DRAFT / unmerged at review; **exact head** [4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128](https://github.com/physicsvigilante/sim_heat/commit/4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128).
- **Base:** reviewed-in-scope, still-draft PR67 commit `4517bf8e14f659e79255bc1d20f7fcb7b72ce695`.
- **Full source tree:** `5cf0e68e87a81ba641b4d6ef5f9f215120670dc5`, independently checked via GitHub Git commit endpoint. [Base-to-head compare](https://github.com/physicsvigilante/sim_heat/compare/4517bf8e14f659e79255bc1d20f7fcb7b72ce695...4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128) reports precisely four additions: N7 Python implementation, N7 README, N7 tests, and its checking-only workflow. Source implementation blob `78c3ff00eb627479f1e6d144d5770bf23aef1b0c` matches the packet.
- **Scope/risk:** R2 — new exact numerical proof, source graph interpretation and refusal/evidence semantics. Read central REQUEST / REVIEWER-PROMPT-01, PROTOCOL, REVIEW-RISK-POLICY, both AGENTS, H1 contract/amendment, pinned N4/N5/N6 sources, complete N7 implementation, its 13 tests, README, workflow and original source facts.
- **Writes and execution:** **no source-repository modification; no OpenModelica query, installation, build, launch, simulation or PR merge.** Independently executed an offline *separately authored Python Fraction reference calculation* in a local container. Did **not** execute/import the checked-in N7 module locally. GitHub-hosted source tests are distinctly identified below.

## Findings

### F-01 — Mathematical proof is valid under the admitted graph premises (PASS, critical proof examination)

Relevant source: [N7 lines 74–184](https://github.com/physicsvigilante/sim_heat/blob/4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128/qualification/h1_n7/verified_junctions.py#L74-L184), [N6 lines 61–96](https://github.com/physicsvigilante/sim_heat/blob/4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128/qualification/h1_n6/exact_junctions.py#L61-L96), [N4 lines 84–202](https://github.com/physicsvigilante/sim_heat/blob/4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128/qualification/h1_n4/static_physical.py#L84-L202).

For the unknown-only Dirichlet system A(g)x(g)=b(g), the midpoint centre x0 is verified *exactly* to satisfy A(gmid)x0=b(gmid) (N7 109–114). Each source edge contributes (gmid−g)(x0_j−T0_other) to the corresponding residual; therefore its magnitude is bounded by (hi−lo)/2 times the **absolute nominal edge gradient**, independent of rod orientation. Summing incident bounds gives a valid r_j (117–125), including parallel rods, multiple known anchors and common-Pi correlations (treating correlated g as independent only enlarges the uncertainty set).

For nonnegative v, known-node barrier values are zero. The lower bound for every A(g)v row is the *sum of separate minima of g_e(v_j−v_other)*. N7 137–149 correctly picks **lo for a nonnegative gradient and hi for a negative gradient**. Thus the checked bound A(g)v >= r applies to every independent conductance selection and, a fortiori, the physically correlated common-Pi selection. N4/N5 reject nonpositive source conductances and unanchored ownerless graph components; the resulting unknown principal Laplacian is a nonsingular M-matrix (strict positivity along anchored paths; inverse entrywise nonnegative). Consequently `-v <= A(g)^(-1)(b(g)-A(g)x0) <= v`, proving x0−v <= x(g) <= x0+v. Clamping with the global known-temperature minimum/maximum is safe by the passive maximum principle, though not as tight as componentwise clamping. A zero r genuinely makes x0 a valid solution for *all* admissible conductances; uniqueness justifies singleton output.

A forged midpoint must pass the exact row residual check; an invalid barrier must pass all exact lower-row inequalities; a failed/broad proof refuses rather than publishing a midpoint as true. This is a **correct conditional algebraic proof**, not independent authentication of physical facts or native dynamics.

**Adversarial signed-gradient counterfactual:** Let a trial barrier have v1=1, v2=2, a J1-to-known anchor conductance 5 and a J1–J2 conductance in [1,10]. The J1 row's actual minimum is `5*1 + 10*(1-2) = -5`, while the **incorrect** lower-endpoint choice would yield `5*1 + 1*(1-2) = 4`. With r1=1 the incorrect method would falsely certify. The N7 source takes 10 on the negative term and therefore does **not** make that mistake. This was a personal analytic adversarial control, not a live mutation of N7.

### F-02 — Original T1-T does not itself exercise uncertainty propagation into junctions (MINOR coverage clarification; not a bug)

Pinned [original T1-T reference facts](https://github.com/physicsvigilante/sim_heat/blob/4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128/qualification/h1_n1/reference-facts.json) connect circular rod `T06` directly **B ↔ P**, both known body-temperature assumptions. Hence the two junction temperatures are independent of the physical Pi conductance: the residual radius for both junctions is **exactly zero**, and both enclosed junction temperatures are exact rational singletons. Using assumed `R=337, B=303, P=318` K, my independent exact Dirichlet solution gave:

- `J_Lower = 8453032705655/25123167961` K (about 336.463646574 K).
- `J_Upper = 8454784897015/25123167961` K (about 336.533390619 K).

T06 retains a genuine Pi-interval flow and influences conditional body rates, but **T1-T's junctions do not stress the new nonzero-barrier argument**. The existing one- and two-junction synthetic N7 tests *do* place circular rods at unknown nodes; documentation and test summaries should distinguish this. Recommended additional regression below; no correction is needed to the actual T1-T graph.

### F-03 — Rigorous Pi bounds, heat-flow interval semantics and graph composition check out (PASS within source-only scope)

Relevant sources: [N4 Machin enclosure lines 234–242](https://github.com/physicsvigilante/sim_heat/blob/4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128/qualification/h1_n4/static_physical.py#L234-L242), [N5 graph assembly lines 49–174](https://github.com/physicsvigilante/sim_heat/blob/4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128/qualification/h1_n5/thermal_graph.py#L49-L174), [N7 interval balance lines 223–268](https://github.com/physicsvigilante/sim_heat/blob/4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128/qualification/h1_n7/verified_junctions.py#L223-L268).

Forty positive-argument alternating arctan terms plus the signed first omitted term rigorously bracket each arctan: `Pi = 16 atan(1/5) - 4 atan(1/239)` gives Pi lower `16*a_lo-4*b_hi`, upper `16*a_hi-4*b_lo`, without a float-Pi substitution. Independently generated exact fractions have width about **4.77600323798372e-58** and bracket a separately calculated 110-digit decimal Pi. Multiplying by positive `k*d*d/(4*L)` preserves these bounds; area-form rods remain rational singletons. Source N4's binary64/static prerequisite can refuse some exotic source values, but this fails closed rather than widening Pi.

N7's four-corner positive-conductance times signed-temperature-difference product includes negative gradients and reversals. The `fromNode→toNode` sign is consistent with outward-port antisymmetry; body `dT/dt=-outward/C` and boundary outward supply have the correct signs. Independently summed flow enclosures can contain a nonzero width at an ideal junction, while the **true correlated junction balance is exactly zero** from the solved equations; N7 explicitly labels the interval sum as an overbound rather than reporting it as [0,0]. There is no time integration or integrated-energy certificate.

### F-04 — Resource limits are fail-closed results, not hard peak-memory guarantees (MINOR, nonblocking)

N7's `bounded` guards check numerators/denominators **after** constructing some `Fraction` sums/products (e.g. lines 113, 125, 147, 235–245); N6 Gaussian elimination likewise computes intermediates before checking them. The 16,384-bit rule caps stored/accepted rational results, but **not** transient allocation or CPU time of an expression immediately before a guard. Independent 4-unknown/4-circular arithmetic reached ~4,575 bits in selected result rationals, within the cap. Source facts are also constrained (256 KiB, at most 32 rods, up to 12 N7 junctions), and the hosted workflow has an overall timeout; no demonstrated out-of-budget miscertification or hang occurred. Do not describe this as a strict memory guarantee. If making an availability/DoS claim, add preoperation/work-budget probes; **not required to accept the present bounded scientific statement**.

## Independent arithmetic evidence (personally executed, not vendor N7 imported)

I authored and ran a separate pure-Python `fractions.Fraction` Dirichlet builder/eliminator, residual/row-barrier comparison and exact endpoint-corner checker offline. For each corner I independently solved the physical A(g)x=b, tested the midpoint residual inequality, rowwise lower comparison and containment in the separately reconstructed barrier envelope. *This tests the proof, not the actual N7 API's behavior on these new inputs.* Rounding below is display only; pass/fail comparisons were exact fractions.

| Fresh calculation | Independent result |
|---|---|
| Serial `H=400 -- G=Pi -- J -- G=1 -- C=300` | Analytic `T_J=(400*Pi+300)/(Pi+1)` monotone in Pi; rational Pi endpoints enclosed. J about **375.8546992994776 K**; independently constructed barrier interval width **1.115e-56 K**; both endpoint solutions inside |
| Original T1-T, T06 B–P circular, source-assumed R/B/P | J_Lower/J_Upper singletons above; `r=0` for both; two choices for the irrelevant T06 endpoint yield identical junction values |
| NEW 4-junction, 11-edge network (below) | **16/16** corner conductance selections independently enclosed; all row bounds satisfied; maximum independent barrier interval width **3.359e-56 K**, maximum corner deviation from rational midpoint **3.308e-57 K**, minimum verified row slack about **6.56e-59 W** |
| Five-edge area-only J1/J2 loop | Exact singleton temperatures `J1=3140/9` K and `J2=3250/9` K; no conductance uncertainty |
| Two unknowns, two Pi-edges, all anchors 350 K | Both junctions exact 350 K singletons, regardless of Pi |
| One junction with uncertain G in [1,10] and another G=1, anchors 400/300 | A candidate barrier exists but calculated **58.03 K** interval width exceeds the source's `1e-6 K` admission rule: must refuse |
| One junction with G in [1,1000] and another G=1 | Candidate `A_min v >= r` fails: must refuse before precision certification |
| Negative-gradient forged-row example (above) | Incorrect endpoint would certify; actual source's signed endpoint rule rejects the false inequality |

**Reproducible NEW graph (all G in W/K; four circular rods share physical Pi):** Known anchor/body assumed Kelvin nodes `H=420, C=275, M=350, X=375, Y=310`; extra isolated known body `IsolatedBody=315` K; unknown ownerless junctions J1,J2,J3,J4. Eleven source-orientable rods: `H→J1:Pi` (circular); `J1→H:1` (area parallel); `J2→J1:3Pi/4` (circular); `J2→J3:2` (area); `J3→J1:1/2` (area loop); `C→J2:Pi/2` (circular); `J3→M:4` (area); `C→J1:4/5` (area); `M→J2:1/5` (area); `X→J4:2Pi/3` (circular, separate anchored component); `J4→Y:7/5` (area). Construct each circular G with `d=0.1, L=1, k=400*c` where `c` is the multiplier of Pi; construct each area G with `k=10, A=G/10, L=1`. Positive sources, junction port degrees and anchor reachability satisfy the N4/N5 shape rules. Enumerate **16 independent endpoint choices** of the four Pi conductance intervals (a conservative superset of one correlated true Pi). Independently computed centre temperatures: J1 ~376.640520647, J2 ~340.757515497, J3 ~349.205429433, J4 ~348.958296834 K. This genuinely exercises a circular–area parallel pair, a J1–J2–J3 loop, reversed orientations, disconnected anchored subgraphs and an isolated body. It is **not represented as a local run of the checked-in solver** or as a native physical model.

## Source-level refusals and authority boundaries

Direct code examination: N4 requires a byte-exact caller-supplied SHA256, unique JSON fields, bounded/positive physical inputs, disjoint ownership and anchored components; this **does not authenticate the owner's source interpretation**. N6 rejects non-ASCII/Unicode-digit, nonfinite, oversized or nonpositive assumed body Kelvin strings; N7 demands exactly the body-node keyset and uses fixed source Kelvin for boundaries. N7 refuses nonpositive conductance, excessive junction inventory, unproved exact-centre identity, nonpositive/unproven barrier, excessive fraction bits and a certified enclosure wider than `1e-6 K`. No-unknown cases return no junctions, all-known heat flows retain interval semantics. Verified source tests include reversed flow, area-only singleton, equal-source singleton, bad hash, negative diameter, bad body keys/tokens, invalid centre mock, wide interval and all false authority flags.

**Do not misattribute personal execution:** the above source-refusal checks were **audited in the pinned code**; direct N7 unittest execution was **hosted CI**, not personally performed in this Chat B environment. My independent local corner/refusal arithmetic used a separately authored model. No artifact ZIP was downloaded or personally rehashed.

N7 response status is `VERIFIED_INTERVAL_ALGEBRAIC_JUNCTIONS_ONLY_NO_TRAJECTORY`. Source inspection confirms false `sourceInterpretationIndependentlyAuthenticated`, `ownerApprovedExpectedReferenceManifestVerified`, `independentlyCertifiedReference`, `referenceAccuracyCertified`, `referenceBundleWritten`, `allGrid77Plus8Plus5Certified`, `nativeExecuted`, `nativeQualified`, `runtimeReady`, `timeTrajectoryComputed`, `initialValueProblemSolved`, `generalH1DynamicsQualified`, `fullSystemAlgebraicAndDynamicStateSolved`, and both proof's independent-native/nominal-is-physical flags.

## Hosted CI and evidence provenance (personally fetched logs; NOT personal N7 execution)

- [PUSH workflow 44535472230](https://github.com/physicsvigilante/sim_heat/actions/runs/44535472230): GitHub API confirms `head_sha=4f4bbabc...`, `conclusion=success`, single offline job success. Retrieved its job log: **13 N7 + 13 N6 + 11 N5 + 15 N4 + 12 N3 + 16 N2 + 17 N1 interval + 34 N1 plan + 152 H1 = 283 distinct offline tests PASS**, docs parity PASS. The preserved source facts and old seven physical-100x refusals/eight native blockers are checked by the workflow; this is hosted assertion, not new native measurement.
- [PR workflow 44535966432](https://github.com/physicsvigilante/sim_heat/actions/runs/44535966432): GitHub API confirms `conclusion=success` for same source head; checkout synthetic commit `5d6384ba6949ecd52488960eacaa63862a5c3dbb` is reported to have the same full source tree. Its retrieved log repeats the same **283 tests**, not 283 new test scenarios. Docs parity PASS.
- [Historical PUSH RED 44535203687](https://github.com/physicsvigilante/sim_heat/actions/runs/44535203687): personally read job log: 13 N7 tests ran, one `KeyError: 'fullGrid77Plus8Plus5Certified'` in a test expected-field name. Later exact-head test uses the actual false field `allGrid77Plus8Plus5Certified`. The red run remains historical and is **not** rewritten as a pass.
- Logs identify push artifact `14536645257`, PR artifact `14536586428`. Their reported SHA256 values and any ZIP CRCs were **not** independently validated here. Successful job metadata cannot itself prove the mathematics.

## Separate scope judgments

| Dimension | Judgment | Basis |
|---|---|---|
| Source interpretation fidelity | **PASS within caller-supplied source facts; provenance UNKNOWN** | N4/N5 parse exact source and topology; T06 B–P confirmed; caller SHA is not owner authority |
| Physical / numerical correctness | **SCOPED PASS** | Verified universal residual and signed-row comparison logic; independent exact fractions and 16 novel corner solutions; no counterexample found |
| Native simulation / observable trajectories | **NOT TESTED / NOT CLAIMED** | No OMC or integrated IVP; all relevant flags false |
| Evidence integrity | **PASS with provenance limits** | Exact pinned tree, four added files, direct hosted log inspection, retained red; no independent artifact rehash |
| Teacher-facing usefulness | **LIMITED / not field-tested** | Rigorous instantaneous K and conditional rate intervals; no visual/native/time-domain qualification |
| Textbook-answer completeness | **NOT IN SCOPE** | No full chapter or original all-grid answer/trajectory certification |

## Recommendation and remaining gates

**Accept N7 for its narrowly described offline rational Dirichlet-junction enclosure semantics only.** No blocking finding warrants changes to the pinned mathematical implementation. The **smallest worthwhile follow-up** is to add a reproducible source-level N7 regression based on the new four-junction/two-component case, comparing returned intervals with an independently implemented rational corner solver and explicitly exercising at least one **negative unknown-to-unknown barrier gradient**; add a note that original T1's circular T06 does not affect its junctions. Treat this as an optional coverage strengthening for the current bounded method, but require it before making broader unfamiliar-composition claims. If future availability guarantees are sought, add a targeted 12-junction/32-rod rational peak-allocation/timeout stress case.

**Still prohibited:** no OpenModelica invocation, reference-bundle promotion, owner/manifest attestation, new native evidence claim, historical C1/frozen reference replacement or merge of PR68/67/66/65/64/63/62/60/59. Earlier seven 100× physical checking-centre failures, eight native blockers and the unsealed private scorer remain. A separate-conversation LLM review is independent in context, not an independent human physics certification.

**Signed:** Chat B — independently authored R2 report at the pinned source head; no production files changed.
