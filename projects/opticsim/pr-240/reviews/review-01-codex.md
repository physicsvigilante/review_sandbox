# Independent Codex review of Opticsim PR #240

**Decision: PASS.** All four application audit findings are resolved. The reviewed head is clear for owner-authorized integration.

| Record | Exact value |
| --- | --- |
| Pull request | [Opticsim #240](https://github.com/physicsvigilante/opticsim/pull/240) |
| Reviewed head | `d95b6d97cce54d14e86824bf8deaf090ae37beac` |
| Reviewed tree | `478f0c1822f2d7caf88b1ee8b20a260bca453ed4` |
| Base | `f1b967785f649ae085db48eeb760379bdba5c927` |
| Pinned PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251` |

## Findings

1. **B1 · Preflight and native Beam sampling.** The original v19 case used a width of `49.99999999999999` mm, density `0.25` and origin `(-100,-10)` mm. The old preflight estimated 12 rays, while native PhyDemo emitted 13 and reached the lens rim. The new preflight derives the sampling lattice from the compiled native segment and rejects the ambiguous half-integer case before tracing. Independent replay gave 12 and 13 completed native emissions at safe neighboring widths of `49.96` and `50.04` mm. Six existing configurations across v19–v23 still completed and their half-integer variants were refused. An independent sweep of 1,800 pinned Beam configurations matched all 55,030 emitted origins exactly.
2. **B2 · Source identity in sampled detector comparisons.** On the original case, changing brightness gave `8` emitted rays and signed relative power `-6.4` against the baseline `8/-3.2`. Changing Beam width gave `4/-1.6`. The actual observations remain available, and both comparisons are now `not-comparable` with `compatibleSourceEmission: false`. Independent width, brightness and source-position changes were refused. Identical illumination and a detector-only change still qualified, and deleting the per-source emission evidence withheld comparison. The check also retains the separately qualified point-source path.
3. **B3 · Delayed example requests.** On real Chrome I held actual localhost requests with DevTools protocol interception. Releasing the original stale success preserved the completed `y=42` edit at revision 5. Releasing a separate stale HTTP 503 preserved the completed `y=43` edit at revision 8. Both retained the completion state, status, title, selector and share URL. A newer example request also won against an earlier held request. I obtained the same results on the independently built candidate and the downloaded hosted static artifact.
4. **B4 · Optics-specific guidance on reopen.** The original v26 and v27 qualified packages completed in Chrome under their correct Beam/return arrangements. v26 labels the dielectric interface and mirror and states the Fresnel limit. v27 describes the two-face slab, the 1 mm separation from the rear face, the one-detector bound and the Fresnel limit. Both gave the same result on the downloaded hosted static artifact. The candidate's six-check Chrome suite also verified the v28 post-lens aperture label.

## Execution and provenance

- An isolated archive of the exact head rebuilt with Node 24.19.0 and pinned PhyDemo. The independent full Node suite ran 1,374 tests with 1,373 passing and one established Windows symlink-privilege skip. The hosted Linux suite passed all 1,374.
- All 11 exact-head pull-request workflows passed. The optical job used synthetic merge commit `402db5afd06669d55152362c3457cd27d7d3d057`. I independently reproduced its tree from the stated head and base. The hosted job ran the six audit Chrome checks. The independently rerun audit suite passed, and a separate Chrome 158.0.8127.37 run against the downloaded hosted demo passed six checks and produced four screenshots. [Optical workflow](https://github.com/physicsvigilante/opticsim/actions/runs/44894197651), [Unified workflow](https://github.com/physicsvigilante/opticsim/actions/runs/44894197546)
- The downloaded static artifact `14703556103` had SHA-256 `e7726c3df99c9a32f4e00ca8dff5c7890a1025f94935c24ec7f1a85af0eb1cfb`; its served `app.js` had SHA-256 `e4e9e48f636442180658192b50eddb5e491ad4f894122e6540819ac65043aa8f`. The independently generated Windows bundle had a different digest and received its own browser replay. The source ledger binds exact current app blob `641960864663c4ed3fde16888a79a33719eb0daa` and exact comparison source SHA-256 `2cb999f03bcb729b81cf7a5c931944d23da41822eb85431304b03d1b92b05925`, while retaining the preceding fixture records. [Hosted artifact](https://github.com/physicsvigilante/opticsim/actions/runs/44894197651/artifacts/14703556103)
