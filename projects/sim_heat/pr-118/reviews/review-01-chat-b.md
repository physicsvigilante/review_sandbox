# Independent review of the short-duration phase-bath enclosure

**Verdict — accept the correction at `16ec74ec1557154bc9ecae3d53a27f5bb17231ff`.** A separate Codex reviewer subagent with fresh context reviewed the four-file diff against `3afe62a6bc8e3e693a79b54887c08d816f950ba8`. GitHub reported the pinned base and head on the open draft PR. The review covers the offline analytical model. Native execution and classroom validation were outside this review. [Pinned request](https://github.com/physicsvigilante/review_sandbox/blob/119a0df883db9024b9d75c574d5518a4a8c602ce/projects/sim_heat/pr-118/REQUEST.md) · [Source PR](https://github.com/physicsvigilante/sim_heat/pull/118)

### Reproduced precision finding

I ran the original one-second case on both PR 116 head `deb8ed877329a6efe21af7926269bcc300f074df` and this PR's base. Each gave [0, 813151.6293625834] J (upper endpoint rounded here). The reviewed head returns [11068046444225730969001/184467440737095516160, 60] J, a width of 3.24719 × 10⁻¹⁸ J. After 0.1 J has transferred at 60 W, both phase inventories exhaust. For the remaining 599/600 s the rate decays exponentially with rate constant 4/C, where C = 999999999999.1 × 999999999999 J/K. My independent 120-digit calculation integrated the exponential by a six-term alternating series. The reference is about 1.19600333334 × 10⁻²² J below 60 J and lies inside the enclosure.

### Physical bounds and uncertainty

The temperature drive stays constant through the first shared plateau and decreases thereafter. Its initial upper rate times the horizon bounds transferred energy from above, as does equilibrium transfer. Before the slowest admissible link exhausts either phase, its energy equals elapsed time times the lower initial rate. Subsequently at least the first plateau's latent budget has been transferred. The smaller of those two quantities supplies a valid lower endpoint. Bisection still operates on monotone passage time. The exact zero-duration and equal-temperature cases have zero transfer.

I independently advanced the energy with a 110-digit Decimal piecewise forward-time solution through each latent event, integrating constant drive on a shared plateau and exponential relaxation on sensible stages. Both port orders were tested at 0, 0.01, 0.1, 0.25, 1, 3 and 10 s. I used transition temperatures 330 and 300 K, latent heats 30 J/kg, specific heats 7 and 13 J/(kg K), and (donor liquid, receiver solid) inventories of (0.2, 2), (2, 0.2) and (0.2, 0.2) kg. The other initial mass in each bath was 1 kg. I tested 2 W/K exactly and injected a synthetic [1, 4] W/K conductance interval at the link-function boundary, sampling both endpoints and the midpoint. All 168 reference states were enclosed for transferred energy, signed bath energies, temperatures, and both phase masses. On each input I also checked every shared field against the untracked plateau calculation. Fourteen focused repository tests passed, including the missing-specific-heat refusal.

### Pinned CI evidence

Both PR-triggered offline workflows reported success at the reviewed SHA. I downloaded the two archives, independently hashed their ZIP bytes and inspected their contents.

- The series ZIP SHA-256 is `18699bfda29fa7332870da00afaefb6b04ad915f9d7350fd3a5399ccab30690c`. Fresh local execution reproduced every field of archived `phase-short-interval.json`. [Series archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44868242667/artifacts/14691734927)
- The general conduction ZIP SHA-256 is `c57095be54ad358d7fe50098f26e1e2c4cb63abae1e07715b94bd3f42f9967b1`. Its embedded source head matched the reviewed SHA. The decompressed output, oracle results and control results each matched the corresponding pinned held-out JSON data. [General conduction archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44868242699/artifacts/14692529004)
