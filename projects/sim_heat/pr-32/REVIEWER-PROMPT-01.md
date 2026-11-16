# Chat B prompt — SIM_HEAT historical PR #32

Independently review **draft [SIM_HEAT PR #32](https://github.com/physicsvigilante/sim_heat/pull/32)** at exact head **`502a6e8c392d8b8cfb8a4361cddcae4fafff6f01`** against frozen V2 PR #31 source `d857c8e807612026ecdf624277b4ace3977fefe3`. Read the [central REQUEST.md](REQUEST.md), review protocol and risk policy.

This is a **focused R2 investigation of a FAILED cross-run reference-reproducibility gate**, not a native OpenModelica or source-merge proposal. The two new Ubuntu 22.04/24.04 hosts produce identical new V2 bundles (`c30e8783…`) that differ from the independently reviewed PR #31 saved V2 bundle (`d2b8e2ca…`). The original saved F0 `hotLead.G` 80× failure remains frozen.

Independently inspect BOTH host artifacts from failed CI [#43921113470](https://github.com/physicsvigilante/sim_heat/actions/runs/43921113470), the original PR #31 artifact from successful CI #43915934653, and the **exact-head forensic** [CI #43922852455](https://github.com/physicsvigilante/sim_heat/actions/runs/43922852455), artifact `14253809455` (SHA-256 `448e3096f809fd773ef1ebf9d6e3f62510abbe375e6e2caa6652d60394d2616c`). Verify full source/ZIP/seal identities, wheel/BLAS/CPU provenance, byte-different fields, 148,037 scalar and 16,004 integral old-vs-new numerical error budgets, and what is **not** established about the cause. Review the seven new-only source paths; do not interpret a green *forensic* job as a passing reference identity gate.

Advise whether an immutable originally reviewed V2 bundle with explicit numerical variation evidence is an acceptable **proposed** future canonical checking reference, or whether a new deterministic generator is required; specify open science and source/one-shot gates. Give scoped PASS, CHANGES REQUESTED or INSUFFICIENT EVIDENCE **for the accuracy of this negative reproducibility record only**.

Commit a new independent report to `projects/sim_heat/pr-32/reviews/review-01-chat-b.md` in `review_sandbox`. Do not modify frozen source, overwrite old evidence, waive 100× accuracy, merge historical PRs, launch OpenModelica or claim completed C1 native transfer.
