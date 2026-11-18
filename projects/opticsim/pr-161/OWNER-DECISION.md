# Opticsim PR #161 — owner integration decision packet

**Prepared 18 November 2026. Owner decision: PENDING. This file is not merge authorization.**

## Decision-ready source, exactly bounded

[Draft integration PR #161](https://github.com/physicsvigilante/opticsim/pull/161) is open, draft, unmerged, targeting production `main`. Reviewed source HEAD **`09ad081a34ced0fa969affc1bf54766cabffb04a`**, Git tree **`1b2caf6186c8eaf678963238d2292001b2fa9667`**. Production main at decision preparation remains **`d3509e82fb65d81aabe336666851f8f2962623f4`**.

[Chat B's combined independent exact-source review](reviews/review-01-chat-b.md): **CLEARED FOR OWNER DECISION, no P0/P1**, explicitly including the latest R5 evidence-refusal correction that had not received a separate source review. This is the only independent integration review needed for this **unchanged** exact Git tree unless source, base, physical claims or safety controls materially change. The reviewer independently inspected source, exact Git blob identities, Git ancestry, CI logs, and recomputed reflection/Snell relations, **not** PhyDemo or Chrome itself. Builder GitHub Actions execution was **832 Node tests passing and 11/11 standard workflows successful** on the combined, matching Git tree.

The candidate adds exactly **13 files** (12 unchanged source/test/doc/example blobs from held PR #144 and the observer-position chain through #159, plus one integration audit document) and does **not** modify existing native PhyDemo, adapters, scene schemas, authoring, the UI, browser or workflows. It directly originates from current main; it is **not** a Git merge of draft feature dependencies.

## What a decision would release into main

- A *strict analytical-only* one-plane apparent-depth query accepting an explicitly supplied incidence angle. Finite-angle mathematical apparent-axis intercept is separate from the paraxial approximation and is **not** a physical image or a native reverse ray.
- A separate *strict analytical-only* one-plane source-to-observer-position query finding a conditional stationary transmitted ray; it returns a **predicted** crossing/heading and possible conditional axis intercept, never an actual detector reading.
- An *opt-in fully specified real native PhyDemo single-ray witness* that authors brightness, Fresnel policy, numerical preset and finite detector with user-chosen tolerances. It can report an **actual sampled detector crossing**, a qualified measured zero, or a withheld/missed result. It does **not** independently find an inverse ray, reconstruct a perceived image, infer full path history, guarantee arrival in all geometries, or certify continuous irradiance.

This is a bounded first-draft **JEE planar** milestone. The reviewed but held parallel-beam v19 (PR #141), thick-lens v14–v18 family, detector-footprint features, prior test-only probes and other experimental branches are **outside** the scope and **not cleared** by #161.

## Outstanding release-process safety (owner/admin action)

The [release-safety issue #123](https://github.com/physicsvigilante/opticsim/issues/123) remains **OPEN**. GitHub branch data reported **`main.protected=false`** on 18 November 2026. The connected GitHub App returned **403 FORBIDDEN** when asked for branch-protection details and cannot configure admin protections. This is a **release-process risk, not a newly identified physics defect**.

Before an owner-authorized merge into main, recommended repository-owner steps:

1. In GitHub repository **Settings → Rules → Rulesets**, establish an active branch ruleset targeting `main` (or equivalent branch protection), requiring pull requests, preventing unintended direct and force pushes and deletion, and requiring relevant **green CI jobs**. If available and practical, add formal human review requirements, but do not mistake a separate Chat B report in review_sandbox for a native GitHub PR approval.
2. Confirm the chosen required CI checks actually execute on PR #161's source/target combination and are green. Do not use a ruleset that accidentally excludes critical native or browser acceptance. Source CI is passing now; protection is still absent.
3. Reconfirm PR #161 remains exactly at approved head `09ad081a...`, main is at the expected base or the new base delta is checked, its exact source tree is unchanged, all required status checks pass, and it is the **only** candidate to integrate. If the merge candidate or acceptance claims change, inspect the delta; request a focused independent review only for a material safety/physics change.
4. **Only after explicit owner approval**, mark the PR ready and merge **PR #161 alone** using the approved release process. Do not separately merge earlier draft PRs #144/#150/#159, or their blocked ancestors, because #161 contains the selected exact content already.
5. Inspect the actual merge/result SHA and run post-integration GitHub Actions, native and real browser acceptance. If a required check fails, diagnose and do not claim success or deploy prematurely.

Issue #123 also requests stacked-branch CI triggering and reduction of redundant heavy jobs. Those improvements are useful for the **future** native parallel/thick-lens branches and should be planned separately; this main-target PR already has full source/merge-tree CI proof. There is no reason to reopen all prior source-physics reviews merely to set branch protection.

## Minor, NONBLOCKING follow-ups

- **N1:** exercise the witness's *classifier-stage* exception catch directly with an injected projection-qualified record. The current artificial accessor test exercises the *earlier* observation-projection infrastructure catch, while the missing/null vector records do test normal refusal with a durable report.
- **N2:** an explicit cross-contract regression in which the observer query's signed incident angle is passed into the explicit-incidence analytical query, comparing conditional apparent-axis intercepts across signs, frames and units.

These are future coverage improvements, **not** reasons to rewrite this frozen reviewed tree or repeat independent review when no correctness issue is identified. Implement as ordinary follow-up tests with builder CI after an owner-approved integration, or handle as a scoped later development candidate if they materially change safety semantics.

## Owner decision choices

- **Authorize integration only after protective rules:** owner confirms branch-protection/ruleset operation, checks, exact source and formally instructs merge of **PR #161**. That instruction is required and has **not** been received.
- **Keep draft held:** maintain source and review artifacts frozen. This is the current state.
- **Request changes:** specify the release-safety concern or source delta; a new bounded review may be necessary if physics/evidence behavior changes.

**No merge/deployment has occurred.** Production main and all excluded optical feature branches remain held. Independent review clearance is not release permission.
