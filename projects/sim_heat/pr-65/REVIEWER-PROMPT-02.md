# Ready-to-paste independent Chat B — SIM_HEAT PR65 R2 corrections R2-01 / R2-02

You are independent reviewer Chat B. Inspect **only two N4 checking-only admission corrections** (not the previously accepted source-physical arithmetic), with original findings anchored to exact old source SHA.

**Source draft PR65:** https://github.com/physicsvigilante/sim_heat/pull/65  
**EXACT corrected HEAD:** `f533d10fd38dc38710bba223e0bdb88f264e4398`  
**Full Git tree:** `a83cfce4fa303bbf173b6b0e387e9734cb3c5f8b`  
**Old rejected HEAD:** `a704e100d6760423b08cb07eca131ada8a629db2`  
**New fail-first tests-only HEAD:** `b11bfccf06f352ab6b93c57e8effa752e7519f4f`  
**Stacked PR64 base:** `0cf275241e718fbcd2b2d2c1f7761565c7c06a92` (still draft/unmerged)

**Read the FULL exact correction request FIRST:**  
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-65/CORRECTION-REQUEST-02.md

Also read [independent review-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-65/reviews/review-01-chat-b.md) and [Chat A response-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-65/responses/response-01-chat-a.md). Examine only old→new three N4-file changes, not a broad PR62/63/64 physics/reference audit.

**R2-01:** Old code accepted an ownerless **degree-one rod end**. New code counts actual rod-port incidences at every node, refuses any unowned node with fewer than two rod ports, while preserving valid degree-two junction, parallel rods, loops and isolated body. Personally attack steady and transient dangling rods and new graph variants, challenge distinct-neighbour vs physical-port counts and conservation implications.

**R2-02:** Old code admitted Modelica-reserved component names. New code keeps a standalone H1-parity reserved-word set applied ONLY to physical component names, not metadata study IDs or synthetic node labels. Personally test reserved instance names `model, flow, SimHeat, time`, plus valid names, `id=flow` and a node label `model`. Look for unexpected refusals or bypasses.

**Exact-head CI:** [PUSH 44512437693](https://github.com/physicsvigilante/sim_heat/actions/runs/44512437693) and [PR 44512447651](https://github.com/physicsvigilante/sim_heat/actions/runs/44512447651) both GREEN. Each ran 15 N4+12 N3+16 N2+17 N1 interval+34 plan+152 H1 = **246 DISTINCT OFFLINE tests**. First red [44512178952](https://github.com/physicsvigilante/sim_heat/actions/runs/44512178952) was deliberately preserved with one failure/one error. PR synthetic source tree exactly matches current HEAD. Preserve the original seven legacy physical-100× checking-centre refusals, eight native blockers and all false native/certificate status flags.

**Publish exactly ONE new independent Chat B report directly to:**  
`physicsvigilante/review_sandbox/projects/sim_heat/pr-65/reviews/review-02-chat-b.md`.

Verdict **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, pinned to corrected HEAD, personal negative/positive probes and honest limits. Preserve previous reviewer report unchanged. NO OpenModelica install/query/build/launch, native evidence/reference adoption, historical C1 rewrite or source PR merges. Owner may tell Chat A **“review done”** after publishing.
