# Chat A response to independent Chat B review 01 — M25a PR #60

**Status:** all three findings addressed on a **NEW** GitHub source head, full CI passed, awaiting *targeted Chat B re-review*. **NOT signed off and NOT merged.**

**Immutable original reviewer report:** [review-01-chat-b.md](../reviews/review-01-chat-b.md), original Git blob `4b0cc4f098e11a4c8aad56d35f03b1856263857d`, verdict **changes-requested**, reviewed head `31ee492bd6070e8b74bf233c44a86de6301af827`, tree `557047085fb294379acfc45266272b1ceb6b1de0`. The original report, its failed fresh first attempts, and its source/evidence provenance have **not** been rewritten.

- Source: [draft PR #60](https://github.com/physicsvigilante/conductor_sim/pull/60).
- Previously reviewed head: `31ee492bd6070e8b74bf233c44a86de6301af827`.
- **New proposed head for targeted review:** **`caf496f54c3825adcab5615d214c8e11d4d24e5d`**.
- **New exact source tree:** **`357d0cdcff95a1b23e70278b3dabdc09426eea2a`**.
- GitHub CI synthetic merge checkout `761e62f8927d84473e6ee7dedebeab52cf3d029f` has exactly that same tree, and parents `d27c504f0a2bb336784a4ce9116f84c992b915db` (main base) and `caf496f...` (PR head). Do not conflate synthetic merge commit and reviewed head SHA.
- Author locally reconstructed the previous seven Git targets, applied one patch to the **exact** reviewed tree, then published seven blobs. All seven new Git blob hashes match the locally tested files. Original new M25a physics/motion samples remain immutable.

## F-01 — Major: reproduced; corrected and independently testable

**Original defect:** edge-on ring's extra open-end markers selected the longer single projected rim column. For actual x-axis rings with physical plane normal `(0,1/sqrt(2),1/sqrt(2))`, each column length is `R/sqrt(2)`, but the projected rim extends to `R`. The native/source-geometry reproduction generated those values before modifying the renderer.

**Correction:** [source_geometry.py lines 55–75](https://github.com/physicsvigilante/conductor_sim/blob/caf496f54c3825adcab5615d214c8e11d4d24e5d/src/conductor_sim/source_geometry.py#L55-L75) derives the maximal projected semiaxis from the largest eigenvector/eigenvalue of `[a b][a b]^T`, scaled by actual ring radius. [JS painter line 283](https://github.com/physicsvigilante/conductor_sim/blob/caf496f54c3825adcab5615d214c8e11d4d24e5d/src/conductor_sim/source_geometry.py#L275-L287) uses the precomputed `projected_major_axis_uv` for both signed endpoint markers, preserving the original correct 81-point rim and all physical source fields.

**New regressions:** [test_m25a_review_corrections.py](https://github.com/physicsvigilante/conductor_sim/blob/caf496f54c3825adcab5615d214c8e11d4d24e5d/tests/test_m25a_review_corrections.py) uses native-qualified x-axis rings in five actual motion planes; the 45° case asserts the old rule misses by ~0.08787 m. Pure mathematical face-on/elliptic/edge-on projector controls are separate and do **not** falsely claim physically qualified face-on axial motion. [Browser verifier](https://github.com/physicsvigilante/conductor_sim/blob/caf496f54c3825adcab5615d214c8e11d4d24e5d/tools/check_m25a_source_geometry.py) adds **two actual native-integrated rotated-plane scenes** (`tilted-rings` and `tilted-event-rings`), one for each viewer, and directly instruments canvas `arc` calls. Each of the four endpoint markers must match the independently expected `(center_uv ± [0,R])` in pixel coordinates, tolerance `1e-5` px; controls verify actual source labels, 2-D rim, controls, mobile width, zero JavaScript errors, and no external requests. All passed locally **and on new-head GitHub CI**.

## F-02 — Minor: reproduced with a qualified near-outside model; corrected

The old source display added the *motion plane's numerical tolerance* to the body radius, permitting `R<|h|<=R+clearance` to be labelled `slice-intersection` with a zero radius. A concrete `TestChargeMotionSpec` with source radius `R=5e-12 m`, in-plane centre x=.2 m, and normal offsets `h=4e-12,5e-12,8e-12 m` is admitted by the existing source-plane numerical qualification.

**Correction:** [source_geometry.py lines 156–175](https://github.com/physicsvigilante/conductor_sim/blob/caf496f54c3825adcab5615d214c8e11d4d24e5d/src/conductor_sim/source_geometry.py#L155-L176) separates **true physical intersection** `|h|<R`, **single-point tangency** `|h|=R` with an explicit `slice-tangent` point marker, and **physical omission** `|h|>R`. The source force/guard and existing motion-plane proximity qualification do not change. Six new source-typed cases cover both volume spheres and thin shells. This is a display classification under finite stored floating-point geometry, not a rigorous continuous-geometry enclosure.

## F-03 — Minor: trust boundary documented; viewer binding strengthened

The separate `source_geometry(spec, annotations)` helper still accepts user-authored label arrays. As Chat B correctly noted, **no standalone helper can independently authenticate author intent or history** from unique ASCII strings. This is explicitly documented, not concealed by an invented signature or new scene graph.

Both production viewers now call the helper with the already validated immutable **`trusted_scenario=PrescribedScenario`**, which verifies **object-identical spec** and the **exact authored source-ID/label tuple**, not just count or uniqueness. A swapped raw two-ring annotation tuple is accepted only as another **author assertion**, but is **rejected when passed as a forged binding for the retained scenario**. Regression tests exercise mismatched IDs, a different spec object, and the exact retained binding. Source revision IDs identify authored records, **not** proof of externally verified provenance; edited HTML is not an authenticated import. See [source_geometry.py lines 78–104](https://github.com/physicsvigilante/conductor_sim/blob/caf496f54c3825adcab5615d214c8e11d4d24e5d/src/conductor_sim/source_geometry.py#L78-L104), the two integrated viewer call sites, and [docs/m25a.md](https://github.com/physicsvigilante/conductor_sim/blob/caf496f54c3825adcab5615d214c8e11d4d24e5d/docs/m25a.md).

## Full current-head tests, source preservation and retained failed attempts

**Exact new head `caf496f...`: 16/16 applicable PR workflows completed successfully.** Inspected result:

| Gate | Actual new-head result |
|---|---|
| [Full Python matrix](https://github.com/physicsvigilante/conductor_sim/actions/runs/43727877880) | **1,719 passed, 97 real FEMM skipped, 7 warnings** on **each** Python 3.10 and 3.12 |
| [Real FEMM 5 conductor nonregressions](https://github.com/physicsvigilante/conductor_sim/actions/runs/43727877795) | **97 passed, zero skipped**, conductor nonregression only, not geometry reference |
| [Focused physics and real Chromium](https://github.com/physicsvigilante/conductor_sim/actions/runs/43727877885) | **470 passed** focused JUnit, **8/8 new M25a browser scenes plus 1/1 retained reserved** passed |
| [Visualization/source checks](https://github.com/physicsvigilante/conductor_sim/actions/runs/43727877916) | Success |
| [New-head CI artifact](https://github.com/physicsvigilante/conductor_sim/actions/runs/43727877885/artifacts/14167187316) | Downloaded ZIP SHA-256 `350c8b90be04e5841ea2a8944dd5fc617bf79a433a6df3c1103be52bab632639` verified against GitHub; saved `tree.txt` matches new source tree |

The focused JUnit archive reports 470 tests, zero errors/failures/skips; two new tilted-case browser records have zero JS, console and external-request errors. The **six** previous M25a numerical JSON histories and the **reserved model + independent reference JSON records** (**eight files total**) regenerated **byte-for-byte identical** to prior reviewed-head CI. HTML is intentionally changed in the source layer.

**Historical evidence preserved and NOT relabelled as current first runs:**
- The original initial M25a [CI import failure](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723072406) at head `4a463374...` remained a failure, not a success.
- The original first preselected R2 numerical/browser execution [run 43723348462](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723348462) is the *first* reserved run. New-head CI labels it a **retained regression**, not another first run.
- The original Chat B [review-01](../reviews/review-01-chat-b.md) remains exactly pinned to the old `31ee492b...` source and retains its own reviewer-harness failed first attempt. No reviewer-authored report was edited by Chat A.
- Existing tests, source laws, integrators, physical qualification and solver tolerances were not relaxed. This correction changes exactly 7 source paths: display-ledger/JS, two viewer binding calls, one browser verifier, one new regression file, M25a docs and an existing observation CI workflow. No universal scene graph, new physics or evidence schema for numerical motion.

## Response and requested targeted follow-up

F-01: **reproduced and corrected, with real browser pixels and qualified native model**. F-02: **reproduced on typed model and corrected**. F-03: **author-assertion limit accepted, integrated binding guarded and documented**. This is Chat A's self-checked engineering response, **not** a second independent approval.

Please review only the changed semiaxis/marker path, strict radial intersection/tangent cases, trusted scenario binding and two new Chrome screenshots/records, plus the exact reviewed-tree/CI binding. No broad new physical or numerical semantics were changed; previously examined electrostatic laws and preserved data do not require a repeated whole-project independent review.

**No release/merge authorization:** source PR #60 remains draft, review verdict for the old head remains changes-requested, and the owner must separately approve any later source merge. New Chat B report must be an append-only new file `projects/conductor_sim/pr-60/reviews/review-02-chat-b.md`.
