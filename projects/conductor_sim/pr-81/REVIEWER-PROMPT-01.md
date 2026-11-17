# M35a PR #81 — Fresh independent Chat B R2 review: project audit corrections and multi-stage physical exploration

You are **Chat B, a fresh separate-context reviewer**, not the implementation assistant. Independently challenge the actual candidate and publish your own findings. Developer tests and this packet are not an independent PASS. A separate ChatGPT context is not independent human certification.

## Frozen source to review

- Production PR: https://github.com/physicsvigilante/conductor_sim/pull/81 — **DRAFT / UNMERGED**.
- **HEAD: `49bab64b06cc4594934a27f9ddbb500c454ba150`**
- **Actual Git tree: `f9d14fedd06659f5abf8f822b31bc7e6353f2a37`**
- Released M34b main/base: `a5113fa4cc924ac10cbb35b2f2d7ac80e11f1bde`, tree `d0646c9e4d518008784c42c1fec1c48c81901a09`.
- Frozen charter-only commit: `ba19e12c519df2338df5dbb9293e9fa7ebd611a8`.
- Prior draft HEAD `81304609...` is superseded and had a failed aggregate audit entry point. Do not review that older candidate in place of this one.

Read [REQUEST.md](REQUEST.md), [STATUS.md](STATUS.md), repository-root PROTOCOL.md, REVIEW-RISK-POLICY.md and REVIEW-TEMPLATE.md. Read production AGENTS.md if present, and the pinned `docs/m35a_charter.md`, `docs/m35a_audit.md`, `docs/m35a.md` and `docs/current_capabilities.md`. Inspect actual source diff, especially prescribed_fields, motion_events, unified_observation_graph, graph_world_fork, graph_event_inquiry and the audit/CI tools. Independently fetch LIVE PR HEAD/base/state, actual Git tree and current CI. Changed HEAD/tree makes this packet STALE; do not silently endorse a floating branch.

## What must be assessed

The user asked for a project audit, error correction or resolution plans, followed by M35a. This candidate combines separately committed reproducible corrections with the bounded multi-stage feature. It does not assert every historic API is now safe or every JEE problem is covered.

**Request validation:** released M34b could accept an originally valid WorldComparison mutated into a self-pair, and a native node mutated to an unknown observation mode. Surrounding native request validation checked types but did not recheck all nested invariants at use time. Candidate revalidates current nodes/cases/edits/comparisons/questions/policy before numerical work and export. It must NOT reconstruct/renormalize genuine caller-owned model or event objects while validating them.

**Numerical normalization:** the smallest-subnormal `(ulp(0),ulp(0),0)` direction normalized to `(1,1,0)` in the old prescribed-field unit helper. Candidate scales only that under-resolved subnormal norm path. Ordinary non-subnormal calculations, M34a's one-ULP already-unit rule, zero/nonfinite/overflow refusal and full physical source/velocity/gravity qualification must remain unchanged. This helper touches more than the new feature: review its real source/event consumers, not only one unit test.

**M35a:** an authentic previously completed GraphWorldForkRun can now parent the next fork. Fresh native event inquiries may select admitted worlds from the entire retained history. A shared iterative per-call history context authenticates the root and each previous stage chronologically, detects malformed/cyclic history before physical work, preserves exact original model/assembly/native object identities and has no unsafe cross-call validation cache. Forking integrates only new admitted worlds; a new inquiry intentionally performs fresh M24a integrations of selected existing models.

Continuation opts into fork plan/run v2 and inquiries on fork history into inquiry plan/run v2. Original graph v1/v2/v3, direct M34b fork v1 and original graph inquiry v1 retain valid old output. Bounds accumulate over history: eight fork stages, 32 requested nonbaseline worlds including refusals, physical depth 12, 1..5 new worlds and 12 physical edits per stage. Direct first-fork limits remain the old 12-world/depth-six contract. No identity, retired-source or resource-budget reset is permitted.

**Important boundary:** this is repeated exploration in one LIVE Python process. No durable restartable sessions, native JSON restore, merging divergent histories, concurrent editing, new force/FEMM/ODE solver, unrestricted 3D or scene graph is included.

## Known high-priority open defect must remain explicit

[Issue #80](https://github.com/physicsvigilante/conductor_sim/issues/80) records legacy EventSweepRun/TrajectorySweepRun permitting complete-without-native exported entries after public dataclass replacement. It remains OPEN. Those older result wrappers are NOT accepted as M35a source histories, but containment is not repair. Independently evaluate that boundary and whether the separate compatibility-reviewed hardening plan is adequate. Do not write a blanket all-project evidence-integrity PASS that conceals this finding. A reviewer may still identify a release blocker if containment or claimed scope is unsound.

## Required independently authored probes

1. **Actual red-before/green-after corrections.** Reproduce the self-pair, malformed-mode and smallest-subnormal defects against pinned released M34b with the same inputs, then verify corrected behavior on candidate. Make sure each rejection reaches the intended condition, not an earlier unrelated policy check. Validate ordinary vectors remain exactly the original arithmetic and caller-owned event normals/objects are not mutated by validation. Test true out-of-plane forces, launch and gravity, invalid source geometry, zero/nonfinite and very small/large inputs within the documented contract.
2. **Unfamiliar multi-stage physics.** Author your own non-dyadic oblique qE+mg source graph and at least three successive real physical stages with structural, physical-property and replacement/removal operations. Include a retired-ID resurrection refusal, unaffected sibling and genuinely fresh inquiries on later-stage worlds. Compute independent three-component SI force, position, velocity and signed M24a detector roots at every actually saved timestamp. Do not import the developer's oracle or production field callback to calculate expectations. Include a separate nonuniform Coulomb/rod reference where feasible; honestly state untested geometry limits.
3. **Reuse and fresh computation.** Instrument actual native source assembly/revision/observation calls. Verify exact previous model/assembly/native object identities and canonical output bytes are retained across successive stages, and only NEW admitted worlds are integrated by each fork call. New inquiries must perform real new M24a studies, not root extraction from saved animation frames. Verify qualified parent models with refused prior observations versus physically absent parents.
4. **Cumulative history and hostile evidence.** Exercise stage count, total requested worlds including refused nodes, physical depth, edit budget and inherited node/stage identity reuse. Try cycles, wrong ancestor class, substituted stage/history/root hashes, forged ancestor parent/model/certificate, forged native status, False-for-zero clocks, shifted root/bracket and modified original graph after issuing a later stage. Test construction, execution and export. Confirm no stale cache can certify mutated history and detached JSON changes cannot modify future genuine exports.
5. **Event scientific limits.** Same ID with different geometry, direction, terminal property or numerical policy is not automatically comparable. Test authentic source guards with early located/later truncated events, terminal stops, multiple/opposite roots and actual shared saved times. No interpolation, afterguard extrapolation or invented complete-duration root pairing. Verify earlier question sets and new inquiry policies are bound to the appropriate actual run.
6. **Compatibility, tools and process.** Generate all FIVE full legacy records (graph v1/v2/v3, direct fork v1, original graph inquiry v1) using your own valid fixture under released and candidate source; compare bytes, not selected keys. Inspect clean-checkout module invocation without PYTHONPATH and verify baseline imports really originate in baseline. Check aggregate PR/main dependency triggers, explicit read-only permission, source pinning, first-failure evidence and absence of temporary publication artifacts. Investigate issue #80 without claiming it is fixed; assess the remaining architecture/CI and owner-side branch-protection plans.

## Current developer evidence — not your own independent review

**23/23 current HEAD PR workflows completed SUCCESS.** Python 3.10 and 3.12 each passed **2,033 tests**, with 97 live-FEMM-only tests skipped in general jobs. Dedicated real FEMM run [#44126201941](https://github.com/physicsvigilante/conductor_sim/actions/runs/44126201941) actually passed **97 solver tests**. Historical real Chromium/source workflow [#44126201451](https://github.com/physicsvigilante/conductor_sim/actions/runs/44126201451) succeeded. Check them live again before a verdict.

Corrected literal-source aggregate [#44126201544](https://github.com/physicsvigilante/conductor_sim/actions/runs/44126201544) passed **42 focused tests, all 15 native/reference/audit commands and five full legacy byte comparisons**. Its artifact #14347851729 ZIP SHA256 is `0d8218bd9829125dc54749e13e102c31adc6f670498ce284bcce69bc70c3b7cf`. Developer actually downloaded/rehashed ZIP, verified all 59 listed file digests and reconstructed source tree `f9d14fedd06659f5abf8f822b31bc7e6353f2a37`, matching locally tested and remote source. Independently verify as your tools permit; do not substitute provider metadata for your own byte checks.

The M35a standalone checker (no conductor_sim imports) evaluated 10 admitted worlds, 210 actual saved 3D states, 126 native comparison rows, 4 fresh event inquiries and 7 altered-evidence controls. Companion developer audit used E=-grad(V), independent 16,000-element rod/ring Coulomb quadrature and an analytic full-period Coulomb circular orbit with 65 samples. These are bounded developer experiments, not your independently invented cases.

**Preserve original failure:** aggregate [#44120203390](https://github.com/physicsvigilante/conductor_sim/actions/runs/44120203390) failed after 39 tests and 14 reference commands when its audit entry point could not import checkout-only examples; legacy comparisons were skipped, not successful. Corrected module invocations, import-root assertions, per-probe red/green checks and clean-environment subprocess tests are in current source. Original duplicate-label/no-op-mass reviewer-side development fixtures and incomplete local timeout were retained, not relabeled as passing executions.

## Required publication and authority boundary

Publish your NEW independently authored report at:

`physicsvigilante/review_sandbox/main/projects/conductor_sim/pr-81/reviews/review-01-chat-b.md`

Include exact observed source HEAD/tree, actual independently executed native experiments and artifacts or honest execution limits, reproducible findings/severities, explicit handling of OPEN issue #80, separate judgments for numerical physics, source interpretation, event completeness, in-process integrity, old compatibility, teacher usefulness and durable-session limitations. End with **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE**. Preserve all first-attempt failures and subsequent fixture corrections.

Do NOT alter production PR #81, mark it ready, merge or invent a PASS from developer CI alone. Your verdict does not authorize release. Unchanged exact-source no-blocker R2 PASS, all still-current CI green and separate owner expected-head authorization are required, then exact merge tree and every actual main-push workflow must be verified before declaring M35a released.
