# Independent R3 — Opticsim PR #155: native first-event integrity

**Review date:** 18 November 2026  
**Reviewer:** Chat B — independent read-only GitHub source, Git-object, diff and decoded CI-log inspection; independent execution of the **exact candidate's extracted JavaScript event validator and result classifier** on deliberately constructed synthetic contradictory records. **No independently rerun native PhyDemo or Chrome/browser session.**  
**Verdict: CHANGES REQUESTED. P0: none found. P1: one — full-Fresnel reflected-branch legitimacy remains insufficiently checked.**

## 1. Frozen source, parentage and evidence identity

| Item | Independently verified |
| --- | --- |
| Target | [Opticsim draft PR #155](https://github.com/physicsvigilante/opticsim/pull/155), open, draft, unmerged at inspection |
| Exact candidate HEAD | `4d4939516ec96accb1b168d0884b35b850bbbcae` |
| Exact candidate Git tree | `f2237c19309c829725109e0fad208fc287b94ad5` |
| True reviewed base | PR #153 frozen HEAD `1107014449ac9fb89fce9bdaa93a44052d664b09`, whose independent R2 remains **CHANGES REQUESTED** |
| Ancestry comparison | Five commits ahead of #153, zero behind, merge-base exactly #153 HEAD |
| Changed files only | `scripts/jee-observer-native-witness.mjs`, `test/jee-observer-native-witness-v1.test.mjs`, `docs/JEE-OBSERVER-NATIVE-WITNESS-V1.md` |
| CI-only PR #156 | Closed unmerged; synthetic merge `fd04830881c9aa112f9539f8cdb974e44d43d954` |
| CI synthetic merge Git tree | Identical `f2237c19309c829725109e0fad208fc287b94ad5` |
| CI synthetic commit's ordered parents | `d3509e82fb65d81aabe336666851f8f2962623f4` (production main), then exact reviewed HEAD `4d4939516ec96accb1b168d0884b35b850bbbcae` |

These identities were checked against [raw candidate Git commit](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/4d4939516ec96accb1b168d0884b35b850bbbcae), [raw CI-merge Git commit](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/fd04830881c9aa112f9539f8cdb974e44d43d954), live PR metadata and the exact base...head GitHub comparison, not merely the review packet's claims. The diff does **not** alter pinned PhyDemo, `src/planar-media.js`, `src/adapter.js`, `src/observables.js`, native observation projection, canonical schema, or the independent analytical parent. Scope is the new critical evidence-integrity correction, not a full rereview of those earlier capabilities.

## 2. What is corrected and sound

I inspected the [exact-head witness source](https://github.com/physicsvigilante/opticsim/blob/4d4939516ec96accb1b168d0884b35b850bbbcae/scripts/jee-observer-native-witness.mjs), [changed tests](https://github.com/physicsvigilante/opticsim/blob/4d4939516ec96accb1b168d0884b35b850bbbcae/test/jee-observer-native-witness-v1.test.mjs), [docs](https://github.com/physicsvigilante/opticsim/blob/4d4939516ec96accb1b168d0884b35b850bbbcae/docs/JEE-OBSERVER-NATIVE-WITNESS-V1.md), and unchanged [native event capture](https://github.com/physicsvigilante/opticsim/blob/4d4939516ec96accb1b168d0884b35b850bbbcae/src/planar-media.js), [observable projection](https://github.com/physicsvigilante/opticsim/blob/4d4939516ec96accb1b168d0884b35b850bbbcae/src/observables.js), [native hit instrumentation](https://github.com/physicsvigilante/opticsim/blob/4d4939516ec96accb1b168d0884b35b850bbbcae/src/adapter.js), [raw observation snapshot](https://github.com/physicsvigilante/opticsim/blob/4d4939516ec96accb1b168d0884b35b850bbbcae/src/native-observations.js), [native run summary](https://github.com/physicsvigilante/opticsim/blob/4d4939516ec96accb1b168d0884b35b850bbbcae/scripts/author-scene.mjs), and [separate observer geometry](https://github.com/physicsvigilante/opticsim/blob/4d4939516ec96accb1b168d0884b35b850bbbcae/src/planar-observer-point-query.js).

- **Original R2 P1 fixed:** a claimed one-interaction transmission with `branches:[]`, transmitted counter zero/mismatch, missing/nonfinite angles, invalid/nonunit transmitted direction, wrong outgoing normal sign, contradictory policy/outcome or native encounter truncation is now rejected by shared `validTransmittedEvent` for **both positive and zero-detector cases**. This is stronger than the unchanged presence-only interface-first-event projection.
- **Measured-zero semantics preserved:** one actual emission, a complete/fresh run, a native count of zero, and a count-matched complete `[]` hit list remain distinct from unavailable evidence. A one-interface negative also checks native/analytical incident/transmitted angles and transmitted outgoing direction. The zero-interface case separately needs zero interaction/transmitted/reflected/TIR/invalid counters, null raw first event and an unavailable/null projected first event. A completed no-encounter event is not fabricated.
- **Fresnel positive control:** under explicit full Fresnel, one transmitted and one reflected branch can be admitted; a genuine pinned-native arrival is retained. Nonfinite powers, wrong branch kinds/counts and a reflection directed forward into the observer medium are rejected.
- **Readings and claims:** a measured zero keeps the actual position, incoming direction and positional error **null**; it never becomes a measured 0 mm location, invisibility proof, image or eye. Positive results still compare an actual native hit and direction to declared tolerances. The repaired report distinction is status-sensitive. Native apparatus consists of one separately authored source, interface and finite passive detector; no itinerary, ray or image ancestry is inferred.

Coordinate/sign reasoning: `interfaceNormal` constructs the positive-normal direction in world y-up coordinates; native `PlaneGlass` uses the corresponding positive half-plane and the adapter converts the native y-down directions to y-up. Positive-normal transmission and negative-normal reflection checks are correct as **necessary** conditions at 0°, ±90°, 180° and oblique orientations. They are **not sufficient** to prove a specular reflected ray is physically compatible with the incoming ray.

## 3. P1 — Physically impossible full-Fresnel reflected branch still passes the common event gate

**Location:** [`validTransmittedEvent` in witness lines 115–174](https://github.com/physicsvigilante/opticsim/blob/4d4939516ec96accb1b168d0884b35b850bbbcae/scripts/jee-observer-native-witness.mjs#L115-L174), specifically the reflected-branch check; the shared admission occurs in `evidenceResult` for both positive and zero crossings.

The reflected branch check correctly requires one reflected branch when the meter says one, explicit Fresnel-on policy, finite unit direction, a negative dot product with the oriented normal, finite nonnegative power, and agreement between the branch's unsigned angle, its **own** calculated unsigned normal angle and `first.reflectedAngleDeg`. But it never checks the reflected angle/direction against the **incident** direction or `first.incidentAngleDeg`. The angle formula uses absolute values, so it discards tangential sign. This permits a ray that goes back into the correct medium with the wrong tangential direction and nonetheless presents a self-consistent unsigned angle.

**Concrete independent synthetic counterexample — not a genuine PhyDemo trace:**

- At a vertical plane `normalDeg:0`, source index 1.5, observer index 1, partialReflection true, use incident angle 10.6161089413°, transmitted angle 16.0419777084°, one interaction, one transmitted branch, one reflected branch, no TIR/invalid counts/truncation, matching source/scene evidence. The transmitted branch and analytical outgoing direction are unchanged and valid.
- The incident ray goes in direction approximately `(+0.98288359,+0.18422770)`. Specular reflection **must** reverse its normal component and preserve its tangential component: `(-0.98288359,+0.18422770)`.
- Deliberately inject `reflected.direction = {x:-0.98288359,y:-0.18422770}`, while leaving `reflected.angleDeg = first.reflectedAngleDeg = first.incidentAngleDeg = 10.6161089413` and all native counters intact. This is **not** specular reflection. It still has a negative normal projection, a unit norm, the expected unsigned angle, correct recorded angle equality and ordinary finite power. The exact validator returns **true**.
- A second contradictory variant sets both reflected angle fields to 5° and the reflection direction to `(-cos 5°, +sin 5°)`; it too passes even though the incident angle remains 10.616°. Therefore the gap is not only a missing tangential-sign test.
- I fetched the frozen source and independently executed its **verbatim extracted** `validTransmittedEvent` and `evidenceResult` function bodies with matching synthetic observation methods/hashes and counters. The wrong-sign reflected event was accepted as `verified-sampled-arrival` with one synthetic matching detector hit, and also as `native-observed-no-crossing` with zero synthetic crossings and `[]` hits. The zero result had reason `MEASURED_ZERO_DETECTOR_CROSSINGS`, null hit; both would receive CLI exit 0. Controls with the physically correct reflected direction also passed. The same validator bypass occurred at 0°, +90°, 180°, −90° and 37° normal rotations. This was a **standalone synthetic execution of exact extracted result logic**, not execution of the full witness CLI or independently observed PhyDemo behavior.

The builder's 22-case mutation matrix checks missing transmission, wrong forward-normal sign and other contradictory counters; its separate wrong-medium reflected control flips reflection into the *positive* medium. Neither covers a backward-normal reflected ray with a reversed tangent or a self-consistent but wrong reflection angle. This is a narrowly reproducible **P1 evidence-integrity flaw** under the review request's explicit requirement that the optional native reflected branch be physically legitimate. The native detector may still genuinely measure a hit/zero; the **combined witnessed first-event qualification** is what remains too permissive. There is no evidence that the real pinned PhyDemo creates this invalid ray.

**Required bounded correction:**

1. In the one-source/one-plane profile, enforce the full specular reflection condition `d_ref ≈ d_inc − 2(d_inc·n)n`, including the **signed tangential component**. `d_inc` can be derived from the exactly authored single-ray heading and verified against the conditional incident geometry under a fixed explicit tolerance; alternatively extend native event capture to expose the actual incoming y-up unit vector with appropriate qualification. Do **not** route/replace the native ray with analytical predictions. Also require `first.reflectedAngleDeg ≈ first.incidentAngleDeg` when a reflected branch exists, with a physically justified small angular tolerance.
2. Add completed, hash-matched **synthetic refusal tests** flipping only the reflected tangential component, altering the reflected angle and direction together while preserving its self-consistency, and covering normals 0°, ±90°, 180°, an oblique orientation, and both signs of tangent displacement. Assert withholding on **both** positive and one-interaction measured-zero branches with null accepted detector hit and nonzero exit. Keep one real native full-Fresnel two-branch admission control plus the existing transmitted-only and no-interface genuine controls.
3. Freeze a **new child SHA/tree**, rerun exact-source relevant checks and standard CI, and request one focused independent check of this physical reflected-branch correction only. Preserve previous R2/R3 source identities and verdicts; do not broaden into unrelated optics features.

**P0:** none found. **P1:** one. This is a release-gating qualification defect for the advertised physically legitimate full-Fresnel branch, not a report of wrong actual PhyDemo outputs.

## 4. Builder CI and provenance boundary

At exactly the candidate HEAD, the GitHub Actions runs API returned **11 completed-success standard PR workflows**, all first attempts. In [Optical composition run #44317233633](https://github.com/physicsvigilante/opticsim/actions/runs/44317233633) and [Plane-mirror run #44317234261](https://github.com/physicsvigilante/opticsim/actions/runs/44317234261), I inspected actual decoded job logs, not just green check summaries. The plane-mirror job reported **819 tests, 819 pass, 0 fail**. The optical job reported ordinary Chrome **27 browser acceptance checks / 15 screenshots** and hosted smoke **5 checks / 1 screenshot** (Chrome 157.0.8103.50). The standard workflow suite is associated with exact candidate HEAD and the synthetic merge with identical Git tree; it is **builder CI, not independent native or browser testing**.

The decoded node log specifically contains:
- `JEE_OBSERVER_NATIVE_EVENT_INTEGRITY_MATRIX`: **22 synthetic completed/matching-record mutations refused**; the marker explicitly says `actualNativeRerunOfMutations:false`.
- `JEE_OBSERVER_NATIVE_FRESNEL_TWO_BRANCH_CONTROL`: **genuine pinned-native two-branch full-Fresnel arrival admitted** and a separately **injected** zero for classifier testing.
- `JEE_OBSERVER_NATIVE_REAL_ZERO_CONTROLS`: two genuine native *separately authored* SingleRay test scenes — 30° transmits and misses the finite detector; 180° misses both interface and detector. These alter the emitted ray heading and **do not** establish a native miss of the analytical observer-directed ray.
- `JEE_OBSERVER_NATIVE_ZERO_CLASSIFICATION`: an explicitly **synthetic** complete zero summary. The original genuine positive detector hit at approximately (100,40) mm remains a regression.

The first-event producer in `src/planar-media.js` observes incoming and outgoing directions around one original native delegation and records unsigned angles, signs, branches and scalar counters. The detector callback independently samples native crossings and withholds ambiguous/incomplete event lists. `evaluateObservables` binds those readings to a matching canonical scene hash and completed execution before labeling them native observations; it deliberately **does not** certify first-event optical shape. These distinctions explain why the witness's extra reflection-law validation matters.

## 5. Nonblockers and retained limits

- **N1 — No universal Fresnel energy proof:** finite nonnegative branch power is checked; no full reflected/transmitted energy conservation proof is claimed or required for this narrow correction. If claiming such correctness later, review its separate physical scope.
- **N2 — Hash is freshness, not authentication:** a deliberately modified synthetic `executeNative` result can be self-consistent and hash-matched; the counterexample is a classifier regression, **not an accusation of hostile tampering or a real native physics bug**.
- **N3 — Model scope:** one qualifying detector hit or complete zero remains a sampled finite-detector observation, not an optical image, observer perception, continuous illumination or source ancestry. Numerical analysis predicts ray geometry but never fabricates PhyDemo rays. Preserve this language.

No further P0/P1 was identified within this bounded R3 source diff; this is not an assurance about unchanged optical families or future integrated composition.

## 6. Disposition and next steps

**CHANGES REQUESTED.** The original PR #153 first-event missing-transmission problem is substantially repaired in #155 and all 11 builder workflows are green, but the new shared gate still accepts an independently demonstrated physically impossible full-Fresnel reflection as qualified first-event evidence. Correct and test the **specular reflected-branch direction/angle consistency**, use a new frozen child and one **focused** independent review. Then prepare **one consolidated JEE integration review** before any new optical capability expansion, subject to owner approval and applicable gates.

**No merges or release authority granted.** Do not merge #155 or the already closed CI-only #156; do not retroactively change frozen #151/#153 reviews. The outstanding [Opticsim branch-protection issue #123](https://github.com/physicsvigilante/opticsim/issues/123) remains unresolved by this review. No Opticsim source, branch, PR status, historical review, test artifact or PhyDemo evidence was modified. This report only creates the requested independent review in `review_sandbox`.
