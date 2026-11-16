# Reviewer prompt 01 — EM Fields PR #25, verified ensemble view selector (R1)

You are **Chat B**, conducting an independent **focused R1 review** of a new sealed-ensemble native view selector, not reviewing floating main, not a broad physics requalification, and not granting source merge approval.

Read [REQUEST.md](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-25/REQUEST.md), [Issue #24](https://github.com/physicsvigilante/emfeeld/issues/24), [source PR #25](https://github.com/physicsvigilante/emfeeld/pull/25), central [PROTOCOL](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md) and [RISK POLICY](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md), and the source repository `AGENTS.md` and native ensemble/view contracts.

**PIN exact source head `4fe896ff6bb98d21a090bc16a84fe26145f9f5e7`, qualified base `bf6a18399c604136dd363ad94d40557dbe2c2543`, PR merge-preview `75f818bdb199ad97ae036bd1dea380f03d7e71f6`.** Establish the exact Git tree independently. Do not accept a moving SHA or silently assume CI has passed because PR status is green. At initial packet publication, Linux and separate real PyVista had passed, Windows was still in progress; verify latest exact-head CI separately.

Independently execute new tests covering (a) exact baseline versus member named `baseline`, (b) 2–4-member identity/index binding and complete native member within partial G1 comparison, (c) malformed selection/tampered ensemble/store/template and incomplete run refusing **before renderer invocation and with byte-identical files**, (d) static and motion sample indices, (e) fresh external screenshot versus existing/symlink/alias/protected paths, and (f) no regression in existing `run`/`inspect` and preflight guards. Inspect actual real-PyVista E1 and G1 view output and distinguish saved-state presentation from numerical recomputation and manual Windows pointer checks.

Publish your own NEW report at:

`physicsvigilante/review_sandbox/projects/emfeeld/pr-25/reviews/review-01-chat-b.md`

Give **scoped PASS**, **CHANGES REQUESTED** or **INSUFFICIENT EVIDENCE**, with exact tested source, novel test results, preserved first failures, remaining limitations and precise reproduction if blocked. **Do not alter source PR #25, merge, prior reviews or saved experiments.** On publication the owner can say “review done” to the implementer; the implementer will fetch this central report and follow normal merge gates.
