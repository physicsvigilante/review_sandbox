# Verbatim-source and chronological origin registry

Migration from Opticsim project-local collaboration drafts into the central multi-sandbox review hub. **This record is additive. No original source, first-attempt Chat B review, or original GitHub comment was edited by migration.**

## Original review packet and protocol

Original shared-protocol first commit on **draft Opticsim PR #76**: `f67f8193d17f24035a896e59400c1e9f4cf2aa06`.

- [Original review protocol](https://github.com/physicsvigilante/opticsim/blob/f67f8193d17f24035a896e59400c1e9f4cf2aa06/collaboration/REVIEW-PROTOCOL.md) — Git blob `93ddb52a706ec1a69ab054eb6f3194997f666dad`.
- [Original review template](https://github.com/physicsvigilante/opticsim/blob/f67f8193d17f24035a896e59400c1e9f4cf2aa06/collaboration/REVIEW-REPORT-TEMPLATE.md) — blob `5d77433f2c260a20a5b9daa309e1e2e94dcdafc1`.
- [Original PR #75 request](https://github.com/physicsvigilante/opticsim/blob/f67f8193d17f24035a896e59400c1e9f4cf2aa06/collaboration/review-packets/pr-75/REQUEST.md) — blob `c52bd8e8ed198c2c78508a7ca0a411c7ae46dd37`.
- [Original reviewer prompt](https://github.com/physicsvigilante/opticsim/blob/f67f8193d17f24035a896e59400c1e9f4cf2aa06/collaboration/review-packets/pr-75/REVIEWER-PROMPT.md) — blob `b4ea4b24a9f6de58f77f5f908ab521925ba432fb`.

The first reviewer correctly noted the original files were **absent from Opticsim main and from PR #75's source tree**. They existed instead on the parallel, unmerged draft PR #76 branch. Neither this central hub nor the origin registry should rewrite those recorded 404 observations.

The Opticsim draft PR #76 second-pass packet commit is `92b09c59655dce0d9e56f4043c5b26d8cbb09c35`. [Original request](https://github.com/physicsvigilante/opticsim/blob/92b09c59655dce0d9e56f4043c5b26d8cbb09c35/collaboration/review-packets/pr-75/REVIEW-02.md) and [original prompt](https://github.com/physicsvigilante/opticsim/blob/92b09c59655dce0d9e56f4043c5b26d8cbb09c35/collaboration/review-packets/pr-75/REVIEWER-PROMPT-02.md) remain accessible by immutable GitHub SHA.

## Original separate-chat review

Exact original Chat B report: [Opticsim PR #77](https://github.com/physicsvigilante/opticsim/pull/77), review branch SHA `5d9f4db4dea2c216df25d672b35ff44bbc4d118a`, file `collaboration/review-results/pr-75/review-chat-b.md`, Git blob **`5da229366be37a4a962bd92d91b7f88d74390f53`**.

The file `reviews/review-01-chat-b.md` here is an **exact-byte copy of that original Git blob**. It was imported by Chat A, NOT freshly authored by Chat B in this hub. Original first-review label is `insufficient-evidence`; no proven production physics defect or independent human expert sign-off is claimed.

## Original Chat A response

- [Chat A triage comment](https://github.com/physicsvigilante/opticsim/pull/77#issuecomment-6894596523): acknowledges G-01 ref resolution and requires targeted E-02 evidence.
- [Targeted review prompt comment](https://github.com/physicsvigilante/opticsim/pull/77#issuecomment-6894629749): original PR #76 follow-up refs.
- The corresponding original GitHub comments remain untouched. This hub's `responses/response-01-chat-a.md` is an attributed snapshot.

## Implementation and saved checks

Source PR #75 exact head: `f4fddec213e04d733920399dc0eeea0b29a60dac` (tree `d8d70b08bddd3c07aa1f50247341423f124818b0`, base `c0d4e3048b9e0935cfd567e5f3c81aab23ddd823`).

Recorded GitHub Actions: [unified 43700823059](https://github.com/physicsvigilante/opticsim/actions/runs/43700823059), [refraction 43700823106](https://github.com/physicsvigilante/opticsim/actions/runs/43700823106). Original Chat B review gives artifact IDs and independently verified SHA-256 digests. Initial migration added **no new native/Chrome execution**; the independently authored second-pass review described below was published on PR #77 during that migration and is preserved separately. Central imports do not perform new tests.

Source documentation PR #76, independent review PR #77 and implementation PR #75 were all draft/unmerged when the central migration began; check live GitHub metadata before taking any merge action.

## Subsequent Chat B follow-up discovered during migration

A new second report was committed to the original review PR #77 during the initial central-repo setup. Its report source is commit `15799f20346c377f5519a8cfdc8f1cf57b390538`, `collaboration/review-results/pr-75/review-chat-b-02.md`, Git blob **`08942038407a156921a393488b6391f280f0bf98`**. Central `reviews/review-02-chat-b.md` is its **exact-byte imported copy**; the original was written by Chat B, but its import was done by Chat A.

New test-only draft [Opticsim PR #78](https://github.com/physicsvigilante/opticsim/pull/78), commit `7ccca3d255ac19e180eaa371851fdcbec2a2866f`, is an **immediate child of frozen source PR #75 head** and adds exactly one 129-line file `test/pr75-chat-b-02-adversarial.test.mjs`. There are no changes to product code, original fixtures, PhyDemo pin or original CI workflow. Independently confirmed all 11 [associated CI runs](https://github.com/physicsvigilante/opticsim/actions/runs/43717283882) successful; the unified raw job log records 729 Node tests / 729 pass and three new Chat B test groups. New checks exercised endpoint/reverse orientation, per-detector overflow isolation, and stale-evidence/callback guards. These are reviewer-authored headless native tests and controlled asynchronous callbacks; they are not independently driven new Chrome scenarios or human classroom evidence.

**Review sequence:** review-01 `insufficient-evidence` → review-02 `pass` **within the bounded targeted source/evidence scope**. Neither review authorizes a source merge. PR #75 remained at `f4fddec213e04d733920399dc0eeea0b29a60dac` during both. Preserve both original reports and their different conclusions.
