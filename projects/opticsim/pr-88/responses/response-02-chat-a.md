# Chat A disposition — PR #88 independent R2 design re-review-02

**Author:** Chat A developer. **Not** Chat B, not a new independent verdict, and not an authorization to implement, release, merge or alter the native optical engine.

**Actual independent report:** [Chat B review-02](../reviews/review-02-chat-b.md), **PASS — DESIGN ONLY** for exact revised documentation-only head `391047a5467f8e27f7b2162074900e8387945b9f` on [draft source PR #88](https://github.com/physicsvigilante/opticsim/pull/88). Original [Chat B review-01](../reviews/review-01-chat-b.md) remains **CHANGES-REQUESTED** for original SHA `28c4aa94bbbf6b5a63a8bef433c80186e08a3d35`.

## B1–B5 dispositions

| Finding | Independent reviewer conclusion | Developer action / held boundary |
|---|---|---|
| **B1** mandatory v9 gate before neutral observer | **Resolved at design level** by separate Stage 0 research, possible Stage 1 **opt-in noncertifying diagnostic**, possible Stage 2 mandatory policy only after new approval | Keep Stage 1 **advisory only**, no automatic measurement withholding. Unique native-calling owner; exact delegate/return invariants and capture-failure negative tests required if separately implemented; critical observer neutrality is not proven by cross-run comparisons |
| **B2** forward t/u cannot validate actual native-reported point | **Resolved at design level**, point-agreement error envelope unproven | A future code result cannot claim `checked` without independently computed `P*` matching native-reported incident location within an independently justified/validated error envelope; otherwise `unknown`. Explicit false (10,7) versus true (10,5) counterexample and computed-point endpoint/corner tests |
| **B3** inconsistent publication surfaces | **Resolved conceptually as a counterfactual Stage 2 matrix** | Keep true native terminal status separate from audit and trusted measurement fitness. Stage 1 advisory UI must conspicuously state canonical native values remain **not independently certified by diagnostic** when contradictory; **never implement Stage 2 atomic withholding without a separate policy/R2 decision** |
| **B4** 128 hit cap/limited Fresnel, source and browser evidence | **Resolved as unproven diagnostic limit with mandatory future tests**, not a validated physics bound | Stage 1 implementation must test 128/129, 1–4 sources, 0–2 detectors, full-Fresnel true and false, weak/truncated cases, BigInt time/space and browser budget; never silently accept clipped events |
| **B5** hook coverage false zero | **Resolved as proposed preflight/ownership contract**, not demonstrated correct code | Require exact source/Glass/detector instance-to-native-handler installation and terminal identity, one real source start/returned ray, same-run event count, and bypass/nonrecording/zero-hit negative controls. Self-counting meters are not independent evidence |

## Verifiable status

- Source [PR #88](https://github.com/physicsvigilante/opticsim/pull/88) remains **draft, unmerged**; production `main` remains `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`. Upstream pinned PhyDemo unchanged at `811f508d2b070898c241a568b0c167dcb8645251`.
- Revised-head GitHub existing CI **11/11 workflows passed**, including [unified run 43757031446](https://github.com/physicsvigilante/opticsim/actions/runs/43757031446). This is documentation-only source revision (one markdown file +60/−22) and tests no novel Stage 1 numerical safeguard.
- The independent reviewer inspected the exact one-file diff and CI summaries; **did not execute new native, browser or offline numerical tests** in review-02. Chat A does not attribute historical Chat A native CI to an independent reviewer execution.
- Historical failures [43752308258](https://github.com/physicsvigilante/opticsim/actions/runs/43752308258), [43752585277](https://github.com/physicsvigilante/opticsim/actions/runs/43752585277), [43752839859](https://github.com/physicsvigilante/opticsim/actions/runs/43752839859) remain retained. Uninstrumented critical native run-to-run variability and near-critical represented-line inconsistency remain **observations requiring caution**, not fixed defects.

## Release disposition

**Recommend an explicit owner decision about Stage 1 only**, with a new branch from current `main`, initially a noncertifying opt-in diagnostic constrained to already admissible v9 scenes. Do **not** merge docs/research PR #88, carry its temporary workflow to production, alter PhyDemo, auto-replace existing results, or begin Stage 2 mandatory withholding. A new Stage 1 candidate would need actual native and Chrome failure-injection evidence, 11/11 exact-head CI, a **fresh independent R2 implementation/code review**, and a separate owner merge approval. **Design pass is the end of the design-review gate, not permission to ship a feature.**
