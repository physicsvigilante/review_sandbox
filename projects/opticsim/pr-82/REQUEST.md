# PR #82 — independent Chat B R2 implementation/code and physical-evidence review

**State: DRAFT independent review request; actual final-head CI status must be confirmed before verdict.** This is **R2 actual code/evidence verification**, NOT another PR #81 design review, a held-out interpretation test, or permission to merge.

## Frozen source identity

- Project: `opticsim`, source repository https://github.com/physicsvigilante/opticsim
- **Implementation source PR:** [draft PR #82](https://github.com/physicsvigilante/opticsim/pull/82).
- **Exact implementation head to review:** `7c62043f1e1e3c3056a409f831ece5f8016e78cf`.
- **Exact current production base:** `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`.
- [Base→implementation diff](https://github.com/physicsvigilante/opticsim/compare/00e6211d6d40c0db8c62910f9e57b910b6aeb6f5...7c62043f1e1e3c3056a409f831ece5f8016e78cf).
- **Approved *design* head:** `d814455cf823907551cbc7914d1f8b3b508efcab` in **separate, unmerged docs PR #81**, [Chat B independent design-only PASS](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-81/reviews/review-02-chat-b.md), dated 2026-11-15.
- Pinned native PhyDemo: `811f508d2b070898c241a568b0c167dcb8645251`, Node `24.19.0`. No upstream change, new ray tracer, physical schema/angle budget modification, original problem-answer solver, or deployment permitted.
- Source [feature documentation](https://github.com/physicsvigilante/opticsim/blob/7c62043f1e1e3c3056a409f831ece5f8016e78cf/docs/NATIVE-RAY-PROVENANCE.md); full source [AGENTS.md](https://github.com/physicsvigilante/opticsim/blob/7c62043f1e1e3c3056a409f831ece5f8016e78cf/AGENTS.md).

## Requested behavior and hard boundaries

Opt-in `detector-ray-provenance` only for existing schema-v5 `planar-media-tracing` with **exactly one native planar interface**, **1–2 real explicit `SingleRay` sources**, **1–2 native passive detectors**, and **zero other components**. Only actual `onSimulationStart.newRays` emitted references and actual `onRayIncident.newRays` *distinct direct-child objects* are associated through per-run `WeakMap` identity. In-place primary ray mutation (including TIR) adds **no** parent edge; `rayIndex` is not a semantic identity. Output for a selected detector is the transitive **observed parent graph of its actually crossed ray objects**, not a physical path, continuous illumination, image, full source interpretation or irradiance measurement. No default/no-opt-in result changes. Native signed detector power remains relative and separate.

**Hard refusal:** source callback or handler ID/native-instance installation loss (including a real detector hit lost by software observation), wrong/missing/duplicate source or child objects, observed-count mismatch, stale native epoch/source SHA, absent parent, native warning/truncation/undefined/stop, unsupported scene, >64 distinct object identities/run, >32 hits/selected detector. Never emit partial `nodes`/`crossings` in raw diagnostics or qualified exports on invalid runs. A legitimate sampled miss is available empty **only** with full source/observer coverage. Two selected detectors share one run-local token ledger but have isolated hit-list caps. The browser's Session/QualifiedUI guards prevent A→B→A stale result publication.

## Review targets and mandatory adversarial checks

**Source paths to inspect:** `src/ray-provenance.js` (private tracker and closeout), `src/adapter.js` (exactly-one source/detector callback and raw-result projection), `src/planar-media.js` (native interface child observation), `skills/sim-ro-image-to-scene/scripts/check-scene.mjs`, `scripts/author-scene.mjs`, `src/native-observations.js`, `src/observables.js`, `src/app.js`, `src/qualified-ui.js` and `src/result-preview.js`. Verify the unchanged pinned native source, including `SingleRay`, `PlaneGlass/BaseGlass`, `Detector`, and `Simulator`. Verify `test/ray-provenance.test.mjs`, `scripts/ray-provenance-acceptance.mjs`, `scripts/ray-provenance-browser.mjs`, `.github/workflows/unified-workflow.yml`.

1. **True zero-hit vs missing root, even when the ray never interacts:** a complete source start is necessary to publish `{"nodes":[],"crossings":[]}`. Challenge source registration/invocation, array length exactly one, identity and strict per-native-source checks.
2. **Chat B A-01:** confirm installation ownership for **selected and nonselected** native detector and interface observers. Challenge silent loss of one or both software counters while the actual native detector receives a hit. Native signed power is an additional contradiction signal, but **zero power is not proof of zero crossings**.
3. **Exactly once / branch identity:** original native callbacks invoked exactly once, same `this`, args, ray reference and return, unchanged source emission/detector signed power/crossings/first interface result/processed/truncation compared to uninstrumented native. No new native ray propagation or double wrappers.
4. **Actual Fresnel vs TIR:** two sources, one native surface, separate real reflected/transmitted detectors. Distinguish actual returned Fresnel child object from in-place primary at TIR. Independently check Snell/reference angles (1.5→1 at 30° = 48.5903778907291°, 50° TIR; critical = 41.8103148957786°), and guard against claiming exact-critical numerical correctness.
5. **Faults and finite bounds:** missing/duplicate child, child=parent, unknown source and parent, 64/65 object cap and 32/33 detector hit cap *by labeled fault-injection*, nonselected detector overflow isolation and compatibility with `detector-hit-events`. These caps are not ordinary reachable source fan physics in v1.
6. **All public surfaces:** inspect `report.native.diagnostics`, `summary.observations`, requested result, browser DOM/debug, qualified exports and raw imports for failure/stoppage/weak Fresnel truncation/unknown/overflow: **no raw parent map or partial graph leak**. A→B→A with an injected delayed first-A callback must not republish even when original and final scene hashes match.
7. **Historical evidence integrity:** `test/fixtures/detector-hit-transfer-freeze.json` and previous `detector-hit-integration-rebase.json` remain byte-unchanged; new `detector-hit-provenance-integration.json` records *later* source hashes. This is a new code regression, **not a retroactive frozen blind textbook test**. Compare legacy no-opt-in output shapes and source/meter behavior.
8. **Browser teacher-facing bounds:** actual Chrome qualified input edit/export/reopen/incomplete/raw-import behaviour. Source labels remain *authored*, not original-question authentication. No path overlay, material inference, image detection or measured teacher effectiveness claim.

## Evidence and reviewer authority

- Full implementation-head CI: [GitHub PR #82 checks](https://github.com/physicsvigilante/opticsim/pull/82/checks); [unified run 43740000096](https://github.com/physicsvigilante/opticsim/actions/runs/43740000096). **At packet creation, final-head suite was queued/running; verify outcome live before deciding.**
- Past preliminary feature CI: earlier source commits passed `npm test`, `scripts/ray-provenance-acceptance.mjs` and actual Chrome, but those runs cannot substitute for full exact-final-head certification.
- Past [PR #79 feasibility](https://github.com/physicsvigilante/opticsim/pull/79) and [PR #80 adversarial research](https://github.com/physicsvigilante/opticsim/pull/80) remain draft/unmerged, and are prior **Chat A same-context** experiments.
- The design-only Chat B v2 PASS does **not** certify this implementation. Chat B must inspect this actual source HEAD, report *actual novel code defects or demonstrated negative runs separately from concerns*, distinguish own execution from prior Chat A CI, and do not infer independent student/physics outcomes.

**Review output:** write your own new independent-context **R2 code/evidence** report at `projects/opticsim/pr-82/reviews/review-01-chat-b.md` in this central hub, using [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md). State `pass` / `changes-requested` / `insufficient-evidence`, source/CI SHAs, exact tests and unsupported claims. If you can add genuinely new test-only native or browser cases, use a *separate* source branch rooted at the exact implementation head, without changing PR #82 production code; record test SHA/run IDs. If execution is impossible, say so. Do not merge anything.

Only the **owner** may separately approve source PR production merge after outstanding findings are resolved and current-head CI passes.