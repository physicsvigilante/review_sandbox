# conductor_sim — shared two-chat review handoff

Adopted: 2026-11-15. This page registers the project only; it is **not** a review request, a reviewer report, a release approval or a modification of the simulation repository.

- **Source repository:** https://github.com/physicsvigilante/conductor_sim
- **Review hub:** https://github.com/physicsvigilante/review_sandbox
- **Canonical governance:** [PROTOCOL.md](../../PROTOCOL.md), [REVIEW-RISK-POLICY.md](../../REVIEW-RISK-POLICY.md), [REVIEW-TEMPLATE.md](../../REVIEW-TEMPLATE.md), [request template](../../templates/REQUEST.md), [reviewer prompt template](../../templates/REVIEWER-PROMPT.md)
- **Source-specific contracts:** [composability](https://github.com/physicsvigilante/conductor_sim/blob/main/docs/composability_contract.md) and [teaching-accompaniment evaluation](https://github.com/physicsvigilante/conductor_sim/blob/main/docs/evaluation_contract.md). Resolve these to the pinned PR head for each review. The source repo had no root `AGENTS.md` at onboarding; do not invent its contents.
- **Accepted source baseline at registration:** `d27c504f0a2bb336784a4ce9116f84c992b915db` (post-M24b corrections).
- **Pending work:** M25a shared source geometry was locally developed and tested in a prior conversation but was **not published or CI-accepted**. Its local previews, claims and patch are **not** a central review packet and imply no source merge. Publish an exact source candidate and pass current-head CI before asking Chat B to review.

## Project-specific risk and verification

- **R0:** documentation, reviewer packets and non-executable notes — source/diff/link checks; normally no second chat.
- **R1:** bounded UI or compatibility work with unchanged physical/evidence semantics — deterministic regressions, full relevant CI and actual browser checks; focused second-chat review if trust or behavior can change.
- **R2:** new physical relationships or solvers, numerical integration/guard or event semantics, source/physical qualification, saved evidence meaning, or geometrical representation that could imply false physical placement — full source-pinned independent review. M25a is provisionally **R2** because off-plane omissions and ring/disc source projections affect interpretation fidelity and viewer evidence, although its physics laws are intended to remain unchanged.

For M25a check independently: true three-dimensional source positions, axes, radii and signed plane offsets; edge-on versus intersecting rings/discs; no falsely projected off-plane rods/charges; correct stable source IDs; camera/projection covariance; unsupported source shapes and axis-only field refusals; numeric records and browser canvases agree with exact pinned source; no invented field lines, conductor response, 3-D scene or trajectory; preserved historical examples and exports. New physical-law validation is not claimed solely from unchanged FEMM regressions.

## How to create the first packet

Only **after** a source draft PR exists with an exact pinned head/tree, passing applicable current-head CI and named artifacts: create `projects/conductor_sim/pr-<number>/REQUEST.md`, `STATUS.md`, and `REVIEWER-PROMPT-01.md`. Include source PR/base/head/tree SHAs, risk, acceptance cases, negative tests, URLs/digests and known limits. Chat A gives the owner a short paste-ready Chat B prompt. Chat B writes an append-only `reviews/review-01-chat-b.md` itself to this hub (or a review-only PR); Chat A must not imitate the reviewer.

After the owner says **"Review complete"**, Chat A reads the latest attributed report from the hub, reproduces and fixes confirmed defects on a new source SHA, runs CI and requests only warranted focused re-review. Preserve old findings and failed first attempts. **Merge only after separate owner approval**, then verify post-merge CI and append a central merge/status record. No central file serves as an automatic source CI check or release gate.
