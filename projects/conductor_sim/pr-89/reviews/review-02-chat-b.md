# conductor_sim PR #89 — independent corrected-source review #02

**Verdict: CHANGES REQUESTED** (new standalone-export integrity defect F4).  
**Reviewer:** separate-context Chat B scientific/evidence reviewer, 18 November 2026.  
**Scope:** read-only production; executed source-pinned GitHub Actions tests in `review_sandbox`. This is not a GitHub merge approval.

## 1. Exact reviewed identity and preserved prior record

| Fact | Independently checked |
|---|---|
| Production pull request | [physicsvigilante/conductor_sim #89](https://github.com/physicsvigilante/conductor_sim/pull/89), draft/open/unmerged |
| Corrected candidate HEAD | `adfe9098742c663e9f4132c3e29e86dddf7ecc1e` |
| **Actual native Git TREE** | `43f8ebae4937eacc25143fdace324115edcfb2d0` |
| Released M36e base | `dc347251c14e449c53d51820b4481d1bfbee2cfb`, tree `60b4f21aa88a2031ec50c5d1e7c15a5135a7becf` |
| Charter-before-code commit | `89dae06df53403a8fab6743ad8bdcc10fc76c514` |
| Old review #01 source | `75c984aaae18e44997332e330ed3a519a7b6a8da`, tree `e1dbb9bb673f4efc2950939d0c1e021697393d59`, **CHANGES REQUESTED** |
| Independent runner | GitHub Actions Ubuntu / CPython **3.12.16** |
| Reviewer runs | [original R2 first attempt #44314994267](https://github.com/physicsvigilante/review_sandbox/actions/runs/44314994267); [matcher-corrected R2 #44315235077](https://github.com/physicsvigilante/review_sandbox/actions/runs/44315235077) |

Fresh `actions/checkout@v4` retrieved the complete source at exact SHA, `git rev-parse HEAD` and `HEAD^{tree}` verified the stated identity, and a **live** GitHub PR query confirmed the same head, draft state and no merge. The tracked source worktree was clean before/after execution. The eight PR-changed filenames were independently enumerated: workflow, charter, design, example, `__init__`, M37a observer, M37a tests, standalone M37a SI checker. No prior solver/M16a/FEMM/viewer/PDF file is part of PR #89.

The [original R1 negative review](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-chat-b-20261118/projects/conductor_sim/pr-89/reviews/review-01-chat-b.md) and [its red first workflow #44307096311](https://github.com/physicsvigilante/review_sandbox/actions/runs/44307096311) remain unchanged, bound to a **different, older** source. Their 11 unexpectedly accepted F1–F3 inputs are not retroactively passed.

## 2. Actual independent execution: 99 reviewed cases, 3 real failures

A new `challenge_r2.py` adapts and **reexecutes** the prior reviewer-owned independent matrix against the corrected source and adds **26 new tests** (24 adversarial/domain cases and 2 genuine tests). A separately maintained `r2_kelvin_oracle.py` derives charge, current, force and induced mechanical energy from the Kelvin image geometry using stdlib math; the production M37a observer and its standalone checker are **not** used as the arithmetic oracle. All developer and original-review source histories remain untouched.

- **First R2 run:** 99 executed; 95 satisfied expectations, **3 unexpected JSON acceptances**, plus **1 reviewer-harness regex mismatch** for a correctly rejected zero charge. This first failure was retained rather than discarded.
- **Corrected R2 run:** 99 executed; **27 PASS**, **68 intended physical/domain/provenance refusals**, **1 explicitly documented JSON-only ODE proof limitation**, **3 unexpected acceptances**; total **96/99 met expectations**. No harness setup, execution or quantitative failure remained. The original F1–F3 attack suite passed.
- A one-line reviewer-only correction extended the generic zero-charge error matcher to allow the newly explicit `nonzero external point charge` refusal. No production alteration and no weakening of the 3 new hostile demands.
- **Workflow conclusion was FAILURE**, correctly, because unexpected acceptance is not scientific PASS. Both executions used `set -euo pipefail`; piping through `tee` did not erase a test failure. The first-run and corrected-run evidence have distinct immutable run IDs and preserved first-attempt directories.

Evidence: [R2 original results](evidence/r2-run-44314994267-attempt-1/independent-results.json), [R2 corrected results](evidence/r2-run-44315235077-attempt-1/independent-results.json), [reproducing reviewer script](challenge_r2.py), [independent Kelvin oracle](r2_kelvin_oracle.py), [actual workflow](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-r2-20261118/.github/workflows/conductor-pr89-chat-b-02.yml).

## 3. New F4 — P2 evidence-integrity defect: three locally false M16a declarations pass the offline checker

**Affected source:** `tools/m37a_ground_wire_reference.py`, `validate_examples`'s handling of `actual_elapsed_time.motion`. Each mutation below was **independently applied to a genuine CLI-generated, previously accepted JSON document**. Each sole mutation left all genuine instantaneous readings and all sample-level force, current and energy equations unchanged. The checker returned success in all three cases:

| Hostile case | Genuine value / mutation | Actual checker outcome | Why independently checkable |
|---|---|---|---|
| `json/r2-false-max-drift` | Actual maximum `2.4507707188721104e-20 J` → forged `1e9 J` | **Accepted** | Maximum `abs(energy_drift_j)` over saved samples is computable from the checked rows |
| `json/r2-negative-surface-guard` | Genuine `guard_m=1e-7` → forged **`-0.3`** | **Accepted** | An approach cutoff in metres cannot have negative physical clearance |
| `json/r2-false-surface-event-on-duration` | Genuine `termination=duration`, `events=[]`; append a structurally valid `surface-guard` event at an authentic intermediate sample | **Accepted** | Duration-complete history contradicts its claimed surface-guard event; event timing/position are already available |

These are **not** the accepted limitation of an offline JSON checker unable to re-integrate an ODE. Their truth can be evaluated **only from the exported snapshot document**; no native numerical propagation or trusted production import is needed. F4 can cause plausible but false exported safety, accuracy and termination metadata to receive the same successful result as a genuine trace. Unlike the earlier F1–F3 gaps, this failure surfaced only in the novel R2 cases.

Minimal reproductions using the public example (one edit per independent copy):

```python
from copy import deepcopy
from examples.grounded_sphere_wire_current import example_data
from tools.m37a_ground_wire_reference import validate_examples

genuine = example_data()
assert validate_examples(genuine)["actual_time_samples"] == 6

bad1 = deepcopy(genuine)
bad1["actual_elapsed_time"]["motion"]["max_abs_energy_drift_j"] = 1e9
validate_examples(bad1)  # CURRENTLY ACCEPTS contradictory maximum

bad2 = deepcopy(genuine)
bad2["actual_elapsed_time"]["motion"]["guard_m"] = -0.3
validate_examples(bad2)  # CURRENTLY ACCEPTS negative guard

bad3 = deepcopy(genuine)
m = bad3["actual_elapsed_time"]["motion"]
row = m["samples"][2]
m["events"].append({
    "kind": "surface-guard", "time_s": row["time_s"],
    "displacement_m": row["displacement_m"],
    "position_m": row["position_m"],
    "description": "False terminal approach during duration-complete run",
})
validate_examples(bad3)  # CURRENTLY ACCEPTS impossible terminal-event claim
```

**Bounded required correction:** preserve the standalone checker's no-production-import constraint. Validate finite positive `guard_m`, check saved source clearance against that guard with documented tolerance, verify the max-absolute-drift summary against individually checked sample drifts, require well-formed event metadata (recognized kind, ordered and bounded time, authored-axis-consistent position), and forbid any `surface-guard` event when `termination=duration`. For guarded termination, require an authentic *internally consistent* final guard event. Do **not** claim that these checks prove the ODE was integrated. Add all three novel case mutants as dedicated regression tests plus genuine duration/turning/guard acceptance. Re-run a fresh independent execution on the resulting **new** HEAD/TREE.

## 4. Previously blocking F1–F3: corrected on this exact source

**F1 — Boolean dimensional values:** All three original public-observer probes now refuse before backend physics: `PointCharge(True,...)` → `source charge must be a finite real number, not a boolean`; `SolidSphere(True,...)` → corresponding sphere-radius error; `ElectrostaticProblem(...,permittivity=True)` → corresponding permittivity error. New `q=False`, nonfinite inputs, an extreme finite source, and speed-cutoff cases were also refused. Genuine signed float scalars and numeric JSON round-trips remain accepted.

**F2 — falsified units:** Original `current:A→mA`, `energy:J→eV`, `motion.time:s→ms`, and absent instantaneous `units` all refused with precise SI-unit errors. New absent nested motion units, wrong acceleration/force/velocity units, extra keys and a non-dictionary units record also refused. The checker stays import-isolated: AST audit found only `__future__`, `argparse`, `json`, `math`, `pathlib`, no production package.

**F3 — identity/provenance:** Original third-sample conductor rename, false `FEMM time-dependent electron drift` method, `prescribed animation` nested mode and electron-flux conventional-current label all refused as intended. New sample centre/radius/permittivity alterations reached actual independent SI mismatch assertions (distance, induced charge, induced energy) rather than mere schema/setup exceptions. Additional false third-sample units, source sign, missing conductor name and claimed full-wave physical regime were correctly rejected.

The F1–F3 corrections are real. They do not remedy the independently discovered F4.

## 5. Physical laws and genuine native M16a evidence

Let `d = |x−c|>a`, `n=(x−c)/d`, `v_r=v·n`, `k=1/(4πε)`. From the grounded Kelvin image `q_i=−qa/d`, image offset `a²/d`, source-minus-image distance `d−a²/d`, the independent oracle finds:

```text
Q_sphere             = -q*a/d
I_sphere_to_ground   = -q*a*v_r/d² = -dQ_sphere/dt
I_ground_to_sphere   = +q*a*v_r/d²
F_radial_on_source   = -k*q²*a*d/(d²-a²)²
U_induced_mechanical = -k*q²*a/[2*(d²-a²)]
```

The energy **half-factor** is mandatory and not wire heating; mechanical force is attractive for either sign of source charge, whereas terminal-current sign reverses. Inward `q>0` gives positive conventional sphere→ground current; tangential velocity gives zero **net** terminal current, not static local surface-charge density. Numerical centred differences on the actual native Kelvin **conductor net charge**, not a copied M37a current expression, matched analytic `-dQ/dt` for 19 independently sampled signed, translated, 3D oblique, near-surface and permittivity-scaled worlds. For one new source-authored test, oracle current `−1.0587088411811485e−10 A` and native finite-difference current `−1.0587088411667589e−10 A` agreed.

Four **genuinely integrated** Motion1DSpec/M16a histories were generated and independently checked (not made-up time sliders):

| Motion | Actual states | Final elapsed time | Outcome | Native-Q temporal central differences |
|---|---:|---:|---|---:|
| Translated oblique inward | 17 | 0.08 s | Duration | 15 |
| Negative source, outward | 13 | 0.12 s | Duration | 11 |
| Negative source, inward guard | 10 | 0.08524769628379199 s | Surface-guard event | N/A at irregular terminal interval |
| Outward/turning/inward | 71 | 0.35 s | Duration and turning event | 69 |

Total: **111 actual saved states, 95 temporal native-charge central differences** in uniformly sampled interior intervals. Every saved position, elapsed time, signed current, native-conductor charge, force, acceleration and kinetic/interaction/total-energy ledger was checked. Typed motion with a forged monotonic timestamp preserving individually genuine physical snapshots was correctly refused after **fresh native M16a reintegration** (`saved elapsed-time motion differs from independently rerun M16a integration`). Fake native events, changed force/energy, velocity and source also refused.

A distinct **documented limitation** was retained, not misreported as a failure: matching monotonic JSON timestamp edits, with all individual snapshots still true, are accepted by the separate JSON-only SI checker because it explicitly **does not run the ODE**. It checks exported consistency, not historical/cryptographic provenance.

## 6. Exact-head CI and original JEE-source fidelity

At the second source-pinned reviewer execution, the live production workflow inventory contained **all 25 exact-source runs completed SUCCESS**: 23 PR and 2 branch-push runs, including dedicated Python 3.10/3.12 M37a tests, ordinary Python checks, real FEMM 5, historical real Chromium/browser checks and M36 JEE/source replays. The independent review itself ran CPython 3.12 only; the developer's dual-version success is not substituted for independent execution. See [captured live complete CI inventory](evidence/r2-run-44315235077-attempt-1/ci-live-summary.txt). **All-green developer CI and FAILED independent reviewer workflow are simultaneously true.**

The reviewer checkout rehashed the **original** `02_conductors_half_size.pdf` (20,685,051 bytes; 17 pages; Git blob `90d8869b0f01cc2ea13f83721985a5d8419f1d0e`, SHA-256 `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d`) and produced new page-8 and page-17 rasters. **Inspection limitation:** this R2 session did not itself visually open the raster pixels. Source interpretation is therefore **explicitly attributed** to R1's preserved independent visual inspection at the identical verified PDF bytes. R1 reports physical p8 Multiple Correct Q21 with a **positive charge approaching the grounded sphere at externally prescribed constant small speed** and p17 answer key **(1),(3)**. No original-source teacher numerical q, a, d, velocity or mass can be inferred. The problem is **not** a freely accelerating Newtonian M16a charge; the M37a supplied-velocity observer matches its local physical interpretation, but M37a still does not deliver an independently graded complete textbook answer or current-versus-time browser overlay.

## 7. Decision and release boundary

**CHANGES REQUESTED** for F4 (P2) while recognizing that F1, F2, F3 and the genuine native Kelvin/M16a physics now pass. The targeted standalone JSON consistency correction is small and should preserve schema and mathematical evidence; no generalized Maxwell solver, FEMM transient model or architectural rewrite is warranted.

Keep `conductor_sim` PR #89 **draft, unmerged and without merge approval**. After an author correction, pin a **new HEAD and native tree**, rerun all required exact-head production CI **and new independent F4 adversarial proof**, then request a separate owner decision. Never overwrite the historical review #01, old red run, or either R2 red attempt. Even a future independent PASS does not itself authorize merge; owner authorization, expected-head guard, exact postmerge main tree and all genuine main-push workflows remain separate gates.
