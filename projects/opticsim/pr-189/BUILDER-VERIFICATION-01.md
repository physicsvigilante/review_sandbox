# Opticsim PR #189 — FINAL BUILDER VERIFICATION & single focused Chat B review instructions

**20 November 2026 — BUILDER evidence; NOT an independent physics review, owner merger, deployment, or completed textbook-answer solution.**
**Release state:** draft/unmerged, requires one focused independent Chat B source/physics/code/evidence review at the exact final tested source.

## 1. Exact Git identities and scope

- [Draft PR #189](https://github.com/physicsvigilante/opticsim/pull/189) exact final **source head**: `c6418afbb02f2421dc04193075819f2a50fd3cd2`.
- Source Git tree: **`153c3fd56b4ed59c8b0274ae33e343186f643747`**.
- GitHub synthetic tested merge commit: `b4131acc3047a312453437aabcf04df8da1e441f` with **identical Git tree `153c3fd56b4ed59c8b0274ae33e343186f643747`**, ordered parents [stable production main `bcf0151c004c94e179adb5ccc47e8d5f9851f23f`, exact PR head `c6418afbb02f2421dc04193075819f2a50fd3cd2`]. This is an additive tree, not a rebase onto a changed production source.
- Baseline production `main`: `bcf0151c004c94e179adb5ccc47e8d5f9851f23f` (independently reviewed and post-merge verified PR #187 J17 inverse). Current `main` was rechecked and unchanged before publishing this packet.
- Previously frozen **source + formula + negative-case protocol** commit: `d9d9afaf2c2ce46789ab83a85213823635c338e9`; protocol blob SHA `99100043ebf148c8cb169b0cd683896553d0e6e2`, byte-identical between the freeze and final tested source.
- Unmodified pinned PhyDemo upstream `811f508d2b070898c241a568b0c167dcb8645251`; no vendor/upstream, native object, canonical schemas, adapters, historical JEE attempts, CI workflows or UI changed.
- **Six additive files only** (no existing file modified or deleted):
  1. `evaluation/jee-j14-prism-two-branch-inverse-v1/frozen-protocol.json`
  2. `src/prism-two-branch-inverse.js`
  3. `scripts/prism-two-branch-inverse-query.mjs`
  4. `examples/jee-j14-prism-two-branch-inverse-v1.json`
  5. `test/jee-j14-prism-two-branch-inverse.test.mjs`
  6. `docs/JEE-PRISM-TWO-BRANCH-INVERSE.md`

The separately researched [PR #188](https://github.com/physicsvigilante/opticsim/pull/188) remains **draft/unmerged and is NOT a dependency or native certification**. Its Fresnel-on rays genuinely produced both forward and return detector callbacks, but every test with both branches was incomplete due native ray truncation. Do not infer complete Fresnel propagation or permit public Fresnel-on v22 scenes from that research.

## 2. JEE source-fact provenance — physical interpretations must stay conditional

- Frozen J14 original **Problems** path `08_Ray_Optics_Explanations/05_Prism/Problems/015.png` from SHA-pinned source archive `08_Ray_Optics_Explanations.zip`, SHA-256 `03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939`.
- Source-only developmental record is held PR #165, exact audit head `6a72bd67e58e9a3fd94a6bf33d88d1f20295b4c2`, `evaluation/jee-post164-coverage-v1/source-review.json`. Prior source collection CI `44360693719`, original source artifact `14454755556` (its ZIP hash is `ec95794b8becfcb10a3819c39063c8c4673cf43f58cb3b6cce3ee523cd755f97`). Original Solutions were not read by builder.
- J14 source facts: finite-wavelength-free, small prism apex; parallel first-face *normal incidence*; second-face partial reflection and transmission; returned branch deviates **4°** from reversed incoming direction; forward transmitted branch deviates **1°**. Ask prism index and apex. **Exterior absolute refractive index, finite prism and beam dimensions/power, ray starts/face intersections, detector and native numeric settings are absent.**
- The new model takes ONLY these angular facts and an explicit two-branch *first-order* convention. It returns a **relative index** unless the caller supplies a separate exterior absolute index. No ambient air is silently assumed.
- This is a **same-assistant developmental** source use, not blind first-attempt JEE scoring, independent interpretation grading or textbook comparison.

## 3. Independent physics review target

Let `m=n_inside/n_outside`, `A>0` small apex, `T>0` forward transmitted deviation and `R>0` return exit deviation from the **reversed** incident ray. At normal first-face entry, the conditional first-order relations are

```
T = (m-1)*A
R = 2*m*A
A = R/2 - T
m = R/(R-2*T)      R > 2*T; m>1
```

At original J14 `T=1°`, `R=4°`, the conditional result is **`A=1°`, `m=2`**. No absolute `n_inside` is reported unless an `outsideIndex` is explicitly added. For exterior `1` the conditional absolute index is `2`; exterior `1.5` yields `3`; exterior `3` implies `6` and is refused as outside the supported [1,4] absolute index domain.

A separate **scalar only** Snell-angle check evaluates
`T_exact=asin(m sin A)-A`, `R_exact=asin(m sin 2A)` in degrees. At J14 they are approximately `1.00030478°` and `4.00244215°`, nonzero first-order residuals well inside the explicit fixed 0.05° guard. **This witness is not a nonlinear exact inverse**, not guaranteed finite face reach, and not actual native ray propagation/branch observation. Slightly above-critical J13 is **not** covered by J14's below-critical small-angle branch.

**Adversarial checks required:** signed return convention and exclusion of first-face-only Fresnel reflection; no exterior index implied by original facts; `R<=2T` zero/negative apex, near-singular `R-2T`, positive tiny deviations, out-of-range implied relative or absolute index, unknown fields, normal vs oblique entry, exact-trig guard, and independence from source intensity/aperture. The fixed first-order caps are engineering admission choices, not rigorous full modelling-error bounds.

## 4. Exact-source CI and evidence — 11/11 PASS

Read GitHub Actions for exact PR head and tested merge tree. All eleven workflows completed successfully:

| Workflow | Run ID | Conclusion |
| --- | ---: | --- |
| Quasi-static source motion checks | 44676511151 | success |
| Deterministic planar angular query checks | 44676511152 | success |
| Qualified authoring checks | 44676511200 | success |
| Original refraction problem pair | 44676511175 | success |
| Optical composition checks | 44676511162 | success |
| Plane-mirror angular inverse checks | 44676511157 | success |
| Numerical ray reliability diagnostics | 44676511145 | success |
| Curved mirror checks | 44676511312 | success |
| Unified problem workflow checks | 44676511132 | success |
| Parameter experiment checks | 44676511136 | success |
| Planar refraction checks | 44676511261 | success |

Actual exact-head Node24 CI log (quasi-static run `44676511151`, job `136089509832`) reports **1,069 tests passed, 0 failed, 0 skipped**. New J14 tests cover the J14 example, independent first-order and trig scalar family, omitted exterior vs absolute indices, singularity, invalid fields, source source-fact boundaries and original-byte/SHA CLI storage. Historical native and real Chrome workflows were executed and green. **No new J14-specific browser scene or physical image/branch screenshot is claimed.**

[Optical composition run 44676511162](https://github.com/physicsvigilante/opticsim/actions/runs/44676511162) produced CI artifacts:
- `llm-authoring-evidence` ID `14601919747`, GitHub metadata digest `sha256:7c4edfa67acfdd733d7930cfb8fde794ef5d9875a6efb73691abd6822afa7ceb`.
- `browser-acceptance-evidence` ID `14601669927`, GitHub metadata digest `sha256:b8fd31b2d016caca5204587c5403265e54f7ca28f7b74b26f89ea1d3cfd0de27`.
- `hosted-browser-evidence` ID `14601809686`, GitHub metadata digest `sha256:fef43a0a48b5d765ff5fcd4fa57b1f48e01de75992b141cbf2fac2410e27cd21`.

**Integrity caveat:** builder read official GitHub artifact names and SHA-256 *metadata* and source-bound test logs. The zip bytes were **not** separately downloaded and recomputed by this builder check. Reviewer can independently download and inspect archive hashes/selected `prism-two-branch-*` input/report pairs; do not claim this has already happened.

## 5. API and CLI isolation, refusals and honest status

Strict standalone `opticsim-prism-two-branch-inverse-v1` JSON schema. No conventional `opticsim-problem-v1` unified-workflow integration is claimed. Only optional `outsideIndex`; every other field is required. Duplicate/extra source optical geometry is not silently removed. Every valid conditional, no-admissible or numerically-indeterminate query returns `native.status:'not-run'`; malformed requests return `rejected`, same native status.

`scripts/prism-two-branch-inverse-query.mjs` exclusively reserves a new output path under `test-artifacts/llm-authoring/`, stores the raw input Buffer using write-once semantics, hashes its *unmodified* bytes, and writes a report and analytical result. It does not call the pinned simulator or generate a portable/qualified scene, saved route, native detector or reconstructed physical image. Existing path safety helper has a disclosed adversarial-concurrent-filesystem race limitation; no new claim of filesystem sandbox security. The new node test verifies valid, physical-unavailable and malformed inputs; no native scene files exist.

Model distinguishes `conditional`, `unavailable`, `numerically-indeterminate` and thrown invalid facts. Conservative limits: small positive measured deviations <=10°, derived apex <=5°, relative index <=4, optional absolute indices [1,4], `|R-2T| <=1e-7°` withheld near singularity except exact zero (unavailable), near-zero measured deviations at 1e-8°, exact Snell near-critical sine margin 1e-5, exact-to-first-order residual <=0.05°. A valid stand-alone result is **not** a fully specified native JEE simulation.

## 6. One focused independent Chat B review due

**Reviewer Chat B:** inspect the final six-file source tree, the frozen J14 source-fact record and (preferably independently) original Problems PNG, derive the *two distinct* conditional Snell/reflection branches and signed inverse **without trusting builder algebra**, verify missing absolute exterior index is never defaulted, check numerical domain and fail-closed statuses/CLI, inspect exact CI and raw archived evidence only to the extent needed, and ensure the one-branch/v22 public PhyDemo contract is unaffected.

Do **not** repeat independent reviews of unchanged previously accepted v22/v23/v24/v25 JEE native physics, historical lens J17, or raw research PR188. This is **one focused physics / numerical-safety / evidence review**, not a new simulated beam capability or a clean blinded LLM score.

**Required reviewer deliverable:** commit full markdown independent review report on `physicsvigilante/review_sandbox` default branch at:

`projects/opticsim/pr-189/reviews/review-01-chat-b.md`

The report must identify reviewed exact source SHA `c6418afbb02f2421dc04193075819f2a50fd3cd2`, Git tree `153c3fd56b4ed59c8b0274ae33e343186f643747`, tested source/merge CI identity, important limitations, any blocking findings, and an explicit final verdict **CLEARED FOR OWNER DECISION** or **CHANGES REQUESTED**. Reviewer must read back the written report and return its immutable GitHub link and review commit SHA. Chat-only verdict is insufficient. **No source edits, PR merge, or deployment** by reviewer.

**Release hold:** PR #189 stays draft, unmerged until the independently committed focused review has been checked against the exact unchanged source and the standing owner release decision is applied. Future JEE sample delta must preserve independent axes of interpretation, physical correctness, simulation coverage, educational value, optional textbook-answer completeness.
