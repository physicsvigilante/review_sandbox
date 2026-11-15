# EM Fields PR #17 — central R2 review and integration status

**INDEPENDENT-CONTEXT R2 SCOPED PASS — SOURCE PR DRAFT/UNMERGED; SEPARATE OWNER MERGE APPROVAL REQUIRED** (2026-11-16, Asia/Kolkata). The user's “review done” confirms handoff completion, **not merge authorization**.

- [Source PR #17](https://github.com/physicsvigilante/emfeeld/pull/17) remains **open/draft/unmerged**, based on qualified `main` `8fe6331aefa252585b3b90f54b8ee7cbbac5e605`.
- Exact approved reviewed implementation head: **`62121252c6526c53c29440dcd8f41b6109f70e04`**; exact canonical Git tree **`339224f69e5c671dea83678cdb00845887ce27b4`**. PR merge-preview `6d1c219e67cf300df7044f24690edf779270ac8f` has the same source tree.
- Original [REQUEST.md](REQUEST.md) and [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md) pin the same exact source and CI evidence.
- Independently authored [Chat B review 01](reviews/review-01-chat-b.md): **scoped R2 PASS**, no demonstrated blocker/major or source code correction requested. Preserved original report Git blob `5f6ecd63e2f0dc5df51abb1db355a5cb976c8755`, central Git commit `b60c706a0d6fa0db0447f2102a41f933186b6696`; **not edited by Chat A**.
- [Chat A response 01](responses/response-01-chat-a.md) gives an attributed disposition of F-01–F-04, explicitly **not a second reviewer verdict**. The findings concern expected incomplete/crashed-store refusal, LF/CRLF raw runtime hash differences with identical canonical Git tree, bounded evidence/teaching limitations and accurately preserved earlier failed CI attempts. None was a demonstrated production blocker.

## Qualified source and independent-context evidence

- [Exact-head full clean-install Linux/Windows CI](https://github.com/physicsvigilante/emfeeld/actions/runs/43751887519) **SUCCESS on Ubuntu 24.04 and Windows 2022**, per OS 1,342 headless + 18 historical behavioral + 33 real-PyVista = **1,393 suite-membership tests**. One unchanged obsolete whole-file freeze assertion remains deselected; the additional 34 focused atomic test executions duplicate tests within headless.
- [Separate exact-head real-PyVista qualification](https://github.com/physicsvigilante/emfeeld/actions/runs/43751887558) **SUCCESS**, including real rendering/slider checks.
- Frozen same-author E1/G1/T1 qualification passed on both OSs: three accepted atomic descendants, six complete baseline/final native runs, one expected old-presentation refusal, **36 independent-expression static observations and seven checked trajectories** per OS. Baseline physical and saved evidence preserved.
- Linux GitHub artifact `14176882398`, SHA256 `932b1689c0d34bb121a1ccaa0539ea1c9db0988ef1ebb60ce88ff5cd11865880`; Windows artifact `14177380152`, SHA256 `e93c60adb6ec39c7f7dd95bb0bcab57edcf65bee2181e616c8aaf2714a6d6ea6`. The separate reviewer reports downloaded ZIPs, CRC-checked 1,629 entries per OS and revalidated six complete run inventories per OS; source Chat A only had earlier GitHub provider digests, not an independent ZIP audit.
- Reviewer independently reran **199 relevant tests** and **14 novel adversarial case groups including eight two-process contention trials**, ran fresh native E1/G1/T1 cases and authored new analytic/independent RK4 comparisons against both archived OS results. Its attempted whole headless test run was **incomplete**, not independently green; hosted author CI establishes the full-suite pass.

## Retained boundaries and next gate

Original failed CI and Chat B's own audit missteps remain historical evidence; none is rewritten. Separate-chat GPT-6 review is independent context and actual independent test authorship, **not** independent human physics certification. Local structural locking, incomplete crash writes and hash inventories are not distributed/crash-recovery ACID nor external-source authentication. Nonrelativistic prescribed-source independent test-particle regime remains unchanged. No manual Windows desktop mouse tests or classroom teacher feedback were obtained. No user's local Conda installation, existing saved models or studies changed; teaching evaluation remains paused.

**Next gate: obtain explicit owner approval specifically to merge PR #17**, then recheck exact head/tree, perform an authorized guarded source merge, run **fresh merged-main** Linux/Windows clean-install plus separate real-PyVista CI, archive exact results in a new append-only central MERGE-REPORT. Do not treat review success, source CI, or this status update as merge permission. Any future source movement requires new qualification and proportionate re-review.
