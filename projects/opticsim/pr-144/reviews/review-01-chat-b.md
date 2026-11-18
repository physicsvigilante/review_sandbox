# Independent R1 — Opticsim PR #144: typed planar apparent-depth query v1

**Review date:** 2026-11-18  
**Reviewer:** Chat B — independent source/physics/Git-object/CI-log inspection  
**Verdict: CLEARED FOR OWNER DECISION — draft source review only; NOT merge or release approval.**  
**Blocking findings:** P0 **none**, P1 **none**.  
**Nonblocking hardening:** N1–N4 below. The ten new tests and existing browser/native CI are **builder execution**, not an independent rerun by this reviewer. The independent execution here was a separate numerical evaluation of the optical equations, not Opticsim, Node tests, PhyDemo or Chrome.

## 1. Pinned review identity and scope — verified

- Draft [Opticsim PR #144](https://github.com/physicsvigilante/opticsim/pull/144) is open, unmerged and not release-approved.
- Production base main: `d3509e82fb65d81aabe336666851f8f2962623f4`.
- Exact PR HEAD: `aea25a9b480260e2498229d80f7f6cbe3d4ac574`.
- HEAD Git tree: `e1fe378b7070ef6be53f34faa798e75774f877a5`, read from the actual Git commit object.
- Synthetic CI merge: `186141dae6c56ae631be4b9e3e0839f6db0a5653`; its actual Git commit object has **the same tree** `e1fe378b7070ef6be53f34faa798e75774f877a5` and **parents in order** [production base, exact HEAD].
- GitHub compare of production base to exact HEAD: **4 ahead / 0 behind**; merge-base equals production base. Four added files, **520 additions / 0 deletions**, nothing else: `src/planar-apparent-depth-query.js` (149), `scripts/planar-apparent-depth-query.mjs` (66), `test/jee-apparent-depth-query-v1.test.mjs` (240), `docs/JEE-PLANAR-APPARENT-DEPTH-QUERY-V1.md` (65).
- No changes to existing v1–v13 schemas, native adapter, pinned PhyDemo, existing browser paths, or held v14–v19 source. This is new analytical production code, **not** inherited approval from test-only PR #143.

Read and inspected the four files at the exact commit and relevant unchanged dependencies `src/angular-math.js`, `src/planar-media.js`, `src/qualified-utils.js` and `scripts/authoring-evidence.mjs`.

## 2. Independent physics evaluation

Take the oriented plane at `P`, normal `n=(cos φ,sin φ)`, CCW tangent `t=(-sin φ,cos φ)`, known source `S` in the negative half-plane, real perpendicular depth `d=−(S−P)·n>0` and source-normal foot `F=P+[(S−P)·t]t`. For signed incidence `i` and a propagating transmitted solution,

`sin r=(n_source/n_observer) sin i`;  
`Q=F+d tan(i)t` (predicted interface crossing);  
`d_app=d tan|i|/tan|r| = d (n_observer/n_source) cos(r)/cos(i)`;  
`A=F−d_app n` (conditional source-normal axis intercept).

The implemented `analyzeApparentDepth` follows this vector construction and correctly uses a conditional **mathematical back-extension**, not native reverse propagation or detected imaging. The cosine-ratio form avoids direct near-axis 0/0. I computed the following independently with standard trigonometric functions, not the implementation.

For S=(-60,0) mm, plane x=0 with normal +x, indices 1.5→1 and a hypothetical detection line at x=100 mm:

| i (deg) | r (deg) | d_app (mm) | predicted y at x=100 (mm) |
|---:|---:|---:|---:|
| 2 | 3.000762438 | 39.969501869753 | 7.337358459 |
| 5 | 7.511987115 | 39.808183423875 | 18.435854238 |
| 12 | 18.171812994 | 38.854078501260 | 45.577216043 |
| 25 | 39.340476504 | 34.133771193526 | 109.945551056 |
| 30 | 48.590377891 | 30.550504633039 | 148.030358054 |

These match the encoded scalar assertions at the stated tolerance. Independently: 1→1 at 5° gives **60 mm**; reversing to 1→1.5 at 5° gives **90.191153657690 mm**. The expressly requested paraxial limit for 1.5→1 is **40 mm**. One exactly axial finite-angle ray does **not** determine an image position and is correctly `not-identifiable`.

Signed and rotated/laterally offset checks: with φ=90°, S=(17,−60) mm, P=(5,0) mm, i=−5°, the true foot is (17,0), computed crossing is (22.249319812,0) and conditional intercept is (17,−39.808183424). With φ=180°, S=(60,13), P=(0,0), i=+12°, crossing is approximately (0,0.246606300), intercept (38.854078501,13). Independent vector-line back-extension matches both constructions. ±i has opposite crossing tangent displacement and equal depth. 6 cm/0.06 m input is numerically equivalent to 60 mm under the documented unit conversion.

Critical incidence for 1.5→1 is `asin(2/3)=41.8103148957786°`. At the critical angle and ±1e−11°, dimensionless Snell-ratio deltas are inside `±2e−12`; `classifySnellTransmission` makes these **numerically-unstable**, before any `asin` clipping can manufacture transmission. At `i_c−1e−5°` a real transmitted direction exists; at `i_c+1e−5°` and 50° the code correctly withholds the value as `TIR-no-transmission`. On very small nonzero incidence or grazing and on unbounded projections, the code returns `numerically-unstable` with `value:null`. There is **no discovered near-critical erroneous acceptance or clamp-to-image**.

## 3. Typed input, numerical refusal and provenance

`fields()` plus finite-number checks enforce a closed top-level/point/plane/observation schema, explicit source coordinates, plane location and signed orientation, explicit refractive indices in [1,4], angle or *separate* paraxial request, and unit mm/cm/m. Reversed/unknown source side is refused; no silent swap of indices or normal. Coordinates are bounded at ±10000 mm; source clearance is at least 0.01 mm from the plane on its **negative side**. Nonfinite numbers, missing fields, unknown keys, invalid angle values, and a contradictory angle on a paraxial request are rejected. Returned axis/crossing coordinates are independently checked for finite bound compliance. Input objects are read, not mutated by the analytical operation.

`native.status:'not-run'`, `native.observations:null`, `nativeImageDetected:false`, the `not-assessed-by-engine` support/interpretation and strong limitations are consistent across analytical and CLI reporting. A real detector hit, observer position, brightness, Fresnel selection, source ancestry, sharpness, PSF or physical image is **not** inferred. Withheld statuses carry `value:null`. The deliberately restricted standalone query is not a substitute for a complete native scene.

The CLI `runApparentDepthEvidence` hashes **original input bytes** with SHA-256 and writes those bytes unchanged to `input.json`. A valid result creates `analytical-result.json` and `report.json`, each keyed to the original hash; malformed JSON creates a rejection report and **no** analytical result; no native scene is authored. It bounds input to 1 MB, reserves a new directory beneath the repository's `test-artifacts/llm-authoring/`, rejects overwrites, checks symlink ancestors, and uses exclusive file creation. This is evidence freshness/provenance, **not** an OS-level tamperproof storage or hostile-concurrent-process guarantee.

## 4. Native tests and actual CI evidence

The ten new tests cover finite-depth benchmarks, ± headings/index direction, translation/rotation, unit equivalence, axial vs separately requested limit, Snell critical/TIR, schema refusal and clearance, a fully authored **test-only** native v5 single-ray cross-check, stale/incomplete suppression, and CLI byte/hash/rejection/no-overwrite. The native-only test explicitly sets source brightness 1, `single-ray` directions, `partialReflection:false`, a finite observer-side detector, and checks **actual native** completed status, one emission/crossing/hit, matching event/transmitted branch direction, incident/refracted angles, detector hit coordinates, observation methods, matching canonical SHA and a stated approximate-Fresnel warning. A line extension of the measured native hit is used solely as **a test oracle**, not returned as a native image. It does not establish multi-ray parentage or a viewing observer.

The stale edit changes an authored source angle after the native run and checks all observables suppressed due to SHA mismatch; setting native max ray depth to zero gives incomplete status, null observations and suppressed outputs. These are appropriately **separate from** the public analytical operation.

I inspected the GitHub Actions **run records, job steps and actual job logs** for this exact HEAD. GitHub's 11 associated pull-request workflow records all report completed/success. [Optical composition #44277301999](https://github.com/physicsvigilante/opticsim/actions/runs/44277301999), job `134708577338`, and [planar angular #44277302418](https://github.com/physicsvigilante/opticsim/actions/runs/44277302418), job `134708578063`, both list the ten new test names passing and each log reports **800 tests / 800 pass / 0 fail / 0 skipped**, followed by their successful builds/acceptance steps. Their PR source-head SHA is `aea25a9...`; the synthetic merge's checked Git object has the same source tree.

**Evidence boundary:** all Node/PhyDemo/Chrome workflow executions are **builder CI**, not an independent test run by this reviewer. The present reviewer independently verified geometry by separate numerical calculations, inspected exact source and CI logs, and verified Git ancestry; no local Opticsim/PhyDemo/Chrome execution, modification or install occurred. Passing tests do not prove unique real-image reconstruction, general source ancestry or scene-composition coverage.

## 5. Findings and bounded disposition

**P0:** None found. **P1:** None found within this intentionally limited standalone analytical v1 contract.

- **N1 — Extend geometry assertions (nonblocking).** Current regression directly tests φ=0° and φ=90° for a centered source. Add φ=180° and a laterally offset source/plane pair with explicit expected crossing and intercept coordinates, not only translated/rotated versions of the centered fixture. The independent calculations above indicate source math is correct; this strengthens regression protection.
- **N2 — Bound numerical state transitions more tightly (nonblocking).** Add explicit just-inside/just-outside `2e−12` Snell-ratio tests, a near-grazing case **also** beyond critical (current order deliberately chooses `numerically-unstable` before definite TIR), coordinate-projection out-of-bounds refusal and near-clearance rotated cases. Document/test this status precedence rather than letting future refactoring silently change it. All such cases withhold values today; there is no known bogus transmission.
- **N3 — Describe evidence immutability narrowly (nonblocking).** The exclusive-write fresh directory is not externally immutable, and symlink checking is not hardened against a hostile process racing path components (as the shared helper itself notes). Avoid upgrading SHA-256/freshness into authentication or tamperproof claims. Consider pre-read file-size validation if this CLI ever accepts untrusted giant local inputs; current 1 MB bound is enforced after `readFileSync` loads the file.
- **N4 — Keep native crossing provenance narrow (nonblocking).** The native test checks recorded interface angles/outcome/directions and native detector hits, with crossing predicted independently; it does **not** independently assert a native planar-interface `pointMm` from that first-event observable, which currently has no planar point field. Do not describe this as direct native crossing-position capture. Add such evidence only if exposed faithfully by the native instrumentation, not by reconstructing a guessed path.

**Verdict: CLEARED FOR OWNER DECISION.** This means the explicitly bounded typed analytical apparent-depth feature is adequately reviewed for an owner-controlled next step. It does **not** authorize merging PR #144, PR #143, held v14–v19 work, or treating #123 branch-protection as resolved. Keep draft/unreleased until a separate owner decision, preserving exact-head evidence and existing independent gates.