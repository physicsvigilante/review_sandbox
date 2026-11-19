# Opticsim PR #183 — builder verification and ONE independent review handoff

**Builder verification, 2026-11-19.** This is the *builder's* evidence report, not an independently issued physics review, solved-JEE benchmark, owner merge authorization or deployment. [PR #183](https://github.com/physicsvigilante/opticsim/pull/183) is **DRAFT / UNMERGED**. Production `main` is unchanged by the candidate.

## 1. Exact Git identity verified through Git objects

| Item | Immutable identity |
| --- | --- |
| Current production base | `487314dcb7e74e7f16f5b711f950090e16400780` |
| Exact final candidate source HEAD | **`6ea3c2edb4440e4e27b2f88f43660bd6ffed974f`** |
| Source Git tree | **`a8ea9878bee361c6ef05a83b9d5d913a3b8a7584`** |
| Actual tested synthetic PR merge | `7d56fc34a331873505748f5c881a9e5f8e63f701` |
| Tested synthetic merge tree | **`a8ea9878bee361c6ef05a83b9d5d913a3b8a7584`** — identical |
| Synthetic merge ordered parents | [production base, exact candidate source] |
| Pinned native PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251` unchanged |

The builder read the [source Git commit object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/6ea3c2edb4440e4e27b2f88f43660bd6ffed974f) and the [synthetic merge Git commit object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/7d56fc34a331873505748f5c881a9e5f8e63f701) separately. This is **Git-object equality**, not an assertion that an in-job test performed an independent tree comparison. The passing CI jobs checked out the GitHub synthetic merge, not a different manually reconstructed tree.

Current-main-to-PR source diff: **56 paths total; 42 added, 14 modified, zero deleted.** Original held [PR #171](https://github.com/physicsvigilante/opticsim/pull/171) supplied 41 additive files initially imported using their old Git blobs; **38 remain byte-identical**, two integration tests and one browser-source-fingerprint fixture were intentionally reconciled for the newer base. The 42nd additive file is the new integration note `docs/JEE-NATIVE-V14-V24-INTEGRATION.md`. Fourteen modified shared/CI/test paths were reconciled, not copied over from the obsolete v21 base.

**All six old core modules retain their original Git blobs:**

| Original PR171 module | Unchanged Git blob SHA |
| --- | --- |
| `src/two-finite-dielectrics.js` | `a970818392f50dcae6f7126bfa3916b697c6ff1b` |
| `src/spherical-lens.js` | `9fc8133b90322d8a5dfac67a78b1da59c45374fe` |
| `src/thick-lens-mirror-composition.js` | `e958faa81eb8a87154b92ec1d3631f2a1908c1c7` |
| `src/two-thick-lens-mirror-composition.js` | `d616e510a5284ecf6a178d5bfce17d50a266a499` |
| `src/thick-lens-aperture-composition.js` | `7370c56ba7752fdf317574bd8089cf9be51b998c` |
| `src/native-v18-aperture-corner-guard.js` | `57728c389ab2a109b5cd708ab1d6fde614501230` |

The original historically reviewed v18 browser app Git blob `cfbea455df3f7ea7a30002d0139730c25b235d32` remains historical; the **newly reconciled** browser `src/app.js` Git blob at final candidate is `ac8ee9e3bf448c4280342d9049052bbbce1691b0`, recorded only as new integration provenance in `test/fixtures/native-v14-v21-app-integration-v1.json`. No old first attempts, source PNGs or review reports have been rewritten.

## 2. Physical admission and numerical safety

The candidate adds **five separately versioned** public native compositions using existing pinned PhyDemo physics:
- **v14:** two separated, strictly convex finite `Glass` regions; explicit same background material, 1–4 exact native SingleRay sources, external detectors.
- **v15:** one or two actual native biconvex `SphericalLens` bodies with explicit radius/thickness/aperture and inside/outside indices.
- **v16:** one thick spherical lens plus finite native plane mirror.
- **v17:** two thick spherical lenses plus finite mirror; explicit v17-only native depth budget up to 16.
- **v18:** two thick spherical lenses, finite mirror and physical centred-gap native `Aperture`; v18-only native depth budget up to 16.

Ray encounters, face normals, refraction, reflection, total internal reflection, absorption and misses come from the genuine pinned native objects. No alternative ray tracing or prescribed route is introduced. Approximate Fresnel-off is stated. Observer results remain conditional on complete, hash-matched native execution; they are not detected physical images.

**Critical v18 fail-closed gate is intact and tested.** Actual outgoing native rays after lens/mirror callbacks are checked for possible forward proximity to any finite aperture endpoint. At or within the 0.01 mm guard distance—or if the observer cannot examine a ray state—**all v18 native observations are withheld even if PhyDemo emitted `simulationComplete`**; the native callback is still delegated once and rays are never changed. A baseline right-going refracted native ray at (50,5.617799867730811) mm motivated five independently authored v18 scene probes: gap-endpoint shifts of −0.03 and +0.03 mm remained numerically admitted; −0.005, 0 and +0.005 mm were explicitly `withheld-uncertain`. Reversed aperture orientation and translated near-world-boundary controls also withheld ±0.005-mm cases. These are conservative sample tests, **not** a universal floating-point proof.

Cross-family rejection preserves the existing v1–v13 and v19–v24 schemas, including v19 finite Beam, v20 decentered ideal lenses, v21 true half-glass, v22 prism Beam, v23 full-circle Beam and **reviewed v24 closed semicircular Glass with inside detectors/absorber**. No foreign scene gets v17/v18 depth 16 by implicit migration, and old qualified native results are not reused under changed materials/scene hashes. Normal detector counts, event availability, stale suppression and partial/Fresnel invalidation retain their qualifications.

## 3. Exact final CI and actual archived evidence

**11/11 exact-source PR workflows SUCCESS** at `6ea3c2edb4440e4e27b2f88f43660bd6ffed974f`. [Optical composition run 44578346034](https://github.com/physicsvigilante/opticsim/actions/runs/44578346034), job [135751867373](https://github.com/physicsvigilante/opticsim/actions/runs/44578346034/job/135751867373) and [planar/refraction run 44578346509](https://github.com/physicsvigilante/opticsim/actions/runs/44578346509), job [135751871340](https://github.com/physicsvigilante/opticsim/actions/runs/44578346509/job/135751871340) both record **1,032/1,032 Node24 tests passed**, zero failed/skipped. Node **24.19.0** and genuine **Google Chrome for Testing 158.0.8127.36** were used; all browser-dependent workflows explicitly require a working Chrome and do not skip/mock it.

The five original v14–v18 real-Chrome suites passed **9+9+10+10+13 = 51 checks**, with **2+2+3+3+4 = 14 PNG screenshots**. Each check JSON has `status=checks-passed`, no browser runtime error, no off-origin HTTP request, and genuine import/edit/rejection/export/reopen/native recomputation. The existing v19–v24 public native and real Chrome suites, base Chrome (27 checks/15 screenshots) and hosted smoke (5 checks/one screenshot) also passed. The six-case v18 native acceptance reports **three native completed, two correctly incomplete and one pre-native refusal**; v18's unsafe near-corner probes report withheld evidence, not false native success.

The builder downloaded and independently validated **the exact final CI artifacts**:
- [Optical native ZIP artifact 14557118216](https://github.com/physicsvigilante/opticsim/actions/runs/44578346034/artifacts/14557118216): SHA-256 **`adc34e8bf0a6938e1bc78a0b41d66c5a7fbc1bbb0f7f8a58390482f8b6a3bee7`** equals GitHub digest, **462 ZIP members CRC-clean**.
- [Native/Chrome planar ZIP artifact 14557632519](https://github.com/physicsvigilante/opticsim/actions/runs/44578346509/artifacts/14557632519): SHA-256 **`9e2d2a017dfa22150ae689f7955f1a0665cd036fe0b206b448cb9abbcf3c7ae8`** equals GitHub digest, **761 ZIP members CRC-clean**.

All **69** source input/report pairs in the optical ZIP exposing a report `inputSha256` or `originalInputSha256` were recomputed from the archived raw `input.json` bytes and **zero mismatches** were found. These are archived builder CI runs and builder archive checks, **not independently operated local PhyDemo or a blind original-JEE score**.

Earlier red-history is retained in GitHub: first source integration had one composition selector syntax comma omission; the next passed 1,031/1,032 with a legacy v21-vs-v24 provenance assertion; subsequent runs passed all Node tests but real Chrome caught literal model-label differences (v14 and v15), fixed in the final viewer while retaining old tested semantics and updating its integration-only Git blob SHA. Native physics modules and v18 corner guard were **not** modified in these fixes.

## 4. ONE independent review required — do not split this gate

Review the exact [PR #183](https://github.com/physicsvigilante/opticsim/pull/183) source SHA **`6ea3c2edb4440e4e27b2f88f43660bd6ffed974f`**, tree **`a8ea9878bee361c6ef05a83b9d5d913a3b8a7584`**, and identical tested synthetic merge. Read actual modified shared source, native tests, 11 CI workflow statuses/logs and downloaded evidence ZIPs; do not rely solely on this builder report.

Review focus: cross-version native `Glass`/`SphericalLens` correct index and local normals; source selection and geometric clearance; v18 after-refraction aperture endpoint uncertainty and **fail-closed** observer fault; true native delegate-once behavior; native depth 8/16 admission; actual detector/face readouts vs invented rays/images; rejected mixtures, stale/partial/critical evidence; old v19–v24 physical and viewer semantics preserved; original frozen historical review blobs vs updated integration-only UI provenance; exact Git tree and real Chrome evidence. Original v14–v18 standalone R2 reviewers' bounded physics modules can be reused by identical blob SHA without duplicating those entire reviews. This is one *new* review of integrated shared changes.

**Mandatory independent GitHub deliverable:** a complete Markdown report committed to default branch of `physicsvigilante/review_sandbox` at:

`projects/opticsim/pr-183/reviews/review-01-chat-b.md`

Reviewer must read back the committed report, then return its immutable permalink, actual review commit SHA, exact reviewed Opticsim source SHA and verdict **CLEARED FOR OWNER DECISION** or **CHANGES REQUESTED**. A chat-only verdict or an uncommitted report does not satisfy the review gate. If publishing fails, explicitly report not published. Reviewer must **not** modify Opticsim source, merge, or deploy.

**Builder disposition: candidate verified and held as DRAFT / UNMERGED; independent review pending.** Production `main` remains at `487314dcb7e74e7f16f5b711f950090e16400780`.
