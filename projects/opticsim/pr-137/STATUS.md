# Opticsim PR #137 — JEE B1 native detector-selected ray-pair design status

**2026-11-18: DESIGN-ONLY DRAFT; INDEPENDENT DESIGN REVIEW PENDING.** No new optics code, native execution feature, browser UI, saved scene schema or merge.

| Identity | Verified value |
| --- | --- |
| Draft design PR | [Opticsim #137](https://github.com/physicsvigilante/opticsim/pull/137) |
| Source baseline actual main | `d3509e82fb65d81aabe336666851f8f2962623f4` |
| Design-only source HEAD | `3db3711c7a21f5dd477b09d5668a9a8becd6a6a7` |
| Authored Git tree | `725d9d450f711a9e379f4137e5c284aa3e0de641` |
| Synthetic PR merge | `29dc4a4c7205597af93fe3256845bfcc93d57459` |
| Synthetic PR merge Git tree | `725d9d450f711a9e379f4137e5c284aa3e0de641` (identical) |
| Sole changed tracked file | `docs/jee-detector-selected-native-pair-design-v1.md`, 182 added lines |
| Prior R2 research gate | [PR #135 Chat B independent R2](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-135/reviews/review-02-chat-b.md) **CLEARED FOR OWNER DECISION — RESEARCH ONLY** |

## Proposed JEE engine capability — NOT IMPLEMENTED

B1 would have an LLM author one existing v5 single-ray/one planar interface/finite detector apparatus and explicitly supply a second source heading. The pinned native engine would execute both independently and measure actual detector hits and first encounters, with **distinct per-run scene hashes**, native completion/warnings and no invented source/ray paths. Only afterward could Opticsim compute an **explicitly advisory** pairwise 2D backward-line intersection. Neither finite detector nor geometric point is an eye, pupil, actual image, native backward-propagated ray or continuous light field.

The draft proposes a strict versioned request and a new CLI instead of modifying the historically frozen existing run CLI; no v20 schema or changes to PhyDemo. It gives **UNVALIDATED provisional numerical display gates** of |outgoing-direction cross|≥0.01, each finite endpoint clearance ≥0.5 mm, extension/scene scale ≤2, oriented plane-relative coordinates. These are conservative proposals, **not calibrated native numerical errors or proven optical accuracy**. A separate preregistered native/numerical stress study and review must justify any public displayed derived point. The first implementation may instead safely expose **native hits only** if evidence is insufficient.

[**Detailed independent design review request**](REQUEST.md) · [**Copy-ready Chat B prompt**](REVIEWER-PROMPT-01.md) · [Design issue #136](https://github.com/physicsvigilante/opticsim/issues/136).

**Independent review PENDING; production source/owner release decision NOT made.** #135 and #133 remain unmerged research/candidate A, as do #129 and all held v14–v19 optics branches. Production main remains unchanged and unprotected under issue #123. The independent review must explicitly challenge the output, numeric and observer inference boundaries before source implementation.


## Builder regression CI on exact design-only source (2026-11-18)

**11/11 GitHub Actions workflows SUCCESS** at HEAD `3db3711c7a21f5dd477b09d5668a9a8becd6a6a7`, source and tested merge Git tree `725d9d450f711a9e379f4137e5c284aa3e0de641`. [Planar workflow #44242161435](https://github.com/physicsvigilante/opticsim/actions/runs/44242161435) checked out synthetic merge `29dc4a4c7205597af93fe3256845bfcc93d57459`, ran Node 24.19.0 with pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`, **790/790 tests passed** and existing planar browser acceptance. [Optical composition #44242161458](https://github.com/physicsvigilante/opticsim/actions/runs/44242161458) passed existing Chrome/browser regressions. The **790** count is the actual production-main baseline; research-only #135's extra **12 native tests are not merged**, so test counts must not be compared as a regression. **Design-only CI does not exercise an unimplemented B1 request or validate candidate numerical thresholds.**

**Independent exact-source design review remains PENDING; no public B1 geometry or observer feature exists.**

## Independent R1 verdict and revised D-02 R2 source — 18 November 2026

[**Chat B R1 design review**](reviews/review-01-chat-b.md) examined **original HEAD `3db3711c7a21f5dd477b09d5668a9a8becd6a6a7`** and returned **CHANGES REQUESTED**: P1-F1 unjustified public advisory numerical intersection, P1-F2 optional rather than mandatory complete run/scene identity, P1-F3 underspecified per-observable status/warnings and partial execution counts. No existing production physics code defect was established; original HEAD/report remain historically intact.

**Intermediate R2 design HEAD (SUPERSEDED)** `4effded78aa9cd285a8595687f5d29d9c8890b1e`; authored Git tree **`176d4c069e4807836ae9161e6d5b258c98aaca7e`**. Tested GitHub synthetic merge **`dcc4009f7ada8422e02e1e147a0ccdbab34a6284`** has the **identical tree**, against still-unmerged/unprotected production `main` `d3509e82fb65d81aabe336666851f8f2962623f4`. Source diff remains **ONE added document `docs/jee-detector-selected-native-pair-design-v1.md`, 196 additions and zero deletions**; no engine, tests, vendor pin, schema, historical CLI or browser change.

**R2 proposal, NOT yet independently cleared:**
- **B1a ONLY** publishes real sampled native crossing counts, hit positions/unit directions, first-interface events, per-run statuses and warnings from two separate v5 single-ray executions through one common finite detector geometry. **Public derived 2D intersection, depth and virtual image coordinates are ALWAYS WITHHELD/NULL**, including the positive 5 mm research fixture. No numerical tolerance is certified. Future opt-in B1b requires a preregistered quantitative native stress/error admission gate, new design/source reviews.
- **Mandatory SHA-256** distinct scene identities and family hash over complete immutable canonical documents with only the one source emission heading removed and component order normalized; strict per-run snapshots/hashes/native pin/input bytes. Reject duplicate modulo-360° directions, invalid nested/duplicate JSON keys, wrong indices/normal/finite detector side/width. A standalone CLI (not the frozen old CLI) preserves exclusive hashed evidence files.
- **Explicit qualification lattice:** each independent run retains 4 full native observable results, raw warnings, method/reason, actual attempted and completed counts. Completed misses return 0/[] and null geometry; stale/incomplete/unreviewed warnings suppress; infrastructure errors and invalid preflight are distinct. A true native `qualified` input cannot be promoted to `available`. Stable typed refusal code and precedence table. Physical eye/image assessment is **not assessed**, not falsely absent.

**Builder CI on corrected R2 HEAD:** all **11/11 existing workflows SUCCESS**, [planar native/browser run #44246744744](https://github.com/physicsvigilante/opticsim/actions/runs/44246744744) logged Node **24.19.0**, pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`, **790/790 production-baseline Node tests PASS**. [Optical composition/Chrome #44246744745](https://github.com/physicsvigilante/opticsim/actions/runs/44246744745) passed unchanged browser checks. This is NOT a B1a implementation or a validated numerical B1b result.

[**Copy-ready R2 Chat B prompt**](REVIEWER-PROMPT-02.md) · [**Detailed independent R2 review request**](REQUEST-02.md).

**Independent R2 design review PENDING.** No merge, release, native observer/eye or image, new public derived point, or B1a source implementation exists. Research-only #135 and candidate A #133 remain separate, and issue #123 still gates main protection.

## FINAL proposed D-02 R2 design source (supersedes intermediate R2) — 18 November 2026

**Review target HEAD:** `7f19f6d5c97608fc0eb1399cea3a3582938f2f6a`; **Git source tree:** `914e1296f1cfb2da61ebbdddc98a907ee32e39a8`; **proposed CI merge commit:** `45f4eaa87128321bc7e479275d5819237f2da4a8` with **identical Git tree**, production base `d3509e82fb65d81aabe336666851f8f2962623f4`. The diff against main still adds **one documentation file only, 197 lines**. Every source implementation, native pin, historical CLI, saved schema, test and browser remains unchanged.

Following the first R2 correction, two minor normative clarifications were committed **before re-review**: full family mismatch detected in preflight is an internal integrity failure with **zero native attempts**, distinct from stale hash reported after execution; B1a counts consistently use `nativeAttempted/nativeCompleted`. Whole-JSON unknown/duplicate/wrong-type precedence is global, even if required facts are missing elsewhere; a later B1a source PR must actually test **both the 2 mm and 10 mm finite detector widths**. These are **requirements for unimplemented source**, not verified runtime behavior.

**R1 CHANGES REQUESTED remains the only independent design verdict so far.** The staged B1a native-hit-only design and all-null derived geometry are PROPOSED. [**R2 Chat B prompt**](REVIEWER-PROMPT-02.md) · [**R2 detailed request**](REQUEST-02.md). Final-head exact CI must be independently verified; the previous 11/11 workflows and 790/790 Node baseline belong to an **intermediate** doc-only commit, not automatic proof about this latest HEAD. **Review pending; no merge or B1a/B1b implementation.**

## FINAL D-02 R2 exact-head regression CI complete — 18 November 2026

**All 11/11 standard GitHub Actions workflows SUCCESS** on exact HEAD `7f19f6d5c97608fc0eb1399cea3a3582938f2f6a`. The [planar native/browser run #44247326360](https://github.com/physicsvigilante/opticsim/actions/runs/44247326360) logged checkout `45f4eaa87128321bc7e479275d5819237f2da4a8`, Node 24.19.0, pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`, **790/790 baseline Node tests PASS**; the tested synthetic Git tree is identical to authored tree `914e1296f1cfb2da61ebbdddc98a907ee32e39a8`. [Optical composition/real Chrome #44247326431](https://github.com/physicsvigilante/opticsim/actions/runs/44247326431) passed current native and hosted/browser checks. No retry needed. This source is **doc-only**, so all executions are unchanged engine compatibility tests, not a B1a/B1b public capability or validation of any numerical coordinate.

**Independent R2 review PENDING** — [copy-ready prompt](REVIEWER-PROMPT-02.md) / [detailed request with raw CI links](REQUEST-02.md). Original R1 remains **CHANGES REQUESTED** in its immutable review record. No PR merged; production `main` unchanged and main protection issue #123 open.
