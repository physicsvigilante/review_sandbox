# Opticsim — first post-PR164 JEE coverage audit

**18 November 2026. BUILDER DEVELOPMENT AUDIT, NOT an independent review, blind LLM benchmark, representative sample, or solved-question percentage.** No Solutions entries were opened. No engine source, native PhyDemo, canonical schema or previously sealed attempt was changed to improve these results.

## 1. Merged baseline and actual post-merge verification

[PR #164](https://github.com/physicsvigilante/opticsim/pull/164) is **merged**. Production baseline commit **8b4ffee3c9deb34fcf7d657221f917fab321de4c**, Git tree **f371366765c8aa96029a0b29d6ae3f770e9b0eb2**, equals the independently reviewed combined planar/v19 source tree. This is now a stable production-main baseline, not another unreleased integration rehearsal. All **11 actual post-merge push workflows passed**, with [post-merge optical run #44355559880](https://github.com/physicsvigilante/opticsim/actions/runs/44355559880), job **134982607188**, checking out the actual main merge commit and reporting **860/860 Node tests**, seven native Beam public cases, 11 dedicated Beam Chrome checks, 27 standard browser checks and five hosted smoke checks. Native/browser executions are builder GitHub CI, not independent reviewer replay or a claim of public website deployment.

## 2. Frozen source sample and direct inspection

[Draft evaluation PR #165](https://github.com/physicsvigilante/opticsim/pull/165) freezes 20 paths across all eight chapters of the supplied `08_Ray_Optics_Explanations.zip`. Its archive SHA-256 is **03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939**. The sample is fixed first/middle/last for core chapters, first/last for prism/curved refraction, first for instruments; it is purposive, not random. Some selected cases overlap the earlier atlas and are **not** claimed unseen.

The source-collection CI artifact **14454755556** from run **44360693719** was downloaded and its ZIP SHA verified as **ec95794b8becfcb10a3819c39063c8c4673cf43f58cb3b6cce3ee523cd755f97**. All 20 original Problems PNGs were directly visually inspected, and all 20 PNG hashes matched the source manifest. `/Solutions/` files were neither extracted nor read. No picture pixel scale was turned into physical lengths. The committed `source-review.json` records source facts, unknowns, supported subsets, modelling limits and educational use for all 20 cases.

The five reduced source requests and three normalized phase probes were frozen in commit **d9209263cab368ec6343bdbeb2a071b6c19c1bdb**, before this trial's runner was added/executed. Original request bytes SHA-256: **c710e199e62d908bab418512423a546c673225a656cc96a84caa225cda31fa49**. They have not been rewritten after execution.

## 3. Exact evaluation execution provenance

Tested evaluation head **6a72bd67e58e9a3fd94a6bf33d88d1f20295b4c2**, tree **354497bd3bfac6a65ca3530e234c819a852f76e7**. The source/CI merge **5e3a0206c06645d7cd473eb7ca942777616f4b9e** has the identical tree and parents [production baseline 8b4ffee..., evaluation head]. The diff adds only four evaluation data/docs files and two tests; **zero existing production files modified**. All **11/11 evaluation-head workflows succeeded**.

[Evaluation optical CI #44363079152](https://github.com/physicsvigilante/opticsim/actions/runs/44363079152), job **135009430361**, archived the actual trial outputs in `llm-authoring-evidence`, artifact **14454927379**, ZIP SHA-256 **bdd7d7c801dd1f31e9d43dedba52a1196ce80e1a066b926c7c4dff814e84401a**. The artifact was downloaded and its digest independently checked against GitHub metadata. Trial evidence paths are under `jee-post164-coverage-execution-v1/`: original `first-requests.json`, 20-case hash-bound source review, eight unedited analytical results, the separately labelled native illustration's canonical scene/summary, and `report.json`.

**CI green means the evaluation harness preserved source identity and evidence invariants, not that every question was solved.** Individual result records, not the overall test badge, establish the observations below. The engine baseline was not tuned to the sample.

## 4. First-run outcomes

### Five source-derived reduced analytical requests

These contain the question's relevant facts plus openly declared ideal/paraxial assumptions. No source brightness, missing aperture or arbitrary focal scale was invented just to compute an analytical answer. All five returned **conditional analytical results, native not-run**, matching separately written **builder-side** scalar reference checks. That cross-check is not an independent review or comparison with textbook solution files.

| Case | Source question | Observed engine result | Qualification |
|---|---|---|---|
| J03 | Two mirrors inclined 70 degrees; second reflection parallel to first mirror | First incidence **50 degrees from normal** | Both allowed orientation/output signs enumerated; actual finite mirror interception not proved |
| J04 | Concave mirror at u=1.5f, object height 2.5 cm | Magnification **-2**, image height **-5 cm**, inverted | Normalized Gaussian/paraxial calculation; absolute f not fabricated; no native image |
| J06 | f=20 cm concave mirror, u=25 cm, object moving at 5 cm/s and 45 degrees toward mirror/up | Image velocity **+56.56854249 cm/s axial**, **-14.14213562 cm/s transverse** | Axial positive away from mirror, transverse upward; stationary/fixed-focal paraxial mapping, not a traced image velocity |
| J10 | Parallel indices 1.60 → 1.80 → 1.30, critical at second boundary | Initial incidence **54.34091230 degrees**, second incidence **46.23825731 degrees**; decreasing initial angle permits transmission under stated assumptions | No thickness/source placement needed for angular invariant; no native exact-critical completion asserted |
| J18 | Coaxial converging lenses f1=20 cm/f2=10 cm, spacing30 cm, object30 cm before first | Final image **7.5 cm beyond second lens**, magnification **-0.5** | Explicit ideal-thin/paraxial/coaxial approximation; mathematical image plane, not physical detected image |

### One partially supported symbolic question: J05

The original swinging-ball question has x=f cos(omega t), origin at mirror curvature centre and positive direction away from mirror. Three **explicitly source-derived normalized phases** use u/f=2+cos(phase), without inventing f or omega. The engine returns:
- phase0: v/f=1.5, m=-0.5;
- phase pi/2: v/f=2, m=-1;
- phase pi (t=T/2): image at infinity, **null finite image distance and magnification**, not a fabricated finite number.

All three subset checks matched the builder reference. They are **one partially supported question**, not three extra full successes or an arbitrary symbolic motion solver.

### Separate teaching-native illustration of J18

The original two-lens source gives axial distances/focal lengths, not brightness, apertures, emission or a detector. A **separate labelled illustration** adds an on-axis point source, explicit brightness0.08, 10-degree directional fan, 100-mm apertures, explicit preview-v1 numerical preset and a 100-mm passive detector at the independently predicted x=375 mm. These are recorded added physical choices, **not source facts**.

Pinned PhyDemo completed a canonical schema4 trace: **three actual emitted samples and three actual detector crossings**, each near **(375,0) mm**, maximum absolute transverse detector coordinate **2.9103830456733705e-15 mm**. Hit events are actual native callbacks with method `native-hit-event-observation`, matching canonical SHA **21df6a899f72a62e9a34149c4662613a0612792d422a4b3c0b60e9343c1a84ad**. The scene does not force the predicted ray path. A detector placed at a mathematical image plane is still **not** native image reconstruction. **This is not counted as an original-question fully specified native success.**

## 5. All 20 source cases retained, including gaps and missing inputs

| Case | Initial developmental disposition |
|---|---|
| J01 | Direction-pair single-mirror angular inverse has sufficient reduced source facts, but no matching standalone API in the audited mirror-angle/reduced-inverse contracts. Native reflection itself exists. |
| J02 | Three-mirror image enumeration is not detector-crossing counting; no complete image-set result asserted. |
| J03 | Conditional reduced analytical execution above. |
| J04 | Conditional normalized mirror-height execution above. |
| J05 | Partial normalized phase checks only, not the whole symbolic time-dependent problem. |
| J06 | Conditional instantaneous mirror-image velocity execution above. |
| J07 | Newly merged planar apparent depth is applicable, but source does not state numerical water/air indices. No silent 4/3 or1 substitution; not a missing planar-physics capability. |
| J08 | Mirror-backed slab tracing is within an existing planar/mirror family, but native illustration needs explicit exterior index and physical extent/emission choices; no complete original trace run in this trial. |
| J09 | Continuous gradient index mu=sqrt(1+y), symbolic thickness and grazing incidence are outside audited homogeneous-medium propagation. |
| J10 | Reduced critical-layer angular execution above. |
| J11 | Symbolic escape cone/opaque disc visibility is not proved by a 2D sampled detector zero. |
| J12 | Flat-plus-curved half-cylinder with parallel input is not current full-circle/one-lens Beam scope. |
| J13 | Three-face prism inverse with internal reflection and 'slightly above critical' is not the current direct two-face transmitted inverse. Do not silently turn the inequality into an exact equality. |
| J14 | Joint small-prism-angle/index inverse using reflected and transmitted beams exceeds current direct-transmission prism inverse; Beam+prism native scene not admitted. |
| J15 | One spherical refracting surface power needs a distinct reduced curved-interface contract, not an invented second glass surface. |
| J16 | Sphere/bubble apparent depth must not use the planar apparent-depth formula. A separately declared meridional native trace does not automatically certify a 3D apparent image. |
| J17 | Two-source common-image inverse placement not supplied by a one-object forward lens-train query; no midpoint guessed. |
| J18 | Conditional analytical execution plus separately explicitly completed native teaching illustration above. |
| J19 | **Concrete JEE gap:** two vertically decentered ideal thin lenses and a parallel input. Current lens train is coaxial; v19 Beam admits at most one ideal lens. No d=0 substitution. |
| J20 | Accommodation/eye power needs declared reduced-eye assumptions; generic ideal lenses are not a physiological eye model. |

These 20 dispositions are not a binary pass/fail score. Some are API gaps despite known physical primitives; some are unsupported models; some need explicitly stated numerical conventions for a native illustration; and six have at least a directly executed reduced analytical part.

## 6. The five evaluation axes remain separate

- **Interpretation fidelity:** every source image was directly inspected; labels and requested operations are retained. Unknown essential material/geometry is recorded rather than supplied from answer intuition. Interpretation is builder-assessed, not independently graded.
- **Physical correctness:** five conditional reduced results and three partial normalized values agree with explicit independent-of-implementation scalar checks written by the same builder; one separately completed native illustration has genuine measured hit evidence. No native, optical or answer correctness claim is assigned to unexecuted cases.
- **Simulation coverage:** no complete original-question native apparatus is claimed from the sparse textbook facts; one explicitly completed illustrative two-lens system ran natively. Many angular/ratio questions are usefully supported analytically without fabricating native apparatus.
- **Educational usefulness:** conditional magnification/velocity/critical-angle explanations and the separately labelled two-lens trace are usable teaching accompaniments; the exact focal singularity remains visible. This is author judgment, not a measured classroom outcome.
- **Textbook-answer completeness:** not the primary success criterion. Five requested reduced numerical relations are available; J05 only selected phases; remaining requested outputs are not misrepresented as solved. No Solutions were consulted.

## 7. Source-driven next capability recommendation

**Do not automatically integrate the large thick-material-lens branch next.** The source-backed two-lens case J18 already works analytically and as an explicitly completed native illustration using the merged ideal-lens engine. More native thickness would not directly solve J19's actual missing feature: a vertically displaced second ideal lens with parallel input.

The next bounded engine milestone should investigate **reusable ideal-lens composability with explicit transverse lens centres and a narrowly validated multi-lens parallel Beam profile**, while retaining existing coaxial contracts and refusal of unqualified corner/stop arrangements. A test-only feasibility study and an adversarial matrix should precede one independent final physics/contract review. Symbolic f,d examples remain symbolic unless an illustrative numeric instance is separately declared.

A subsequent narrowly scoped **curved-interface paraxial power/apparent-position** API is supported by J15/J16. Gradient-index trajectories, 3D visibility and physiological eye models remain distinct later scope, not ad hoc numerical patches.

This prioritization is an **engineering recommendation from a fixed, nonrandom 20-case sample**, not a statistical ranking of the JEE corpus. No new production optics has been implemented by this audit; no additional independent review request is needed for source collection alone. PR #165 stays draft and the working engine stays on the approved merged baseline.
