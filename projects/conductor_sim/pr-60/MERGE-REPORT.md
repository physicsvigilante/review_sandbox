# M25a PR #60 — owner-approved merge and exact-main CI

**Status: MERGED; all 16/16 `main` post-merge push workflows completed SUCCESS.** Recorded 2026-11-15. This is Chat A's factual merge and CI record, not a new Chat B review, independent subject-matter certification, or deployment.

## Owner authorization and Git identity

- Source: [physicsvigilante/conductor_sim PR #60](https://github.com/physicsvigilante/conductor_sim/pull/60), M25a physically honest source-geometry observations for M24a and M24b.
- **Owner explicitly replied "approved" to the separate request to merge PR #60 after the independent scoped PASS**. An earlier "Review complete" was not treated as merge authorization.
- Exact frozen **reviewed head**: `caf496f54c3825adcab5615d214c8e11d4d24e5d`; [source tree](https://github.com/physicsvigilante/conductor_sim/tree/caf496f54c3825adcab5615d214c8e11d4d24e5d).
- Original base/first parent: `d27c504f0a2bb336784a4ce9116f84c992b915db`.
- **GitHub `main` merge commit**: [`c5cc9bf818f1c8d83901bcadef745cc29f6d1675`](https://github.com/physicsvigilante/conductor_sim/commit/c5cc9bf818f1c8d83901bcadef745cc29f6d1675).
- **Merged source tree**: `357d0cdcff95a1b23e70278b3dabdc09426eea2a`, identical to the exact source tree that Chat B passed; checked against both `main` branch metadata and the merge-commit Git tree.
- The merge's parents are exactly `d27c504f0a2bb336784a4ce9116f84c992b915db` and `caf496f54c3825adcab5615d214c8e11d4d24e5d`. PR #60 is merged/closed. The merge used GitHub's `expected_head_sha` lease to refuse a moving source head, and no extra production modification occurred.

## Historical independent reviews, preserved

- **[Chat B review-01](reviews/review-01-chat-b.md)**: `changes-requested` on old head `31ee492bd6070e8b74bf233c44a86de6301af827`. Original immutable report Git blob `4b0cc4f098e11a4c8aad56d35f03b1856263857d`, including its first-attempt failure evidence.
- **[Chat A corrective disposition](responses/response-01-chat-a.md)**: fixed F-01 ring projected endpoint markers on rotated qualified planes, F-02 strict sphere/shell slice inside/tangent/outside, F-03 trusted immutable scenario source identity binding; added regression and real-browser checks without changing electrostatic laws, motion integrators, guards, numeric policies, or qualification.
- **[Chat B review-02](reviews/review-02-chat-b.md)**: `pass` **strictly for F-01/F-02/F-03** at the final reviewed head `caf496f54c3825adcab5615d214c8e11d4d24e5d`, tree `357d0cdcff95a1b23e70278b3dabdc09426eea2a`. Independently performed 10,000 projection stress cases and two fresh browser replays of saved qualified tilted models; inspected original and corrected numerical/artifact evidence. It did **not** rerun the native simulation engine or certify teaching effectiveness.
- **[Chat A final disposition](responses/response-02-chat-a.md)**: no blockers, two optional nonblocking hygiene suggestions, no additional review or unreviewed production change.
- Preserve original first failing M25a CI [43723072406](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723072406) (Python invocation/import issue), rather than relabel it as successful. The reserved R2's first execution was an author-exposed prior-head run [43723348462](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723348462); corrected-head and post-merge repeats are **retained regressions**, not new blind transfer experiments. Review-01 and review-02 remain untouched.

## New post-merge CI — main branch only

GitHub's source-matched **`main` push run batch** at SHA `c5cc9bf818f1c8d83901bcadef745cc29f6d1675` has exactly **16/16 SUCCESS**:

| Workflow | Main push run | Conclusion |
|---|---|---|
| M19a prescribed fields and test-charge physics | [43731503997](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731503997) | PASS |
| M21d distant connected spheres | [43731504024](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504024) | PASS |
| M19e source identity and world-oriented ring viewer | [43731504113](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504113) | PASS |
| M19b fixed-source offline viewer and physics integrity | [43731504180](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504180) | PASS |
| M20a paired prescribed-field exploration | [43731504010](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504010) | PASS |
| M21e composed electric and gravity review | [43731503991](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731503991) | PASS |
| M22a structural composability review | [43731504154](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504154) | PASS |
| M17c motion authoring and review | [43731504111](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504111) | PASS |
| M18b held-source viewer and correctness | [43731504055](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504055) | PASS |
| M15c authoring and browser acceptance | [43731504110](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504110) | PASS |
| M21c composite symmetry review | [43731503976](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731503976) | PASS |
| M18c held-source authoring and independent physics | [43731503974](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731503974) | PASS |
| FEMM 5 real-solver validation | [43731504201](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504201) | PASS |
| M21b JEE source-faithful static E, V and work | [43731504072](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504072) | PASS |
| Python checks | [43731504286](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504286) | PASS |
| Visualization and source checks | [43731504006](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504006) | PASS |

**Important provenance:** GitHub also shows 1 later same-SHA run(s) on *other branches*, excluded from the `main` post-merge denominator. Branch identity and event matter; do not present branch tests as extra post-merge results.

### Critical result checks from actual merge-commit jobs

| Check | Verified result |
|---|---|
| [Python 3.10 & 3.12, run 43731504286](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504286) | **1,719 passed per interpreter**, 97 real-FEMM-dependent skips, 7 warnings per interpreter (six preexisting, one new benign test-class collection warning) |
| [Real FEMM 5, run 43731504201](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504201) | **97/97 passed**, zero skipped. Conductor nonregression only; not a projection geometry reference |
| [Focused source + Chromium, run 43731504072](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504072) | **470/470 focused tests passed**; M25a eight source-geometry browser scenes (including *both* 45° rotated planes) passed; reserved R2 retained regression passed; existing M24a/M24b browser and source checks passed |
| [Visualization/source, run 43731504006](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504006) | SUCCESS, including historical Chromium force, energy, cavity, elapsed-time and curved-path viewers |

The Python, focused and FEMM counts overlap; never sum them into an alleged total. Browser checks are actual Chromium execution of supplied viewer data, not user studies or proofs of general physical fidelity.

### Merge-head artifact references

GitHub's artifact metadata binds each to the exact `main` merge SHA. Digests below are **GitHub-reported**; this release record does not claim to have independently downloaded and rehashed these three new archives.

| Artifact | Main-branch run | Artifact ID | GitHub SHA-256 |
|---|---|---|---|
| JEE source + focused browser | [43731504072](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504072/artifacts/14168234505) | `14168234505` | `399fcbc6e80ef81fb6d983b04883e428a84cec0d9162e57bfe4048b81c8a9c22` |
| FEMM visuals | [43731504201](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504201/artifacts/14169205545) | `14169205545` | `d9a7fd5753b7963c99438627c78022846e78f5a09817dc695e181597d62dacfa` |
| Historical visualization | [43731504006](https://github.com/physicsvigilante/conductor_sim/actions/runs/43731504006/artifacts/14169350085) | `14169350085` | `0cf58e2d22efdf46e1de4fec5573b374d1354e4cb9877e06572a3d55c6f78c0d` |

## Scope, remaining limitations, and next cycle

M25a improves trustworthy 2-D apparatus/source projections without a new physics solver, off-axis ring/disk field calculation, conductor-response transient, or universal 3-D scene graph. Off-plane sources still contribute their actual 3-D field while omitted from the drawn slice. Authored source IDs and model revision digests are integrity/lineage assertions, not cryptographic verification of external provenance.

Two minor reviewer observations remain **nonblocking** and deferred rather than changing an already independently accepted exact head: alias an imported `TestChargeMotionSpec` in the correction tests to avoid one pytest collection warning; optionally test the tiny-body tangency glyph in standalone Chromium. No new review is warranted solely for unchanged M25a.

**M25a complete: explicit owner approval → exact reviewed source merge → identical merged tree → all 16 `main` post-merge workflows passed → permanent central evidence record.** The next new capability should use a new source PR and its own risk-classed review; this report is neither automatic merge authority nor a blanket physics certification.
