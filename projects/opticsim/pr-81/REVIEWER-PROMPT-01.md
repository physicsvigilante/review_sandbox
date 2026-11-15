# Paste into a separate ChatGPT conversation — Opticsim PR #81 R2 design critique

You are **Chat B**, a separately situated reviewer. This task is to **independently challenge a PRE-IMPLEMENTATION design**, **not** to attest that the implementation works (there is no implementation) or to merge code.

**Canonical review hub:** https://github.com/physicsvigilante/review_sandbox
**Review request:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-81/REQUEST.md
**Status:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-81/STATUS.md
**Source PR #81 (draft, docs only):** https://github.com/physicsvigilante/opticsim/pull/81
**Exact pinned design HEAD:** `df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7`
**Exact production base:** `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`
**Pinned proposed contract:** https://github.com/physicsvigilante/opticsim/blob/df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md

1. Read the central hub `AGENTS.md`, `PROTOCOL.md`, `REVIEW-RISK-POLICY.md` and the pinned request. Read Opticsim `AGENTS.md` at the exact production base, the **pinned design text** and existing `src/adapter.js`, `src/native-observations.js`, `src/observables.js`, `scripts/author-scene.mjs`, `docs/DETECTOR-HIT-EVENTS.md` and necessary pinned native evidence.
2. Do not inherit Chat A's interpretation. Critique whether *actual* PhyDemo object references returned by observed source/incident callbacks are sufficient to claim **only** immediate parent-child relationships for rays later observed at a detector. Identify novel counterexamples: unobserved emission with no incident, lost/duplicate native child, TIR/in-place mutation, source ID ambiguity, event overflow, nested observer order, detector readouts and stale-hash callbacks.
3. Challenge the proposed **one planar interface / 1–2 single-ray sources / 1–2 detectors**, **64 object / 32 crossing limits** and the complete/unknown/refusal contract. Distinguish correct limited source ancestry from *unsupported full ray history*, detected images, physically correct critical-angle paths and continuous illumination.
4. Inspect [PR #80 CI run](https://github.com/physicsvigilante/opticsim/actions/runs/43729455968) and [raw artifact](https://github.com/physicsvigilante/opticsim/actions/runs/43729455968/artifacts/14166949457) only to the extent access allows. Prior tests were **same-assistant research**, not your own execution. When evidence is missing, say so. A design-only review may identify issues without running software; never claim to have run new tests unless actually done.
5. Write your **own, new, attributable** report to the CENTRAL repository as `projects/opticsim/pr-81/reviews/review-01-chat-b.md` (directly on main, or via independent review PR). Follow `REVIEW-TEMPLATE.md` and cite exact source/CI SHAs and line references for concrete findings, risks, reproduction/test proposals. Do **not** edit the pinned design PR, create a fake Chat B report from Chat A's text, or merge anything.
6. State `pass`, `changes-requested` or `insufficient-evidence` **FOR DESIGN ONLY**. A design pass cannot authorize production or replace independent R2 review of any eventual implementation. Distinguish source interpretation fidelity, physical/numerical correctness, native trace evidence, provenance integrity, educational usefulness and textbook-answer completeness.

When complete, provide the GitHub URL of the **new report**, or state clearly why writing it was impossible. The owner can then say **“Review complete”** in the Chat A conversation; Chat A will fetch the report from the hub.