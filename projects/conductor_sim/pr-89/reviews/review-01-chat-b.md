# PR #89 / M37a — independent Chat B review 01

**Verdict: CHANGES REQUESTED.**

**Reviewer:** Chat B, ChatGPT, separate from the production author. **Date:** 18 November 2026. This is an executed scientific/code review, not owner approval or a GitHub approval review on production.

The signed Kelvin current, self-field-free force, induced mechanical energy and native M16a timeline checks passed the independent tests below. Three validation defects nevertheless require correction: Boolean physical scalar inputs, unchecked SI unit declarations, and contradictory trace metadata/identity. Eleven original hostile cases were unexpectedly accepted. The first independent run remains red. All **25 enumerated current-head production workflow runs subsequently reached SUCCESS**; that does not invalidate the new findings.

## 1. Identity, scope and execution provenance

| Item | Verified value |
|---|---|
| Production repository / PR | `physicsvigilante/conductor_sim` / [#89](https://github.com/physicsvigilante/conductor_sim/pull/89) |
| Candidate HEAD | `75c984aaae18e44997332e330ed3a519a7b6a8da` |
| Native candidate TREE | `e1dbb9bb673f4efc2950939d0c1e021697393d59` |
| Released base | `dc347251c14e449c53d51820b4481d1bfbee2cfb` |
| Native base TREE | `60b4f21aa88a2031ec50c5d1e7c15a5135a7becf` |
| Frozen charter commit | `89dae06df53403a8fab6743ad8bdcc10fc76c514` |
| Production status at recheck | Open, draft, unmerged; same HEAD and base |
| Independent test runtime | CPython 3.12.16, Ubuntu GitHub Actions |
| Reviewer script revision executed | `dc5339df9c1b1e4b88ca518f5c7d0bed739cda5b` in review_sandbox |

A fresh full-history production checkout executed native `git rev-parse HEAD`, `HEAD^{tree}`, and the base tree check. The audit also confirmed the charter is an ancestor, its standalone commit changes only `docs/m37a_charter.md`, and its text is unchanged at the candidate. The complete eight-file diff was checked, not inferred from the PR description:

```text
.github/workflows/m37a-grounded-sphere-wire.yml
docs/m37a.md
docs/m37a_charter.md
examples/grounded_sphere_wire_current.py
src/conductor_sim/__init__.py
src/conductor_sim/grounded_sphere_wire.py
tests/test_m37a_grounded_wire_current.py
tools/m37a_ground_wire_reference.py
```

Thus the legacy solver, M16a implementation, FEMM implementation, viewers and original PDF have no changes in this diff. All eight changed files and the relevant native Kelvin/model/motion dependencies were read. Production remained read-only; no production file, branch, comment, review, ready state or merge was changed. The execution checkout's tracked working tree remained clean.

Primary evidence: [native first identity](evidence/run-44307096311-attempt-1/identity-identity.json), [second native/live identity](evidence/supplement-44307692757-attempt-1/identity-evidence.json), [worktree status](evidence/run-44307096311-attempt-1/production-worktree-status.txt).

Local GitHub network access was unavailable. I therefore authored and executed a dedicated source-pinned sandbox workflow, as permitted by the request. This is not a claim of local Python 3.12 execution. No developer test summary was substituted for the independent oracle.

## 2. Required corrections

### F1 — P2: the public instantaneous observer accepts Boolean physical scalars

**Location:** [observe_grounded_sphere_wire][observer], especially its input validation and observation construction. The pre-existing model constructors permit these values; M37a does not close that gap at its new public boundary.

The independent cases `domain/boolean-source-charge`, `domain/boolean-permittivity`, and `domain/boolean-radius` all returned observations instead of a domain/type refusal. For example:

```python
from conductor_sim import (
    ElectrostaticProblem, PointCharge, SolidSphere, Grounded,
    observe_grounded_sphere_wire,
)
p = ElectrostaticProblem(
    (PointCharge(True, (0., 0., .247)),),
    (SolidSphere(.083, Grounded(), name="Reviewer sphere R"),),
)
record = observe_grounded_sphere_wire(p, (0., 0., -.06)).as_dict()
# record["point_charge_c"] is True, not a valid authored SI scalar.
```

**Actual:** `True` is numerically treated as 1 coulomb. The recorded observation contains `point_charge_c: true`, induced charge `-0.3360323886639676 C`, and sphere-to-ground current `0.08162730089003262 A`. Analogous calls accept `permittivity_f_per_m=True` and `radius_m=True` (using exterior distance 2 m for the latter). Boolean supplied velocity, by contrast, is correctly rejected.

**Expected:** refuse Boolean q, radius and permittivity before solving. An LLM-authored Boolean must not silently become a dimensional physical value. The producer also emits a Boolean that the accompanying JSON checker's strict scalar validator rejects; the public API and export contract are inconsistent.

**Correction:** apply the existing strict finite, non-Boolean real-scalar policy to all consumed physical scalar inputs before arithmetic/backend invocation; retain positivity/nonzero conditions. Add genuine acceptance plus Boolean refusal tests and an observer-export-to-checker round-trip test. A broad rewrite of the already qualified solver is not needed.

**Evidence:** all three full returned observations are retained under their case names in [independent-results.json](evidence/run-44307096311-attempt-1/independent-results.json). The actual JSON Boolean-charge attack is separately refused with `source charge: expected finite SI number, not Boolean`.

### F2 — P2: the independent SI checker accepts false or missing unit declarations

**Location:** [check_instant and validate_examples][checker]. Neither validates the exported unit maps.

Starting from a genuine example, each of the following separate edits passed unchanged numerical checking:

| Independent case | Sole edit | Actual result |
|---|---|---|
| `json/units-current` | Instantaneous `units.current`: `A` to `mA` | Accepted |
| `json/units-energy` | Instantaneous `units.energy`: `J` to `eV` | Accepted |
| `json/units-time` | Native motion `units.time`: `s` to `ms` | Accepted |
| `json/missing-units` | Delete instantaneous `units` | Accepted |

Each returned `{"prescribed_states": 3, "actual_time_samples": 6, "motion_termination": "duration"}`. No quantities were converted. The genuine maps explicitly promise SI units; these edits change or remove that promise while the checker reports success.

Minimal reproduction:

```python
from copy import deepcopy
from examples.grounded_sphere_wire_current import example_data
from tools.m37a_ground_wire_reference import validate_examples
bad = deepcopy(example_data())
bad["instantaneous_prescribed"][0]["units"]["current"] = "mA"
validate_examples(bad)  # Currently succeeds; numerical values still encode amperes.
```

**Impact:** an export labelled milliamperes or milliseconds can receive the same SI-validation result as its genuine amperes/seconds source. This is an explicit scientific-export validation gap, not a demand for general unit conversion support.

**Correction:** require the schema's complete documented SI unit declarations for instantaneous records and native motion. Reject absent, malformed or contradictory units. If alternative units are ever introduced, version the schema and convert explicitly rather than ignoring labels. Keep the independent checker free of production-physics imports.

**Evidence:** [current mutant](evidence/run-44307096311-attempt-1/attack-json-units-current.json), [energy mutant](evidence/run-44307096311-attempt-1/attack-json-units-energy.json), [time mutant](evidence/run-44307096311-attempt-1/attack-json-units-time.json), [missing map](evidence/run-44307096311-attempt-1/attack-json-missing-units.json), and the corresponding first-attempt results.

### F3 — P2: the checker accepts contradictory trace attribution and changing conductor identity

**Location:** [validate_examples][checker], when validating the outer trace, nested motion and per-time observations.

These four independent, otherwise-genuine exports also passed:

| Independent case | Mutation accepted |
|---|---|
| `json/sphere-identity-midtrace` | Rename just the third observation's sphere to `Different physical conductor` |
| `json/motion-method` | Set nested motion method to `FEMM time-dependent electron drift` |
| `json/motion-mode` | Set nested motion mode to `prescribed animation, not dynamics` |
| `json/trace-current-sign-label` | Set trace sign declaration to `sphere_to_ground positive for electron flux` |

**Impact:** the checker accepts a purported single fixed-conductor M16a trace with contradictory origin/direction metadata or a different conductor identity in mid-trace. It correctly checks the instantaneous sign string and some outer schema/mode strings, making these unchecked nested contradictions especially misleading. The native Python motion observer correctly rejects a forged method; the gap described here is in the standalone exported-document checker.

**Correction:** validate compatible trace and nested motion mode/method declarations, the conventional-current direction declaration, and fixed conductor identity across a single trace. Bind the conductor name and fixed geometry/permittivity consistently across observations. Reject contradictions even when all instantaneous numerical quantities remain valid. This needs schema consistency, not cryptographic attestation or an independent ODE integrator in the JSON tool.

**Evidence:** [identity mutant](evidence/run-44307096311-attempt-1/attack-json-sphere-identity-midtrace.json), [method mutant](evidence/run-44307096311-attempt-1/attack-json-motion-method.json), [mode mutant](evidence/run-44307096311-attempt-1/attack-json-motion-mode.json), [sign-label mutant](evidence/run-44307096311-attempt-1/attack-json-trace-current-sign-label.json).

**Do not repair these findings by weakening the independent challenges, broadening the claimed physical domain, or describing all metadata as unverified while continuing to issue the same unqualified validation summary.** Keep the numerical checks and the documented distinction between consistency and provenance.

## 3. Independent physical derivation and positive evidence

The separately authored [stdlib Kelvin oracle](kelvin_oracle_chat_b.py) uses the image source construction, rather than calling M37a or its reference checker. It imports only `math`.

For source displacement `x-c`, define `d=|x-c|`, `n=(x-c)/d`, `vr=v dot n`, and `k=1/(4*pi*eps)`. The image charge and its offset from the sphere centre are `q_image=-q*a/d` and `b=a*a/d`. Gauss' law gives the physical conductor net charge `Q=q_image`. The physical source excludes its self-field, so its induced radial force is `k*q*q_image/(d-b)^2`. The reaction potential at the source is `k*q_image/(d-b)`; charging up the linear induced response gives the mechanical energy `q*phi_reaction/2`, not `q*phi_reaction`.

Consequently:

```text
Q_sphere = -q*a/d
dQ_sphere/dt = q*a*vr/d^2
I_sphere_to_ground = -q*a*vr/d^2
I_ground_to_sphere = +q*a*vr/d^2
F_radial = -k*q^2*a*d/(d^2-a^2)^2
U_induced = -k*q^2*a/[2*(d^2-a^2)]
```

The source force is attractive for either charge sign. Q and I reverse with q, while force and U do not. Positive q moving inward has positive conventional sphere-to-ground current; electrons move oppositely. Pure tangential velocity yields zero net terminal current, not a claim that local surface charge stops redistributing. `dU/dt` is not this terminal current, and U is not wire Joule heat.

I also checked the independent energy gradient against the force, the half-factor relation to reaction potential, and central differences of **native solved conductor charge** at physically shifted source positions. This last comparison does not merely differentiate a copied M37a current formula.

For one actual reviewer-authored SI case, `q=+2.4e-9 C`, `a=.083 m`, `d=.247 m`, `vr=-.073 m/s`, and `eps=8.8541878128e-12 F/m`, the reference gives:

```text
Q_sphere = -8.064777327935223e-10 C
I_sphere_to_ground = +2.3835171859889524e-10 A
native-equilibrium finite-difference current = +2.383517185918369e-10 A
F_radial = -3.623459064471587e-7 N
U_induced = -3.969668108688305e-8 J
```

These are reviewer numerical choices, not printed workbook givens.

### Executed matrix

[First attempt 44307096311](https://github.com/physicsvigilante/review_sandbox/actions/runs/44307096311), with unmodified scripts and `set -euo pipefail`, recorded **73 cases**:

| Outcome | Count |
|---|---:|
| Positive physics/motion/genuine export/import-isolation checks passed | 25 |
| Hostile or unsupported cases refused for the intended reason | 36 |
| Documented standalone-checker limitation observed as expected | 1 |
| Unexpected acceptances requiring F1–F3 | 11 |
| Setup/execution errors or quantitative assertion failures | 0 |

Thus 62 cases met their recorded expectations, including the one explicitly documented limitation; this is **not** a 73/73 pass. The workflow's failure conclusion is intentional and retained.

The 18 standalone physical worlds combine positive/negative q, inward/outward/tangential velocities, axial and oblique 3D geometry, a translated centre, changed permittivity, and a strictly exterior near-surface case. The oblique unit direction is `(2,3,6)/7`; a transverse direction is `(-3,2,0)/sqrt(13)`. Near-surface distance is `.083*(1+2e-4) m`. These numerical parameters differ from the developer's teacher examples.

### Real M16a histories

All four histories were actually generated with public `Motion1DSpec` and `integrate_motion_1d`, then accepted by the native M37a observer. Every saved source state was checked against reviewer arithmetic and native resampled equilibria.

| Trajectory | Saved samples | Final time (s) | Termination / event | Actual-time native-Q central differences |
|---|---:|---:|---|---:|
| Translated oblique inward | 17 | .08 | Duration | 15 |
| Negative-q outward | 13 | .12 | Duration | 11 |
| Negative-q guarded approach | 10 | .08524769628379199 | Surface guard, before requested .3 s | 0 |
| Outward, turning, then inward | 71 | .35 | Duration with turning point | 69 |

There are **111 saved motion states and 95 actual-time central-difference checks**. The guard trajectory was not counted as having uniform-time central differences across its irregular terminal interval; its states still received the separate native-position derivative and independent physical checks. The real guard remained exterior and produced no invented impact or continuation.

Checked quantities include exact authored initial state, axis/displacement-derived position, ordered actual time, signed source charge, sphere identity, vector velocity, induced Q, both terminal currents, force, acceleration, K, induced U, total energy and drift. Independent U comparisons use the physical energy scale; drift is additionally recomputed from individually validated stored energies in the same summation order. This avoids fabricating a physics failure by comparing independently rounded, nearly cancelling energies at the much smaller drift scale.

Recorded maximum absolute drifts are respectively `1.5948042210022374e-21`, `2.6297726034285856e-20`, `4.5853143032731705e-11`, and `8.176163367203833e-23 J`. These values are observations, not a universal accuracy certification beyond these inputs.

The complete trajectories, observations and per-case details are in [first-attempt evidence](evidence/run-44307096311-attempt-1/).

## 4. Adversarial timeline results and checker independence

The first attempt executed 48 hostile/domain cases in addition to the 25 positive checks. Important intended refusals include:

| Attack | Actual refusal |
|---|---|
| Change an intermediate time by .0013 s while preserving monotonic ordering and every physical snapshot | `saved elapsed-time motion differs from independently rerun M16a integration` |
| Flip an intermediate velocity sign while retaining its unchanged kinetic energy | Same independent M16a timeline refusal |
| Insert a geometrically consistent but fabricated turning event | Same independent M16a timeline refusal |
| Forge native method | `saved motion method misattributes the integration protocol` |
| Put a surface event in a duration-complete history | `duration-complete history contains an impossible surface guard` |
| Unsupported rebound event | `motion has an invalid event` |
| Reverse saved force | `saved motion force contradicts physical Kelvin state` |
| Remove induced-energy half factor | `saved motion interaction energy contradicts physical Kelvin state` |
| Boolean native time or velocity | `motion sample has nonfinite or Boolean numerical data` |
| Change native q magnitude or permittivity without changing states | Physical Kelvin-force contradiction |
| Forge maximum drift or saved position | Saved-state drift or authored-position contradiction |
| Isolated conductor, hollow shell, extra source/conductor, zero q, interior/touching source | Relevant domain-specific refusal |

The JSON checker also rejected wrong signed current, inconsistent opposite-terminal current, changed induced Q with current retained, q-sign tampering, Boolean charge/time/velocity, false centre/source position, wrong force/U/permittivity, fabricated printed givens, and a false instantaneous mode. None of these were counted as a refusal merely because of a missing file/import or unrelated setup exception.

The genuine example JSON was generated by its actual CLI and accepted by both `validate_examples` and the standalone checker CLI. AST inspection found only `__future__`, `argparse`, `json`, `math`, and `pathlib` imports in the checker, with no production-physics imports or dynamic import/exec/eval calls.

**Important non-finding:** editing both matching JSON timestamp fields to a new monotonic intermediate time was accepted by the standalone checker. That tool explicitly does not re-integrate M16a. The case is recorded as `ACCEPTED_DOCUMENTED_LIMITATION`, not a failure. The corresponding native typed-history attack was correctly rejected by fresh M16a integration. Neither mechanism provides cryptographic proof against a modified execution engine. F3 requests only internal schema consistency, not an impossible provenance guarantee from bare JSON.

## 5. Original workbook: actual visual inspection and answer

I downloaded the **original full PDF bytes from the pinned source checkout**, not a teacher reconstruction, and independently rehashed them locally. I visually inspected the retained raster of physical **page 8, printed page 3.40**, including Q21's figure and all four options; I also inspected physical **page 17, printed page 3.49**, containing the answer key. No OCR was used. Web PDF viewing was unavailable; the authenticated original was rasterized with Poppler and inspected as images instead.

| Original artifact | Verified value |
|---|---|
| Repository file | `02_conductors_half_size.pdf` |
| Size | 20,685,051 bytes; 17 pages |
| Git blob, identical on base and candidate | `90d8869b0f01cc2ea13f83721985a5d8419f1d0e` |
| Independently rehashed SHA-256 | `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d` |

Source evidence: [Q21 page raster](evidence/run-44307096311-attempt-1/source-p08.png), [extracted original page 8 PDF](evidence/run-44307096311-attempt-1/source-page-8.pdf), [answer-key page raster](evidence/supplement-44307692757-attempt-1/source-p17.png), [PDF identity](evidence/supplement-44307692757-attempt-1/original-pdf-identity.json).

The printed problem specifies a **positive** charge q approaching a grounded metallic sphere of radius R at **constant small speed v**. Its figure shows the external charge to the right, an inward velocity arrow, the radius and the ground connection. The options ask about conventional current direction and whether its magnitude increases or decreases as the charge approaches. The source does not supply the teacher example's numerical charge, radius, separation, velocity or mass.

For this particular prescribed protocol, `vr=-v`, so

```text
I_sphere_to_ground = q*R*v/d^2 > 0
dI_sphere_to_ground/dt = 2*q*R*v^2/d^3 > 0.
```

Therefore the physical statements in **options (1) and (3)** follow. The printed **Multiple Correct Answers Type** key on page 17 explicitly gives Q21 **(1),(3)**. This is the workbook exercise section, not the separate JEE Advanced archives section; no official-past-paper attribution is added.

Static Kelvin electrostatics alone supplies Q(d), not a current without kinematic information. Here the original itself supplies v, so the instantaneous observer's closure is relevant. In contrast, freely integrated Newtonian M16a motion generally accelerates under the induced force: it is **not** the source's externally maintained constant-speed protocol. The genuine M16a examples demonstrate a useful different mode, not a literal reproduction of Q21.

This review establishes the original wording/figure/qualitative answer relationship. It does not edit the production coverage matrix or award a new automated whole-question/JEE completion. A later source-specific authored fixture should retain the prescribed-speed meaning, expose the requested option mapping, and distinguish any teacher numerical demonstration from printed givens.

## 6. Complete production CI status and preserved red history

The audit paginated the repository Actions runs for the exact candidate SHA and collected their jobs. The first snapshot had 21/25 successful runs; the second had 23/25. Those snapshots remain unaltered. I subsequently queried the two remaining Python runs and their complete job summaries through the GitHub connector: both runs and both Python 3.10/3.12 jobs in each were **completed/success**. The PR Python run's update time is `2026-11-18T12:50:49Z`; the push Python run's is `2026-11-18T12:52:40Z`.

**Final reconciliation: all 25 enumerated exact-head production runs SUCCESS, none pending/cancelled/failed.** This is observed existing production CI, not a claim that Chat B reran the whole legacy suite. The independent first-attempt review remains **FAILURE** because of F1–F3.

| Production workflow | Trigger | Exact-head run | Final conclusion |
|---|---|---|---|
| M35a audit and dependency-aware regression | PR | [44304645211](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645211) | SUCCESS |
| M21c composite symmetry | PR | [44304645130](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645130) | SUCCESS |
| M15c authoring/browser | PR | [44304645640](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645640) | SUCCESS |
| M34b certified incremental world fork | PR | [44304645336](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645336) | SUCCESS |
| M36e source answers/Chromium | PR | [44304645248](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645248) | SUCCESS |
| M19e source identity/world ring viewer | PR | [44304644971](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304644971) | SUCCESS |
| M21e electric/gravity composition | PR | [44304645296](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645296) | SUCCESS |
| M21d distant connected spheres | PR | [44304645188](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645188) | SUCCESS |
| M36b source replays/physics/Chromium | PR | [44304645136](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645136) | SUCCESS |
| M36d solid-source physics/Chromium | PR | [44304645355](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645355) | SUCCESS |
| M20a paired prescribed-field exploration | PR | [44304645780](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645780) | SUCCESS |
| M18c held-source authoring/physics | PR | [44304645279](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645279) | SUCCESS |
| M18b held-source viewer | PR | [44304645051](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645051) | SUCCESS |
| M36c conductor-source physics/Chromium | PR | [44304645818](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645818) | SUCCESS |
| M17c motion authoring | PR | [44304645388](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645388) | SUCCESS |
| Full Python 3.10 and 3.12 checks | PR | [44304645351](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645351) | SUCCESS |
| M22a structural composability | PR | [44304645256](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645256) | SUCCESS |
| M19b offline viewer/physics | PR | [44304644968](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304644968) | SUCCESS |
| M37a current/independent SI, Python 3.10 and 3.12 | PR | [44304645033](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645033) | SUCCESS |
| M33b native graph-world events/SI | PR | [44304645205](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645205) | SUCCESS |
| M19a prescribed fields | PR | [44304645259](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645259) | SUCCESS |
| FEMM 5 real-solver validation | PR | [44304645456](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645456) | SUCCESS |
| Visualization and source checks | PR | [44304645374](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304645374) | SUCCESS |
| Full Python 3.10 and 3.12 checks | Push | [44304634790](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304634790) | SUCCESS |
| M37a current/independent SI, Python 3.10 and 3.12 | Push | [44304634762](https://github.com/physicsvigilante/conductor_sim/actions/runs/44304634762) | SUCCESS |

Full captured records: [second CI summary](evidence/supplement-44307692757-attempt-1/exact-head-ci-summary.json), [complete run/job data](evidence/supplement-44307692757-attempt-1/exact-head-ci-full.json). The two later Python completions above supersede only their pending status in that earlier snapshot; no snapshot was rewritten.

The released-base main-push results were independently queried: **20/20 SUCCESS** at the exact released base, retained in [released-base-push-ci.json](evidence/supplement-44307692757-attempt-1/released-base-push-ci.json). These are baseline provenance, not substitutes for candidate CI.

### Historical failures remain failures

Seven older failed M37a runs are retained in [historical-red-m37a-runs.json](evidence/supplement-44307692757-attempt-1/historical-red-m37a-runs.json): `44302874444`, `44303002144`, `44303094358`, `44303360204`, `44303368728`, `44303882882`, `44303891405`.

The sandbox token could read run/job metadata but received HTTP 401 when downloading old job logs. Those retrieval errors remain recorded, not disguised as successful downloads. The connected GitHub log reader subsequently provided original logs for these concrete checks:

| Historical source / run / job | Actually inspected log result |
|---|---|
| `de3146b17e6bb69659f746ca3d140c31a488fd8a`, [44302874444 / 134796824809](https://github.com/physicsvigilante/conductor_sim/actions/runs/44302874444/job/134796824809), Python 3.12 | `4 failed, 109 passed in 1.10s`, logged at `12:20:17.6846264Z`; native saved energy-drift comparisons failed |
| `313103d6f18b952d5482be7660fbb88df955b585`, [44303002144 / 134797250475](https://github.com/physicsvigilante/conductor_sim/actions/runs/44303002144/job/134797250475), Python 3.12 | `4 failed, 109 passed in 1.25s`, logged at `12:20:51.0700294Z`; same failure class |
| `87d68ce4f27ad84a0a57571fc4c5d76ce15db246`, [44303882882 / 134800290898](https://github.com/physicsvigilante/conductor_sim/actions/runs/44303882882/job/134800290898), Python 3.10 | `1 failed, 112 passed in 1.69s`, logged at `12:30:35.4449633Z`; checker rejected the genuine instantaneous mode string |

These are excerpts independently read from actual failed logs, not full raw-log archives in the attached ZIP. In particular, the last inspected 112/1 failure is an **instantaneous-mode declaration mismatch**, not an inferred energy-rounding failure merely because the PR narrative mentions one. Earlier corrected revisions may have other failures; their recorded red statuses are not relabelled PASS. None of these older runs was rerun or overwritten by this review.

## 7. Reproduction and retained artifacts

The executed original scripts are [kelvin_oracle_chat_b.py](kelvin_oracle_chat_b.py), [challenge_chat_b.py](challenge_chat_b.py), and [audit_chat_b.py](audit_chat_b.py). Their executed revision is pinned above; [the first workflow](../../../../.github/workflows/conductor-pr89-chat-b-01.yml) preserves failure exit status rather than hiding it behind `tee`.

With source and reviewer checkouts available, the exact independent challenge invocation is:

```bash
set -euo pipefail
SOURCE=/absolute/path/to/conductor_sim
REVIEW=/absolute/path/to/review_sandbox
OUT=/absolute/path/to/new-review-output

git -C "$SOURCE" checkout --detach 75c984aaae18e44997332e330ed3a519a7b6a8da
git -C "$REVIEW" checkout --detach dc5339df9c1b1e4b88ca518f5c7d0bed739cda5b
test "$(git -C "$SOURCE" rev-parse HEAD^{tree})" = e1dbb9bb673f4efc2950939d0c1e021697393d59
mkdir -p "$OUT"
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="$SOURCE/src:$SOURCE"
python "$REVIEW/projects/conductor_sim/pr-89/reviews/challenge_chat_b.py" \
  "$SOURCE" "$OUT" 2>&1 | tee "$OUT/independent-first-attempt.log"
```

Use Python 3.12 for comparison with the actual reviewer run. The expected baseline exit code is **1** because the eleven defects are present. The script itself asserts HEAD and TREE, saves every case result and the relevant JSON mutants, and preserves genuine histories. It does not require installing or changing the production package. The workflow separately executes the read-only live/native audit and original-page rasterization.

The genuine example and checker commands exercised inside the challenge are:

```bash
python "$SOURCE/examples/grounded_sphere_wire_current.py" --output "$OUT/genuine-example.json"
python "$SOURCE/tools/m37a_ground_wire_reference.py" --input "$OUT/genuine-example.json"
```

Retained run/artifact identities:

| Artifact | Workflow / artifact ID | Independently downloaded ZIP SHA-256 |
|---|---|---|
| First-attempt review evidence | [44307096311](https://github.com/physicsvigilante/review_sandbox/actions/runs/44307096311) / `14429420502` | `92556a12cff680c0ac730baf42b5827bdb5aa0f3f558eddb6e5aa12b93717d7a` |
| Original full workbook | [44307692757](https://github.com/physicsvigilante/review_sandbox/actions/runs/44307692757) / `14429660387` | `52d2e679f48556e2456d0ebc2cd0eac429dff14417587935a36e236ba8510943` |
| Source/CI supplement | [44307692757](https://github.com/physicsvigilante/review_sandbox/actions/runs/44307692757) / `14429281780` | `d78bd17af66b5bdc80bc9d6857b14c3d484c874dea2a79746e33ae58d5d7068a` |

All three ZIPs were actually downloaded and SHA-256 rehashed locally against their artifact digests. The original PDF's SHA-256 and native Git blob were independently recomputed after extraction. The supplemental workflow's SUCCESS means **evidence collection succeeded**, not that the failed scientific review was rerun or passed. The first scripts, original failure results and original red run remain intact.

## 8. Remaining limits and release decision

No redesign of the core electrostatic law or M16a integrator is requested. This is a useful reusable observer on an already qualified narrowly defined model. General physical arrangements, multiple conductors/sources, isolated or hollow conductors, nonradial free 3D dynamics, finite wire impedance, electromagnetic delay/radiation, electron drift, collision/contact and a general grounding circuit remain outside this milestone.

There is no new synchronized current-plot viewer in M37a. Inherited real browser/source CI was checked; I did not claim a new M37a browser capture or graph. A current-versus-time visualization with faithful provenance is a separate future task, not an acceptance blocker invented for this JSON milestone.

**Required next gate:** correct F1–F3 with targeted regression tests while preserving the successful physics and native timeline checks. Retain these eleven baseline failures as historical evidence. A changed candidate needs new exact HEAD/TREE identification, exact-head CI and scoped independent re-review; this verdict does not transfer to a different SHA.

**Keep production PR #89 draft and unmerged. No owner merge authorization is given.** Even a later independent PASS requires a separate owner decision, expected-head protection, native merged-tree verification and actual postmerge main-push CI.

[observer]: https://github.com/physicsvigilante/conductor_sim/blob/75c984aaae18e44997332e330ed3a519a7b6a8da/src/conductor_sim/grounded_sphere_wire.py#L84-L127
[checker]: https://github.com/physicsvigilante/conductor_sim/blob/75c984aaae18e44997332e330ed3a519a7b6a8da/tools/m37a_ground_wire_reference.py
