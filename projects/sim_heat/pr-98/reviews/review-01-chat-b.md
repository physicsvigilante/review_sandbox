# Chat B review of steady networks sharing two ideal contacts

**Verdict — accept for the bounded offline calculation.** No blocking findings. Reviewed [PR 98](https://github.com/physicsvigilante/sim_heat/pull/98) at head `039a686eb76deff90350fe284ec5fedd54b511dc` against its verified parent `a192da4d8d79b1fa39c8a5b81d86a7d34368f17d` under the [pinned R2 request](https://github.com/physicsvigilante/review_sandbox/blob/040e69cadf97b4328ed0768e638e70fa37fce226/projects/sim_heat/pr-98/REQUEST.md).

## Physical result and independent challenge

Joining the named pairs gives each contact a common temperature and zero combined supply. With external temperatures held, the two contact rows therefore solve a grounded 2-by-2 system. Substitution of those temperatures into each external row gives the Schur complement. Source inspection confirms both off-diagonal terms enter the determinant and that division requires a strictly positive determinant enclosure. Shifting all temperatures by the same constant leaves rod flows invariant, which justifies using differences from the coldest maintained boundary.

I independently transcribed the star's three conductances (2, 3, 5 W/K) and triangle edges (warm–middle 3/5, warm–cool 1, middle–cool 3/2 W/K) from their Modelica inputs. For every ordered pair selection on each side (6 × 6), I stamped the six rods into a five-node Laplacian and solved all three interior rows directly by exact rational Gaussian elimination. Two unit excitations gave both external response columns. A separate solve used the maintained bath temperatures. For all 36 pairings, each of four coefficients, both contact temperatures and both signed supplies enclosed its exact value, with interval widths below 1e-12 in the respective units.

- Authored arrangement, from warm to cool: conductance 1230/1261 W/K, contact temperatures 401680/1261 and 402680/1261 K, external supplies +123000/1261 and −123000/1261 W. The explicitly connected six-rod solution agrees at both junctions and reservoirs in the focused test.
- Challenge connecting left warm to right cool and left middle to right middle: conductance 410/427 W/K, contact temperatures 19680/61 and 134760/427 K, supplies −41000/427 W on left cool and +41000/427 W on right warm. The sign changes with the maintained bath assignment.
- A two-terminal composite wall joined at both ends to the triangle left one maintained terminal. Both contacts returned exactly 280 K and the remaining reservoir supplied exactly zero watts.

## Refusals and provenance

The three focused tests passed locally with the designated interpreter. They include left-side duplicate and unknown ports, contact-order reversal and lack of an external anchor. Additional calls refused a duplicate right port, an unknown right port, a one-element contact pair and a deliberately incorrect right-side facts digest. I recomputed the six source hashes in the archived composed law from the pinned study, model and facts bytes on both sides. The local full-model replay used the request's workflow facts pin and the generic conduction input checks.

## Exact-head CI and archived replay

Both Actions jobs succeeded on the reviewed SHA. I downloaded both archives, recomputed the requested digests and checked all member CRCs. The study archive contained 32 entries and the general archive four. Fresh composed-law and six-rod direct outputs each matched their entire decoded archived JSON record. Both records carry false values for native execution, native qualification, independent reference certification and runner consumption.

- [Study job](https://github.com/physicsvigilante/sim_heat/actions/runs/44863297643/job/136721286150), [archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44863297643/artifacts/14690558650), SHA-256 `2a87eb474bfba026a239e776938021383afef43b67117fc8313a246329d320e1`.
- [General conduction job](https://github.com/physicsvigilante/sim_heat/actions/runs/44863297641/job/136721286073), [archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44863297641/artifacts/14690302760), SHA-256 `ec97485f598851f564417037f6ee0b92c5957ad26c2093f96f0ba84e279b1161`.

The same-author full-model replay establishes consistency with the authored assembly. The separate rational calculation supplies the independent numerical check for the examined arrangements. This review covers steady, storage-free ideal contacts. Native OpenModelica behavior, classroom outcomes and C1 external authoring remain outside the evidence. The source PR remains for owner disposition.
