# Independent R2 targeted review — Opticsim PR #146, observer local-root P1 correction

**TARGETED R2 SOURCE REVIEW ONLY. DO NOT MERGE.** The independent [PR #145 R1 review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-145/reviews/review-01-chat-b.md) returned **CHANGES REQUESTED** due to a reproducible P1 in a **test-only mathematical oracle**. This new child candidate is not approved by that prior review, and the previous R1 verdict remains frozen and historically correct.

## Exact source and CI identity (independently verify)

- [Draft PR #146](https://github.com/physicsvigilante/opticsim/pull/146), base is frozen research PR #145 HEAD `a2d0adfe692bc837656a4dd09edc84ab4f490d2f`, **not** production main.
- **Corrected HEAD:** `2621c08812eb389b70a3e4fa246537ca50b3bc4d`.
- **Corrected source Git tree:** `c8c682f6fbc4f1dcb5827f82fe9768f3f11683d9`.
- Temporary main-target [CI-only PR #147](https://github.com/physicsvigilante/opticsim/pull/147) synthetic merge **`e1ed85400bf9a0f34c648e0781bf34e56e3704aa`**, with **identical tree** `c8c682f6fbc4f1dcb5827f82fe9768f3f11683d9`. Parents: actual production main `d3509e82fb65d81aabe336666851f8f2962623f4` followed by corrected HEAD. Check actual Git objects/parents, not PR text.
- Diff to frozen #145: **only** `test/jee-observer-native-feasibility.test.mjs` and `docs/JEE-OBSERVER-REFRACTION-NATIVE-RESEARCH.md`. No production `src/`, canonical schema, native PhyDemo, adapter, browser, prior reviewed source or release decision changes.
- Temporary #147 is a CI harness and must be **closed unmerged** after evidence capture; no main integration implied.

## P1 and independently supplied counterexample

The old test-only `shootingReference` bisected absolute tangent coordinates `q` near 9000 mm, then asserted an absolute unscaled Snell residual ≤`1e-12`. Valid physical example: infinite plane x=0; source S=(-0.02,9000) mm, observer O=(0.02,9000.01) mm, source index 1.5, observer index 1. Source/observer distances from plane are 0.02 mm, within the stated 0.01-mm clearance, and positions within ±10000 mm. Independent R1 reconstructed the physical stationary root via high-precision local geometry and showed the old world bisection stagnates, returning residual ∼`1.67e-10` before it even tries native PhyDemo. This is **not a solver/PhyDemo optics defect** and does not discredit original source (-60,0) → observer (100,40) native evidence.

## Child correction and precise claims to audit

1. Solve for **local tangent offset `v=q-u_s`**, with span `u_o-u_s`; bracket between 0 and span (ordered). Calculate residual from `ns*v/hypot(ds,v)-no*(span-v)/hypot(do,span-v)`; detect adjacent local binary64 midpoints. Fail closed with `status:'numerically-unstable',reasonCode:'LOCAL_ROOT_UNRESOLVED'` if local root cannot be certified, rather than generic assertion.
2. Construct analytical incoming/outgoing direction in the local normal/tangent basis. Reconstruct world crossing Q only after local solve; independently check *represented world-coordinate* Snell residual. If it is >`1e-12`, return **`numerically-unstable / WORLD_COORDINATE_ROUNDING`**, with null Q, initial direction and apparent point. This is conservative withholding, not proof that a physical root is absent. Preserve only explicitly noncertifying internal numeric diagnostics. **No native ray authored** for unstable references.
3. A *test-only* conservative `cos(refracted normal angle) < 0.02` threshold withholds as `NEAR_GRAZING_EXIT`. Distinguish the physical Snell critical angle from this arbitrary research acceptance tolerance. Near-but-nonzero axial displacement below 1e−10 mm is `NEAR_AXIAL_INFERENCE`; exactly axial remains a real native ray but its single-ray virtual-depth inference is null.
4. Ensure all original positive single-ray cases still compile and propagate using unmodified pinned native PhyDemo, with real finite detector positions, complete/hash-bound methods, Fresnel omission warning and stale/incomplete suppression. Do **not** relabel analytically reconstructed intersection `Q` as directly recorded native `pointMm`.
5. Independently check whether world residual certification, local-to-world reconstruction, sign conventions, coordinate-representability check, root-stagnation and numeric-status priority are correctly implemented for negative signed tangent span, rotated normals, equal/reverse indices, and physically bounded but challenging coordinates. If source metadata is invalid, no fabricated path should be accepted. A returned stable reference does **not** prove broad physical visibility, ray ancestry, refracted wave power or a perceived image.

## Actual builder evidence to inspect (not an independent rerun)

**11/11 standard GitHub Actions workflows successful** on exact source HEAD. [Optical/native run #44289842505](https://github.com/physicsvigilante/opticsim/actions/runs/44289842505), job `134751896241`, and [plane-mirror run #44289843134](https://github.com/physicsvigilante/opticsim/actions/runs/44289843134), job `134751899142`, record **799/799 Node tests passing**, including both new R2 named regressions.

The key new builder log:
`JEE_OBSERVER_LOCAL_ROOT_WITHHELD` -> `status:numerically-unstable`, `reasonCode:WORLD_COORDINATE_ROUNDING`, `localResidual:0`, `worldResidual:-4.1488867896788406e-11`, `nativeRayAuthored:false`.
Named R2 regression tests for 9000-mm translation cancellation and near-critical observer/near-axial withholding pass.
The original `JEE_OBSERVER_NATIVE_ARRIVAL` sample still reports independent reference Q=(0,11.2461557712) and **actual native** detector hit (100,40) mm at the expected outgoing direction; `JEE_OBSERVER_NATIVE_SUPPRESSION` still records withheld stale and incomplete results.

**Independence boundary:** GitHub Actions Node/PhyDemo/Chrome are builder-run. Reviewers should inspect actual source, Git identities, logs and independently recompute geometry; do not claim to independently rerun the native engine unless genuinely done.

## Requested R2 review deliverable

Independently inspect all changed source/test/documentation and relevant existing v5 interfaces. Check the P1 counterexample using JavaScript binary64 **and** mathematically reason about near-grazing/near-axis and native sampling boundaries. Identify P0/P1 blocking findings or explicitly state none; record nonblocking recommendations and exact evidence provenance.

Publish `projects/opticsim/pr-146/reviews/review-01-chat-b.md` in review_sandbox with exact SHA/tree, concrete issue priorities and verdict **CLEARED FOR NEXT SCOPED DEVELOPMENT / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. **No source edits, no PR merges, no retroactive rewriting of PR #145 R1 or old #141/#143/#144 reviews.** This is a test-only research correction, not release authorization. Branch protection issue #123 remains unresolved.
