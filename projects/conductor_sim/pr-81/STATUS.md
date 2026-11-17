# M35a PR #81 — Project audit and multi-stage exploration status

**Developer audit and implementation validation complete; independent R2 review pending. PR #81 remains OPEN / DRAFT / UNMERGED. No merge is authorized by this record. One high-priority legacy finding remains OPEN.**

## Current immutable source target

- PR: https://github.com/physicsvigilante/conductor_sim/pull/81
- Candidate HEAD: **`49bab64b06cc4594934a27f9ddbb500c454ba150`**
- Actual candidate Git tree: **`f9d14fedd06659f5abf8f822b31bc7e6353f2a37`**
- Released M34b main/base: `a5113fa4cc924ac10cbb35b2f2d7ac80e11f1bde`
- Released base Git tree: `d0646c9e4d518008784c42c1fec1c48c81901a09`
- Frozen charter-only commit: `ba19e12c519df2338df5dbb9293e9fa7ebd611a8`
- Branch: `m35a-multistage-exploration-audit`
- [Full review request](REQUEST.md); [fresh independent reviewer prompt](REVIEWER-PROMPT-01.md).
- Required new reviewer output: `reviews/review-01-chat-b.md` — no independent verdict is claimed here.

The earlier candidate `81304609f04f87a54a689486ece5b2d3b5f3a963` / tree `0f3272a0094e2572d96882f8c151460c4ce77965` is superseded by the clean-checkout correction, not retroactively described as this validated head. Live PR/source/main identity was rechecked after the correction. Main remains the released M34b, not M35a.

## Audit outcome and what is still open

The full [project audit](https://github.com/physicsvigilante/conductor_sim/blob/49bab64b06cc4594934a27f9ddbb500c454ba150/docs/m35a_audit.md) inventories the entire released source and examines selected physical, numerical, authoring, evidence, architectural, documentation and CI boundaries. It is not an exhaustive proof of every possible geometry or every production line.

| Finding | Disposition |
| --- | --- |
| Nested native comparison changed into a same-world pair was accepted by the released fork runner | Fixed in candidate: current nested request invariants revalidated before numerical work and export |
| Mutated unknown observation mode reached a numerical study refusal instead of invalid-authoring rejection | Fixed in candidate; red-before/green-after probe now hits this precise boundary |
| Smallest-subnormal direction could normalize to `(1,1,0)` instead of unit length | Fixed only for the subnormal path; ordinary finite arithmetic and actual plane/source guards retained |
| Older EventSweepRun/TrajectorySweepRun can export contradictory `complete` without model/native result | **OPEN, high priority for authoritative export consumers: issue #80** |
| Stale current-release documentation | Current capability index and milestone navigation clarified; M35a explicitly draft |
| Duplicated CI and transitive numerical-reference coverage gaps | Added read-only dependency-aware PR/main reference gate; measured consolidation deferred |
| Main branch lacks server-enforced protection in inspected API response | Owner configuration recommended; no administration settings changed |
| Private-module coupling and repeated ancestor serialization | Shared bounded iterative per-call history resolver added; broader service extraction deferred |
| Clean-checkout audit/snapshot entry points failed because local PYTHONPATH hid imports | Corrected module invocations plus three clean-environment subprocess tests |

[Issue #80](https://github.com/physicsvigilante/conductor_sim/issues/80) is intentionally not closed or claimed fixed. The affected older sweep result wrappers are not admissible M35a source histories, but that containment does not repair their public export APIs. The next hardening plan is documented: characterize legacy callers, enforce status/model/native consistency at construction and every export, define the genuine issued-result trust boundary, test censored/refused results and mutated clocks/roots, and preserve valid legacy bytes/renderers. No blanket claim that all historical evidence wrappers are tamper-resistant is justified.

## M35a behavior and limits

Completed fork results can now be used as the authentic source of a subsequent physical fork. Later typed event inquiries can select worlds throughout that retained history. Previous model, assembly and native observation identities are preserved; only newly admitted worlds receive fresh integration during forking. A new event inquiry intentionally performs a fresh native M24a study for each selected admitted model.

A shared iterative per-call resolver validates the original graph and earlier stages chronologically, detects malformed/cyclic history before numerical work and discards its context after the call. Continuations opt into fork plan/run v2, and inquiries on fork history into inquiry plan/run v2. Original graph v1/v2/v3, direct fork v1 and original graph inquiry v1 remain unchanged for tested valid legacy inputs.

Cumulative bounds: eight fork stages, 32 requested nonbaseline worlds including rejected nodes, physical lineage depth 12, with 1..5 new worlds and at most 12 physical edits per stage. Direct first-fork limits remain as before. No history-budget reset, retired-source resurrection, matching-only-by-event-ID shift or postguard interpolation is allowed.

**Same-process exploration only.** This is not durable saved-session restoration after restarting Python, trusted imported JSON, merging divergent histories, concurrent editing, a new field/ODE/FEMM solver, arbitrary 3D physics or a scene graph.

## Final current-source CI: 23/23 completed SUCCESS

On 2026-11-17, a fresh exact-head query returned **all 23/23 PR-associated workflow runs COMPLETED/SUCCESS**, with zero pending, failed or cancelled runs. These are developer/CI results, not the new independent review.

| Validation | Result / actual run |
| --- | --- |
| Python 3.10 | **2,033 passed**, 97 real-FEMM-only skipped, 17 warnings — [#44126201718](https://github.com/physicsvigilante/conductor_sim/actions/runs/44126201718), job 134190548233 |
| Python 3.12 | **2,033 passed**, 97 real-FEMM-only skipped, 17 warnings — same workflow, job 134190549042 |
| Real FEMM 5 | **97 actual solver tests passed** in 21.15 s — [#44126201941](https://github.com/physicsvigilante/conductor_sim/actions/runs/44126201941) |
| Historical source/visualization/real Chromium | **SUCCESS**, all recorded workflow steps succeeded — [#44126201451](https://github.com/physicsvigilante/conductor_sim/actions/runs/44126201451) |
| M35a exact-source aggregate | **SUCCESS**, 42 focused tests, all 15 native/reference/audit commands, five full legacy byte comparisons — [#44126201544](https://github.com/physicsvigilante/conductor_sim/actions/runs/44126201544) |
| Supplemental local Python 3.13.5 | **2,033 passed**, 97 FEMM deselected, 17 warnings; all 15 reference commands completed and five legacy record files identical |

The 97 skipped tests in each ordinary Python job are not counted as real-solver success; the dedicated FEMM job actually executed them. The retained PDF benchmark reports 13 runnable, 6 blocked, 0 failed; blocked textbook cases are not passing simulations. Historical Chromium success does not assert a newly authored M35a browser interface.

The standard PR workflows check out GitHub synthetic merge `05998f8195487c7a98058857e533b3dfad8fbfbf` of current candidate into unchanged main. The new aggregate explicitly checks out literal candidate `49bab64...` and archives it. Those are different commit identities; do not silently call the synthetic merge the literal source HEAD.

## Reproduced corrections and numerical transfers

The corrected aggregate ran the same audit against exact released and candidate source with explicit import-path assertions. Released source accepts the mutated self-pair and malformed mode, and returns nonunit `(1,1,0)` for the smallest-subnormal direction. Candidate rejects the malformed requests at their intended boundaries and returns `(0.7071067811865475,0.7071067811865475,0)`. Each of the three outcomes is asserted separately, avoiding an earlier conjunction that could conceal a wrong probe boundary.

The standalone M35a numerical checker imports no conductor_sim. It verified **ten admitted worlds, 210 actual saved three-component SI samples, 126 literal comparison rows, four fresh native event inquiries and seven altered-evidence controls**. The separate audit checks E=-grad(V) for point, rod, full ring, sphere and shell examples; performs independent 16,000-element rod/tilted-ring Coulomb quadrature; and checks a nonuniform inverse-square circular orbit over a full period with 65 saved samples. These are finite developer-authored physical transfers, not separate reviewer science or universal error bounds.

## Artifact bytes and source identity actually checked

Corrected aggregate artifact **#14347851729** from run #44126201544 was downloaded. Its ZIP SHA256 was recomputed as **`0d8218bd9829125dc54749e13e102c31adc6f670498ce284bcce69bc70c3b7cf`**, matching provider metadata. All **59 manifest-listed files** passed individual SHA256 checks. Rebuilding the Git tree from its `candidate-source.tar.gz` gives **`f9d14fedd06659f5abf8f822b31bc7e6353f2a37`**, matching the remote Git commit object and the locally tested source tree.

The released baseline full-source artifact **#14337844992**, review run [#44108932124](https://github.com/physicsvigilante/review_sandbox/actions/runs/44108932124), was also downloaded, ZIP SHA256 `dbb6edc57080857ead78293cac6a3bdc727e38b901888b1fa400f92ab165320c` recomputed and its released source tree reconstructed as `d0646c9e4d518008784c42c1fec1c48c81901a09`. These are actual byte checks, not only copied provider-reported digests.

Current real-FEMM artifact #14346964447 was downloaded and its ZIP SHA256 recomputed as `af9f6a6d4cfb45bdf2bb8b0ccd8192bbb47c99c1c2421b04f6eb65508ef8eb75`. Its historical visualization artifacts do not substitute for the actual 97-test success in the FEMM job log.

## Original failure chronology preserved

Initial aggregate run [#44120203390](https://github.com/physicsvigilante/conductor_sim/actions/runs/44120203390) **FAILED** after 39 focused tests and the first fourteen reference commands passed. Command 15 could not import the checkout-only examples namespace. Candidate legacy-snapshot calls had the same latent invocation dependency. The failed artifact #14345335833 was downloaded and ZIP SHA256 `9dadd210c4f3548cc4fc1b432542cceacb17442993ccd50bdc575996e8429c3f` verified; failed command logs remain. The legacy comparison steps were skipped on that attempt and are not reported as passed.

Current correction uses module invocations and new subprocess tests with PYTHONPATH removed. It also repairs an audit-probe fixture that reached an earlier policy gate rather than the malformed-mode boundary. Earlier local duplicate-display-label and no-op-mass depth fixture errors were corrected without weakening native physical validation. Incomplete timed-out invocations were not counted as completed successful runs.

## Release gate

**Ready for a new full separate-context R2 review, not release.** Reviewer must challenge the audit corrections, unfamiliar multi-stage physics, original-object reuse, real event/refusal boundaries, cumulative history integrity, legacy byte compatibility, clean-checkout tools and issue #80 containment on this exact HEAD/tree. Publish `reviews/review-01-chat-b.md` with PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE and actual independently authored evidence.

Only an unchanged no-blocker independent review plus still-green current-source CI and separate owner expected-head authorization permits merge. After any approved merge, verify actual main Git tree and every triggered main-push workflow before claiming M35a released. Main remains M34b now.
