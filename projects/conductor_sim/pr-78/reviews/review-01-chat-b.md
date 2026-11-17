# M34a PR #78 — Chat B original independent R2 scientific / evidence review #01

**Outcome: PASS (bounded scientific source-qualification scope; no demonstrated candidate production blocker).** This is a fresh separate-conversation LLM review, NOT an independent human physics certification or owner merge authorization. Do not represent earlier developer CI or reviewer-hub developer scripts as these new tests.

- Source PR: https://github.com/physicsvigilante/conductor_sim/pull/78 — **OPEN / DRAFT / UNMERGED** when checked.
- Reviewed exact candidate HEAD: `95bbb1b39e650e1db633ea8cef9c8ad4e129dcce`
- Independently fetched Git TREE: `87b1271d437a5bcc58f9328cca9773827a3da7d8`
- Live released `main` and PR base: `28f93622fd8cfb816e23ef36027992b1a5aaded8`; released tree `2ce33c744440248b4491c38f4ccb673636c08035`
- Frozen charter commit: `d422011f0927815b6f39d4154c67694ea804deb2`.
- Reviewer: Chat B, GPT-6, separate ChatGPT conversation; 2026-11-17 UTC; R2 physical source model admissibility, SI force, M24a event, M20b/M22a ancestry, source integrity.
- Production files changed by reviewer: **NO**. New reviewer-only probe and workflow files committed to `review_sandbox/main`, not to `conductor_sim`.
- Exact source code path: [prescribed_motion.py lines 146–163](https://github.com/physicsvigilante/conductor_sim/blob/95bbb1b39e650e1db633ea8cef9c8ad4e129dcce/src/conductor_sim/prescribed_motion.py#L146-L163). Exact M22a invariants: [structural_scenarios.py lines 116–144](https://github.com/physicsvigilante/conductor_sim/blob/95bbb1b39e650e1db633ea8cef9c8ad4e129dcce/src/conductor_sim/structural_scenarios.py#L116-L144).
- Original inherited finding: [issue #77](https://github.com/physicsvigilante/conductor_sim/issues/77); earlier [M33b independent F-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-76/reviews/review-01-chat-b.md).
- New reviewer-owned source: [review-01-chat-b-probes.py](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-78/reviews/review-01-chat-b-probes.py); [new pinned independent workflow](https://github.com/physicsvigilante/review_sandbox/blob/main/.github/workflows/m34a-review01-chat-b-independent.yml).
- **Final independent reviewer execution** [run #44070616754](https://github.com/physicsvigilante/review_sandbox/actions/runs/44070616754) **SUCCESS**; artifact [#14321229784](https://github.com/physicsvigilante/review_sandbox/actions/runs/44070616754/artifacts/14321229784). Reviewer source SHA at final execution `aa2425bb2666c64a27fb4d45323ea3379723c9e6`. The action rechecked both exact Git HEADs and trees before executing. Provider-reported artifact ZIP SHA256 `d86b92e04ac218b6c6c6dab20df58be397fdfa68c77391e619587a05a49aec5a`; ZIP bytes were **not** separately downloaded and independently rehashed.

## Findings

### F-01 — inherited real oblique reassembly refusal: FIXED for independently authored new qualifying model

**Severity: previously major composability limitation, now independently demonstrated corrected for the reviewed scope. No remaining production blocker shown.**

New independently authored **original** teacher input, deliberately unlike the developer's (1,2,-1) case:

- Raw plane normal `(3,5,-7)`; normalized binary64 `math.hypot` is `0.9999999999999999` (one native representable step below 1.0).
- Fixed original E = `(140,70,110)` V/m; q = `3.2e-9` C; mass = `2.4e-6` kg; original position = `(.006,-.010,.005)` m; velocity = `(.14,.07,.11)` m/s; gravitational acceleration = `(.035,.042,.045)` m/s². Each vector force/velocity is truly in the authored noncardinal physical plane (normal-dot-vector zero in exact arithmetic).
- Genuine held new in-plane E = `(56,-14,14)` V/m, introduced with a separate source ID and M22a reassembly.
- Exact original scenario revision `55ddaad7972cfe6c36c6f15a22b7470abc02dc5616ba638bd13f2782ef348cbe` **identical on both pinned versions**, and original normalized tuple `.hex()` bits identical.
- The old *released* M33b source **genuinely refuses** the otherwise valid new child: `ValueError: structural operation cannot edit particle, analysis or numerical controls`. Exact same qualified initial physical input on pinned candidate M34a source **genuinely admits** it with identical original plane float bits, new actual child model revision, and source inventory; no production code patched by reviewer.
- Original immutable source record was unchanged; reviewer independently recomputed source-model SHA256 from canonical model records.

The changed condition in `TestChargeMotionSpec.__post_init__` takes fully validated native finite vectors, preserves raw normal only for `abs(hypot(*normal)-1.0) <= ulp(1.0)`, otherwise applies the existing `_unit`. It leaves generic event and source axis normalization unchanged, with original full `_certify` still executed. A machine precision discrepancy of about `2.22e-16` in length is many orders below the unchanged `1e-11` physical-closure checks; this avoids an artificial second perturbation, not an author-controlled physical-plane change. The exact unchanged-analysis M22a field comparison is still present.

### F-02 — actual new native dynamics, revisions, source ancestry and signed events: PASS

Reviewer-authored graph consists of genuine whole-source-world nodes: original; added uniform held source; changed probe mass from `2.4e-6` to `3.1e-6` kg; structural replacement of held source A by genuinely different B (E = `(-21,35,16)` V/m); subsequent removal; independent sibling that introduces source ID A under a **different** physical field E = `(14,28,26)` V/m; attempted resurrection of A in its previously retired branch (refused); and a separately qualified added nonuniform `FixedPointField(2e-11 C, (.076,.060,.085) m)`. Source and branch inventory/type/label are real native model objects rather than detached fiction.

The final new-source workflow printed `{"checks":1905, "mode":"new", ...}`. These are **individual assertions/check messages, including repeated per-component and per-timestamp checks, not 1,905 statistically independent physical problems**.

For six genuine uniform-field event worlds, the reviewer independently calculated in SI, *without using production force callbacks for expected values*:

- `F_i = q E_i + m g_i`; `a_i = F_i/m`.
- `r_i(t)=r_i(0)+v_i(0)t+(1/2)a_i t²`; `v_i(t)=v_i(0)+a_i t` for **every actual native saved time**.
- Independent positive x-plane crossing root at `x=.100 m`, with actual M24a signed event/sample and root bracket.

Per component expected/native tolerances: position `7e-8` m; speed `7e-8` m/s; force `3e-12` N; acceleration `6e-8` m/s²; E `3e-9` V/m; roots `5e-7` seconds. The distinct nonuniform point-charge world used an independently written fixed-step RK4 reference (`0.0002 s`, independently computed Coulomb `kQ r/r³` and full gravity), checking all native saved 3D positions, velocities and forces and a genuine signed root. That independent implementation is an analytic/numerical cross-check, not a formal global RK truncation-error bound.

True scenario revision SHA256, exact immediate parent model *object* identity, the M22a wrapper's actual earlier assembly parent when applicable, active/seen/retired IDs, and sibling independence were challenged. A structural-after-physical replacement and a distinct later structural-after-structural removal both successfully retain the full source lineage. Attempted resurrection after retirement was correctly `rejected-structural-model` with no fabricated native scenario or event run. True M33b `GraphEventInquiryPlan` re-asked *new* positive x detector `x=.160 m` on selected previously accepted original/mass/replacement worlds with new M24a runs, unchanged source object identities, actual event roots and genuine graph digest binding. Cross-world comparison world hashes and orientation were inspected.

### F-03 — negative plane qualification, machine boundary and evidence hostility: PASS in tested regime

The new script rejected malformed/wrong-shape zero, NaN, infinity, text and Boolean normal components; true transverse initial velocity and gravity; genuinely transverse uniform field; unpaired off-plane point and rod sources; and a manually modified retained launch in an attempted M22a structural-only operation. Those real physical refusals remained enforced despite the fix.

The exact, +one-ULP, and near-unit-below normals were retained verbatim and through repeated `dataclasses.replace`; normals outside the window were fully normalized. Additional positive/negative and mixed-sign oblique normals were tested for idempotent repeated construction. No source force, initial condition, gravity, field symmetry or other real physical constraint was weakened in this review's tests.

Adversarial native pre-export edits were rejected: first normal's binary64 bits, original author label, graph plan ID, immediate parent object, source ancestry, invented source-guard termination, a root sample moved `+0.03` s, substitution of `False` for `0.0` native time, and forged new M33b inquiry status. A detached JSON status mutation did not corrupt original runner-authenticated graph export. This supports the **original in-process receipt threat model**, not external cryptographic authenticity, privileged arbitrary Python code isolation or PDF/textbook source authentication.

### F-04 — unaffected historical outputs: PASS byte-for-byte

This reviewer independently authored a *different* benign legacy source input and ran actual released M33b and candidate M34a source code with v1/v2/v3 source graph APIs and a freshly asked M33b typed event inquiry. Both exact Python output files were compared using literal `cmp`: **byte identical**, SHA256 `f68691bfd51b95b0644a837548803ae6b8ee3984b4050a1e06118ec5f149d21a` on each. This applies to the deliberately unaffected historical input; the newly admitted previously refused oblique world legitimately has a new child source SHA.

### F-05 — first two independent test failures: reviewer setup errors, retained

- [First run #44070402701](https://github.com/physicsvigilante/review_sandbox/actions/runs/44070402701) **FAIL** after successful pinned old-source false-refusal reproduction. The reviewer incorrectly expected every M22a assembly `.parent` to be a `PrescribedScenario` rather than the actual preceding `ScenarioReassembly` object for a structural-after-structural edge. Production source was not modified. Corrected reviewer assertion verifies both the native wrapper object and genuine immediate underlying scenario identity.
- [Second run #44070511392](https://github.com/physicsvigilante/review_sandbox/actions/runs/44070511392) **FAIL** after the revised six-world physics/source graph passed and reached additional negative/boundary probes. A reviewer-authored `nextafter` boundary input accidentally passed a tuple rather than the tuple's first float; fixed only that reviewer fixture. No production code changed.
- [Final run #44070616754](https://github.com/physicsvigilante/review_sandbox/actions/runs/44070616754) **SUCCESS** old-source rejection, candidate corrected true admission, new original native physics and hostility, true M33b inquiry, independently authored unaffected legacy byte comparison. All earlier failure logs/artifacts remain in GitHub workflow history.

These are not evidence of production defects and are not silently relabeled successful.

## Live source and developer CI — checked separately, NOT reviewer-authored science

Independently queried GitHub REST live PR, `refs/heads/main`, exact Git commits/trees and `actions/runs?head_sha=95bbb1b39e650e1db633ea8cef9c8ad4e129dcce`. Candidate has **18/18** PR-associated workflows `completed/success`, plus a separate successful push Python job. This includes:

- [Exact current HEAD Python #44067433710](https://github.com/physicsvigilante/conductor_sim/actions/runs/44067433710): 1,973 passed each Python 3.10 and Python 3.12, with 97 FEMM-only skips in the general jobs; 17 warnings.
- [Dedicated actual FEMM 5 #44067433481](https://github.com/physicsvigilante/conductor_sim/actions/runs/44067433481): 97 passed (not general-job skipped cases).
- [Historical real Chromium/source #44067433636](https://github.com/physicsvigilante/conductor_sim/actions/runs/44067433636): completed/success, retained existing browser tests; no claim of brand new browser feature.
- [Developer-authored independent-form SI oracle #44067433693](https://github.com/physicsvigilante/conductor_sim/actions/runs/44067433693): completed/success; NOT Chat B's independent tests.
- [Developer earlier M34a 10-test smoke #44066889697](https://github.com/physicsvigilante/review_sandbox/actions/runs/44066889697): completed/success but pinned to earlier source HEAD; not substituted for current HEAD independent checks.
- [Developer exact old/new demonstration #44067636119](https://github.com/physicsvigilante/review_sandbox/actions/runs/44067636119) and [developer old/new legacy bytes #44068338253](https://github.com/physicsvigilante/review_sandbox/actions/runs/44068338253): completed/success; distinct from new reviewer old/new and byte comparison results.

No source root `AGENTS.md` was present at the exact candidate path (GitHub contents 404). Read the frozen charter, new M34a contract, source M19/M20b/M22a/M24a/M32/M33 implementation interfaces, source-ancestry receipts, central review protocol and issue #77. Full source code review was concentrated on changed physics rule and relevant native qualification/graph paths, rather than every unaffected conductor/FEMM implementation.

## Separate scope judgments

| Dimension | Judgment | Evidence and limits |
| --- | --- | --- |
| Source interpretation fidelity | **PASS (authored source model)** | Explicit new teacher-authored stationary sources, complete 3D physical motion in certified noncardinal plane, source identity/parent history checked; no external textbook/PDF fact independently authenticated |
| Physical/numerical correctness | **PASS (bounded tested worlds)** | Independent three-component Newtonian SI at each saved time; novel nonuniform point-charge integration; genuine signed detector roots and numerical brackets; not universal ODE proof |
| Native simulation and observable coverage | **PASS (tested native scope)** | Real source/physical/structural changes, independent native event investigation and subsequent inquiry, honest refusal and time-completeness behavior |
| Evidence integrity and provenance | **PASS (declared in-process threat model)** | SHA source graphs, true parent objects, source IDs, adversarial mutations, Boolean time, altered roots, detached output; NOT an authenticated external signature |
| Teacher-facing usefulness | **PASS for this bounded authoring workflow** | Noncardinal source combinations and legitimate physical edits now compose; no scene graph or unrestricted 3D promised |
| Textbook-answer completeness | **NOT APPLICABLE** | All test worlds are invented teacher-hypothetical source data, not sourced textbook interpretations |

## Explicit verdict and release advice

**PASS — no independently demonstrated new candidate blocker or major physics/evidence defect in M34a's declared correction scope.** The separately authored native run and all current-head developer regression workflows succeeded, and unaffected native legacy exports are reviewer-computed byte-identical.

Remaining limits: reviewer was an LLM in a separate conversation, no independently authenticated original author facts/PDF, no external signature, no exhaustive continuum of all near-unit 3D planes, no formal RK root error guarantee, no independent rerun of FEMM/Chromium by Chat B (source CI was live inspected), and no expanded arbitrary 3D physics. These are scoped limitations, not silently waived guarantees.

**Keep PR #78 DRAFT/UNMERGED until the owner separately authorizes merge against exact expected HEAD `95bbb1b39e650e1db633ea8cef9c8ad4e129dcce`.** Reconfirm HEAD/tree and all associated CI after this report; any changed HEAD needs source-pinned re-review of impacted paths. Postmerge inspect exact main source/tree and all main-push checks before claiming released M34a. **This report does not merge, mark ready, edit or authorize source release.**
