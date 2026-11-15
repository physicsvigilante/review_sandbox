# EM Fields PR #13 — R2 independent review request

- projectId: `emfeeld`
- sourceRepo: `physicsvigilante/emfeeld`
- sourcePR: https://github.com/physicsvigilante/emfeeld/pull/13
- baseSha: **`c67d1115ad6fc982f29fe113583430e676938902`**
- headSha: **`766633a60679208f534c5d299578b100d2d29eea`**
- sourceTreeSha: **`6b10046d4b3b1f8480f53b59467b5cc84656960f`**
- CI merge-preview checkout: `30d84131709823b9fce5d4d29d0c8a19fb50a6ee` — **same tree** `6b10046d4b3b1f8480f53b59467b5cc84656960f`.
- reviewClass: **R2 — physical/evidence critical** (derived measurement and qualification semantics)
- Scope: first full separate-chat review of a *post-processing* ratio/separation capability; no modified physics laws or numeric solver.
- Current state: **awaiting-review**. Source PR **draft, unmerged**. No independent review claimed.
- Review report destination: `projects/emfeeld/pr-13/reviews/review-01-chat-b.md` (unique NEW file, authored by Chat B).
- Existing reviews: none; original Chat A attempts/commits remain in source PR history.

## Pinned source and requirements

Review **exact SHA `766633a60679208f534c5d299578b100d2d29eea`**, not floating main. Start with the source [AGENTS.md](https://github.com/physicsvigilante/emfeeld/blob/766633a60679208f534c5d299578b100d2d29eea/AGENTS.md), [derived design contract](https://github.com/physicsvigilante/emfeeld/blob/766633a60679208f534c5d299578b100d2d29eea/docs/DERIVED_OBSERVATIONS_V1.md), and [exact PR diff](https://github.com/physicsvigilante/emfeeld/compare/c67d1115ad6fc982f29fe113583430e676938902...766633a60679208f534c5d299578b100d2d29eea).

Review these files, in scope:
- `src/emfeeld/derived_observations.py` — only added production module.
- `tests/test_derived_observations.py` — 25 new tests and first failing test history.
- `tools/qualify_derived_observations.py` — E1/G1/T1 same-author checks.
- `.github/workflows/release-candidate.yml` — source CI extension.
- Trusted native evidence interfaces: `src/emfeeld/model_runs.py`, `src/emfeeld/observations.py`, `src/emfeeld/trajectory_samples.py`; existing `docs/PHYSICS.md`, `docs/VALIDATION.md`, `docs/TRAJECTORY_OBSERVATIONS.md`.

## Exact qualified CI and artifact identities

- **Linux+Windows fresh release:** https://github.com/physicsvigilante/emfeeld/actions/runs/43724035417 — both succeeded on this pinned head and CI merge preview. **Per OS:** 1,244 headless (includes 25 derived checks), 18 historical behavior, 33 real-PyVista; **1,295 completed tests per OS**. A historical all-file freeze assertion remains explicitly deselected, unchanged. The two platforms repeat the same cases, not 2,590 distinct capabilities.
- **Separate real-PyVista workflow:** https://github.com/physicsvigilante/emfeeld/actions/runs/43724035504 — succeeded.
- **Source snapshot:** https://github.com/physicsvigilante/emfeeld/actions/runs/43724035513 — succeeded, provenance only.
- Linux release artifact ID `14165479296`, name `rc-ubuntu-24.04-30d84131709823b9fce5d4d29d0c8a19fb50a6ee`, ZIP SHA256 `0c2fb874d84725a70fe3bc345a1035d541e3d18ca49d04ddff7eaa7efc92f8ca`.
- Windows release artifact ID `14165888630`, name `rc-windows-2022-30d84131709823b9fce5d4d29d0c8a19fb50a6ee`, ZIP SHA256 `174b21de4360ee0e565f5d82db99be594ac503a769dedf36cc552e377c49937a`.
- Downloaded both artifacts and **independently read-only audited** the exact SHA256 ZIP digest, sealed derived-file inventory, captured request SHA, native run SHA, packet SHA, named observation arithmetic, unit and time semantics. Both are 1,230-file artifacts; E1/T1 complete, G1 deliberately partial for one mismatched-time request while the valid separation remains available.
- E1 native field-magnitude ratio approximately **1.20110629666**. G1 ratio approximately **0.83184832278**, synchronized separation approximately **2.68691827999 m**, and intentionally unmatched time unavailable. T1 two static electric field-magnitude ratios approximately **11.7816091954** and **0.365853658537**. References are same-author ideal-source formulas and separate fixed-step RK4 for G1; not independently reviewed physics.
- The initial full *local* headless attempt timed out around 34%, **not a pass**. Subsequent focused local check: 192 passed with warnings as errors. Hosted full tests above are the release evidence. No historical fingerprints or tolerances were weakened.

## Expected source-backed behavior

A request pins a sealed, completed native run by exact run.json SHA256 and reads existing uniquely identified and recorded observations; never reintegrates or alters source evidence. It may request:
1. **Ratio** of explicitly selected, same-unit eligible scalar measurements: field/force magnitude, potential difference, saved speed or kinetic energy. Reject absolute electric/gravitational potential and reference-dependent potential/total energy ratios. Refuse zero denominator, nonfinite numbers, mismatched units, different saved trajectory times, missing/failed observations. Successful result dimensionless unit `1`; retain operands and evidence status.
2. **Separation** between distinct test bodies' successful saved position observations at **exactly the same actual physical time and saved sample index**. No interpolation or implied particle-particle forces. Result unit metres, null uncertainty bound.
3. Every unavailable derived request retains its ID, explicit reason and null value; a partial request batch cannot claim complete. Output request and native bindings are hashed; output inventory is sealed and reinspection performs only deterministic saved-result arithmetic.
4. Do not expand the physical source regime, change old model/sweep APIs, invent textbook givens, claim independent reference accuracy or imply classroom acceptance.

## Adversarial questions to answer independently

- Can a malformed source native result, wrong pin, tampered inventory or altered request falsely produce a completed derived report? Distinguish ordinary integrity checks from adversary-proof signatures.
- Can two records from different times/particles, incomplete source run, invalid selected samples or failed authored checks pass as valid observations?
- Are ratio eligibility, sign, units, potential reference dependence, zero/near-zero denominator, over/underflow, finite floats, and stable magnitude semantics defensible? Could an unexpected type or shape produce a false success?
- Is separation physically the Euclidean distance of distinct saved positions, and consistent with a separately implemented analytic/trajectory reference without introducing unmodeled interactions?
- Does the added CI verify new semantics with explicit negative controls, and do exact artifacts support what Chat A claims?
- If execution tools permit, author genuinely new adversarial test-only cases, either locally or on a separately pinned test branch; record exact code SHA and result. **Do not** modify PR #13 production or historical evidence.

## Known limitations / preservation

- Chat A corrected one source-evidence omission and finite saved-time validation in `680a860`. Initial attempted source remains `53cf57d`.
- Contract originally mislabeled the preselected static **electric** T1 arrangement as gravitational. Corrected and explicitly recorded in `766633a`, not relabeled as a new blind case.
- Separate formulas and tests share Chat A authorship. This review is a separately situated LLM context, **not necessarily a different model family**, independent human subject-matter expert, novel held-out corpus, or teaching-outcome evaluation.
- No new solver, viewer, time interpolation or partial-native-run salvage is included. Partial native source runs are refused at this boundary.
- Preserve first-review and negative test evidence unchanged. A new head after reviewer findings needs new CI and re-review only to the risk-appropriate extent.

## Reviewer output

Write a **new**, independently authored report at [`projects/emfeeld/pr-13/reviews/review-01-chat-b.md`](https://github.com/physicsvigilante/review_sandbox/tree/main/projects/emfeeld/pr-13/reviews/) in this central repository or a review-only PR, following [REVIEW-TEMPLATE.md](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-TEMPLATE.md). Outcome must be scoped **pass / changes-requested / insufficient-evidence**; include concrete reproduction, CI/source identities, unrun controls and separate interpretations of physics correctness, provenance and teaching usefulness. Never merge the source PR. The owner will tell Chat A **“Review complete”**, and Chat A will fetch your report from GitHub.
