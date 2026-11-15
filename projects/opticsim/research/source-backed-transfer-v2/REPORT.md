# Opticsim — current-main source-backed transfer and native ray-lineage feasibility

**Research status: verified test-only; draft PR #79 deliberately unmerged.** This is a same-assistant feasibility/replay record, **not** a new independently authored Chat B review, physics-engine certification, held-out model score or teacher study.

- Source main baseline: `physicsvigilante/opticsim` at `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`.
- Research-only [draft PR #79](https://github.com/physicsvigilante/opticsim/pull/79), corrected head `ab0285940878eb30625605754e7a90847d574286`.
- GitHub merge-test checkout `8156339a1dc4352c152a130f612795ea4f5cab3a`: same research tree, parent existing main + corrected head; no production `src/`, PhyDemo pin, numerical budget or scene-schema modification.
- [Corrected unified CI 43726325138](https://github.com/physicsvigilante/opticsim/actions/runs/43726325138): supported **Node 24.19.0**, **729/729 Node tests** (0 failure/skips/cancelled), public replay and lineage probe completed; all **11/11 corrected-head GitHub PR workflows passed**. Existing Chrome checks passed in ordinary workflow; no new reviewer-driven browser acceptance.
- **Corrected replay/lineage evidence:** GitHub artifact `14166447261`, verified ZIP SHA-256 `0bdb0bf0686afe4bbf066ed73dd0c15ae359ea4ec4d7e4ae624872db57823f6d`, 44 entries inspected. Old first-run partial artifact `14166173017`, SHA-256 `74cb15309c2f455b8849e8704eedf40c1cfe9e21cfec79ab04bdba526acc9064`, retained with the actual test-harness failure.

## Exact-frozen public request replay

Original 2026-11-15 selection was frozen **before viewing six Problems images**. Image archive hash `03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939`; pre-image selection hash `e26b38854d0bf2bddf3dbf22d6bcd40bce41e5f3413813289ff0a50c27a96d77`. All eight original public JSON byte strings (T1–T6 plus separate two teaching analogues C1R2 and C2R) were reconstituted and *all eight hashes verified against preexecution frozen values*, then all eight raw input files checked again in the downloaded CI artifact. No Solutions opened; no change to source interpretations.

| Original case | Current-main public result | Native calls |
|---|---|---:|
| T1 repeated ideal-plane-mirror virtual-image enumeration | unavailable | 0 |
| T2 plate/convex-mirror image coincidence | unavailable | 0 |
| T3 pole-in-lake shadow | Snell-only conditional sub-result **32.02776011381499°**; requested continuous shadow unavailable | 0 |
| T4 four-layer refraction | existing conditional branches **40.54160187350451°**, **26.633118749155926°** — **already exposed B06 control**, exclude from unfamiliar denominator | 0 |
| T5 silvered-prism retrace inverse | unavailable | 0 |
| T6 material slab and lens symbolic inverse | unavailable | 0 |

**Eligible original full-task coverage = 0/5**; one eligible case, T3, has one conditional angular sub-result. The exposed T4 is not relabeled unfamiliar. Every original input lacks a validated complete authoring scene and was withheld from native execution rather than assigned invented dimensions, brightness or routing. Do not infer general unfamiliar problem success from these five cases; source interpretation remains same-assistant and unreviewed by separate subject-matter evaluators.

**Separate fully specified synthetic teaching analogues** both completed using actual pinned PhyDemo: C1R2 had one emitted ray and four real mirror reflections (5 processed segments); C2R had one native 32.027760113815° water refraction and one actual downstream detector crossing (3 processed segments), all zero truncation and undefined behavior. The existing qualified-scene edit of water index `4/3→1.5` yielded **28.1255057020557°** while retaining original provenance and recording a hypothetical physical edit. These are *not* original task answers or a continuous shadow.

## Test-only native ray identity and direct-child observation

The research-only wrappers delegate once to actual `onSimulationStart` and `onRayIncident`, recording `WeakMap` identity tokens for emitted native ray objects and any distinct `newRays` actually returned from a parent interaction; not a new source attribution claim or ray tracer.

- A single object was observed at **four successive native mirror interactions** with unchanged identity; baseline uninstrumented and observed simulator both processed **5** segments.
- Two **separate** explicit native single rays encountered the same planar interface and produced two directly observed Fresnel-reflected child objects. Both children subsequently hit a reflected-ray detector, while both transmitted original objects hit a second detector. **2 source emissions, 2 interface interactions, 2 children, 2 upper + 2 lower detector crossings**, with expected parent identity and original source linkage *within this test*. Instrumented and baseline runs processed **10** segments. No unknown/duplicate object references, truncation or undefined behavior.
- `rayIndex` is a simulator-array index, **not** a safe semantic source identity. The test-only tokens are not durable native path IDs.

Unverified: near-TIR/critical, merged surfaces/corners, weak truncated branches, multiple dense fans, stoppage, all browser races, missing primary emission callbacks, branch consistency through arbitrary systems. Nothing establishes continuous irradiance, detected images, automatic original-text interpretation or general path reliability.

## Failure transparency and release decision

First [research CI 43726148526](https://github.com/physicsvigilante/opticsim/actions/runs/43726148526) completed the exact-frozen replay but failed its **test-only lineage harness** before native assertions because it read authoring `components` as canonical `physics.components`. This specific one-line helper was corrected in the second research commit; the initial failure and partial artifact are preserved. The corrected run passed every workflow without any production or original-input change.

**Do not merge this research PR.** It temporarily modifies the unified CI workflow solely to emit replay/feasibility artifacts, and does not propose a production ray-lineage API. If the owner later selects a bounded source/branch event observation, it must be a separate **R2** source/evidence-semantics milestone with fresh native counterexamples, full CI and a Chat B review packet in this central hub. Do not add special-case textbook handlers to compensate for the 0/5 unsupported original tasks.

This entry belongs in the hub's **research/ record**; it is **not** a `reviews/review-01-chat-b.md` file and must not be presented as a second ChatGPT's findings.
