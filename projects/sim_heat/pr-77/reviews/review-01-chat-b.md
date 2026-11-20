# SIM_HEAT PR #77 — independent Chat B R2 review of H1-N10

**Verdict: SCOPED PASS — numerical source-only corroboration ONLY.** No native qualification, independently certified all-grid 100× physical error bound, reference adoption, owner authentication, production merge, or deployment is approved.

| Field | Reviewed identity / provenance |
|---|---|
| Source repository / PR | [physicsvigilante/sim_heat PR #77](https://github.com/physicsvigilante/sim_heat/pull/77), still DRAFT and UNMERGED when inspected |
| Exact reviewed source HEAD | [`1caea6afae55b3529c9818405d2ae669ea00be5c`](https://github.com/physicsvigilante/sim_heat/commit/1caea6afae55b3529c9818405d2ae669ea00be5c) |
| Parent / comparison base | `8e47a0a7c0a99694649fa8a1526ef50088e7dbd2` (draft PR #76, not re-reviewed wholesale here) |
| Exact source Git tree | `1e5c8b669b4948dd3cc5883257f0f327ca616e22` |
| CI synthetic PR merge checkout | `ae003550728c67c49527d2ce04e2963969903b38`; **same Git tree** `1e5c8b669b4948dd3cc5883257f0f327ca616e22`, parents base + corrected HEAD |
| Reviewer / date | Chat B, separate ChatGPT conversation, GPT-6; 2026-11-20 (UTC+05:30). Independent context and independent scratch arithmetic, **not** a different verified human examiner/model family |
| Risk / scope | R2: physical equations, numerical method, sample-level checking and provenance. Read `review_sandbox/PROTOCOL.md`, risk policy, request, source `AGENTS.md`, H1 implementation contract, offline amendment and C1 freeze |
| Source changes during review | **None**. This report is the only requested new GitHub file |
| Personal execution | An independently authored **offline SciPy DOP853** physical thermal-network calculation at selected times; **no N10 full-grid rerun**, no OpenModelica, no native launch, no artifact ZIP download/rehash |
| Hosted execution inspected | Actual red and green GitHub workflow metadata, per-step states, full job logs, original source diff, exact-commit Git tree metadata and uploaded artifact metadata |

## 1. Exact-source and CI identity

**PASS for this scope.** Git compare from PR76 base to this HEAD shows precisely four *added* paths: `.github/workflows/h1-n10-dynamic-ci.yml` (144 lines), `qualification/h1_n10/README.md` (40), `qualification/h1_n10/dynamic_crosscheck.py` (420), and `qualification/h1_n10/tests/test_dynamic_crosscheck.py` (128). No existing N1–N9, H1 production Modelica/runner, original model/study/facts, C1, reference bundle, archive, or historical review is changed. The final commit has one parent `444299274bb460a38e18704e553cb0856e6571b7` and alters **only** the new test's `T_Plug.C` assertion (`assertEqual(mpf(0.41)*mpf(390), mpf(159.9))` to `mp.almosteq(..., abs_eps=1e-80)`). The physics implementation, N1 reference, acceptance allowances and input facts were not altered by this fix.

Preserve the **actual FAILED** [first hosted run #44702322384](https://github.com/physicsvigilante/sim_heat/actions/runs/44702322384), source `444299...`, job `136173422781`: five of six N10 probes passed; one failed on different last-digit mpmath representations of `0.41*390` versus separately parsed `159.9` (the red log shows `AssertionError`). Historical hold, N9 full-grid and N10 full-grid steps were **SKIPPED** on that red run. This was a legitimate failing test, not a passing run and not an observed dynamic-physics mismatch. The correction is a test-only tight numerical comparison, not a general tolerance relaxation.

The corrected [run #44702458746](https://github.com/physicsvigilante/sim_heat/actions/runs/44702458746) has event `pull_request`, source `head_sha=1caea6af...`, **completed/success**, job `136173870186`; all substantive steps passed. The checkout is GitHub's synthetic merge `ae003550...`; I separately fetched the Git commit/tree metadata for this merge and exact source HEAD and found **identical tree SHA** above, rather than treating a green badge as proof of source identity. The workflow checks its two merge parents against the fixed base and event source head, exactly four added paths, three source-blob SHA pins, and an unchanged original-source subtree fence. Its dependencies are checking-only Python `numpy==2.3.5`, `scipy==1.17.0`, `mpmath==1.3.0` on Python 3.13.5; there is no OMC install/version/build/launch command.

The actual job log reports **313 distinct Python tests passed** (six N10 and 307 inherited N1–N9/H1), product docs parity, the eight-blocker/seven-failure hold, N9 100,828 static sample checks and N10 648,180 comparisons. These are **hosted observations**, not my own reruns. Artifact [14613567475](https://github.com/physicsvigilante/sim_heat/actions/runs/44702458746/artifacts/14613567475) is present in GitHub metadata, 1,594,995 bytes, GitHub-reported ZIP digest `sha256:9e311b5c83bff23fbb2561a0b86bbadd34fd3f4409cdada1a8d4837e662a5d25`. **I did not download, independently hash, or reconstruct that ZIP/source.tar**; its digest is provider-reported provenance, not an independently rehashed artifact.

## 2. Physical equation and signed-flow challenge

**PASS as a separately implemented *numerical* physics formulation for the pinned T1-T network.** I read `qualification/h1_n1/reference-facts.json`, original `inputs/T/model.mo`, and the original `inputs/T/study.json` directly at the exact source commit, not inferred from N1 trajectory exports. Physical facts are 3 finite bodies, fixed baths at 367/289 K, 2 ownerless junctions and 10 rods. Initial body states (Ridge/Collar/Plug) are (337, 303, 318) K, with capacities `147.2, 199.2, 159.9 J/K`. T06 is a circular **diameter** `d=0.016 m`, giving `A=πd²/4`; it is oriented `B→P`, not `P→B`.

The independent N10 assembly implements an oriented undirected-conductance Laplacian: each rod adds `+G` on its two node diagonals and `-G` off-diagonal, `G=kA/L>0`. Junctions satisfy `L_jj*T_j=-(L_jd*T_d+L_jf*T_f)`; the general mpmath junction inverse determines `T_j` without N1's special 2×2 interval Schur/Taylor data. Dynamic bodies satisfy `C_i*dT_i/dt=-Σ_j L_ij*T_j`, with fixed-temperature forcing; the 7×7 augmented ODE tracks 3 actual temperature states, their 3 temperature integrals and affine 1. The matrix-exponential step is advanced exactly once per original grid interval in **90-decimal-digit arithmetic**. This construction is dimensionally and sign-consistent with the H1 Modelica thermal connector contract and has no invented junction capacitance.

The independently reconstructed quantities in `snapshot` use the actual first-author request operations: 3 body temperature targets; Ridge and Plug energy changes; oriented T06/T10 heat flows; and `T03.port_a - T_Cool.port`. For a rod, `Q_flow=G*(T_a-T_b)`, `port_a.Q_flow=+Q_flow`, `port_b.Q_flow=-Q_flow`; its contribution to the **connected node** is `-Q_flow` at a and `+Q_flow` at b. Thus a body's `Q_in` is net incoming, each boundary's `Q_to_network` is **minus** its node incoming, each body `dU=C*(T-T_initial)`, and integrated flows use integrated node temperatures including fixed boundaries' `t*T_fixed`. Global identity: `Σ_body ΔU = ∫(Q_Warm,to_network+Q_Cool,to_network)dt`. Reversing rod orientation changes that rod's reported signed flow but not its Laplacian/body trajectory; N10 contains an explicit T06 reversal test. The isolated two-body test checks a conserved zero mode, not an artificial fixed bath.

**Personal independent spot calculation (not N10 execution):** I separately hand-transcribed the first-author rod graph and source values and solved the two Kirchhoff junction equations and body-energy ODE with Python/SciPy `solve_ivp(DOP853, rtol=atol=2.3e-14)`, integrating body and bath heat flows as *additional* physical ODE states. This uses ordinary double-precision source literals (hence is **not** a 90-digit bound/certification):

| Time (s) | Independent numerical observations |
|---|---|
| 0 | `T_JUpper ≈336.53339061936 K`, `T_JLower ≈336.46364657423 K`; `T06.Q_flow≈-1.02815759572 W`; `T10.Q_flow≈+0.00215334739 W`; body `dU` and all flow integrals are zero |
| 600 | (Ridge, Collar, Plug) `≈(334.86411247,307.69088794,318.26104216) K`; `T06≈-0.724518957 W`, `T10≈+0.001611560 W` |
| 1200 | `T10≈-0.005854433 W` **changes sign** from initially positive, while `T06≈-0.564861064 W`; a nontrivial signed-flow challenge |
| 2400 | (Ridge, Collar, Plug) `≈(332.39702298,315.39009452,321.84374510) K`. Integrated bath supply `≈(+4946.23283243,-2541.06937913) J`; body `ΔU≈(-677.55821670,+2468.10682814,+614.61484186) J`; global energy mismatch approximately `2.1e-11 J` at double precision |

At these instants, the separately coded junction flow-balance residuals were around `1e-14 W` and per-body heat-integral balances around `1e-11 J` or smaller. These independently challenge source orientation, energy conservation and a later-time T10 sign reversal. They do **not** assert equality to any personally reloaded N1 CSV/JSON, prove uniform all-grid bounds, or replace the hosted comparison.

## 3. Entire-grid comparison and certificate boundary

**PASS as audited hosted numerical corroboration; NO as an independently certified error enclosure.** In `audit`, N10 first verifies original raw source-facts, model and study SHA256 pins:

- Facts: `39f18db09fa618bc73bbe75ca40f33d41ded70a1c73865b2a0e376973d9adfbf`.
- Model: `2c60e40f1ad8d85f46968f03712d23e8cd6b9c656cf6099a38a97d198d0873ae`.
- Study: `12ad51f59d2bd6c6561d4059f68b4263e7d4e39cdf5493f353a7affee6929d2a`.

It regenerates N1 candidates **only in disposable scratch**, checks their own report-to-blob digest, invokes unchanged N9 `verify_historical_grid` and N4 exact-source static crosscheck **before** comparing a numerical dynamic sample. N9 rejects non-original complete-trace bytes, wrong field inventory, nonfinite values, false evidence flags, foreign units, changed static bits and changed original grid. Both original complete trace digests are retained, not rewritten: `b13877c8d069a60928cf3b23ae007b1a10feb53151f00ffb65a57082a7fc10af` (2401 samples) and `9ba71a1d2fccb39be071df0647793f6fb844737e2ac9c91bb143546ab8d26b40` (4801). There is no native MAT/CSV import.

N10 `compare_grid` enumerates each original saved instant, checks `timestamp == float(2400*i/grid)` **without interpolation**, checks **exact channel name sets** of independent predictions vs original candidate, derives units from source operations (and checks exported column unit labels) and calls the fixed per-unit scalar comparator on *each channel at each sample*. Totals are `(77+8+5)*(2401+4801)=90*7202=648180` (216,090 primary; 432,090 dense). Note that the 77 exports **include 14 static quantities** already checked by N9: 100,828 of the N10 scalar comparisons revisit static channels; some dynamic port/public quantities are also algebraically related. The count is honest but must **not** be described as 648,180 statistically independent physical facts.

The comparator uses predeclared conservative **1/100-native-allowance** limits: temperature `1.1e-7 K`, flow `1e-8 W`, energy/integral `1e-5 J`, and `0.64 ULP` for static C/G/A at their candidate floating-point magnitude. It checks each scalar independently, not a sum/max error budget pooled across channels. The exact hosted receipt printed in the green log reports:

| Grid | Exports max ratio / allowance | Public requests | Integrated flows |
|---|---:|---:|---:|
| 2400 intervals | 0.7692307692307693 | 2.5834224890436064e-7 | 4.545830383616656e-8 |
| 4800 intervals | 0.7692307692307693 | 2.5837877244600293e-7 | 4.545830383616656e-8 |

All are below 1. The 0.76923 highest ratio is from the **static export** group and is compatible with ordinary correct binary64 rounding under a 0.64-ULP limit; it is not a rigorous time-integration error estimate.

**Fundamental evidence limit, NOT a newly discovered code defect:** mpmath's 90-digit arithmetic, `mp.inverse`, repeated `mp.expm` steps and agreement with SHA-pinned N1 candidates provide *no proved outward rounding/truncation enclosure* or independent global propagation bound, even if all comparisons are tiny. N1 remains a same-source, unapplied checking candidate. Shared source facts can carry a common conceptual error, and neither checker executed OpenModelica. Therefore N10 correctly keeps `newMethodIsRigorousIntervalProof=false`, `fullDynamicPhysical100xIndependentlyCertified=false`, `referenceAccuracyCertified=false`, and `independentlyCertifiedReference=false`. Any statement that N10 **certifies** a 77+8+5 full-grid physical 100× reference, validates native output, or authorizes reference migration is unsupported.

## 4. Findings and adversarial input/authority boundaries

**F-01 — no demonstrated blocker in the exact pinned audit path (positive scoped finding).** `load_original → N4 parse_facts → audit → fresh N1 certify → N4 static candidate → N9 full-blob verify → compare_grid` has source SHA fences, full trace identities, unit/name/finite checking, per-sample physics comparison and an output target restricted to a *new* scratch directory outside the repository. Workflow and report do not advertise a native result. The inherited rejection tests, N10's six probes, source-tree fence and hosted full-grid pass support this restricted statement. The original negative red result is retained.

**F-02 — MINOR, untrusted *direct helper* hardening; NOT an audit-path certification bypass.** Source `qualification/h1_n10/dynamic_crosscheck.py`, `assemble` docstring and rod-kind `if/else`, and `compare_grid` trace field indexing. These helpers assume a previously **N4-admitted** fact object or **N9-verified** trace; they do not independently authenticate arbitrary direct callers. In `assemble`, any non-`RodArea` `kind` with a `d` key follows the circular branch instead of a new explicit kind refusal. In `compare_grid`, a malformed direct trace missing `columns` / `requests` / `integrals` can raise a raw `KeyError` instead of `ReplayRefusal`. In `compare_value`, a giant Python integer can produce an `OverflowError` in `math.isfinite` (I independently confirmed this Python behavior, not an N10 end-to-end exploit). Direct use of `snapshot` similarly assumes `assemble` produced a validated system. **Static source inspection / Python language probe**, not a demonstrated issue in trusted audit or CI. The exact public `audit` does not accept substituted physical facts or unverified original traces, so none of these helpers can turn a forged scratch graph into a source-authorized native result. Recommended before making these helpers a public untrusted API: make their preconditions explicit/internal, or add an admission/refusal wrapper and negative tests covering unknown rod kinds, wrong/absent field types, nonfinite/oversized integers and direct-call bad traces.

**F-03 — MAJOR release/certification condition, known and correctly preserved, not blocking N10's limited mathematical result.** No independent *rigorous* full-dynamic 100× physical error bound; no source/owner authentication or live native evidence. Numerical corroboration cannot close these gates. Do not update release-status words or adopt a runner reference based on this review.

**F-04 — provenance limitation, non-blocking scoped source review.** Hosted artifact name, size and ZIP SHA256 were checked via GitHub job log and artifact metadata; the ZIP itself and internal archived `source.tar` were **not** independently downloaded/rehash-validated. A release requiring artifact-chain assurance must perform that separate verification. Log and Git tree matching are strong source-checking evidence but not a substitute for binary artifact custody.

## 5. Historical holds — explicitly unchanged

The seven original legacy `h1.reference.prepare` physical-static 100× failures remain **FAIL/OPEN**: `T02.G`, `T06.A`, `T06.G`, `T07.G`, `T08.G`, `T10.G`, `T_Plug.C`. Corrected CI asserts this exact list, asserts **eight native execution blockers** and `nativeCallsThisCheck == 0`; neither N9 nor N10 retroactively repairs old checkers. The first-author private evaluator/scorer key remains lost/unsealed; no recovered hidden independent authority, independent owner seal, signed one-shot lease, verified OMC/MSL/host identity, approved native plan, runner-compatible reference bundle or successful actual native qualification is established. The receipt's `runtimeReady`, `referenceBundleWritten`, `externalOwnerApprovalVerified`, `nativeExecuted`, `nativeQualified` and `historicalReferenceRegenerated` fields are all **false**. Old attempts, failures, native archives, source N1 traces, PR76 and PR77 draft/unmerged states must remain preserved.

## 6. Separate scope judgments

| Dimension | Decision | Basis |
|---|---|---|
| Source interpretation fidelity | **PASS for pinned illustrative T1-T** | Original author `model.mo` connectivity, source facts and eight `study.json` requests inspected; 10 correct oriented rods, 2 ideal junctions, SI units and circular diameter respected. These inputs are illustrative, not presumed textbook facts |
| Physical/numerical correctness | **SCOPED PASS, certificate UNKNOWN** | Independent sign/Kirchhoff/energy derivation, locally computed nonzero-time physical samples and signed reversal; hosted 648,180 checking comparisons. mpmath does not provide a rigorous global error enclosure |
| Native simulation / observable coverage | **NOT TESTED / BLOCKED** | Zero native launches; eight blockers; no certified native traces; no actual viewer/teacher session |
| Evidence integrity/provenance | **PASS with limitations for checking-only provenance** | Exact source-vs-synthetic tree, CI logs and step status, original SHA pins, preserved first red and two original N1 trace digests; artifact ZIP itself not personally rehashed |
| Teacher-facing usefulness | **UNKNOWN / NOT TESTED** | No pedagogical interaction, classroom study, native viewer or UI run |
| Textbook-answer completeness | **NOT APPLICABLE** | A source-illustrative thermal graph with eight authored observations, not a claimed textbook exercise solution |

## 7. Disposition and minimal next actions

**SCOPED PASS** for retaining N10 as an independent-method **source-only, high-precision numerical corroboration** layer at exactly `1caea6afae55b3529c9818405d2ae669ea00be5c`. No demonstrated defect requires changing this pinned audit before accepting that limited claim; F-02 is helper-hardening advice if those functions acquire an untrusted/public call boundary.

For any **stronger** physical-reference claim, produce a separately justified and independently checked all-grid outward error certificate for the physical source (including decimal-to-physical interpretation, matrix inverse/exponential/truncation/rounding, time propagation, signed integrals, 77 exports and eight requests); preserve both original N1 trace SHA pins and compare without loosening predeclared allowances. Native run, owner trust, original seven legacy reference failures and eight native blockers require their **own** authorizations/repairs, not a relabeling of N10. A review of a new source/physical method is a new R2 event; owner separately controls all merges.

**No OpenModelica installed, queried or executed; no original reference promoted; no simulator/source file, historical evidence, PR branch, or native bundle changed; no deployment or merge.**
