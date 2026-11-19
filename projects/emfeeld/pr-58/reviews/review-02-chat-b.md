# EMFEELD PR #58 — independent scoped review 02 (Chat B)

**Date:** 2026-11-19  
**Verdict:** **PASS — scoped to F1, F2, and A1 on the corrected exact HEAD.**  
**Disposition:** F1 CLOSED; F2 CLOSED; A1 CLOSED in reviewer-owned Linux EGL/native VTK testing. **No production merge or classroom/Windows-human acceptance is authorized.** Keep the draft PR unmerged for separate owner release gates.

## Identity and historical boundary

- Corrected PR: https://github.com/physicsvigilante/emfeeld/pull/58
- Corrected HEAD: **635c4985cf45c634ccc8b481e71c4ae65f4d7043**
- Reconstructed corrected Git tree: **95f6f0b09cb24daaa0c9b1dd064fc68e3d09dced**
- Qualified production main baseline: **51eee59836aac801c989e31712960571ceb94f39**
- Synthetic CI merge **2c17f1ed3750b76e2927ca2ae9d01e462fa70da4** is NOT production main. Current PR is OPEN, DRAFT, UNMERGED.
- Original reviewed HEAD: **6f073802aa36601c7a78bc1bd320b74f43dbbfd1**. The immutable Review 01 (CHANGES REQUESTED) stays at [review-01-chat-b.md](review-01-chat-b.md). The old findings, review data, and R1/R2 boundaries are not retroactively edited.

Independent source reconstruction from the supplied original-source ZIP: all 13 outer-kit SHA-256 checks passed, source ZIP SHA-256 **75145b4ac353d373e8b19c99125d2362f9449170d5e438c4febb28cf40a35e48**; inner tested-source.tar SHA-256 **f335800e9c25205ae51f9b2f3baa131b3473c0a51e247176d01f0fc741f6a03c**. Git index reconstruction from all **441 files** gave the exact corrected tree above; the 441 Git index entries matched the archived git-tree.txt listing. The seven-file review01_to_corrected.diff applied cleanly in reverse to the corrected source. No candidate production files were edited.

## Independent F1 challenge — PASS, CLOSED

Used fresh reviewer-owned tests OUTSIDE the candidate source; **63 F1 named probes/groups**. Checked both isolated-charge and battery-voltage modes:

- Raw authored numeric JSON tokens of each sign: extreme underflow (1e-400, 9.81e-9000), subnormal 5e-324, excessive 1e309, and sub-threshold but finite nonzero controls. Underflowing nonzero authored values are **refused**, rather than silently becoming neutral.
- Exact 0, -0, 0.0, -0.0, and zero exponent tokens are admitted as physically zero. Negative signed floating zero is preserved where JSON float syntax applies; integer -0 is semantically integer zero.
- Direct CapacitorState admission rejects tiny signed Q and V; both positive and negative derived Q or derived V below the documented minima are rejected. Defensive measure() rejects an artificially bypassed tiny Q or V before publishing an inconsistent zero.
- Accepted boundary cases have finite nonzero C, Q, V, E, U and surface density with correct polarity. At kappa=1, P=0 for physical reasons; at kappa>1 with admitted nonzero control, P remains nonzero with the correct sign.
- Independently cross-checked reports against C=epsilon0*kappa*A/d; Q=C*V; E=V/d; U=Q*V/2; and P=epsilon0*(kappa-1)*E, including upper/lower surface charge signs.

The corrected implementation enforces the explicitly documented bounded lesson domain: independently authored nonzero **|Q| >= 1e-18 C** and **|V| >= 1e-12 V**, plus derived lower-bound/refusal checks. This is an **engineering-scale finite-float contract**, not arbitrary-precision or universal numerical exactness. Original Review 01 F1 underflow examples are refused.

## Independent F2 and genuine native A1 challenge — PASS, CLOSED

Runtime: **Python 3.13.5, VTK 9.6.2, PyVista 0.48.4, NumPy 2.3.5, SciPy 1.17.0**, Linux headless **vtkEGLRenderWindow** / software OpenGL. PyVista and its pure-Python extras were installed solely in a disposable target from the kit's offline wheels; native VTK was already available. Reviewer-owned experiment script and logs live outside the source.

**F2:** Instantiated the actual production CapacitorLesson, with **negative free Q = -2.3e-9 C** and authored initial **kappa=9**. Real vtkSliderWidget representation gave bounds **[1,10]**, knob **9**, fully matching the physical contract. SetValue(10) followed by an actual **EndInteractionEvent** on the native slider widget produced knob/physical/readout **kappa=10**, a newly prepared field and recomputed energy. The reverse native event returned all to **9**, and a further 10 event behaved consistently. At fixed negative Q, observed correct C ratio 10/9 and signed V and U ratio 9/10. At kappa=10: V = **-9.741153199491242 V**, U = **1.1202326179414929e-08 J**, physical readout kappa=10; preparation count increased once per effective edit.

**A1 native transitions:** Actual VTK interactor **KeyPressEvent** for 'v' toggled prediction/reveal; real **LeftButtonPressEvent/MouseMoveEvent/LeftButtonReleaseEvent** rotated the native camera. A deliberately poisoned physics-preparation function proved reveal and camera orbit use existing prepared state without new field preparation. Actual '0' key reset restored original negative-Q kappa=9 physical state, knob 9 and fresh consistent measurement. Separately, a native gap-slider EndInteractionEvent requested an invalid factor 1.5 near the d/sqrt(A) boundary: the model and prepared state remained unchanged, notice displayed refusal, and the knob returned to 1.0. A later allowed factor 0.8 succeeded.

**Separate zero-field native scene:** New genuine PyVista rendering with kappa=4, Q=0 showed 0 V, 0 E, 0 stored U, no field arrows, neutral plate display, source/current match and a fresh valid screenshot.

**73 total independent named checks/groups: 63 F1, 1 F2, 9 A1; all PASS.** These are independently authored and executed; they do not count developer-owned tests or the previous 264-case physics reference study.

## Reviewer-owned evidence and provenance

Fresh reviewer-owned files (available in the accompanying chat evidence ZIP, **EMFEELD_PR58_R2_Independent_Evidence.zip**, SHA-256 **837ac049e468e25e814ee6b7fad667015cc6495b4eea39bbd8d383f3b2b3a25c**):

- Independent replay source: reviewer_f1_f2_a1.py (SHA-256 **78d75d8a1058119e7094affe3eeaca9b2664f8288dc6a45d42c3cc4d2b8ac56f**) plus run log, 73-case JSON results and native-event JSON trace.
- Current-state negative-Q **kappa=10 PNG**: reviewer_owned_native_k10/view.png, SHA-256 **29c2c85eed37ab59c53cb41b707104f1674d64e7b7086467007c4bfaf370a59e**; accompanying authored-input.json, lesson.json, report.json, physical field_samples.npz, integrity.json. The source and current states correctly differ. All receipt SHA checks passed; computed SI vectors matched current native preparation. Screenshot independently opened and visually checked: positive upper plate red, negative lower plate blue, field arrows downward, kappa=10 readout/slider and dielectric.
- Reviewer-owned **zero-field PNG**: reviewer_owned_native_zero/view.png, SHA-256 **543289c10743e4ce91490331ba0b15c37ccac881302a28ce4c1ca30baf6a046b**, with its own source/current receipt and SI samples. All receipt checks passed; screenshot opened and checked for neutral plates and absent arrows.
- Complete source/current receipt and code hashes are contained in the evidence ZIP; no developer screenshot was substituted for reviewer-owned replay.

Separately, the supplied **developer-owned** nine-scene original archive was audited: **9/9** reports matched physical laws, **9/9** sample arrays matched prepared source, all **63/63** per-file integrity digests matched, and all nine PNGs were nonblank with source-code hashes matching the corrected tree. This confirms *archive integrity only*, not reviewer ownership of the developer scenes.

## Exact-head hosted CI (developer-owned)

Verified read-only from GitHub for corrected HEAD **635c498**: all eight named Actions runs completed with **SUCCESS**, including dedicated capacitor **44563564350**, source snapshot **44563564702**, general real PyVista **44563564440**, Gauss **44563564449**, cavity **44563564736**, dipole **44563564365**, browser/Three.js **44563564526**, clean-install **44563564778**. The last run's **Windows Server 2022 Python 3.13.5** and **Ubuntu 24.04 Python 3.13.5** jobs are individually completed/SUCCESS. None are pending and none should be confused with production-main qualification.

## Preserved findings / limitations

- **Historical Review 01:** CHANGES REQUESTED for F1/F2 and reviewer-native A1 gate at old SHA; remains unchanged and valid *for that historical source*. This review only closes these items on the corrected exact SHA.
- **R1 (nonblocking):** The rendered scene identifies its gap as exaggerated, but does not print the current numeric exaggeration factor on-screen. Retain as a possible clarity improvement, not a new blocker.
- **R2 (scope boundary):** Uniform ideal field, no finite-plate fringing, no partial insertion/networks, no charge transfer or dynamics; stored field energy is not net battery work or mechanical work.
- No 264-case reference replay, full engine re-review, Windows human desktop test, classroom usefulness acceptance, or production-main release qualification was performed. A Linux headless genuine VTK/PyVista event replay does **not** establish those broader gates.

**FINAL: PASS on corrected HEAD 635c498 / tree 95f6f0b for F1, F2, A1 only.** Keep PR #58 unmerged and preserve the previous review; separate owner-controlled merge and release checks remain necessary.
