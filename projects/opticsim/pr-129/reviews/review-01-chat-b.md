# Chat B independent targeted review — Opticsim PR #129

**Verdict: CHANGES REQUESTED (P1 boundary bypass).** Reviewed 2026-11-18. No source changes or PR merges performed.

## Exact identity / review scope

- Correction PR #129: draft/unmerged, HEAD `491229a29257a2cf7e4368372120d087e736a4c7`, Git tree `07ff1ea9a8ff5660520ae6d37389b895d49fb163`.
- Its research dependency PR #128 is HEAD `1b712dc00a0e49b0bc320b86b62f0c1d4bb94120`; current PR #129 base is `research/jee-v19-reverse-medium-corner-probe` at that SHA.
- Synthetic CI merge `51f4fea5ab18f1b4f784c110f7292d197f96b28c` was independently checked via GitHub Git commit objects: tree is exactly `07ff1ea9a8ff5660520ae6d37389b895d49fb163`, identical to correction HEAD. Merge parents include corrected HEAD.
- Inspected all three patches versus PR #128: `src/parallel-beam.js`, `test/jee-v19-review-secondary-routes.test.mjs`, `docs/NATIVE-PARALLEL-BEAM-V19.md`. No changes in this diff to native PhyDemo, adapter, observables, schema, historical files or the frozen PR #127 review.

## Independent optical and signed-coordinate reasoning

A width-40 mm, density-0.2 canonical Beam emits eight midpoint samples at world-y `±17.5, ±12.5, ±7.5, ±2.5` mm. A source at x=-100, forward +x through a thin f=100 mm lens at x=0 reaches lens height y0 and, in the thin-lens ideal model, has subsequent `y(x)=y0(1-x/100)`. Hence at x=50 the extreme pair reaches `y=±8.75` mm, coinciding exactly with the inner endpoints of a centred 17.50 mm aperture. The pre-lens straight-ray corner test instead compares ±17.5 against ±8.75 and does not catch this collision. A 17.46 mm gap gives corner coordinates ±8.73 (the outer samples fall on opaque arms), whereas a 17.54 mm gap gives ±8.77 (the pair passes inside gap); the original builder-native report of 2/6 versus 0/8 is physically consistent. This shows an admission-policy hole, **not** wrong PhyDemo reflection/refraction.

For an exactly horizontal source direction, direction.x is +1 at 0° and -1 at either +180° or -180° within floating-point rounding. Signed plane order `(planeX-sourceX)*direction.x` correctly reverses forward-vs-behind for right-origin sources. The correction adds the right *kind* of guard (source → lens → aperture without tracing a substitute ray), but its threshold is inconsistent with existing admitted source clearance.

## P1 blocker — exact 0.01 mm forward-plane boundary escapes the new refusal

The newly added refusal in `src/parallel-beam.js` is a conjunction of **three strict** comparisons:

```js
(lens.x-source.x)*direction.x > 0.01 &&
(stop.x-source.x)*direction.x > 0.01 &&
(stop.x-lens.x)*direction.x > 0.01
```

Yet the existing `outsidePlane` admits the whole source segment **at** 0.01 mm, not only strictly beyond it (`endpoint.x <= planeX - 0.01` or the opposite). The lens-to-aperture guard rejects `abs(lensX-stopX) < 0.01`, likewise allowing equality. Thus a physically forward lens 0.01 mm from the source is *admitted* by the old source clearance but does **not** satisfy the new strict `>0.01` gate, regardless of how far the aperture is beyond it.

Concrete independent geometry for a targeted regression: a horizontal Beam centered at (0,0), width 40, density .2; ideal f100 lens plane x=.01, with sufficiently tall native aperture; centred finite aperture at x=50, openingLength `17.5035` mm; detector beyond x=50. The initial extreme sample starts y=17.5, crosses lens at x=.01, and ideally reaches `17.5 * (1-(50-.01)/100) = 8.75175` mm at the aperture, precisely its inner gap corner `17.5035/2=8.75175`. The initial straight sample is nearly 8.75 mm from that corner, so the old initial-sample guard does not exclude it. At x=.01 the existing source/lens clearance permits equality while the new forward lens test is false. This is a static code/geometry counterexample; I have **not** executed it in native PhyDemo. It is sufficient to invalidate the claimed universal post-lens refusal and requires correction.

**Required correction:** classify strictly forward *topological ordering* using positive signed plane differences (or an explicitly consistent tolerance rule which also refuses every admitted downstream configuration), rather than using `> BEAM_CLEARANCE_MM` for the three order predicates while other validators allow equality. Add regression for source-to-lens exactly 0.01 mm with downstream aperture, lens-to-stop exactly 0.01 mm where admissible, and values just below/above boundaries; cover 0° and both ±180° (avoiding fragile absolute-equality assertions where cosine is rounded). Confirm no legitimate upstream stop is inadvertently rejected. This fix will require a **new HEAD and fresh exact-head CI and review**, not amendment of this frozen decision by description alone.

## What the current corrected HEAD does successfully

- In ordinary well-separated source → lens → stop layouts the new refusal is appropriately fail-closed, based only on authored planes; it does not prescribe or alter native rays. The three checked 17.46/17.50/17.54 gaps are rejected; reverse x-direction +180° and -180° analogous far-separated cases are rejected.
- Before-lens stop remains admitted and actual builder-native output is `[emitted=8,absorbed=6,detector crossings=2]` for both forward and reverse arrangements.
- Canonical source beginning inside slab gave native completed with 8 emitted, zero first-plane, 8 second-plane events and 8 detector crossings. Reverse source outside slab gave completed with 8 encounters per plane and 8 detector crossings. Both ±180° reverse lenses gave completed with 8 focal detector samples at x=-100.
- Deliberately canonical `maxRayDepth=0` produced native `incomplete` and three suppressed observations, as required; the revised docs distinguish it from public default 8.
- No evidence in this three-file change of old v1–v13 optical versions becoming permissive, or of native solver replacement. Composition model dispatch continues to limit the Beam to the dedicated v19 model families. The unmerged earlier review of PR #127 remains frozen.

## CI/archival evidence actually inspected

Inspected GitHub Actions `44140095830` actual job log `134240224413`: Node 24 `813 tests / 813 pass / 0 fail`; `JEE_PARALLEL_BEAM_PUBLIC_ACCEPTANCE` reports 7 cases (4 completed native, one incomplete, two refused); `JEE_PARALLEL_BEAM_CHROME PASS: 11 checks, 6 screenshots`. Verified log records `V19_POST_LENS_STOP_REFUSAL`, `V19_PRE_LENS_STOP_ALLOWED`, `V19_REVIEW_INSIDE_SLAB`, `V19_REVIEW_REVERSE_SLAB`, `V19_REVIEW_REVERSE_LENS`, `V19_REVIEW_NUMERIC_DEPTH` and their stated counts. Queried the GitHub Actions run list by the exact HEAD: **11 distinct completed workflows, all successful**. These demonstrate builder execution, but do not cover the newly identified 0.01-mm escape.

**Independence limits:** I independently inspected the linked source, the Git object/tree identities, the GitHub CI job log, and recomputed thin-lens/corner and signed-plane geometry. I did **not** rerun pinned PhyDemo, Node tests or real Chrome in a separate environment. The 7/7 and 11/11 browser claims are verified against CI logs, not independent re-execution or visual re-inspection of PNG bytes in this review. Research #128's exact-corner native absorptions were inspected through its preserved record and prior review request, not reproduced on #129 (which is supposed to refuse them).

## Severity and release disposition

- **P0:** none identified.
- **P1 blocker:** post-lens aperture remains admissible at a supported 0.01 mm source/lens boundary; fix guard and expand boundary regressions.
- **N1 nonblocking:** conservative refusal restricts useful downstream aperture arrangements; only widen after independent secondary-corner qualification.
- **N2 nonblocking release gate:** v14–v18 are separately held; a combined future source tree needs fresh integration checks, archived-regression preservation, and owner authorization.
- **N3 nonblocking numerical limit:** 0.01 mm is an admission tolerance, not a universal binary64 guarantee for secondary native encounters. Keep incomplete/undefined measurement suppression.

**Final verdict: CHANGES REQUESTED.** This verdict concerns only PR #129 at the exact SHA/tree above. Do not merge #129, #128, the previously cleared #127, or any held PR. A corrected descendant requires independent exact-head review before an owner decision.
