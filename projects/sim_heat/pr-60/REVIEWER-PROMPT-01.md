# Chat B — SIM_HEAT PR60, H1-N1-P0 pre-native DESIGN review

Use a fresh independent reviewer conversation. This is **one R2 review of a proposed bounded native experiment and reference design**, not a request to run a compiler or certify numerical results that do not exist.

**Source draft PR:** https://github.com/physicsvigilante/sim_heat/pull/60
**Exact HEAD:** `469ab08f4b0fbe3144110bae41b57d29695447bb`
**Git tree:** `7e2158153d0ef8aa7e8afa3d12a0b996e2af49db`
**Base main:** `f52613c39c539b2d4543a9838e5658d526fca10e`
**Actual PR CI synthetic checkout:** `04b4860d06de32d7ed26ac9a197f378ac4cb434a`, identical candidate tree.

**Read full request FIRST:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-60/REQUEST.md

Then read the exact candidate's `qualification/h1_n1/PLAN.md`, `REFERENCE-CONTRACT.md`, `plan.json`, `reference-facts.json`, `SOURCE-PINS.json`, labelled `PLANNING-SCREENING.json`, checker/tests and workflow. Compare against the unchanged native_batch runner, companion/resolution helpers, current H1 numerical policies, verification and MAT decoder. Read AGENTS and central review protocol/risk policy.

The original T1-T model/study/notes are byte-identical to the independently source-reviewed UNSEALED trial; no new physical law or production engine changes. Proposed physical window remains **0–2400 s**. Primary uses 2400 intervals/tolerance1e-8; tight companion same grid/1e-10; dense companion4800 intervals/1e-8. Three separate one-case invocations, **at most3 OMC version queries,3 fresh builds,3 launches,zero retries**, only after future owner permission. Currently **ZERO native operations**.

Challenge these actual issues independently:
- Existing batch runner permits at most2 cases; old campaign helper hard-codes a1000-grid/seven-launch campaign and must not be reused here.
- Four primary/dense flow allowance fields differ slightly; existing comparator would refuse equality. Proposed future comparator uses **primary presealed allowance only**, never sum/max or widened tolerance, while each run is independently checked. That new implementation is **not present yet**.
- The checking reference needs an independently justified error bound at least100x below every applicable comparison allowance, not mere high-precision/algorithm agreement. Assess the proposed interval Taylor/scaling-squaring, source/rounding/Pi handling, Schur elimination,77exports/eight observations, integrals, full-grid temporal/quadrature budgets and constant-export precision. **No certificate is claimed to exist.**
- Preserve the original finite horizon; do not claim five-time-constant equilibrium (screening estimates that much later).
- Actual runtime image/OMC binary/MSL/host identities, new same-host reference seals, comparator/certificate software, executable manifests and single-use/containment controls are **unbound/unimplemented** and expressly block execution. No fake runtime hashes, no spoofed GitHub host environment, no native workflow included.

Verify successful exact-head offline [push44364726234](https://github.com/physicsvigilante/sim_heat/actions/runs/44364726234), [PR44364885661](https://github.com/physicsvigilante/sim_heat/actions/runs/44364885661) and [audit44364885768](https://github.com/physicsvigilante/sim_heat/actions/runs/44364885768). Plan jobs each pass **16negative/structural+152H1 tests** and docs parity while explicitly retaining `nativeExecutionReady=false`, `referenceAccuracyCertified=false`, native calls0 and seven blockers. Source receipts show twelve additions only. Artifact IDs/hashes are in the request; audit records six original archives BYTE_IDENTICAL without native execution. Distinguish personally run offline checks from inspected CI; green CI does not validate an absent reference algorithm.

**Write your own NEW independent report to:**
`physicsvigilante/review_sandbox/projects/sim_heat/pr-60/reviews/review-01-chat-b.md`

Verdict: **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, specifically for **PRE-NATIVE DESIGN ONLY**. Identify concrete design defects and smallest corrections, distinguish sound design from still-open runtime/certification implementation gates. A plan pass must not imply execution readiness, numerical qualification or owner native permission. Later readiness additions should receive targeted review in this same bounded scope rather than a repeated whole-project review.

**Strict stop:** do not invoke/query/install/build/launch OpenModelica, generate native data, change original source/reference files, merge PR60 or evidence-only PR59, rewrite historical C1/T1 outcomes, promote archived diagnostics or deploy. The original source-only requests remain not_computed; the lost T1 scorer remains unverified.