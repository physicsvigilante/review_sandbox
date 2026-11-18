# Opticsim — release gate and next JEE native integration audit

Snapshot: 18 November 2026. **Analysis only. No merges, branch retargeting, source edits or owner authorization.** This report does not substitute for the separately completed independent source review of PR #161.

## 1. Reviewed first-stage JEE integration status

[Opticsim draft PR #161](https://github.com/physicsvigilante/opticsim/pull/161) remains **draft and unmerged**, exact HEAD `09ad081a34ced0fa969affc1bf54766cabffb04a`. Its [Chat B independent combined review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-161/reviews/review-01-chat-b.md) is **CLEARED FOR OWNER DECISION, no P0/P1**, for this exact source and **not** for older experimental branches. The source adds 13 paths, modifies **zero** existing production paths, and its 12 capability blobs are exact copies of separately frozen PR #144 / #150 / #159 R5 files. [Combined CI](https://github.com/physicsvigilante/opticsim/actions/runs/44329347455) passed **832/832 Node tests and 11/11 standard workflows** on a Git-tree-identical synthetic checkout. The independent reviewer verified source, exact Git objects and scalar math; native PhyDemo and Chrome evidence is **builder CI**, not independent replay.

Production `main` remains `d3509e82fb65d81aabe336666851f8f2962623f4`. GitHub branch metadata reported **`main.protected:false`**, the repository ruleset listing returned **`[]`**, and [release-safety issue #123](https://github.com/physicsvigilante/opticsim/issues/123) remains **open**. The connected app lacks branch-protection administrator access (a prior protection endpoint attempt returned 403), so it cannot truthfully claim that protection is set. **No merge is authorized by “continue” or by review clearance.**

## 2. Exact shared-file audit for held next native branches

I compared the open draft heads directly against the unchanged production-main commit, not against the currently held PR #161. Each source below has main as its merge base, is still draft, and is **not included in the PR #161 clearance**.

| Held line | Candidate head | Files added relative to main | Existing files modified | Key shared-file risk |
| --- | --- | ---: | ---: | --- |
| JEE native parallel beam [#141](https://github.com/physicsvigilante/opticsim/pull/141) after earlier [#127](https://github.com/physicsvigilante/opticsim/pull/127) | `6d6d6b213fedb6f028cd1ffef241aef239d37c62` | 10 | 8 | `src/adapter.js`, `src/authoring.js`, `src/contract.js`, `src/observables.js`, composition/app and workflow |
| Native two-glass foundation [#107](https://github.com/physicsvigilante/opticsim/pull/107) | `fe3a030be7bfba8e5808e4e1e2e66d6815e7add7` | 8 | 7 | shared contract/app/composition and planar CI |
| Native thick-lens + aperture cumulative [#120](https://github.com/physicsvigilante/opticsim/pull/120) | `1c566103842cc6c4841aa97360cc893b0ed710c4` | 35 | 12 | overlapping adapter, authoring, contract, observables, planar media, app and workflow; includes earlier v14–v17 dependency chain |
| Direction-resolved sampled detector footprint [#118](https://github.com/physicsvigilante/opticsim/pull/118) | `7d44e52d2c4c5db30d91e4e87970b706c18a90f6` | 6 | 10 | `src/observables.js`, `src/native-observations.js`, app/evidence panel and related UI |

Measured path overlaps:
- **PR #161 versus #141/#120/#118:** **zero** common changed file paths; the planar addition is textually isolated. Still rerun combined source tests when installing a native branch later; path disjointness is not proof of physical composability.
- **PR #141 versus #120:** **eight shared modified paths** — `.github/workflows/opticsim-ci.yml`, `src/adapter.js`, `src/app.js`, `src/authoring.js`, `src/composition-profiles.js`, `src/contract.js`, `src/observables.js` and `test/composition-profiles.test.mjs`. A naïve concatenation or independent cherry-pick may silently overwrite physics admissions.
- **PR #120 versus #118:** at least the overlapping existing `README.md`, `src/app.js`, `src/observables.js` and `test/detector-hit-transfer.test.mjs` (four files). Detector evidence semantics must not be weakened by a later optical-composition integration.
- **PR #141 versus #118:** `src/app.js` and `src/observables.js` overlap. Any combined integration requires explicit event/provenance and stale/incomplete suppression tests.

The figures above are **GitHub base-to-head comparison path counts** at this snapshot, not an independent physics review or a prediction that Git's textual merge will fail. A clean textual merge can still have an optical measurement or source-ancestry regression.

## 3. Recommended release and development sequence

**Gate A — prepare production safety, then obtain a separate owner decision for PR #161.** The repository owner should set an active **main-target branch ruleset** via GitHub Settings → Rules → Rulesets (or equivalent branch protection): require pull requests, prohibit force/direct pushes and deletion, and choose required successful CI contexts verified to represent the actual native and browser acceptance jobs. A separate Chat B report in review_sandbox **is not** GitHub's native PR approval. Revalidate branch state/HEAD, ruleset enforcement, source/CI tree and required checks immediately before an explicit owner-authorized merge of **PR #161 alone**. Only afterward check the real resulting merge SHA and post-merge CI/native/browser, and do not falsely treat these pre-merge results as post-merge measurements.

**Gate B — prioritize the JEE v19 native parallel beam next.** A single coherent main-based integration candidate should use the **latest independently judged safe** v19 scope (including post-lens aperture boundary refusals in #141), not earlier unsafely superseded draft heads or test-only probes. After Gate A, audit the new actual main base and bring v19's reviewed source into one integration, preserving the exact incident/source identities, finite apertures, native detector evidence and composable thin-lens/planar-media behavior. Builder must run combined regression and real browser/native witnesses. Request **one independent cross-feature integration review** only after adversarial tests, source/CI tree equality and all required checks pass; no redundant review of unchanged frozen v19 physics.

**Gate C — stage the native thick-lens v14–v18 chain later as a coherent cumulative branch.** Do not independently merge the v14/v15/v16/v17/v18 drafts into production merely because they have valid local reviews. Audit cumulative adapter, media, lens, mirror, aperture and depth policies against Gate B's native parallel-beam changes. Handle the eight shared-file overlaps with reviewed physical scope, not mere conflict resolution. Keep native finite regions/test-only research and public capabilities distinct.

**Gate D — integrate detector footprint across optics composition only after fresh combined evidence checks.** Reconcile its output/provenance with the actual native emitter/interface/hit event constraints from the installed engine, including multiple sources, branches, count limits, stale/incomplete suppression and Fresnel warnings. One targeted integration review may suffice if substantial physical evidence semantics change.

**Gate E — CI reliability/branch workflow improvement (issue #123).** All 11 standard workflows currently target PRs to `main` (per the issue's audited evidence), prompting fragile temporary main-target CI harness PRs for stacked feature branches. Before the next stacked development, make a reviewed supported-base trigger plan and verify actual checks run on proper feature/research parents; preserve full Node 24 physics verification and every native/Chrome acceptance gate. Combine duplicate heavy test execution only after proving all required checks remain enforced. Chrome discovery failures should be retried **on unchanged source**, preserving both attempts; do not mistake infrastructure retries for independent physics tests.

## 4. How to reduce independent reviews without relaxing safety

Use risk-based review policy [here](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/REVIEW-AND-INTEGRATION-POLICY.md): a complete **builder adversarial preflight** before the final frozen source, exact-source full CI, one independent review for genuinely changed physical/result semantics or combined integration, and **focused** independent correction only if a reviewer demonstrates a P0/P1. Routine docs/tests without changed safety claims do not receive automatic separate Chat B reviews. Once a result is independently cleared, do not repeatedly review the same unchanged source blob inside every integration unless a new interaction warrants it.

Maintain four separate judgments: interpretation fidelity, physical correctness, native evidence completeness, and educational usefulness. Conditional mathematical apparent-axis intercepts are **not** reconstructed physical images; a native detector count zero is **not** absent evidence or invisibility; synthetic test summary corruption is **not** physical PhyDemo output; and SHA checks are freshness rather than tamper-proof authentication.

## 5. Current decision and status

**Status: OWNER RELEASE-SAFETY ACTION PENDING.** Production main and all 62 open draft/research PRs remain unmerged. No new review or optical feature is required merely for this risk audit. PR #161 is already independently cleared; if its exact code, target main or physical claims remain unchanged, setting main protection alone does not demand a new independent optical review. A **separate explicit owner merge authorization is still necessary**. This document makes no changes to production code, GitHub rules or PR states.
