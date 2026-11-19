# SIM_HEAT PR63 — CORRECTION-REQUEST-02: focused R2 review of F-01 and F-02

**Decision sought:** **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** for exactly the two changed read-and-refusal boundaries in the N2 checking-only comparator, not a new full H1 physics audit, native qualification or production merge.

## Pinned code and historical source identity

- [Draft PR63](https://github.com/physicsvigilante/sim_heat/pull/63), corrected HEAD **`6baba681ae1680e2fcae1ea8efbf0953afcb031b`**, whole Git tree **`27b6ce015d5ba8229ee5990d3fa1e90352fe3f45`**.
- [Independent review-01](reviews/review-01-chat-b.md) reviewer blob **`2daa8c65a055725b5b079043d5ecb225839e28d6`**, **CHANGES REQUESTED** for OLD head `232bca1737210a80e1fb8e41b7ec67c6248f6a9f` / tree `87dae90d2975516553d01af9040f7f62ef82071a`. The original report remains unchanged and accurately pinned to the old source.
- [Fail-first test-only commit `41d735e5...`](https://github.com/physicsvigilante/sim_heat/commit/41d735e500d306d0d235b5306eabf880734078ab) reproduced failures on unchanged implementation; [red CI 44482131234](https://github.com/physicsvigilante/sim_heat/actions/runs/44482131234) preserves 2 fail-first race test FAIL and 3 malformed-input ERROR.
- [Final corrective commit `6baba681...`](https://github.com/physicsvigilante/sim_heat/commit/6baba681ae1680e2fcae1ea8efbf0953afcb031b), parent test-only commit; [old reviewed→new comparison](https://github.com/physicsvigilante/sim_heat/compare/232bca1737210a80e1fb8e41b7ec67c6248f6a9f...6baba681ae1680e2fcae1ea8efbf0953afcb031b) changes **exactly three N2-specific files**: `compare.py`, its tests and README. Full PR remains four N2-only additions to reviewed PR62 base `29bc126967d180e7f92b0a8bc29f50ee17608eb7`.
- Synthetic PR CI commit `d7e368ed34ce6c5f04a5ecb1301972ca91f37a77` has **identical full source tree** to corrected HEAD, ordered parents base then head. Existing production H1, old comparator, Modelica, original T1-T facts/study, native runner/reference, historical C1, previous reviewer reports unmodified.

## Exact targeted challenges

**F-01 (BLOCKER, original-file TOCTOU):** Before correction `_original_inputs` verified source SHA on the first file read but parsed **second reads**. Reviewer's scratch race/reseal demonstration returned `checks_passed` with forged provenance as the parsed trust source. Corrected code MUST read each original facts, model and study file *once*, retain raw bytes, hash those exact bytes and parse *only the same verified snapshots*. Inspect real `_original_inputs` code and challenge a race or mocked `Path.read_bytes` mutation after the first digest. Personally execute a negative that changes **facts provenance**, **study content**, and if possible a source physical fact between former reads. The comparator must not consume the changed bytes or return success for freshly re-sealed caller data that differs from the true original. Show no unbound file second-read for any source. The test fixture's scratch files and original immutable Git sources must not be changed in the reviewer repository.

**F-02 (MINOR structured refusals):** Test malformed top-level primary/companion bundles `{}` / `[]`, missing `spec`, `spec=None`, oversized int allowance (`10**400`), non-UTF-8-encodable string with an unpaired surrogate, and optionally bad receipts/other nested malformed records. Public `compare_candidates` must return an actual `h1.model.Refusal` rather than raw `KeyError/TypeError/OverflowError/UnicodeEncodeError`. Verify that legitimate H1 `Refusal` is not silently converted to `checks_passed`, that existing passing and failed numeric comparator statuses are preserved, and that a forged allowable budget still depends on externally pinned pre-output reference seals.

**Unchanged main numerical path:** The reviewer previously independently checked full **77 exports +8 public observations**, both per-run verifier prerequisites, public signed temperature difference, exact planned common times (no interpolation), and PRIMARY allowance only despite four mismatched primary/dense float scales. Spot-check unchanged behavior, do not redo broad physics/reference assembly if no related source changed. No previous static-reference physical refusals may be relaxed.

## Verified hosted evidence (checking only)

- [PUSH 44482539578](https://github.com/physicsvigilante/sim_heat/actions/runs/44482539578) **SUCCESS**, artifact `14509540394` GitHub SHA-256 `0ab5c25265fecb7be40701b002b1a6a2c4f67819a710e8767458b3f0aef56319`.
- [PR 44482548998](https://github.com/physicsvigilante/sim_heat/actions/runs/44482548998) **SUCCESS**, artifact `14509501395` GitHub SHA-256 `8d9313c56b39ccfd3493a43207610ab38df00c260e114c8afc8740f95754bd4e`.
- Each ran **16 N2 comparator +17 N1 interval +34 N1 plan +152 original H1 =219 distinct PASS** (not additive across hosts/runs); docs parity PASS, fixed original SHA gates and original legacy seven static 100x refusals/eight native blockers retained. Full candidate raw source and runner unchanged by these N2 corrections.
- These ZIP digests are GitHub API reported; reviewer may independently CRC/SHA/tree verify if desired. An outside-repo scratch fake provenance is a synthetic trust-boundary test, **not genuine native output**.

## Reviewer output and STOP

Publish exactly one newly authored independent report `physicsvigilante/review_sandbox/projects/sim_heat/pr-63/reviews/review-02-chat-b.md` with own personally executed counterexamples, checked exact source HEAD, attributed GitHub versus personal evidence, and verdict **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** for this correction ONLY. Preserve review-01 CHANGES REQUESTED on its old source SHA. If new blocker: regression and new SHA, then narrow another review. Don't grant native acceptance, external oracle certification or merge.

**No OpenModelica query/install/build/launch, no native MAT, no old reference repair, no C1/archive rewrite, no PR63/62/60/59 merge or deployment.** Seven original checking-centre failures, eight execution blockers and lost original private scorer remain.
