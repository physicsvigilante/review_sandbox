# M25a PR #60 — targeted second-review request after F-01/F-02/F-03 corrections

**Review status: targeted independent-context re-review REQUIRED.** PR #60 is still DRAFT and unmerged. This is NOT a second whole-project physics review.

- [Original R2 request](REQUEST.md), **historical** head `31ee492bd6070e8b74bf233c44a86de6301af827`, tree `557047085fb294379acfc45266272b1ceb6b1de0`.
- [Unchanged original Chat B findings](reviews/review-01-chat-b.md), verdict **changes-requested**, review blob `4b0cc4f098e11a4c8aad56d35f03b1856263857d`.
- [Attributable Chat A response](responses/response-01-chat-a.md); this is NOT Chat B verification.
- **NEW source PR head:** `caf496f54c3825adcab5615d214c8e11d4d24e5d`.
- **NEW exact source tree:** `357d0cdcff95a1b23e70278b3dabdc09426eea2a`.
- [Source draft PR #60](https://github.com/physicsvigilante/conductor_sim/pull/60) (same base `d27c504f0a2bb336784a4ce9116f84c992b915db`).
- [Final-head source/diff](https://github.com/physicsvigilante/conductor_sim/tree/caf496f54c3825adcab5615d214c8e11d4d24e5d) and [GitHub comparison from previously reviewed head](https://github.com/physicsvigilante/conductor_sim/compare/31ee492bd6070e8b74bf233c44a86de6301af827...caf496f54c3825adcab5615d214c8e11d4d24e5d).
- **Report destination, authored only by Chat B:** `projects/conductor_sim/pr-60/reviews/review-02-chat-b.md` on central main or in a reviewer-only central PR. Do not overwrite `review-01`.

## Actual changes to review

1. **F-01 major ring endpoint markers:** new `_projected_major_axis` in `src/conductor_sim/source_geometry.py` computes the true principal projected semiaxis from both 2D rim-basis vectors (largest eigenvalue/eigenvector of `aa^T+bb^T`). The JS painter uses the resulting `projected_major_axis_uv`. R=0.3m, 45° in-plane x-axis ring formerly had false markers at ±0.212132 m; true rim extrema and corrected markers are ±0.3m. Preserve original 81-point rim path, and do not alter physical fields or treat the projection as an in-plane charged rod.
2. **F-02 narrow sphere/shell radial-boundary truth:** strict outside `abs(h)>R` now reports omitted source, exact tangent `abs(h)==R` reports `slice-tangent` point, inside `abs(h)<R` uses actual positive cross-section radius. Source qualification/proximity, E/V, guards and integrator are unchanged. Six tiny-body cases use actual qualified typed particle models.
3. **F-03 source-ID trust:** raw `source_geometry(spec, annotations)` remains an *author claim*, not externally authenticated; both integrated viewer call sites now pass a trusted immutable `PrescribedScenario`, requiring object-identical spec and exact source annotation tuple. A raw swapped source inventory can be newly authored, but cannot masquerade as the retained trusted scenario. HTML is not a trusted import format. Verify no invented cryptographic proof or new registration layer.
4. **New regressions:** `tests/test_m25a_review_corrections.py` adds 19 tests; native-qualified five in-plane rotations, true tangent/outside radial bodies and explicit false-binding rejections. `tools/check_m25a_source_geometry.py` adds two real native-simulated rotated ring cases with CanvasRenderingContext2D `arc` interception and independent pixel endpoint assertions, one in each M24a/M24b viewer. Existing offline/browser preservation and source guard rules remain.

These are seven changed source paths relative to the originally reviewed head (two viewer call sites, geometry helper, one new test file, browser verifier, documentation and existing observation workflow). **No new physical law, numerical algorithm, source qualifier, event semantics, saved numerical run schema, or motion integrator.**

## Current-head CI evidence and exact identity

GitHub final-head PR workflow runs: **16/16 completed SUCCESS**. Exact source head `caf496f54c3825adcab5615d214c8e11d4d24e5d`, tree `357d0cdcff95a1b23e70278b3dabdc09426eea2a`. CI synthetic merge `761e62f8927d84473e6ee7dedebeab52cf3d029f` has the **same tree** and is descended from the exact new head and original base; do not confuse checkout commit SHA with code head.

| Gate | Exact run / result |
|---|---|
| Full Python 3.10 and 3.12 | [43727877880](https://github.com/physicsvigilante/conductor_sim/actions/runs/43727877880): **1,719 passed, 97 real-FEMM skipped, 7 existing warnings** on each |
| Dedicated real FEMM 5 nonregression | [43727877795](https://github.com/physicsvigilante/conductor_sim/actions/runs/43727877795): **97/97 passed**, unchanged conductor physics only |
| Focused, source and real Chromium | [43727877885](https://github.com/physicsvigilante/conductor_sim/actions/runs/43727877885): **470/470 JUnit passed**, **8/8 M25a geometry browser** including both new tilted cases + **1/1 reserved retained transfer** |
| Existing visualization/source CI | [43727877916](https://github.com/physicsvigilante/conductor_sim/actions/runs/43727877916): success |
| Browser artifact | [14167187316](https://github.com/physicsvigilante/conductor_sim/actions/runs/43727877885/artifacts/14167187316): verified ZIP SHA-256 `350c8b90be04e5841ea2a8944dd5fc617bf79a433a6df3c1103be52bab632639`, archive `tree.txt` matches new tree |

Historical prior-head [source artifact](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723348462/artifacts/14165651772) and original Chat B report remain unchanged. Eight previous numerical JSON records from prior artifact and new CI are **byte-identical**. Historical first CI import failure [43723072406](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723072406) is still a failed first run, not a successful attempt; reserved R2 was first performed in prior-head [43723348462](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723348462) and is now a *retained regression*, not a second first execution. Counts overlap. FEMM does not independently test viewer source geometry.

## Reviewer tasks and scope limits

Independently check correctness of the **three original findings only**, with source lines, new browser evidence and ideally one fresh counterexample or local execution. Check that both 45° scenes have actual native-qualified x-axis motion and that markers meet real ±R rim extrema rather than a fabricated post hoc HTML change. Check 2×2 eigenvector degeneracies (face-on/elliptical math controls only—do not invent a qualified face-on axial trajectory), strict radial inside/tangent/outside, and exact-source scenario-ID guard. Confirm no changed 3D fields, off-plane field omissions, force/event/energy semantics, or hidden viewer painting. Check source tree/digest binding, preserving original reviewer failed tests as historical.

State **pass / changes-requested / insufficient-evidence** for this scoped correction; distinguish fresh independent tests from reused CI. Do **not** perform another broad general optics or conductor physics review, and do **not** merge source PR #60. If the PR head moves from `caf496f...`, report stale-head rather than transferring an old verdict.

This second ChatGPT conversation is independent in context, not necessarily an independently trained model or human expert. Source merge requires **separate owner approval after reviewer verdict**, followed by post-merge CI and central status update.
