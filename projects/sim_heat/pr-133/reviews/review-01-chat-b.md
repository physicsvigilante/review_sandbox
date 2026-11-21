# Independent Chat B review of SIM_HEAT PR 133

**Verdict — accept the pinned offline lesson, with one nonblocking regression-coverage finding.** I reviewed the five-file diff from `9b0414cd7bb56150948869cf84785afb3d3e3530` to `d04bc85bcb33660fcc129468f3008a6dc8d1c275` as a fresh Codex reviewer against packet `e7c007fa6ea561dd5df8206bc95fda869225b4d2`. The change composes an existing engine and leaves its numerical method intact. [Source diff](https://github.com/physicsvigilante/sim_heat/compare/9b0414cd7bb56150948869cf84785afb3d3e3530...d04bc85bcb33660fcc129468f3008a6dc8d1c275)

## Physics and interpretation

The source geometry gives conductances of 4, 1 and 3 W/K. Both series halves have conductance 4 W/K, giving 2 W/K per wall. Integrating A's conductivity factor over the temperature rise gives x + x²/320. Forward continuity gives x = 60 K. Reverse continuity gives x = √134400 − 320 K. Substituting x = 100 − m/2 gives the stated reverse-current polynomial. Its derivative is negative throughout the tested magnitude interval [0, 200] W, so the endpoint inequality encloses the physical root.

I ran the pinned lesson and independently checked the reported rational bounds using 100-digit decimal evaluation of the radical. Forward and reverse gave 340 K, +120 W and 326.6060555964672 K, −106.7878888070656 W. Both constant controls gave 330 K and signed rates of +100 W and −100 W. Every checked interval contained its independent value with width below 10⁻¹⁰ in its own units.

The reverse replay releases opposite contact labels. This reproduces the reversed two-terminal current because each wall shares a common conductivity factor across its rods. A retained hot bath supplies heat and a retained cold bath extracts it. On each wall the source-oriented facing, strip and insert report +|Q|, +|Q|/4 and −3|Q|/4 in *both* runs. I checked all 24 rod intervals, eight retained-bath intervals, contact labels and offline flags. A fixed physical probe on a wall whose baths were exchanged would reverse its sign. The lesson explicitly describes the label convention used in its JSON.

## Archive and regression evidence

- Both linked jobs concluded successfully. I downloaded each ZIP, recomputed its SHA-256 and verified its run metadata against the candidate head. The series ZIP was `39c9233488a11ee9b3dca5f81b83e10e09257174a263b0fce27488e3e2b41be7`. Its archived four-case lesson matched fresh local CLI output as parsed JSON. [Series job](https://github.com/physicsvigilante/sim_heat/actions/runs/44874072146/job/136754770647)
- The TwinBridge ZIP was `ff95fb4e6eec35538d60c598b9d1dccbef32a783515241dc1d75ffba4b719fb9`. Its source-head file matched the candidate. Its decompressed output, oracle results and control results matched the preserved held-out JSON at that source. This archive covers the inherited offline replay. [TwinBridge job](https://github.com/physicsvigilante/sim_heat/actions/runs/44874072176/job/136754770609)
- Eight focused joined-conductor, variable-conductivity and network-join tests passed locally. Scope is an illustrative offline exercise. Native execution, native qualification and classroom validation remain outside this evidence.

## Minor finding

The lesson guard checks total current and contact temperature. A reviewer-only mock replaced the left insert's interval with [0, 0] W after every engine call. All four lesson guards still passed. The genuine archive and fresh execution give the correct signed branch shares. A regression check on signed rod shares would protect the answer to the exercise's branch question. [Replay guard](https://github.com/physicsvigilante/sim_heat/blob/d04bc85bcb33660fcc129468f3008a6dc8d1c275/tools/wall_reversal_lesson.py#L17-L33)

The source PR remains for the owner's separate merge decision.
