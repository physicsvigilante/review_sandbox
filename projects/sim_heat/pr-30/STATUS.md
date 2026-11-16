# SIM_HEAT PR #30 — F-01 narrow negative-audit review

**Status: awaiting independent focused R2 review.** Source [PR #30](https://github.com/physicsvigilante/sim_heat/pull/30) remains draft/unmerged and historical-F0-only. Candidate exact HEAD `feeac951b3fc732c8e3885fbf6b637791cc7be94` based on reviewed PR #28 `baabeb3ed176f4d9fa83d6be09a58b4f21fa8319`. Original F0 baseline `dd8c9432abe97563414bb3ed809e61e673473812`.

**Scope:** 3 new audit/notes/CI files only, no edits to frozen H1/source model/study/checker/runner/reference/plan. The strict exported static value `hotLead.G` has only **80×** original sealed exact-arithmetic reference margin, short of required **100×**, and remains **FAIL/HOLD**. Hypothetical nearest binary64 value would give 320× but has **not** been sealed or substituted. A new host-local re-preparation yields a different seal from the archived original; this difference is openly recorded, **not** a retroactive source or artifact update. PR #28 Chat B had previously verified the actual archived original bundle.

**CI:** [#43911465414](https://github.com/physicsvigilante/sim_heat/actions/runs/43911465414) SUCCESS at exact source, [artifact #14247172858](https://github.com/physicsvigilante/sim_heat/actions/runs/43911465414/artifacts/14247172858), GitHub digest `a1f32660256f98c41eaab0edff409e1c7f3164b199df38c67fe2d63645160df8`. 23 pinned file checks, frozen 149 regressions, explicit negative F-01 check; zero OMC commands. Retain failed developer CI #43910999267, #43911134453 and #43911222494.

**Native gate remains `HOLD_NO_NATIVE_EXECUTION`.** No accepted correction to frozen F0 reference or native execution plan has been made, no 100× compliance claimed, no fully blind C1 or native acceptance. Future separately hashed checking reference and one-shot native source/host/run gating require distinct approval and review.

Reviewer packet: [REQUEST.md](REQUEST.md), [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md). Await Chat B independent new file `reviews/review-01-chat-b.md`; never create Chat B output as Chat A. Historical PR #28/#29 and this source PR #30 must not be merged to main.
