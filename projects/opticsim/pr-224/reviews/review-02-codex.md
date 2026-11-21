# Opticsim PR #224 independent focused review R2

**CLEARED for owner-authorized integration at this exact candidate.** The omitted opaque-contact and browser-provenance blockers are resolved.

| Identity | SHA |
|---|---|
| Candidate | `a34450ec5a37386d8921c0593965bcbd1defe995` |
| Candidate tree | `0413901b0c9c807d452939bf36b6da9240f2bcba` |
| Production base | `85c0534a4e5199bf989ae81a857b1d4077c2dbb6` |
| GitHub PR test merge | `a9d8f6eb80f7c1e1ee0f59bc0b75bbb78052c093` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

The test merge has the reviewed candidate and base as parents and exactly the candidate tree. [Initial blocked review](https://github.com/physicsvigilante/review_sandbox/blob/044f47fde8a680f3f35c6cfab5e3147c699c0d2c/projects/opticsim/pr-224/reviews/review-01-codex.md).

## Native qualification

The v35 scene requires one authored SingleRay, four separated axis-aligned finite Mirror segments and one interior opaque target. The native engine chooses encounter order. Qualification checks actual ray identity, continuity, authored brightness channels, finite-wall position and endpoint reserve, reflection direction, terminal Blocker absorption, completion diagnostics and one observed count per ID. The additional read-only check compares each already observed incoming wall segment with the authored opaque target. It refuses a leg crossing or numerically approaching that target before its wall callback.

I reproduced the original suppressed native hit on the first segment and independently suppressed one genuine early optical contact on the leg after two walls. In both mutations, the native test apparatus still produced four later wall callbacks and genuine final absorption. The corrected audit withheld all accepted observations in both cases. The unmodified native controls correctly absorbed at the earlier encounter. Independent controls with missing walls, displaced contact and origin, altered outgoing direction or brightness, inconsistent absorption, depth truncation and stale scene hashes also withheld the requested readings.

The independent 144-scene matrix varied aspect ratio, near-world-edge translations, target orientation, component order and launch reversal. All 96 qualifying scenes produced one true native reflection on each wall and final absorption, with the expected orders and 384 observed reflections overall. The remaining 48 scenes withheld results. Maximum deviations versus the separately reviewed unfolded controls were 7.76e−8 mm at wall contacts and 1.27e−7 mm from the synthetic target centres. The user-facing results are callback counts by ID. The synthetic geometry leaves the original A04 question in its separate symbolic workflow.

## Browser provenance and verification

The app provenance chain retains the v34 blob `94e5c54e8c9076856b75ac2cce7a574d9e24b3b1` and adds the exact v35 app blob `8e2d783783a5b953f58ac2264a1e0e6f7df11ce0`. The inherited provenance test and the independently replayed scoped test group passed, 39 tests in total.

Real Windows Chrome passed all seven v35 checks, including valid import, withholding after a launch change, fresh rerun and a qualified revision reopen with the exact edited direction. The normal v35 public CLI qualified all five requested readings after one emitted ray and five processed native segments.

All 11 exact-head hosted workflows passed. [Optical composition job](https://github.com/physicsvigilante/opticsim/actions/runs/44877062167/job/136763977825) passed 1,316 Node tests and the actual v35 Chrome acceptance.

The [hosted authoring archive](https://github.com/physicsvigilante/opticsim/actions/runs/44877062167/artifacts/14697050580) matched SHA-256 `c93f951a5126f732589941b6b2c4bfdc2658b1cf03fb0133d1d454fc0848108e`. All 30 scoped records matched independent execution byte for byte, comprising six v35 CLI records, twelve A04 analytical and native records, and six each from the historical v33 and v34 examples.

The [hosted browser archive](https://github.com/physicsvigilante/opticsim/actions/runs/44877062167/artifacts/14696492119) matched SHA-256 `4caca38156dd150569e681e8dd4ee4bc4127474fabe3d244c98b0d07610fdc0e`. It contains the same seven passing check identities on Chrome for Testing 158.0.8127.36, one screenshot and the qualified revision download.

Integration and post-merge verification remain separate gates.
