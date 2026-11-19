# SIM_HEAT PR65 — Independent R2 review-01: generic source-exact static physical reference candidate

**Decision sought:** SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE for a NEW **offline-only, graph-independent static thermal quantity candidate**. This is a genuine physical/numerical implementation requiring independent source-math scrutiny. It is **not a runnable native reference or full H1 trajectory/generality certification**.

## Pinned source

- [Draft source PR65](https://github.com/physicsvigilante/sim_heat/pull/65) exact HEAD **`a704e100d6760423b08cb07eca131ada8a629db2`**, complete Git tree **`b3e3036622639814f830470dcd8319ffd70a7761`**.
- Stacked on independently scoped-approved but still DRAFT PR64 base HEAD **`0cf275241e718fbcd2b2d2c1f7761565c7c06a92`**, tree **`4f253f1959797362d68ad4e153552b776ff82f33`**. Earlier PR63/62/60/59 also remain draft/unmerged; production main unchanged.
- GitHub PR synthetic merge `8cd709902b9127d838ed3c5d2e34d8574a9dc129` has **exact same whole Git tree**, ordered parents PR64 base then PR65 exact HEAD. Exact [base→head compare](https://github.com/physicsvigilante/sim_heat/compare/0cf275241e718fbcd2b2d2c1f7761565c7c06a92...a704e100d6760423b08cb07eca131ada8a629db2) adds only **four N4 paths**: `qualification/h1_n4/static_physical.py`, `README.md`, `tests/test_static_physical.py`, and `.github/workflows/h1-n4-static-reference-ci.yml`. No production H1/Modelica/runner, old N1/N2/N3, old checking reference or frozen C1/first-author evidence touched.
- Original T1-T facts SHA256 **`39f18db09fa618bc73bbe75ca40f33d41ded70a1c73865b2a0e376973d9adfbf`**, model SHA **`2c60e40f1ad8d85f46968f03712d23e8cd6b9c656cf6099a38a97d198d0873ae`**, study SHA **`12ad51f59d2bd6c6561d4059f68b4263e7d4e39cdf5493f353a7affee6929d2a`**.

## Physical and authorability objective

A new supported H1 fact graph composed of `Body`, `RodArea`, `RodCircular` and maintained boundaries should require no code modifications to derive static body `C=m*c`, conductor `G=k*A/L` and circular `A=πd²/4`; neither T1-T-specific labels nor native/candidate values enter core. Inputs are separately expressed reference facts raw UTF-8 bytes + matching SHA, consumed as exactly read. Caller-supplied SHA is **not an authenticated pre-output manifest** and does not independently prove source fidelity.

The candidate parses decimals as bounded Decimal/Fraction exactly, refuses duplicate JSON keys, nonfinite/exponent bombs, unknown/implicit geometry, invalid rod/graph ends, unowned/unused nodes, unsupported steady/transient analysis and bad source hash. It uses Machin rational alternating-series bounds for mathematical Pi, integer-only IEEE binary64 nearest-even rounding (including ties/subnormals/overflow) and requires **both exact physical endpoints round to identical bits**. For each static output, computed centre must have maximum exact-rational physical interval distance <= **1/100 of ORIGINAL 64-ULP native static allowance =0.64 ULP**. No broadened thresholds, source-order hypothesis promoted as physics, fitted values or chosen-after-result target.

Original T1-T **14** new candidate C/G/A bit patterns match the independently **predeclared** PR60 correctly-rounded-physical feasibility witnesses, but the original seven **unchanged** legacy checking centres still fail their old source-physical 100x bound. These new static candidates are **not adopted** by legacy `h1.reference.prepare` or the existing native runner, and must not be substituted into old reference bundles. Tests demonstrate two new developer-authored component compositions (steady/transient). They are NOT the independent post-freeze unfamiliar H1 composition required by N3 to establish generalized LLM authorability.

## Hosted evidence, not independent proof

- Initial implementation push [CI 44500952639](https://github.com/physicsvigilante/sim_heat/actions/runs/44500952639) SUCCESS with 11 new static tests.
- Final exact-head PUSH [CI **44501357510**](https://github.com/physicsvigilante/sim_heat/actions/runs/44501357510) **SUCCESS**, artifact ID **14516099708**, GitHub SHA256 `a916850787df7b93fee7efe249cb59aeccb30439c1ec8746dfc80d238c01c93d`.
- Final exact-head PR checkout [CI **44501759662**](https://github.com/physicsvigilante/sim_heat/actions/runs/44501759662) **SUCCESS**, artifact ID **14517098201**, GitHub SHA256 `f568ceec9ade9df5f236567670cc435a8684f08ee7b64bfeb35927a849d63801`.
- Hosted decoded logs: per workflow **12 new N4 +12 N3 design +16 N2 comparator +17 N1 interval +34 N1 plan +152 H1 =243 distinct tests PASS**, docs parity PASS, exact diff/source SHA checks PASS, old seven failures/eight native blockers remain, zero native calls. Two CI runs overlap. Artifacts above have GitHub-reported hashes; Chat A has **not personally downloaded or CRC-rehashed ZIPs** in this milestone.
- Final source-only static candidate JSON appears only as a **labelled offline CI artifact**; it is not a reference bundle, native trace or independent physical method certificate.

## Reviewer attack scope

Review exact source and tests, independently reproduce source-physical C/G/A equations (including circular RodCircular), Pi interval remainder, IEEE binary64 ties/ulp at normal/subnormal boundaries, exact physical 0.64 ULP gate and refusal on wider/ambiguous enclosure. Verify no source/operation-order approximation silently displaces Level-P physical target. Challenge bogus node/geometry/source/analysis changes, provenance/sha trust, id collisions, unknown components and anything that makes a T1-specific shortcut masquerade as generic physics. Independently construct at least one *different* supported H1 fact graph and check inventory/values without editing core; distinguish this from independent locked *post-freeze* authorability qualification. Examine report's truthful false native/certificate flags, the continued legacy seven failures, and no direct production runner/simulation imports.

Read source AGENTS.md, H1_OFFLINE_AMENDMENT, N1 REFERENCE-CONTRACT and central PROTOCOL/RISK POLICY. Do not redo accepted N3 external-approval DESIGN or unchanged N2 comparator. If a defect is found, preserve reviewer first attempt and propose a new source regression/correction; only re-review affected part.

**Reviewer publication:** write exactly one NEW independent report to `physicsvigilante/review_sandbox/projects/sim_heat/pr-65/reviews/review-01-chat-b.md` on central main. Verdict SCOPED PASS/CHANGES REQUESTED/INSUFFICIENT EVIDENCE pinned to current HEAD. Reviewer reports own performed tests separately from hosted logs.

**STOP:** No OMC install/version query/build/launch, no native-reference/certificate claim, no C1 history rewrite, no reference promotion, no PR65/64/63/62/60/59 merge or deployment. Seven old static physical 100x refusals, eight native blockers and original UNSEALED private scorer remain.
