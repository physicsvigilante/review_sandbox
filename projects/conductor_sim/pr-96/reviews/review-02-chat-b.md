# Independent focused correction review #02 — conductor_sim PR #96 (M39a)

**Verdict: PASS for the bounded numerical-integrity correction F-01/F-02/F-03. NOT authorization to merge.**

## Immutable source identity and prerequisite production gates

- Production PR: https://github.com/physicsvigilante/conductor_sim/pull/96
- Literal corrected production HEAD: 8d235eab5bf14bebf191e15771d296878a151a23
- Native Git TREE: 820ab1e35aee40a30eb45e9b32157416dfd59642
- Predecessor independently reviewed HEAD: 1a11bd03d51645bcc7994ab0ec50a553dd47dc7a, TREE 1295380ec4b4c97cb3a8c99aeea1bdb3c8102122
- The GitHub Actions API confirmed all **24 exact-corrected-commit production workflow runs SUCCESS**, including full Python, real FEMM, browser/source, historical and dedicated M39a. Developer CI is only prerequisite evidence. The corrected M39a developer run: https://github.com/physicsvigilante/conductor_sim/actions/runs/44491580782
- Independently executed literal-SHA checkout asserted HEAD and TREE using git rev-parse. Git diff predecessor..corrected HEAD contained **exactly four modified files**: src/conductor_sim/cavity_gauss.py, tools/m39a_gauss_reference.py, tests/test_m39a_cavity_gauss.py, docs/m39a.md. PDF, charter, FEMM, and browser source remained unchanged.
- Original source PDF hashes revalidated unchanged against review #01: 02_conductors_half_size.pdf SHA256 9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d; POTENTIAL_CONDUCTORS1.pdf SHA256 8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5.

## Reviewer-owned independent evidence

- Probe source: projects/conductor_sim/pr-96/reviews/review-02-chat-b-probes.py
- CI workflow: .github/workflows/pr96-m39a-independent-chat-b-02.yml
- **FINAL PASS**: https://github.com/physicsvigilante/review_sandbox/actions/runs/44494282327
- Final run: **76/76 native M39a regressions** on Python 3.12, genuine isolated and grounded teacher-export/checker CLI, and **21/21 reviewer-authored adversarial probes**. All steps passed. The reviewer independently computed expected charge totals with Python stdlib Fraction from the admitted binary64 source values. Production solver and actual standalone CLI were used only as systems under test. Artifacts include JSON, actual CLI acceptance/refusal outputs, source SHA and tree, logs and content hashes.
- **PRESERVED FIRST ATTEMPT FAIL**: https://github.com/physicsvigilante/review_sandbox/actions/runs/44494039186 . It passed 20/21 probes, including ALL corrected F-01/F-02/F-03 probes, and 76/76 native regressions. The sole failed SIX_CAVITY_ISOLATED reviewer assertion compared legitimate two-stage binary64 rounding (global source total, then metal-plus-rounded-total) against an inapplicable one-stage exact rational sum: -7.500000000000009e-10 versus -7.500000000000008e-10 C, a one-ULP difference. Only the reviewer-owned six-cavity expected arithmetic was corrected to use the true public rounding boundaries. This was a **review harness defect, not a production defect**. No production code was edited and no original red evidence was overwritten. The full scoped job was rerun once.

## F-01 — PASS: strong cancellation, order invariance, native and standalone integrity

Grounded one-cavity sources: large +1e150 C, residual +1e-9 C, negative -1e150 C. Independent exact Fraction arithmetic proved the total equals the admitted binary64 +1e-9 C and entire induced inner-face charge is -1e-9 C. Three opposite source orders all passed actual native solution, exported record, standalone checker and standalone CLI, with exact named source IDs preserved.

The three named sources were also placed in separate cavities in the orders P/R/N and N/P/R. Original-source global aggregation retained the small residual in both arrangements despite enormous opposite cavity totals. Isolated net metal charges of 0 C and +0.25 C gave the correct total outer-face charge and Gauss flux with permittivity 1 F/m, preserving source/cavity IDs. A truly canceling +1e150,-1e150 pair remained exact zero. No residual was fabricated or destroyed by ordering.

**Finding F-01 corrected** for all independently exercised orderings and across-cavity cancellation cases.

## F-02 — PASS: strict nonzero flux underflow, true zero and overflow

One sealed empty cavity, isolated metal charge +1e-300 C, homogeneous epsilon 1e100 F/m mathematically has nonzero exterior flux around +1e-400 V*m, below binary64 representation. Native solve raised **UnsupportedProblem** with explicit underflow rather than exporting 0.0. Negative charge -1e-300 C was independently refused as well.

A correctly shaped forged record with that same physical charge and epsilon but saved 0 exterior flux was rejected by the checker function and the **actual standalone CLI** for numerical underflow. A genuinely grounded nonzero signed-source case correctly retained mathematically exact zero exterior flux. True isolated cancellation also remained accepted. A representable tiny nonzero flux around 1e-200 V*m passed native and CLI, and intentionally overflowing flux was refused by the native solver.

**Finding F-02 corrected**, without confusing zero with underflow, overflow, or a representable small nonzero.

## F-03 — PASS: subnormal signed zero and sign integrity plus positive tolerance control

One empty cavity, epsilon 1.0 F/m, isolated metal charge +5e-324 C, the smallest positive binary64, produced genuine positive nonzero outer charge and Gauss flux, both accepted by native solution, checker and actual CLI. Repeated for charge -5e-324 C and corresponding negative outputs.

For each polarity the reviewer separately replaced **outer_face_total_charge_c** and **exterior_electric_flux_v_m** with numeric 0.0 while retaining genuine inputs and other values. All four forged records were refused for forged zero by both checker and CLI. Individually reversing the sign of each saved field was also refused. For a normal-scale signed-cavity assembly, a saved outer-charge variation of **one ULP** was still admitted, demonstrating that appropriate rounding tolerance remained available.

**Finding F-03 corrected** for both saved numeric fields and polarities.

## Unchanged positive controls and trust-boundary verification — PASS

Reused the ten named sources over six independent authored cavities from reviewer #01, in nC: North (+7,-2), West (-4,+1), Neutral (+6,-6), Empty, South (-8,+1.5), East (+2,+0.5). Independent Fraction arithmetic checked all cavity signed enclosed charges and induced inner-face totals. Total enclosed is approximately -2 nC, isolated metal +1.25 nC yields about -0.75 nC on the outer face, and grounded outer charge/flux are exactly zero. Actual CLI and native checks passed both cases.

Boolean versus numeric-zero injection and duplicate/multiply-assigned source IDs were rejected. Native forged cavity-face identity contradictions were rejected. An externally rewritten, entirely self-consistent record with distinct swapped IDs remains acceptable to an **unanchored** numerical consistency checker; comparing IDs with an independently trusted original manifest detected the rewrite. This limitation is correct and is **not** cryptographic authentication or a numeric-integrity failure.

Native calls for local E(x), local V(x), sigma(x), source force, and ground-wire current all raised UnsupportedProblem. Geometry, source position and time evolution remain expressly unverified. The model provides conditional entire-face Gauss totals under a teacher-declared, bounded connected ideal metal with 1–8 truly sealed disjoint cavities, no exterior sources/fields and positive homogeneous permittivity. It does not verify spatial containment, a local 3D field/density map, or any newly solved original JEE PDF item.

## Disposition and release conditions

**PASS — no remaining blocker was reproduced within correction-review #02 scope.** This targeted review intentionally does not repeat unrelated legacy FEMM or Chromium execution whose source blobs did not change; these passed production exact-head CI. The predecessor CHANGES REQUESTED report and its 35/38 run remain preserved at https://github.com/physicsvigilante/review_sandbox/pull/18 and https://github.com/physicsvigilante/review_sandbox/actions/runs/44489870114 .

Production PR #96 must remain **DRAFT AND UNMERGED** until separate explicit owner permission. This PASS does **not** grant merge permission. Before any independently authorized merge, recheck production PR HEAD, use expected-head protection, verify the merged tree, and inspect actual successful post-merge main-push CI. No auto-merge.
