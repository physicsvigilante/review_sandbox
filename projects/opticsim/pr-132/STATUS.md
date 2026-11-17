# Opticsim PR #132 — proposed apparent-depth design status

**2026-11-17: DESIGN DRAFT READY FOR INDEPENDENT REVIEW. NOT IMPLEMENTED.**

[Draft PR #132](https://github.com/physicsvigilante/opticsim/pull/132) adds exactly one 140-line design document and no `src/`, test, native, schema, viewer, CI or provenance change to the actual production main base. [Review request](REQUEST.md) and [copy-ready Chat B reviewer prompt](REVIEWER-PROMPT-01.md) are available.

| Item | Verified |
| --- | --- |
| Source HEAD | `07dcf1d6ed0c094071d2d5347ab14baa2bd35c04` |
| Base main | `d3509e82fb65d81aabe336666851f8f2962623f4` |
| Authored source Git tree | `0917d9d70a01ae107b08bb0a031524cc32df3a07` |
| Synthetic PR-merge commit | `ab6f82ef377a31f9e1649c12a4678936a78b186c` |
| Synthetic PR-merge Git tree | `0917d9d70a01ae107b08bb0a031524cc32df3a07` (identical) |
| Diff | Only `docs/jee-apparent-depth-observer-contract-v1.md`, 140 inserted lines |

**Design choice:** A first proposed JEE reduced-facts *conditional paraxial* apparent depth with explicit assumption, no native trace, no v20 saved scene or image claim. A user-stated object-medium maximum incidence angle may produce a separately labelled **symmetric-ray** depth envelope, not native error certification. A **future separate** native B would require actual rays through the same short finite detector window, fully qualified crossing data and warning-preserving derived statuses, with separately validated conditioning. It cannot claim eye perception or unique physical image.

This responds to [independent reviewer P1-A/P1-B findings for test-only PR #131](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-131/reviews/review-01-chat-b.md). That original review cleared the *feasibility checkpoint only*. No newly implemented engine or observer feature exists in this document.

**Review gate:** Independent Chat B design review pending. On clearance, implement A on its own new draft branch with source/node/browser integration verification and a fresh independent physics review; B needs a separate finite-window native feasibility study. Nothing is merged or released. Held #129 and main safety #123 remain separate.


## Independent R1 verdict and design revision R2 — 18 November 2026

[**Independent Chat B review #1**](reviews/review-01-chat-b.md) examined original exact HEAD `07dcf1d6ed0c094071d2d5347ab14baa2bd35c04` (tree `0917d9d70a01ae107b08bb0a031524cc32df3a07`). Verdict: **CHANGES REQUESTED**; no P0 physics blocker. Reviewer independently verified exact Git and CI identity, checked existing dispatcher, and recomputed scalar physics, without executing PhyDemo/Node/Chrome.

**Required R1 P1 findings:** (A) conditional analytical status rather than unqualified `available`, plus missing/invalid/unsupported taxonomy; (B) explicit paraxial model domain, guard against wide, near-critical and grazing cones; (C) normative `opticsim-problem-v1` kind/query/fact mapping and no-native CLI/verifyNative behavior. B's finite-detector/pupil distinction, warning propagation and numeric conditioning remain separate future research gates.

**Corrected design-only source HEAD:** `c97064d8e3d9a8b05ed31a6a753dc246b1dbcc31`; source Git tree **`6a29497776d60fb8b709c6bd4add2300f9783376`**; synthetic PR merge `0434a815aa0f4bb1490b228ff79c75fb9cef4bbe` has the **identical tree**. Original R1 HEAD remains in immutable commit history. The only diff vs current main is the design document, now 174 added lines and no code/test/native changes.

**R2 design changes proposed, NOT independently cleared yet:** `conditional` results; explicitly declared `paraxial`, optional maximum object-side incidence **≤5° and ≤1% difference between paraxial/symmetric-ray geometric constructions**, with typed refusals; bounded [0.01,10,000] mm real depth and finite result limit; exact typed `paraxial-apparent-depth` query under existing `opticsim-problem-v1`; pure reduced facts with **zero native calls**, no scene/portable package; a separately blocked `verifyNative:true` request. These constraints are design-policy decisions, not observational/accuracy guarantees.

[**Copy-ready R2 Chat B prompt**](REVIEWER-PROMPT-02.md) · [**Full R2 request with physical/control checks**](REQUEST-02.md).

**R2 independent review PENDING.** No A implementation or actual eye/observer-image capability has been authorized by design. All held physics PRs and production main remain unmerged and unchanged; issue #123's unprotected main remains a release gate.

**Corrected-source R2 regression CI (builder):** all **11/11 GitHub Actions workflows SUCCESS** at exact HEAD `c97064d8e3d9a8b05ed31a6a753dc246b1dbcc31`. [Optical composition run #44151601237](https://github.com/physicsvigilante/opticsim/actions/runs/44151601237) passed the existing Node and Chrome regression steps. These test unchanged native/production code only, not the unimplemented apparent-depth A method. Independent design R2 remains pending.


## Independent design R2 completed — later verification (2026-11-18)

[**Chat B review #2**](reviews/review-02-chat-b.md) independently cleared revised source HEAD `c97064d8e3d9a8b05ed31a6a753dc246b1dbcc31`, tree `6a29497776d60fb8b709c6bd4add2300f9783376`, verdict **CLEARED FOR OWNER DECISION — design only**. Original R1 remains **CHANGES REQUESTED**, unchanged. Reviewer verified source/tree identities, recomputed Snell/paraxial/symmetric angle controls, and confirmed all three R1 P1 requirements were addressed at *design level*: conditional status/refusals; narrow ≤5° AND ≤1% symmetric-construction discrepancy; exact no-native deterministic planner/CLI query and explicit blocked `verifyNative:true`. Reviewer did **not** run native PhyDemo, Node or Chrome, and did not review later implementation source.

[Draft implementation PR #133](https://github.com/physicsvigilante/opticsim/pull/133) is a separate actual-engine change based directly on production main. Its final-source builder CI passed **802/802 Node24 and 11/11 workflows** after retaining one earlier historical frozen-file SHA failure and a final-source browser-runner retry. [Independent source/physics review prompt](../pr-133/REVIEWER-PROMPT-01.md) is prepared. No production merge or image/eye capability is implied.
