# M36d PR #87 — Corrected exact-source scientific R2 review request #02

**DRAFT production PR:** https://github.com/physicsvigilante/conductor_sim/pull/87

**Authoritative CURRENT source HEAD:** `e5fa85abe990abe8fdedc555e9313ac0420a56a7`
**CURRENT native Git TREE:** `523d02e95dbb4791acd630f9c535eb552262c606`.
**Released M36c base/main:** `6e6f53aa6762c327f58ef709379c41b1477c0931`, reviewed tree `c43134db1726dc2f1ff48b0b9a560dff090bf56d`.
**Frozen M36d charter-only before coding:** `466fa7090996cdd7d46e7fdd3e9f441042cb94c0`.

**Earlier scientific request #01 and prompt #01 ARE STALE.** They targeted superseded source HEAD `d607d1b9564c5b45e99a19cac3b33adcb33852f9` / TREE `d8ac1b3fbe7467b85ba0e32afdddc948a1458667`. DO NOT independently approve or review a mismatched candidate. The HEAD/TREE check is a primary gate.

## Source-science objective — authentic p26 SOLID conductor, not a fake hollow shell

Read the original [full science request](REQUEST.md) for baseline physics scope, then read **current source** [M36d preregistration](https://github.com/physicsvigilante/conductor_sim/blob/e5fa85abe990abe8fdedc555e9313ac0420a56a7/docs/m36d_charter.md), [implementation notes](https://github.com/physicsvigilante/conductor_sim/blob/e5fa85abe990abe8fdedc555e9313ac0420a56a7/docs/m36d.md), [minimal backend change](https://github.com/physicsvigilante/conductor_sim/blob/e5fa85abe990abe8fdedc555e9313ac0420a56a7/src/conductor_sim/mixed_radial.py), [real original and teacher models/viewer](https://github.com/physicsvigilante/conductor_sim/blob/e5fa85abe990abe8fdedc555e9313ac0420a56a7/tools/m36d_true_solid_sphere.py), [separate stdlib SI checker](https://github.com/physicsvigilante/conductor_sim/blob/e5fa85abe990abe8fdedc555e9313ac0420a56a7/tools/m36d_solid_reference.py), [35 positive/adversarial tests](https://github.com/physicsvigilante/conductor_sim/blob/e5fa85abe990abe8fdedc555e9313ac0420a56a7/tests/test_m36d_true_solid_sphere.py), [real Chromium inspector](https://github.com/physicsvigilante/conductor_sim/blob/e5fa85abe990abe8fdedc555e9313ac0420a56a7/tools/check_m36d_solid_browser.py), [full M36d workflow](https://github.com/physicsvigilante/conductor_sim/blob/e5fa85abe990abe8fdedc555e9313ac0420a56a7/.github/workflows/m36d-true-solid-source.yml).

Original `POTENTIAL_CONDUCTORS1.pdf` physical p26 Illustration 1 is a **SOLID conducting sphere** with symbolic radius R/charge Q, asks V(R/2) and V(3R/2). Historically M6 and M36c used a documented HOLLOW shell proxy for equal radial V/E measurements but *non-authentic source shape*. M36d actually authors `SolidSphere`, and the existing M5 viewer draws an actual filled metal sphere cross-section with **one outer surface and no inner cavity**. Source numerical R=.10m Q=+1nC is explicitly teacher-supplied, not an original given. A real changed-Q/changed-R/translated-centre negative world and a grounded empty-space world are two separately labelled **teacher hypothetical** solutions; source original apparatus count remains one.

## First full-source CI failures: preserve and recheck correction

First PR source `d607d1b...` triggered **one old M14b negative-admission test** that explicitly expected a lone SolidSphere to be `unsupported`. The new source's *sole physical capability* is precisely to admit that one solid. First [M21d workflow #44272283613](https://github.com/physicsvigilante/conductor_sim/actions/runs/44272283613) ended **FAILURE: 99 passed, 1 failed**, from `tests/test_m14b_mixed_radial.py::test_reject_invalid_shapes_and_point_sources_before_numerical_solver`. First [branch Python #44271994213](https://github.com/physicsvigilante/conductor_sim/actions/runs/44271994213) **FAILED 1, passed 2172**; paired Python 3.10 run was CANCELLED. These are genuinely red historical runs, not automatically green because new M36d-specific tests were all passed. Root cause was a **stale old test's invalid admission assertion**, not a source physics/ODE/FEMM/browser defect.

One corrective commit `e5fa85abe990abe8fdedc555e9313ac0420a56a7` changes **only the old M14b test** so it now recognizes a single genuine SolidSphere in source-free uniform vacuum as supported, while preserving ALL true invalid cases (point charge outside/inside, overlapping shells, shifted nonconcentric shells, two solid bodies). The production backend, original source runner, stdlib reference, Chromium inspector and original PDF bytes are unchanged relative to the failed old head. Check the exact source diff to verify this.

## Developer-controlled CURRENT exact-head evidence (not independent Chat B)

- [Corrected current source M36d PR workflow #44273099112](https://github.com/physicsvigilante/conductor_sim/actions/runs/44273099112) has **COMPLETED SUCCESS** on exact `e5fa85abe990abe8fdedc555e9313ac0420a56a7` after actual 35 focused physics/hostile tests, 3 genuinely recomputed solid-sphere states, 3 separate stdlib SI checks, and 3 offline Chromium static viewer frames with full screenshots. This is *developer-controlled* science, NOT independent reviewer tests.
- Corrected source full HEAD-associated Python 3.10/3.12, real FEMM5, 73-step historical Chromium, M36b/c compatibility, M21d negative domain and other 20+ workflows were **still running** when this request was prepared. Reviewer must fetch LIVE all current-source runs and insist they are COMPLETED/SUCCESS before a favorable independent review. Do not borrow old source green statuses.
- Old branch source-first run #44271994311 was also green but is pinned to stale old code and is not release proof.

## Novel independent reviewer-owned physical tests REQUIRED

1. Independently verify literal current HEAD and actual Git tree, and the complete current-head CI including M21d updated expectation and full Python+genuine FEMM+actual Chromium. Inspect first red runs and corrective diff. If source moved, STOP as stale-head.
2. Independently view the actual p26 original PDF page and actual rendered source/teacher screenshots, check truly filled solid cross-section `inner_radius=0`, no hollow ring or imaginary inner sigma, stable physical name, visible teacher input disclosures, no implied elapsed-time charge transfer.
3. Write original non-fixture **positive physics tests** on at least THREE different qualified input patterns: new positive/net sphere Q and radius, new negative Q with a *nontrivial translated 3D centre*, grounded empty-space or true zero isolated; compute signed E at +/− directions, V inside/outside, outer sigma with a separately derived `k=1/4πepsilon`. Verify the backend with real public API and real `ConductorResult`.
4. Write **negative physics tests**: original single hollow `SphericalShell` must still be rejected by `MixedRadialBackend`; one solid with any point source (inside or outside) must be rejected; two solids and nonsymmetric/overlapping mixed spheres must still be rejected; no hidden time-current. Actual metal boundary E must be refused, not replaced by average one-sided field.
5. Freshly generate real detached source/teacher native JSON on literal commit and independently mutate: source p26 page/Illustration, charge sign, physical name, imaginary inner radius, outer Q or σ, field vectors, signed teacher/grounded source attribution, fake original JEE count, fake hollow-rendered geometry. Check the no-production-import `m36d_solid_reference` rejects *each* for the intended reason after a positive control. Do not just rerun developer-written tests.
6. Verify full M36b/M36c source examples and M14b solver continue to work; **historical M6 hollow source remains unchanged** and M36d is a distinct source-faithful viewer, not a misleading rewrite.

Reviewer may run original authored Python probes in a separate `review_sandbox` GitHub Actions workflow checking out exact `e5fa85abe990abe8fdedc555e9313ac0420a56a7`, asserting `git rev-parse HEAD^{tree}` equals `523d02e95dbb4791acd630f9c535eb552262c606` and retaining first fails, actual native fields, SI reference values, and screenshots/artifact digests. Do not copy developer test method names and call them independent science. Do not misstate downloaded/rehashed ZIPs unless truly done.

## Deliverable and release authority

Publish an original independent report at `projects/conductor_sim/pr-87/reviews/review-01-chat-b.md` in `physicsvigilante/review_sandbox` (direct main or separate PR), with **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE** for exact current code. Check source geometry, genuine SI physical states, saved evidence, visible viewer, all current CI and unchanged physical boundaries. No claim of automatic PDF parsing, a new count of 3 original JEE problems, overall `N/30` solved percentage, point-induced-sphere charge or arbitrary 3D metal.

**REVIEWER DOES NOT MERGE OR AUTHORIZE RELEASE.** After no-blocker PASS, Chat A needs explicit separate owner approval, guarded expected-head merge, exact same native Git tree verified on main and full real postmerge main-push CI.
