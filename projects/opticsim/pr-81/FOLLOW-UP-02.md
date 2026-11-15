# PR #81 targeted design follow-up — R2 review-02

This is a **targeted re-review of revised proposal wording only**, not a new independent implementation review and not a repeated broad project audit. The first Chat B [report](reviews/review-01-chat-b.md) at head `df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7` is immutable and accurately records **CHANGES-REQUESTED**.

## Freeze

- Source [draft PR #81](https://github.com/physicsvigilante/opticsim/pull/81); production base `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`.
- **New exact revised head for review:** `d814455cf823907551cbc7914d1f8b3b508efcab`.
- The *only* changed file since first review is `docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md` (+46/−18). [Pinned revised design](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md), [specific v1→v2 diff](https://github.com/physicsvigilante/opticsim/compare/df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7...d814455cf823907551cbc7914d1f8b3b508efcab).
- [Chat A point-by-point response](responses/response-01-chat-a.md) is an attributed developer proposal, **not proof** of closure.
- [Original PR #81 CI (v1 head)](https://github.com/physicsvigilante/opticsim/actions/runs/43730335002) was 11/11 workflows green; current updated-head CI must be checked separately. Neither tests unimplemented provenance.

## Targeted questions

1. **F-01 (major):** Does the new all-source native callback registration/invocation/returned-ray/WeakMap-identity ledger reject a missing root even on a **true no-hit** scene with zero downstream incident callbacks? Can any source legitimately return zero/multiple rays within this exact SingleRay authoring scope? What proof/test would falsify the ledger?
2. **F-02 (major):** Is the proposed *one owning callback wrapper per native method* and same object/return/args/once delegation coherent with current `observeSourceSet`, `observeInterfaceSet`, `observeDetectorSet` semantics? What new counterexample remains?
3. **F-03 (major):** Is no-raw-evidence-publication on any invalid attempt and a private **run epoch plus SHA** adequate against A→B→A delayed callbacks? Must the proposal clarify how accepted graph is projected to the existing `execution.summary` without temporary leaks?
4. Confirm the revised status priority, per-target detector/global cap isolation, 0-other-component allowlist and injected-only cap guards (F-04/F-05); near-critical separation of source identity from numeric optics (F-06); machine-readable limitations (F-07). Flag any remaining material contradictions or unintended scope expansion.

**No new feature exists to run.** A conceptual design re-review can identify design defects without running native code; do not claim to have executed tests. Avoid a full new project review unless this amendment creates an unforeseen evidence/physical scope change. Remain honest about missing implementation tests. Keep PR #81 draft/unmerged.

## Reviewer output

Write **your own** new append-only report to:

`projects/opticsim/pr-81/reviews/review-02-chat-b.md`

Use the central [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md) and preserve original first report. Verdict must be explicitly **design-only**: `pass`, `changes-requested`, or `insufficient-evidence`. If the exact head moved, mark it stale. Do not merge or commit to source PR. A design `pass` is *not* implementation sign-off or owner authorization.