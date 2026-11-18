# Opticsim PR #161 — ONE independent integration + final R5 evidence-integrity review

**Review date request: 18 November 2026. Status: REVIEW-ONLY, DRAFT, UNMERGED.** This is a combined **critical source-evidence and cross-feature integration gate**, deliberately replacing two serial review requests. The owner asks for fewer reviewer interruptions **without weakening physical safety**. Reviewer must explicitly audit the previously unreviewed R5 correction *and* the integrated exact Git tree; source review alone is not enough, and an earlier source's clearance does not automatically authorize release.

## 1. Exact source identity and provenance: independently check Git objects

- [Draft PR #161 — reviewed integration candidate](https://github.com/physicsvigilante/opticsim/pull/161).
- **Review HEAD:** `09ad081a34ced0fa969affc1bf54766cabffb04a`.
- **Review source Git tree:** `1b2caf6186c8eaf678963238d2292001b2fa9667`.
- The integration branch is a **single-parent, main-based** commit series (NOT a merge of another draft PR): base `d3509e82fb65d81aabe336666851f8f2962623f4`, original main Git tree `45ff3bcd9093a527652f13f76c3cc0b02826642f`. First integration commit `b43607e5d6af0d72d9c20657884d2e9d2cf99c12` directly parents main, with source-blobs-only tree `292e5ff46bd041dfbd94f898108fcb5841af80ba`. Final HEAD adds **one** review-only audit document.
- GitHub Actions synthetic PR merge `2583730832daa310bef1dcaa1fcfecffb3e58c5a`, exact Git tree **`1b2caf6186c8eaf678963238d2292001b2fa9667`**, parents in order `[d3509e82fb65d81aabe336666851f8f2962623f4, 09ad081a34ced0fa969affc1bf54766cabffb04a]`. Verify the raw Git commit objects. Main stays unchanged, branch protection issue #123 unresolved.
- Exactly **13 added files** versus main, **no existing modified/deleted files**: **12 unchanged Git blob** copies from separately frozen sources plus `docs/JEE-PLANAR-INTEGRATION-CANDIDATE-V1.md` (new review audit). Check all source blobs byte-for-byte, not just file names. **NO production `src/adapter.js`, `src/authoring.js`, `src/contract.js`, `src/observables.js`, native PhyDemo, browser or existing CI workflow changed.**

## 2. Sources: distinguish independently cleared vs still review-gated

**A — explicit-angle conditional apparent depth, [PR #144](https://github.com/physicsvigilante/opticsim/pull/144)**, HEAD `aea25a9b480260e2498229d80f7f6cbe3d4ac574`, tree `e1fe378b7070ef6be53f34faa798e75774f877a5`. Four added **unchanged** files:
- `src/planar-apparent-depth-query.js`
- `scripts/planar-apparent-depth-query.mjs`
- `test/jee-apparent-depth-query-v1.test.mjs`
- `docs/JEE-PLANAR-APPARENT-DEPTH-QUERY-V1.md`

Prior [independent R1 review of PR #144](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-144/reviews/review-01-chat-b.md): **CLEARED FOR OWNER DECISION**, scope analytical conditional mathematical virtual-axis extrapolation, not detected image/native reverse ray. Recheck integration interactions; no need to duplicate the entire original source-review process for unchanged physics.

**B — observer-position analytical source, [PR #150](https://github.com/physicsvigilante/opticsim/pull/150)**, HEAD `0fb738f69b3257113c73dbf9d1f2917037daa5cc`, tree `8cd6b5df7cceaf68d04deca4926eb91245986216`. Four added **unchanged** files inside R5 source:
- `src/planar-observer-point-query.js`
- `scripts/planar-observer-point-query.mjs`
- `test/jee-observer-point-query-v1.test.mjs`
- `docs/JEE-OBSERVER-POINT-QUERY-V1.md`

Prior [independent R1 review of PR #150](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-150/reviews/review-01-chat-b.md): **CLEARED FOR OWNER DECISION**, strictly one ideal plane, explicit source/observer/indices/normal/units, local Snell root, predicted crossing and conditional axis intercept. It **always** says native `not-run`.

**C — explicitly physical optional native witness, [PR #159](https://github.com/physicsvigilante/opticsim/pull/159)** final R5 HEAD **`70ff5d34140e0d29c6a22c70897322d8459db0e8`**, source tree **`c6bb20d8fa6c0678731ca8bf237a559cfcac4455`**. Four original/additional source blobs copied unchanged into PR #161:
- `scripts/jee-observer-native-witness.mjs`
- `test/jee-observer-native-witness-v1.test.mjs`
- `examples/jee-observer-native-witness-v1.json`
- `docs/JEE-OBSERVER-NATIVE-WITNESS-V1.md`

**IMPORTANT — source C/R5 is NOT independently cleared yet.** Its frozen parent [PR #157 R4 independent review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-157/reviews/review-01-chat-b.md) was **CHANGES REQUESTED (P1)**: the specular reflected direction was dereferenced before the validator checked whether `r.direction` exists or is an object, resulting in TypeError/possible missing final report on a malformed complete/native-shaped first event. Earlier PRs #151/#153/#155 have their own historical CHANGES REQUESTED verdicts at different immutable SHAs. **The combined review of PR #161 must independently decide whether exact PR #159 R5 fixes the R4 blocker, then decide the integrated tree.** Never retroactively revise older reports.

## 3. Detailed R5 safety verification REQUIRED (not inherited)

In the standalone one-source/one-plane native witness:
- Full-Fresnel reflected branch must obey **signed** specular law `d_ref=d_inc−2(d_inc·n)n` against the known **authored** SingleRay heading, not a fabricated measured native incoming ray. Compare reflected normal/tangent components and native reflected vs first-incidence angle. The opposite signed tangent with the same unsigned angle must be refused. Allow one real reflected branch alongside the native transmitted branch when explicit Fresnel-on policy is selected, without claiming Fresnel energy conservation.
- Exact R4 P1: `r.direction` **omitted, null, wrong type, partial coordinates, nonfinite, nonunit** MUST be rejected **before any coordinate dereference**, yielding native evidence refused with null accepted hit and a saved JSON report; no TypeError.
- A fail-closed qualification exception boundary was added to preserve a final refusal report if classifier processing itself throws. A deliberately artificial accessor fault which arises **earlier during `evaluateObservables` projection** is separately classified `native-infrastructure-error`, exit 2, with durable report and preserved analytical+scene files. This status is not a verified native hit or a fabricated measured zero. Do not assume it exercises the later classifier catch.
- Observe exact native success vs false negative: a completed, fresh **zero** detector crossing and complete empty hit list are valid sampled data, **not unavailable evidence**; zero interface encounters legitimately have no first event; a one-interaction zero still needs physically valid transmission and analytically consistent first native event. Missing/malformed methods, counters, contradictory event branches, stale hash, truncated native runs and zero emissions must not qualify. One real native hit is an actual sampled detector coordinate/direction within explicitly chosen tolerances, never a perceived image or universal inverse-tracing guarantee.
- Challenging adversarial tests must distinguish deliberately **synthetic** hash-matched summary corruptions from separately authored **genuine pinned native** hit/miss/Fresnel controls. A synthetic checker record is not a physically observed ray.

## 4. Combined exact-head builder preflight (inspect decoded logs)

**The full 13-file integrated PR #161 passed 832/832 Node tests and all 11/11 standard GitHub Actions workflows SUCCESS** at exact HEAD. This is a new integrated-tree execution, not the sum of the individual branch results:
- [Combined optical composition run #44329347455](https://github.com/physicsvigilante/opticsim/actions/runs/44329347455), job **134889188157**, passed Node/real native and browser acceptance steps.
- [Combined plane-mirror run #44329347588](https://github.com/physicsvigilante/opticsim/actions/runs/44329347588), job **134889189837**, decoded log prints **832 tests, 832 pass, 0 fail** plus named explicit-angle JEE, observer-point, true native witness, R5 malformed reflected vector and report persistence tests.
- R5 standalone [source CI #44328323151](https://github.com/physicsvigilante/opticsim/actions/runs/44328323151) and [plane-mirror #44328323494](https://github.com/physicsvigilante/opticsim/actions/runs/44328323494): final corrected HEAD `70ff5d...` passed **822/822 Node** and **11/11 workflows**, including ordinary real Chrome.
- Final R5 marker `JEE_OBSERVER_REFLECTED_DIRECTION_MISSING_MATRIX`: 22 **synthetic** reflected-direction malformed records (11 forms x detector-hit/observed-zero) result in safe `native-evidence-unavailable`, saved refusal report, no accepted native hit. `R5 hostile projected-event getter` is an **injected accessor/projection failure** with saved `native-infrastructure-error` report, not real native output.
- Preexisting 40 synthetic signed-reflection attack refusals, 10 real native full-Fresnel controls across 0°, ±90°, 180°, 37° normal and signed tangent; 22 additional malformed native-event cases; real positive native hit, two separately authored real native zero-detector controls; local/world numerical withholding, analytical input refusal, stale/incomplete suppression must remain present. No image or observer assertion.
- **Pre-review CI history matters:** two earlier R5 builder-only working heads `befcadde9e9ebf7e84dbda81a1bded2d95189d4a` and `1a61f3b92293f7f0b0a25419560040bcbe33d0d6` each had **821 pass / 1 fail of 822 tests**, because a deliberately hostile getter test expected the *witness classifier* refusal while the event was actually rejected earlier by native-observation projection. The test was corrected to assert the true early `native-infrastructure-error` fail-closed stage, and the **final corrected source** `70ff5d...` passed. These failed intermediate tests are not hidden, not a native physics failure and are not the final review source.
- No independent reviewer execution of pinned PhyDemo/Chrome is presumed from builder runs.

## 5. Cross-feature integration audit

Ask whether the 12 reviewed/candidate blobs coexist safely on production main: distinct input format IDs and CLI/output names, no hidden physics defaults, consistent x-right/y-up and indices, independent analytical (native `not-run`) vs opt-in native witness, no collision across `src/`, scripts, docs, examples/tests and deterministic scene/evidence rules. Examine whether tests of both analytical entry points plus physical native witness all run in the same suite, that no pre-existing canonical scene schema or PhyDemo behavior changes, and that errors/refusals remain truthful. All independent optical physical claims must stay strictly bounded to single-plane/single-source/sample.

The **broader** native parallel-beam v19 (PRs #127/#141), v14–v18 thick-lens and other experimental JEE branches are intentionally excluded because they change shared `src/adapter.js`, `src/contract.js`, `src/authoring.js`, composition or workflows. Do NOT certify or release those branches by examining this planar-only candidate. Review audit: [docs/JEE-PLANAR-INTEGRATION-CANDIDATE-V1.md](https://github.com/physicsvigilante/opticsim/blob/09ad081a34ced0fa969affc1bf54766cabffb04a/docs/JEE-PLANAR-INTEGRATION-CANDIDATE-V1.md). Risk-policy: [review and integration policy](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/REVIEW-AND-INTEGRATION-POLICY.md).

## 6. One combined independent verdict requested

Publish **`projects/opticsim/pr-161/reviews/review-01-chat-b.md`**, with verified exact source HEAD/tree, R5 missing-reflection refusal/report persistence conclusion, interactions of the JEE analytic/opt-in-native features, real measured-vs-inferred scope, explicitly independent recomputation and evidence/provenance boundaries, P0/P1/nonblocking findings, and verdict **CLEARED FOR OWNER DECISION / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**.

If a blocker exists, describe its exact reproduction so a **single focused correction** can be made. If clear, it clears **only this combined planar integration candidate** for a **separate owner release decision**, not a merge authorization. The source PRs #144/#150/#159 and held historical #151/#153/#155/#157 retain their individual states/reviews. The integration candidate **must remain draft/unmerged** unless the owner explicitly authorizes a merge; branch protection issue #123 remains unresolved. Do not edit code, merge, deploy, rewrite source reviews or claim stronger physics.
