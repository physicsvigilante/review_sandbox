# Independent review request #01 — conductor_sim post-M40b audit PR #104

**Author-prepared request, NOT an independent PASS or merge permission.** Use a fresh reviewer context. Review the bounded corrections below, not the entire historical project again. Production stays DRAFT/UNMERGED. Full current-head hosted CI was still completing when this packet was prepared; independently require all applicable exact-head workflow/check runs completed-success before issuing PASS.

## Exact source and scope

Production PR: https://github.com/physicsvigilante/conductor_sim/pull/104

- Literal candidate HEAD: `d35149d89b049a4b3db59ada558145798eff958b`.
- Native Git TREE: `25e91e0fd53749bf6c6c578583310b219e1ecb4f`.
- Released M40b baseline: `4bae2f6be5a1689b9e1dc80d2dd146b77d366a3e`, tree `5ea6098d463eec12fbc184ab3a6fca2f27699e9a`.
- Separate prior audit charter commit: `3852eaf862f88ca7ed87eed792d5d582b0894560`, parent is that released baseline.
- Candidate branch: `audit/post-m40b-corrections`. M40c charter branch must remain untouched.
- Report: `docs/post_m40b_audit.md`; scope: `docs/post_m40b_audit_charter.md`.

Check out the literal candidate, independently assert HEAD and HEAD^{tree}, inspect the full delta and unchanged original PDFs, and recheck the live PR head/state before verdict. The reported 22-file delta includes a byte-identical relocation of the old long README into README-MILESTONE-HISTORY.md, replacement current navigation, a report/charter, additive CI path changes, two regression files and the small source corrections. No independent PASS may silently apply to a changed source.

Original source hashes remain:
- `02_conductors_half_size.pdf`: `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d`
- `POTENTIAL_CONDUCTORS1.pdf`: `8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5`

## Reproduced defects and intended correction

**A1, physical direction error.** Previously a raw direction such as `(ulp(0.0), ulp(0.0), 0)` could become the non-unit vector `(1,1,0)` through a rounded subnormal norm. This affected ConductingPlane, Motion1DSpec axis, motion_2d._unit and visualization.unit. The new private `_directions.unit_direction` rescales components only for a subnormal norm. Ordinary normalization arithmetic and invalid/overflowing-norm refusals remain. Original M40a precision-sensitive near-unit query rays and Decimal surface kernel are NOT changed or routed through this helper.

**A2, incomplete M40b witness.** An externally shortened visible cavity list and corresponding per-face witness lists could pass while authoritative native records still contained the omitted cavity. The new independent checker requires visible cavity count to match authoritative void/Gauss inventory, retaining existing identity and numerical checks. This is not historical/cryptographic authentication of arbitrary JSON or separately edited HTML.

**A3/A4, navigation and CI.** The README/current map/architecture were stale. They now describe released M40b, this correction candidate and charter-only M40c; historical README bytes remain at the root with links intact. Seven newer workflow PR filters gain conservative upstream source/config/reference coverage; no old scientific/browser/FEMM step removed. Twenty regression cases expose the old omissions.

## Required focused reviewer-owned checks

1. Reproduce A1 on the literal unmodified baseline with at least one NEW subnormal signed/oblique direction not merely copied from the developer fixtures. Compare candidate normalization with independently rescaled or high-precision direction ratios. Test an actual grounded-plane real+mirror potential, vector field, force and signed surface density for a translated/rotated unfamiliar signed source arrangement. Expected values must NOT come from the new helper or native image constructor. Confirm correct physical plane location and ordinary-input compatibility, plus zero/nonfinite/overflow refusal.
2. Check that the same geometry contract survives one actual native motion investigation or a physically valid plane/axis construction and one slice world/project roundtrip. Verify unit length, orthogonality and physical metre scale. Test an ordinary direction and a same-ray subnormal encoding. Do not change the physical tolerance to conceal a discrepancy. Existing qualified domains are not widened.
3. Independently construct an authentic M40b atlas and remove an EMPTY cavity and, separately, a CHARGED cavity plus their face witness entries while retaining full authoritative native records. Confirm the baseline checker accepts the demonstrated omission and the corrected checker refuses. Confirm complete unfamiliar one-/multiple-cavity records still pass with unchanged source IDs, raw rays and units. Try duplication/order/Boolean tampering as small additional controls. This is a checker correction, not a new renderer or electrostatic kernel.
4. Inspect the seven workflow path-filter changes and new source-pinned dual-Python audit workflow. Verify each downstream reference/browser consumer is triggered by relevant upstream changes; no green result from a different HEAD substitutes for current-head acceptance. The new workflow intentionally preserves baseline **43 tests / 37 failures / 0 errors** as negative controls and requires candidate **43 tests / 0 failures / 0 errors**. A workflow may succeed because it correctly recognizes expected red baseline controls; do not mislabel the baseline as defect-free. Freshly inspect actual JUnit/logs.
5. Review current README/map/architecture and audit claims against source. Verify old README byte identity and working relative links; M35a/b released, M40b baseline and M40c charter-only labels; no newly solved original JEE question count or 30-case success percentage invented. Sensible composability means qualified reuse, not adding independent responding-conductor solutions or forcing a universal graph. Legacy Boolean/coercion behavior is deliberately left as a documented compatibility migration, not advertised as repaired. The JSON-only checker still cannot authenticate edited external HTML.

Actual developer local evidence: Python 3.13.5 baseline 2,560 passed / 97 FEMM deselected, corrected final 2,603 passed / 97 deselected; 43/43 new tests green. Those are supplemental, NOT hosted Python 3.10/3.12, real FEMM, Chromium or independent-review evidence. Local Chromium was blocked by managed ERR_BLOCKED_BY_ADMINISTRATOR; no browser policy was changed. Hosted applicable checks must finish successfully. Reuse unchanged historical scientific evidence rather than rerunning the whole M40a six-cavity or M40b viewer review; add only targeted checks warranted by these corrections.

## Publication and release control

Publish a reviewer-owned branch/PR in review_sandbox with report `projects/conductor_sim/pr-104/reviews/review-01-chat-b.md`, original independent probes, first-attempt outcomes, exact source/tree, actual numerical values and tolerance, and actual runner artifacts. Preserve failed first attempts and developer red controls. Do not modify production, old reports, PDF hashes or previous release evidence.

Return scoped PASS or CHANGES REQUESTED with reproducible findings. PASS requires unchanged literal production HEAD/TREE and complete-success applicable current-head CI, but is NOT merge permission. Separate explicit owner approval, expected-head guard, reviewed tree equality on main and successful actual postmerge main-push CI remain mandatory. No auto-merge. Do not describe the broad developer audit or green tests as proof that the project has no remaining errors.
