# Post-PR164 JEE coverage evaluation — frozen 20-case development sample

**Prepared 18 November 2026. Status: selection frozen; original-image interpretation and case execution NOT YET completed.** This is an engineering evaluation of the newly merged main, not a blind independent model benchmark and not a claim that 20 original questions were successfully simulated.

## Baseline and source

PR #164 was owner-authorized and merged into Opticsim main at **8b4ffee3c9deb34fcf7d657221f917fab321de4c**, Git tree **f371366765c8aa96029a0b29d6ae3f770e9b0eb2**, identical to the independently reviewed integration tree. This is the fixed engine baseline for the initial batch. No thick-lens, footprint, or held CI-feature branch is included unless already present in that exact commit. Do not change the engine between first attempts to inflate coverage.

[selection.json](selection.json) was committed first, at review_sandbox commit **f84e300f3a2257c0aee4d6114b0dd887eb8391be**, before reading the selected source pixels or any corresponding Solutions content. It references the exact existing source inventory at engine baseline, blob **3224c05dfc43a7de7f6e6f15b9759374a3dfed11**, and its historically verified original archive SHA-256 **03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939**. The new evaluation has not yet reread/rehashed those archive bytes; verify them before relying on any extracted original.

The old atlas inventories **114 Problems PNGs in eight chapters**, with 40 previously inspected by that atlas and 74 marked not-reviewed. This sample selects only from those 74, with fixed chapter quotas [3,3,3,2,2,2,3,2]. For each chapter, lexicographically sort eligible paths and take zero-based positions floor(k*(N-1)/(q-1)) for k=0..q-1. This yields exactly 20 cases spanning plane and curved reflection, general refraction, TIR, prisms, curved refraction, lenses, and optical instruments. It does not guarantee each question contains a newly implemented feature, or that the sample statistically represents all JEE questions. The old atlas's not-reviewed label does NOT prove a case was never exposed in another prior project trial; record any earlier exposure and never describe this same-chat development assessment as an independent blind model score.

## Execute against original questions, not imagined substitutes

For each fixed selected path:
1. Read the exact **Problems** PNG from the verified source archive. Record its SHA-256 and preserve a source reference. Do not open its Solution until the first interpretation and original authoring attempt are saved. Never treat the chapter name, old atlas summary, expected topic, or filename as the problem text.
2. Record what the source explicitly states, what is logically derived, what is missing/ambiguous, and which requested observation the question asks for. Preserve its physical interpretation and approximations. Diagram scale is not numerical geometry. Do not silently supply a refractive index, finite aperture, source brightness, Fresnel policy, unknown direction, observer location or other missing scene fact.
3. Produce exactly one initial JSON request using the existing published contracts, or a specific missing-data / unsupported-scope / numerical-refusal disposition. Preserve the first bytes and checksum without post-result edits. A partial analytical calculation or honest refusal must not be presented as a complete native scene.
4. Validate and execute only that initial request on the fixed engine baseline. Native output must come from pinned PhyDemo, with scene hash, completeness, qualified method, warnings and actual observed events. Analytical values remain explicitly not-run or conditional. Complete native zero crossings are measured data; stale, truncated or absent data are not zeros. Retain failure results and nonexecuted cases in the denominator.
5. After all first attempts are frozen, compare against an explicitly identified reference source or separately reasoned physical check. Record discrepancies between original question, diagrams and reference explanations rather than silently reconciling them. A provided solution is evidence to inspect, not an infallible replacement for the problem's own facts.
6. Any repair, synthetic teaching companion, additional numerical assumption, expanded native scene or engine patch is a separate follow-up record. It cannot rewrite the original attempt or be counted as original-problem native coverage. Unsupported cases are not replaced by easier ones.

## Separate assessment dimensions

- **Interpretation fidelity:** Were stated apparatus, quantities, signs, material sides, units, requested result and explicit assumptions preserved? Runnable but wrong physics is not success.
- **Authoring and simulation coverage:** Is the supported representation native, analytical-only, partial, missing physical facts, unsupported composition or numerically indeterminate? Distinguish JSON validation from physically faithful support.
- **Physical correctness and evidence completeness:** Are claimed quantities supported by the declared model and an independent check? Distinguish real native completed measurements, available measured zero, incomplete/withheld output, and conditional analytical inference. A detector hit is not a reconstructed image, eye perception, continuous irradiance or arbitrary source ancestry.
- **Educational usefulness:** Does the result faithfully illustrate the supported physical aspect, explain scope and uncertainty, and avoid misleading learners? A clearly labelled partial teaching result may be useful without solving the entire textbook question.
- **Textbook-answer completeness:** Track separately and optionally. Matching an answer choice does not repair incorrect interpretation or absent native evidence; lack of the textbook's full solution sequence does not itself invalidate a faithful teaching simulation.

Do not pool these into a single misleading model-accuracy percentage. Report counts with clear denominators and evidence provenance, and retain a case-level ledger.

## Review cadence and scope

This batch preparation is metadata/process work; it changes no Opticsim source, safety validator or public physical claim. No per-question independent review is requested. Consolidate the 20 case findings and the most consequential interpretation/physics disagreements into one batch assessment. New engine physics, changed native-evidence semantics or loosened numerical admissions still require their normal independent review at a final tested candidate. Routine data preparation and tests do not create automatic review checkpoints.

No external model API invocation, paid inference, solution transmission or bulk public republication of source images is authorized by this plan. Existing archived attempts stay historical. Same-chat model-authored JSON is labelled as such, not independent verification.

## Decision after the evaluation

Prioritize reusable engine limitations shown by the actual source-backed cases: for example missing physical components, composition restrictions, conservative numerical bounds, deficient observables, or difficulty expressing a supported system through JSON. Distinguish those from underdetermined problem inputs and authoring mistakes. Decide whether to integrate held refractive-system work only after that diagnosis. Do not begin another feature merely to force a textbook answer.

**Current ledger:** 20 paths selected; 0 newly source-image-inspected cases recorded; 0 first attempts published; 0 per-case executions/scored outcomes. This is intentionally not a completed coverage claim. Append progress and results in new files without rewriting the frozen selection.
