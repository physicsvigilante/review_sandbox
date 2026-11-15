# Shared sandbox review hub

This is the **central GitHub handoff repository** for independent-in-context ChatGPT reviews of the owner's sandbox projects. Production source, native execution, tests and CI stay in each sandbox's own repository. This repo holds stable review rules, review requests, reviewer prompts, written findings and developer responses.

**Two chats:** Chat A implements and publishes a draft source PR. Chat B independently reviews an exact commit and writes an append-only report here. The owner decides merges. Chat B need not paste findings into Chat A's conversation; say "Review complete" and Chat A reads the report from GitHub.

## Read first

- [PROTOCOL.md](PROTOCOL.md) — exact-SHA source review, results handoff, preservation and escalation.
- [REVIEW-RISK-POLICY.md](REVIEW-RISK-POLICY.md) — minimize redundant independent reviews without relaxing test gates.
- [REVIEW-TEMPLATE.md](REVIEW-TEMPLATE.md) — reporting format.
- [Review request template](templates/REQUEST.md) and [reviewer prompt template](templates/REVIEWER-PROMPT.md).

## Projects

- [Opticsim — PR #75](projects/opticsim/pr-75/STATUS.md): migrated first separate-chat assessment and second scoped-pass review (original reports preserved); implementation still unmerged.

Structure: `projects/<project-slug>/pr-<PR-number>/`. Every packet identifies **source repository, base SHA, reviewed head SHA, project PR, evidence links and reviewer-report paths**. Do not use floating default-branch code as the reviewed source.

Review findings use unique append-only files under `reviews/`; developer responses under `responses/`. The first report imported by Chat A is explicitly labeled as a **verbatim copy** and links to its original Chat B GitHub PR. Future Chat B reports should be authored directly here as new files, not silently overwritten.

This is a public GitHub repository. Owner-controlled source material can be linked here; credentials, API keys and tokens never belong in source control. Review PRs may be used for report attribution and conflict avoidance, but **direct creation of a uniquely named report on main is also supported**, so no extra approval cycle is required merely to submit findings.

This repository is **not a CI substitute, automated independent model, or verified physics authority**. A separate ChatGPT conversation does not necessarily use a different underlying model. No PR is merged in any sandbox automatically by this handoff.
