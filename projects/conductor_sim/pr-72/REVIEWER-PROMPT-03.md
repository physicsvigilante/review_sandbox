# M31b PR #72 — Targeted independent R2 re-review #03: F-04 physical provenance

**Developer-authored handoff, NOT independent PASS or merge authorization.** Retain both original CHANGES-REQUESTED reviews #01/#02 unchanged. Production PR #72 remains DRAFT / UNMERGED.

Source PR: https://github.com/physicsvigilante/conductor_sim/pull/72
NEW exact source HEAD: 7f52376c197d4667dba8c54463f995fce4d7df73
NEW actual source Git TREE: fe3df0fff668887d8f938b8be35ea124f6b22816
Original review #02 source HEAD: 72c5f9ffc133da1db79b11c6ba878f95fb8d90c8
Original review #02 Git TREE: 6033283cf38345abd2f2cace5cd7999997509984
Base/main: ec4f4f10ae6392335c8078cd7ecb0bc575addf04, released M31a
Bounded diff: https://github.com/physicsvigilante/conductor_sim/compare/72c5f9ffc133da1db79b11c6ba878f95fb8d90c8...7f52376c197d4667dba8c54463f995fce4d7df73

Read [review #02](reviews/review-02-chat-b.md), [original independent probes](reviews/review-02-chat-b-probes.py), [review #01](reviews/review-01-chat-b.md), [developer response #02](responses/response-02-chat-a.md), [REQUEST](REQUEST.md), [central PROTOCOL](../../../PROTOCOL.md), [R2 policy](../../../REVIEW-RISK-POLICY.md), [report template](../../../REVIEW-TEMPLATE.md), [pinned charter](https://github.com/physicsvigilante/conductor_sim/blob/7f52376c197d4667dba8c54463f995fce4d7df73/docs/m31b_charter.md) and [M31b typed contract](https://github.com/physicsvigilante/conductor_sim/blob/7f52376c197d4667dba8c54463f995fce4d7df73/docs/m31b.md). Check for source AGENTS.md. Independently fetch LIVE source PR HEAD and Git tree and verify DRAFT/OPEN/UNMERGED. If the source moved, report STALE HEAD rather than inspecting floating main.

## The original demonstrated blocker

At old source 72c5f9ff, Chat B independently EXECUTED a native dataclasses.replace bypass on an authentic M31b coupled event: reauthor the M31a physical hypothesis from Enew=(150,0,0) V/m plus mass 2e-5 kg to false Enew=(175,0,0) V/m and mass 3e-5 kg, constructing a coherent replacement physical plan/family/entry/event child, while native child scenario and M24a event observations remained genuine for original physics. The old native M31b event receipt remained unchanged, yet typed construction and detached JSON both ACCEPTED the false authoring evidence. Another ordinary replacement falsely changed top-level plan_id. Original reviewer-native first-attempt workflow #44020279830 preserved those ACCEPTED_UNEXPECTEDLY F-04 results and deliberate nonzero exit; the first negative findings remain valid at that pinned source.

The same independent review #02 established that F-01 moved root times, F-02 fake parent/child refusals, F-03 failed M31a child event rescue had all been FIXED at the old source head; real M24a native physics and signed gravity+Ey analytical roots passed. This third review must not reopen unchanged physics without new evidence.

## Exact new correction, one commit only

NEW commit 7f52376c197d4667dba8c54463f995fce4d7df73 changes ONLY:
- src/conductor_sim/coupled_event_family.py
- tests/test_m31b_coupled_event_family.py
- docs/m31b.md

The existing runner-issued in-process observation receipt now includes the **complete native M31a CoupledPhysicalRun.as_dict() evidence**, not merely native M24a event-run data and child case/revision identifiers. That binds ORIGINAL plan ID, ALL true atomic physical edits/notes/component IDs, branch selection, real parent-child source-model SHA identities, source inventory, physical scenarios, ordinary native physical trajectories and literal SI comparison rows. The unchanged typed constructor and pre-export validator recheck the SAME runner-issued receipt. No imported JSON is trusted as a model and an arbitrary dataclasses.replace may not issue a fresh trusted receipt. This is ordinary Python result-value integrity, NOT cryptographic protection against malicious private module modification. No physical law, M31a qualifier, numerical RK, M24a event locator, M28a shared clock or M28b root-pairing code changed.

Three new source-native regressions reproduce the exact F-04 altered two-property values, foreign plan ID, changed hypothesis note and post-construction replacement before JSON export; authentic original results must still pass.

## Developer recheck — NOT an independent PASS

[Exact corrected-head native replay of UNCHANGED original reviewer #02 probes, run #44020944747](https://github.com/physicsvigilante/review_sandbox/actions/runs/44020944747) SUCCESS. Live Git checkout verified exact new source SHA 7f52376c197d4667dba8c54463f995fce4d7df73 and tree fe3df0fff668887d8f938b8be35ea124f6b22816. Logs explicitly show:
- F04_HYPOTHESIS_PROVENANCE_REBIND: REJECTED
- F04_PLAN_ID_REBIND: REJECTED
- Original F-01/F-02 attacks still REJECTED, authentic refusal preserved, F-03 failed child and valid sibling preserved
- Genuine rod event and independent reviewer gravity+Ey analytic native positive controls PASS

[Developer-run output artifact #14300757813](https://github.com/physicsvigilante/review_sandbox/actions/runs/44020944747/artifacts/14300757813), GitHub-reported ZIP SHA256 860862802a49a7658b01068b1d2f2663bd57de870c056180430e46d9cfdd7bf8, not independently downloaded/rehashed by developer. NOTE: the original unchanged reviewer probe's JSON includes its historic old-source SHA/tree literals. The new workflow checkout and job log pins (not the historic script-embedded literals) verify exact source execution. This developer-controlled replay is NOT Chat B independent review.

## Narrow independent reviewer tasks

1. Independently construct an authentic new M31b CoupledEventRun. Try the same coherent multi-dataclass replacement with false physical E and mass, keeping old issuer/digest and original event results. Test both new construction, dataclasses.replace and post-construction export. Try relabeling the plan_id, note, a stable component ID/property, a source membership/label or a revised scenario. Verify no ordinary coherent public dataclass attack can retain original-issued provenance falsely. Distinguish excluded arbitrary private Python manipulation.
2. Verify the full M31a original/hypothesis/branch/source inventory/trajectory is now in the receipt snapshot, and correct result is not falsely rejected. An externally supplied changed physical family must not be able to regenerate a trusted issuer or hash through ordinary result construction. Inspect exact code.
3. Preserve previous F-01 shifted root +0.030s, F-02 parent/child fake refusals, genuine event-study refusal with separately observed accepted child, F-03 test-injected M31a numerical failure with valid sibling, real signed gravity+Ey native crossings, retained real rod/DOP853 science.
4. Verify exact HEAD 7f52376c197d4667dba8c54463f995fce4d7df73, Git tree fe3df0fff668887d8f938b8be35ea124f6b22816, PR still DRAFT/unmerged, completed and SUCCESSFUL full current-head Python 3.10/3.12 (expected 1,912 each; verify actual log), 97 real FEMM, historical Chromium, separate source-head rod Coulomb+DOP853. PR jobs may use GitHub synthetic merge checkout while direct push jobs run literal head. At prompt creation full corrected-source CI was still completing. Never claim success on pending/failed checks.
5. Provide a precise remaining trust-boundary statement: typed in-process evidence consistency, not cryptographic attestation or exact global ODE error bounds. No user-authored PDF model interpretation certification is implied.

## Required new independent report

Independently publish a NEW review to physicsvigilante/review_sandbox/main at:

projects/conductor_sim/pr-72/reviews/review-03-chat-b.md

Include the exact source SHA/tree, what attacks you personally executed versus only inspected from developer CI, original F-04 closure verdict, no-regression F-01/F-02/F-03 results, source paths and limits, and explicit PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE with blockers. Preserve both original CHANGES-REQUESTED reports untouched. Do NOT modify, approve, mark ready or merge production PR #72. A separate ChatGPT context is not independent human expert certification.

Only fresh independent source-pinned no-blocker PASS, all-green exact-head CI and owner standing expected-head merge authorization permit Chat A to release and verify postmerge main.


## Completed corrected-HEAD release-candidate CI — verified 2026-11-17 IST

**The full 18/18 workflow run inventory at literal PR source HEAD `7f52376c197d4667dba8c54463f995fce4d7df73`, source Git TREE `fe3df0fff668887d8f938b8be35ea124f6b22816`, now reports COMPLETED SUCCESS for every run. No pending or failure.** This is developer verification, **not** an independent review #03 PASS. PR #72 remains **DRAFT / OPEN / UNMERGED**.

- [PR Python 3.10/3.12 run #44020903118](https://github.com/physicsvigilante/conductor_sim/actions/runs/44020903118): both interpreters report **1,912 passed, 97 real-FEMM-only skipped, 16 warnings**. The PR jobs check out GitHub's synthetic merge `f7a4780...` into unchanged released M31a base, not literal source-HEAD.
- [Separate literal source-head push Python run #44020896167](https://github.com/physicsvigilante/conductor_sim/actions/runs/44020896167): both Python 3.10 and 3.12 **1,912 passed, 97 FEMM-only skipped, 16 warnings**, checked out literal source HEAD. These counts include the three new reviewer F-04 negative regressions.
- [Actual real FEMM 5 workflow #44020903084](https://github.com/physicsvigilante/conductor_sim/actions/runs/44020903084): **97 passed** historical conductor cases, not novel M31b FEMM event calculations. [FEMM artifact #14300663636](https://github.com/physicsvigilante/conductor_sim/actions/runs/44020903084/artifacts/14300663636), GitHub-reported ZIP SHA256 `c4df3cbb141800569f7f7d1376f1fdfd481ebabd9f4f063709c8bfa936d709cd`.
- [Historical real Chromium/visualization #44020902879](https://github.com/physicsvigilante/conductor_sim/actions/runs/44020902879): **SUCCESS**, historical browser/authoring suite plus **1,912 non-FEMM Python cases passed, 97 deselected, 16 warnings**, no new M31b HTML. [Browser artifact #14300553962](https://github.com/physicsvigilante/conductor_sim/actions/runs/44020902879/artifacts/14300553962), GitHub-reported ZIP SHA256 `fd94d4154723a8ac75f508f433a5b0cbe8c9ad985317c67b414e12e2c2fe6b56`.
- [Independent-form rod/Coulomb/DOP853 #44020902913](https://github.com/physicsvigilante/conductor_sim/actions/runs/44020902913): **SUCCESS** with literal source-HEAD checkout, authentic parent/child M31b native event times **0.5529332747459412 s / 0.4985157885551453 s**; separately coded SI quadrature+SciPy DOP853 **0.5529332751693771 s / 0.49851578891918547 s**. [Numeric evidence artifact #14300064144](https://github.com/physicsvigilante/conductor_sim/actions/runs/44020902913/artifacts/14300064144), GitHub-reported ZIP SHA256 `33a535858fe6cf7ca09574e1e8dd69e26c74b1ab447093135e7c44579bea4314`.
- [Same unmodified reviewer #02 native F-04 probes rerun at new corrected source SHA/tree #44020944747](https://github.com/physicsvigilante/review_sandbox/actions/runs/44020944747): **SUCCESS**. Both originally accepted F-04 attacks now **REJECTED**; original F-01/F-02/F-03 negative cases and genuine event-study refusal/sibling and reviewer-authored native gravity+Ey case still pass. This was developer-triggered, not reviewer #03.

Artifact digest statements above are **GitHub provider-reported**; developer has NOT downloaded and rehashed original ZIPs. Do not equate provider digests with independent artifact verification. All original review #01/#02 negative attempts remain unchanged. **Now ready for one narrow separate-context independent R2 review #03**, with the new report at `projects/conductor_sim/pr-72/reviews/review-03-chat-b.md`. DO NOT merge on developer CI or replay alone.
