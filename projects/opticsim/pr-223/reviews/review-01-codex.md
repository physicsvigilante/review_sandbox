# Opticsim PR #223 independent review R1

**BLOCKED at exact candidate `28f6bb20e0bedc59d23f837d5f6e38637c031f2d`.** Three single-mirror numerical witnesses require correction.

| Identity | SHA |
|---|---|
| Candidate tree | `aed5d3a61b1f16a5aee0f3a5aaffe470f5e40cfe` |
| Production base | `3313624ae9173ebf8dad738ac27f246e235389a9` |
| GitHub PR test merge | `3f23cfa90f79a1e213afd7f0364d7574cd7953c9` |

## Findings

- **Near-grazing normal does not reproduce the requested reflection.** Incoming (1,1), outgoing (1,1.00000000201) qualify just above the 1e−9 unit-chord limit. The reported normal (−0.7071066707165873, 0.7071068916564903) produces an outgoing unit vector 3.1346e−7 from the requested unit vector when used in the reflection equation, more than 300 times the intended turn. For acute heading pairs, the normal line can be recovered stably as the perpendicular to the large sum of the two unit headings. The incident–outgoing difference remains stable for obtuse pairs.
- **Rounded chord qualifies a grazing-band input.** Incoming (−4.858584759550399, −6.222875581039037), outgoing (−2.6497192137419563, −3.393760496487345) return a qualified result based on a rounded unit chord of approximately 1.0000000936451704e−9. An exact rational test using the represented raw vectors shows the chord is at most 1e−9. For positive dot product C, compare C² with (1−eps²/2)² times the product of the two squared norms.
- **Near-normal incidence is given as exact zero.** Incoming (1,0), outgoing (−1,1e−16) give an incidence result of 0° and a normal y component of 5e−17. The representable positive incidence is about 2.86479e−15°. Evaluate the incidence directly using atan2 of the absolute cross product and negative dot product, with numerical handling that protects nonzero cross products at the lower representable limit.

## Positive and preserved controls

The exact A01 and A02 PNGs matched their frozen Problems-only hashes. Solutions stayed unopened. The A01 original headings imply a 30° incidence. A02 specifies input parallel to the second mirror and output parallel to the first, after the two reflections in order. Its 60° acute inclination, 120° principal directional change and 240° accumulated magnitudes of the two turns are well defined as separate quantities.

Five frozen native controls and 17 scoped tests passed independently. A supplementary independent native sweep checked every one of 16 supported directed branches across the four crossed parallel/perpendicular relations. In each case the finite pinned Mirror callbacks occurred in the required order and a real native Blocker absorbed the final ray. No other substantive blocker was identified in the two-mirror branch.

This release verdict is bound to the stated initial source. A corrected candidate needs focused verification and full hosted CI.
