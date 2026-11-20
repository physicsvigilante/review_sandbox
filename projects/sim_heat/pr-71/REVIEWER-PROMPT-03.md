# Ready-to-paste Chat B — SIM_HEAT PR71 pending-baseline R2 review-03

You are independent Chat B. Review ONLY the remaining PR71 **F-01 source-only teaching UI pending-baseline timing blocker** from independent review-02. That review already PASSED F-02 source study/model SHA binding and F-03 component SI input/provenance completeness; do not re-open accepted physics or those fixes absent a new concrete dependency defect.

**Source DRAFT PR71:** https://github.com/physicsvigilante/sim_heat/pull/71
**EXACT corrected HEAD:** ae044ccad6bf58c171c9cc834b427b34cb892101
**Whole Git tree:** cc06d37a27f3fb65e3acd0d60d58e36e266a6a60
**OLD review-02 CHANGES REQUESTED head:** 9199e695f5aae410cb8d0e89f463b3b1b6e57c15
**Tests-only RED head:** 79ee34687b89357ce2a6e1a1d9835393b10c2559
**Scoped-reviewed but DRAFT PR70 base:** c2bd9ce63a6d725fdcd63d2d5d7c5416c7843739
**PR synthetic checkout:** f0d02b337b0afb554ca895aa67e3665cef1a102d (same tree, parents [PR70, corrected PR71]).

**READ full review request first:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-71/CORRECTION-REQUEST-03.md

Read the previous [independent review-02](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-71/reviews/review-02-chat-b.md) and [Chat A response-02](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-71/responses/response-02-chat-a.md). Old-reviewed to new-source diff changes ONLY viewer/source_preview/app.mjs and tests/browser_authoring_workbench.py. The old H1/Modelica physics/native runner, original source and archived C1 remain untouched.

**Case A:** Hold a valid S1 baseline File.text read while admitting a D1 source-only scenario. Verify queued latest D1 visibly waits until S1 admits, then comparison identity, graph/details/requests and controls are S1 baseline / D1 scenario, with no endless Checking.

**Case B:** Delay initial TEACH_SPLIT3 baseline fetch (workbench serves admitted D2). Select user scenario D1 before the baseline arrives. It must remain the chosen scenario when baseline D2 admits, and the server-default D2_K2 must NOT overwrite D1, even after delayed responses. Verify source SHA identities, public requests all not_computed and false native claims.

**Adversarial:** invalid baseline while queued, second scenario during baseline pending, pending scenario from old baseline generation, stale/default VARIANT response, invalid user JSON, and previous loaded A→B→bad C and slow-A/fast-B. Confirm no stale graph/provenance/requests, no dangling Checking and no unhandled async errors. Browser-uploaded data is display-schema checked, not independently original-Modelica-source authenticated.

**Actual evidence:** tests-only [RED PUSH 44669151018](https://github.com/physicsvigilante/sim_heat/actions/runs/44669151018) and [RED PR 44669155472](https://github.com/physicsvigilante/sim_heat/actions/runs/44669155472) fail on first missing waiting state against unchanged app; corrected [PUSH 44669547472](https://github.com/physicsvigilante/sim_heat/actions/runs/44669547472) and [PR 44669553291](https://github.com/physicsvigilante/sim_heat/actions/runs/44669553291) both SUCCESS, 327 collected/326 PASS/one optional skip plus real HTTP Chromium pending-case screenshots and six OFFLINE diagnostic archive replays. Push artifact SHA256/CRC/tree independently checked by Chat A, not Chat B; distinguish personally executed adversarial probes from hosted logs.

**Publish exactly ONE NEW independent review report to:**
physicsvigilante/review_sandbox/projects/sim_heat/pr-71/reviews/review-03-chat-b.md

Verdict SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE pinned to this exact head. Preserve reviews #01 and #02 unchanged as historical CHANGES REQUESTED. No OpenModelica install/query/version/build/launch, native result/reference promotion, original C1 rewrite, owner source seal, PR merge or deployment. All relevant PRs remain draft/unmerged, seven old physical checking-centre failures/eight native blockers still active. Owner may say “review done” only after your report is committed.
