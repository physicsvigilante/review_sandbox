# Opticsim — risk-based review and integration policy (18 November 2026)

**Goal:** preserve independent physics/evidence safety gates while avoiding unnecessary reviewer cycles, duplicate full reviews and an ever-growing stack of unmerged experimental branches.

## General rule: build evidence before asking for independent review

The builder develops the full bounded feature, writes requirements and testable safety invariants, performs **adversarial preflight** across positive, negative and deliberately contradictory native evidence, and obtains exact-source CI before handing a single frozen commit to Chat B. The reviewer independently inspects code, physics, provenance and relevant CI artifacts. Green builder CI is not independent validation. If a P0/P1 is found, the builder uses a new child source and obtains a **focused** independent review of the correction with regression evidence; the previous verdict remains frozen. Do not request a new review for every partial implementation or routine test fixture adjustment. Historical source SHAs, Git trees, original reviews and release holds must never be rewritten.

## Risk categories

| Class | Examples | Verification and review |
|---|---|---|
| **Critical — independent required** | New native optical capability; new analytical physics or geometric inverse; any change to native-result meaning, observation qualification, admission/refusal boundaries, numerical stability and safety-critical authoring; general optical composition | Builder adversarial/property controls, full relevant CI, exact-tree identity; independent review at **final frozen candidate**; release/integration review after dependency combination |
| **High — independent review of combined source, not every commit** | Composing previously independently reviewed but unmerged capabilities, changing physics-facing public contracts, source ancestry/observer/detector semantics | One consolidated exact-head independent integration review after preparing the complete merge candidate, dependency audit and full suite; record what earlier reviewed code is unchanged |
| **Routine — builder verification generally sufficient** | Docs/typos, labels that do not change claims, ordinary tests with no change to safety/physics semantics, mechanical refactors with no behavioral changes | Scoped tests and diff checks. No separate Chat B review unless changing evidence provenance, failure policy, test oracle correctness or a release safety claim |
| **Infrastructure — separate from physics** | CI runner lacks Chrome, transient external downloads, artifact upload failure | Retry same exact source run, preserve original attempt and provenance; do not change physics or request independent physical review just for a proven runner failure |

No PR may be merged merely because its source review says **CLEARED FOR OWNER DECISION**. A **separate owner authorization** and any required integration/security/branch-protection gates remain necessary. Outstanding branch-protection issue #123 must not be represented as resolved.

## Mandatory builder preflight checklist for critical features

1. **Physical model and exact scope:** coordinate frame and signed normals, indices and side/order, source/detector geometry, ideal-model limits, Fresnel settings, phase/power exclusions, ray parentage and what is **not** measured. Compare a separate analytical reference to actual pinned native data, never steer the native ray with the expected path.
2. **Native outcome matrix:** complete with one/many/zero events, available measured zero, missing/out-of-order first event, real native transmission/reflection/TIR, partial reflection enabled/disabled, detector miss/hit/endpoint/overflow, native truncation/stopped/undefined/warnings, stale scene hashes, contradictory/missing counters and event branches.
3. **Numerical adversarial matrix:** both signs of tangent displacement, source/observer side reversal, normal rotations 0/90/180, translation/units, distances exactly at 0.01-mm bounds, large world offsets, near-axial, ingress/egress grazing, near-critical/TIR, nonfinite/out-of-bounds, and explicitly withheld uncertainty where needed. Verify the *rounded authored direction* separately from mathematical root solvability when claiming observed arrival.
4. **Safety and preservation:** unknown physics **refuses**; canonical schema remains pinned and backward compatible; legitimate positive cases remain; failed native runs never promote analytical predictions to native evidence; finite detector crossings are sampled observations, not an image/eye/continuous illumination; evidence storage hash is freshness, not authentication.
5. **Real native vs test-injected evidence:** separately label native pinned-PhyDemo runs and deliberately mutated complete summaries used to test the result classifier. Never present a synthetic zero, synthetic missing branch, or predicted interface crossing as a measured native event.
6. **Full builder CI, exact identity:** confirm source Git HEAD/tree and synthetic CI merge Git tree equivalence, relevant Node/PhyDemo/real-browser coverage and workflow statuses; preserve failure attempts and follow-up retries on same source. Resolve failed tests before independent review (unless failure itself is the research subject).
7. **Review packet:** one minimal exact-HEAD diff, accepted/refused scope, adversarial evidence matrix, known limits/uncertainties and concrete reviewer questions. Reviewer independently checks failures (rather than merely restating positive CI). Do not ask Chat B to repeat earlier exact-HEAD reviews of unchanged source.

## Integration instead of unbounded feature accumulation

Before starting new JEE optics categories, inventory reviewed but unmerged branches, identify exact dependencies, preserve independent reviews and test-only research boundaries, and assemble **one minimal final integration candidate** on the agreed production base. Prefer integration and release-readiness over opening more small experimental PRs. Run full CI on the combined exact Git tree and request **one independent integration review** for cross-feature interactions, overlap and safety boundary changes. Do not merge a chain automatically; owner decision remains explicit. Avoid presenting test-only probes as public features.

## Status transparency

Maintain four separate judgments: **interpretation fidelity**, **physical/model correctness**, **native execution/evidence completeness**, and **educational usefulness**. A correct textbook-style analytical value is not a native hit or an observed image. A measured zero is data, not absence of data, and says nothing about continuous visibility. An incomplete or stale native run cannot qualify. Record P0/P1 issues with immutable source SHA/tree and exact failure counterexamples, and resolve them before critical features advance.

This process document is a review-coordination instruction, not independent evidence or an authority to weaken future reviewer judgment or bypass branch protection.
