# EM Fields PR #14 — centralized R2 review status

**AWAITING FIRST CHAT B REVIEW. Source PR DRAFT and UNMERGED. No independent review verdict yet.**

- Source: [physicsvigilante/emfeeld PR #14](https://github.com/physicsvigilante/emfeeld/pull/14).
- Exact base `7e6bd8c72cac7708ab3c2355cc1a98db09762133`, head `d46d04e23a142ea1c969b964ae5e1780110264c9`, source tree `c274d94dd2185dcecdfca735e2951edae3e3d835`.
- CI merge-preview checkout `014d74123551cd1ab0ce5fbc335082663d160352` has identical source tree.
- Risk **R2** because new test-particle structural revisions change initial-condition membership, stable physical identities, native index mapping, and saved-evidence meaning.
- [Linux and Windows full release CI](https://github.com/physicsvigilante/emfeeld/actions/runs/43740900095) **PASS**, per platform 1,308 headless, 18 historical, 33 real-PyVista tests. [Separate real-PyVista CI](https://github.com/physicsvigilante/emfeeld/actions/runs/43740899982) passed. E1/G1/T1 native run/reference cases complete with one expected refusal for removed-body observations.
- Downloaded CI artifact identities: Linux `14172094227`, SHA256 `a56b4b1352fcdcc31089ceca9b54ffb3e23910587f828ecc66b48b2e6830fed1`; Windows `14172751162`, SHA256 `aa975b9ff5cd309df360b2f618c6b6b4163b6d1ca41b5a05612fa33baee29d08`. Both 1,451 entries, CRC clean, with preserved original runs and exact mapping/reference reports.
- [REQUEST.md](REQUEST.md) documents physical acceptance criteria, author test history, non-goals and evidence. [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md) is the user's ready-to-paste handoff.
- Chat B must independently author a NEW `reviews/review-01-chat-b.md` file directly in this review hub (or a reviewer-owned central PR). **Chat A has not authored a reviewer finding.**

After the owner says **“Review complete”**, Chat A fetches the new report, triages defects, adds regression tests and obtains new exact-head CI as required. A separate explicit owner approval is needed to merge, followed by post-merge Linux/Windows and viewer checks and an append-only central release report.

No physics law, integrator, existing model evidence, user installation or classroom evaluation was changed by this review workflow.
