# M35b PR #82 — Legacy M28a/M28b issued evidence correction release status

**2026-11-17: candidate DRAFT/OPEN/UNMERGED, developer/native physical validation complete, full PR CI still finishing, separate independent R2 review NOT STARTED/PUBLISHED. No merge authorization.**

- [Source PR #82](https://github.com/physicsvigilante/conductor_sim/pull/82): current frozen candidate HEAD **cb5eec5afb6a64b3cf11f00d2e38e85b5e6f3200**, actual native Git TREE **6d704170cde51c3959af3e78fd089490a0dc4663**.
- Released M35a main/base **808d7ce9245aaeda3f8f58faff7181776d20183a**, Git TREE **f9d14fedd06659f5abf8f822b31bc7e6353f2a37**, 17/17 literal main-push workflows passed.
- Frozen charter-only source commit **a37f510ce936a8027739798af42d52e92be378a7**.
- [FULL reviewer science and hostile evidence REQUEST](REQUEST.md) · [fresh reviewer PROMPT #01](REVIEWER-PROMPT-01.md) · expected independently authored report **reviews/review-01-chat-b.md** (NOT yet published).
- Original reproducible issue: [source issue #80](https://github.com/physicsvigilante/conductor_sim/issues/80), **OPEN** pending source correction/review/release.
- Scope: legacy M28a/M28b native result evidence and status integrity; NOT new conductor/field/equation, numerical ODE, moving source, 3D solver, scene graph or problem parser.

## Reproduced defect and candidate correction

The released old `TrajectorySweepRun` and `EventSweepRun` could have a physically complete result entry mutated with ordinary `dataclasses.replace` to `status='complete'` but absent source scenario/native observation and still export contradictory JSON. This is an evidence-meaning defect, **not** a demonstrated force/field/ODE calculation error.

M35b adds strict native status/model/termination/question/parent-revision and Float-typed SI clock validation at issued Run construction and **every detached export**, including public nested mutation after issue. The run is bound to the exact original v1 complete record by a private **in-process** SHA256 issuance receipt, not a third-party signed crypto certificate. Standalone entry as_dict checks prevent complete-without-actual-scenario/native. Genuine source guard, terminal, rejected physical model, rejected event study and integration-failed statuses remain distinct. Direct unauthorized native Run constructors fail closed. M35a graph/fork/inquiry does not start trusting old wrapper objects as source histories. No imported JSON is trusted as native physics.

**No production field laws or event solvers changed.** Nine genuine old M28a/M28b full v1 source/export records were proven byte-identical on the pinned original versus candidate sample fixtures.

## Developer real source execution — independent reviewer still required

- [First source-pinned test #44139887181](https://github.com/physicsvigilante/review_sandbox/actions/runs/44139887181): **FAILED** (18/19 passed, one test incorrectly expected word receipt while the engine correctly rejected changed evidence with word issued). Retained failed ZIP artifact #14352878870. No original source code was weakened to satisfy the test.
- [Second source-pinned native #44140105158](https://github.com/physicsvigilante/review_sandbox/actions/runs/44140105158): **SUCCESS**, 19 new authentic/adversarial tests + 33 retained native M28a/M28b scientific/renderer tests passed. Pinned early source HEAD `445ad482d5a5fed875d52865df5aba52d570c354` and TREE `f5032042f2ebfa85b5317f2d7fba2c972b9b1e0c`, production validation code unchanged between early and final.
- [Literal old released M35a versus new candidate nine genuine original M28a/M28b full native record byte-identity workflow #44140425617](https://github.com/physicsvigilante/review_sandbox/actions/runs/44140425617): **SUCCESS**, original and candidate source SHA/TREE independently verified, full detached JSON **byte-identical** under literal Unix cmp. Includes nine original physical cases: uniform and ring charges, nonuniform point/gravity source guard, two opposite signed roots, terminal event and genuine physical/event-study refusals. Workflow original candidate pin is early source SHA as above.
- [Actual latest-source M35b native/independent reference #44141135361](https://github.com/physicsvigilante/conductor_sim/actions/runs/44141135361): **COMPLETED SUCCESS** at exact final HEAD. 19 new adversarial tests and 33 old native tests passed. A standard-library only checker with **NO conductor_sim import** recomputed 6 genuine original+changed native M28a/M28b physical runs, **126 actually saved three-component SI samples**, **84 literal shared-time difference rows**, **2 genuine signed M24a detector time shifts/root brackets**, and **10 hostile changed detached native record controls rejected**. Artifact #14353873607, GitHub-provider reported ZIP SHA256 d96341d31a76a3bafd0ee75193636e419615d01bd31e7921c95f60876a1a2db9; artifact ZIP was not independently downloaded and rehashed.

## Current-source full PR workflow state (must recheck live)

At initial status authoring, exact source HEAD **15/17** current-source PR workflows were completed SUCCESS, zero failures. Pending: full Python 3.10/3.12 and historical real Chromium/source checks. [M35a dependency-aware aggregate #44141135071](https://github.com/physicsvigilante/conductor_sim/actions/runs/44141135071) was already SUCCESS. Dedicated [real FEMM5 #44141134871](https://github.com/physicsvigilante/conductor_sim/actions/runs/44141134871) completed SUCCESS in this PR, but read actual job log before reporting the **97** count. [Python #44141134966](https://github.com/physicsvigilante/conductor_sim/actions/runs/44141134966) and [historical Chromium #44141135413](https://github.com/physicsvigilante/conductor_sim/actions/runs/44141135413) remain pending; no postmerge evidence exists for M35b because **PR #82 is unmerged**. Do not call released or full CI green before all checks finish.

## Required release gate

A fresh separate-context reviewer must author truly novel physics and adversarial tests (not simply developer uniform E), reproduce old red/new green, verify actual nonuniform guard/root/status/trajectory physics and **complete unchanged original v1 export bytes**, and publish original R2 verdict PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE at **reviews/review-01-chat-b.md**. A project-wide tamper-proof authentication claim is NOT permitted by in-process receipts. If source HEAD/TREE changes, re-pin CI and review.

Even after a no-blocker independent PASS, **separate explicit owner approval** is required before marking PR ready and GitHub expected-head merge. Verify actual merge Git TREE equals reviewed TREE and **all** triggered exact-main-SHA main-push workflows completed SUCCESS before marking M35b fully released and closing issue #80.


## Verification note — historic Chromium run cancellation and exact-head re-run

For exact source `cb5eec5afb6a64b3cf11f00d2e38e85b5e6f3200` / Git TREE `6d704170cde51c3959af3e78fd089490a0dc4663`, 16 of the originally associated 17 PR workflows were completed SUCCESS, but the [historical visualization/source run #44141135413](https://github.com/physicsvigilante/conductor_sim/actions/runs/44141135413) ended `CANCELLED` in its first attempt, after 53+ historic steps had proceeded. **Cancelled is not PASS, even though no test failure was recorded in the cancelled job.** It therefore does not establish a complete premerge CI gate.

The visualization **specific cancelled job #134243918623 was explicitly rerun** via GitHub after verifying the production PR HEAD had not moved. GitHub accepted the request and reports run #44141135413 **attempt #2 `in_progress`** on the unchanged source SHA at the time of this note. Do not represent 17/17 green until that rerun is actually completed/success. The independent reviewer should fetch current attempt live and preserve original cancellation in chronology. PR #82 remains **DRAFT / UNMERGED**, issue #80 remains OPEN; no owner merge authorization is inferred.

A separate exploratory draftless branch `m35b-legacy-sweep-evidence-consistency` was briefly used for issue-80 adversarial comparisons, but it has **NO PR and NO release authority**; avoid confusing its pinned 45/45 smoke or byte check with PR #82's independently pinned production candidate. The canonical M35b review target is **only PR #82** at the exact source SHA/tree above, with its own developer tests and independent reviewer.
