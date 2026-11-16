# SIM_HEAT PR #16 — targeted R2 follow-up Review 02

**Status:** Chat A's correction is finished, **independent targeted re-review pending**. PR remains draft, unmerged. Chat B's [original R2 Review 01](reviews/review-01-chat-b.md) at `e76df818fcbb9b6826b03db776b6140dd40c4be4` concluded `changes-requested`. Do not overwrite it.

## Pin this corrected candidate, not floating branch HEAD

- Source PR: https://github.com/physicsvigilante/sim_heat/pull/16
- Base on main (unchanged): `c977773578b04a571dfefebe615350b9ed1dcf3e`.
- **Exact corrected head SHA:** **`099bd4330a56e129f35493b42231830209a9e964`**.
- **Exact corrected Git tree:** `85a62320977092f47cf5d100bf98c4b2bf955599`.
- **Correction-only diff:** [previous reviewed head → corrected head](https://github.com/physicsvigilante/sim_heat/compare/e76df818fcbb9b6826b03db776b6140dd40c4be4...099bd4330a56e129f35493b42231830209a9e964).
- Exactly **three** paths: `viewer/network/tools/build_steady_case.py`, `viewer/network/tests/test_steady_adapter.py`, `viewer/network/README.md`. No other source or physics changed.
- Chat A's [response-01](responses/response-01-chat-a.md) explains exact dispositions, preservation and known limits. This is developer evidence, **not** an independent review finding.

## Exact-new-head evidence

- [CI run 43834101967](https://github.com/physicsvigilante/sim_heat/actions/runs/43834101967): `completed`, **SUCCESS**, exact corrected head, 151 H1 + 4 analytical + 11 Python adapter + 14 JS viewer tests, all passed, real Chromium desktop/mobile PASS with original four cases/refusals and delayed file races.
- [CI evidence artifact 14210406363](https://github.com/physicsvigilante/sim_heat/actions/runs/43834101967/artifacts/14210406363), ZIP SHA-256 **`015ee3b1874996df29e70f2ec2aefa33902704b271fe60e3d11b183c9159a92d`**, 3,544,109 bytes. Developer re-downloaded, verified ZIP SHA/CRC, head marker, logs and screenshots.
- [Source snapshot 14210401348](https://github.com/physicsvigilante/sim_heat/actions/runs/43834101967/artifacts/14210401348), ZIP SHA-256 **`d7a0b09fcdbb1a25649cf1b0e0f7b30bccbe8a862056c1e9cd5b6f424e1c0220`**. This exact-head source was independently executed against the **original legitimate S1 native archive** plus eight SHA-repinned adversarial copies: original accepted/reproduced the byte-identical shipped S1 case; 8/8 copies refused. All are Chat A's author checks, not reviewer-pass evidence.
- Original authentic [S1 native run 43820600508](https://github.com/physicsvigilante/sim_heat/actions/runs/43820600508), original artifact **14204656273**, SHA-256 `82b4a87b66e0022d582da931253649b3829f6633119a57081c02dc253dc5dbd9` remains unchanged. Original native 56/56 diagnostic checks, `nativeQualified=false`. No new OMC execution for this correction.
- Historical intermediate correction run [43833850755](https://github.com/physicsvigilante/sim_heat/actions/runs/43833850755) **FAILED** at old Python test call signature after the new mandatory expected run/commit parameters were added. It remains failed and accessible. It is not the final source CI.

## Required narrow questions to answer independently

**F-01 MAJOR — repinned contradictory receipts:** On the exact corrected adapter, try an adversarial *repacked ZIP with updated member SHA entries and a fresh valid outer ZIP SHA*, not just stale-hash rejection. Specifically mutate (1) all recorded `verification.checks[*].passed=false`, (2) `verification.requests[0].values=9999`, (3) original case `referenceSeal`, (4) verification `referenceSeal`, (5) case `referenceFileSha256`, (6) `reference.bundle.json` seal/payload, and (7) omit an otherwise present `build.mos` file from the manifest. The old reviewer reproduced acceptance in the uncorrected code. Confirm corrected behavior refuses with the intended reason. Check that `h1.verification.check_candidate` reproduces the published verdict exactly using original native CSV/presealed bundle/receipt, rather than reference-filled native values or independently invented numerical thresholds.

**F-02 MINOR — incomplete source member:** Remove original MAT, CSV, study, verification or reference bundle from a repacked ZIP; check structured `steady_evidence` refusal rather than raw KeyError or silently missing data. Ensure original successful ZIP remains admitted.

**F-03 QUESTION — external GitHub provenance:** Caller must now supply `expected_run_id` and `expected_commit_sha` separately; their mismatch with `attempt.github` refuses. Confirm CLI uses these arguments and README correctly states that they require prior trusted verification of actual GitHub Actions run/commit/artifact. The adapter does **not** query GitHub or authenticate an arbitrary newly self-pinned archive, and nobody claims an independently measured physical temperature. Challenge a bogus run/commit and evaluate whether residual trust risks are accurately bounded.

**Preservation:** The original `sim_heat.viewer.native_case/1` contract, D1/D2/DEV_BRIDGE bundles, native material facts, S1 numeric JSON/CSV, original H1 engine and numerical allowances are byte-identical; only the three above files changed. The extra tests use **test-only synthetic ZIP/MAT stand-ins**, not genuine new native builds. Browser time semantics and graph ownership were already reviewed and are unchanged.

## Reviewer output and controls

Chat B should independently test targeted source/archive behavior where possible. Clearly distinguish (a) direct independent executions, (b) inspected Chat A CI and ZIP evidence, and (c) untested limitations. Follow [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md), report every remaining real blocker or insufficient evidence, and write **a new attributed report** directly to:

`physicsvigilante/review_sandbox/projects/sim_heat/pr-16/reviews/review-02-chat-b.md`

Do **not** modify source code, overwrite Review 01, run new native OpenModelica simulations, certify reference accuracy, authorize merge or merge PR #16. A scoped PASS still requires explicit separate owner merge approval. Do not expand to a full original R2 architecture review unless corrections altered physical/evidence behavior outside the examined path.
