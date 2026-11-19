# Ready-to-paste Chat B — SIM_HEAT PR70 independent typed snapshot review-02

You are independent reviewer Chat B. Review only the **R2-01 typed frozenset/set source-integrity correction** to the main-based SIM_HEAT PR70 audit. The old independent review #01 was CHANGES REQUESTED; the other maintenance findings were supported. Do not re-audit all earlier accepted changes unless this correction invalidates a premise.

**DRAFT PR70:** https://github.com/physicsvigilante/sim_heat/pull/70
**EXACT corrected HEAD:** c2bd9ce63a6d725fdcd63d2d5d7c5416c7843739
**Complete Git tree:** 3e71e670a8af88ef9661b29125407a2c9fe4139d
**Old review-01 CHANGES REQUESTED HEAD:** 3f718ce0f1bb3fbc75162f99862796e32d2b0752
**Tests-only RED HEAD:** 649e3d3b05f2276ab34d969dc1bf856f8b1e2869
**main base:** f52613c39c539b2d4543a9838e5658d526fca10e
**PR synthetic checkout:** 8643bf65443faf1fca3add0368e953572e8981f3 (identical whole source tree)

**READ FULL bounded correction request:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-70/CORRECTION-REQUEST-02.md

Review [original independent review-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-70/reviews/review-01-chat-b.md) and [Chat A response-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-70/responses/response-01-chat-a.md). Review only two changed files vs old HEAD: h1/study.py and tests/test_audit_regressions.py.

**Attack the actual API:** Start with loaded D1 Study anchored_nodes frozenset({0,1}), replace nested Topology anchored_nodes with frozenset({0,True}) using dataclasses.replace. Python set equality incorrectly treats these equal. Corrected \`_same_typed\` must return False, \`verified_snapshot\` and \`build_source_preview\` must refuse typed identity. Test direct set and frozenset collisions including \`frozenset({True})\` vs \`frozenset({1})\`. Test legitimate unordered set copies, unchanged D1/TEACH_SPLIT3/D2_K2, and other source/provenance/request/disk mutation refusals. Challenge the one-to-one match recursion and type exactness; do not assert a forged physical result that nobody reproduced.

**Hosted evidence:** Tests-only [source-preview RED 44582420338](https://github.com/physicsvigilante/sim_heat/actions/runs/44582420338) and [workbench RED 44582420385](https://github.com/physicsvigilante/sim_heat/actions/runs/44582420385) both failed exactly two new tests on unchanged comparator. Corrected [core 44582867852](https://github.com/physicsvigilante/sim_heat/actions/runs/44582867852), [source preview 44582868025](https://github.com/physicsvigilante/sim_heat/actions/runs/44582868025), [workbench 44582867906](https://github.com/physicsvigilante/sim_heat/actions/runs/44582867906) all SUCCESS. Source-preview/workbench suites: 315 collected/314 pass/1 optional skip, docs parity, six original archived outputs replayed, hosted Chromium browser interaction. NO native OpenModelica operations.

**Publish ONE NEW independent review directly to:**
physicsvigilante/review_sandbox/projects/sim_heat/pr-70/reviews/review-02-chat-b.md

State SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE on exact NEW HEAD; distinguish personally performed tests from hosted CI. Preserve review-01 unchanged. No OpenModelica version/install/build/launch, native MAT/reference promotion, original C1 rewrite, source PR merge or deployment. All related PRs remain draft/unmerged. Owner may say "review done" to Chat A after report publication.
