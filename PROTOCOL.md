# Cross-sandbox review protocol — two ChatGPT conversations

**Canonical handoff:** `physicsvigilante/review_sandbox`. Each sandbox keeps its **implementation, tests, native runtime, CI, build artifacts, original inputs and source PRs** in the original repository. This hub holds requests, prompts, reviewer findings, developer responses and provenance pointers.

## Roles

**Chat A (implementer):** plans, implements and self-tests a coherent milestone in the source repo; publishes a draft PR with exact source SHA, deterministic CI and physically bounded acceptance evidence. It selects risk level using [REVIEW-RISK-POLICY.md](REVIEW-RISK-POLICY.md), publishes a review packet here when required, and supplies the user a ready-to-paste reviewer prompt for each review cycle. It must never write a purported Chat B finding.

**Chat B (reviewer):** starts in a separate conversation and reads the review packet and **the exact pinned source SHA**, not floating main and not Chat A's private reasoning. It conducts adversarial source/evidence review, independently executes new tests if tools allow, and distinguishes observed evidence from assumptions. It publishes its **own** report as a **new uniquely named file** under `projects/<slug>/pr-<number>/reviews/`, either directly on central main or in its own review branch and PR. A new report should not overwrite an older report. If it cannot write, state the limitation rather than fabricate a committed report.

**Owner:** chooses milestones, approves production merges separately, and may waive an independent review only under documented risk policy. A separate chat may use the same underlying model and GitHub account: report independence is limited to separate context, not proven distinct weights or human expertise.

## Smallest complete workflow

1. **Freeze** one coherent candidate, source PR number, base SHA, head SHA, risk class, physical scope and acceptance criteria. Source CI must pass before independent review unless the review itself investigates a failing gate.
2. **Publish** one central packet `projects/<project>/pr-<PR>/REQUEST.md`, latest `REVIEWER-PROMPT-<NN>.md`, and `STATUS.md` with exact links to CI artifacts and known limitations. There is no need to copy large binaries or production source to the hub.
3. **Review** one candidate using the minimal scope required by the risk class. Chat B reports concrete findings, evidence and unknowns. If GitHub file writing is enabled, use unique `reviews/review-<NN>-chat-b.md` directly on main; prefer a separate review PR for sensitive or contentious reviews. Neither method grants source merge permission.
4. **Respond** in `responses/response-<NN>-chat-a.md` or as an attributable link to the source PR discussion. Triage every blocker or major claim as reproduced, disproved with evidence, deferred with risk or unresolved. If source changes, record a NEW head SHA and rerun CI.
5. **Targeted re-review**, only when needed: Chat B checks the correction and its regression evidence; a new broad review is required if the correction changes physical/numerical/evidence semantics beyond the originally examined scope. Old reports stay bound to old SHAs.
6. **Owner approval → source merge → post-merge verification**. Central review status alone never triggers merges. Record exact merge SHA and results.

User handoff: Chat A always provides a reviewer prompt. Chat B writes the result to GitHub. The owner can simply say **“Review complete”** in Chat A; Chat A fetches the newest attributed report from this hub directly—no copy-pasting review text.

## Interpretation and evidence boundaries

Evaluate **source interpretation fidelity, physical and numerical correctness, native simulation/measurement coverage, evidence integrity, and educational usefulness** separately. Optional textbook-answer completeness is not a substitute for these. Independent reference calculations, actual pinned native traces, screenshots, automated test passes, separately executed novel cases and real classroom observations carry different evidence.

Require explicit source facts, units and assumptions; no invented geometry, material index, ray route, source attribution, detected image, illumination, 3D inference or answer substitution. Preserve native run completion, failure, truncation, stale-hash suppression, endpoint guards and frozen original-attempt fingerprints. Read each source repository's own `AGENTS.md` and domain contracts before reviewing.

The reviewer's **first attempt** and negative results must stay unchanged; if later work corrects a test expectation or a source implementation, append the correction and new source-evidence mapping. A reviewer finding that could not be executed is a hypothesis/limitation, not a demonstrated production bug. If an issue is critical and unverified, keep the PR draft/unmerged rather than using a review budget as a release override.

## Links, versioning and coexistence

Each review request has a stable `project-id`, source repository URL, PR number, `baseSha`, `headSha`, reviewer scope, CI run URLs, artifact hashes and output path. GitHub commit links should pin the material from which a report was derived. On a head move the report is stale for the NEW code, not retroactively wrong.

The initial Opticsim review was created before this central repository existed. Its report is copied here **byte-for-byte by Chat A**, with a link to the original Chat B PR for attribution; this migration is NOT a newly executed independent review. The older collaboration files on the Opticsim PR #76 branch remain historical. Future reviews live centrally.

Do not commit secrets or model API keys. This is a public, owner-directed review hub, without LLM APIs or automated GitHub-to-GitHub merge gates. A central report does **not** appear automatically as a required GitHub status check on the source PR.
