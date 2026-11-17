# Opticsim PR #132 — independent design review request

**Requested verdict:** CLEARED FOR OWNER DECISION / CHANGES REQUESTED / INSUFFICIENT EVIDENCE.
**Do not merge anything. Do not imply that a design review is a production physics audit or runtime execution.**

## Exact source identity and audited surface

- **Draft [Opticsim PR #132](https://github.com/physicsvigilante/opticsim/pull/132)** — design only, open/unmerged.
- Production base commit: `d3509e82fb65d81aabe336666851f8f2962623f4`
- Design source HEAD: `07dcf1d6ed0c094071d2d5347ab14baa2bd35c04`
- Source tree: `0917d9d70a01ae107b08bb0a031524cc32df3a07`
- Synthetic CI merge: `ab6f82ef377a31f9e1649c12a4678936a78b186c`; tree **also `0917d9d70a01ae107b08bb0a031524cc32df3a07`** (checked against Git commit objects).
- Sole changed file: [`docs/jee-apparent-depth-observer-contract-v1.md`](https://github.com/physicsvigilante/opticsim/blob/07dcf1d6ed0c094071d2d5347ab14baa2bd35c04/docs/jee-apparent-depth-observer-contract-v1.md), 140 added lines; no `src/`, schema, tests, vendor pin, existing optics, viewer or workflow change.
- Underlying independently reviewed [PR #131 research evidence](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-131/reviews/review-01-chat-b.md) covered the separate test-only HEAD `aa36f2ce10f148e404d5534e4000f53adc62f9b5` and did not authorize production.

## Review questions — independently assess each

1. **Scope/meaning:** Does candidate A make a useful JEE near-normal **conditional analytical** apparent-depth capability without inventing observer position, native rays, global image point, scene schema v20, or optical coverage? Does the proposed fact request have sufficient required fields without silently introducing a viewing direction or other hidden assumptions? Should A be narrower or modified?
2. **Math:** Independently derive `d_a=d n_v/n_o` and the symmetric-pair finite-angle expression `d_s(i)=d_a sqrt(1-(n_o/n_v sin i)^2)/cos i`, the `i→0` limit and monotonic envelope versus `sin² i`, including `n_o=n_v`, `n_o<n_v`, `n_o>n_v`. Recompute 120 mm, 1.5→1, i_max=5° and 30° controls. Distinguish object-medium incidence from observer-medium direction, TIR, near-critical sensitivity and a geometric symmetric-pair envelope from actual uncertainty or an observer image.
3. **Output semantics:** Is A's `status:'available'` safe if `method:'conditional-analytical-paraxial'`, `qualification.basis:'assumption-dependent'`, explicit limitations and `native.status:'not-run'` are always retained? Are absent-cone `symmetricAngleEnvelope:null` and rejection of missing assumptions sufficient? Would a `conditional` status be safer for the real dispatcher?
4. **Follow-on native B:** Does actual finite native detector-window selection (not PR #131's huge research detector) properly bound the claim? Audit first/second run scene compatibility, complete native branch evidence, one path per run, source/observer-side orientation, Fresnel policy, true backward intersection and inability to infer unique physical imaging or eye visibility. Identify hidden path/lineage assumptions.
5. **P1 status propagation:** Check B's lattice for incomplete/suppressed/unavailable/qualified/available, retained per-run warnings and hashes. Check for accidental `qualified → available` promotion, data loss from stale/async evaluations, or falsely inferred source identity.
6. **Numerics:** Identify fragile cases beyond near-parallel (antiparallel, near grazing/critical, huge translation/extrapolation, near-equivalent indices) and whether the proposed sensitivity and truncation checks suffice as a design plan. The test harness's fixed `1e-6` thresholds are not an error certificate.
7. **Architecture and governance:** The proposal must not create or silently migrate a v20 scene or collide with held v14–v19. Confirm no new code touched, branch and CI-tree identity, dependence on the already supported v5 contract, and separation from held #129 aperture safety and main protection #123. A new implementation must require its own source review and release decision.

## Evidence scope

Inspect independently the design diff, linked exact-source PR #131 reviewer report, one native log as needed, and existing `src/problem-workflow.js`, `src/planar-angle-queries.js`, `src/observables.js` for registry/result compatibility. No native rerun is required for this **design-only** review; if you do not rerun PhyDemo or Chrome, explicitly state that fact. Passing historical CI is not a correctness certification for this unimplemented API.

## Deliverable

Publish `projects/opticsim/pr-132/reviews/review-01-chat-b.md` with exact source HEAD/tree, independent derivation, ranked P0–P3 findings, required changes, evidence limits, and **one** verdict. Preserve the reviewed PR #131 report and all held sources unchanged. State explicitly that clearance, if granted, is **design clearance only**, not implementation approval, merge authorization, a physical-image result, or release.
