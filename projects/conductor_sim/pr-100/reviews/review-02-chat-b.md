# Independent targeted scientific review #02 — conductor_sim PR #100 M40a B1

**VERDICT: CHANGES REQUESTED.** The original accepted near-unit *radial* off-sphere error is fixed. A narrower **admitted oblique / near-wall input-direction precision defect remains**. This is a reviewer-owned, actually executed numerical finding. No merge authorization.

## Immutable source and review gates

- Production [draft PR #100](https://github.com/physicsvigilante/conductor_sim/pull/100): actual HEAD **e4a64a580cf1a3eca93d4b7315ed1f4aa4ab585e**, actual Git TREE **03eee7d1f4b97d627eb8ccf1a2ff41e837e94ea6**. Independent [first run #44549264045](https://github.com/physicsvigilante/review_sandbox/actions/runs/44549264045) checked out this literal SHA and asserted both HEAD and HEAD^{tree}; both matched.
- Original #01 HEAD **f38fb82f27312f9ea1526c1a65bb93657937a0cb**, tree **0495115a3ad0d38c71f704ae14a8842d466afe55**. Actual Git diff confirms ONLY four modified M40a files: docs/m40a.md, src/conductor_sim/spherical_multicavity.py, tests/test_m40a_spherical_multicavity.py and tools/m40a_spherical_reference.py. No legacy physics, FEMM, Chromium, viewer, PDFs or charter changed.
- Reviewer runner verified frozen SHA256: 02_conductors_half_size.pdf = **9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d**; POTENTIAL_CONDUCTORS1.pdf = **8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5**; M40a charter = **b9da8056206f0c3026edee543712ff7fca070f535e11f95d89eb1beea4e7fdf3**.
- Independent GitHub Actions/check-runs enumeration for corrected HEAD: **24/24 production workflows SUCCESS and 29/29 check runs SUCCESS**, including Python 3.10/3.12, focused M40a, FEMM5 and historical browser/source checks. Developer CI is a prerequisite but cannot replace fresh independent physics.
- Previous [independent #01 / reviewer PR #23](https://github.com/physicsvigilante/review_sandbox/pull/23) remains **CHANGES REQUESTED** and unchanged. Its six-cavity/12-source, signed Gauss integral and 35-refusal positive results are not re-run wholesale or misrepresented.

## Independent physics method

The reviewer [source script](./review-02-chat-b-probes.py) invokes the actual native production code, but it derives mathematical expected densities **independently from the real charge plus Kelvin-image normal electric field**, not from the production closed-form Poisson kernel or bundled oracle.

For a spherical cavity radius a, physical source displacement u, d = |u| and a raw queried normal direction, the reviewer normalizes the **raw binary64-encoded components directly in 105-digit Decimal** to get n. The physical wall is X = a*n. The Kelvin image has q_image = -q*a/d and position u_image = a²*u/d². The independently derived metal-side sigma is

sigma = -(1/(4*pi)) * [q * n·(X-u)/|X-u|³ + q_image * n·(X-u_image)/|X-u_image|³].

This is a separate physical E-normal calculation; the native solution and bundled verifier are not expected-value oracles. The reviewer separately computes the field at the *already rounded native saved canonical vector* only as a diagnostic of where the discrepancy comes from.

### Original B1 radial pole: FIXED

Grounded sphere cavity a = 0.85 m, q = +3.1e-9 C, d = a*(1-1.2e-8).

| Value | Sigma C/m² |
|---|---:|
| Independent analytical Kelvin pole -q(a+d)/(4*pi*a*(a-d)²) | -4742217.655739457 |
| Independent real + image field at raw (1+9e-13,0,0) | -4742217.655739458 |
| Actual native (1,0,0) | -4742217.655739458 |
| Actual native (1+9e-13,0,0) | -4742217.655739458 |

The saved unit normal is [1.0,0.0,0.0], signed SI matches; the genuine export and mathematically correct alternate near-unit normal encoding pass the bundled checker. A forged record carrying the *old off-sphere density* is rejected. Grounded outer sigma = 0.

### Blocking residual B1-R: double normalization changes the queried oblique physical direction

**Code:** [native direction validator](https://github.com/physicsvigilante/conductor_sim/blob/e4a64a580cf1a3eca93d4b7315ed1f4aa4ab585e/src/conductor_sim/spherical_multicavity.py#L65-L82), [density evaluation](https://github.com/physicsvigilante/conductor_sim/blob/e4a64a580cf1a3eca93d4b7315ed1f4aa4ab585e/src/conductor_sim/spherical_multicavity.py#L268-L310), [standalone record checker](https://github.com/physicsvigilante/conductor_sim/blob/e4a64a580cf1a3eca93d4b7315ed1f4aa4ab585e/tools/m40a_spherical_reference.py#L205-L235).

Native accepts length deviation <=1e-12, then first normalizes the admitted raw tuple in ordinary binary64 with component/hypot. The high-precision Decimal density routine receives only that already-rounded direction. At the qualified 1.2e-8 relative source-wall gap, a ~1e-16 tangential rounding shift in an oblique direction ~5e-9 radians away from the source pole produces a 1e-9 **relative** density error. This is not an off-sphere evaluation or wrong force law; it is lost input-direction fidelity before the sensitive high-precision calculation.

**Exact accepted reproducer (grounded, +3.1 nC):**

- a = 0.85 m, source displacement (0.5099999938800001, 0.67999999184, 0) m.
- Let v be ordinary unit-normalization of (0.6+5e-9, 0.8-2.5e-9, 1e-9); pass input n = v*(1+9e-13). The actual raw n is (0.6000000044005399, 0.79999999670072, 9.999999990008999e-10), norm 1.0000000000009, therefore admitted.
- Native saves and samples (0.6000000043999999, 0.7999999967, 9.99999999e-10), a subtly different physical direction.

| Physical raw direction scenario | Actual native sigma C/m² | Independent raw-direction Kelvin-field sigma C/m² | Relative error |
|---|---:|---:|---:|
| Oblique XY, +3.1 nC grounded | -3532142.2752839886 | -3532142.26790142 | **2.0901107e-9** |
| Same geometry, -2.4 nC isolated metal +1.1 nC | +2734561.761510185 | +2734561.7557946476 | **2.0901109e-9** |
| Genuine 3D radial (0.48,-0.64,0.6), +3.1 nC grounded | -4242770.356589729 | -4242770.360599676 | **9.4512473e-10** |
| Same genuine 3D geometry, -2.4 nC isolated metal +1.1 nC | +3284725.43735979 | +3284725.440464265 | **9.4512475e-10** |

**All four exceed the unchanged 2e-10 independent tolerance.** Native agrees exactly with an independent field computation at the *rounded saved normal*. This isolates the defect to early floating-point direction rounding, rather than incorrect Kelvin mathematics or source charges.

The bundled JSON checker accepts the self-consistent native canonical-normal exports, but in **all four cases rejects a record carrying the same accepted raw near-unit direction and the independent high-precision physically correct density at that direction**, raising “independent surface density disagrees with independent Kelvin image field.” Its current normalization verifies the *rounded* direction rather than the input's exact encoded orientation. If the contract intentionally defines a rounded canonical direction rather than the direction supplied, that limitation and its near-wall error must be explicitly qualified; the existing strict raw-direction fidelity cannot be presumed.

## Focused positive and negative outcomes

- **15/15 actual refusals PASS**: arbitrary norm 1+2e-12, zero, nonfinite and Boolean normals; source on or inside excluded clearance; signed-sigma reversal and false zero; units and provenance tampering; unqualified tiny/huge charges; falsely near-cancelled density. No dangerous permissive expansion was found.
- Two actual native positive controls passed separate Kelvin-field and real JSON checks: near-center displacement 1e-250 m gives sigma -2.202836582586787e-10 C/m²; ordinary displacement 0.17 m gives -2.7080690570342197e-10 versus independent -2.7080690570342207e-10.
- Grounded outer sigma = 0. Isolated metal +1.1 nC with cavity source -2.4 nC gives uniform outer sigma **-1.1494523667747998e-11 C/m²**, correct signed Gauss result.
- Scientific claims remain bounded: one connected ideal metal, disjoint spherical cavities, identified teacher-authored static point charges, separate grounded/isolated hypotheses and **conditional local surface sigma only**. No general 3D E/V, source force, ground current, irregular-cavity solution, or newly solved original JEE PDF question.

## Actual first-attempt evidence

- [Reviewer's source-pinned Actions run #44549264045](https://github.com/physicsvigilante/review_sandbox/actions/runs/44549264045): exact native HEAD/TREE, four-file correction, frozen hash and installation steps **PASS**; actual first mathematical/native step **FAIL by reviewer scientific assertion**; evidence hashing and artifact upload **PASS**. This is NOT infrastructure failure and must remain red.
- [Original first-attempt artifact #14542860269](https://github.com/physicsvigilante/review_sandbox/actions/runs/44549264045/artifacts/14542860269) retains the first-attempt log, independent structured results JSON, Git identity/diff/hash logs and reviewer source SHA256 **633e2ab94bd8ea26bf9a598246154093a68563d4f2ca3e936bb5405c6ba4a881**.
- **11 science case records, 15 correctly refused attacks, 8 linked scientific assertions** (four physical-direction discrepancies and four corresponding correctly-valued raw-direction evidence refusals). The runner continued to collect all results and exited intentionally nonzero.
- Original first review and red evidence remain unchanged; do not suppress, rerun-to-green or widen the 2e-10 mathematical tolerance.

## Required bounded corrective action

1. Preserve the successful radial projection and 90-digit near-wall theorem. Avoid destroying tangential information by **premature binary64 normalization** of admitted near-unit oblique inputs; define and consistently represent the same physical-wall direction in native evaluation and saved independent evidence.
2. If a double-precision canonical unit-vector field cannot certify every admitted 1.2e-8 wall-gap raw direction to the existing tolerance, **reject genuinely ill-conditioned direction queries explicitly** or extend the trustworthy source/evidence representation. Do not quietly label a materially changed orientation as the supplied physical direction.
3. Add exactly these source/normal/charge/grounding regressions, correctly valued raw-direction JSON acceptance and forged-density refusal while keeping invalid normals and too-near-wall sources refused. Do not change older physics or solve irregular JEE problems.
4. Preserve #01 and #02 first-attempt evidence. Pin a corrected production HEAD/TREE, obtain actual all-green source CI, request another **fresh narrowly targeted** independent review, and then separately seek explicit owner merge authorization. PR #100 stays **DRAFT/UNMERGED**; no auto-merge.

**Bottom line:** the original B1 radial blocker is corrected, but a physically meaningful near-wall oblique input-direction precision issue remains. **CHANGES REQUESTED**; no broad M40a architecture reopening.
