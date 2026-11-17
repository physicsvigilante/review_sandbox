# Opticsim — engine architecture, physical integrity and release audit

**Date:** 2026-11-17. **Scope:** production `main`, unreleased v14–v18 physics candidates and separately held native directional footprint, plus source-CI evidence and a deliberately non-release cross-feature integration rehearsal. **Not:** an independent local reproduction of the pinned PhyDemo runtime, a certified optical image/point-spread assessment, human teaching evaluation or authorization to merge.

## Executive assessment

Opticsim has a **sound separation of responsibilities**: physical authoring contracts and conservative geometry admission; native PhyDemo geometric-ray propagation; observations of actual callbacks; and conditional analytical results/portable provenance. The pinned `v5.4.0` PhyDemo at `811f508d2b070898c241a568b0c167dcb8645251` is deliberately unchanged, and current public execution gates generally withhold readings when the native run is incomplete, stopped, undefined, weak-ray truncated or stale. These are meaningful design strengths.

The largest current risks are **release coordination and extensibility**, not a demonstrated sign error in the already reviewed scalar optical references. Production `main` remains at `d3509e82fb65d81aabe336666851f8f2962623f4` while eight separate feature/research PRs remain held. Individually green branches are not the same as a verified combined, shipped simulation engine.

## Evidence and directly inspected surface

- [Source main](https://github.com/physicsvigilante/opticsim/tree/d3509e82fb65d81aabe336666851f8f2962623f4) and [v18 candidate #120](https://github.com/physicsvigilante/opticsim/pull/120): `src/composition-profiles.js`, `src/contract.js`, `src/authoring.js`, `src/adapter.js`, `src/spherical-lens.js`, `src/thick-lens-aperture-composition.js`, `src/finite-aperture.js`, `src/session.js`, `src/observables.js`, `src/qualified-utils.js`, `src/qualification.js`, `src/qualified-ui.js`, native numerical/parentage audit code, reduced lens mathematics, problem workflows and evaluation scripts.
- [Main-based detector footprint #118](https://github.com/physicsvigilante/opticsim/pull/118), [native angular fan research #121](https://github.com/physicsvigilante/opticsim/pull/121), and [non-release cross-feature integration rehearsal #122](https://github.com/physicsvigilante/opticsim/pull/122). Their current Git heads and dependencies were checked via repository metadata; see the separate per-PR CI and review records.
- Native fan evidence from #121: a centered 36° `AngleSource` at medium density emits ten sampled rays; a higher density setting emits twenty. In y-UP Opticsim coordinates the original ten native angles are `+18°, +14.4°, …, −14.4°`, **not** the opposite order. For a vertical aperture 50 mm after the source, independent initial straight-line intercepts predict 7/3/0 first-pass opaque-arm hits for gaps 8/20/40 mm and the actual native events agree. Additional return-side absorptions are 2/4/2, respectively. All of these sampled traces completed without reported truncation or undefined behavior. Neither discrete count divided by emission count nor the RMS of sampled detector hits is continuous radiometric throughput.
- Native detector footprint #118 computes **unweighted, sample-based mean, span and population RMS** separately by signed detector-normal crossing direction; it refuses contradictory positions, near-grazing rays, >32 event overflow, and incomplete/stale runs. No inferred optical image or per-source history is supported by this statistic.
- Branch metadata currently reports `main.protected=false`. Each of the 11 standard CI workflow files filters PR events to base branch `main` and invokes `npm run setup` and `npm test` independently. Source-branch/review-verifier CI checks were examined; workflows are not independent physics replications. A recent standalone planar-angular Chrome job failed to create `DevToolsActivePort` on one attempt and succeeded on rerun with unchanged source; the root cause was **not established**.

## Ranked findings

### P0 release safety — unprotected production branch and held integration gates

**Observation:** The default branch has no GitHub branch protection, while owner-approved review holds currently exist. This permits an accidental direct write even if the development conversation intends to forbid a merge. **Correction in progress:** [release safety issue #123](https://github.com/physicsvigilante/opticsim/issues/123) requests branch protection and stacked-PR CI rules; repository administration permissions are needed. No release branch was merged. **Gate:** explicit owner decision, applicable CI and review per independent PR; no auto-merge.

### P1 physical/measurement integration — independently green is not combined

**Observation:** The v18 optics source and the main-based footprint each passed separately but had **four overlapping paths**: README, `src/app.js`, `src/observables.js` and `test/detector-hit-transfer.test.mjs`. A test of #118 alone cannot prove its opt-in hit collection works on the v18 two-thick-lens/aperture return. **Action:** [draft research PR #122](https://github.com/physicsvigilante/opticsim/pull/122) copies both frozen candidate features onto a separate branch without merging them into production or changing their reviewed heads. It preserves their old viewer hashes, records a new combined blob and adds real native crossing-direction, true-zero and depth-truncation regression cases. First CI run failed a **historical exact-source SHA assertion** after the viewer changed; the assertion was corrected on the research branch to preserve *both* source identities rather than erasing the old freeze. **Gate:** all Node, public CLI and actual browser integration checks on an exact combined source tree, followed by separate review of any future integration-release candidate.

### P1 CI reliability and provenance

**Observation:** 11 workflow jobs each do heavy setup/full test execution, and workflows do not trigger automatically on PRs targeting feature dependency branches. This has encouraged temporary retargeting of stacked PRs to `main` and back, with exact Git tree checks added manually. CI fan-out may increase runner contention, but the observed Chrome startup failure has no proven cause. **Plan:** extend reviewed CI triggers for actual dependency bases; consolidate redundant full Node test setup without dropping family-specific native/Chrome tests; require source/tree match and failures/retries preserved. Track under [#123](https://github.com/physicsvigilante/opticsim/issues/123).

### P1 bounded-general architecture versus a catalog of special combinations

**Observation:** Composition profiles are **whole-system admission rules**. They correctly refuse unsupported combinations and protect old saves, but v14–v18 each require a new schema/profile for a specific physical mix (two finite glasses; two thick lenses; mirror; aperture). This is robust yet does not equal arbitrary composability. **Plan:** extract an audited capability policy built from shared native component validators plus whole-scene constraints: medium topology, disjoint finite bodies, finite-surface clearances, source modes, detector passive geometry, numeric budget and forbidden interactions. Keep versioned profiles as reviewed *admissions*, not a permissive Cartesian product, and test compatibility by negative/positive physical scenes and metamorphic orientation/scaling. Preserve source IDs and do not encode a ray route.

### P1 incomplete source-family coverage — angular beams and incident edge ambiguity

**Observation:** The native PhyDemo `AngleSource` correctly traced through the v18 optical objects in test-only PR #121, but **v18 canonical authoring intentionally still accepts single rays only**. Extending this is not just a one-line mode whitelist: discrete native samples can hit aperture arm/gap endpoints, lens rims and curved-face tangencies; brightness cap, density and backward-return events need distinct qualification. **Plan:** first a stricter test-only edge/brightness/density matrix; then an isolated versioned beam profile with explicit angular bounds, full native completion gates, terminal absorption direction and sample-count diagnostics, public CLI and Chrome tests. Avoid a continuous beam, image, source lineage or PSF claim.

### P2 measurement scope, source identity and optical teaching semantics

**Observation:** `blocker-absorptions` counts **all native incident absorptions**; for a return system, it combines initial forward blocking with later backward blocking. #121 showed this is materially different: with 20 mm opening, 3 forward and 4 backward hits out of 10 emitted native rays. Similarly, directional detector footprints are unweighted summaries, limited to 32 recorded hits, without general source attribution. **Plan:** add an *opt-in bounded directional absorber evidence* study (no source-pairing), and decide whether a higher event limit is warranted only after performance/memory tests. UI must always label sampled results and distinguish zero observed hits from unavailable/incomplete measurements.

### P2 independent numerical verification

**Observation:** Green Node/Chrome CI exercises actual pinned physics and several independent scalar checks (Snell, spherical normal, reflection, Fresnel, TIR and native finite-face intersections), but many geometry families and near-coincident contacts remain represented only by bounded examples. Separate Chat B reviews recompute scalar physics and inspect CI; they generally have not rerun a separate pinned-native experiment. **Plan:** build a reproducible independent reference harness, not a second production ray tracer: calculate isolated analytical intercepts, Snell and specular references, TIR thresholds, symmetry/reversal transformations, and numerical perturbation envelopes. For high-risk cases that produce ambiguous native results, withhold rather than repair.

### P2 educational usefulness and original-problem interpretation

**Observation:** The existing teaching-fidelity and original-problem evaluation layers deliberately separate interpretation, native correctness and educational claims, but the teaching-fidelity runner still declares **zero teacher and student participants**, and its fixed inputs are not evidence of broad unseen-problem generalization. **Plan:** score unfamiliar problems with a frozen interpretation protocol and separate labels: interpreted apparatus/assumptions, physical correctness, simulation coverage, educational explanatory usefulness, and optional textbook final-answer completeness. Maintain explicit unsupported/needs-information outcomes. Test portability using the existing manual JSON workflow before pursuing direct LLM in-app authoring.

### P3 maintainability and evidence presentation

**Observation:** Strict append-only viewer SHA assertions have successfully prevented unnoticed changes to frozen R1 evidence, but each new browser feature needs a new separate post-exposure identity and legacy-tests update. This is both a strength and a frequent CI integration failure source, as shown in v18 and #122. **Plan:** preserve the original historical freeze verbatim while centralizing later *reviewed feature source lineage* into a single append-only, machine-validated manifest, with old SHA values retained and a test validating parent-child provenance. Do not reclassify exposed test material as blind.

## Priority release and engine roadmap

**Stage A — stabilize held releases:** obtain separate independent v18 review (#120) and address findings without silently changing earlier reviewed source heads. Use an explicit dependency-order owner release plan for v14 #107 → v15 #110 → v16 #113 → v17 #116 → v18 #120. The main-based #118 measurement must be separately integrated/tested as its own release decision. Keep research #119/#121/#122 unmerged and close/supersede them when incorporated into a reviewed release.

**Stage B — demonstrate combined compatibility:** complete and independently inspect the research integration for v18 and #118, especially the adapter collector opt-in, directional hit statistics, true detector misses and stale/incomplete readout suppression. Record exact source/tree matching and Chrome evidence. Do not confuse a research cherry-pick with release authorization.

**Stage C — reusable light-source families:** validate a native directional angular source with sampled stop/lens interactions, before generalizing apertures, mirrors and refractive regions further. The hardest acceptance cases are near arm ends, lens rims, oblique propagation, density changes and full-Fresnel truncation. Keep native rays exclusively owned by PhyDemo.

**Stage D — principled medium/component composition:** add reusable disjoint-solid and finite-surface constraints instead of creating an unrestricted “anything with anything” contract. Demonstrate source/mirror-first/reverse-path/missed-component cases for every new admitted family.

**Stage E — teaching validation:** prospectively test actual unseen educational problems with user-friendly readouts, documented assumptions and bounded unknowns. Preserve the user's preference for manual JSON transfers; LLM automation is not required to advance the physical core.

## Invariants that should never be weakened without explicit independent review

- Canonical input contains only fully stated physical data or separately labeled assumptions; **no fabricated optical route or missing source values**.
- PhyDemo pinned native engine owns reflection, refraction, ray spawning, absorption, detector intersections and stopping.
- New measurements are derived from complete native observations, opt-in and bounded; incomplete/stale/error/truncated runs **never become qualified values**.
- A conditional ideal image, sampled RMS, source emission count or visual Chrome rendering is **not** independent proof of a detected physical image or arbitrary JEE textbook answer.
- Existing schema versions, source hashes, independent review reports and historical frozen evaluations are append-only evidence; never rewrite them to make tests green.
- Review clearance, exact-source CI, explicit owner release approval and production merge are **four distinct events**.

**Current disposition:** Product direction remains technically promising with substantive native capabilities. The immediate engineering priority should be safe release/integration and validated reusable source/geometry composition, not more answer formatting or UI automation. This audit is a source-and-evidence review with documented limits; it does not claim a universal numerical correctness certificate.


## Post-audit integration outcome — same date, separate evidence

[Research PR #122](https://github.com/physicsvigilante/opticsim/pull/122) completed its **source-CI compatibility rehearsal** at head `70cf502d19e243e4a8d7d1e0795f008c101c582d` (Git tree `df9282da11ff416d0033cdf7e09509ba8dc24bc9`). The synthetic main-target CI merge was independently inspected as the **same exact tree**. **865/865 Node 24 tests and 11/11 workflows passed**, including 5 existing public directional-footprint CLI cases, 7 real-Chrome footprint checks, 13 v18 aperture Chrome checks, and four new combined native integration tests.

Actual native evidence in this source-CI run: the v18 two-lens/mirror return crossed the detector twice in opposite normal directions (one in each group; each one-event sample RMS 0, **not a physical zero-width image**). An aperture-blocked case had zero native detector crossings with **null** mean and RMS statistics in both groups, and reported one true native absorber hit. A footprint-only requested result still enabled the pre-existing hit-event observer; depth-8 incomplete propagation suppressed all sampled measurements. The first attempted combined CI failed a *historical v18 viewer Git-blob pin*; it was fixed **in the disposable integration branch only** by preserving original v18 and footprint pins and introducing a separate integrated viewer SHA. Failed CI remains visible.

**Disposition:** The specific compatibility risk between held #118 and v18 #120 has been reduced by positive exact-source native/public-CLI/Chrome evidence, but no independently rerun PhyDemo reviewer experiment, targeted cross-feature physical review, owner approval or production release occurred. The branch was retargeted to v18 as a draft and remains **UNMERGED**. Release governance and v18 independent physics review remain the highest-priority gates.
