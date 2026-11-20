# EMFEELD PR #61 — independent focused follow-up review-02 (Chat B)

**VERDICT: PASS — scoped strictly to the two findings F1/F2 on corrected HEAD.** Review-01 remains **CHANGES REQUESTED** on its *old* reviewed commit and is not retrospectively converted into a PASS. This is not whole-engine, classroom, human Windows GUI, or postmerge certification.

**Immutable reviewed source:** feature HEAD **76edda620213710e80860c3ee8abe312228b6c10**; Git tree **047eca847cfc6bacfc3afebd51cf912a2f9deb18**. Previous reviewed HEAD d7151a35ecddace3f79786315fb4f07858e398cc, old tree 9886308b8a036eb65ca8e37dc86ef173c6e91e12. Base/main d2f90afbf6c8910c410c41147925e311320f96b0 unchanged. [Production PR #61](https://github.com/physicsvigilante/emfeeld/pull/61) was independently confirmed on **2026-11-20** as **open, DRAFT, UNMERGED**, at exactly this corrected head/base. **No merge performed.**

## Independent source/evidence/CI gates

- Verified all **10/10** outer-kit manifest SHA-256 entries. Original corrected hosted source ZIP **5e7c23c341891e33e6ad28157a722b79b64af9c2bfe74c0d704f7c6c96ee7f09**; original wire ZIP **fe8f58380aff5928678c1acffa34df38db44cc26cb0d9013095f3ed5419259d1**. Both ZIPs CRC clean.
- Both original archives embed byte-identical **tested-source.tar**, SHA-256 **5c3d55e810946aa22ce97ec779cc053d4b409702deecc28ec118614dd1ebe7ce**. Extracted source, freshly indexed **452 tracked files**, and reconstructed Git tree with Git write-tree: **047eca847cfc6bacfc3afebd51cf912a2f9deb18**. Reviewer tests below ran on that extracted source; no production file changed.
- GitHub commit comparison: **one new commit, exactly six changed feature paths** (wire_magnetism.py, wire_view.py, two wire test files, qualify_wire.py, WIRE_MAGNETISM_V1.md). Not a broad rewrite.
- Queried corrected-head Actions directly: **9/9 completed SUCCESS**, including wire **44616482262**, source **44616482180**, real PyVista, Gauss, capacitor, cavity, dipole, Three.js and release-candidate **44616482245**. The last has **two distinct completed SUCCESS jobs**: Ubuntu 24.04 / Python 3.13.5 (135886429861) and Windows 2022 / Python 3.13.5 (135886430571). The commit combined-status endpoint showed no additional statuses. These are **developer CI**, not reviewer-owned tests. The builder's attempted local full suite timed out near 33% and is **not** counted as a local full-suite pass.
- Independently re-audited **seven original hosted native scenes** and all **49/49** per-file SHA-256 receipts; original/current authored inputs, code hashes, SI positions, B fields, positive tangents, arc weights and independently recalculated signed circulation match. Those archived screenshots are *not* my fresh native evidence.

## F1 — previously missing visible positive Ampère traversal arrow: RESOLVED

Reviewed native view's new positive_ampere_circulation_arrow, renderer-neutral immutable tangent data and unchanged magnetic-field/line-integral data. The **BLUE** VTK actor has a real arrow mesh and an explicit legend distinguishing **fixed + Ampère circulation** from **GREEN B direction**. It is computed from adjacent physical positive loop tangents, not current sign, field-arrow vectors or schematic glyph length. The .40 display-unit arrow geometry does not enter SI circulation.

**Fresh reviewer-authored challenge**, not a copy of the shipped test: tilted wire origin **(-2.3, 3.7, -1.1) m**, axis **(2.5, -1.2, 3.8)**, radius **0.37 m**, **97** loop samples, initial **+13.25 A**. Independently checked **e1 × e2 = u**; each tangent equals **u × radial_unit**; SI B was recomputed from **mu0 * I/(2*pi) * (u × rho)/|rho|²**; the signed integral was separately recalculated using **Σ(B · tangent * physical_arc_weight)**, not rendered arrows or normalized-to-target output.

The real **PyVista 0.48.4 / VTK 9.6.2** viewer opened **vtkEGLRenderWindow**, **vtkGenericRenderWindowInteractor**, **vtkOpenGLCamera**. Dispatched genuine VTK **KeyPressEvent** for **N (reverse), 4 (zero), 0 (reset)**. In all four states, verified actual named VTK actor/mapper with **101 blue mesh points**, visible property, exact blue RGB from **#2374b9**, arrow vertex projections from origin to **+.40** along the positive physical tangent, and no meaningful blue direction/geometry change (float tolerance 5e-14). Its approximately fixed direction: **(-0.6329543435174132, -0.753324273317383, 0.17852545547701934)**.

Actual **green** VTK mesh counts: **13 positive**, **13 negative**, **0 zero**, **13 reset**. Each real mapper's projected arrow length is .42 in its signed SI-derived B direction; green direction reverses under negative I. The unchanged blue traversal arrow persists through zero. Independent signed SI circulations are **+1.6650441061827497e-5**, **−1.6650441061827504e-5**, **0**, **+1.6650441061827497e-5 T m**, consistent with **mu0 I**. A guard raising on physical prepare() confirmed that camera rotation and V hide/reveal did not recompute physics.

**Fresh reviewer-owned source-bound screenshots**, all genuine 1050×700 PNGs; visually inspected the negative and zero captures. PNG SHA-256:

| State | I (A) | Reviewer PNG SHA-256 |
|---|---:|---|
| positive | +13.25 | 18a37872a0f6fe0de991dd6437d170b08df7028d373e1c1468dd04a687605b98 |
| negative | −13.25 | 8d00a675d7bf58f1996b166e79d62d9b0a334297c0e78efcb0902b8685bb7f07 |
| zero | 0 | c9479e08114a3e8668f6bf8646313d9c61ddc9d90bcf03445642b09a781c3f70 |
| reset | +13.25 | e04c55ad2b4c66f1409dff316452706439c87a64e79589cb13d1936aa38bc0a4 |

Every new snapshot has **7/7 verified SHA receipts**, distinct original/current state, authored-input hash, physical SI samples, exact source code SHA-256 and renderer metadata. The evidence bundle **PR61_R2_Independent_Review_Evidence.zip** is attached in the originating ChatGPT review conversation (not currently uploaded into review_sandbox). It contains reviewer_checks.py, logs, all four original reviewer-native captures (PNG + JSON/NPZ/receipts), native-summary.json and hosted-audit script/result. These are **not** the seven developer-hosted images. No human desktop mouse or manual Windows GUI claim.

## F2 — raw mixed-Boolean direct-Python probe acceptance: RESOLVED

Reviewed the new **_contains_raw_bool** preflight in src/emfeeld/wire_magnetism.py, which precedes NumPy conversion. Independent tests reject **[True,0,0]**, **[1.0,False,0.0]**, nested list/tuple probes, Python/NumPy booleans, pure Boolean ndarrays and mixed object ndarrays for **zero, +5 and −11 A**. Real int/float lists, tuples, integer/float ndarrays and batched numeric probes still compute. Authored JSON Boolean and nonzero on-axis singular refusals remain intact. An integer ndarray *already pre-coerced by an external caller* cannot expose its original Boolean provenance and is not an achievable requirement.

## Execution, first failures and limits

- Reviewer-owned **51 PASS**, with **-W error**: **27** raw Boolean refusal cases; **21** genuine numeric probe cases; authored-JSON/singularity check; physical handedness/immutable tangent/field check; and genuine VTK current/actor/screenshot event test.
- Separately replayed shipped feature tests from this exact source: **108 PASS**, -W error, across tests/test_wire_magnetism.py, tests/test_wire_presentation.py and viewer_tests/test_wire_runtime.py. Do not add overlapping CI and local test counts.
- **First independent test attempt: 50 passed, 1 harness failure**. The reviewer's first assertion wrongly demanded *bitwise* array equality between separately normalized 3D tangents after redraw; ordinary last-bit floating rounding differed although the physical tangent/actor direction was invariant. Corrected **only reviewer test** to a strict 5e-14 numeric tolerance; first log preserved.
- **Second attempt: 50 passed, 1 reviewer harness/output-path failure**. A previous attempt had already created a screenshot directory; production protect_saved_evidence appropriately rejected overwriting it. Reran to a fresh **native_final/** destination with **51 PASS**, no production edit. Both failure transcripts retained alongside final transcript.

## Decision

**PASS, only for F1/F2 at corrected HEAD 76edda620213710e80860c3ee8abe312228b6c10.** The distinct blue positive traversal marker is real, correct, visible and current-invariant; green B glyphs reverse/vanish correctly; physical SI circulation remains computed from B · tangent · arc-weight; mixed raw Boolean Python probes now refuse before numeric upcasting. **No open blocker within this narrow correction.**

**Historical review-01 remains CHANGES REQUESTED on its original SHA**. This verdict does not claim general Biot–Savart, finite-wire effects, classroom learning benefit, human Windows GUI acceptance, or re-review unchanged electrostatic/gravitational lessons. Leave **PR #61 DRAFT/UNMERGED** until owner-directed guarded merge; separately run actual-main CI and artifact qualification after any later merge. Reviewer did not merge or alter production source.