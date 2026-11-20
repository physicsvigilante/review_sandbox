# Opticsim PR #190 — FINAL BUILDER VERIFICATION and one focused Chat B review instructions

**Date:** 2026-11-20 (IST). **BUILDER / developmental evidence, NOT an independent review or a textbook answer certification.** This packet is a handoff for **one focused independent source/physics/numerical/code/evidence review** of a *new conditional analytical index bound plus test-only genuine native witness*. **PR #190 remains draft and unmerged.**

## 1. Exact final source, tree and frozen JEE inputs

- [Draft PR #190](https://github.com/physicsvigilante/opticsim/pull/190) **final tested HEAD `cbf96405ac7a63da4eead04fb8b0d5974fa7ca06`**, Git tree **`25efbe0ed82c3b3ab6d11cf7e37815b12925d3f4`**.
- Tested GitHub synthetic merge **`116315dff20573961cd3dcd821dad9d53153d0cf`**, independently fetched and verified by builder to have **identical tree `25efbe0ed82c3b3ab6d11cf7e37815b12925d3f4`** and ordered parents [production `main` `c4e436fca34c01b3ce63bd426dc71bd0daf1daa9`, exact feature head `cbf96405ac7a63da4eead04fb8b0d5974fa7ca06`]. No base/main drift. Production `main` was read back and remains `c4e436fca34c01b3ce63bd426dc71bd0daf1daa9`.
- Original pre-execution native/source geometry protocol committed first at **`6fb6625453eb62c24d9d7b40d929b9cfb75d5596`**, **Git blob `e8efe248e64c3a5e9329c9a3d69e73262eeb58ea`**. Frozen protocol blob remains byte-identical in final HEAD. All native trial case identities, numerical controls, source constraints and critical threshold were frozen **before** implementation.
- Pinned upstream PhyDemo remains `811f508d2b070898c241a568b0c167dcb8645251` (unchanged). **Eight added files only, zero deletions or modifications to any existing repository file**: research frozen protocol, research README, native research test, new pure analytical module, strict byte-preserving CLI, J13 source-only example, analytical/CLI test and docs. No shared engine, renderer, canonical native scene schema, v8/v22 physics, test harness, CI workflow, historical first attempt or source dataset has been modified.

## 2. Original JEE J13 source and physical interpretation boundary

- Original **Problems** image: `08_Ray_Optics_Explanations/05_Prism/Problems/001.png` from source archive `08_Ray_Optics_Explanations.zip`, historical archive SHA-256 `03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939`.
- Frozen prior source audit: held PR #165 at `6a72bd67e58e9a3fd94a6bf33d88d1f20295b4c2`, file `evaluation/jee-post164-coverage-v1/source-review.json`; original Problems source-collection run `44360693719`, artifact ID `14454755556` (historical archive SHA-256 `ec95794b8becfcb10a3819c39063c8c4673cf43f58cb3b6cce3ee523cd755f97`).
- Source-fact record: **equilateral prism**, original ray enters **AB**, reflects internally at **AC** at an angle **slightly greater than critical**, emerges through **BC** at 30° to BC normal; asks original incidence angle and prism index. The image does NOT specify an absolute exterior index, ray launch coordinates, finite prism size, source brightness, detector, or numerical epsilon for “slightly above”. The builder did not open Solutions. The source visual inspection belongs to the historical source audit; **the reviewer should independently inspect the original PNG** to confirm this geometry/naming.
- This is a same-assistant engineering coverage exercise, not a blind LLM performance score, unique textbook answer, native source-complete simulation, empirical education study or physically imaged JEE solution.

## 3. New analytical physics — independent reviewer must derive, not trust code

For the **explicit principal 2D branch** with left vertical AB, upper AC, lower BC and a ray coming from the left, define `m=n_inside/n_outside>1`, external entrance i, internal angle r and exterior emergence e measured from BC outward normal. For **a physical AB→AC(TIR)→BC sequence**, equilateral geometry gives BC internal incidence magnitude `r`; Snell at entrance and exit:

```
sin(i) = m*sin(r) = sin(e)
=> i=e on the supported principal branch.

AC internal incidence = 60deg-r
TIR strictly above critical requires:
m*sin(60deg - asin(sin(e)/m)) > 1

=> m > (2/sqrt(3))*sqrt(1+sin(e)+(sin(e))^2)
```

At the original `e=30°` this yields **conditional `i=30°` and strict relative lower bound `m>sqrt(7/3) ≈1.52752523165`**. **Equality is critical, NOT strictly-above-critical, and the qualitative word “slightly” cannot be converted into a numeric epsilon.** No unique material ratio or absolute glass index is determined. The alternative J14 partial Fresnel two-branch inverse is NOT used; J13 involves native TIR and a three-face reflected route.

At original source-only input, the new standalone `src/three-face-prism-tir-bound.js` returns precisely the strict relative bound with `outsideIndex:null`, `insideIndexLowerBoundExclusive:null`, `uniqueIndexInferred:false`, and `native:{status:'not-run'}`. Only an added `outsideIndex` permits converting that *strict lower bound* to an absolute open bound; even then there is no unique glass index. A separately supplied candidate `candidateInsideIndex` requires an explicitly supplied `outsideIndex` and must pass strict TIR plus the conservative numerical safety guard; **this is NOT finite face interception or native path certification**.

Review the additional prospective (non-JEE) family of exit angles e=0.1,1,5,10,20,30° against independent Snell geometry. The public analytical intake is deliberately limited to e in [0.1,30] degrees, explicit named branch and model, optional absolute indices in [1,4], an open strict inequality, and `|m*sin(60-r)-1|>1e-5` to classify known candidates. At/below critical or too near, material mismatches, mismatched source schema/branch convention, invalid types, unknown fields, missing exterior with candidate, or an impossible [1,4] interval fail closed. These are **conservative admission choices**, not universal numerical or physical measurement bounds.

## 4. Actual pinned PhyDemo native witnesses — strictly separate, source apparatus synthetic

**Nine** predeclared raw-native cases were run by a **test-only** script using existing authorable v8 `SingleRay + Glass`. The native geometry was explicitly **added**: A=(0,+70) mm, B=(0,−70) mm, C=(70√3,0) mm, source from the left crossing AB at y=20 mm, source launch angled +30° and brightness 0.08, with synthetic exterior index 1 and interior candidates 1.5, 1.6, near √(7/3), and numerical stop controls. These are not original source dimensions or a discovered JEE glass index.

Actual final-head native log (quasi-static motion workflow run `44680367482`, job `136102029656`) records:

| Frozen case | Real native Glass sequence | Native result | Test-only 3-face witness |
| --- | --- | --- | --- |
| m=1.6 above critical | face-12 → face-31 → face-23 | completed, real AC TIR, BC emergence 30.000000000000004° | **yes**, margin 0.0662446581 |
| m=1.5 below critical | face-12 → face-31 | completed, no TIR; exits at upper AC | no |
| m=√(7/3)+0.0001 | face-12 → face-31 → face-23 | completed, real TIR and BC exit 30° | **yes**, margin ~9.1651×10⁻⁵ |
| m=√(7/3)−0.0001 | face-12 → face-31 | completed, no TIR | no |
| m=√(7/3) | face-12 → face-31 → face-31 | raw native terminal may be completed, but critical route ambiguous | no |
| m=√(7/3)+1e−8 | face-12 → face-31 → face-23 | raw native complete, margin ~9.165×10⁻⁹, **withheld** | no |
| translated m=1.6 | face-12 → face-31 → face-23 | completed, real TIR, 30° exit | **yes** |
| depth zero | no qualified route | incomplete, truncation 0.08 | no |
| processed limit one | face-12 → face-31 (partial) | stopped | no |

The test observes actual native callback points and delegated PhyDemo results, uses the existing read-only face observer, verifies complete status, real TIR branch, finite original output and critical margin, never inserts a fake ray or enforces a physically required route. Complete callback sequences in an uncertified near-critical case are **still unqualified**. The analytic API NEVER uses test-only native results or upgrades `native:not-run`. **A separate research witness is not the original textbook's native scene.**

An earlier test-only CI source `f31dbfd1...` failed because the research observer incorrectly interpreted a valid missing `invalid` property as true. The corrected test at `2abdc96f...` normalized that property to a boolean and passed; the frozen protocol and pinned upstream were unchanged. **Do not claim clean first-attempt success**. All subsequent checks on the exact final `cbf96405ac7a63da4eead04fb8b0d5974fa7ca06` passed.

## 5. Exact CI and source-bound evidence

**11/11 final exact-head CI workflows SUCCESS**, with **1,079/1,079 Node24 tests passed, 0 failed, 0 skipped** in run [44680367482](https://github.com/physicsvigilante/opticsim/actions/runs/44680367482), job `136102029656`. The newly added tests cover the J13 source-only open bound, independently calculated thresholds across several e, optional index/candidate queries, above/below/near critical, strict type and branch refusal, 9 genuine native controls, incomplete/stopped cases and byte-bound CLI evidence. Existing historical native and real Chrome regressions also finished successfully. **No new J13-specific Chrome visualization or human usability study is claimed**.

All final PR workflows: Parameter experiment checks (run 44680367598); Plane-mirror angular inverse checks (run 44680367494); Numerical ray reliability diagnostics (run 44680367478); Planar refraction checks (run 44680367433); Original refraction problem pair (run 44680367577); Quasi-static source motion checks (run 44680367482); Curved mirror checks (run 44680367572); Deterministic planar angular query checks (run 44680367592); Qualified authoring checks (run 44680367463); Unified problem workflow checks (run 44680367729); Optical composition checks (run 44680367615).

[Optical composition run 44680367615](https://github.com/physicsvigilante/opticsim/actions/runs/44680367615) uploaded:
- `llm-authoring-evidence` artifact ID **14603633871**, GitHub-declared digest `sha256:6c9e82236dc3651d399015d3f44f9b9496ba857c3e2129dbae2d30a7f34f544f`.
- `browser-acceptance-evidence` artifact ID **14603084624**, GitHub-declared digest `sha256:51ce7df3c9be46cf6aeb3b65fcb4b30e3e25782873815b071d7083fb9a6835a9`.
- `hosted-browser-evidence` artifact ID **14603459036**, GitHub-declared digest `sha256:3de3f2616c29b27606d65a9ee3e494fa989fd62ac1acae60c7f409e1f989aee2`.

**Integrity limit:** These hashes were read from GitHub artifact metadata by the builder, **not** independently downloaded and rehashed by this builder check. Reviewer should independently inspect artifact inputs/reports and zipped raw source hash pairs if available. The CLI `scripts/three-face-prism-bound-query.mjs` saves original raw input bytes + SHA-256, stores conditional, unavailable, and rejected reports, never creates a native scene or image, and refuses reused evidence paths; it retains the pre-existing concurrent-adversarial-filesystem caveat of the shared output helper. This is a standalone query and is not automatically present in unified `opticsim-problem-v1` authoring.

## 6. ONE focused independent review due — required deliverable on GitHub

**Reviewer Chat B:**

1. Independently review the *original J13 Problems PNG* and face naming/direction, explicitly checking the meaning of “slightly above critical”; **do not read Solutions**.
2. Derive signed equilateral AB-entry/AC-TIR/BC-exit Snell relations for `i=e` and the **strict** lower material-ratio bound. Check whether any missing source fact or 2D diagram ambiguity invalidates the claimed conditional branch. Verify the threshold for general supported e, and that exterior material remains unknown.
3. Verify that nonunique inequality vs unique numerical answer is honest, and the conservative `1e-5` near-critical band and [1,4] candidate-index refusals cannot silently promote an impossible critical/numerical path. Review strict schema and raw byte/SHA CLI, including limitations.
4. Inspect actual **native** full 3-face callback evidence, negative below-threshold cases, exact/near-critical withheld cases, stopped/truncated native states, and the test-harness correction. These are **additional synthetic JEE teaching controls**, not original-source native simulations.
5. Verify exact final source commit/tree, synthetic GitHub merge tree equality, unchanged old v8/v22/native schemas and workflows, all 11 exact-head CI runs, and relevant original source and test evidence artifacts. Cite what you independently ran vs inspected.

**Do NOT re-review unchanged v8/v22 PhyDemo refraction algorithms or existing independently accepted v25/J14 code; do NOT review raw research PR #188 as if it were a dependency; do NOT merge or deploy PR #190.**

Publish and read back **one complete Markdown review report** on default branch of `physicsvigilante/review_sandbox` at:

`projects/opticsim/pr-190/reviews/review-01-chat-b.md`

Include exact reviewed source head **`cbf96405ac7a63da4eead04fb8b0d5974fa7ca06`**, Git tree **`25efbe0ed82c3b3ab6d11cf7e37815b12925d3f4`**, synthetic merge `116315dff20573961cd3dcd821dad9d53153d0cf`, source limitations, explicit blockers if found and final verdict **CLEARED FOR OWNER DECISION** or **CHANGES REQUESTED**. Give immutable report link and review commit SHA. **A verdict written only in chat does not satisfy the release gate.**

**Release hold:** PR #190 remains draft/unmerged until complete independent source/physics/numerical/evidence review is verified against the exact final unchanged source, then apply standing owner release instruction. No original 20-question solved-score rewrite, no automatic Fresnel-on release or deployment.
