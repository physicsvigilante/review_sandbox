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
