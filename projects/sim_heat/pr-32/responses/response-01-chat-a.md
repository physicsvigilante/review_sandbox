# SIM_HEAT PR #32 — Chat A disposition of independent reference-reproducibility review

**Reviewer report:** [review-01-chat-b.md](../reviews/review-01-chat-b.md).
**Exact reviewed source:** `502a6e8c392d8b8cfb8a4361cddcae4fafff6f01`, tree `ef08c7029975c7e3c224c6a13d9c5663986604b8`, historical F0 baseline `dd8c9432abe97563414bb3ed809e61e673473812`.
**Disposition:** ACCEPT **scoped PASS for faithful negative forensic evidence**. The previously reviewed PR #31 V2 checking reference is **not reproducible bit for bit** in the tested fresh environments. That failed identity gate remains FAIL/HOLD; a successful diagnostic CI does not change it. Neither policy exception, canonical-fixture promotion, native F-02 execution, nor production merge is authorized.

## Findings and follow-through

- **F-01 — source/archival integrity: accepted.** Exact seven-addition historical branch diff; unchanged authoring, F0 physics/checker/runner, original 80× failed reference, original V2 numeric candidate and native plan. No original artifact or tolerance modified.
- **F-02 — identity failure: accepted and preserved.** PR #31 separately reviewed V2 raw SHA `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368`, canonical seal `d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`; both new hosts yield raw SHA `456b82081aa97b59f55e86830ddabfc36f14fd74991542e350a2266e0f9962f5`, seal `c30e8783d39c7b0198c1adf0273ac84568f698f08287f02bf79eeed224830b07`. The two-host CI is genuinely **failed**; its forensic follow-up **passed recording evidence**, not reference certification.
- **F-03 — sampled numerical fidelity: accepted.** Independent high-precision reviewer checks of *both distinct V2 objects* confirm strict unchanged 100× budgets across 37 × 4,001 scalars and 4 × 4,001 integral values. Original F0 80× static breach remains FAIL. Small between-reference numerical drift does not convert mismatched SHA into identical identity.
- **F-04 — provenance: accepted with limits.** Complete two-host wheel/CPU/BLAS records, no authenticated cause of PR #31-to-new drift; do not infer root cause from OS or BLAS speculation. Mutation tests and frozen pins examined with clearly distinguished execution provenance.
- **F-05 — major gate: OPEN.** Source-independent bitwise regeneration of PR #31's archived V2 is not established and will not be claimed.

## Decision for next development milestone (not a release approval)

Pursue **Option A as a draft candidate**, subject to a distinct owner/independent R2 gate: preserve the **actual PR #31 V2 bytes**, raw SHA, canonical seal, original source/spec identities and exact numeric allowances in durable repository storage beyond the 90-day Actions retention; implement fail-closed **read-only exact-artifact loading** with identity/budget/negative mutation tests. Never call `reference.prepare` as fallback, never automatically accept `c30e…` as equivalent to `d2b8…`, never modify F0 core or historical bundles. A draft policy and storage experiment may be developed and independently reviewed, but **promoting its new contract to certified reference use requires explicit owner approval**. No native workflow will be created or launched in the draft policy milestone.

**Status:** PR #32 remains draft/unmerged with its reproducibility FAIL/HOLD. PR #31's exact sampled mathematical PASS remains independently supported but not native or source-independent regeneration certified. Historical PR #28–32 never merge into production main.
