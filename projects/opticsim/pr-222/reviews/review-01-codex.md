# Opticsim PR #222 independent review R1

**BLOCKED at `957394f3a7e86454e4ada0035c4d6839218a4f77`.** Three numerical witnesses expose incorrect acceptance or output geometry.

| Identity | SHA |
|---|---|
| Candidate tree | `b564250061f30cefcee0c59ac838d8df294ee4c6` |
| Production base | `8991e8c4c8dc2f1b26999f5ea7bffb5f84acb64f` |
| GitHub PR test merge | `e35d1fe137fe976af928d3435d313dc252676459` |

The PR test merge has the stated base and candidate as parents and the exact candidate tree.

## Findings

- **Fixed wall coordinate can be outside the box.** With W=37.21, H=26.37 mm, A=(2.017, 4.013) and B=(12.345, 5.33), a qualified top contact reports y=26.370000000000005, above its authored wall. The tagged fixed axis is already exact from the wall identity and needs no quotient or approximate fold.
- **Returned binary64 heading can enter the withheld corner band.** With W=H=90.31 mm, A=(18.062, 18.062) and B=(27.093, 27.092999976293616), the positive-positive branch qualifies. The exact line from the returned represented direction (0.7071067812307417, 0.7071067811423534) crosses the right wall at a normalized top-end clearance of 9.99999423316998e−11. That is inside the stated withholding band of 1e−10. Recheck both publicly represented directions from their own endpoints.
- **Reported along-wall coordinate can enter the same band.** With W=H=100 mm, A=(21, 24) and B=(28.999999999999996, 24.101265796455678), a qualified positive-positive branch serializes y=99.99999999 at its right-wall contact. The reported represented value has normalized clearance 9.999993721976352e−11. Check the serialized position as well as the exact unfolded crossing.

I independently viewed the A04 Problems bitmap. Its SHA-256 `ec0d4946a67825e5df7df46eb97940864c4217ce38d74f0d3f1352da08d6e4db` matches the frozen source. Solutions stayed unopened. A symbolic rectangle yields the four translated target directions and their conditional reversals without inferred dimensions. For the synthetic numeric control geometry, genuine finite pinned mirrors and opaque targets observed all eight intended journeys, and 29 focused tests passed. The blocker is specific to numerical output qualification beyond those positive controls.

This source requires correction and an exact-head follow-up before integration.
