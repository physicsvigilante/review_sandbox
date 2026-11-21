# Chat B review of SIM_HEAT #121

**Accept for the offline supported phase-bath scope.** I found no blocking physics or evidence issues in the changes from `e590b32e61cf749ae81383e07bc5a082e5149c08` to `c914a4da93ecb6eafe70176ff0d12fcd9a0f4dd3`. I performed the review as a separate Codex reviewer subagent. The evidence covers steady conduction, a single radiating face, fixed support temperatures and a finite bath up to first phase depletion. Native qualification and educational validation remain outside this verdict. [Pinned request](https://github.com/physicsvigilante/review_sandbox/blob/5742b47d519aea3159d0634a5ce2271a436c1575/projects/sim_heat/pr-121/REQUEST.md) · [Source diff](https://github.com/physicsvigilante/sim_heat/compare/e590b32e61cf749ae81383e07bc5a082e5149c08...c914a4da93ecb6eafe70176ff0d12fcd9a0f4dd3)

## Independent four-terminal calculation

I used the joined six-rod network, with bath middleR at 310 K, radiating face coolL, and two maintained supports warmL and coolR at 380 and 280 K. The area was 0.8 m², emissivity 0.75, and radiation constant 0.0000000567 W/(m² K⁴). Initial solid and liquid inventories were 0.02 and 0.03 kg at 200000 J/kg. From the six physical rod endpoints, for face temperature T I used junction temperatures J2 = [3(760 + 5T) + 10(0.6 × 310 + 280)]/37 and J1 = (760 + 5T + 3J2)/10. I solved the signed surface balance at 100 decimal digits and evaluated the bath and both supports directly from adjacent rods. [Source network](https://github.com/physicsvigilante/sim_heat/blob/c914a4da93ecb6eafe70176ff0d12fcd9a0f4dd3/studies/joined_terminals/model.mo)

| Enclosure K | Face K | Into bath W | Into warmL W | Into coolR W | Into enclosure W |
|---:|---:|---:|---:|---:|---:|
| 160 | 268.248319 | -53.209868 | -161.961549 | 61.316886 | 153.854531 |
| 500 | 484.291237 | -0.658888 | 106.632348 | 148.901853 | -254.875312 |
| 600 | 584.286033 | 23.664170 | 230.950203 | 189.440284 | -444.054657 |

All four signed rates sum to zero within 1e-85 W in the independent calculation. The returned intervals enclosed the independent face temperatures, each heat rate, depletion times and clipped latent energies, with widths below 1e-10 in the respective units. All three cases still had both phases at 1 s and had exhausted the expected phase at 10000 s. At 500 K the enclosure supplies the network while the bath freezes. The two supports jointly absorb more power than the enclosure supplies.

## Refusals and compatibility

A fresh near-cancellation test on the pinned star, with bath middle at 316.745947807105612415 K, face warm, enclosure 420 K, unit area and emissivity and the same radiation constant, raised `latent heat-flow direction is unresolved`. I chose the decimal by solving for zero bath flow independently. The supported-bath, two-terminal radiating-wall, surface, latent-bath and bath-target suites passed locally (14 tests). They cover missing, shared and unknown faces, missing exterior, exact equilibrium, and exchanging the two-terminal bath orientation. The candidate keeps explicit signed reservoir rows and clips phase conversion at the first exhausted inventory.

## CI evidence

Both GitHub runs reported success at the reviewed head. I downloaded both archives and hashed the zip bytes. The six-file wall archive had SHA-256 `2c799d255b9d447c5a05f37228a71333f39ce9097016838997134b4fda8010fb`. Both supported freezing and melting JSON objects matched fresh local executions field for field, including the offline provenance flags. [Wall run](https://github.com/physicsvigilante/sim_heat/actions/runs/44869101229)

The four-file TwinBridge archive had SHA-256 `a9332e5dbddd5bbbd9e894fb13ca1f9ba263f442b8a8f11f9774bbaf308e1c1e`. Its recorded source head matched. Its decompressed trace, oracle results and seven refusal/control results matched the pinned historical JSON. This checks preservation of earlier evidence. The four-terminal calculation above exercises the new physics. [TwinBridge run](https://github.com/physicsvigilante/sim_heat/actions/runs/44869101269)
