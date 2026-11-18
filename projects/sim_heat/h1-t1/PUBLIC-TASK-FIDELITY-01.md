# H1-T1-UNSEALED — retrospective PUBLIC-TASK fidelity check, completed BEFORE H1 validation

**Classification:** `UNSEALED_RETROSPECTIVE_SOURCE_FIDELITY`. Original selector private key remains **UNAVAILABLE / SHA-256 commitment NOT VERIFIED**; this is a post-author comparison against a separately timestamped and locked PUBLIC task statement, **not** a successful sealed-key blind scoring. This record was created BEFORE running the pinned H1 validator, numerical checker, source preview or any native operation on the submitted T1 models.

**Authorization:** [UNSEALED-AUTHORIZATION-01](UNSEALED-AUTHORIZATION-01.md) — owner explicitly accepted the downgraded offline source-only evaluation after [KEY-UNAVAILABLE-01](KEY-UNAVAILABLE-01.md).

**Original source identities:**
- Selector task original [issue comment 6981681502](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6981681502), already sealed, entire raw comment SHA256 `8f45ad3d4a763952e25d60658ae4d8eeae37fd266bd372b3cd80fb19b81fa2a2`, [verbatim task snapshot](intake/TASK_SET_V1_COMMENT_6981681502.raw.md).
- Author first attempt original [issue comment 6982616288](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6982616288), already sealed, entire raw comment SHA256 `fa96e40b24fe3b039e823a78f54546bdf0ed2400e0f3b1b9519bbeb764e3c893`, [verbatim first-attempt snapshot](intake/FIRST_ATTEMPT_V1_COMMENT_6982616288.raw.md). [FIRST-ATTEMPT-LOCK-01](FIRST-ATTEMPT-LOCK-01.md) confirms original capture BEFORE this evaluation.
- Target evaluator implementation/source tree: SIM_HEAT `f52613c39c539b2d4543a9838e5658d526fca10e` / `0c44961b473d23737b0c9f3b3f2cd3db65b9f264`. No code under that SHA was run yet on these T1 files.
- The author's seven original Markdown code fences were read directly from the locked full comment, not re-authored model files. For prospective file extraction, use the exact code-fence content **plus one LF** before the closing fence (as the author states they wrote LF-terminated physical files), and record this explicitly as a **derived exact-LF extraction**. The code fences themselves contain their contents, but not an independently uploaded original file. Distinguish authoritative raw Markdown comment from reconstructed file bytes.

## Method (source facts before engine admission)

Using only original public task S/T tables and the first submitted Modelica/study text, Chat A performed a **standalone deterministic syntax-shape comparison**, not H1 parsing or a physics/numerical solve:
- Read each selector's fixed rod-ID, `port_a` node, `port_b` node, rod kind, k/L/A or d numeric values, boundary temperatures, body m/c/T_initial values and public request identities.
- Read first authored declarations/real literal values and `connect` expressions; construct undirected port-equivalence classes by union-find and compare **the complete sorted port-membership partitions** to those specified by the locked public graph. This verifies source topology and orientation, not thermal flux direction or an actual solver result. Every rod endpoint's `port_a/port_b` belongs to the expected class, without extra link or owner.
- Compare source quantities numerically in SI, including the **diameter**, not radius, for circular rods S08/T06. Compare public operation/operand order and named component/port identities exactly, model mode and the provisional transient grid.
- Compare direct provenance targets/kinds with every declared physical slot. `@model` adopted-assumption notes refer to the requested constant-property/lumped/conduction regime. Distinguish source-attribution claims (the tasks were selector-invented illustrative values) from externally verified textbook givens; no external textbook source was used.
- Recompute SHA-256 of the literal code-fence Modelica text plus one terminal LF using a SHA-256 implementation verified against published empty-string/`abc` and Unicode test vectors. Verify both exact author-provided model hashes; the same text WITHOUT final LF has a different digest, so the derived-byte extraction choice is material and recorded.
- Inspect original unsupported-task `X/REFUSAL.md` for necessity of nonlinear thermal radiation, refusal of a fake conducting rod, and no numerical answers. A symbolic formula for the missing law is not a simulated result.
- No hidden evaluator key was received or reconstructed; this is a **retrospective transparent public-task rubric**.

## T1-S — source-fidelity preliminary result

**PUBLIC-SOURCE-FIDELITY-PASS** for the original steady `Three-thermostat guarded heat spreader` statement, subject to later **separate actual H1 admission**.

- **11 exact components:** thermostats `S_Hot=386 K`, `S_Cold=294 K`, `S_Guard=326 K`; area rods `S01` through `S07`; circular rod `S08` with exact diameter `d=0.018 m`. **All eight rods' k, L, A/d match** locked public table, as do all 3 original boundary T facts.
- **13 authored connect expressions** form **exactly the six locked ideal port-equivalence nodes**, including three thermostat-owned nodes H/C/G and three distinct **ownerless ideal junctions** `J_North`, `J_South`, `J_Center`. Every rod orientation `port_a`/ `port_b` matches. Graph partition EXACT, no substituted short-circuit/junction body, extra rod or missing link.
- `mode="steady"`, empty `analysis={}`, no finite bodies. **All 6 public requests** match selector ID, operation, rod/port operands and sign/order, including both a-minus-b `temperatureDifference` requests.
- **27/27 effective authored scalar fields** directly covered by 27 `illustrative` source attributions, plus one `@model` adopted-assumption record; no attribution to an invented textbook.
- Study ID `H1T1SFirstAttemptV1`. Embedded model digest `26113226ae046634c36e0acd51cdeb84f6ce9c500dbaaa86f31e5d34fbfce2a7` equals SHA-256 of **1,411 derived model UTF-8 bytes including final LF**. Without final LF digest differs (`18a06b59afa1116e9b06af18e4602fc13c28b3c49981cda1784b2f2fe607e594`). Prospective derived LF-terminated study file is 7,045 UTF-8 bytes. No external mechanical digest repair indicated.

## T1-T — source-fidelity preliminary result

**PUBLIC-SOURCE-FIDELITY-PASS** for the original transient `Two-feed three-block thermal lattice` statement, subject to later **separate actual H1 admission**.

- **15 exact components:** maintained boundaries `T_Warm=367 K`, `T_Cool=289 K`; finite bodies `T_Ridge(m=.32,c=460,T_initial=337)`, `T_Collar(m=.24,c=830,T_initial=303)`, `T_Plug(m=.41,c=390,T_initial=318)`, SI; area rods `T01`–`T05` and `T07`–`T10`, circular `T06(d=.016m)`. All 10 original rod k/L/A/d values exactly match selector's givens.
- **18 authored connect expressions** produce **exactly the seven locked ideal port-equivalence nodes**: W/K boundaries, R/B/P body-owned nodes and distinct ownerless `J_Upper` / `J_Lower`. No direct owner-owner short-circuit or invented junction storage; all signed rod-port orientations and loops/branches match the original task graph.
- `mode="transient"`, prescribed `startTime=0, stopTime=2400s`; author picked `intervals=2400` even, `solver=dassl`, `tolerance=1e-8`, **provisional sampling only**. These settings were NOT prequalified as numerical solver accuracy or native permissions.
- All **8** requested public observation IDs, operations, targets and temperature-difference operand order match EXACTLY. **41/41 scalar slots** directly covered by 41 `illustrative` source attributions, plus one `@model` regime note. Model/external-source fidelity is limited to selector's self-described illustrative numbers, not independent textbook proof.
- Study ID `H1T1TFirstAttemptV1`. Embedded model digest `2c60e40f1ad8d85f46968f03712d23e8cd6b9c656cf6099a38a97d198d0873ae` exactly equals SHA-256 of **1,945 derived model UTF-8 bytes with final LF**. Without final LF hash `9d843b89f0640083d69dd136e549305fb4f14dfb0d891e6dd891a1582f2424ea` differs. Prospective derived LF-terminated study file is **10,530 UTF-8 bytes**; no external hash repair indicated.

## T1-X — unsupported-law boundary

**PUBLIC-REFUSAL-FIDELITY-PASS** on original `X/REFUSAL.md` text. It explicitly refuses to fabricate H1 conduction across an evacuated gap, identifies required bead-to-black-enclosure thermal-radiation `T^4` law, emissivity, surface area and radiative net exchange, the bead's heat-storage balance, and lack of an H1 radiation component; proposes a future reusable radiation extension **without** pretending it exists now. It provides **no X/model.mo, no X/study.json and no computed radiative power or 300-second temperature**. Symbolic restatement of missing physics is not a numerical result. Its source values are attributed to original selector-invented illustrative facts, not a JEE textbook.

## Open gates and scientific limits

**This source-fidelity finding is a prerequisite for, NOT a substitute for, actual H1 admission.** It verifies the authored source facts, topology, provenance linkage and public requests against the locked public task; it does not prove H1 parser accepts these original bytes, numerical conditioning/time-grid checks, source-only viewer rendering or native physical correctness. The original private scorer key's unavailability forever prevents calling this comparison a *verified precommitted hidden-key trial*, regardless of later parser PASS. The selector and author both used the same GPT-6 family with separate contexts and disclosed prior project exposure; do not overstate independent model weight, blind human evaluation or verified textbook origin. Any failed parser/admission is a real separate first-attempt outcome, not permission to patch source without preserving it.

**Next after committing THIS report:** run the exact pinned H1 offline validator against the precisely extracted original LF-terminated S/T files in a scratch directory; do not modify authoring facts or native code. Save original file byte digests, actual stdout/stderr/refusals, and source-only preview when admitted. Unsupported X remains a refusal. No native OpenModelica/build/launch, original six archived diagnostic mutation, frozen C1 repair, new physical/numerical references, production source merge or deployment.
