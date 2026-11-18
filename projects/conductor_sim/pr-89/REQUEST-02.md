# M37a PR #89 — Independent re-review REQUEST #02 (review #01 F1–F3 corrections)

**Fresh separate-context reviewer, not the production author.** Read the entire report and original reviewer reproduction before testing. Preserve the historical review result, which remains **CHANGES REQUESTED** on the earlier, different source. No merge authority is granted.

- **Production PR:** https://github.com/physicsvigilante/conductor_sim/pull/89
- **EXACT corrected source HEAD:** `adfe9098742c663e9f4132c3e29e86dddf7ecc1e`
- **Actual Git TREE:** `43f8ebae4937eacc25143fdace324115edcfb2d0`
- **Released base:** M36e main merge `dc347251c14e449c53d51820b4481d1bfbee2cfb`, native tree `60b4f21aa88a2031ec50c5d1e7c15a5135a7becf`, all 20/20 main-push workflows successful.
- **Frozen original charter:** `docs/m37a_charter.md` committed `89dae06df53403a8fab6743ad8bdcc10fc76c514` before implementation.
- **Old source:** `75c984aaae18e44997332e330ed3a519a7b6a8da`, TREE `e1dbb9bb673f4efc2950939d0c1e021697393d59`. **NOT the review target.**
- **Original independent review #01 (CHANGES REQUESTED):** https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-chat-b-20261118/projects/conductor_sim/pr-89/reviews/review-01-chat-b.md
- **Review_sandbox PR #6 (preserved negative evidence + original challenge scripts):** https://github.com/physicsvigilante/review_sandbox/pull/6
- **Original reviewer first source-pinned red workflow:** https://github.com/physicsvigilante/review_sandbox/actions/runs/44307096311 ; 73 executed cases, 25 genuine positives, 36 intended hostile refusals, one documented static-JSON proof ceiling, **11 unexpectedly accepted for F1–F3**; never reclassify the old run as green.

**At publication the current full exact-head 25-workflow CI had not all finished**; check LIVE and require all required PR/push workflows successful including real FEMM5, Python 3.10/3.12 and historical real Chromium. Focused M37a source workflow on the corrected head passed **118 tests each in Python 3.10 and 3.12** plus example generation and independent no-production-import SI JSON validation. That is developer-controlled proof, NOT independent PASS.

## Specific corrections on current candidate

Only the new source-level observer, its separate stdlib SI checker and tests changed since the first review; no original solver/M16 integration/FEMM/generic viewer/PDF edits. Inspect actual PR diff, not this assertion.

1. **F1 — Boolean dimensional model values:** M37a observer now calls strict finite non-Boolean `_number` on authored `q`, sphere radius `a`, and model permittivity *before* the static Kelvin backend; continues to require one nonzero exterior source + one grounded solid sphere. The historical immutable model constructors are deliberately unchanged. Retest original Boolean `q=True`, `a=True`, `epsilon=True`, plus unfamiliar Boolean/NaN/overlarge input without weakening nonzero, positivity or 0.1c refusal. Genuine float/int physical values should work; exported physical fields must be numeric, not JSON booleans.
2. **F2 — SI unit metadata integrity:** production-independent `tools/m37a_ground_wire_reference.py` now requires the **complete exact** `units` dictionary for instantaneous `charge=C, length=m, velocity=m/s, current=A, force=N, energy=J` and nested M16a `time=s, displacement=m, velocity=m/s, acceleration=m/s^2, force=N, energy=J`. Replay all four original unit attacks: current `mA`, energy `eV`, time `ms`, and missing instantaneous map. Also attack missing motion map, extra/renamed keys and contradictory acceleration/force labels. None should pass merely because SI numbers remain unchanged.
3. **F3 — Contradictory physical trace claims:** checker enforces the exact outer conventional charge-flow sign label, its honest ideal-quasistatic regime, nested M16a `mode=elapsed-time classical dynamics` and exact `method=Adaptive RK4 step doubling; existing analytical force_energy at each RHS evaluation`. Across samples, require same physical conductor **name, 3D centre, radius, and permittivity** (signed source charge is already bound to M16a input and each recorded state rechecked by independent SI). Replay original four attacks: third sample sphere name changes, forged FEMM method, fake prescribed-animation mode, false electron-flow trace sign. Try an unfamiliar centre/radius/permittivity mutation while preserving apparent point-source field data. Require specific provenance/type or physics rejection, not a file import error.

**Reviewer authenticity:** use author-controlled fresh checkout of the exact corrected HEAD + verified native tree; author and execute an independent harness against corrected code. You may examine the original [review #01 script](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-chat-b-20261118/projects/conductor_sim/pr-89/reviews/challenge_chat_b.py), but do not overwrite its first-attempt artifact. Re-run the original 11 failings and generate additional novel attacks. A clean genuine source still must be accepted. No green assertion unless a real execution succeeded with `set -euo pipefail`; if tests are run under `tee`, exit status must propagate. Preserve first attempts, including any corrected reviewer harness failure, and do not mistake a successful evidence collection workflow for a physics PASS.

## Independent physics and JEE source fidelity must remain intact

Independently re-derive and check from actual new source:
```
n = (x - c)/d; d>a; vr = v dot n; k=1/(4*pi*epsilon)
Q_sphere = -q*a/d
I_sphere_to_ground = -dQ_sphere/dt = -q*a*vr/d**2
I_ground_to_sphere = +q*a*vr/d**2
F_source_radial = -k*q*q*a*d/(d*d-a*a)**2
U_mechanical_induced = -k*q*q*a/[2*(d*d-a*a)]
```
The half in `U` is important. Test actual **native Kelvin conductor-charge finite differences** under source movement, signed currents under ±q and incoming/outgoing/tangential velocities, translated/nonaxial 3D centre and changed eps, actual M16a inward/outward/turning/guarded trajectories, false monotonic timestamps that preserve local physical snapshots, fake event/velocity/force/source-energy. For the already documented static JSON proof ceiling, do not require an *offline JSON-only scalar checker* to rerun an ODE: the public typed observer already recomputes the exact M16a numerical history; the offline checker must be honest about its lesser claim.

The first independent reviewer visually inspected **physical p8, workbook Multiple Correct Q21** and physical p17 answer key of `02_conductors_half_size.pdf` (original PDF SHA256 `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d`). Real printed source says `q>0` approaches grounded sphere radius R at **externally prescribed constant small speed v**, not freely accelerating M16a; options **(1) and (3)**. For `vr=-v`, `I_sphere_to_ground=+q R v/d²` increases as d decreases. Re-read source figure/answer or attribute prior reviewer provenance precisely; original numeric `q,a,d,v,m` are **not specified** by textbook. No automatic whole-question/JEE score, nor new current graph, is established by M37a.

## Publication and release gate

Publish a NEW attributed report at `physicsvigilante/review_sandbox/projects/conductor_sim/pr-89/reviews/review-02-chat-b.md`, directly on main or a new review PR, with verdict **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** for the exact new HEAD/TREE. Include actual original and novel attacks, independent SI evidence, false sign/unit/identity rejection reasons, genuine M16a history, full exact-head CI, source education limits, first reviewer execution logs. Do not overwrite review #01 or its failure evidence.

**KEEP PRODUCTION PR #89 DRAFT AND UNMERGED. DO NOT EDIT IT, MARK READY OR MERGE.** Even a true fresh review PASS cannot authorize a merge. Chat A must separately obtain explicit owner approval, then use reviewed `expected_head_sha`, verify the main Git tree equals the independently reviewed tree, and require actual postmerge main-push CI.
