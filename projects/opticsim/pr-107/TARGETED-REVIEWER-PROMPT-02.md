# Chat B — targeted R2 follow-up of Opticsim PR #107 (F1/F2 only)

Act as a **separate independent reviewer**. The prior separately authored review is [review-01-chat-b.md](reviews/review-01-chat-b.md). Its verdict was **INSUFFICIENT EVIDENCE** without a confirmed source defect. **Do not change that original report.** This follow-up is limited to testing its F1/F2 evidence gaps, safety gates and test-only scope.

## Exact candidate and isolation

- Production admission PR: https://github.com/physicsvigilante/opticsim/pull/107, **still draft/unmerged**.
- **Current exact candidate HEAD:** `fe3a030be7bfba8e5808e4e1e2e66d6815e7add7` (a merge of test-only [PR #108](https://github.com/physicsvigilante/opticsim/pull/108) into the previously reviewed v14 branch).
- Previously reviewed PR #107 commit: `3c1bcc317689386333c4155ee414f8fa99a1caea`.
- Test-only PR #108 final test commit: `1074f1be19656ee7e0ffc3ea52fce3c517836ff5`.
- The original pinned PhyDemo release is `811f508d2b070898c241a568b0c167dcb8645251`. Do not change native core, seed, thresholds, physics, or accepted-result policy to make tests pass.
- The source delta from the first reviewed commit must be **only** `test/two-glass-r2-review-regressions.test.mjs` plus the merge commit. Confirm this independently via GitHub compare/file diff, rather than relying on Chat A's claim.

## F1 — native two-glass full Fresnel, truncation and withholding

Inspect the test directly at the exact candidate HEAD. Both bodies are `partialReflection:true`, with a 10° authored incident ray and shared exterior index 1.

Check at minimum:

1. A first real G1 event yields two genuine native branches, with incident relative power `0.5`, transmitted `0.4799922574927362` and reflected `0.020007742507263775`. Independently calculate unpolarized Fresnel reflectance for n=1 to n=1.5 at 10° (approximately `0.04001548501452753`) and compare to the native reflected fraction. Verify native outgoing reflection direction and Snell transmission.
2. G2's first real event has incident relative power `0.4607864858766648`; transmitted branch `0.4529440199529672`; a weak reflected branch is **not** propagated and its native `nativeTruncation` is **`0.007842465923697658`**, not a physical-zero claim. Do not assume equal s/p polarization downstream of G1.
3. The complete native diagnostic reports `status=incomplete`, accumulated truncation `0.016320925290886495`, no undefined events in the observed run, and **all three requested results suppressed**. An independently depth-limited case also withholds all requested values. Check both that the test enforces these properties and that the implementation does not silently qualify a truncated Fresnel result.

These values are **source CI-observed diagnostics on the test-only commit**, not an independent rerun. Verify they remain true at the new feature HEAD.

## F2 — independent native internal TIR then face exit

With the ordinary two-glass fixture unchanged except a source at `(340,-50) mm` directed 60°:

- G2 first right-face incident at `(350,-32.6794919243) mm`; `n=1.3 -> 1`, critical angle approximately 50.28486°, so 60° incidence is TIR. The native event must report actual `total-internal-reflection`, source inside G2, and no transmitted first branch.
- The reflected ray reaches the **different top face** at `(273.397459622,100) mm`; actual native transmission angle must agree with independent Snell reference **40.541601874°**.
- G1 must have **zero** interactions, with no route invented in the authoring or test harness. The complete native run exposes qualified sampled counts but no physical imaging claim.

## F3 (optional) and regression isolation

The reviewer also suggested an explicit conservative diagonal 20×20 mm square separation case: centers `(0,0)` and `(20.008,20.008)` are Euclidean >0.01 mm apart yet lack a >=0.01-mm full supporting-face certificate, so rejection is intentional. The test-only follow-up includes this refusal plus a positive 0.011-mm face-margin control.

Verify that old v1–v13 contracts, golden results, native-vendor files, source SHA freeze and original Stage-2 measurement-withholding rules remain unchanged.

## Execution evidence and independence

The source test commit `1074f1be...` passed **806/806 Node 24 tests**, **11/11 standard workflows** and retained real-Chrome scenarios. **Separately, on exact current PR #107 HEAD `fe3a030be7bfba8e5808e4e1e2e66d6815e7add7`**, all **11/11 standard workflows succeeded**. [Exact-head unified Node 24 run (806/806)](https://github.com/physicsvigilante/opticsim/actions/runs/44024873262) and [exact-head planar/real-Chrome run with `R2_F1_NATIVE_EVIDENCE` and `R2_F2_NATIVE_EVIDENCE` logged](https://github.com/physicsvigilante/opticsim/actions/runs/44024873455). Verify actual head_sha and run conclusions independently; do not confuse source CI with a new independent reviewer execution.

If able to run a fresh supported checkout, use Node >=24.19 with the pinned upstream, run `npm run setup`, `node scripts/build.mjs --test`, then `node --test test/two-glass-r2-review-regressions.test.mjs`. Recompute independent scalar Fresnel/Snell and geometry facts; do not treat source unit tests alone as independent reproduction. If the environment cannot run the native core, disclose this limitation explicitly. Do not claim new browser evidence unless actually executed by you.

## Independent report

Write a **new separately authored report** to `projects/opticsim/pr-107/reviews/review-02-chat-b.md` in the `physicsvigilante/review_sandbox` repository. Identify the exact reviewed source HEAD, distinguish independently executed calculations from source GitHub CI, and give an explicit verdict:

- `CLEARED FOR OWNER DECISION` only if F1/F2 evidence and branch safety are now sufficient (with any residual limitations stated);
- `INSUFFICIENT EVIDENCE` if uncertainty remains;
- `CHANGES REQUESTED` if a substantive new defect is demonstrated.

Do not merge source PR #107 or misrepresent the reviewer as a human optics expert. Independently reviewed approval and owner authorization are separate release gates. Focus on engine capability, not LLM answer-format completeness or teaching outcomes.
