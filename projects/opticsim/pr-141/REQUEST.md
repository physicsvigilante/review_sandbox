# Independent targeted R3 request — Opticsim PR #141 (v19 downstream aperture boundary)

**Review request, not an approval or a builder self-review. Do not merge.**

## Exact source identity

- Target: [draft PR #141](https://github.com/physicsvigilante/opticsim/pull/141), correcting Chat B R2 P1 on [draft PR #129](https://github.com/physicsvigilante/opticsim/pull/129).
- **Review candidate HEAD**: `6d6d6b213fedb6f028cd1ffef241aef239d37c62`.
- **Source Git tree**: `39884a78ec265a77dc18877a838b937103998160`.
- Immediate base/prerequisite: PR #129 HEAD `491229a29257a2cf7e4368372120d087e736a4c7` (PR #129 itself depends on the held research #128; the original review-cleared #127 is frozen).
- **Synthetic main-target source-CI merge**: `4e038a1a1e76f990d461acc41962cdeea0af70e8`. Independently inspect the Git commit objects; its tree was verified by the builder to be exactly `39884a78ec265a77dc18877a838b937103998160` and its parents were main `d3509e82fb65d81aabe336666851f8f2962623f4` and the candidate HEAD. The temporary [CI-only PR #142](https://github.com/physicsvigilante/opticsim/pull/142) has no release/merge authorization.

## Reason for this review

[Chat B's original independent PR #129 report](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-129/reviews/review-01-chat-b.md) gave **CHANGES REQUESTED, one P1**: the lens→aperture refusal used `> BEAM_CLEARANCE_MM` (0.01 mm) for all three positive signed-order comparisons, but existing source/plane clearance can **admit equality** at 0.01 mm. A post-lens aperture could therefore bypass the new fail-closed admission policy; this was a static geometry and code counterexample, not proof that pinned PhyDemo computed wrong ray physics.

Original forward example: horizontal native parallel beam (centre x=0, width40 mm, density0.2), thin converging lens at x=+0.01 (f=100 mm, aperture large enough), downstream finite stop at x=+50 with opening length 17.5035 mm, detector beyond it. Initial sample height ±17.5 mm, after lens the extreme sample reaches ±8.75175 mm at x=50 by thin-lens reference; those are exactly the two inner gap endpoints. Existing initial straight sample guard cannot certify this later corner. A 0.01-mm source→lens gap can be admitted by the old source-plane clearance while bypassing the strict `>0.01` downstream classification.

## Candidate correction

PR #141 changes **only** `src/parallel-beam.js` and `test/jee-v19-review-secondary-routes.test.mjs` versus PR #129:

1. Three signed order comparisons for source→lens→aperture change from `> BEAM_CLEARANCE_MM` to **`>0`**, so physical topology is not confused with clearance thresholds. Independent source-plane, lens-stop separation and aperture endpoint checks remain in place; there are **no new ray calculations, solver patches, measurement transforms or schema fields**.
2. New tests refuse downstream apertures when source-to-lens and lens-to-stop clearances lie at or just around 0.01 mm (0.009, 0.01, 0.011), in 0°, +180° and −180° directions; they assert ordinary aperture-before-lens compositions still prepare. For reverse exact-boundary checks, the source is translated to x=64 and lens to x=63.99: because cos(±180°)=-1 but sin(±180°) is not exactly zero, a zero-centred finite reverse emitter had tiny x offsets that caused a **source-clearance** refusal before the **topology** rule. This was a **test-design issue on the initial CI run**, not a demonstrated new solver issue.
3. Inspect whether the test assertions meaningfully distinguish the intended downstream refusal from an unrelated rejection, especially near the threshold. Request tightened tests if necessary.

## Builder's exact-head CI evidence to inspect, not to assume

11/11 standard GitHub Actions workflows ended **success** on exact candidate HEAD (temporary main-target PR #142; inspect commit/tree identity yourself). Key optical job: [run #44269514330](https://github.com/physicsvigilante/opticsim/actions/runs/44269514330). Its archived job log includes:

- **815 Node tests / 815 pass / 0 fail**, with both new R2 P1 boundary/pre-lens tests passed.
- `JEE_PARALLEL_BEAM_PUBLIC_ACCEPTANCE` — 7/7 cases (4 fully native complete, 1 native incomplete, 2 properly refused).
- `JEE_PARALLEL_BEAM_CHROME` — 11 actual Chrome checks, six screenshots.
- `V19_POST_LENS_STOP_REFUSAL` — forward gaps 17.46/17.50/17.54 refused and both reverse ±180 similarly refused.
- `V19_PRE_LENS_STOP_ALLOWED` — builder-native forward and reverse readings [8 emitted, 6 absorbed, 2 detector crossings].
- `V19_REVIEW_INSIDE_SLAB` and `V19_REVIEW_REVERSE_SLAB` — native completed; `V19_REVIEW_REVERSE_LENS` — 8 focal detector samples for each reverse direction; `V19_REVIEW_NUMERIC_DEPTH` — depth 0 incomplete and observations suppressed.

**Do not call this independent execution**: only builder CI ran Node/PhyDemo/Chrome. Do not use the initial failed test-only HEAD `b1dd1db9bc9906d465336fb4156eeaad0dd8d42c` as acceptance evidence. Its 814/815 result identified the signed-endpoint source-clearance interaction; the current candidate fixes the test geometry and is the only requested source revision.

## Questions for an independent reviewer

1. Is `>0` for strictly downstream signed plane order sufficient to refuse **all otherwise admitted** source→forward-lens→aperture arrangements at both positive and reverse horizontal headings, including exact 0.01-mm clearance and floating-point edge cases? Inspect complete validators, not just the changed if statement.
2. Are truly upstream apertures still admitted and propagated natively without changing valid source/detector geometry? Are near-coincident lens/stop cases already bounded by existing separate clearance guards?
3. Do new tests truly exercise the old escape and avoid false positive refusal caused by a different guard? Independently check small signed distances around 0.01 mm and source endpoint rounding at ±180°.
4. Did the patch affect any other composition, old v1–v13 authoring, physical invariant or native PhyDemo interface?
5. Verify claimed Git tree match and inspect actual CI job logs/artifacts, distinguishing verified builder runs from anything the reviewer independently executes.

Publish `projects/opticsim/pr-141/reviews/review-01-chat-b.md` with exact SHA/tree, P0/P1 findings, physically reasoned counterexamples or lack thereof, evidence limits and verdict **CLEARED FOR OWNER DECISION / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. Do not edit reviewed code, approve as the builder, merge any held branches or claim publication as a user release decision. The held v14–v18 integration and issue #123 branch protection remain separate gates.
