# Independent scientific review #01 — conductor_sim PR #100 M40a

**Reviewer: Chat B, independently authored source-pinned test suite.**  
**Verdict: CHANGES REQUESTED** — one concrete, reproducible local-sigma accuracy blocker at the admitted near-unit-normal / near-wall boundary. The new multicavity Gauss/Kelvin physics otherwise passed the reviewed unfamiliar composition.

This is not a production merge authorization. [Production PR #100](https://github.com/physicsvigilante/conductor_sim/pull/100) must remain **DRAFT / UNMERGED**. No production source, historical FEMM/browser, original problem PDFs or production branches were modified by this reviewer.

## Source identity and preserved scope

- Literal reviewed candidate **HEAD**: `f38fb82f27312f9ea1526c1a65bb93657937a0cb`.
- Actual native Git **TREE**: `0495115a3ad0d38c71f704ae14a8842d466afe55`.
- Released base: `6257ae9c7d7a0e7da2a12cb01a8519b0f2baa7b0`.
- Independent GitHub Actions runner checked out the **literal commit**, asserted `git rev-parse HEAD` and `HEAD^{tree}`, fetched complete history, and asserted `git diff --name-status base head` contained precisely **seven A-only files**, no legacy edits/deletions. The review also rechecked the live PR HEAD, draft and merge state after tests.
- Exact candidate source files examined: `src/conductor_sim/spherical_multicavity.py`, original `cavity_gauss.py`, `tools/m40a_spherical_reference.py`, `tools/m40a_spherical_example.py`, `tests/test_m40a_spherical_multicavity.py`, scientific charter/documentation and CI definition.
- Original PDF SHA256 on pinned runner: `02_conductors_half_size.pdf` = `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d`; `POTENTIAL_CONDUCTORS1.pdf` = `8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5`. Charter digest: `b9da8056206f0c3026edee543712ff7fca070f535e11f95d89eb1beea4e7fdf3`. Compare confirms old PDF blobs unmodified.
- Developer's dedicated [exact-head M40a workflow](https://github.com/physicsvigilante/conductor_sim/actions/runs/44533737399) concluded SUCCESS. The PR reports a broader 24-workflow/29-check preflight; this review did **not** independently re-run inherited FEMM or Chromium suites.

## New independent teacher model: physical geometry and identities

Reviewer-authored, **six** genuinely nonconcentric spherical cavities and **12** individually named charges: a nonempty signed-neutral cavity (A), an empty cavity (C), four unequal, obliquely placed signed/mixed cavities (B/D/E/F), a single spherical exterior with center `(0.35,-0.21,0.40) m` and radius `12 m`. The six void radii are `0.85, 1.15, 0.65, 0.92, 1.20, 0.70 m`. This is neither the developer three-void illustration nor an invented original workbook answer.

Independent Euclidean geometry, **not** production's validated flag:

| Independent check | Result |
|---|---:|
| Minimum metal gap between two distinct voids | 2.5910021391573324 m |
| Minimum void-to-outer-wall metal gap | 5.057059510848684 m |
| Minimum source-to-assigned-void wall gap | 0.368639169484382 m |
| Physical source ID inventory | 12 distinct named IDs |
| Empty cavity / distinct-site neutral cavity | Yes / Yes |

All placements were recomputed by reviewer 3D vector subtraction, Euclidean norms and physical one-to-one source membership. The exact names and source ordering are in [reviewer source](../reviews/review-01-chat-b-probes.py).

## Separate physics derivation and native execution: PASS

Independent normal-field formula was derived from a real charge plus the Kelvin image placed at `a^2 u / |u|^2` with charge `-q a / |u|`; the wall sigma is `-epsilon E_cavity dot n`. A **second** independent computation used a one-sided radial finite difference of the Dirichlet real-plus-image *potential*, not the production closed-form sigma kernel. On genuinely unit nonaxial normals, all **30** native local-density comparisons (15 distinct local probes repeated for isolated and grounded states) matched the separate Kelvin-field mathematical predictions and finite-difference checks at the reviewer-specified tolerances. The bundled oracle was used only as an additional JSON trust-boundary check, **not** as the source of expected native values.

Native `inner_surface_charge_density` was then integrated with independently authored 2D midpoint quadrature in `mu=cos(theta)` and azimuth `phi`; an independent real+image surface quadrature used higher resolution. Numerical convergence from coarser to finer grids:

| Cavity | M39a Gauss face charge | Independent 64×128 | Independent 128×256 | Native 48×96 |
|---|---:|---:|---:|---:|
| B (mixed) | -3.800000000e-9 C | -3.800031947e-9 | -3.800007987e-9 | -3.800056791e-9 |
| E (mixed) | -1.500000000e-9 C | -1.500085456e-9 | -1.500021363e-9 | -1.500151934e-9 |
| A (distinct-site net-zero) | 0 C | +1.124547e-14 | +2.810579e-15 | +1.999776e-14 |

Nonzero neutral cavity A *local* sigma was confirmed (e.g. `-1.6362833422109133e-10 C/m²` at the first oblique normal) while its integrated charge is zero. An independently authored centered-source analytic check gave `-3.5728660694098953e-10 C/m²`; displaced near/far pole checks reproduced `-1.5631289053668295e-9` and `-1.0004024994347706e-10 C/m²`, respectively.

Under exactly the same source inventory and geometry:
- Isolated `Q_metal = +2.8e-9 C`, total internal source charge `+2.8e-9 C`, `Q_outer = +5.6000000000000005e-9 C`, outer uniform `sigma = 3.0946794490090764e-12 C/m²`, exterior flux `632.4690777288907 V·m`.
- Grounded `Q_metal = -2.8000000000000003e-9 C`, `Q_outer = 0`, outer `sigma = 0`, exterior flux zero.
- All 15 tested inner samples were **identical between the two separate static hypotheses**.
- Moving a source within original A changed local sigma from `-1.6362833422109133e-10` to `-9.432380962362559e-11 C/m²` without changing its zero integrated face charge or mutating the parent model.
- Source reordering, cavity ordering with matched source IDs, 3D rigid world rotation and transformed normals, and uniform world translation preserved the physics.

## Hostile qualification and evidence-boundary probes: PASS

**35** independently authored invalid-input/native-and-JSON refusals passed. They include Boolean/nonunit/nonfinite normals; Boolean positions/radii/charges; duplicated, wrong and swapped IDs; source on/too close to its wall; genuine *intervoid wall contact with every source translated along with its void*; genuine outer-wall contact with sources still internally valid; missing geometries; invalid outer IDs; wrongly labeled SI/provenance/grounding and false original-JEE counts; invented E/V/force/wire time; native low-level Gauss-ledger tampering; near-cancelled theoretically nonzero local sigma. Exact same-location opposite-charge cancellation correctly returned zero.

Very near-wall **admitted** geometry yielded finite nonzero sigma; slightly closer (below clearance) was refused. Near-center displacements `5e-324`, `1e-250`, `1e-160`, `1e-50`, and `1e-12 m` passed the standalone high-precision witness against **actual native records**. Qualified extreme finite cases produced `-1.9894367886486919e-252` and `-7.957747154594768e+190 C/m²`, while out-of-range charges were refused.

External JSON checking establishes self-consistency with labeled teacher source/geometry, not cryptographic authenticity. The honest scope of **zero new original JEE problems solved** and **no arbitrary irregular 3D local E/V/force/time solver** was retained.

## BLOCKER B1 — admitted nearly-unit normals are evaluated off the sphere

**File locations:** [native normal gate L69–74](https://github.com/physicsvigilante/conductor_sim/blob/f38fb82f27312f9ea1526c1a65bb93657937a0cb/src/conductor_sim/spherical_multicavity.py#L69-L74), [wall-vector evaluation L215–234](https://github.com/physicsvigilante/conductor_sim/blob/f38fb82f27312f9ea1526c1a65bb93657937a0cb/src/conductor_sim/spherical_multicavity.py#L215-L234); [standalone checker L207–215](https://github.com/physicsvigilante/conductor_sim/blob/f38fb82f27312f9ea1526c1a65bb93657937a0cb/tools/m40a_spherical_reference.py#L207-L215).

`_normal()` accepts length error up to `1e-12` but returns the raw input. The density kernel evaluates the distance using `a*n - u`, so a nearly-unit radial vector of length `1+9e-13` evaluates at radius `a*(1+9e-13)` — **off the defined spherical face**. The effect is amplified by the inverse-cube distance close to an *admitted* source-wall gap.

Minimal [independent native reproduction](../reviews/review-01-chat-b-nonunit-repro.py): one grounded conductor, cavity radius `a=0.85 m`, charge `q=3.1e-9 C`, source displacement `d=a*(1-1.2e-8)` (a permitted `1.2e-8` relative wall gap), same radial direction queried twice:

| Accepted normal input | Native sigma (C/m²) |
|---|---:|
| `(1.0,0,0)` | `-4742217.655739457` |
| `(1.0+9e-13,0,0)` | `-4741150.895344369` |

The true Kelvin pole value equals the first native result; relative difference is **0.0002249496907416605 = 0.022495%** with input length deviation only `9e-13`. The independent probe recorded this exact behavior in [source-pinned reviewer run #44540915561](https://github.com/physicsvigilante/review_sandbox/actions/runs/44540915561), even though this diagnostic run itself completed SUCCESS because the test explicitly asserts the presence of the discrepancy.

**Why this blocks PASS:** the public contract allows *nearly*-unit input normals while claiming genuine **surface** sigma. Both accepted inputs encode the same radial orientation, but one produces a materially different value by evaluating the kernel at a point outside the physical surface; the JSON checker also accepts this self-consistent off-surface evaluation. This is a numeric/surface-geometry defect inside the advertised qualified domain, not a demand for arbitrary high precision outside it.

**Minimal requested correction:** after rejecting arbitrary nonunit/Boolean/nonfinite normals, **normalize accepted near-unit normals to a canonical unit direction before all surface calculations and saved samples**; keep the standalone checker physically consistent with the same canonical direction, or explicitly tighten the allowed norm tolerance in a physically justified gap-aware manner. Add targeted native and saved-JSON regression for the *same physical direction* at the admitted near-wall cutoff, with rigorous expected Kelvin pole/oblique references. Do not quietly accept general arbitrary nonunit directions. Make the no-exterior/no-field and unsolved irregular-domain boundaries unchanged.

No other scientific blockers were found in the tested domain. The rest of the physical theorem, geometry and source identity handling passed the independent tests.

## Reviewer-owned first-attempt evidence (history preserved)

1. **[Run 44539424875](https://github.com/physicsvigilante/review_sandbox/actions/runs/44539424875) — failure, review-CI infrastructure only.** HEAD/TREE matched; `git diff base..head` failed because the literal candidate checkout initially used shallow history. Native/math tests were not reached. Logs retained, not reclassified as physics success.
2. **[Run 44539575344](https://github.com/physicsvigilante/review_sandbox/actions/runs/44539575344) — SUCCESS**, first actually executed independent six-cavity native mathematics, integration and hostile checks following `fetch-depth: 0` on the pinned checkout.
3. **[Run 44540169253](https://github.com/physicsvigilante/review_sandbox/actions/runs/44540169253) — SUCCESS**, additional genuine gap-contact and signed near-zero tests; first outcomes preserved.
4. **[Run 44540915561](https://github.com/physicsvigilante/review_sandbox/actions/runs/44540915561) — SUCCESS**, same full suite (30 mathematically compared samples and 35 refusals), plus the independent near-unit-normal precision reproduction above. This run's success does **not** erase the scientifically blocking observation. All jobs stored first-attempt artifacts and source/HEAD/TREE/hash logs.

Reviewer script: [`review-01-chat-b-probes.py`](../reviews/review-01-chat-b-probes.py); accuracy reproducer: [`review-01-chat-b-nonunit-repro.py`](../reviews/review-01-chat-b-nonunit-repro.py); independent CI: [`m40a-pr100-review01-independent.yml`](../../../../.github/workflows/m40a-pr100-review01-independent.yml).

## Gate / next action

**CHANGES REQUESTED.** Correct **B1 only** on the production DRAFT branch; preserve the original candidate and all reviewer evidence. Pin the *new* resulting production Git HEAD/TREE, run the narrow near-unit-normal/native-and-checker regression and relevant existing M40a targeted tests, then obtain **targeted correction review**. Do not repeat the unchanged legacy FEMM/browser matrix solely because this new numerical boundary changed. No merge and no auto-merge; even a future independent PASS still requires separate explicit owner authorization.
