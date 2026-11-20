# SIM_HEAT PR #78 — independent Chat B R2 mathematical/evidence review

**Verdict: SCOPED PASS** for the **pinned, source-only H1-N11 outward-rational T1-T mathematical enclosure candidate**. This is **not** a runner-compatible/reference-accuracy certificate, a native result, a source/owner authentication, an external theorem-prover certificate, or merge/deployment permission. No blocking defect was found in the implemented interval proof for its exact admitted source and two saved grids.

**Review date:** 2026-11-20. **Reviewer:** Chat B, separate conversation and independent source/evidence inspection. **Scope:** [source draft PR #78](https://github.com/physicsvigilante/sim_heat/pull/78), [request](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-78/REQUEST.md), repository protocol/risk policy and source AGENTS.md.

## 1. Exact object reviewed, not a floating branch

| Identity | Independently checked value |
| --- | --- |
| Source repository | physicsvigilante/sim_heat |
| Source HEAD | **c96f4e1381d5eeb6c91ac075202a35633388bd8e** |
| Source Git tree | **3798a095e025a7bf90ef33a12df36c6f07ae3c9c** |
| N10 base commit | **1caea6afae55b3529c9818405d2ae669ea00be5c** |
| N10 base Git tree | **1e5c8b669b4948dd3cc5883257f0f327ca616e22** |
| Hosted PR synthetic checkout commit | **b1257ca0f3c1f5ad9e25f6512663bbe8fe2a5b0a** |
| Synthetic checkout Git tree | **3798a095e025a7bf90ef33a12df36c6f07ae3c9c**, identical to source HEAD tree |
| Source PR status at review | Open, **DRAFT**, unmerged; six commits ahead of base, zero behind |

I fetched the Git commit/tree metadata independently, compared **both complete recursive Git trees** (neither truncated: 333 and 339 entries including directory objects), and checked the six-commit compare. The **only four changed leaf files** are additions: .github/workflows/h1-n11-rational-proof-ci.yml; qualification/h1_n11/README.md; qualification/h1_n11/rational_dynamic_proof.py; qualification/h1_n11/tests/test_rational_dynamic_proof.py. Other changed tree objects are only their parent directories. There is no edit to the old H1/model/study, N1–N10, runner, C1, archived native references, or production paths relative to the reviewed base.

I downloaded CI artifact **#14619377095**, personally SHA-256-hashed the ZIP and obtained **b699279a88962b5719c061694dae30a34b48b5bd4ba2e1ea3b62882ed75f02f2**, exactly GitHub's reported artifact digest. I safely unpacked its source.tar in a separate local scratch directory, reconstructed the Git tree using Git object hashing, and obtained **3798a095e025a7bf90ef33a12df36c6f07ae3c9c**. Thus my offline reproduction used the same source tree as the PR head, not merely an archive with a plausible title. The artifact checkout-head is the synthetic commit above, with the same tree. I separately rehashed the archived source inputs: facts **39f18db09fa618bc73bbe75ca40f33d41ded70a1c73865b2a0e376973d9adfbf**; Modelica model **2c60e40f1ad8d85f46968f03712d23e8cd6b9c656cf6099a38a97d198d0873ae**; study **12ad51f59d2bd6c6561d4059f68b4263e7d4e39cdf5493f353a7affee6929d2a**. All match their frozen pins. These are source-identity checks, **not proof of independently authenticated first-author facts**.

## 2. Personally executed evidence versus hosted CI

**Personally executed by Chat B, outside the actual repository and without OpenModelica:**

- Ran the **actual archived N11 test module** on Python 3.13.5: **8/8 PASS**. This includes negative affine-row cases (both a nonzero row and an interval merely containing zero), source-hash and bad-rod refusals, one-ULP/nonfinite value checks and arithmetic/geometry checks.
- Ran a **fresh full N11 offline audit** from the exact archived tree to a new scratch output directory: **216,090 checks on 2,401 points** and **432,090 checks on 4,801 points**; total **648,180/648,180 PASS**. Full N1 byte digests reproduced exactly: 2,401-grid **b13877c8d069a60928cf3b23ae007b1a10feb53151f00ffb65a57082a7fc10af**, 4,801-grid **9ba71a1d2fccb39be071df0647793f6fb844737e2ac9c91bb143546ab8d26b40**.
- Independently probed the **actual Box implementation** with 3,000 seeded rational input pairs and **107,262 exact endpoint/midpoint containment assertions** across signed addition, subtraction, multiplication, division and inversion: all accepted assertions passed. A nonzero exact number smaller than 10^-88 correctly produces a zero-containing Box and **must refuse inversion**, rather than claim an unjustified reciprocal enclosure.
- From a regenerated, SHA-verified N1 primary trace, experimentally reversed T06 endpoints in a *scratch copy of the parsed facts*: the physical observation changed sign and checked_grid correctly refused at **T06.T_a @ 0**. Changed only **T10.G at saved index 2400 by one ULP**: correctly refused. Changed T06.Q_flow's SI unit, deleted that field, and forged nativeExecuted in altered original trace bytes: each refused (the forged flag at the original-byte hash gate). Perturbed a junction reconstruction by 0.1 dimensionless units: **physical ownerless junction balance enclosure failed**, not clamped to zero. These experiments modified neither GitHub source nor legacy archives.
- Independently assembled a separate numeric graph/Laplacian from the original model/facts, solved the two junctions and checked nonzero-time signed energy and rod flows. The Gaussian pivots are approximately **0.1276098827643** and **0.1902845440818** W/K; T06 a→b flow is approximately **−1.028157596 W** at t=0, **−0.564861064 W** at t=1200 s, and **−0.442357991 W** at t=2400 s. Body and whole-network integrated-energy residuals were near double-precision roundoff. This extra SciPy calculation is **numerical corroboration only**, not a rational proof or an independent full-grid certificate.

**First-probe corrections retained in this review record:** My initial extra test wrongly expected inversion of 10^-100 to work; the implementation correctly refused because rounding at the specified 10^88 scale includes zero. My first endpoint-reversal assertion expected the first failure at T06.Q_flow, but the correctly earlier tested T06.T_a field failed first. I corrected **only the scratch-test expectations** and reran successfully. Neither negative result evidences a source defect.

**Hosted, not personally re-executed in its original runner:** [CI run #44715215240](https://github.com/physicsvigilante/sim_heat/actions/runs/44715215240), job **136216752692**, triggered by pull_request, attempt 1, completed **SUCCESS** for exact head c96f4e1 and synthetic checkout b1257ca0. Logs give the individual unittest suite counts **8+6+6+18+13+13+11+15+12+16+17+34+152=321 PASS**, including **8 new and 313 inherited** tests, plus the N9 **100,828** static replay, N10 **648,180** high-precision numerical comparisons and the full N11 rational pass. Actions/checkout, setup-python and upload-artifact are pinned by action SHA. The CI-only package install is Python/numpy/scipy/mpmath, not an OpenModelica toolchain. The job performed **no OMC install/version/build/launch**. Green logs alone would not establish any of the proofs below; the separate mathematical inspection and local replay are important.

## 3. Mathematical checks and independent reasoning

### M1 — signed outward rational arithmetic: PASS within stated domain

[Box lines 56–125](https://github.com/physicsvigilante/sim_heat/blob/c96f4e1381d5eeb6c91ac075202a35633388bd8e/qualification/h1_n11/rational_dynamic_proof.py#L56-L125) use integer endpoints divided by S=10^88. Floor on the exact low rational and ceiling on the exact high rational include both endpoints, including negative rationals. Addition and sign reversal are exact on integer endpoints. For multiplication, the minimum/maximum of all **four** endpoint products are divided by S with outward floor/ceiling. A positive interval reciprocal uses floor(S²/high) and ceil(S²/low); negative intervals use sign reversal; every zero-crossing or zero-touching denominator refuses. Division is outward multiplication by that reciprocal. This argument works for signed and mixed-sign inputs; no floating-point operation is needed in this interval path. The random probes above challenged, but do not replace, this reasoning.

### M2 — 43-term Machin Pi and circular geometry: PASS

[Pi/source lines 152–170 and 210–224](https://github.com/physicsvigilante/sim_heat/blob/c96f4e1381d5eeb6c91ac075202a35633388bd8e/qualification/h1_n11/rational_dynamic_proof.py#L152-L224) implement Pi = 16 atan(1/5) − 4 atan(1/239). As an independent identity check, tan(4 atan(1/5))=120/119 and subtracting atan(1/239) gives tangent exactly 1 in the first quadrant. Each alternating atan series has decreasing positive term magnitudes. The first omitted k=43 term is **negative**; hence the 43-term partial sum is the upper atan endpoint, and partial-plus-omitted is the lower endpoint. The negative coefficient for atan(1/239) is reversed correctly in the final Pi bounds. Independently computed exact fractions give Pi interval width about **2.8458×10^-62**; a 130-decimal-digit mpmath value fell within it as a non-proof sanity check. The circular rod uses **A=Pi*d²/4**, with source decimals parsed to exact Fractions, then **G=k*A/L**. The N4 grammar supplies bounded exact source decoding, **not** N4's physical results.

### M3 — graph, interval Gaussian pivots and normalized dynamics: PASS

[Physics lines 191–291](https://github.com/physicsvigilante/sim_heat/blob/c96f4e1381d5eeb6c91ac075202a35633388bd8e/qualification/h1_n11/rational_dynamic_proof.py#L191-L291) reconstruct the ten oriented rods over seven original nodes. Each physical edge adds (+G,+G,−G,−G) to the proper Laplacian entries; by this paired construction each **true** row sums exactly to zero, while its interval residual merely must include zero. Neither ownerless junction is assigned capacity. For the 2×2 junction matrix [a b;c d], interval Gaussian elimination applies m=c/a, s=d−mb; the admitted intervals require **a.low>0 and s.low>0**. The separate known-node right-hand-side solves x2=(rhs2−m rhs1)/s, x1=(rhs1−b x2)/a therefore enclose each true physical solution. Dependency overestimation is conservative, not a false inverse. Positive independent approximate pivots are reported in §2.

For normalized u=(T−289 K)/(78 K), tau=t/(2400 s), the body equation C dT/dt = −L T becomes du/dtau = −2400 C^-1 L u with the constant fixed-boundary contribution; the 289 K offset vanishes because the **actual** L has zero row sums. Three integrated states obey d(v_i)/d tau=u_i, and the seventh constant state is 1. There is no float-dependent conversion of source parameters here. Initial states, boundary offsets and the 2400 scaling have correct dimensions. The model and explicit port orientation agree with the stored original Modelica model and SimHeat thermal-port semantics.

### M4 — descending 24th-degree matrix Horner and global tail: PASS

[Exponential lines 294–337](https://github.com/physicsvigilante/sim_heat/blob/c96f4e1381d5eeb6c91ac075202a35633388bd8e/qualification/h1_n11/rational_dynamic_proof.py#L294-L337) build X=B/N, take each entry's **outward absolute upper endpoint**, and sum each row to obtain rho >= ||X_true||_infinity, not a fitted midpoint or an externally accepted rho input. The procedure refuses unless **0<rho<=1/2**. Starting H=I and descending k=24,...,1 with H←I+XH/k produces **exactly** the 24th-degree Taylor polynomial I+X+X²/2!+...+X^24/24! before outward interval evaluation. Interval matrix multiplication encloses each corresponding true product.

For every actual X in the input boxes, submultiplicativity gives ||X^k||_infinity <= rho^k; thus the tail after degree 24 obeys ||R||_infinity <= exp(rho) rho^25/25! <= **2 rho^25/25!**, and each matrix entry is bounded by the same scalar. The implementation rounds **this exact Fraction tail outward** to a whole fixed-point radius and expands **every** H entry, so it cannot understate the tail at 10^-88 resolution. The source B's full last generator row is separately required to equal **integer endpoint [0,0] in every column**; merely containing zero fails. Only then is the exponential's last row exactly [0,...,0,1] and safe to replace. That guard covers the prior affine-row defect class.

The independently checked norm values are approximately **rho=0.001230091018559613** (N=2400) and **0.000615045509279807** (N=4800), both well inside 1/2. The corresponding exact-receipt tail values are about **2.2846×10^-98** and **6.8087×10^-106**; rounding to the 10^-88 interval tick remains outward. Inductive interval matrix-vector multiplication encloses the true state at **every saved step**. This is not an interpolation or continuous-time claim between saved instants.

### M5 — physical outputs, signed conservation and full-grid budgets: PASS

[Sampling lines 343–425](https://github.com/physicsvigilante/sim_heat/blob/c96f4e1381d5eeb6c91ac075202a35633388bd8e/qualification/h1_n11/rational_dynamic_proof.py#L343-L425) independently reconstructs T=289+78u and its exact-in-time integral ∫T dt=289t+78·2400∫u d tau, including fixed boundaries and Gaussian-solved junctions. Each rod carries q_ab=G(T_a−T_b), q_ba=−q_ab and corresponding integrated flow; body Q_in is the sum **into** that body; maintained-boundary Q_to_network is **minus** the flow into the boundary. Body dU=C(T−T_initial) is not imposed to equal integrated Q; separate interval residuals check the identity. Ownerless node flux must contain zero and global stored energy minus signed boundary supply must contain zero. The deliberate junction corruption in §2 actually failed these checks. The checks alone would be weak if made with unbounded intervals, but here the full-grid physical enclosures are very narrow: maximum exported width about **6.42×10^-59** and integrated-flow width about **1.07×10^-58** on both grids.

[Field comparison lines 428–526](https://github.com/physicsvigilante/sim_heat/blob/c96f4e1381d5eeb6c91ac075202a35633388bd8e/qualification/h1_n11/rational_dynamic_proof.py#L428-L526) require exact source-grid times and matched field inventories, authoritative export SI-unit strings, original SHA-verified N1 traces, and all **77 internal exports + 8 original requests + 5 integrated flows** at **2401+4801** points. Every original binary64 centre is converted to its **exact Fraction**. The actual check is stronger than simple distance-to-interval: max(|centre−lo|,|centre−hi|) <= allowance. Allowances are frozen at **1.1×10^-7 K**, **10^-8 W**, **10^-5 J**, or **0.64 ULP** for positive C/G/A; no network-scale dilution or post hoc tolerance fitting. The independently rerun maximum error/budget ratios are:

| Grid | Exports | Public requests | Signed integrals |
| --- | ---: | ---: | ---: |
| 2401 samples | 0.7692307692307693 | 2.5834224890436064e-7 | 4.545830383616656e-8 |
| 4801 samples | 0.7692307692307693 | 2.5837877244600293e-7 | 4.545830383616656e-8 |

All ratios are below 1. These **648,180 checks are correlated quantity/sample checks**, not 648,180 independent experiments. N9's earlier **100,828** static comparisons overlap this inventory; N10's 90-digit calculation remains corroboration, not the N11 proof.

## 4. Findings and required disposition

**F0 — No blocking mathematical defect found (PASS within scope).** The source admits a valid outward real interval calculus and exact Pi/source rational domain; Gaussian pivots enclose the true junction solution; the Horner remainder is justified by a real induced-matrix norm; the affine-row replacement has the necessary exact premise; and accumulated full-grid fields and signed energy were checked. The independent replay and adversarial refusals support that code inspection. No scope broadening is inferred.

**F1 — LOW, wording clarity, nonblocking.** The receipt field **individualPhysicallyEnclosedSamples** and phrases such as "the N1 observation is enclosed" can be read as requiring each *float64 centre itself* to belong to the narrow real physical Box. That is **not** the criterion in compare_float: the Box encloses the **ideal real source-physical answer**, while the N1 centre must lie within the conservative checking allowance of **both** interval endpoints. It may be outside the Box by sub-ULP rounding and still correctly pass. Recommended future documentation/receipt wording: **648180 centre-versus-rigorous-physical-enclosure budget checks**. Do not modify tolerance or change current source merely for terminology.

**F2 — LOW, future regression hardening, nonblocking for this pinned SHA.** The eight committed focused N11 tests do not individually freeze all of the successful Chat B direct-tamper cases: reversed rod orientation, a late one-ULP constant, missing field, wrong unit, original-byte fake-native flag, and perturbed nonzero-time junction balance. Add bounded tests for these **before future proof-semantic changes** to prevent regression. The present exact-head audit/independent probes did reject them. No wider retest of unchanged N1–N10 is requested just to satisfy review volume.

**F3 — OPEN EXISTING AUTHORITY BOUNDARY, not an N11 proof defect.** A real proof conditional on the pinned transcribed source facts does **not** independently authenticate that the first author supplied those facts, reproduce a lost private scorer key, seal first-author evaluation, or establish a native Modelica/runner output. N11 still calls the prior N4 source grammar for input validation and regenerated, SHA-pinned N1 traces for **candidate float64 centres**; it does not import N4 static numeric answers or N1 physics to build the independent outward enclosure. This is **algorithmic mathematical independence within a common source**, not independent source provenance or external certification.

**F4 — OPEN EXISTING NATIVE/REFERENCE BLOCKERS, not waived.** Artifact original-hold.json again records **nativeExecutionReady=false**, **referenceAccuracyCertified=false**, **nativeCallsThisCheck=0**, and **eight** execution blockers:
1. R2_PLAN_REVIEW_NOT_YET_COMPLETE
2. EXACT_RUNTIME_IMAGE_BINARY_AND_MSL_MANIFEST_UNBOUND
3. INDEPENDENT_100X_REFERENCE_ERROR_CERTIFICATE_NOT_IMPLEMENTED_OR_VERIFIED
4. STATIC_CHECKING_CENTRES_FAIL_PHYSICAL_100X_BOUND
5. TARGET_HOST_ALL_THREE_NEW_REFERENCE_SEALS_AND_REPLAY_NOT_READY
6. PRIMARY_ONLY_COMMON_TIME_COMPARATOR_NOT_IMPLEMENTED_OR_REVIEWED
7. EXACT_EXECUTION_MANIFEST_SINGLE_USE_CONTROL_AND_COMPANION_BYTES_NOT_READY
8. SEPARATE_EXPLICIT_NATIVE_OWNER_PERMISSION_NOT_GRANTED

The **seven historical physical 100× failures remain open and unchanged**: **T02.G, T06.A, T06.G, T07.G, T08.G, T10.G, T_Plug.C**. The original first-author scorer remains **H1-T1-UNSEALED**. N11 does not repair, mask, replace, promote or re-baseline any of these. In the new receipt, independentExternalMathematicalCertification, fullDynamicPhysical100xIndependentlyCertified, referenceAccuracyCertified, independentlyCertifiedReference, runtimeReady, referenceBundleWritten, externalOwnerApprovalVerified, nativeExecuted, nativeQualified and historicalReferenceRegenerated are **all false**.

## 5. Gate conclusion

**SCOPED PASS** is appropriate **only** for the bounded proposition: at source commit **c96f4e1381d5eeb6c91ac075202a35633388bd8e**, the separately implemented, outward-rational N11 source-physical mathematical method provides defensible enclosures and checks the existing two original full-grid float64 T1-T candidate traces against the predeclared 100× *candidate* budget. Hosted CI was reviewed and a fresh offline replay and independent adversarial probes were personally executed. No unaddressed N11 mathematical blocker was identified.

**Do not** use this review to set any currently false authority/certification flag true, adopt a runner reference, rework the seven failing legacy checking centres silently, override eight native blockers, seal the missing author scorer, run/install/build/launch OpenModelica, promote any native artifact, merge PR #78 or PR #77, or deploy. Those are **separate unsatisfied gates requiring explicit owner approval and the appropriate native/provenance evidence**. Historical source, negative evidence and prior reports remain untouched.

*Review publication itself is a new Chat B report in the central review hub; it is not a GitHub review/approval of the source PR and cannot automatically change its required status checks.*
