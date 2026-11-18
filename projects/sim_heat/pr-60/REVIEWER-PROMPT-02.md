# Chat B — SIM_HEAT PR60 targeted F-01 correction review 02

This is a **targeted R2 PRE-NATIVE DESIGN re-review** within the existing PR60 scope, not a new whole-project audit. Preserve your original review-01 (CHANGES REQUESTED on old HEAD469ab08...) unchanged. No native operation or source merge is authorized.

**Source:** https://github.com/physicsvigilante/sim_heat/pull/60
**Exact NEW HEAD:** `58ca02b293f2afbd931ab7ad1832fc4e34df1574`
**Git tree:** `c31fe1a37a598f30fa5859227a3ccbc5abf5c470`
**Pinned main:** `f52613c39c539b2d4543a9838e5658d526fca10e`
**Successful synthetic PR checkout:** `0c6f885043a2cdc813f2e82991bedbef822716a2`, same entire tree, parents main then new HEAD.

Read the complete correction request:
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-60/CORRECTION-REQUEST-02.md

Then inspect the exact five-file corrective diff: N1 REFERENCE-CONTRACT.md, plan.json, check_plan.py, tests/test_plan.py and plan CI. Original model/study/notes, production H1/reference/Modelica/viewer/runner, numeric policies and historical C1 are unchanged. Full PR still has twelve additions relative to main.

**F-01 correction to challenge:** all fourteen static C/G/A exports now have a prospective two-level arithmetic ledger. Level P is exact source mathematics with independent rational Pi enclosure and remains the **mandatory** physical delta<=epsilon/100 target. Level R records independently computed RN-even binary64 operation trees. Matching R is only representation consistency; it cannot hide R-to-P error or replace physical accuracy. Keep native64ULP and reference100x requirements unchanged; no exemptions, fitted thresholds, native-output-selected targets or silently adopted constants.

The old checking centres still **REFUSE** physical100x for seven exports: T02.G,T06.A,T06.G,T07.G,T08.G,T10.G,T_Plug.C. Explicit eighth execution blocker retains this failure. Reproduce T10's3.275x discrepancy, parsed-input warning and T06.A/G one-ULP order differences; none are observed native results. Check exact RN-even/Pi, all-export coverage and negative controls.

The checker shows mathematically correctly rounded physical-centre **feasibility witnesses**, but they are **not adopted checking values**, not reference-bundle replacements or full trajectory certificates. Any future use requires a separately versioned/reviewed checking implementation, complete dynamics/integral bounds, new N1-only seals and exact runner binding. No current native-readiness claim exists.

**Exact new-head CI:** push44376836623, PR44376848205, audit44376847910 all SUCCESS. Plan jobs each **34 focused+152 H1=186 unit passes**, docs parity, all zero-native/false-readiness/eight-blocker assertions intact. Artifacts14460713898/14461696589/14462475448 have verified SHA256 and CRC/source-tree details in the full request; audit preserves six original archives BYTE_IDENTICAL without native execution. Attribute personal tests separately from hosted inspection. A green plan regression that correctly reproduces refusal is not physical certification.

Write your own NEW report:
`physicsvigilante/review_sandbox/projects/sim_heat/pr-60/reviews/review-02-chat-b.md`

Verdict **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, specifically for this F-01 design correction. Distinguish a resolved arithmetic specification from the still-failing current checking values and absent full certificate/runtime/comparator/one-shot controls. Do not reopen already accepted source fidelity without a concrete new discrepancy.

**Stop:** no OpenModelica installation/query/build/launch, native runner, source merge, frozen-reference regeneration, C1 historical integration, diagnostic promotion or deployment. PR60 and evidence-only PR59 remain draft/unmerged; future native permission requires a separate explicit owner decision after complete readiness evidence.
