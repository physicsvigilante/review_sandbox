# EMFEELD PR #58 — independent scoped review 01 (Chat B)

**Date:** 2026-11-19  
**Verdict:** **CHANGES REQUESTED** — narrowly scoped to the new capacitor V1 implementation.  
**Disposition:** Keep PR #58 DRAFT / UNMERGED. This review provides no production merge or release authority, and does not repeat the unchanged EMFEELD physics-engine review.

## Reviewed source and scope

- Candidate HEAD: `6f073802aa36601c7a78bc1bd320b74f43dbbfd1`
- Candidate tree: `841fe1c8b876363a2872ba98655ca9cffc0d5e3b`
- Main baseline: `51eee59836aac801c989e31712960571ceb94f39`
- Synthetic hosted merge: `afa8b4006d9b6fef21a098dee980b6e42ac68874` (**not** production main)
- Source: original hosted source ZIP and TAR in `PR58_Capacitor_Review_Kit.zip`; all five top-level kit manifest SHA-256 digests matched. Reviewer independently reconstructed all **439 tracked source files** with Git and obtained exact tree `841fe1c8b876363a2872ba98655ca9cffc0d5e3b`.
- Relevant new paths: `src/emfeeld/capacitor_lesson.py`, `capacitor_presentation.py`, `capacitor_view.py`, their focused tests, authored lesson, native qualification tool and guide. The unchanged Coulomb/gravity/Gauss/conductor/dipole engine and browser viewer were **not re-reviewed**.

## Reviewer-owned checks

1. Independently evaluated **264 accepted model states** spanning both signed-Q/fixed-voltage modes, signs `- / 0 / +`, admissible area/gap geometry and `κ = 1, 2, 4, 10`. Performed **3,696 cross-checks** against separately expressed Gauss/constitutive laws and field-energy density `U = (1/2) ε₀ κ E² A d`: capacitance, Q on both plates, signed V and E, energy, two free surface densities, P and two bound surface densities, and potential at three positions. **All passed.** Checked one-sided field refusal at each exact plate face, zero field outside, immutable SI sample arrays, arrow direction and display aspect normalization.
2. Independently verified the expected signed constrained comparisons: filling with `κ=4` multiplies `C` by 4; at fixed Q, `V,E,U` are divided by 4 and Q is constant; at fixed V, `Q,U` multiply by 4 while `V,E` remain constant. At `d × 1.5`, `C × 2/3`; fixed Q gives `E × 1` and `U × 1.5`, while fixed V gives `E,U × 2/3`. **All passed.**
3. **14 independent standard admission/refusal probes** and **3 raw duplicate/nonfinite-JSON probes** passed; additional extreme-value probes revealed Finding F1.
4. Reran the **63 available shipped physics/presentation tests** in this container with pytest plugin autoload disabled and warnings treated as errors: **63 PASS**. These are additional regression evidence, not the basis of independent reference claims.
5. Inspected all **8 original hosted PyVista PNG scenes**, their source/current reports and physical SI `.npz` vectors. **56/56 archived integrity digests matched.** Source code hashes, authored input SHA, exact current-state physics, readout state, stored field positions/vectors, screenshot SHA, and display-gap factor matched the reconstructed source. Visual checks found lower red / upper blue for positive Q, inverse for negative Q, green arrows reversing direction, no E arrows at zero Q, and material fill in dielectric cases. Hidden prediction mode retains true measurements in the evidence report without presenting them numerically on-screen.
6. Exercised a real installed **VTK slider representation** (not a PyVista scene) for admitted κ=10. With limits [1,8], `SetValue(10)` returns `GetValue() == 8`. This confirms the normal-input range inconsistency in F2.
7. **Limitation:** Independent full native PyVista event/scene execution was **not possible here**: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0 and VTK 9.6.2 are present, but PyVista is absent; isolated package retrieval failed due unavailable network/DNS. The eight original hosted PyVista scenes are credible developer-owned evidence, **not reviewer-owned native replay**. In particular, the shipped native tests trigger key events but call the `set_kappa`/`set_gap_factor` methods directly instead of dispatching a real slider end-interaction event.

## Required changes

### F1 — BLOCKER: silent underflow violates nonrepresentable-value refusal

**Where:** `src/emfeeld/capacitor_lesson.py` lines 22–31, 84–105, 164–175; strict admission/no-unrepresentable-values claim in `docs/CAPACITOR_LESSON_V1.md` lines 33–38 and charter Issue #57.

**Reproduced:**
- An otherwise valid raw JSON lesson with `"charge_C": 1e-400` (also `-1e-400`) is silently parsed/admitted as `0.0` (or `-0.0`) rather than refused, changing a nonzero authored physical state to neutral.
- `CapacitorState(charge_C=1e-170)` yields **nonzero V and E but exactly zero stored field energy**, because `0.5 * Q * V` underflows.
- `CapacitorState(mode="battery_voltage",charge_C=None,voltage_V=5e-324)` yields **nonzero E** with **reported free Q = 0**, violating the representable numerical consistency of `Q=C V` / Gauss-law reporting.

These values are outside normal JEE teaching ranges; however, the explicitly stated contract is to **refuse** nonrepresentable states, not silently accept altered outputs. The positive `charge_C=1e-170` input is itself a representable float, so JSON parsing alone is not the whole problem.

**Required fix:** Either enforce a documented nonzero lower engineering range for Q/V (preserving exact zero), or implement decimal-aware input validation and a sufficient representability/precision check for all derived reports. Guard underflow of nonzero Q, V, E, polarization where applicable, and stored U; preserve sign and zero behavior. Add regression tests for underflowing JSON numbers, positive/negative near-zero Q, near-zero fixed V, and nonzero inputs that produce zero/invalid derived energy or charge. Refuse rather than coerce silently.

### F2 — BLOCKER: admitted dielectric state cannot be faithfully represented by the real slider

**Where:** `src/emfeeld/capacitor_lesson.py` lines 52–53 (κ allowed in [1,10]); `src/emfeeld/capacitor_view.py` lines 60–69 and 133–139 (slider only [1,8] and widget synchronization).

**Reproduced:** VTK `vtkSliderRepresentation2D` with [1,8] bounds clamps `SetValue(10)` to 8. Thus a valid authored κ=9 or κ=10 may show the actual physical κ in the right readout while the dielectric slider indicates κ=8. On reset after a κ=10 authored state, this inconsistency recurs.

**Required fix:** Set the slider's admissible range consistently to the physical [1,10] (preferred), or consistently narrow the model contract and lessons. In real PyVista verify κ=9 and κ=10 input, slider knob/readout agreement, native slider change events, physical recomputation, reset, and resulting screenshot/current-state receipts.

## Remaining acceptance / improvement notes

- **A1 — required before scoped PASS:** Reviewer-owned actual native PyVista event replay on the repaired exact source, including real slider `EndInteractionEvent` behavior, key predict/reveal, camera changes without physics recomputation, negative polarity, zero field, and new source/current screenshot receipts. Hosted green PyVista CI is not a substitute for separate independent native execution.
- **R1 — nonblocking clarity:** The 3D panel truthfully says **"Gap EXAGGERATED; finite-plate fringing omitted"** and reports numeric `d`/area, while the evidence records the actual live magnification (20× for the original, 16.67× after adjustment). Displaying the current numeric exaggeration factor directly on-screen would better prevent a student treating the physical gap as literal scene scale. Continue labeling E arrows as direction-only.
- **R2 — preserved boundary:** Do not interpret differences in `U` as battery work or mechanical work. Do not add fringing, partial dielectric insertion, networks, charge-transfer animation, or unchanged-engine re-review to this narrow PR.

## Current-head CI verification (developer-owned)

Read-only GitHub verification for commit `6f073802aa36601c7a78bc1bd320b74f43dbbfd1` on 2026-11-19 found all **8/8 PR workflows complete / SUCCESS**: capacitor, general real-PyVista, Gauss, cavity, dipole, Three.js, source snapshot and clean-install release. The formerly pending **Linux** and **Windows** jobs of release run `44552107447` both now explicitly report **SUCCESS**. This replaces the stale "Windows pending" handoff status; it does not resolve F1/F2.

**Re-review gate:** Correct F1 and F2, publish focused reviewer-reproducible tests plus a fresh exact-head native control/scene capture, then request another narrow independent review. Keep PR draft/unmerged; any owner-controlled guarded merge and actual-main release qualification are future separate gates.

**No repository implementation files, developer evidence, historical review or PR merge state were changed by this review.**
