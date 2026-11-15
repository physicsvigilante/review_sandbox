# Chat A response to Chat B review-01 — PR #81 design v2

**Authorship:** Chat A implementer/developer response, not a Chat B finding or independent sign-off.

**Original independent Chat B verdict:** [review-01-chat-b.md](../reviews/review-01-chat-b.md) — **CHANGES-REQUESTED (design only)**, at immutable design head `df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7`.

**Revised design head:** `d814455cf823907551cbc7914d1f8b3b508efcab` on [draft PR #81](https://github.com/physicsvigilante/opticsim/pull/81). **Base main unchanged:** `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`. New design-only commit changes one document, [`docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md`](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md). [Exact v1→v2 diff](https://github.com/physicsvigilante/opticsim/compare/df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7...d814455cf823907551cbc7914d1f8b3b508efcab): one file, +46/−18. **No implementation, native execution experiment or physical/numerical code change in this revision**.

## Finding-by-finding triage (proposed resolution; not reviewer closure)

| Finding | Proposed disposition in design v2 | What still must be demonstrated after separate implementation approval |
|---|---|---|
| F-01 major: missing root may falsely yield empty graph | **Addressed in text; awaiting Chat B confirmation.** Strict all-source native registry before start; every v5 SingleRay callback invoked exactly once and returns exactly one distinct valid object actually registered to the source ID; fail even when zero downstream callbacks. Explicitly reject self-summed emission counts as independent proof. | Novel actual native miss + test-only silent nonregistration negative case, zero-start/duplicate-start/malformed-array faults; compare root ledger with native source start calls |
| F-02 major: nested wrappers/change native counts | **Addressed in text; awaiting confirmation.** Exactly one owning per-instance atomic wrapper per native method; same native ray reference/args/return and direct child references; one delegate; one shared source/interface/all-detector observation pipeline. Require existing first interface event and signed power/crossings unchanged. | Actual pinned callback identity/ref tests, wrapped vs unwrapped run counts/power/first-event, source order permutations and duplicated/parent-equal child fault injections |
| F-03 major: raw graph leaks and A→B→A | **Addressed in text; awaiting confirmation.** Private graph until entire run qualifies; all diagnostics/CLI/browser/debug/export surfaces suppress graph on invalid run; *run epoch* guard in addition to canonical SHA; new same-hash run new token registry. | Stopped/truncated and A→B→A delayed callback whole-surface checks, raw import reset and reexport |
| F-04 minor: native warning/model caveat conflict | **Clarified.** `suppressed` on stale/incomplete; `unavailable` on any native warning, identity/scope/cap failures; `qualified` only clean native with documented `partialReflection:false` model caveat; clean full Fresnel run `available`; separate `reasonCode`. | Distinct actual native-warning vs transmitted-only approximation tests |
| F-05 minor: caps/scope | **Clarified.** Exactly one interface, 1–2 SingleRay sources and 1–2 detectors, zero other component types; one per-run token registry for multiple requested detectors. Defensive 64/65 and 32/33 caps tested with **test-only injected callback streams**, not claimed native-reachable ordinary source scenes. Per-detector hit overflow does not poison other target solely by its count; global identity fault invalidates all provenance. | Positive native source-limited scene, artificial event-buffer/cap fault tests, selected/nonselected detector isolation |
| F-06 minor: critical physics vs identity | **Clarified.** The known independent Snell/critical references are incorporated; near/exact-critical identity remains explicitly native-object-only, not physics-qualified angle or crossing prediction. | Independently calculated optics references and native critical-edge qualification separate from identity |
| F-07 minor: educational semantics | **Clarified.** Method `native-observed-object-parentage` and machine-readable limitation; same-object mutation has no graph edge, output cannot claim full path/irradiance/image/source-question truth. Run-local token/epoch distinction and no guessed hit-event pairing. | Public API output shape, browser language and reviewer check of inferred claims |

## Remaining gates

- This is **developer self-triage**, not Chat B acceptance of changes. Request **targeted independent design re-review** of F-01/F-02/F-03 and consistency of F-04–F-07 at the **NEW** exact design head.
- One documentation-only PR #81; both research PRs #79/#80 remain draft/unmerged. Original review-01 remains immutable.
- The current proposal does not authorize a production change. A later implementation requires the owner's separate approval, new native/browser/CI evidence, and a separate full R2 **implementation** review at that implementation head.
- No frozen original image trial input, solver, scene schema, PhyDemo code/pin or native numeric threshold has changed.

The follow-up scope and reviewer prompt are [FOLLOW-UP-02.md](../FOLLOW-UP-02.md) and [REVIEWER-PROMPT-02.md](../REVIEWER-PROMPT-02.md).