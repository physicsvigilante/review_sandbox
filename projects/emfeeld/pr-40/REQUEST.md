# EM Fields PR #40 — independent R2 review request, project-wide audit

**Author request, not independent verdict. DRAFT/UNMERGED.** Current candidate is [PR #40](https://github.com/physicsvigilante/emfeeld/pull/40), tracking [Issue #39](https://github.com/physicsvigilante/emfeeld/issues/39). No reviewer PASS or new release qualification is claimed here. Hosted CI must finish and original archives must be inspected before an archive/OS qualification claim.

## Immutable source

- Released base/main: `066c94e4953c3ef29302c0bb6d0ee2f6cb8b8ca0`; tree `33b58fb55b387ec2b7c1bdd61bf1af7764db97cd`.
- Candidate head: **`9fa09dec92b8925591505d1da0bc2639a53a30d9`**; exact tree **`9491d39d3f0415a5e90f1848173cf73af5d02584`**.
- Branch `fix/project-audit-evidence-numerics-20261117`; one commit; 21 changed paths, 371 tracked files, 30 engine Python modules (new shared output safety helper). Each uploaded file blob was compared to the exact locally tested bytes. Independently built local/remote trees matched. A full patch applied to a fresh original baseline reconstruction also produced this exact candidate tree.
- [Detailed source audit and capability/forward plan](https://github.com/physicsvigilante/emfeeld/blob/9fa09dec92b8925591505d1da0bc2639a53a30d9/docs/PROJECT_AUDIT_2026_11_17.md).

## Reproduced issues and scope

1. Public writers could create fresh output within existing sealed evidence and invalidate its original inventory. The new `protect_saved_evidence` is a no-write preflight applied across native model import/run/view, apply, study, observations, scene CLI, capabilities, sweep/derived/comparison/ensemble, question-first and replay writers. Test unrelated sealed roots, symlink-parent aliases, output equal to input, pre-store-mutation refusal, existing-directory exception compatibility, normal ordinary replacement and intended child outputs inside an unsealed active workflow. Recognizable roots include integrity inventories, stores, question locks, completed studies/replays/attempts. It is not a lock or malicious concurrent-filesystem guarantee.
2. Oversized JSON integers in analysis checks and display settings crashed before expected rejection. Existing finite float64 admission now precedes conversion. Confirm a readable rejected analysis with no native solver output, not a forged completed numerical result.
3. A parallel/antiparallel camera view-up basis was accepted. Confirm invalid basis is refused before renderer creation and valid finite camera settings still work.
4. Sphere potential evaluated an unused interior branch for an exterior point and overflowed despite a finite exterior answer. Confirm piecewise evaluation preserves the original analytic expressions, references, scalar/vector behavior and boundary continuity for electric and gravity cases.
5. Zero-strength tiny solid/shell field calculations unnecessarily divided by an underflowed cube. Confirm exact zero behavior without hiding nonzero-source singularity/overflow errors.
6. Captured full-scene trajectories bypassed the already-rejected saved-time grid. Confirm `unresolvable_time_grid`, `integration_attempted=false`, no solver call and no fabricated captured arrays.
7. Nonobject revision proposals crashed at `.get`. Confirm ordinary rejection occurs before proposal reservation or store writes.
8. Nonstring/unhashable entity ordering crashed. Confirm retained rejection without silently converting identities.
9. README/AGENTS now distinguish shipped features, this unmerged candidate, historical PR #1-only review exception and present review/release gates. Check capability claims against runtime code, particularly V1/V2 convenience apply versus V3 native support.

## Actual author execution (do not count as reviewer-owned cases)

Offline Linux CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, pytest 9.0.2; warnings as errors. Untouched reconstructed base: **1,585 passed**. Final exact published source full headless: **1,629 passed in 134.80 s**, including **44 new audit executions** (37 admission/output plus seven numerical). Historical behavioral: **18 passed, one obsolete all-file freeze guard deselected**. Published V6 replay **10 cases**, discovery replay **two cases**, Physics Demonstration **17 native observations /64 reference checks**, all passed. Compileall and diff whitespace checks passed.

Original negative evidence retained locally and supplied to the owner in `EM_Fields_Audit_Evidence.zip`: 15 first safety/admission failures, five initial numerical failures, separate original zero-strength sphere failures, seven additional malformed-input failures and one passing control. Intermediate correction had a FileExistsError-versus-ValueError regression, fixed without changing the historical test. Publication-time equivalent argparse keyword ordering was detected by Git-blob comparison and the final full suite rerun on exact bytes. These original local logs are not GitHub-hosted just because they are named here; do not claim you downloaded them unless the owner supplies the archive. Original new CI artifacts will be separately downloadable when finished.

**Local real PyVista was not run.** It is absent and isolated installation failed DNS/package retrieval; the attempt log is retained. The user machine was not changed. Old baseline viewer/Windows qualification does not qualify this changed source. Fresh exact-head [Linux/Windows workflow #44131680713](https://github.com/physicsvigilante/emfeeld/actions/runs/44131680713) and [separate real-PyVista #44131680696](https://github.com/physicsvigilante/emfeeld/actions/runs/44131680696) were observed IN PROGRESS; source snapshot also triggered by the PR. No fresh hosted PASS or original artifact audit claimed yet.

## Critical compatibility boundary

The field implementation bytes change; this is not documentation-only. Existing recorded studies that pin `fields.py` may correctly refuse viewing under the corrected implementation. Preserve original evidence and its pinned environment, or replay unchanged inputs into fresh outputs. **Do not rewrite old source receipts or numerical tolerances to force compatibility.** Current engine inventory is 30 modules, not the historical 29. No physical law or tolerance relaxation is proposed, but the floating-point/error-admission behavior is deliberately corrected.

No branch protection, license, dependencies or user Conda settings were changed. Main protection was disabled at audit time; administrative policies and license selection need separate owner decisions. Independent provider/withheld-judge trial #36 is still distinct and unrun.

## Independent review required

Read exact candidate diff and source. Derive and execute fresh adversarial cases, not just the author's two new test files. Include positive normal workflows and old sealed-evidence preservation, field analytic limits, overflow/zero/invalid-grid negatives, camera valid/invalid settings, malformed input and store immutability. Review all public writer integrations for premature side effects and unsealed-workflow compatibility. Audit fresh original source/Linux/Windows/viewer ZIPs for exact tree and actual native evidence after their jobs finish; retain first reviewer failures separately. Do not claim full corpus solving, human visual acceptance, general security or teacher usefulness.

Publish an attributable **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** report at `projects/emfeeld/pr-40/reviews/review-01-chat-b.md`, pinning head/tree, environment, commands, fresh cases and limitations. **Do not merge.** Owner-controlled guarded integration and new actual-main post-merge qualification remain separate gates.