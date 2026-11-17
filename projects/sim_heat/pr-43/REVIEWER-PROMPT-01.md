# Chat B — SIM_HEAT PR #43 independent stale-snapshot CAS R2

Continue as independent Chat B reviewer of historical [draft SIM_HEAT PR #43](https://github.com/physicsvigilante/sim_heat/pull/43).

**Review exact HEAD `4e220a152e702c06b07320850f5caacff1091bb3`**, Git tree `4a931c0e017eb650c0b4a63c5dfdf38097ad9d72`, based on independently reviewed PR42 `32cbb7d02b7db0cbc322fb0e7826861fd902a77a`.

Read full [central review request](REQUEST.md):
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-43/REQUEST.md

This PR adds exactly **four offline fake-CAS source/test/docs/CI files**. It demonstrates why a **stale snapshot needs atomic compare-and-swap** but remains **NOT a real cross-host owner-controlled one-shot gate**.

Independently test/inspect:
- 16 stale readers of ONE fake initial snapshot and ONE memory store: exactly **1 toy first claim / 15 stale refusals**.
- Unsafe read-then-use with no CAS: **2 fictional first claims**.
- TWO independent fake stores using the same campaign: **each claims first**, proving split-brain.
- Erase/recreate fake state: a new first claim is possible, although old-epoch replay is refused.
- Lost acknowledgment after a fake committed claim: retry denied on that fake, **no native result can be inferred**.
- Forged snapshot/bool/float scalars, native-budget/owner/release flags and forbidden CLI verbs must refuse; `require_real_native_permission` must **always raise** and PR41's **11 actual native-release gates remain MISSING**.

Check exact-head [CI #44051422673](https://github.com/physicsvigilante/sim_heat/actions/runs/44051422673) and [artifact #14313149095](https://github.com/physicsvigilante/sim_heat/actions/runs/44051422673/artifacts/14313149095), whole ZIP SHA-256 **`00d70f397c6e05fd5746583390c92fae3970e635684abb7bac2b99e24958d46c`**, 30,078 bytes, **44/44 CRC valid**, **309/309 OFFLINE tests**. Confirm original frozen physics, Modelica author/evaluator inputs and exact approved PR31 raw reference/seal untouched. Original F0 80× vs required 100× accuracy FAIL, and PR32 cross-host original-seal bitwise regeneration FAIL remain historical.

Commit a **NEW independent report** to `physicsvigilante/review_sandbox/projects/sim_heat/pr-43/reviews/review-01-chat-b.md`, with **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, evidence and clear separation of your independently executed probes vs CI-inspected tests. A scoped PASS is for an **untrusted OFFLINE differential** only; it authorizes no external CAS, OpenModelica version query/build/launch, owner native budget, production merge, or real scientific qualification.

Do not modify source, execute or install OpenModelica, regenerate original references, merge historical F0 PRs, or claim a true native launch lock. Real native work requires a separate authenticated owner-approved release/host/plan, durable external CAS and fresh R2 plus explicit owner authorization.