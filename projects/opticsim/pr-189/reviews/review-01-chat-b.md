# Opticsim PR #189 — Chat B independent focused review 01

**Date:** 2026-11-20  
**Verdict: CLEARED FOR OWNER DECISION**  
**Scope:** Source-fact fidelity, independent first-order two-branch physics, numerical admission/refusal, standalone CLI/evidence, exact CI identity and unchanged native/public capability boundary. This is **not** a native Fresnel-on qualification, independent textbook-solution grading, deployment authorization or PR merge.

## 1. Immutable reviewed identities

- **PR:** [physicsvigilante/opticsim #189](https://github.com/physicsvigilante/opticsim/pull/189), observed draft, open and unmerged.
- **Exact reviewed source head:** `c6418afbb02f2421dc04193075819f2a50fd3cd2`.
- **Exact reviewed source Git tree:** `153c3fd56b4ed59c8b0274ae33e343186f643747`.
- **Production base `main`:** `bcf0151c004c94e179adb5ccc47e8d5f9851f23f`.
- **GitHub Actions tested synthetic merge:** `b4131acc3047a312453437aabcf04df8da1e441f`, independently checked to have **the same tree** `153c3fd56b4ed59c8b0274ae33e343186f643747`. Ordered parents: production base `bcf0151c004c94e179adb5ccc47e8d5f9851f23f`, PR source `c6418afbb02f2421dc04193075819f2a50fd3cd2`. The workflow records also identify the exact source head and PR #189.
- **Frozen-before-model protocol:** commit `d9d9afaf2c2ce46789ab83a85213823635c338e9`; protocol Git blob `99100043ebf148c8cb169b0cd683896553d0e6e2` remains identical in final source tree.
- **Exact base-to-head comparison:** six commits ahead, zero behind; **six added files, zero modifications and zero deletions**. The files are `src/prism-two-branch-inverse.js`, `scripts/prism-two-branch-inverse-query.mjs`, `evaluation/jee-j14-prism-two-branch-inverse-v1/frozen-protocol.json`, `examples/jee-j14-prism-two-branch-inverse-v1.json`, `test/jee-j14-prism-two-branch-inverse.test.mjs`, and `docs/JEE-PRISM-TWO-BRANCH-INVERSE.md`.

## 2. Independently inspected original source

The reviewer downloaded source-bound GitHub Actions artifact **14454755556** from run [44360693719](https://github.com/physicsvigilante/opticsim/actions/runs/44360693719), recomputed the downloaded ZIP SHA-256 as **`ec95794b8becfcb10a3819c39063c8c4673cf43f58cb3b6cce3ee523cd755f97`**, and confirmed agreement with GitHub's artifact metadata. Inside the ZIP, the independently viewed image `jee-post164-coverage-v1/sources/J14.png` has SHA-256 **`5ef7dc1e6778bcde10a59950b03514980555c7733ec0a9c7e4346986cdabfe6a`**, matching the archived source manifest mapping to `08_Ray_Optics_Explanations/05_Prism/Problems/015.png`.

The image states normal incidence of a parallel beam on prism face 1, a small prism angle, partial transmission and reflection at face 2, subsequent return to and exit through face 1, a **4°** angle to the reversed incoming direction, and a **1°** deviation of the forward transmitted beam. It requests prism index and angle. It supplies **no numerical exterior absolute refractive index** or finite apparatus/beam/observing geometry. These statements agree with frozen J14 source facts. The image was read independently; no Solutions image was read. The original underlying source ZIP hash `03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939` was checked against the archived manifest, **not** independently recomputed from the original source ZIP bytes.

This is a same-assistant developmental interpretation, not an independent first-attempt score or completed textbook-answer certification.

## 3. Independent signed two-branch physics

Choose the forward incident beam as the positive longitudinal axis, the second-face outward normal rotated by a small positive apex angle `A`, and `m = n_inside/n_outside > 1`. At face 1 the beam enters normally and has no refraction-induced direction change.

- **Forward transmission at face 2:** The internal incidence magnitude is `A`; Snell gives external relative-to-face-normal magnitude `asin(m sin A)` if that exit propagates. The signed forward direction differs from incidence by `A - asin(m sin A)`, so the positive transmitted deviation is `T_exact = asin(m sin A) - A`. For small angles: **`T = (m-1)A`**.
- **Second-face reflection then first-face return:** Specular reflection at face 2 turns the backward-going interior ray by `2A` away from exactly reversed incidence. Its first-face interior return incidence is therefore `2A`; Snell on exiting face 1 gives **`R_exact = asin(m sin 2A)`**, measured from the reversed incident ray. First order: **`R = 2mA`**. This is **not** the unrelated first-face Fresnel-reflected ray, which would return near zero angular deviation at normal incidence.
- Solving the independent pair: **`A = R/2 - T`**, **`m = R/(R-2T)`**. The declared positive-apex, `m>1` branch requires `R>2T`. At `T=1°`, `R=4°`, the first-order conditional values are **`A=1°`** and **`m=2`**.
- Independent scalar trig evaluation at those first-order values gives `T_exact ≈ 1.000304779914531°`, `R_exact ≈ 4.0024421496998075°`; largest deviation from first order `≈0.0024421496998°`, smaller than the explicit **0.05°** admission guard. These nonzero residuals are important: the routine **does not** perform or claim an exact nonlinear inverse.

The code correctly returns **relative index** `m=2` with `outsideIndex=null` and `insideIndex=null` for the source-only query. A caller-provided exterior index `1` conditionally yields absolute inside index `2`; `1.5` conditionally yields `3`; exterior `3` is refused because implied inside index `6` exceeds the declared [1,4] absolute-index domain. No default air index is inferred from the J14 image.

## 4. Source/code and refusal review

Directly inspected all six final-source files plus the pre-existing `scripts/authoring-evidence.mjs` helper and earlier frozen source-review J14 record. Results:

1. **Scope control PASS.** Exact format/kind/model/branch convention/degree units are required. Foreign fields (including arbitrary geometry, brightness, reflectance and alleged detectors), missing facts, invalid numeric types and an unsupported first-face-only reflection convention are rejected. The isolated API is **not** wired into a conventional unified `opticsim-problem-v1` or portable native scene contract.
2. **Singularity and domain PASS.** Zero/negative deviations are unavailable; positive deviations at the resolution floor are numerically indeterminate; `R=2T` is zero-apex degeneracy; a near-zero denominator is indeterminate; `R<2T` is no-admissible-positive-apex; large input/apex/index values are unavailable. Index values are bounded. Nonpropagating/near-critical Snell exits and exact-versus-first-order residual failures are withheld. All cutoffs are **engineering admission choices**, not guaranteed physical error bounds.
3. **Native nonclaim PASS.** On valid, unavailable and numerically-indeterminate queries, the result always records `native.status: 'not-run'`, no observations or branch-completeness certification, and no original-question solution claim. Malformed JSON becomes a rejected report with the same native status. The function never instantiates PhyDemo or synthesizes source paths.
4. **CLI evidence PASS.** It exclusively reserves new output under `test-artifacts/llm-authoring/`, preserves original input bytes before parsing, records their SHA-256, keeps a rejected report separate from a valid analytical result and creates no native scene. The already-existing path helper discloses its adversarial concurrent-filesystem race limitation; this is not a newly hardened filesystem sandbox.
5. **Public capability isolation PASS.** The base-to-head diff has no engine, upstream PhyDemo pin, native object, canonical schema, v22 authoring path, UI or CI workflow changes. The one-branch public v22 restrictions are therefore not expanded by this PR. Separate [research PR #188](https://github.com/physicsvigilante/opticsim/pull/188) remains draft and unmerged; its Fresnel-on cases with real forward/return callbacks were numerically truncated and cannot serve as complete native certification.

## 5. Exact tested CI and independently downloaded output

GitHub Actions independently reports **11/11 successful PR workflows** on source `c6418afbb02f2421dc04193075819f2a50fd3cd2` (and the reviewed synthetic merge tree): runs `44676511151`, `44676511152`, `44676511200`, `44676511175`, `44676511162`, `44676511157`, `44676511145`, `44676511312`, `44676511132`, `44676511136`, `44676511261`. The actual [run 44676511151](https://github.com/physicsvigilante/opticsim/actions/runs/44676511151) job `136089509832` log reports **1,069 passed, 0 failed, 0 skipped**. This reviewer did not rerun the full test suite or new native browser execution locally.

From [optical composition run 44676511162](https://github.com/physicsvigilante/opticsim/actions/runs/44676511162), independently downloaded artifact **14601919747**, calculated downloaded ZIP SHA-256 **`7c4edfa67acfdd733d7930cfb8fde794ef5d9875a6efb73691abd6822afa7ceb`**, and matched GitHub's official metadata digest. The reviewer then inspected all three archived `prism-two-branch-*` evidence case directories and recomputed the input SHA for each:

| Archived query | Observed status | Original-byte hash | Native status | Generated native scene |
| --- | --- | --- | --- | --- |
| Ordinary J14 first-order query | `conditional` | matching | `not-run` | absent |
| Inadmissible branch query | `unavailable` | matching | `not-run` | absent |
| Malformed JSON | `rejected` | matching | `not-run` | absent |

Where present, the analytical result's hash and status agree with the corresponding input and report; malformed JSON has **no** analytical-result file. The current artifact is now **byte-verified**, improving on the builder's metadata-only artifact check. Separate hosted-browser and browser-acceptance artifact ZIPs were not independently redownloaded here; their workflow success was verified in GitHub Actions. No J14-specific native screenshot or complete physical two-branch tracing is claimed.

## 6. Findings, residual risks and release scope

**Blocking findings: none within the declared isolated first-order J14 analytical contract.**

- **Nonblocking precision/interpretation boundary:** This is a conditional, positive-apex greater-index branch with fixed numerical limits. It cannot determine an absolute glass refractive index without an added exterior index, an exact nonlinear inverse, finite ray interception, intensity or native Fresnel completeness. Preserve that language in the owner decision and any UI.
- **Nonblocking evidence boundary:** The original PNG bytes and two downloaded GitHub artifact ZIP digests were checked independently, but the underlying original source-archive ZIP bytes, other browser ZIP bytes, and full native browser execution were not independently replayed. Exact-head successful CI remains the regression evidence.
- **Optional future intake hardening, not a release blocker:** Standard `JSON.parse` accepts repeated object keys with last-key-wins behavior. The original raw input is archived unmodified so such a case is auditably visible; if rejecting duplicate JSON members becomes a stated input-forensics requirement, add an explicit duplicate-key parser/control rather than treating the current schema checks as that guarantee.

There is no basis to conflate this analytical addition with public Fresnel-on branch qualification, with a solution to J13's above-critical geometry, or with improved native-simulation coverage of the original J14 problem. Education value and textbook-answer completeness remain separately unscored.

## 7. Final verdict and hold

**CLEARED FOR OWNER DECISION** on exact source **`c6418afbb02f2421dc04193075819f2a50fd3cd2`**, tree **`153c3fd56b4ed59c8b0274ae33e343186f643747`**, tested merge **`b4131acc3047a312453437aabcf04df8da1e441f`** (same tree). The required focused independent source/physics/numerical-safety/evidence review has not found an in-scope blocker.

**Owner release hold remains in effect.** Keep PR #189 draft/unmerged until the owner confirms this recorded review applies to the unchanged exact candidate and makes the separate release decision. Reviewer performed no source edits, PR merge or deployment.
