# M37a / conductor_sim PR #89 — Independent scientific R2 request #01

## Target, provenance, and hard stop

- **Production draft PR:** https://github.com/physicsvigilante/conductor_sim/pull/89
- **Exact candidate HEAD:** `75c984aaae18e44997332e330ed3a519a7b6a8da`
- **Native Git TREE:** `e1dbb9bb673f4efc2950939d0c1e021697393d59`
- **Released reviewed base:** M36e main merge `dc347251c14e449c53d51820b4481d1bfbee2cfb`; Git TREE `60b4f21aa88a2031ec50c5d1e7c15a5135a7becf`; 20/20 actual postmerge main CI SUCCESS.
- **Frozen preregistration:** `docs/m37a_charter.md`, standalone pre-implementation commit `89dae06df53403a8fab6743ad8bdcc10fc76c514`.
- **At packet creation exact-head CI was still QUEUED, NOT PASS.** Reviewer must query actual exact HEAD workflows after they finish. Prior red runs are preserved.
- This request is for a **new independent separate-context reviewer**. Review must be read-only against production. Do not merge PR #89, mark ready, or edit production. Review PASS never grants merge authority; independent owner authorization is needed later.

STOP as STALE if production PR head or real native tree changes. Do not carry a verdict across a new SHA. The objective is one **new ideal quasistatic grounding-wire current observable**, not a new electrostatic solver, FEMM AC transient, particle collision, or verified completion of a new original JEE problem.

## Scientific target and exact intended meanings

The existing `ExternalGroundedSphereBackend` solves a single nonzero point charge `q` external to **one grounded solid conducting sphere** radius `a`, fixed centre `c`, exterior distance `d>a`, uniform `eps>0`. Existing `force_energy` supplies the self-field-free force and induced mechanical energy, and `integrate_motion_1d` supplies physically integrated radial classical trajectories.

New M37a exports two distinct modes using the exact same public core:
1. `observe_grounded_sphere_wire(problem, velocity)`: teacher-imposed **instantaneous kinematics only**; source position and 3D velocity are genuine inputs, not an inferred trajectory. Handles radial and tangential source velocity.
2. `observe_grounded_sphere_motion(actual_M16a_result)`: genuinely elapsed-time radial M16a result. Recompute every snapshot's Kelvin physics **and rerun the existing M16a integration** from original immutable initial conditions; fail on forged monotonic time stamps that were formerly indistinguishable from true simulation.

Analytical, independent standard SI reference:

```text
unit n = (x - c)/d; vr = velocity dot n; k = 1/(4*pi*eps)
Q_sphere(d) = -q*a/d
dQ_sphere/dt = +q*a*vr/d**2
I_sphere_to_ground = -dQ_sphere/dt = -q*a*vr/d**2
I_ground_to_sphere = +dQ_sphere/dt
F_radial_on_source = -k*q*q*a*d / (d*d-a*a)**2
U_mechanical_induced = -k*q*q*a / (2*(d*d-a*a))
```

The sign is **conventional positive-charge flux**, not electron drift direction. A positive external charge moving inwards has `vr<0`, `dQ_sphere/dt<0`, **positive** `I_sphere_to_ground`; with negative q the sign reverses. If `vr=0`, there is no **net ground-wire** current at that instant, even though tangential motion may redistribute local surface charge. Do not confuse `dU/dt`, field energy, electrical Joule heating, surface-current density, induced net charge and physical wire-terminal current. Grounding is modelled ideally and instantaneously; **not Maxwell/FEMM time evolution**.

## Required source provenance

Independent reviewer must actually read or rasterize the original `02_conductors_half_size.pdf` physical **page 8**, **Multiple Correct Q21**, and its figure and answer/options if present. M36a's provisional coverage matrix labels this original source case `p08-multiple-21` as PARTIAL. Record *what the printed source really gives and asks*, which parts are/are not answered by a static image-charge model, by an assumed speed, and by a genuine Newtonian orbit. Teacher examples `q=+1 nC`, `a=.1 m`, `d=.2 m`, radial speed and mass are **not authenticated as printed original givens**. If source requires an externally controlled trajectory or a current in a different grounded circuit, do NOT claim it solved.

No new original JEE question count is awarded by default. The parser is not autonomous and the viewer has not yet acquired a ground-wire current plot.

## Actual tests, not claimed tests

The developer-controlled initial source CI first ran 109 tests pass/4 fail due near-cancelling energy-drift arithmetic; next candidate 112 pass/1 fail in its independent standard-library checker. These red runs are retained in Actions, *not relabeled successes*. Corrections retained the independent SI U check, and evaluate drift using numerically verified M16a energy records to avoid false errors at the `~1e-22 J` scale. The latest exact HEAD additionally checks strict event geometry, source mode semantics and genuine recomputation of the time history. **NONE is independent PASS.** Query final CI live; both Python 3.10/3.12, real FEMM5 regressions and original historical Chromium still matter for compatibility, despite M37a producing JSON only.

Reviewer MUST:
- Pin `git rev-parse HEAD` and `HEAD^{tree}` to exact strings. Check PR is draft, unmerged, check changed files are only M37a docs/tests/example/reference/workflow/new observation + public export, and legacy production solver/M16/FEMM/generic renderer/PDF bytes unchanged.
- Execute source checkout with Python 3.10 or 3.12, **author a genuinely new separate independent Python/stdlib SI oracle**, derive force+induced-energy half factor and Gauss Q; do not treat developer module as oracle. Test both source-signed q (positive/negative), incoming/outgoing 3D velocity, tangential net zero, moved centre, arbitrary 3D direction, altered permittivity, near-surface but strictly exterior cases, source-q reversal symmetry.
- Recompute `-dQ/dt` through a numerical central difference of **native Kelvin equilibrium Q** for both chosen velocities and real M16a output snapshots; confirm sign and physical units independent of direct current formula. Verify force is from native self-free Kelvin model (not q times total field including singular source self-field) and U carries exact **1/2 induced**.
- Generate genuine **actual time-integrated** source state with public `Motion1DSpec` + `integrate_motion_1d`, compare position/velocity/force/energy drift and `Q(t),I(t)` to reviewer arithmetic; test turning or outward branch if feasible and separate true guarded inward approach. Confirm real terminal guard and no fake impact/contact or continuation.
- Devise unfamiliar hostility attacks on actual production observer and on emitted genuine JSON. At least 12, covering: wrong sign of current, swapped direction, forged net charge despite matching displayed current, q negative with wrong sign, spoofed Boolean SI charge/time/velocity, fake 3D centre/charge position and units, forged but *strictly increasing* M16a intermediate timestamp with all local physical snapshots otherwise intact, method spoofing, made-up turning/surface event, false energy half factor/force, altered permittivity, wrong grounded vs isolated/shell/extra sources. Refusal must be the **intended physical assertion**, not unrelated exception/missing file. Keep genuine acceptance positive.
- Test that standalone `tools/m37a_ground_wire_reference.py` has **zero production physics imports**, re-check its complete output on authentic saved JSON, plus reviewer-crafted signed/energy/timeline tampering. Distinguish what independent SI static sample checking proves from what separate native M16a re-integration guarantees. A fake export cannot be authenticated cryptographically solely from a JSON file.
- Independently inspect source PDF p8 and text as above. Since M37a has **no new visualization**, do not demand a new Chromium M37a current trace; instead inspect inherited actual Chromium CI for non-regression and identify synchronized current-plot viewer as future separate milestone.
- Run full exact-head GitHub CI and obtain actual terminal SUCCESS (not queued/in-progress). If a job fails/cancels/timeout, diagnose, retain logs and report CHANGES/INSUFFICIENT; no PASS on stale green older SHAs.
- Use a self-authored source-pinned checkout/run in `physicsvigilante/review_sandbox` if necessary; `set -euo pipefail`; do not hide failures behind `tee` or missing-path errors. Preserve exact first-attempt scripts, machine-readable output, tests, source-tree SHA, PDF page raster/screenshot if used, and first workflow run. Do not claim artifact independent rehash unless you downloaded and hashed it.

## Deliverable and verdict

Publish your attributed independent report in `physicsvigilante/review_sandbox/projects/conductor_sim/pr-89/reviews/review-01-chat-b.md` (main or a dedicated review PR). Include exact source HEAD/TREE, verdict **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, actual own executed source-pinned evidence, distinct physical sign/energy laws, source figure findings, honest unresolved limits, full CI status and URLs. Preserved failed developer runs remain failed historical records.

**No production changes, no merging**, no declaration of solved p8 question until the actual source and requested output is independently proven. A PASS can only trigger a *separate owner approval decision*. Chat A then must use reviewed `expected_head_sha`, matching Git tree, and actual postmerge-main-push CI, or keep PR draft.
