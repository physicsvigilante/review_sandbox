# M36a — Narrow Chat B completion review prompt #04 (no production-source change)

You are Chat B, separate-context reviewer of [conductor_sim PR #84](https://github.com/physicsvigilante/conductor_sim/pull/84). **This is not a repeat of the entire JEE-30 physics review.** Your already published [review #02](reviews/review-02-chat-b.md) concluded **INSUFFICIENT-EVIDENCE** solely because its original hostile Python and binary PDF tamper probe had not actually been executed. It provided the complete 77-line original Python script in its report.

**Required initial reads:** [review #02](reviews/review-02-chat-b.md), [Chat A execution evidence response](responses/response-02-chat-a.md), [original reviewer-script preserved verbatim](probes/review-02-original-hostile-controls.py), and [GitHub run #44238910525](https://github.com/physicsvigilante/review_sandbox/actions/runs/44238910525). Check live GitHub rather than trusting Chat A's summary.

**Exact source review target:**
- Source PR: `physicsvigilante/conductor_sim#84`, DRAFT, unmerged until owner authorization.
- **Source HEAD** `527e6cee5f96a011729d2d0a668da9b688ab03d0`.
- **Native Git TREE** `fff1c03417c857b6cce04156427e3eeaf9919a65`.
- Released base `73e076cf7eaf7fefbae2b24afc1f54ff8f0b6fc6`.
- Review-sandbox execution workflow commit `545d71848a3fd686f238c522a47c00454be4197a`; [actual workflow source](https://github.com/physicsvigilante/review_sandbox/blob/main/.github/workflows/m36a-pr84-reviewer-controls.yml).

## Required minimum completion checks

1. Verify GitHub source PR HEAD and actual Git TREE are **still** the above and all actual current-head premerge CI remains **16/16 completed SUCCESS** (including entire historical 73-step Chromium workflow, both Python matrices, real FEMM 5), without rewriting old failing/cancelled attempts.
2. Confirm the review-sandbox CI job checkout truly asserted exact source HEAD and native TREE, not floating `main`; the 77-line script equals the ORIGINAL Chat B report #02's Python code, without alterations.
3. Read the GitHub-hosted job #44238910525 attempt #1 and its original test output. Confirm the legitimate 30-case audit passed, exactly **nine expected hostile ValueError refusals** occurred (three F-02 source/grouping, three F-03 local-3D route swaps, one F-04 metadata-collusion and two real independent copied-PDF midpoint byte flips), and the job ended `ALL NOVEL PYTHON CONTROLS PASSED` with full workflow SUCCESS.
4. Verify both source PDFs were **actually hashed from raw bytes** and matched literal pinned M21a SHA-256 values. If inspecting the artifact, note GitHub's reported digest and whether you yourself downloaded/rehashed it; do not falsely claim third-party signature.
5. Decide whether this actually closes the review #02's **only remaining independent-execution gap**. The implementer orchestrated the GitHub job, but the script was verbatim reviewer-authored and executed against independent pinned real source in a distinct `review_sandbox` workflow. Distinguish this execution model from interactive Chat B execution and human audit.

If any gate still unfulfilled, report **INSUFFICIENT-EVIDENCE** or **CHANGES-REQUESTED** with precise missing fact, not a guessed PASS. Do **not** add or modify production code, mark PR ready, merge it or authorize release.

## Publish distinct completion verdict

Write a **new** `projects/conductor_sim/pr-84/reviews/review-03-chat-b.md` to `physicsvigilante/review_sandbox` with actual source SHA/tree, live CI and original runner IDs, line-by-line hostile outcomes, previous F-01–F-05 dispositions, and **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE** scoped specifically to M36a's provisional *inventory and evidence* correction. Preserve review #01 CHANGES-REQUESTED and review #02 INSUFFICIENT-EVIDENCE as immutable history.

**Provisional JEE planning only:** 24 documented qualified routes, 3 partial, 3 unsupported, **ZERO** new 30-source-case physics simulations or original-question viewer validations. No `24/30 solved` or physics milestone claims.

Even a no-blocker reviewer PASS is **not merge permission**. Separate explicit owner approval, expected-head merge, exact reviewed tree and every real postmerge main-push check remain mandatory.
