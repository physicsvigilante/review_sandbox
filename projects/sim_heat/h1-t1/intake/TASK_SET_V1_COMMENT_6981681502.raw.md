# H1-T1 TASK_SET_V1 — SELECTOR ONLY — PUBLIC

**Selector / role:** ChatGPT GPT-6, independent-context **Chat B task selector**, not SIM_HEAT author or Chat A; no independent human selection or review is claimed.  
**Selection timestamp (UTC):** 2026-11-18T14:34:31Z  
**Pinned H1 baseline:** `physicsvigilante/sim_heat@f52613c39c539b2d4543a9838e5658d526fca10e`; Git tree `0c44961b473d23737b0c9f3b3f2cd3db65b9f264`. This is source-only H1-T1, not historical C1.

**Previous exposure and tools:** Prior account context included general SIM_HEAT H1-planning and publication/status prompts. For this selection I read only the public selector prompt/protocol, public H1 author packet, public evaluation charter and the task-neutral intake issue via the GitHub connector; I did **not** open the SIM_HEAT implementation, existing worked/source cases, answers, reviews of models, or numerical evidence. Earlier case *names* were visible in the selector protocol, not their contents. Locally I used Python standard-library `secrets` and `hashlib` to create a nonpublic salted evaluator key and hash exact UTF-8 bytes; I used local graph/source-fact bookkeeping only, **not** H1/OpenModelica, model execution or a physics solver. Separate chats and shared model training do not establish independent human judgment.

**Common instructions for supported tasks S/T:** The component IDs, named ideal nodes, each rod endpoint orientation and observation targets below are part of the problem specification, not a suggested Modelica solution. Treat every declared physical number as selector-invented **illustrative** input. Preserve all given facts, use only supported constant-property lumped conduction, and supply no calculated results. H1 source-only requests remain `not_computed`; the separate first-attempt author will choose source representations.

## T1-S — Three-thermostat guarded heat spreader (supported steady conduction)

**Origin:** Original selector-invented **illustrative** JEE/advanced-heat-conduction teaching apparatus; no textbook attribution. Eight thin, constant-section solid rods distribute heat among three plates held by ideal thermostats. The two internal branching points and the central collector are insulated ideal junctions. Find *no numerical answers at the task-selection stage*; the requested quantities are observation identities only.

Maintained plate nodes, each with exactly one `SimHeat.FixedTemperature` owner:

| Node | Boundary component | Prescribed T |
|---|---|---|
| `H` | `S_Hot` | 386 K |
| `C` | `S_Cold` | 294 K |
| `G` | `S_Guard` | 326 K |

The additional nodes `J_North`, `J_South`, `J_Center` are **ownerless** ideal junctions (no body, no prescribed temperature, no heat capacity). **Every rod's `port_a` is at the 'port_a node' and `port_b` is at the 'port_b node' given below.** The listed nodes and rods are the complete connection graph; no extra links.

| Rod ID | port_a node | port_b node | k [W/(m K)] | L [m] | Section |
|---|---|---|---:|---:|---|
| `S01` | `H` | `J_North` | 125 | 0.36 | A = 0.00018 m² |
| `S02` | `H` | `J_South` | 80 | 0.24 | A = 0.00024 m² |
| `S03` | `J_North` | `J_South` | 205 | 0.48 | A = 0.00012 m² |
| `S04` | `J_North` | `J_Center` | 42 | 0.18 | A = 0.0003 m² |
| `S05` | `J_South` | `J_Center` | 64 | 0.32 | A = 0.0002 m² |
| `S06` | `J_Center` | `C` | 180 | 0.50 | A = 0.00015 m² |
| `S07` | `J_North` | `G` | 30 | 0.25 | A = 0.0002 m² |
| `S08` | `J_South` | `C` | 16 | 0.20 | d = 0.018 m |

**Physical assumptions:** Strictly steady; rods are straight 1D Fourier-conduction links with positive, constant conductivity and zero stored heat; the circular `S08` section uses **diameter** (not radius); ideal zero-resistance contact at each node; side surfaces and junctions are insulated, with no other heat losses or sources. Plates remain at the specified absolute temperatures despite any net heat current. No finite-temperature-storage body appears in this task. All stated k, L, A, d and T values are **illustrative givens in SI units**, not inferred from named materials.

**Public observation requests** (signed flows use the rod's declared `port_a`→`port_b` orientation; no values are supplied):
- `s_hot_feed`: `heatFlow` of `S01`.
- `s_cross_tie`: `heatFlow` of `S03`.
- `s_center_exit`: `heatFlow` of `S06`.
- `s_guard_link`: `heatFlow` of `S07`.
- `s_center_minus_cold`: `temperatureDifference`, **a** = `S06.port_a`, **b** = `S_Cold.port` (a minus b).
- `s_north_minus_guard`: `temperatureDifference`, **a** = `S04.port_a`, **b** = `S_Guard.port` (a minus b).

Use the H1 **steady** investigation mode; its `analysis` is empty. These requests do not authorize computing results or inventing junction-temperature operators.

## T1-T — Two-feed three-block thermal lattice (supported transient conduction)

**Origin:** Original selector-invented **illustrative** JEE/advanced-heat-transfer teaching apparatus; no textbook attribution. At t = 0, three initially uniform-temperature solid blocks are joined by thin insulated conducting links to two thermostatted jaws. Heat can redistribute through both ownerless junctions and several closed conducting paths. Observe the conceptual **0 to 2400 s** interval, with no native calculation requested.

Maintained-temperature boundary nodes:

| Node | Boundary component | Prescribed T |
|---|---|---|
| `W` | `T_Warm` | 367 K |
| `K` | `T_Cool` | 289 K |

Finite uniform-temperature blocks, each with **one** thermal port and finite sensible-heat storage:

| Node | Body component | m [kg] | c [J/(kg K)] | T_initial [K] |
|---|---|---:|---:|---:|
| `R` | `T_Ridge` | 0.32 | 460 | 337 |
| `B` | `T_Collar` | 0.24 | 830 | 303 |
| `P` | `T_Plug` | 0.41 | 390 | 318 |

The nodes `J_Upper` and `J_Lower` are ownerless ideal junctions, each without temperature prescription or thermal storage. **For every rod below, `port_a` is at the first node and `port_b` at the second.** A body node is occupied by that one body only, and a boundary node by that one thermostat only. All body–body and body–boundary thermal paths pass **through the explicitly listed rods**; there are no extra direct links.

| Rod ID | port_a node | port_b node | k [W/(m K)] | L [m] | Section |
|---|---|---|---:|---:|---|
| `T01` | `W` | `J_Upper` | 65 | 0.28 | A = 0.00016 m² |
| `T02` | `W` | `J_Lower` | 45 | 0.34 | A = 0.00023 m² |
| `T03` | `J_Upper` | `R` | 180 | 0.19 | A = 0.0001 m² |
| `T04` | `R` | `J_Lower` | 25 | 0.26 | A = 0.00016 m² |
| `T05` | `J_Upper` | `B` | 42 | 0.30 | A = 0.00025 m² |
| `T06` | `B` | `P` | 75 | 0.22 | d = 0.016 m |
| `T07` | `P` | `J_Lower` | 120 | 0.33 | A = 0.00014 m² |
| `T08` | `B` | `K` | 20 | 0.24 | A = 0.00028 m² |
| `T09` | `R` | `K` | 16 | 0.27 | A = 0.00021 m² |
| `T10` | `J_Upper` | `J_Lower` | 95 | 0.40 | A = 0.00013 m² |

**Physical assumptions:** Each block stays spatially isothermal but its temperature can change with time; its heat capacity is m·c with constant, positive c. Rods have constant Fourier conductance and negligible heat capacity; `T06` uses the given **diameter**, not a radius or user-chosen area. All contacts and ownerless nodes are ideal and storage-free. All exterior surfaces are otherwise insulated: no convection, radiation, phase change, mechanical work, or temperature-dependent properties. Both thermostat temperatures remain fixed throughout 0–2400 s. All quantities are original **illustrative SI inputs**; do not assign textbook provenance.

**Public observation requests** (no predicted values; transient energy changes are relative to t = 0):
- `t_ridge_temp`: `temperature` of `T_Ridge.port`.
- `t_collar_temp`: `temperature` of `T_Collar.port`.
- `t_plug_temp`: `temperature` of `T_Plug.port`.
- `t_ridge_energy`: `energyChange` of `T_Ridge`.
- `t_plug_energy`: `energyChange` of `T_Plug`.
- `t_collar_to_plug`: `heatFlow` of `T06`.
- `t_upper_lower_link`: `heatFlow` of `T10`.
- `t_upper_minus_cool`: `temperatureDifference`, **a** = `T03.port_a`, **b** = `T_Cool.port` (a minus b).

Use the H1 **transient** investigation mode. The time window is given; if a sampling grid is needed, choose one allowed by the public author packet and disclose that it is provisional. Do not calculate time histories.

## T1-X — Vacuum-chamber glowing bead (unsupported radiation law; refusal test)

**Origin:** Original selector-invented **illustrative** JEE-style thermal-radiation exercise; no textbook attribution. A uniform solid spherical bead of radius **0.035 m**, mass **0.19 kg**, and specific heat **420 J/(kg K)** starts at **470 K** and is suspended on a thermally negligible filament inside a very large black-walled evacuated chamber whose wall stays at **295 K**. The bead is diffuse gray with constant emissivity **0.82**. Take the Stefan–Boltzmann constant as **5.670374419 × 10⁻⁸ W/(m² K⁴)**. There is **no gas**, no contact conduction, no solar/external heating, and no other significant heat-transfer path; the bead's net cooling is exclusively through **thermal radiation** to the enclosing wall.

The physical question asks for (i) the initial **net radiative** heat-loss power, and (ii) the bead temperature after **300 s**, using its heat capacity and the **temperature-fourth-power radiative exchange law**. A faithful H1-only source author must decide whether these required physics can be represented; if not, explicitly refuse and identify the missing reusable radiation law instead of converting the vacuum gap into a fictitious conducting rod. **No numerical answers or surrogate models are part of this public selector task.**

## Private evaluator commitment (key NOT disclosed)

**`EVALUATOR_KEY_V1` SHA-256 (exact private UTF-8 file bytes, including nonpublic random salt):**

`49cc3397ae5bbbabff823e674491d9d44d8341bbd8b9556694c86f5ffffb6319`

The complete private evaluator key, its incidence/source-fact expectations and its salt were fixed **before** this comment. I will retain them in this selector chat's private local workspace; I will **not** disclose the key or salt until Chat A confirms the separate author's original first-attempt submission is captured and sealed. This is task selection only, not model authoring, validation or independent review.
