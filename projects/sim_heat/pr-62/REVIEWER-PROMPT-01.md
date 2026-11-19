# Ready-to-paste — independent Chat B R2 review of new H1-N1 interval code, PR62

You are **fresh independent Chat B** reviewing the NEW numerical checking implementation, not the prior reviewer of the PR60 design and not the separate LLM author. One consolidated R2 numerical/source-fidelity/evidence review. **Do not perform native OpenModelica calls.**

**Source candidate:** https://github.com/physicsvigilante/sim_heat/pull/62 — **DRAFT, stacked on still-draft PR60, DO NOT MERGE**.

**PIN:** exact source HEAD `12bb67e7abac54c8a2488109cb706d779c61bf93`, complete Git tree `bde985adb097d463627cfd6278b7f80f0b45ef10`. Base is PR60 HEAD `58ca02b293f2afbd931ab7ad1832fc4e34df1574`, complete tree `c31fe1a37a598f30fa5859227a3ccbc5abf5c470`. GitHub synthetic PR checkout `28a69478310d5fb2566d9621a450765654b1b88c` has identical tree, parents base then candidate. Only **four newly added files** in this PR; H1 Modelica/production physics/viewer/numerics/old reference/archived C1 unchanged.

**Read the COMPLETE central review request FIRST:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-62/REQUEST.md

Then inspect exact pinned `qualification/h1_n1/certified_reference.py`, `tests/test_certified_reference.py`, `INTERVAL-REFERENCE-V1.md` and the new offline workflow; compare to PR60's already independently reviewed `REFERENCE-CONTRACT.md`, `check_plan.py`, `plan.json`, original `reference-facts.json`, author model/study and original H1 numerical acceptance policies. Read source AGENTS and central review policy.

**Independently challenge**: full Schur source topology, exact-decimal + rational-Pi provenance, fixed-point interval signs/division and outward rounding, seven-state augmented exp, rho<=1/2 and exact Taylor remainder, repeated matrix-interval enclosure, full-grid 77 native export ID meanings /8 public requests /5 flow integrals, signed energy/flow balance, conservative true 100x per-quantity acceptance bounds, rounding to output floats, and negative/adversarial controls. A five-time mpmath cross-check is NOT a proof; personally reproduce decisive arithmetic cases when feasible.

**Verify actual hosted CI:**
- Push https://github.com/physicsvigilante/sim_heat/actions/runs/44462528376 **PASS**, artifact `14500473424`, SHA256 `3d181bff0452189c3cd4117bd3b86e2e2b50bd9e6b539c77340ca8d86775e8d5`.
- PR https://github.com/physicsvigilante/sim_heat/actions/runs/44462629831 **PASS**, artifact `14501215246`, SHA256 `b01f3acc0cf6d9373c7f520ad0c7bafbe1bdc217d5f7623c94b83d8aef228ff0`.
- Each: **11 new +34 existing plan +152 H1 =197 passing tests**, both sample grids (2401/4801), 77 internal /8 public/5 integral mathematical reference candidates; original eight readiness blockers remain. Chat A rehashed/CRC-checked both artifacts and full Git trees, and read trace receipts. Distinguish personally run vs hosted-only evidence.

**Do not conflate outcomes.** New separate candidate has `mathematicalIntervalSelfCheckPassed=true` but `independentlyCertifiedReference=false`, `runtimeReady=false`, `nativeExecuted=false`, `nativeQualified=false`. Existing PR60 **seven static checking-centre REFUSALS** remain, and the old runner/reference bundle is unmodified. New checking values are not adopted and no actual native data exist. The original H1-T1 evaluator private key remains missing/**UNSEALED**.

**Publish ONE genuinely new independent report at:**
`physicsvigilante/review_sandbox/projects/sim_heat/pr-62/reviews/review-01-chat-b.md`

Give **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** and distinguish confirmed interval proof/defects, source/CI claims and unimplemented runtime/host/executable/adoption gates. Do NOT change source, run/install/query/build/launch OpenModelica, merge PR60/PR62/PR59, regenerate historic frozen references, claim a qualified native solution, or rewrite prior reviewer reports. Stop after posting; the owner can say **“review done”** in Chat A.
