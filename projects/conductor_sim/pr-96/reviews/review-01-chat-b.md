# Independent review 01 — conductor_sim PR 96 (M39a exact multicavity Gauss ledger)

**Verdict: CHANGES REQUESTED — numerical-integrity blockers. No merge authorization.**

This is a reviewer-owned, read-only review of production. The source PR remains DRAFT/UNMERGED. No changes were made to conductor_sim, its historical PDFs, its prior viewers or FEMM physics. The review scripts/workflow and this report belong only to review_sandbox.

## Source identity and boundaries

- **Production PR:** https://github.com/physicsvigilante/conductor_sim/pull/96
- **Literal reviewed HEAD:** 1a11bd03d51645bcc7994ab0ec50a553dd47dc7a
- **Native Git TREE:** 1295380ec4b4c97cb3a8c99aeea1bdb3c8102122
- **Base main:** 0dc25ca686fd84891bc0d9291111ee48c4de3a9d
- **Last source-head recheck:** PR 96 still pointed to the literal reviewed SHA, DRAFT, open, not merged.
- **Scope:** git diff verified *exactly seven added files and no modifications or deletions* from the released base. The new files are the M39a charter, design document, solver, reference checker, example, tests, and focused workflow.
- **Original source PDF hashes, recorded by the independent run:** workbook 9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d; notes 8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5.

The pre-existing frozen audit (docs/m36a_jee30_coverage.json) still marks workbook p11 Linked Q28 and notes p70 three nonconcentric cavity Illustration 9 as **unsupported** for local irregular cavity fields/surface densities. This review inspected the frozen audit, charter and unchanged PDF identities; it did **not** independently view/render the PDF page images. The model adds **zero** newly solved original JEE workbook items. All novel charge values below are independently teacher-authored.

## Actual reviewer execution and preserved first attempts

Reviewer-created reproducible test source:

- Probe script: projects/conductor_sim/pr-96/reviews/review-01-chat-b-probes.py
- Workflow: .github/workflows/pr96-m39a-independent-chat-b.yml
- **Final comprehensive independent run:** https://github.com/physicsvigilante/review_sandbox/actions/runs/44489870114
- **First full native adversarial run:** https://github.com/physicsvigilante/review_sandbox/actions/runs/44489408552
- **Extended numeric adversarial run:** https://github.com/physicsvigilante/review_sandbox/actions/runs/44489689003
- Earlier reviewer harness-first-attempt traces, also retained: https://github.com/physicsvigilante/review_sandbox/actions/runs/44489007008 (shallow checkout lacked release-base object) and https://github.com/physicsvigilante/review_sandbox/actions/runs/44489194790 (external reviewer script lacked the source checkout on PYTHONPATH). Those two runs failed before physical probes. Corrections were made **only** to the reviewer-owned workflow; the failed logs were not overwritten.

The comprehensive GitHub Actions job checked out the **literal production commit**, asserted HEAD and native TREE, verified the entire seven-added-files diff, ran the production package install and **72/72 actual focused Python 3.12 regressions**, executed the genuine three-cavity example CLI, executed its standalone checker on both generated JSONs, and ran **38 independent novel/adversarial probes** with distinct teacher-authored values and an independently implemented high-precision Decimal calculation. **35/38 probes passed; 3 reproduced material numerical-integrity violations.** All three errors appear in the first-attempt review log and saved artifacts in the full run, not as deductions from developer green CI.

All 22 distinct developer workflow runs checked for this pinned source head had status completed/success, including the prior Python, browser/source, true FEMM and new focused M39a regression; those developer passes are necessary but were **not** counted as independent reviewer pass evidence.

## Independent physical model and positive results

A new six-cavity, one-connected-metal topology used exactly ten named point sources. Expected source totals and inner-face induced totals (all values below in nC) were derived from the reviewer's immutable own charge inventory, not from the production solver:

| Cavity | Sources | Enclosed q | Entire inner face Q |
| --- | --- | ---: | ---: |
| North | +7, −2 | +5 | −5 |
| West | −4, +1 | −3 | +3 |
| Neutral | +6, −6 | 0 | 0 |
| Empty | none | 0 | 0 |
| South | −8, +1.5 | −6.5 | +6.5 |
| East | +2, +0.5 | +2.5 | −2.5 |
| **Total** | ten sources | **−2** | **+2** |

For **isolated** metal with independently authored Q_metal=+1.25 nC, the native solver produced Q_outer=−0.75 nC and exterior flux −84.70568005297643 V·m at epsilon0=8.8541878128e−12 F/m, agreeing with the reviewer arithmetic. A **separate grounded static assembly** gave Q_metal=+2 nC, Q_outer=0, flux=0, and exterior-field-zero uniqueness flag true. The source and cavity inventories remained intact.

Positive independent probes also verified source/cavity order permutations, moving one source ID to a different authored cavity while preserving the parent by dataclasses.replace, an empty cavity distinct from a nonempty signed cancellation cavity, Boolean charge/flux refusals, duplicate identities, false JEE provenance and false geometry/time flags, wrong units, forged normal-scale face/outer charges, wrong native face identities, overflowing source totals, overflowing exterior flux, and informative unsupported errors for potential_at, electric_field_at, surface_charge_density_at, force_on_source, ground_wire_current. These positive results support the conditional integral Gauss theorem **but not** an arbitrary-geometry local E(x), V(x), sigma(x), FEMM or time-current capability.

## Finding F-01 — BLOCKER: valid source-order permutation fails the standalone Decimal checker

**Location:** tools/m39a_gauss_reference.py, check_gauss_record; per-cavity and global sums use sum(..., Decimal(0)) without raising the default Decimal precision of 28, even though the flux division uses a 70-digit localcontext.

**Independent exact native reproducer:** one sealed Stress cavity with ordered named charges:

~~~python
CavityCharge("large", 1e150)
CavityCharge("residual", 1e-9)
CavityCharge("negative", -1e150)
~~~

The finite, admitted native Gauss solver computes enclosed +1e−9 C and entire inner-face −1e−9 C, with a valid grounded external zero-field theorem and serializable, native-validated JSON. The standalone checker rounds its first two Decimal operands to 1e150 before subtracting 1e150, infers an **incorrect expected zero**, and raises:

> ValueError: independent cavity enclosed charge differs from exact zero Gauss-law integral

Changing only the source ordering to large, negative, residual makes the exact same charge inventory pass both native solver and reference checker. This is an independently reproduced **false rejection of a valid case** and violates the mandated source-order invariance in the finite admitted domain.

**Required correction:** use genuinely exact/order-invariant accumulation of all parsed SI charges at **both cavity and whole-conductor levels** (e.g. stdlib Fraction from saved finite decimal strings, or a guaranteed sufficient high-precision Decimal context spanning the entire accepted IEEE range). Preserve the independent implementation (no production physics imports), then test both source permutations, global cancellation across cavities, and extremes near admitted overflow/underflow. Do not weaken equality to mask incorrect expected zeros.

## Finding F-02 — BLOCKER: native admitted finite inputs silently underflow exterior flux to zero

**Location:** src/conductor_sim/cavity_gauss.py, solve_cavity_gauss: exterior flux is computed with float division; the guard rejects only nonfinite/overflow, not nonzero exact quantities rounded to zero.

**Independent native reproducer:**

~~~python
GaussCavityAssembly(
    "TinyMetal",
    (SealedCavity("Void"),),
    FixedNetCharge(1e-300),
    1e100,  # homogeneous positive permittivity in F/m
)
~~~

All input fields are finite and currently admitted. The exact exterior flux is **1e−400 V·m**, strictly positive. The production solver returns **0.0**, and native export succeeds. The standalone checker also treats float(expected) == 0 as an expected exact zero, so it does not detect this lost quantity.

**Required correction:** either explicitly refuse numerical underflow (distinguishing true theorem zero from a nonzero result below float range) with a clear UnsupportedProblem, or define and enforce a narrower physically/numerically qualified parameter domain *before* arithmetic. Preserve exact-grounded-zero and true signed-source-cancellation cases. Do not export a rounded underflow as an exact conditional Gauss zero.

## Finding F-03 — BLOCKER: forged zero outer charge passes standalone validation for an accepted finite subnormal

**Location:** tools/m39a_gauss_reference.py, _same: tolerance 64*ulp(abs(expected_float)) can exceed the magnitude of a nonzero subnormal expected total. The isclose comparison then accepts 0.0 in its place.

**Independent native/JSON reproducer:** isolated metal, one empty cavity, fixed metal charge **5e−324 C** (minimum positive binary64), permittivity **1.0 F/m**. An authentic exported native record has nonzero outer charge and flux, and the checker accepts that record. Edit *only* the saved JSON outer_face_total_charge_c from the nonzero value to **0.0**, keeping the original metal input, face totals and flux; the standalone checker **also accepts this forged record**. The native in-process ledger integrity is a separate trust boundary; this finding concerns the explicit standalone JSON mathematical-integrity promise.

**Required correction:** enforce zero/nonzero and sign invariants before tolerant nonzero comparisons. Also bound admissible subnormals and absolute tolerances so 64 ULPs cannot cover a nonzero expected result all the way to zero. Add a normal-scale control verifying the existing tolerant floating-point rounding behavior remains accepted.

## Identity-swap trust-boundary clarification (not treated as a fourth numerical blocker)

A standalone JSON record whose two *distinct valid source IDs* are swapped across cavities without changing charges or totals remains self-consistent and is accepted by the JSON checker. The reviewer-owned input manifest detects the identity change by comparing against its anchored expected IDs. The frozen charter explicitly disclaims cryptographic authentication of self-consistent externally re-authored JSON, so the model cannot infer historical source identity from the record alone. The reviewer prompt asks for unconditional saved-ID-swap rejection at the native/checker boundary; **that stronger demand is not attainable without a trusted external identity anchor**. Resolve this wording conflict explicitly, or introduce an external authenticated manifest/digest if that demand really is required. Native cached face-ID contradiction and duplicate/multiply assigned ID attacks already reject as intended.

## Scientific scope and merge gate

The physical Gauss integral formulas and grounding uniqueness theorem are consistent with the frozen charter *conditional on truly sealed, disjoint cavities and the declared no-exterior-fields domain*. All source membership is **authored**, never geometrically proved. There are no new verified JEE answers and no local 3D fields/surface density. The code is additive and legacy production geometry/FEMM/browser blobs are unchanged.

**Verdict: CHANGES REQUESTED**, due to F-01, F-02, F-03. Do not merge; PR 96 must remain draft/unmerged. Request a focused production correction to the checker arithmetic/zero guard and the native SI underflow admission boundary, preserving these first-attempt red transcripts. Re-review only changed boundaries and these established positive controls; requalify the corrected exact HEAD/TREE and the necessary CI, then require separate explicit owner merge approval and full postmerge main-push CI. This independent review itself does **not** authorize merge.
