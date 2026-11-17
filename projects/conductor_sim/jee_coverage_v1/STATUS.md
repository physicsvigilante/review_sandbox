# JEE-30 v1 — Actual JEE problem-family evaluation status

**2026-11-17: Phase 0 registration complete, Phase 1 12 literal released-source scientific probes PASS. This is NOT a 30/30 simulation-coverage result.**

## Exact scope and source

- [Frozen benchmark charter](CHARTER.md), [30 original synthetic JEE-style cards](cases.json), [registration integrity validator](validate_cards.py), [12 source-pinned independent-form physics/refusal checks](physics_smoke.py).
- Bank SHA256: `af26127e358fd51bf3ee7fac0e6089fea8a6edee11796354f6ef2bd7fcdf8fa0` (computed by live validation run on exact checked-out review hub bank). Frozen original problem cards are preregistered and **unscored**.
- Released production engine: [M34b main commit `a5113fa4cc924ac10cbb35b2f2d7ac80e11f1bde`](https://github.com/physicsvigilante/conductor_sim/commit/a5113fa4cc924ac10cbb35b2f2d7ac80e11f1bde), real Git tree `d0646c9e4d518008784c42c1fec1c48c81901a09`. Literal Git SHA and TREE verified by actual checkout before physics run. **No production code was altered by JEE-30.**
- Separate draft [M35a PR #81](https://github.com/physicsvigilante/conductor_sim/pull/81) was independently confirmed OPEN/DRAFT/UNMERGED on its own HEAD `49bab64b06cc4594934a27f9ddbb500c454ba150`, source tree `f9d14fedd06659f5abf8f822b31bc7e6353f2a37`, with **23/23 current-source CI completed/success**, but its separate-context independent R2 `projects/conductor_sim/pr-81/reviews/review-01-chat-b.md` was **not present** at the most recent check. Do NOT merge on CI alone. Its [R2 reviewer prompt](../pr-81/REVIEWER-PROMPT-01.md) remains ready for a fresh independent conversation.
- JEE content is aligned at topic level with the official [JEE Advanced 2026 syllabus](https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf) and the existing [teaching-accompaniment evaluation contract](https://github.com/physicsvigilante/conductor_sim/blob/a5113fa4cc924ac10cbb35b2f2d7ac80e11f1bde/docs/evaluation_contract.md). The new cards are **NOT** copied/verified past-year questions, and are NOT an arbitrary-text JEE interpreter evaluation.

## First literal real-source scientific execution

[Successful JEE-30 source-pinned GitHub workflow #44134468820](https://github.com/physicsvigilante/review_sandbox/actions/runs/44134468820): `COMPLETED/SUCCESS`, zero failed steps. Exact literal released engine SHA/tree asserted, `30/30` original cards structurally validated as `REGISTERED_UNEVALUATED`, and all **12/12** new original physical/refusal probes passed using independent analytic references.

| Type | Original case IDs | Count | Physical evidence |
| --- | --- | ---: | --- |
| Static electrostatics/work/conductor | F01, F02, F03, F04, F05, C01, W01, R01 | 8 | Coulomb point superposition, dipole V=0 with nonzero E, 12,000-element independently summed finite rod, two axial rings, one-sided disk field jump, Kelvin grounded-sphere induced charge/force with correct half-energy, uniform-field work and charged-shell surface discontinuity |
| Genuine native time-integrated trajectories | M01, M02 | 2 | Complete x/y native r(t), v(t), qE force at actual saved SI timestamps; M02 negative-acceleration trajectory correctly **does not locate** a velocity reversal outside its 0.7-s observation horizon (true constant-acceleration root at 4 s) |
| Correct physical-domain refusals | R02, R04 | 2 | Axial-only finite disk off-axis field is refused; unpaired off-plane point source cannot masquerade as free planar dynamics |
| **Total actual independently expressed developer probes** | **12 original cases** | **12** | **PASS** |

**Evidence artifact:** [#14351357320](https://github.com/physicsvigilante/review_sandbox/actions/runs/44134468820/artifacts/14351357320), GitHub-provider reported ZIP SHA256 `c5b2de3204d0d7323749d580f77c32a66deb41e507b28a32e539a6ad99a739d9`; this ZIP has **not** been independently downloaded/rehashed. Three retained per-file native artifact files: registration report, detailed Phase-1 numeric/refusal report and SHA256 manifest. No claim of third-party authenticated source truth.

### Honest denominators (never call this 12/30 solved JEE)

- **30/30** synthetic teacher-authored prompts preregistered across **six strata of five**.
- **12/30** sampled for open physics/refusal probes; **18/30 not yet sampled**.
- **8** static physical probes calculated; **2** actually time-integrated numerical trajectory cases; **2** justified explicit refusals. Correct refusals are **not** simulated problem successes.
- **0** independently blinded LLM question-to-model interpretations graded.
- **0** new benchmark viewers graded for student usability or real Chromium visual quality.
- **0** actual source-verified past-year JEE questions graded from this new bank.
- **0** claims of a complete answer key or all-30 broad engine coverage.

The 12 probes were authored openly by the same developer, and physics expectation expressions were known while constructing them. They are valuable scientific regression signals, but do not constitute an independently blinded pedagogical capability score or a separate-context R2 review.

## Negative first-attempt evidence preserved

- [Original run #44134142817](https://github.com/physicsvigilante/review_sandbox/actions/runs/44134142817): FAILED after successfully registering the thirty cases; physics harness stopped at a developer-only incorrect `PrescribedScenario` import location before any physics probe executed. Fixed the test harness import, **no production physics modification**.
- [Second run #44134291788](https://github.com/physicsvigilante/review_sandbox/actions/runs/44134291788): FAILED at M02 fixture because its original source display label exceeded the existing 48-character input contract. The production engine correctly refused invalid authoring. Fixed the fixture label, **no production source validation weakened**.
- [Third run #44134468820](https://github.com/physicsvigilante/review_sandbox/actions/runs/44134468820): SUCCESS, all 12 independently expressed probes and honest result-denominator controls passed. Earlier failures remain accessible and **were not relabeled success**.

## Next benchmark execution gates

1. Have a fresh separate-context Chat B independently review M35a PR #81 before any owner-approved merge. Do not mix the benchmark with that source release.
2. Address known [legacy sweep evidence consistency issue #80](https://github.com/physicsvigilante/conductor_sim/issues/80) in a separate compatibility-reviewed corrective PR; a green JEE benchmark cannot override that integrity finding.
3. Extend the 18 untested original cards in independently developed batches. For each, log the typed model, full source inventory, real solver admission/refusal, native physics, independent reference, present/excluded phenomena and exact time/geometry boundaries. Preserve each first failure.
4. Conduct a **blinded** natural-language-to-model evaluation by a fresh author unaware of card reference answers. Separately evaluate student-facing offline HTML/Chromium images and affordances; score the four mandatory teaching dimensions and optional final-answer completeness. No labels prefilled in preregistered cards.
5. Add at least 10 source-verified actual JEE questions with pinned PDF and diagram transcription and clear original/illustrative parameter separation. Do not claim benchmark generalization until these holdouts are assessed.

**No JEE-30 production PR or M35a release was created by this benchmark effort.** Preserve source SHA/tree and owner/reviewer merge gates.
