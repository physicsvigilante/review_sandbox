# SIM_HEAT PR65 — CORRECTION-REQUEST-02: targeted R2 review of open-rod-port and reserved-identifier admission

**Decision required:** SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE on two N4 fail-closed source-admission corrections ONLY, not a new broad physical-arithmetic review or native qualification.

## Pinned identities, historical evidence and exact diff

- Corrected [DRAFT source PR65](https://github.com/physicsvigilante/sim_heat/pull/65): HEAD **`f533d10fd38dc38710bba223e0bdb88f264e4398`**, complete Git tree **`a83cfce4fa303bbf173b6b0e387e9734cb3c5f8b`**, stacked on still-draft independently design-reviewed PR64 base **`0cf275241e718fbcd2b2d2c1f7761565c7c06a92`**.
- Original [independent review-01](reviews/review-01-chat-b.md) authored blob **`0a2f14619da7e2017446171cba279df65ffebdd4`** returned **CHANGES REQUESTED** for OLD HEAD **`a704e100d6760423b08cb07eca131ada8a629db2`**, tree `b3e3036622639814f830470dcd8319ffd70a7761`. Preserve that historical report unchanged.
- New fail-first TESTS-ONLY [commit `b11bfccf...`](https://github.com/physicsvigilante/sim_heat/commit/b11bfccf06f352ab6b93c57e8effa752e7519f4f) reproduced both issues on unchanged implementation in [RED push CI 44512178952](https://github.com/physicsvigilante/sim_heat/actions/runs/44512178952): one open rod-end without refusal and one missing reserved-word guard. Positive composition tests already passed. First-red logs/artifact preserved.
- New single [corrective commit `f533d10f...`](https://github.com/physicsvigilante/sim_heat/commit/f533d10fd38dc38710bba223e0bdb88f264e4398) changes exactly THREE N4-only files from old reviewed head: `static_physical.py`, tests and README. PR synthetic merge `ad37f358dce61d53a98e879cde15ba8a75787e74` has **exactly same full source tree** as corrected head, parents [PR64 base, current PR65 HEAD]. Production `h1/`, `tools/`, old references, Modelica, N1/N2/N3, original T1-T facts/model/study, C1 and main untouched.

## R2-01 attack: explicit physical rod-end incidence

Original static checker admitted a rod `a=Hot, b=Free` where `Free` was unowned with **one** rod endpoint, because it appeared in `used` and a connected component intersected a thermostat owner. Independently observed steady and transient dangling endings had `PASS_CANDIDATE_NOT_NATIVE_QUALIFIED` values despite the H1 public component contract refusing open ends.

Corrected `parse_facts` builds `port_incidence` from each actual rod end (not unique other-neighbours), requires **>=2 rod ports for EACH unowned node**, and preserves other anchors. Challenge a steady boundary→dangling rod, transient body→dangling circular rod, multiple disconnected assemblies and any case with one port at an ownerless node, including a parallel-port trick. Verify **valid degree-two ownerless junctions, parallel rods, closed loops and an isolated body** still admit. Do not invent a physical boundary to make a failing case pass. A rod endpoint attached to a body or maintained boundary may have degree one.

## R2-02 attack: physical component identifiers, not metadata labels

The old N4 `_ident` regex accepted rod instance `model`, conflicting with production `h1.model.identifier`. Corrected source defines a standalone `COMPONENT_RESERVED` set and `_component_ident`, used **only for body/boundary/rod instance names**; tests require exact set parity with existing H1 `RESERVED`. Independently challenge `model, flow, SimHeat, time, class, Real, false` for all three instance categories and check that a normal name is admitted. Distinguish graph node labels and study metadata IDs: `id=flow` and node `model` must **NOT** be rejected just because those labels are not Modelica instance names. Investigate inadvertent collisions or wrong mutation paths.

## Unchanged physical math and evidence boundaries

Spot-check the original source-exact 14 C/G/A physical candidates, rational Machin Pi, RN-even, 0.64 ULP physical reference error, immutable T1 source SHA and no arrangement-specific arithmetic. The original independent reviewer already found no mathematical defect, including independent 493 tie cases, 14 source witnesses and a genuinely different graph. A new full thermal proof is not necessary unless source changes invalidate it. All reference outputs still require exact input bytes/SHA and remain `sim_heat.h1_n4.static_physical_candidate/1`, not a runner-consumable `reference_bundle/2` or complete dynamic reference.

**Hosted checking-only evidence:** corrected [PUSH 44512437693](https://github.com/physicsvigilante/sim_heat/actions/runs/44512437693) and [PR 44512447651](https://github.com/physicsvigilante/sim_heat/actions/runs/44512447651) both SUCCESS, each **15 N4 +12 N3 +16 N2 +17 N1 interval +34 N1 plan +152 H1 =246 distinct tests**, docs parity, seven old 100× static refusals, eight native blockers and zero native calls. Sources on exact HEAD and PR checkout have same entire tree. GitHub artifact ZIP digests reported, not personally rehashed by Chat A.

**Required reviewer output:** one independently authored new `physicsvigilante/review_sandbox/projects/sim_heat/pr-65/reviews/review-02-chat-b.md` with exact HEAD, own adversarial controls, source and status limits, verdict SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE. Do not overwrite review-01 or edit implementation during independent review.

**STOP:** PR65/64/63/62/60/59 all DRAFT/UNMERGED. No OpenModelica installation/version query/build/launch, native output, certified dynamic reference, untrusted source promotion, historical C1 edit, production merge/deployment or claim to recover H1-T1's missing private scorer.
