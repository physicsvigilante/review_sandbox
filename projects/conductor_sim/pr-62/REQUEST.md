# conductor_sim PR #62 — M27a R2 independent physics and visualization review

**Status: awaiting independent Chat B review. Source PR is DRAFT and UNMERGED.** This packet is authored by Chat A (implementer), not the independent reviewer or the owner. Do not treat CI or this packet as a passing independent verdict.

| Pin | Immutable value |
|---|---|
| Project | `conductor_sim` |
| Source repo | [physicsvigilante/conductor_sim](https://github.com/physicsvigilante/conductor_sim) |
| Source PR | [Draft #62](https://github.com/physicsvigilante/conductor_sim/pull/62) |
| Base SHA | `923ac2c49b23439cc9c76604bfd2a945e984d221` (verified merged M26a main) |
| **Exact source head for review** | **`666e6815390830cb6b70b474648b5b5ec765e380`** |
| **Exact source tree for review** | **`72a6dc67383b270b11e639ad81c1e52b693b0565`** |
| Risk | **R2 — new electrostatic E/V law and near-singularity numerical/observation semantics** |
| Report destination | `physicsvigilante/review_sandbox/projects/conductor_sim/pr-62/reviews/review-01-chat-b.md`, authored by Chat B only |

Read [central cross-sandbox review protocol](../../../PROTOCOL.md), [risk policy](../../../REVIEW-RISK-POLICY.md), [report template](../../../REVIEW-TEMPLATE.md), [the source composability contract pinned to the head](https://github.com/physicsvigilante/conductor_sim/blob/666e6815390830cb6b70b474648b5b5ec765e380/docs/composability_contract.md), and [evaluation contract](https://github.com/physicsvigilante/conductor_sim/blob/666e6815390830cb6b70b474648b5b5ec765e380/docs/evaluation_contract.md). Check for an actual AGENTS.md in this source tree; report a missing file rather than inventing instructions.

## Physically bounded new capability

Historical `UniformRingAxisField` supports V and E only on its real symmetry axis. It is **unchanged and still refuses off-axis evaluations**. New source `UniformRingField` in [prescribed_fields.py](https://github.com/physicsvigilante/conductor_sim/blob/666e6815390830cb6b70b474648b5b5ec765e380/src/conductor_sim/prescribed_fields.py) represents the **same ideal nonconducting uniformly charged thin ring**, but computes genuine off-axis *static* E and V in arbitrary 3D world positions and ring orientations. Sources are fixed and nonresponding; their charges never redistribute because of the probe or other sources.

In cylindrical coordinates about ring centre/axis, use total Q, radius a, radial coordinate rho, axial z, permittivity epsilon, Coulomb k=1/(4*pi*epsilon), b=sqrt((a+rho)^2+z^2), d=sqrt((a-rho)^2+z^2), elliptic m=4*a*rho/b^2:
- `V = 2*k*Q*K(m)/(pi*b)`
- `E_z = 2*k*Q*z*E(m)/(pi*b*d^2)`
- `E_rho = k*Q*(K(m) + ((rho^2-a^2-z^2)/d^2)*E(m))/(pi*rho*b)`
- `E_world = E_z * axis + E_rho * unit(radial_displacement)`

These are evaluated in pure Python using bounded Carlson RF/RD duplication of complete K/E, with the **complementary** elliptic parameter `p=d^2/b^2` directly (not numerically hazardous `1-m` near the wire), normalized coordinate scale, and a near-axis fourth-order potential expansion avoiding cancellation in radial E. The physical wire's V/E divergence is explicitly `SingularField`; `clearance_at` is the 3D distance to an ideal line singularity, NOT material contact. Invalid/poorly resolved geometry is refused. Negative Q reverses field/potential; linear source superposition and permittivity scaling remain supported.

**Crucial M27a scope:** This is STATIC E/V. Existing `TestChargeMotionSpec` and `DipoleMotionSpec` now explicitly refuse `UniformRingField` until a separately validated M27b motion-plane/guard contract. No general particle motion, phantom axial guide, induced conductor physics, new ODE, source dynamics, field-line integration or time evolution has been implemented.

## Source-faithful educational example and static observer

The new [ring_field_observer.py](https://github.com/physicsvigilante/conductor_sim/blob/666e6815390830cb6b70b474648b5b5ec765e380/src/conductor_sim/ring_field_observer.py) samples a complete 3D E and V on an authored 2D `SliceSpec` plane. It stores world E vectors AND components parallel/normal to the chosen observation plane; dark SVG arrows show **only in-plane projections**, labelled as such. Ring rims are dashed true 3D orthographic projections, not charged rods actually in the slice. Grey masks exclude nodes near the actual 3D ideal charged wire or point, never assert E=0. A separate validator reconstructs the saved source inventory and recomputes grid observations and projected geometry; browser has NO physics solver, ODE or time-slider.

[examples/m27a_ring_field.py](https://github.com/physicsvigilante/conductor_sim/blob/666e6815390830cb6b70b474648b5b5ec765e380/examples/m27a_ring_field.py) uses the previously independently source-checked workbook physical p12 Q40–41 Ring A/B: both horizontal world-x axes, +10 μC and −20 μC, each radius .30 m, separation .40 m, vertical world-+y uniform E=100,000 V/m. The **display slice/grid/mask** are explicit teacher-chosen values. The real transverse E remains in the saved E-normal field and world vectors. Q40 endpoint work is independent of the fictitious axial-motion interpretation; Q41 supplies a symbolic mass, not a numerical trajectory. The new static viewer does not claim that the test particle remains on x.

The old M21b 2D point-field map, M19b axial-only motion exports, conductor API and standalone viewer stay unchanged. New sources are an opt-in distinct built-in source kind, with typed stable IDs through existing `PrescribedField`/observer contracts.

## Immutable charter and exact source delta

- Preimplementation [frozen M27a charter](https://github.com/physicsvigilante/conductor_sim/blob/666e6815390830cb6b70b474648b5b5ec765e380/docs/m27a_charter.md) was committed at `ba9fd06729150ffc86c2e3a5e89650b6b9fa567e` **before** source implementation or first reserved execution.
- First functional candidate `ea5436f525618bee156bf756e9ef5e1b37d7a057` added new source formula, static observer/HTML, tests, source example and CI checks. **17 of its 18 applicable PR workflows passed; the new browser step failed due to a real 390-pixel mobile overflow (399 pixels).** [Original failed visualization run 43749110967](https://github.com/physicsvigilante/conductor_sim/actions/runs/43749110967). Its failed screenshot/log and artifact remain historical evidence.
- Candidate `d87209f9e17e61afd1e3037a4fe4037de7959903` addressed an additional valid tilted `SliceSpec` observer round-trip: projection coordinates tolerate a few floating-point ulps after reconstructing normalized plane vectors, while IDs/source world quantities stay strict. This added one test and did not modify the physical source law.
- **Final exact head `666e6815390830cb6b70b474648b5b5ec765e380`** corrected the mobile layout by wrapping static source/readout tables rather than hiding overflow. No old physics, integrator or historical viewer behavior was modified in these revisions.
- [PR #62 diff](https://github.com/physicsvigilante/conductor_sim/pull/62/files) has 15 changed/new files, comprising frozen charter/docs, new physics and static observer modules, narrow safeguards/exports, new example, test/browser/reserved tools, workflow steps and README.

## Exact-head GitHub CI — observed by Chat A, not independent review

**18/18 applicable PR workflows completed SUCCESS at `666e6815...`**.

| Gate | Verified result |
|---|---|
| Complete Python 3.10/3.12 | [Run 43749664846](https://github.com/physicsvigilante/conductor_sim/actions/runs/43749664846): **1,788 passed, 97 live-FEMM-dependent skipped, 9 warnings** on EACH interpreter |
| Actual FEMM 5 | [Run 43749664972](https://github.com/physicsvigilante/conductor_sim/actions/runs/43749664972): **97 passed**, genuine conductor-domain **nonregression**, not a numerical ring reference |
| New fixed-source physics + reserved | [Run 43749664865](https://github.com/physicsvigilante/conductor_sim/actions/runs/43749664865): **141 focused passed** (1 warning), reserved independent Coulomb-line and static Ring A/B HTML/JSON generation all pass |
| Full visualization/real Chromium | [Run 43749664767](https://github.com/physicsvigilante/conductor_sim/actions/runs/43749664767): success, including **real Chromium M27a two-ring** source/normal-E/physical mask/390px checks (no console, page errors or network requests) |
| Final static HTML/JSON/PNG evidence | [Artifact 14175598957](https://github.com/physicsvigilante/conductor_sim/actions/runs/43749664767/artifacts/14175598957), GitHub-published `sha256:ab340a971b81c81df98bbd1dd04bda49795a475fb0b3efacd2fdbe94986516f4`. **Not independently downloaded/rehashed by Chat A**. |
| Focused field/source artifact | [Artifact 14175258151](https://github.com/physicsvigilante/conductor_sim/actions/runs/43749664865/artifacts/14175258151), GitHub-published `sha256:4eb7bf5b016ea318a76187ed3f653d2f5bc2b8fbb25b0d61c2fa367c50b324fa` (not independently rehashed). |

**Reserved R1 first execution** occurred on already frozen first source candidate via [run 43749110983](https://github.com/physicsvigilante/conductor_sim/actions/runs/43749110983), **before subsequent viewer/round-trip fixes**; it PASSED without retuning the source physics. At final head it is a regression rerun, not a new first attempt. Original frozen inputs: Q=-2.3 nC, a=.17 m, center=(.08,-.06,.11), axis=(2,-1,3), point=(.155,.047,.227), epsilon=1.35*epsilon0. Final source-head reserved direct Coulomb reference has potential relative error 0, max component field relative error `2.320503542318095e-14`, max finite-difference E=-grad V error `1.75755601605089e-09`. These errors support THAT specific case, not global error bounds. The independently coded direct Coulomb circular-line midpoint rule (not the Carlson implementation) is in tests and reserved tool; a separate independent ChatGPT has not yet verified it.

## Adversarial independent review tasks (no predetermined verdict)

1. **Physical law and conditioning:** Independently derive or numerically check K/E formulas for arbitrary signs, off-axis rho inside/outside, z signed, radial E sign, far-field decay, `E=-grad V`, axis reversal and rotated/translational coordinate covariance. Challenge novel points near-but-not-on ideal wire (with independent quadrature/high-precision computation), near the axis, and extreme resolvable scales. Does Carlson RF/RD and near-axis expansion give trustworthy E/V or hide a pole/false zero?
2. **Physical qualification and scope:** Can `UniformRingField` silently enter `TestChargeMotionSpec`, M24b driven motion, or constrained dipole dynamics despite M27a's static-only contract? Are legacy axial-only ring failures, conductor response, historical source models and guard meanings preserved? Does adding new `SOURCE_TYPES` admit unintended dynamic paths?
3. **Static map/source geometry:** Verify true 3D ring rim projection vs actual slice intersection, source masking by real 3D proximity rather than the projected outline, complete E including normal component, actual negative and positive Q, unchanged field and source order, and validated data against tampering. Check weird rotated planes and 390px Chromium presentation. SVG arrows may normalize length and field colours are visualization scalings; no time evolution should be implied.
4. **Independent evidence:** Inspect exact GitHub SHA/tree, full Python 3.10/3.12, real FEMM nonregression, focused quadrature/reserved first attempt, failures and corrected mobile output. If executable tooling is available, independently author at least one *new* off-axis ring situation not among developer cards and calculate V/E via independent circular line integration, derivative or trusted reference. Document every attempted test including first failures and any missing tools.
5. **Separate educational judgments:** Evaluate JEE source fidelity vs added teaching parameters, physical/numerical correctness, static simulation coverage, visual honesty, usefulness and optional textbook answer completeness independently. An authentic Ring A/B map is **not** an executed particle-motion solution or a representative performance survey.

**Known boundaries:** Ideal infinitesimal nonconducting ring; homogeneous eps; stationary prescribed sources; no finite-thickness conductor, charge induction, arbitrary free-3D motion, general disc off-axis fields, collision, ring source dynamics, external JSON authenticity, universal 3D field-line map or auto PDF interpretation.

## Required independent output and merge boundary

Chat B must author its own **new append-only review report**
`projects/conductor_sim/pr-62/reviews/review-01-chat-b.md` under
`physicsvigilante/review_sandbox` (directly on review hub main or a review-only PR), following the [template](../../../REVIEW-TEMPLATE.md). State exactly reviewed SHA/tree, pass / changes-requested / insufficient-evidence, concrete severity/scoped findings, independent calculation attempts and unknowns. Never write a review verdict on behalf of Chat A, and **do not edit or merge PR #62**. If it cannot write the report, say so clearly.

Once the owner returns and says **"Review complete"**, Chat A retrieves and triages the report. Even an independent PASS requires separate explicit owner approval to merge.