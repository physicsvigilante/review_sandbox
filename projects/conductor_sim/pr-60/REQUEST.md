# conductor_sim PR #60 — M25a R2 independent review request

**Status: awaiting-review. Not a production merge approval.**

| Pin | Immutable value |
|---|---|
| projectId | `conductor_sim` |
| sourceRepo | [physicsvigilante/conductor_sim](https://github.com/physicsvigilante/conductor_sim) |
| sourcePR | [Draft #60](https://github.com/physicsvigilante/conductor_sim/pull/60) |
| baseSha | `d27c504f0a2bb336784a4ce9116f84c992b915db` |
| baseTreeSha | `c34fccca5409c81c28a749b74f904e75f98ad1dd` |
| **headSha to review** | **`31ee492bd6070e8b74bf233c44a86de6301af827`** |
| **sourceTreeSha** | **`557047085fb294379acfc45266272b1ceb6b1de0`** |
| reviewClass | **R2 — evidence/geometry interpretation critical**, not new physics |
| review scope | M25a shared-source geometry, both offline motion viewers, source-projection qualification, preservation/negative cases |
| report destination | **`projects/conductor_sim/pr-60/reviews/review-01-chat-b.md`** (authored by Chat B, never Chat A) |

Read [central protocol](../../../PROTOCOL.md), [risk policy](../../../REVIEW-RISK-POLICY.md), [report template](../../../REVIEW-TEMPLATE.md), and the [source composability contract pinned at head](https://github.com/physicsvigilante/conductor_sim/blob/31ee492bd6070e8b74bf233c44a86de6301af827/docs/composability_contract.md) and [teaching evaluation contract](https://github.com/physicsvigilante/conductor_sim/blob/31ee492bd6070e8b74bf233c44a86de6301af827/docs/evaluation_contract.md). No root `AGENTS.md` was present at source registration; report an actual 404 if still missing instead of inventing guidance.

## Expected source-backed behavior

This is **an observational geometry change only**, not a new electrostatic law, dynamics engine, conductivity/induction simulation or general scene graph. The new `src/conductor_sim/source_geometry.py` builds a bounded typed projection/omission ledger shared by `motion_event_viewer.py` (M24a) and `driven_viewer.py` (M24b). Each source has stable identity, original 3-D coordinates, orientation, charge and radius where applicable, signed motion-plane offset and a declared status.

- **Physical in-plane shapes:** point charges appear only when physically in the qualified plane; rods appear as actual line segments only if both endpoints are in-plane. Off-plane points and rods must be **omitted** from the slice while still contributing their true 3-D fields.
- **Radial bodies:** uniformly charged nonconducting volume spheres and thin shells show a true plane intersection, with derived radius `sqrt(R²-h²)` when valid, not a false sphere of full radius centred in the plane.
- **Axis-only ring/disk:** display a 2-D orthographic projection of the original 3-D rim, including degenerately edge-on cases, physically distinct from rods. This is a geometry-only projection; ring/disc E/V laws remain restricted to their certified axes. Preserve actual circle radius and world axis.
- **Fixed uniform field:** direction arrows only, not invented spatial field lines. Applied M24b schedules remain separately identified; display toggles change painted sources, not the computed trajectory, event times, forces or dissipative work.
- **Shared, bounded renderer:** same source-geometry data and painting used by both motion viewer families; independent retained old static M19b viewer stays unchanged.

Check the preimplementation [M25a charter](https://github.com/physicsvigilante/conductor_sim/blob/31ee492bd6070e8b74bf233c44a86de6301af827/docs/m25a_charter.md), [reserved numerical card](https://github.com/physicsvigilante/conductor_sim/blob/31ee492bd6070e8b74bf233c44a86de6301af827/docs/m25a_reserved_card.md) and [M25a documentation](https://github.com/physicsvigilante/conductor_sim/blob/31ee492bd6070e8b74bf233c44a86de6301af827/docs/m25a.md).

### Pinned implementation and source inputs

Review the **[exact GitHub head source tree](https://github.com/physicsvigilante/conductor_sim/tree/31ee492bd6070e8b74bf233c44a86de6301af827)** and [PR #60 diff](https://github.com/physicsvigilante/conductor_sim/pull/60/files); the delta is 10 files: existing CI workflow and two viewer modules, three M25a docs, new source_geometry module, new test module, and two browser/transfer tools. The implementation is from local patch SHA-256 `53ebb2d377d7c0ec972dfa56942c4d1316eeec690cbe830fd831acd7be04c695`; all original `index` target Git blob hashes were checked against the first published source commit. Final commit only fixes CI invocation mode, leaving production code and numerical tests byte-identical.

## Current-source CI and evidence (checked by Chat A)

**All 16/16 applicable PR workflows completed successfully** for head `31ee492bd6070e8b74bf233c44a86de6301af827`, tree `557047085fb294379acfc45266272b1ceb6b1de0`.

| Gate | Verified source-run evidence |
|---|---|
| Full Python matrix | [run 43723348354](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723348354): **1,700 passed, 97 separate real-FEMM skips, 6 existing warnings** on **each** Python 3.10 and 3.12 |
| Real FEMM 5 | [run 43723348336](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723348336): **97 passed, zero skipped**; conductor nonregression only, NOT source-geometry reference |
| Focused physics and actual Chromium | [run 43723348462](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723348462): **451 passed, zero skipped** focused JUnit, **6/6 new geometry browser cases plus 1/1 reserved first transfer browser** passed |
| Full visualization/source checks | [run 43723348454](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723348454): success |
| New browser/source evidence artifact | [artifact ID 14165651772](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723348462/artifacts/14165651772), ZIP SHA-256 **`6df60dad34955f58c1cc2081cb655c90540f648a7c0d78280c49f50641fa1950`** (downloaded and recomputed; matches GitHub metadata). Includes saved HTML, JSON, PNG, browser results, focused JUnit and `tree.txt` matching the pinned tree. |

**Preserved first failed attempt:** initial frozen source head `4a463374b80a5b7525b3428543911c1fae4ad298` had one failed browser workflow [run 43723072406](https://github.com/physicsvigilante/conductor_sim/actions/runs/43723072406): `ModuleNotFoundError: No module named 'examples'` from directly invoking the verifier script. Only the CI invocation was repaired to `python -m tools.check_m25a_source_geometry` at current head `31ee492b...`; there were no changes to production physics/viewer modules or acceptance tests. This was not a successful first CI run. The reserved R2 script did **not** execute in the failed run.

**First reserved R2 run:** after the corrected candidate was pinned, a previously unexecuted developer-exposed model composed a thin charged axial ring, fixed E, gravity, drag and two applied-field phases. Observed downward detector crossing `0.3049467453360558 s`; separate numerical reference `0.3049467455367558 s`, difference `2.0070e-10 s`. Maximum checked position difference `1.524e-12 m`, velocity `5.241e-12 m/s`, work `9.163e-22 J`. Same source model retained; real Chromium source painting and 390-pixel display passed with zero JS/console/network errors. **This is same-developer, author-exposed, not a blind independently authored Chat B model.** Precision differences are scoped checks, not universal error bounds.

## Reviewer acceptance questions (no predetermined verdict)

1. Independently examine the exact projection maths (world circle rim basis, handedness, degenerate edge-on ring/disc, arbitrary axis orientation, perspective/slice distinction), cross-section radii and numerical stability. For no-intersection/tangency, does the ledger reject or label it accurately?
2. Check a novel off-plane point/rod arrangement: do all omitted sources truly remain omitted visually, while their signed offsets, identities, 3-D geometry and computed force remain intact? Can a world-frame rotation or model revision create false in-slice markers or clipped source evidence?
3. Examine binding validation and viewer JS: can edited/forged source records misrepresent physical objects without check? Is projection logic shared consistently between both viewers and do toggle/on-screen geometry claims actually correspond to the source model? Are negative/refusal contracts enforced before physics and preserved by the new path?
4. Scrutinize the seven actual browser reports and one first-pass reserved transfer. If possible, run or author fresh adversarial tests (separate context; distinguish from artifact inspection); flag missing independent execution as an evidence limit, not a demonstrated physics defect.
5. Verify old motion, source identities, saved schemas, event/drag/energy meanings, global qualification and historical observations remain intact. Verify no invented field-line/potential map, conductor response, off-axis ring/disk field solve, or post-termination motion.
6. Record teacher-facing effectiveness as a separate assessment, not a proxy for correct physics. Distinguish renderer limitations and scope from blockers.

## Known limits and scope

2-D projections and actual cross-sections only, no rotatable 3-D scene; source omission is not removing its electric field. Historic static M19b renderer is intentionally not migrated. No exact conductor contact, induced charge, time-varying magnetic field, off-axis ring/disc field laws, new experimental data or demonstrated blinded LLM teaching capability. Any unsupported geometry or physical law must remain a refusal. Original and failed CI evidence remain accessible.

**Output:** Chat B writes a *new, attributable* `projects/conductor_sim/pr-60/reviews/review-01-chat-b.md` directly on review_sandbox main (or review-only PR), using the central template. Preserve initial independent attempted tests even if they fail. Do **not** merge the source PR. Chat A will fetch the report after the owner says **“Review complete.”**
