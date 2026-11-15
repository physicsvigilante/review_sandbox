# Risk-based verification policy — minimize review work without weakening stability

The smallest adequate **independent review** is determined by *what changed*, not whether existing tests happen to pass. Deterministic checks remain necessary for every class. Batch related work into one coherent milestone and review **after** Chat A has done self-review, adversarial probes and current-source CI.

| Class | Typical changes | Required verification | Separate-chat review |
|---|---|---|---|
| **R0 — procedural** | docs, examples, packet updates, non-executable notes | diff and link/format checks; applicable CI | Not normally required |
| **R1 — bounded implementation** | optics-neutral refactor, UI layout without measurement-meaning change, narrow backward-compatible wiring | focused regressions, existing full CI when source changed; real browser checks for UI | **Focused review** if contracts, evidence presentation or behavior can change; otherwise not normally required |
| **R2 — physical/evidence critical** | new physics relation, inverse solver, native measurement, refraction/reflector behavior, numerical guard, source-interpretation or qualification semantics, runner provenance | pinned native tests, independently expressed numerical/geometry references, negative/refusal cases, historical fingerprints, full CI, browser evidence where applicable | **One full separate-chat review** of the completed milestone |

**Escalate** to R2 if a supposedly minor change changes the meaning of measured values, native completeness, source provenance, numerical thresholds, historical contracts, safety gates, or physics calculations. Chat A must not downgrade merely because CI is green.

**Correction policy:** fix confirmed defects with a new regression and new commit; rerun relevant full/current-source CI. Re-review **only the affected path** for a localized change unless it invalidates other physical/evidence assumptions. Substantial semantic changes receive a new R2 review of affected physical behavior. Do not automatically run repeated whole-project reviews for an unchanged pinned source. Unresolved blockers always prevent a sign-off regardless of the review budget.

**One review is the default budget, not a sign-off shortcut.** If Chat B reports `insufficient-evidence`, request narrow new evidence/test cases rather than broad repetitive prose. If an adversarial test cannot be executed, report precisely what remains unknown and ask the owner to accept explicitly scoped residual risk or retain draft status.

**Independent context limits:** Chat B should obtain original facts/source requirements and code from pinned GitHub refs, not from Chat A's desired verdict. A separate ChatGPT chat is not independent human expert evaluation, even if it offers useful adversarial scrutiny. Blind interpretation evaluations additionally require held-out references not revealed before first capture.

**Merge gate:** accepted source-specific CI, resolved blockers, accurate remaining limitations, current source SHA and separate owner approval. Central GitHub files do not automatically block or approve source PRs. Production merges and deployment are never implicit.
