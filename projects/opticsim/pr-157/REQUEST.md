# Opticsim PR #157 — targeted independent R4: signed specular Fresnel event integrity

**Critical evidence-integrity source gate. Do not merge or release.** This review is narrowly scoped to the reflected-ray correctness deficiency independently demonstrated on frozen PR #155. No need to repeat earlier full reviews of unchanged optics authoring, analytical geometry, detector instrumentation, or prior research.

## Exact frozen source and CI identity

- [Draft PR #157](https://github.com/physicsvigilante/opticsim/pull/157): HEAD **`c1bcf2b5537767e6c0bd710590f9a763b0db40d7`**, source Git tree **`317eff764dd82c2c42dc1cffca5c5f856d92d464`**.
- True base is [frozen PR #155](https://github.com/physicsvigilante/opticsim/pull/155) HEAD **`4d4939516ec96accb1b168d0884b35b850bbbcae`**, whose [independent R3 review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-155/reviews/review-01-chat-b.md) returned **CHANGES REQUESTED — one P1**. Its original SHA/tree/review remains unchanged.
- Temporary main-target [CI-only PR #158](https://github.com/physicsvigilante/opticsim/pull/158), synthetic merge **`359ae0f66f49d5a54b8c1c10108e959701e44f9e`**, has **identical Git tree `317eff764dd82c2c42dc1cffca5c5f856d92d464`** with parents [actual production main **`d3509e82fb65d81aabe336666851f8f2962623f4`**, exact PR #157 HEAD]. Please verify actual Git commit objects, not PR prose. PR #158 is a CI harness, **closed unmerged** after evidence capture.
- Compared with PR #155, only three existing child files change: `scripts/jee-observer-native-witness.mjs`, `test/jee-observer-native-witness-v1.test.mjs`, `docs/JEE-OBSERVER-NATIVE-WITNESS-V1.md`. No edit to pinned native PhyDemo, `src/planar-media.js`, `src/adapter.js`, canonical schema, `src/observables.js`, reviewed analytical parent #150, or production main.

## Precisely what Chat B found on R3

The prior witness correctly required an observed first planar event, transmitted branch, index/side/Fresnel policy, finite unit directions, native count consistency, and incoming/outgoing normal signs. For an optional genuine full-Fresnel **reflected** branch, it checked only a negative normal projection and a **self-consistent unsigned** angle with the normal.

The independently executed counterexample corrupted a synthetic reflected native branch to `d_ref=(-0.98288359,-0.18422770)` when the native single source incident direction was approximately `d_i=(+0.98288359,+0.18422770)` and plane normal +x. Real specular reflection requires `(-0.98288359,+0.18422770)` — preserving signed tangential direction. The former has unit length, negative normal projection and matching unsigned angle but is physically impossible for that source. A second synthetic attack changed reflected direction and the two self-consistent unsigned reflected angle fields together from ~10.616° to 5° while leaving the incident angle unchanged. Both were incorrectly accepted as either a verified sampled detector hit or a measured-zero native observation in the **extracted exact-source event classifier**. **These were intentionally forged test records, not real PhyDemo outputs.**

## New R4 source correction to evaluate independently

The corrected shared first-event validator, used by BOTH the `verified-sampled-arrival` and `native-observed-no-crossing` result branches, derives a reference **incident** world y-up unit direction solely from the explicitly *authored* SingleRay heading `analysis.value.predictedInitialDirectionDeg`. It is legitimate to use that authored direction for this narrowly admitted scene: one source, one ideal planar boundary, one detector, with no earlier mirror/lens/medium or multiple source rays. It is NOT claimed as a separately measured native incoming vector, and PhyDemo remains the actual forward ray propagator.

For oriented interface unit normal `n`, the predicted specular reflected unit is:

`d_expected_ref = d_authored_incident − 2(d_authored_incident·n)n`

The actual native reflected unit must agree within an explicit **1e-7 Euclidean unit-vector tolerance**; the reflected first-event angle must agree with native recorded incident angle and with the independent authored incident-angle magnitude within **1e-5 degrees**, retaining existing branch angle/method/counts/Fresnel/normal-side checks. This must detect flipped signed tangential components, self-consistent incorrect reflection angles and rotated-normal equivalents. No native ray is redirected, repaired or fabricated. No Fresnel power/energy-conservation certificate is claimed.

## Builder pre-review evidence — inspect actual logs

At the **final exact HEAD** above, **820/820 Node tests PASSED, 11/11 standard GitHub Actions workflows concluded SUCCESS** on the tree-identical synthetic merge. Real pinned PhyDemo and actual Chrome/browser acceptance were builder executed, **not reviewer-independent native or browser runs**.

- [Plane-mirror workflow #44321863943](https://github.com/physicsvigilante/opticsim/actions/runs/44321863943), job **134862636069**, decoded log prints `JEE_OBSERVER_SPECULAR_REFLECTION_ADVERSARIAL` with **5 normals [0,+90,−90,180,37]**, both positive/negative tangent signs, **10 separately genuine pinned-native full-Fresnel two-branch arrivals admitted**, and **40 synthetic counterfactual records refused** (each tangent-flip/wrong coherent 5° reflection, both *positive native-hit* and *complete measured-zero* pathways). The ordinary Node summary is **820 tests, 820 pass, 0 fail**.
- [Optical composition run #44321863739](https://github.com/physicsvigilante/opticsim/actions/runs/44321863739) and other workflows also completed successfully. Prior genuine pinned-native source (-60,0) → observer (100,40) hit, positive full-Fresnel and transmitted-only cases, separately authored genuine zero-crossing PhyDemo controls, stale/incomplete and input refusals remain regression requirements.
- [Curved-mirror run #44321864087](https://github.com/physicsvigilante/opticsim/actions/runs/44321864087) attempt 1 failed after passing 820/820 Node tests because **no Chrome/Chromium was available** on that runner. An unmodified-source job retry, **attempt 2** (job **134864030941**), succeeded. This is a preserved infrastructure exception, NOT a physics test failure or new source patch.

The 40 corrupted records are injected **synthetic complete/hash-matched summaries** designed to check classifier refusal; they are not observations of physically impossible light produced by PhyDemo. Native positive controls are genuinely executed. Do not conflate the two kinds of evidence.

## Focused independent reviewer tasks and acceptance

1. Re-derive reflection law in signed normal/tangent coordinates and test both original R3 attacks, including oblique normals and reversed tangent sign. Compare physically required reflection vectors to the actual validation code; check numerical tolerance and rejection path.
2. Inspect the actual one-source/one-plane canonical v5 scene admission to confirm authored incoming heading is a sound scoped expectation, not a native observation of incoming ray direction or an inferred itinerary. Check correct y-up/native-y-down conversion, normal orientation at 0/±90/180/37, and no false rejection of actual full-Fresnel transmitted+reflected branches.
3. Verify the entire shared first-event validator and both result paths still hold: complete/native SHA/method/counts, measured zero as available data, zero native interface encounters with legitimate missing first event, real positive detector hit tolerance, Fresnel policy, actual vs predicted directions, no unqualified success for inconsistent events. Probe a genuinely new adversarial example instead of repeating builder assertions.
4. Independently check raw Git identity and CI logs, distinguish builder CI from independent mathematical/source validation. Identify a concrete P0/P1 if any; keep nonblocking observations separate.
5. If cleared, recommend **one consolidated JEE integration candidate** and **one later integration review**, rather than opening more feature branches. The source R4 review does not authorize merging any draft; owner release decision and [branch protection issue #123](https://github.com/physicsvigilante/opticsim/issues/123) remain separate.

Publish a single report to **`projects/opticsim/pr-157/reviews/review-01-chat-b.md`** with exact SHA/tree, independent equations/tests/evidence provenance and verdict **CLEARED FOR NEXT SCOPED DEVELOPMENT / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. This is a **targeted final correction review**, not another comprehensive review of all unchanged JEE features. **No Opticsim source edits, merges, release authorizations, or alterations of historical adverse reviews.**
