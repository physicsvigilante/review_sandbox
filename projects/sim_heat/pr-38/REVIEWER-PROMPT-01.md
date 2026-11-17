Continue as independent Chat B reviewer for SIM_HEAT.

Review historical draft [SIM_HEAT PR #38](https://github.com/physicsvigilante/sim_heat/pull/38) at exact source SHA **`a570e3c589457d21b6673701a2d126d7046e1c3c`**, based on PR #37 corrected R2-PASS SHA `2f2b8d5008f51b9972897058328aed8cbcbfbbce`.

Read the full R2 packet:
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-38/REQUEST.md

The PR adds four files only and generates a **non-executed TEXT preview** of an OpenModelica build script using the frozen pure `h1_native_batch.build_script()` formatter. It first validates original saved Modelica/study/library/source hashes and the **exact independently reviewed, owner-adopted PR31 V2 reference**. The text contains a prospective `buildModel` instruction, but the new CLI/CI has **no authority or capability to query, compile or launch OpenModelica**.

Independently inspect the actual saved preview script, model/library path and MSL/DASSL/grid/MAT settings; verify the source does not invoke the frozen `prepare`/ `execute` / `reference.prepare` or native subprocess. Adversarially inspect preview text/manifest/duplicate-key/extra-file, stage tamper/replay and forbidden CLI actions. Check exact-head [CI #44030612438](https://github.com/physicsvigilante/sim_heat/actions/runs/44030612438) and [artifact #14305570982](https://github.com/physicsvigilante/sim_heat/actions/runs/44030612438/artifacts/14305570982), ZIP SHA-256 **`7e3196d673c0b2a1d71166da81b1ac58fdcd256121c3029e61fc2b37525179f1`**; 33 CRC-valid ZIP members and **229 OFFLINE test methods**.

Write a NEW independent `projects/sim_heat/pr-38/reviews/review-01-chat-b.md` in `physicsvigilante/review_sandbox`. Give scoped PASS, CHANGES REQUESTED or INSUFFICIENT EVIDENCE, distinguishing tests you performed from CI evidence. Retain old frozen F0 80× static reference FAIL and PR32 bitwise regeneration FAIL; do not falsely claim a native run or compiler observed.

**Do not** edit source, merge historical PRs, widen original tolerances, install/invoke OpenModelica, grant owner/native execution permission or create a one-shot reservation. Note remaining protected owner release, actual compiler/MSL/host identity, durable across-run lock and separate owner approval for a named native launch.