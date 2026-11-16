# Paste into separate Chat B — PR #89 targeted R2 implementation re-review (round 2)

You are Chat B in a separate ChatGPT conversation, reviewing **actual code corrections** to the prior independently rejected Opticsim Stage-1 finite-hit diagnostic. This is not a new design review, Stage-2 policy approval, or request to merge.

**Central hub:** https://github.com/physicsvigilante/review_sandbox
**New follow-up request:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-89/FOLLOW-UP-02.md
**Original Chat B implementation review (CHANGES REQUESTED):** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-89/reviews/review-01-chat-b.md
**Chat A correction response:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-89/responses/response-01-chat-a.md
**Source draft PR:** https://github.com/physicsvigilante/opticsim/pull/89
**Original reviewed source HEAD:** `3f2d31aa19a851d92a8d1c46ede2249c52e0e223`
**NEW EXACT CORRECTED SOURCE HEAD:** `e8889ce9a3771d4079d7f50070f341cbe5cddaa9`
**Production base/main:** `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`
**Exact old→new 4-file diff:** https://github.com/physicsvigilante/opticsim/compare/3f2d31aa19a851d92a8d1c46ede2249c52e0e223...e8889ce9a3771d4079d7f50070f341cbe5cddaa9
**Red test-only native/Node CI:** https://github.com/physicsvigilante/opticsim/actions/runs/43832903891 (764/766, two F-01/F-02 failures)
**Corrected full CI:** https://github.com/physicsvigilante/opticsim/actions/runs/43833318184 (11/11 workflows; 766/766 Node)
**New native ZIP:** https://github.com/physicsvigilante/opticsim/actions/runs/43833318184/artifacts/14209911320
**New real-Chrome ZIP:** https://github.com/physicsvigilante/opticsim/actions/runs/43833318184/artifacts/14209213388

1. Read central `PROTOCOL.md`, `REVIEW-RISK-POLICY.md`, frozen original PR #89 review-01, new FOLLOW-UP-02.md, pinned source `AGENTS.md`, and the **NEW exact 4-file source diff**, not a floating branch. Verify original first review remains changes-requested at the old SHA. Don't trust Chat A's disposition without re-checking.
2. **F-01:** independently execute or inspect the source-level original near-parallel input (x≈10−10⁻¹², ray dy≈−1 on vertical x=10 edge), translated case, shallower case and well-conditioned forward control. The new `sqrt(Number.EPSILON)` normalized angular sine boundary is a **deliberately conservative numerical-conditioning refusal**, not a validated physical grazing threshold, native cutoff, or proof of full optical correctness. Look for false clean, vector sign/units and avoid treating a possible valid shallow ray returning unknown as physical error.
3. **F-02:** inject missing/nonfinite/degenerate `SingleRay` newRays objects, duplicated emitted identity and a valid real ray in a true zero-hit run. A reported native source meter `emitted=1` with `newRays:[{}]` must NOT result in `checked-no-hit`. Require direct valid p1/p2 identity without creating/reconstructing any ray, and preserve exactly one original native source delegation and default outputs.
4. **F-03:** check that proven same-run finite-edge contradiction remains `inconsistent` despite a native warning; otherwise native warnings without a proved contradiction cause `unknown`. This precedence was clarified, not an optical model change.
5. Verify *actual* corrected GitHub CI, original red-before-fix failures, eight new public native and ten real-Chrome outcomes, 128/129 cap, old native measurement stability, raw exports, A→B→A guards. The same physical critical case had **six actual callbacks** in corrected CI versus five earlier; inter-run critical variability remains, no new route is invented. If possible independently rehash GitHub ZIPs. **Do not claim native tests you didn't personally run**.
6. If helpful, run novel test-only probes in an isolated scratch branch *based on the exact corrected SHA*, never touch production PR source. Pin any test SHA, original test failure and actual execution; do not change authored optical inputs to force a desired result.
7. Submit your **NEW independent report** under `physicsvigilante/review_sandbox` at `projects/opticsim/pr-89/reviews/review-02-chat-b.md`. State **pass / changes-requested / insufficient-evidence** for the **TARGETED R2 IMPLEMENTATION** at exact revised SHA. Include concrete severities, evidence actually executed, residual risks and smallest further test. Do not overwrite `review-01` and **DO NOT MERGE** PR #89, #87/#88 or any review-only branch.

Return the published review URL. The owner can then say **“Review complete”** in Chat A. Even a targeted pass does not authorize Stage-1 merge or Stage-2 mandatory suppression.
