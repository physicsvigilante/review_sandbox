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
