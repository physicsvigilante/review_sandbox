# Chat B independent targeted R3 review — Opticsim PR #141

**Verdict: CLEARED FOR OWNER DECISION.** Review date: 2026-11-18. **P0: none identified. P1: none remaining in the reviewed boundary correction.** Nonblocking test-hardening notes below. This is an independent source, numerical-geometry and archived-CI review, **not** independent PhyDemo/Node/Chrome execution, release approval or permission to merge.

## Exact identities and scope

- Reviewed [draft PR #141](https://github.com/physicsvigilante/opticsim/pull/141), **HEAD `6d6d6b213fedb6f028cd1ffef241aef239d37c62`**, **Git tree `39884a78ec265a77dc18877a838b937103998160`**.
- Compared against frozen PR #129 HEAD `491229a29257a2cf7e4368372120d087e736a4c7` (tree `07ff1ea9a8ff5660520ae6d37389b895d49fb163`). GitHub comparison reports exactly three descendant commits and exactly two changed files: `src/parallel-beam.js` (6 insertions/3 deletions) and `test/jee-v19-review-secondary-routes.test.mjs` (45 insertions).
- Independently fetched Git **commit objects**, rather than trusting CI status alone: the PR #141 HEAD points to tree `39884a78ec265a77dc18877a838b937103998160`. PR #142's synthetic merge `4e038a1a1e76f990d461acc41962cdeea0af70e8` points to **the identical tree**, with parents `d3509e82fb65d81aabe336666851f8f2962623f4` (main) and the reviewed `6d6d6b2...` HEAD. PR #142 is now closed **without merging**.
- The earlier [PR #129 R2 review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-129/reviews/review-01-chat-b.md) remains a historically correct **CHANGES REQUESTED** verdict for that **different** SHA/tree. This R3 only addresses its P1 via a child patch.

## P1 resolution — independent reasoning

**Finding: resolved for the admitted v19 lens profile.** The old downstream refusal used three signed order comparisons of the form `signedDistance > 0.01`. Yet source-to-lens `outsidePlane` admits equality (`<= lensX - 0.01` or `>= lensX + 0.01` on the entire emitter), and the lens-to-stop guard rejects only `abs(lensX-stopX) < 0.01`. Thus a genuinely forward lens/stop with exactly 0.01 mm separation could pass the independent clearance policy while failing the old downstream classification.

The new code at `src/parallel-beam.js:100-103` uses **strict `> 0`** for:
1. `(lens.x - source.x) * direction.x`;
2. `(stop.x - source.x) * direction.x`;
3. `(stop.x - lens.x) * direction.x`.

The validator permits only heading `0`, `180`, or `-180` in its lens model (`src/parallel-beam.js:75-79`); in these cases `direction.x` is +1 or -1. Therefore every actually admitted source → forward lens → downstream aperture has positive signed separations and triggers the unconditional downstream refusal before aperture-specific geometry/clearance checks. The profile has at most one ideal lens and one finite aperture; there is no secondary-lens order ambiguity. The 0.01-mm tolerance is still applied separately to physical clearance, not reused as a topological threshold.

The independently recomputed forward counterexample uses Beam x=0, width=40 mm, density=0.2, lens x=+0.01 mm with f=100 mm and sufficient aperture, stop x=+50 mm with openingLength=17.5035 mm, detector x=+100 mm. The outer emitted sample at y=17.5 mm would reach `17.5 × (1 - 49.99/100) = 8.75175 mm` at the stop under the thin-lens reference, exactly half the opening. The initial straight-sample corner check does not address this post-lens encounter. The **old** topology condition is false at the 0.01-mm source/lens boundary; the **new** condition is true and refuses before native propagation. This establishes the policy fix, not an independent assertion about PhyDemo's exact-corner collision convention.

### Binary64 / reverse heading checks

I independently evaluated the relevant formulas with V8/JavaScript binary64 arithmetic, using the patch's actual fixture geometry, **without running the project tests or native solver**:

| Heading and boundary | Clearance/order outcome |
| --- | --- |
| 0°; source x=0, lens x=0.009/0.010/0.011 | 0.009 source clearance refuses; 0.010 clearance admits and new downstream rule refuses (old rule misses); 0.011 downstream rule refuses |
| +180° and -180°; source x=64, lens x=64−0.009/0.010/0.011 | Same admission/refusal structure; for the 0.010 authored gap signed double-precision separation is approximately 0.00999999999999801, still **positive**, so new rule catches it while old `>0.01` misses it |
| 0°, ±180°; source 100 mm behind lens, stop 0.009/0.010/0.011 mm beyond lens | All positive signed lens-to-stop orders cause the new refusal before the independent lens-stop guard |
| True stop between source and lens | Signed stop-to-lens separation is negative; the new downstream predicate remains false and the ordinary pre-lens geometry is not misclassified |

At source x=0 and ±180°, `Math.sin(±Math.PI)` leaves emitter endpoint x-offsets of approximately ±2.4493e−15 mm (width 40), which can conservatively fail an **inclusive** 0.01-mm source-plane guard. Translating to source x=64 rounds both endpoints to x=64 and allows the source-clearance fixture to reach the intended new rule. This is not an aperture admission bypass: the original unshifted geometry is rejected, rather than allowed. Authoring coordinates are bounded to ±10000 mm, far from a floating-point spacing that would reverse the sign of any admissible ≥0.01-mm separation.

## Test quality and preservation

- At `test/jee-v19-review-secondary-routes.test.mjs:150-179`, **0.010 mm source/lens** (all three headings) and **0.009/0.010/0.011 mm lens/stop** assertions use the specific phrase `downstream of a forward ideal lens`, so a generic clearance error would **not** satisfy them. The 0.009/0.011 source/lens loop, in contrast, uses a broad regular expression including `UNSUPPORTED_SCOPE`; that part could pass for an unrelated validation failure.
- At test lines 181-190, a true **upstream** aperture is asserted to prepare at all three headings. The already existing native pre-lens test at lines 193-217 checks completed behavior, with 8 emitted / 6 absorbed / 2 crossings forward and reverse.
- For the lens-stop fixture at reverse 180° with lens x=64 and stop x=63.99, actual binary64 `abs(lensX-stopX)` is slightly **below** 0.01. The new error is specifically the topology error because that guard runs first, but the **old** code would also have been able to reject this fixture through the separate clearance rule. A tighter reverse equality test should choose e.g. lens x=0, stop x=−0.01, source x=+100, with a distant detector; this makes `abs(lensX-stopX) === 0.01` in binary64 and isolates the historical bypass. The forward x=0→0.01 fixture already tests an admitted equality.
- The code diff does not change native PhyDemo, adapter, optical ray propagation, detector observables, schema, clearance constants, or legacy component/profile definitions. The only production modification is the v19 downstream ordering gate; v1–v13 selection/validation still lives in separate registered contracts. The unchanged native pre-lens, slab and reverse controls provide supporting builder evidence.

## GitHub Actions provenance (verified, not independently rerun)

Queried the repository's Actions runs filtered to reviewed HEAD `6d6d6b2...`: **11 distinct completed workflows, 11 successful** on 2026-11-18. Inspected actual optical composition run [#44269514330](https://github.com/physicsvigilante/opticsim/actions/runs/44269514330), job **134682306888** and its archived log. Its checkout log explicitly fetches `4e038a1a1e76f990d461acc41962cdeea0af70e8:refs/remotes/pull/142/merge` (not merely an assumed HEAD equivalence). Key log records:

- **815 Node tests / 815 passes / 0 failures**, including both new `R2 P1` named test cases.
- `JEE_PARALLEL_BEAM_PUBLIC_ACCEPTANCE`: 7 cases, 4 native completed, 1 incomplete, 2 refused.
- `JEE_PARALLEL_BEAM_CHROME PASS: 11 checks, 6 screenshots`.
- `V19_POST_LENS_STOP_REFUSAL`: the three 17.46/17.50/17.54 mm post-lens opening configurations and both reverse headings refused.
- `V19_PRE_LENS_STOP_ALLOWED`: both orientations [8 emitted, 6 absorbed, 2 detector crossings].
- `V19_REVIEW_INSIDE_SLAB`: completed [8 emitted, 0 first-plane, 8 second-plane, 8 detector crossings]; `V19_REVIEW_REVERSE_SLAB`: completed [8,8,8,8]; `V19_REVIEW_REVERSE_LENS`: each ±180° direction completed with 8 focal detector samples.
- `V19_REVIEW_NUMERIC_DEPTH`: explicit maximum ray depth 0 incomplete, three measurements suppressed.

Verified that workflow artifacts including `browser-acceptance-evidence`, `hosted-browser-evidence` and the static demo were uploaded. **I did not separately open the PNG screenshots or independently run Node, PhyDemo or Chrome.** The initial red intermediate child `b1dd1db9bc9906d465336fb4156eeaad0dd8d42c` is not treated as acceptance evidence.

## Severity, recommendations and release disposition

- **P0: none identified.**
- **P1: none remaining in this specific boundary correction.** The original P1 counterexample is now fail-closed by independent signed-order reasoning and a targeted exact-boundary test. This is not a claim that all v19 optical physics is independently requalified.
- **N1 (nonblocking test hardening):** Split the 0.009 and 0.011 mm source/lens assertions. Check a *specific source-clearance error* below 0.01, and a *specific downstream-topology error* above 0.01. Avoid catchall `UNSUPPORTED_SCOPE` in the positive-boundary branch.
- **N2 (nonblocking regression precision):** Add a reverse exactly-equal lens/stop fixture with binary64-representable 0.01-mm distance that otherwise satisfies the separate clearance guard (e.g. lens 0, stop −0.01, source +100, detector sufficiently beyond). The present shifted reverse fixture tests the new guard but does not independently prove that the **old** clearance policy would admit this exact lens-stop equality.
- **N3 (scope/release note):** Keep universal post-lens aperture refusal conservative until any separate validated secondary-corner qualification. A subsequent release still requires the owner's decision, integration review for held v14–v18, and resolution of branch-protection issue #123.

**Final verdict: CLEARED FOR OWNER DECISION** for PR #141 at exactly HEAD `6d6d6b213fedb6f028cd1ffef241aef239d37c62` / tree `39884a78ec265a77dc18877a838b937103998160`, with N1–N3 recorded as nonblocking. This does **not** override the frozen PR #129 R2 decision or authorize merges/releases. No Opticsim source changes, historical review edits, branch mutations or PR merges were performed by this reviewer.
