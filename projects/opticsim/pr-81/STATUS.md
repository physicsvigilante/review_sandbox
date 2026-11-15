# Opticsim PR #81 — R2 design-review status

**State: READY FOR A SEPARATE-CHAT DESIGN REVIEW; no independent Chat B report submitted.** This is a pre-implementation R2 conceptual critique request, not a production readiness decision.

- Source proposal PR: https://github.com/physicsvigilante/opticsim/pull/81 — **draft, unmerged**.
- Freeze: base `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`, proposed documentation head `df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7`.
- Exactly one added proposal file (137 lines), no executable changes. Actual optics code and test suite remain those of the production base.
- Research inputs PR #79 and PR #80 remain **draft and unmerged**. PR #80 CI had 11/11 workflows passed at Node 24.19.0; four of twelve native scenarios properly withheld and one invalid geometry preflight rejected.
- Proposed design candidate CI: [GitHub unified workflow 43730335002](https://github.com/physicsvigilante/opticsim/actions/runs/43730335002), check live status; this is software regression verification **only**.
- Review request: [REQUEST.md](REQUEST.md).
- Owner handoff prompt: [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md).
- Review file to be **authored by independent-context Chat B**, not prewritten: `reviews/review-01-chat-b.md`.

**Open gate:** Independent R2 design feedback required before Chat A proposes implementation. A design pass does **not** sign off future code. Any production implementation later requires a separate owner approval, tested feature PR, new CI/evidence and a fresh R2 review at its exact implementation SHA. No GitHub source merge or deployment is authorized by this packet.