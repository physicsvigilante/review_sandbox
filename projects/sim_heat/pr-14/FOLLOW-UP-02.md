# SIM_HEAT PR #14 — targeted R2 correction review 02

**Scope:** Re-review only the four demonstrated *viewer evidence-presentation* findings from the immutable [Review 01](reviews/review-01-chat-b.md), plus regressions and source/CI preservation. **Not** a renewed broad OpenModelica/physics architecture review or scientific qualification.

| Identity | Pinned value |
| --- | --- |
| Source PR | https://github.com/physicsvigilante/sim_heat/pull/14 — **draft/unmerged** |
| Original reviewed head | `281c5a45b536b698ea2b6896710e3cc49e20698b` |
| Corrected head | **`72991baed9eeb59ae523a90533a174bdb8dd6454`** |
| Corrected Git tree | `a8d6dcf7f2f3b2d83f496ce27aab15f0e4bb4e8c` |
| Unchanged base | `a33a0d79da405ff4c7191b9bfb94e096b10e2a9f` |
| Final CI | https://github.com/physicsvigilante/sim_heat/actions/runs/43750366629 — **PASS** |
| Final artifact | https://github.com/physicsvigilante/sim_heat/actions/runs/43750366629/artifacts/14175642800 |
| Original artifact SHA-256 | `33f4efd9034db15d0d4ee9394479f72d9150479072db887f1ef6949df04ee5e2`, 1,983,792 bytes |
| Preserved failed correction-CI attempts | [43749919396](https://github.com/physicsvigilante/sim_heat/actions/runs/43749919396) and [43750210292](https://github.com/physicsvigilante/sim_heat/actions/runs/43750210292) — **FAIL** in Chromium held-digest test sequencing |
| New Chat B report | `projects/sim_heat/pr-14/reviews/review-02-chat-b.md`, **Chat B only** |

Read [developer response-01](responses/response-01-chat-a.md) for exact defect dispositions and all failed/successful CI evidence. Review the [five-file original-to-current diff](https://github.com/physicsvigilante/sim_heat/compare/281c5a45b536b698ea2b6896710e3cc49e20698b...72991baed9eeb59ae523a90533a174bdb8dd6454) and source `docs/H2_02_REVIEW_CORRECTIONS.md` at exact current commit.

## Narrow acceptance questions

1. **F-01 blocker:** After loading valid bridge/D2 values, a deliberately mismatched case JSON/digest refusal must clear **every old case-bound quantitative field**, energy J, power W, model ID, run URL, plots, logical graph, observation/legend options, time/reversal and import statuses. New case state should remain recoverable, and a stale request must not re-populate old data.
2. **F-02 blocker:** Case switches increment an epoch and invalidate in-flight full native CSV imports after file reading, after async SHA/CSV parsing and before display or old error notifications. Examine a browser test holding the **actual SHA-256 promise** for a test-only repinned synthetic D1 CSV, switching to genuine D2, then releasing the digest. D2 must continue to show **its own** 21 preview samples and no D1 values/NaN. Do not misrepresent synthetic fixture as the genuine historical D1 CSV. Check the first two failed correction browser attempts and the final corrected sequencing; no SHA source-check bypass is allowed in production.
3. **F-03 major:** Recomputed catalog digests must **not** legalize a reversed D1 rod, swapped D2 temperatures/energies or swapped heated/cooled reservoir power. Validate strict port_a/from and port_b/to identity, exactly one owner of each Modelica port, owner-bound K/J/W, junction temperature tied to an endpoint on its physical junction, and refusal on phantom/one-sided ports. Do not infer a perfect source-authentication guarantee from structural consistency alone; trusted adapter and saved native evidence remain separately required.
4. **F-04 minor:** A zero touch (+/0/+, −/0/−) is not a reversal; opposite recorded signs with possible intervening zero(s) permit a *saved-sample* bracket (−/+ bridge still 1720–1730 s). There is no invented exact crossing or interpolated physical sample.
5. **Preservation and budget:** No pre-existing H1 physical/numerical/parser/runner/reference/verification code changed, no new OMC launches; D1, D2, bridge original model/MAT/CSV and case bundles remain unchanged. `diagnostic_only` and `nativeQualified=false` remain unchanged. Historical failed CI runs are retained and not silently reinterpreted.

## CI details and reviewer evidence boundaries

The exact-head final run passes **151/151 H1, 4/4 analytical, 4/4 adapter, 9/9 Node viewer tests** plus **real Chromium desktop/mobile** smoke and refusal/race screenshots. Original ZIP digest and CRC, saved head SHA and actual screenshots were examined by Chat A, but this is not independent Chat B execution. Chat B may independently examine screenshots and execute targeted source/Node/browser tests if tools allow; report failures and environment blocks truthfully. Real original native D1/D2/bridge input hashes have already been independently checked in Review 01, and no additional native solver call is required for these viewer-only corrections.

## Output and gate

Publish **one newly authored Chat B file** `reviews/review-02-chat-b.md` under this same central PR #14 directory, following [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md), with exact reviewed SHA and a **scoped** verdict: `pass`, `changes-requested` or `insufficient-evidence`. Do **not** overwrite Review 01, source code, or previous failed CI; do not merge. If no new substantive physics/evidence semantics were introduced, request targeted additional evidence, not an automatic broad new full R2 cycle. **Merge needs separate explicit owner approval** even if Chat B passes.
