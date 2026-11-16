# M31b — Separate-context R2 independent reviewer prompt #01

You are **Chat B**, a separate-context reviewer of the **draft and unmerged** conductor_sim M31b PR #72, not its implementer. Review independently rather than adopting the developer's desired outcome.

**Source PR:** https://github.com/physicsvigilante/conductor_sim/pull/72  
**Exact candidate SOURCE HEAD:** `7c177e7da153992d963c966091c76ed12faab5a0`  
**Git TREE:** `23ea42ef39d2a3a67df4bb564398aa5727c828b5`  
**Base/main (released M31a):** `ec4f4f10ae6392335c8078cd7ecb0bc575addf04`  
**Frozen charter first commit:** `bb73766db681d1f15b1bfc843e87f58e8e52709b`

**Read first:** [full reviewer REQUEST](REQUEST.md), [status](STATUS.md), [central PROTOCOL](../../../PROTOCOL.md), [review risk policy](../../../REVIEW-RISK-POLICY.md), [review template](../../../REVIEW-TEMPLATE.md), [pinned source charter](https://github.com/physicsvigilante/conductor_sim/blob/7c177e7da153992d963c966091c76ed12faab5a0/docs/m31b_charter.md) and [M31b contract](https://github.com/physicsvigilante/conductor_sim/blob/7c177e7da153992d963c966091c76ed12faab5a0/docs/m31b.md). Query the actual live PR, Git commit tree and every CI run at its **exact HEAD**, and check project AGENTS.md if any. **If the source HEAD has moved, stop and report STALE-HEAD**, not a verdict on another revision. If any exact-HEAD CI remains pending, explicitly report it rather than inventing a success; full green CI is a release gate.

## What changed and why review is R2

New native M31b `CoupledEventPlan` and `run_coupled_event_family` combine **unchanged M31a atomic physical revisions** with **newly integrated real M24a event questions** on original, actual structural parent and coupled children. Source IDs and two-stage SHA parentage must remain intact. Only same-direction single resolved events in two duration-complete native M24a runs can be paired via unchanged M28b; preserved root brackets are finite-resolution numerical evidence, not ODE error bounds. Genuine source-guard/terminal/unresolved observations, physical versus event-study refusals and exact literal M24a sample clocks must not be confused. Public CoupledEventRun validates real typed results at constructor and before JSON export. No changed Coulomb/rod/gravity field laws, RK controller, event locator, FEMM, conductor response or HTML renderer.

Review [exact base→candidate diff](https://github.com/physicsvigilante/conductor_sim/compare/ec4f4f10ae6392335c8078cd7ecb0bc575addf04...7c177e7da153992d963c966091c76ed12faab5a0) and `src/conductor_sim/coupled_event_family.py`, `tests/test_m31b_coupled_event_family.py`, `examples/m31b_rod_reference.py`, `tools/m31b_independent_dop853.py` in detail. Use [REQUEST.md](REQUEST.md) for concrete adversarial and physics test cards and first-failure chronology.

## Run your independent challenges

1. **Native source identity and exact time/root:** independently design a fresh physical two-property hypothesis and detector/reversal, then run an authentic M24a event integration on actual revised model (if tools allow), and challenge with an independently written SI analytic or high-accuracy numerical reference. Distinguish true native execution from the developer's CI logs and from a standalone Python semantics reproduction.
2. **Scientific refusal and truncation:** authentic source guard with early root but unobserved far root, at least one multiple-/opposite-direction case, a parent event-study refusal on a physically admitted world with successful coupled child, and terminal/unresolved status semantics. Do not pair a censored whole-horizon root or invent later motion. Check structural inventory and original→structural→coupled hashes.
3. **Evidence integrity:** forge or mutate a typed EventRun/trajectory source, event question/policy, Boolean time 0.0, unknown termination and root; try constructor and pre-export checks. Inspect whether any bypass fits the declared typed-result contract versus excluded cryptographic trust boundary. If unexecuted, label it a predicted defect only.
4. **Provenance and CI:** independently confirm actual Git tree `23ea42ef39d2a3a67df4bb564398aa5727c828b5`, check completed full exact-head Python 3.10/3.12, 97 real FEMM, historical Chromium, and the 96-node independent Coulomb+DOP853 event transfer. Developer transfer predicts parent t=0.5529332751693772 s vs native 0.5529332747459412 s; coupled child t=0.4985157889191854 s vs native 0.4985157885551453 s. Don't assume developer reference automatically counts as separate Chat B independent calculation. Verify ZIP SHA256 reported in [CI #43941414594](https://github.com/physicsvigilante/conductor_sim/actions/runs/43941414594) if independently downloadable.
5. **Historical failures:** developer first test import collection failure at `344ce68c`; then invalid case ID test failure at `5b081405` (1898 other passes). Current `3799acf1` was 1905 green both Python interpreters, while current `7c177e7da153992d963c966091c76ed12faab5a0` adds numeric transfer/CI. Preserve failed attempts rather than relabeling earlier runs as PASS.

## Deliverable

Write a newly authored, separate-context report to **physicsvigilante/review_sandbox/main**:

`projects/conductor_sim/pr-72/reviews/review-01-chat-b.md`

Report **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE**, remaining blockers and smallest remedy, exact pin/tree, observed execution vs inspected source/developer CI, separate physics/identity/evidence judgments, and reasoned release advice. No source modification, PR approval, ready-state change or production merge by Chat B. Separate-context LLM review is not independent human certification.

If you cannot write to the review hub, say so explicitly and supply the report for the owner without claiming it was committed.
