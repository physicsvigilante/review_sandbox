# Independent R2 review of SIM_HEAT #179

**Verdict: changes requested.** The thermal calculation passed independent probes. The Python entry point admits ambiguous environment identifiers that cause a serialized result to lose the controlling condition.

Packet 4b7413d9eda726b11c93c855dedfdbb22305f594. Source base 0cbced5a1dbcc0f67219b97ee8ab10e35472339f and reviewed head 8b9745f02de9277b324d8b9aa980d4d6fdb35d91.

## Evidence integrity finding

In tools/shell_environments.py, investigate checks truthiness and membership of each condition name before using it as a JSON object key. Python distinguishes integer 1 and string "1". Serialization emits duplicate "1" members. A normal JSON round trip silently retains the last one.

I called investigate with the composite-wall cold port, spherical inner radius 0.1 m, fixed layer (0.13 m, 1.4 W/m/K), coating conductivity 0.8 W/m/K, stocked radii 0.33, 0.155 and 0.21 m, emissivity 0.73, sigma 0.0000000567 and a 1 W budget. The conditions were [(1,"444","9","405"),("1","380","0","380")]. After json.loads(json.dumps(result)), all three rows report over_budget, while the only recorded exposure in each row reports within_budget. This affects the callable Python entry point. Argparse supplies strings for the CLI. Require nonempty string names before using them as keys and exercise the collision as a refusal regression.

A separate malformed-input probe supplying ("a",None,None,"270") surfaced KeyError('airTemperatureK') during result assembly. Require the two explicit air fields at the multi-condition entry point and exercise this refusal. The single-case function supports a radiation-only mode.

## Independent checks

- Verified the GitHub job's head and success, the archive digest d3c038729a490f9a85323dbe0eaa0828de2edb1b9118f8318153a2f6a029ee1e and archived head.txt. Archived regression.log records 258 passing tests. The pinned replay matched both shell evidence JSON objects. Five focused shell tests passed locally.
- Independently solved spherical heat transfer at 100 decimal digits using port open temperature 380 K and resistance 0.5 K/W, the exact spherical layer formula, area 4 pi r squared, and a scalar root for the sum of signed convection and radiation. For the geometry above the separate (air K, h W/m2/K, enclosure K) triples were (270,8,455), (294,3,260) and (444,9,405). Checked all nine signed rates and magnitudes against their rational bounds, plus the three maxima. In ascending size order, worst magnitudes were approximately 85.72389453, 87.58814342 and 85.97877916 W. At 68 W all fail. At 86 W the first and last fit and the minimum is 0.155 m. At 88 W all fit. Reversing both input orders preserved the structured result.
- Verified each valid single-condition result against the base implementation for these three environments and against the archived cylinder example. Inspected the unresolved-smaller guard and reran its existing regression, equality and no-fit cases. Empty conditions, repeated string names, an empty name and a negative film coefficient raised ValueError.
- Scope is finite specified steady exposures, fixed geometry, fixed materials and common budget. No native execution, native qualification or independent certification of the tool's outputs is claimed. Independent context is a fresh reviewer agent. New evidence needed for re-review is confined to Python input validation and serialized condition identity.
