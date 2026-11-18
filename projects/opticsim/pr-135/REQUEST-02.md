# Opticsim PR #135 — independent Chat B R2 review of corrected native B research

**Verdict requested:** CLEARED FOR OWNER DECISION — RESEARCH ONLY / CHANGES REQUESTED / INSUFFICIENT EVIDENCE. **Do not merge** or infer an observer-eye/image/public API.

## Exact source and R1 context

- Original [independent Chat B R1](reviews/review-01-chat-b.md) reviewed HEAD `58001725e8fd97cbfeb00ee9eaff705a864ecae5` (tree `ff0c6e46ea97b650c5e7e58680f180c458a437c1`) and returned **CHANGES REQUESTED**. Its native finite 5 mm crossing and backprojection findings were corroborated, but a **P1 preregistration acceptance gap** remained: no actual equal-index native paired run required by [issue #134](https://github.com/physicsvigilante/opticsim/issues/134). P2: no mixed cross-run component ordering or raw native-warning retention for suppressed readouts. The R1 report stays immutable.
- Corrected **DRAFT / TEST-ONLY** [Opticsim PR #135](https://github.com/physicsvigilante/opticsim/pull/135): HEAD **`d6aff4e388aef982c3fc1b88039d4ac6951b4fca`**; source tree **`afc157ed2976e937dbe9de942b05ffd205e6a083`**; synthetic PR CI merge **`10b8b07e782626eff81f7bdbc5d9ec71ecf8bf44`** with **identical tree** (verify Git commit objects yourself). Base is unchanged production `main` `d3509e82fb65d81aabe336666851f8f2962623f4`.
- Compare: **one added file only**, `test/jee-finite-detector-window-feasibility.test.mjs`, now 559 added lines; no other tracked changes, native pin, production `src/`, browser, schemas, frozen tests or CI scripts.
- R2 change only to this existing research file; preserve original R1 source, reports and native logs. The source is not merged, and no production B observer component exists.

## R1 P1 correction — independently inspect actual PhyDemo results

**New exact-native equal-index tests:** use actual original v5 scene structure with one native single-ray source at (-120,0) mm, one normal x=0 plane, one finite D1 detector center (40,0) mm, 5 mm long, source direction -0.5° and +0.5° in two separate executions. Test **both indices 1.0→1.0 and 1.5→1.5**, with full Fresnel policy explicitly enabled and correct orientation.

Independent scalar prediction for each equal-index case:
- Undeviated outgoing angle = ±0.5°; crossing y = ±(120+40)tan(0.5°) = **±1.39629884652 mm**, safely within real endpoints ±2.5 mm, nearest clearance ≈1.10370115348 mm.
- Native crossing point/direction must be read from opt-in `detector-hit-events`; no Snell result is fed to the solver. There should be one complete native emission and interface transmission per run, one real native detector crossing; inspect native reflection behavior rather than presuming zero.
- Backward extension of **measured outgoing lines only** must yield normal depth **120 mm**, source-side intersection near (-120,0), not ~80 mm. The original 1.5→1 baseline must still back-project to ~79.996192 mm. No eye, pupil, actual simultaneous observation or continuous field can be concluded.

**Builder Node24 log first positive evidence** on final correction: both equal-index configurations recorded native hit heights ±1.396298846521404 mm and derived depth 120.0000000000008 mm, with native reflected counts zero; new tests passed in the early mirror-angular workflow. Independently inspect full final-source logs and CI run identities (do not just accept the numbers in this prompt).

## R1 P2 corrections — prove scope, do not overclaim

- **Cross-run mixed component ordering:** source `[-.5°]` in normal component array order; partner `[+.5°]` in reversed component array order. Their canonical scene hashes should differ but the normalized **entire apparatus + simulation settings**, excluding ONLY emission direction and sorted component order, match. Require 2 genuine native crossings and the same derived source-side geometric depth, not callback-order attribution.
- **Suppressed warning preservation:** `provenance()` now records `rawNativeWarnings` per invocation, separately from `evaluateObservables()` statuses/warnings, and deduplicates each invocation's warnings with its immutable source label and scene SHA. Check warning-bearing **null** results retain both evaluated run records. An injected `SYNTHETIC_RESEARCH_WARNING_PROVENANCE_CONTROL` on an otherwise actual, incomplete native result is explicitly a **synthetic metadata test**, not a genuine warning emitted by PhyDemo; ensure the review and implementation never misrepresent it as physical evidence.
- The earlier completed **qualified native miss** must continue to preserve the two independent native `qualified` statuses and Fresnel-omission warnings. No `qualified→available` promotion, source attribution via native hit callback order, stale run reuse or claimed full ray-lineage.

## Retained existing evidence and validation

- Independent R1 already corroborated true 5 mm finite-window native crossings for 1.5→1, real shifted/shortened detector misses, reverse/rotation/unit controls, TIR/near-critical refusal, incomplete budget suppression, near-parallel/antiparallel withheld intersections and noncertifying numerical perturbation sensitivity. Verify that the amended test still preserves them and adds no assumptions inconsistent with #134.
- Existing research-only conditioning thresholds (line sine 1e-4, 0.05 mm endpoint margin, max backward extension 10× scene scale) are **not validated physics/native error budgets**. A two-line residual of zero is algebraic, not a numerical uncertainty certificate.
- The final implementation is a test file: no public observer-geometry/eye/image API or new browser interface. Pinned native PhyDemo remains `811f508d2b070898c241a568b0c167dcb8645251`. Exact-tree Node24/native/Chrome builder CI and result identities are to be verified. Old PR #133's conditional A is independently reviewed but unmerged, not a dependency.

## Deliverable

Publish **`projects/opticsim/pr-135/reviews/review-02-chat-b.md`** with exact HEAD/tree/synthetic merge identity, independently recalculated equal-index and baseline geometries from actual recorded native events, P1 and P2 disposition, ranked P0–P3 findings, full CI conclusions, and **ONE** research-only verdict. State which actions are actual independent computations versus reviewing builder-CI logs; **never claim independent PhyDemo/Node/Chrome replay unless performed**. If any required check or final CI is incomplete, do not clear research. Do not merge or release.
