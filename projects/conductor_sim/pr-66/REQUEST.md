# conductor_sim PR #66 — Independent R2 review request for M28b typed event sweeps

**Status: AWAITING SEPARATE CHAT B REVIEW.** [Source PR #66](https://github.com/physicsvigilante/conductor_sim/pull/66) remains **DRAFT and UNMERGED**. This review request is authored by Chat A (implementer), not an independent reviewer. The owner issued standing authorization to continue routine implementation/validated merges without repeated approvals, but asked to **interrupt for independent reviews**; no independent M28b verdict exists yet.

| Pin | Exact value |
| --- | --- |
| Project | `conductor_sim` |
| Source repository | [physicsvigilante/conductor_sim](https://github.com/physicsvigilante/conductor_sim) |
| Source PR | [draft #66](https://github.com/physicsvigilante/conductor_sim/pull/66) |
| baseSha/main | `abb085d41399b0a17429aa207614aad357ccd77c` (verified M28a merge) |
| **headSha to review** | **`414e69bd960bc71f3df65c7346e81bf58c1540b8`** |
| **source Git tree** | **`ac06b4990b8002394fa7965fa2391eda8ca9f16e`** |
| frozen charter commit | `d6959425783bed00a5f76f3ba2ebb8b6f5a4ec24`, before new production |
| risk | **R2 — physically/evidentially meaningful event matching, truncation and time bracket semantics** |
| reviewer report destination | `projects/conductor_sim/pr-66/reviews/review-01-chat-b.md` (Chat B authors only) |

Read [central protocol](../../../PROTOCOL.md), [risk policy](../../../REVIEW-RISK-POLICY.md), [report template](../../../REVIEW-TEMPLATE.md), exact-head [M28b charter](https://github.com/physicsvigilante/conductor_sim/blob/414e69bd960bc71f3df65c7346e81bf58c1540b8/docs/m28b_charter.md), [API and limitations](https://github.com/physicsvigilante/conductor_sim/blob/414e69bd960bc71f3df65c7346e81bf58c1540b8/docs/m28b.md), [composability contract](https://github.com/physicsvigilante/conductor_sim/blob/414e69bd960bc71f3df65c7346e81bf58c1540b8/docs/composability_contract.md) and [teaching evaluation contract](https://github.com/physicsvigilante/conductor_sim/blob/414e69bd960bc71f3df65c7346e81bf58c1540b8/docs/evaluation_contract.md). Independently confirm if source root `AGENTS.md` exists.

## New source capability

M28a already independently requalified and integrated genuine static-field charged-particle sweeps using M20b stable-ID revisions, M27b qualified curved ring motion and the original RK. M24a already located `PlaneEvent` and `VelocityReversal` numerical events using genuine physical-state force/root refinement. M28b adds a small **compositional adapter, not a new field law or integrator**:

- `src/conductor_sim/event_sweep.py`: `EventSweepPlan`, `run_event_sweep`, typed `EventSweepRun`/entries. Wrap a frozen M28a `TrajectorySweepPlan` with *one shared* tuple of 1..16 M24a typed questions and one `EventPolicy` numerical study policy. For baseline and 1..6 independent variations, re-create actual physical model from identical parent and call **fresh M24a `EventStudy` + `investigate_motion`**. **Never** infer events by interpolating M28a samples or browser frames.
- Each child is categorized individually as `rejected-physical-model`, `rejected-event-study`, `integration-failed`, `complete` or `censored` with original termination `duration`, `source-guard`, `terminal-event`, `event-unresolved`; keep true source IDs, physical origin/teacher hypotheses and SHA model ancestry. One child's failure does not silently erase siblings.
- Preserve **all** original M24a `LocatedEvent` root brackets, signed directions, residual units, actual saved time/force/energy, all original `initial_conditions`, `unresolved` candidates and exact M24a `outcomes`: `located`, `located-with-unresolved-candidates`, `unresolved`, `not-found-at-requested-resolution` or `search-truncated`. A guard-truncated search does not prove later detector absence.
- Cross-scenario `event_time_comparisons` pairs roots **only for the same event ID, exactly one root per scenario, both with outcome `located`**. Pairing returns the original two numerical brackets, an estimated difference of reported root sample times, and *numerical bracket difference interval* `[variation.lo−baseline.hi, variation.hi−baseline.lo]`. Multiple roots, unresolved and nonlocated questions are marked **unpaired**, never arbitrarily select first. Root-localization bracket is not rigorous full-ODE physical error. It is worth independently challenging whether unlike signed crossing directions under a direction-0 query should also be regarded as unpaired, not just recorded separately.
- `exact_time_trajectory_comparisons` reuse M28a matching of **literally identical actual saved physical timestamps**, not sample list indices; original event-specific terminal times may not align and must not be extrapolated.
- `src/conductor_sim/event_sweep_viewer.py`: standalone offline *event-time observation horizon chart and table* (not source-ring apparatus or particle trajectory space). It uses original saved event roots and source-specific author assertions, draws timelines only to each actual stop, labels all bracket/shift statuses, and safely escapes hostile model IDs/provenance. No browser ODE, event root solver, physical contact law or network.
- `examples/m28b_event_sweep.py`: ring charge + x=.275 m detector, analytic constant-E mass changes, a two-crossing detector case and an earlier-guard baseline with duration-complete gravity variation.
- `tests/test_m28b_event_sweep.py` and real Chromium `tools/check_m28b_browser.py`: independent analytic detector-time reference, 90° rigidly rotated mixed point/uniform system, stopped-model study refusal, source-guard truncation, multiple-root unpaired, malformed questions, JSON detachment and hostile HTML text; true 390px mobile offline browser testing.

## Physical/source provenance boundaries

Original source scanned workbook p12 Q40–41 gives ring A +10 μC, B −20 μC, each radius .30m, separation .40m, +world-y uniform electric field 100kV/m and test particle q=+10 μC. M27b's numeric mass .01kg, launch x=.20m, v_x=.1m/s, duration .015s and M28b's passive detector x=.275m, all sweeps and numerical policies are **teacher hypotheticals**. This is not the original symbolic-mass, released-from-rest, guided axial Q41 mathematical answer. The generic renderer must never assert this workbook provenance for unrelated uniform/point/gravity cases.

M28b does **not** add 3D free motion beyond original qualified planes, conductor response, induction, an actual charged-ring collision/contact, transport current, field-switch propagation or browser numerical physics. `source-guard` stops before an ideal source singularity; `ideal-stop-surface` is an authored ideal observation boundary, not a reacting conductor. M24a's event brackets are finite-resolution numerical localization, not mathematical guarantees of all roots or exact ODE trajectory error.

## Exact current-head CI and evidence

**All 16/16 workflow runs returned for final head `414e69bd960bc71f3df65c7346e81bf58c1540b8` PASSED**:
- [Python 3.10 and 3.12 run 43849797928](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849797928): **1,835 passed, 97 real-FEMM-only skipped, 11 warnings on EACH interpreter**.
- [Real FEMM 5 run 43849797863](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849797863): **97 passed**; this is conductor nonregression, **not** M28b's event-root validation.
- [Full offline Chromium + all legacy visualization run 43849798098](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849798098): **PASS**. Four new M28b pages: ring-detector (three located roots in three independently solved scenarios), uniform-mass (three located roots), multi-crossing (four total roots from two studies, marked unpaired) and gravity-guard (baseline source-guard, variation duration; no fabricated far detector). Each 390px viewport/document, 348px chart; zero JS/page/network errors.
- [Separate push Python run 43849788853](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849788853) also passed.
- [Exact-head full visualization artifact 14217990023](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849798098/artifacts/14217990023), GitHub **reported** SHA256 `dc05d29f011ad5cf8581eb5a9279585765b64254e2a1814da6f7cb9f81150cf0`. Chat A did **not** download or independently rehash this ZIP; do not claim independent rehash unless personally done. Historical CI `commit.txt` can identify a synthetic test-merge commit instead of PR head; verify the Git **tree** and actual source bytes, not merely this path label.

**Preserve first failed attempts rather than restating them as first-run passes:**
- [Initial run 43849386943](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849386943) and [visualization run 43849386867](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849386867): a Python return-string continuation syntax error in the new HTML renderer broke imports, not a failed physical law.
- [Next visualization run 43849638674](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849638674): new browser *test expectation* incorrectly compared JSON arrays to Python tuples for vector sweep values, fixed by canonical JSON-native comparison, without changing solved numeric physics or viewer.
- Final corrected head subsequently passed full CI and actual real Chromium.

## Reviewers: independent adversarial work

1. Build an **unfamiliar**, physically qualified fixed-source setup with at least one real detector/reversal and vary a true physical source or initial condition via stable ID. Compare true event time/root bracket against independent constant-acceleration or direct Coulomb + alternate ODE/root localization if possible. Merely rerunning M28b's built-in cards is weaker evidence.
2. Challenge same-event identity with multiple crossings and opposite signed crossing directions under a direction=0 query; verify the chosen root pairing rule is physically meaningful, not arbitrary. Distinguish a `not-found-at-requested-resolution` duration case from `search-truncated` after guard.
3. Challenge event-study-only refusal (physically valid revised launch on wrong side of authored ideal-stop surface), mismatched model lineage, inaccessible source IDs, arbitrary callback event, duplicate event IDs, invalid numeric policy and a variation that fails while another completes.
4. Challenge direct event shift bracket algebra (including negative shifts) and time-frame comparisons with event-specific terminal/non-grid states; ensure nothing is silently interpolated or swapped by index.
5. Inspect actual browser HTML/PNG and original numerical JSON for true source-specific attribution, saved event markers/brackets, absent postguard events, potential textual script injection, and 390px/no-network correctness. Distinguish artifact metadata and GitHub CI from reviewer-observed native tests.

Write a **new independent** `projects/conductor_sim/pr-66/reviews/review-01-chat-b.md` under central `review_sandbox` (or a review-only PR) using the standard template. Report exact reviewed head/tree and your own performed tests vs developer CI; verdict **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE**; list blockers and residual limitations. Do not modify or merge source PR #66. The owner's standing permission to continue routine merges applies **only after independent review PASS and exact-head validation**, not as a review waiver.
