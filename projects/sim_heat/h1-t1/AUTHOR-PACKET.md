# H1-T1 — public authoring packet (blind source-only trial)

**Trial:** `H1-T1` (new trial, NOT historical H1-C1-F0).
**Implementation pinned:** `physicsvigilante/sim_heat@f52613c39c539b2d4543a9838e5658d526fca10e`, tree `0c44961b473d23737b0c9f3b3f2cd3db65b9f264`. This packet describes the *currently implemented* restricted H1 grammar; it adds no physical law, parser, solver or execution authorization.

## Read boundary and the first-attempt rule

**Author:** read only THIS packet and the independently locked public H1-T1 task statements supplied in the intake issue. Do **not** inspect the SIM_HEAT implementation, existing H1 cases, source tests, prior review reports, historical C1, evaluator rubric, answer keys or previous model solutions. Do not ask Chat A for physics or formatting repairs. Disclose any previous exposure; separate chat context does not establish a genuinely unseen problem or independent model weights.

Produce one **original first submission for all three tasks** before receiving evaluator feedback. No pre-submission H1 validator/workbench, code search, compiler, OpenModelica, solution engine, simulated readings or direct project source modifications. Standard-library SHA-256 hashing of YOUR OWN scratch model bytes is allowed if disclosed. If unable to compute a hash, say `HASH_UNRESOLVED` in notes and leave the intended SHA field explicitly unresolved; this is an incomplete raw first attempt, not a reason to fabricate a digest. The evaluator may later supply **mechanical** hashes as separately recorded assistance, never backdate them as original first-attempt author output. Preserve the originally submitted text exactly, even if refused.

The task selector—not Chat A—chooses and seals the task statements **before** you begin. Positive tasks will request only supported conduction; the negative task deliberately demands unsupported physics. Do not quietly replace the task by a simpler apparatus to obtain admission.

## What H1 represents (and does not)

H1 is **constant-property, lumped conduction** with uniform-temperature finite bodies, **storage-free** conducting rods and maintained-temperature boundaries. Ideal thermal connections share temperature and conserve signed heat flow. There is **no** fluid motion, radiation, convection, phase change, mechanical work, variable material law, arbitrary PDE, symbolic/inverse solution, general geometry engine, source-identity authentication, native solver launch or automatic physical answers. A request to model an unsupported law must be **explicitly refused** as an unsupported task, not approximated with a fabricated rod. Material names do not automatically provide physical properties.

A valid source model is not yet a simulation: H1 admission and the source-only workbench report all physical observations **`not_computed`**. Do not claim a native reading or predict a final temperature.

## Physical file `model.mo` — fully bounded Modelica subset

Use UTF-8 text, optional `within;`, one `model ModelName`, component and optional typed scalar parameter declarations, optional `equation` with only `connect(name.port, other.port_a);`-style statements, and exactly matching `end ModelName;`. Names begin with an ASCII letter and contain only letters, digits and underscore; use distinct identifiers, not Modelica/SimHeat names or keywords. Comments `//` and `/*...*/` are supported; arbitrary equations, algorithms, imports, arrays, inheritance, strings, functions, arithmetic and annotations are not.

Only these constructors and named SI inputs exist:

| Constructor | **Every** required named field | External thermal ports |
|---|---|---|
| `SimHeat.Body` | `m` kg, `c` J/(kg K), `T_initial` K | `port` |
| `SimHeat.RodArea` | `k` W/(m K), `L` m, `A` m² | `port_a`, `port_b` |
| `SimHeat.RodCircular` | `k` W/(m K), `L` m, `d` m (**diameter**, not radius) | `port_a`, `port_b` |
| `SimHeat.FixedTemperature` | `T` K | `port` |

Declarations follow `SimHeat.<Constructor> identifier(field=value, ...);`; supply all and only the fields shown once. All mass, specific heat, absolute temperature, conductivity, length, area and diameter must be **positive, finite SI values**. Derived heat capacity, rod area and conductance are *not additional author inputs*.

Each field accepts a finite signed/unsigned decimal or scientific literal, a **previously declared type-compatible scalar parameter**, or a permitted unit conversion with literal arguments only: `SimHeat.Units.from_degC(x)`, `SimHeat.Units.from_cm(x)`, `SimHeat.Units.from_cm2(x)`, or `SimHeat.Units.conductivityFromKcal(x, J_per_kcal)` where the second argument is an explicitly justified positive conversion factor. Typed parameters use `parameter Modelica.Units.SI.Type name = value;`; allowed Types: `Mass`, `SpecificHeatCapacity`, `Temperature`, `ThermalConductivity`, `Length`, `Area`. No parameter arithmetic or hidden/default physical constants.

All connections use named external ports. A `connect(a.port, b.port_a);` statement joins two ideal ports; multiple statements can define an **ownerless ideal junction**, which needs no custom component or heat capacity. Each ideal node has **at most one** `Body` or one `FixedTemperature`; do not directly connect body-to-body, body-to-boundary or boundary-to-boundary ports. Both ends of every rod must be connected; do not connect both ends together, leave isolated rods/boundaries or duplicate unordered connection pairs. Loops/branches/parallel rods are possible *within these rules*. Transient mode requires at least one body. Steady mode has **no Body**, needs rods and maintained boundary anchors in each connected network, and uses `analysis: {}`. Component limits: max eight bodies, eight boundaries, 32 rods, 64 logical nodes, 128 connections, 256 parameters; model <=64 KiB. Numerical conditioning can still refuse an otherwise syntactically valid graph.

## Investigation file `study.json`

Use valid UTF-8 JSON with **exactly** top-level keys `schema`, `id`, `model`, `mode`, `requests`, `analysis`, `provenance`. Do not create a `revision` object for T1. Avoid duplicate/unknown keys, `NaN`, `Infinity`, guessed/model-independent physical overrides. Identifiers have the same ASCII constraints as model names.

- `schema` = `sim_heat.study/1`.
- `id` = new, truthful source identity.
- `model` = `{"path":"model.mo","sha256":"<64 lowercase hex characters of exact model.mo bytes>"}`. Compute the actual SHA-256 of the submitted model, including newlines. Do not invent it.
- `mode` = `"steady"` or `"transient"`, as physically required by the **locked** task.
- `analysis` = `{}` for steady. For transient, the object has **exactly** `startTime` (zero), `stopTime` (seconds, 1e-6 through 1e7), `intervals` (even integer 1000 through 20000), `solver` (`"dassl"`) and `tolerance` (numeric `1e-8` or `1e-10`). Choose a reasonable **provisional** grid if the task supplies none, mark it provisional in notes; admission is not numerical qualification or approval to execute.
- `requests`: no more than 32 unique-ID entries in the exact public grammar below, no predicted values:
  - `{"id":"r1","op":"temperature","target":"body.port"}`
  - `{"id":"r2","op":"temperatureDifference","a":"rod.port_a","b":"boundary.port"}`
  - `{"id":"r3","op":"heatFlow","target":"rod"}`
  - `{"id":"r4","op":"energyChange","target":"body"}` (only when a Body exists).
- `provenance`: up to 2048 records, each **exactly** `{"target":"component.field","kind":"illustrative","locator":"locked task ...","note":"truthful attribution"}`. Targets may instead be previously declared scalar parameter names, whole component (only as additional general notes) or `@model`. Every effective physical field needs direct or bound-parameter attribution, **not** only a whole-component note. Include an `@model` record with kind `adopted_assumption` or `solution_assumption` describing the constant-property/lumped/storage-free regime. Allowed kinds: `source_given`, `source_diagram`, `solution_assumption`, `adopted_assumption`, `unit_convention`, `illustrative`. For selector-invented teaching numbers, clearly use `illustrative` (do not invent textbook provenance). For actual externally given facts, report source locators honestly.

The model path must remain inside its case directory, inside the allowed case root, with no symlinks/path escape. The study file is <=256 KiB. Keep the task's identity, every source fact, assumptions and requested observations faithfully; do not silently modify a source problem to fit the H1 interface.

## What to submit before evaluation

For supported task **S** and supported task **T**, include separate, complete, unmodified plain-text artifacts `S/model.mo`, `S/study.json`, `S/AUTHOR_NOTES.md`; and analogously for T. The notes state your author/model, prior SIM_HEAT exposure, sources/tools used, hashing assistance, uncertainties, assumed unit conversions, any provisional analysis grid, and task-fidelity concerns. Record the FIRST output; do **not** revise it after you see admission results.

For deliberately unsupported **X**, include **`X/REFUSAL.md`** explaining the physical law outside the current library, which task demands it, and what additional reusable law would be needed. Do **not** submit a misleading conduction surrogate or fictional native values. If you believe it *is* supported, explain your interpretation without hiding the mismatch.

Send **all three first-attempt artifacts together in one intake comment** labeled `H1-T1 FIRST_ATTEMPT_V1` on the source issue identified in the selector task handoff. Then **stop**. If you cannot write to GitHub, return raw complete blocks and stop so the evaluator can capture them *before* running H1. Do not request validator feedback before first capture.

**Evaluation is staged:** physical/source fidelity vs the independently locked task first; exact unassisted admission next; mechanical digest/packaging assistance separately recorded; source-only inspector fidelity next; unsupported-law refusal as its own criterion. Neither project admission nor consistent source hashes authenticate externally authored facts.

This trial **does not** run OpenModelica, create new native evidence, change physics, rewrite C1, or authorize a production merge/deploy. 
