# Opticsim PR #195 — FINAL BUILDER VERIFICATION and ONE focused independent v27 review

**20 November 2026, 17:xx IST. BUILDER VERIFICATION, NOT independent physics clearance or a JEE solved-problem score.** This is the **one final review** requested for a combined, reusable versioned native engine capability and its pre-frozen test-only feasibility. [Draft PR #195](https://github.com/physicsvigilante/opticsim/pull/195) stays draft/unmerged until a committed independent review on the exact unchanged source and standing owner release decision.

## 1. Source, ancestry, frozen protocol, and isolation

- Exact final CI-tested PR source HEAD: **`e7e2d199b6be25265decb6f7ec7826a3477ab24f`**; Git tree **`83e3dc418784c9c233267527b0e0dd99576899a5`**.
- GitHub synthetic PR merge commit **`3194bb332531a37950b6c6d6634951f4b1513e8c`** has **the same Git tree `83e3dc418784c9c233267527b0e0dd99576899a5`**, ordered parents [production reviewed v26 `main` `4f81a1625cc45ce731d3ee0e286ff3173f72f4fe`, final feature HEAD `e7e2d199b6be25265decb6f7ec7826a3477ab24f`]. Production main was read back and remained `4f81a1625cc45ce731d3ee0e286ff3173f72f4fe`.
- The **11-case research/source protocol** was committed **before actual native experiment** in `research/native-parallel-two-plane-mirror-v27/frozen-protocol.json` at `e3f18c39bc83cae77d86d8c2e672c2411442627b`. Protocol Git blob **`9ac5a79bbdc945b01c1e969964ebe4231c0aeb8d`** is byte-identical at final HEAD.
- Pinned native upstream PhyDemo `811f508d2b070898c241a568b0c167dcb8645251` is **unchanged**. No native optical propagation kernel, source profile v19/v26, ray events, existing detector retention cap, old source benchmarks/answers or previous reviews were modified.
- Base-to-HEAD diff has **15 changed files: 9 added and 6 modified**. Added: research protocol, research README, v27 documentation, explicit native example, public v27 validator, raw pinned-native research test, public v27 Node test, public JSON qualification script, and real Chrome acceptance script. Modified only: public profile registry, versioned contract, LLM authoring capability metadata, 2 historical catalog count tests, and optical-composition CI workflow. The old **32 profiles v1–v26 remain**; exactly one **v27** is added. Old v19/v26 saves do not silently acquire a second plane+mirror.
- The historical review of v26 PR #194 identified a **real half-integer native Beam sampling omission**. Its separately independently reviewed correction at `3564886de1372e4f9d74bb771f90f87a8944dd75` is already merged in production. v27 imports that exact-native-sampling helper unchanged, including the conservative 1e-10 half-integer withholding rule. **Do not re-review the whole upstream v26 physics; verify the correct reuse within v27.**

## 2. Reusable public engine composition, with strict physical scope

v19 already supports a finite native `Beam` and **two** `PlaneGlass` interfaces without a mirror. v26 supports a finite native `Beam`, **one** `PlaneGlass` and **one** finite mirror. v27 fills their intersection: a fully authorable finite Beam crosses **two genuine planar refractions** through a homogeneous slab, reflects on an independently finite mirror strictly **beyond** the slab, and returns through both surfaces. Actual source emission, hits, reflected rays and detector observations come **only** from unchanged pinned PhyDemo, not an algorithmic ray-path reconstruction.

Public schema 27 `native-parallel-slab-mirror-tracing` admits **exactly** one deterministic finite `parallel-beam`, exactly two vertical `planar-interface` objects (normalDeg=0), exactly one vertical finite `plane-mirror`, and **zero or one** passive source-side `ray-detector`. Entire Beam starts on negative/source side and travels positive x, 0–60 degrees; width 10–100 mm, ray density .048–1, brightness no more than density, 1–100 actual emitted samples, finite authored coordinates. First interface negative/positive indices and second positive/negative indices are authored separately but must represent the *same* exterior index and a single slab index greater than/equal to exterior, all within existing absolute [1,4] index bound. Both interfaces **require** `partialReflection:false`: a transmitted-only Fresnel approximation, **not full Fresnel power or branch completeness**. Pinned native TIR itself remains enabled. No arbitrary third medium, tilted mirror, extra glass/lens/stop, reverse source, 3D optics, calibrated irradiance or optical image reconstruction.

**The mirror does NOT touch the slab.** Slab thickness must be >=1 mm; mirror must be at least **1 mm beyond the second interface**. A Mirror at x=the rear interface, or smaller than 1-mm separation, is refused before native. Every exact native emitter sample is screened with a separate necessary Snell geometry calculation for finite positive/return checkpoints, finite mirror first encounter >0.1 mm inside both mirror endpoints and finite detector endpoint clearance >0.1 mm. This witness only checks *authorability*; it never writes light paths into native scene objects or treats predictions as observed rays. Native incomplete/stopped/undefined/stale errors suppress all qualified observable results. Above **32 actual detector crossings**, the full hit-position list is withheld, not clipped, while genuine complete counts may still be measured.

**Important JEE provenance:** Original JEE J08's mirror **rests directly on the plate** and the prior source audit did not establish a numeric exterior index or source apparatus. v27's baseline adds an explicitly **synthetic 30-mm gap** beyond the slab and explicitly authored index pair 1/1.5. Therefore **v27 is not a source-complete or answer-certified simulation of J08**. It expands reusable teaching-engine composability without inflating the frozen 20-case JEE solved score.

## 3. Raw native geometry and genuinely observed evidence

Predeclared synthetic baseline: native Beam center (−100,0) mm, width 40 mm, direction +30 degrees, relative brightness .08 and density .2. Front Glass x=0, n0=1→n1=1.5; back Glass x=60, n1=1.5→n0=1; finite vertical native Mirror at x=90 (30-mm third-medium gap), length 420 mm; passive Detector x=−10 mm. No optical path generated outside native PhyDemo.

Independent *paper* Snell/specular relationships for this extra synthetic geometry:
```
r = asin((1/1.5)*sin(30deg)) = 19.47122063449069deg
front-surface return lateral shift =
  2*60*tan(r) + 2*30*tan(30deg) ≈ 77.06742302257038mm
source-side detector inbound/return spacing adds 2*10*tan(30deg)
  ≈ 88.6144284063629mm
```
These are necessary geometry checks, not source ancestry, a detector image or any native steering.

Actual final-source [Optical composition workflow 44730867302](https://github.com/physicsvigilante/opticsim/actions/runs/44730867302) native log and archived raw ten-plus cases:
| Test-only raw control | Emissions | Plane 1 encounters | Plane 2 encounters | Mirror | Detector | Qualification |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Baseline/translated/normal/higher slab index | 8 each | 16 | 16 | 8 | 16 | Raw native complete, zero truncation |
| Denser Beam | 16 | 32 | 32 | 16 | 32 | Raw native complete, zero truncation |
| Mirror absent | 8 | 8 | 8 | 0 | 8 | Real native no-return control |
| Mirror **coincident with rear Glass** | 8 | 16 | **0** | 8 | 16 | Raw `simulationComplete` but **wrong intended physical route — unqualified** |
| Mirror gap **0.005 mm** | 8 | 16 | 16 | 8 | 16 | Explicitly unqualified near-contact |
| Raw Fresnel-on first Glass | 8 | 16 | 24 | 16 | 24 | Incomplete, truncation **0.1265077484007037** |
| Native ray-depth 0 | 8 | 0 | 0 | 0 | 0 | Incomplete with truncation |
| Processing limit 1 | 8 | 0 | 0 | 0 | 2 | Native `simulationStop` |

The frozen protocol remains unchanged. The raw v19 two-plane+Detector canonical scene is cloned *only in the test* to append a real native Mirror and record actual pinned callback points; these raw clones are never claimed to be qualified public v19 or v27 scenes. Actual native Mirror specular direction check is included.

## 4. Additional late negative-control discovery and safety correction

After the initial final-green candidate at `148cb54390e92c89fcdc403a26f786d50253a850` (1,138 Node tests), an **additional test** found that putting **two source-side passive detectors** on both inbound and return paths causes **nine actual native optical interactions per ray**: Detector2 → Detector1 → Plane1 → Plane2 → Mirror → Plane2 → Plane1 → Detector1 → Detector2. The v27 native depth policy is **8**, so that six-object scene reports **incomplete**, not fully qualified sampled return. An earlier test *incorrectly expected complete* and failed CI on the intermediate source `4b454aea2d68079d7a55f9bb203ff73a1dab6c4a`; it was **not** treated as a successful release.

The **final** v27 profile was deliberately **narrowed to 0–1 passive detector** (still not widening native depth or changing old profiles). Two-detector scenes are explicitly refused **before native**. A separate marked **RAW test-only six-object clone** positively reproduces real PhyDemo depth-eight truncation and is never used to qualify or export a public scene. A newly added **exact 1-mm mirror-gap positive** verifies both real Glass interfaces on each trip; 0, .005, .5 and .999999999-mm gaps fail authoring. The final Node test positively verifies **0 and 1 detector complete; 2 detectors rejected**. These extra safety tests are **not a modification to the frozen original research matrix**.

The research README was also corrected to distinguish its initially test-only status from the later same-PR public candidate. This is an explicit chronology, not a first-attempt clean-success claim.

## 5. Final exact-head CI, public authoring and actual Chrome

**11/11 exact final-HEAD GitHub workflows PASS** on `e7e2d199b6be25265decb6f7ec7826a3477ab24f`; actual Node24 logs from run [44730867302](https://github.com/physicsvigilante/opticsim/actions/runs/44730867302), job **136269957233**, record **1,141 passed / 0 failed / 0 skipped**, including the additional v27 exact-minimum-gap, 0/1 detector and 2-detector raw incompleteness tests.

- Curved mirror checks: run 44730867372 — success
- Qualified authoring checks: run 44730867290 — success
- Planar refraction checks: run 44730867578 — success
- Optical composition checks: run 44730867302 — success
- Original refraction problem pair: run 44730867373 — success
- Parameter experiment checks: run 44730867283 — success
- Quasi-static source motion checks: run 44730867338 — success
- Numerical ray reliability diagnostics: run 44730867348 — success
- Deterministic planar angular query checks: run 44730867419 — success
- Unified problem workflow checks: run 44730867346 — success
- Plane-mirror angular inverse checks: run 44730867378 — success

The ordinary public `scripts/native-two-plane-mirror-v27-acceptance.mjs` actually passed: **4 native completed / 5 refused before native**. Baseline qualified results: **8 Beam emissions, 16 front surface contacts, 16 rear surface contacts, 8 native Mirror reflections, 16 detector crossings and 16 recorded hit events**. Input bytes are preserved and SHA-hashed; qualified portable bundle does not store cached ray results. Refused controls: mirror in direct contact, near-contact, second-face Fresnel-on, inconsistent third medium, and missing exterior index.

A **real Chrome** v27 import/edit/export/reopen run passed **10 checks with 6 screenshot files**. It verified loading the qualified public v27 scene, native counts, Beam-width edit, *invalid* change of one slab material parameter only, then a valid coherent change of **both** slab interface indices, qualified save, explicit direct-contact mirror refusal, clipped short-mirror refusal and reopening the portable saved scene with actual retraced counts. The browser did NOT draw fake rays or run any external model request. This is **builder CI execution**, not an independent reviewer-run Chrome session.

The full set of older pinned-native and Chrome regression workflows also passed. The source and synthetic merge commits have identical Git trees; reviewed v26 has 11/11 postmerge green workflows. No source JEE answer-completeness scores, upstream pin, 32-hit limit or existing saved formats were rewritten.

## 6. Artifact integrity boundaries and independent review instructions

Exact final optical run `44730867302` uploaded:
- `llm-authoring-evidence` artifact ID `14626013257`, GitHub-declared SHA-256 `6cac155eec6cce37082581c510c7abdbc8ed23c378d5054af3edbbcc94e5b882`.
- `opaque-blocker-evidence` artifact ID `14626143133`, declared SHA-256 `3ed3beb32276a572c8cdacfd9d36c30b283c70604a1bf7998082cf751c43d651` (also contains new v27 Chrome report/screenshots).
- `browser-acceptance-evidence` ID `14627065075`, declared SHA-256 `08d5fb0b87e27fff41068117043b922c76878b44bc9be9aaa512caca790dbbfa`.
- `hosted-browser-evidence` ID `14626486698`, declared SHA-256 `7a5710036eb8a6e41ba996b8afe3d998c944a55036c9e0d11494fb2a0dec6652`.

**Integrity limit:** builder read official GitHub artifact digest metadata and actual CI/job logs; builder did **not independently download/re-hash final ZIP bytes or internal saved members**. Reviewer should independently inspect exact raw native input/report hashes and 11 frozen controls, public 9-case JSON/qualified evidence, source and screenshot files, and compute ZIP SHA-256 when possible. Distinguish reviewer-recomputed evidence from builder logs.

### ONE focused independent Chat B review due

Review **the combined v27 capability as one release**, not the prior test-only feasibility as another review. Inspect:

1. Exact source HEAD `e7e2d199b6be25265decb6f7ec7826a3477ab24f`, tree `83e3dc418784c9c233267527b0e0dd99576899a5`, synthetic merge `3194bb332531a37950b6c6d6634951f4b1513e8c`, frozen protocol blob and final 15-file diff. Confirm the original 32 profiles v1–v26 are unchanged and v27 cannot be silently downgraded to v19/v26.
2. Independently derive two-interface Snell/reflection/return cross-section, review signed geometry and actual pinned native callback order for baseline and negative controls; in particular **coincident Mirror giving ZERO rear-glass callbacks despite `simulationComplete`**, which must always refuse.
3. Confirm **v26 B1 exact emission-sampling reused unchanged**, all emitted samples/rim/finite-side checks, one-millimeter gap guard, material/index match, no Fresnel-on, no extra optics, true *source-side* detector constraints and detector endpoint margin.
4. Independently scrutinize **the detector-depth issue**: verify 0–1 passive detector public profile, raw six-object nine-event depth-eight truncation and pre-native refusal of 2 detectors; do NOT merely assume 0–2 based on prior v26 capabilities. Check stopped/incomplete/stale suppression, >32-hit whole-position withholding and qualification integrity.
5. Audit actual public JSON→native→qualified save, Chrome 10 checks/six screenshots and archived source-bound event members, including independent ZIP/input/manifest hashes as accessible. Note what was independently calculated or executed vs builder's original real Chrome/Node traces.

**Do NOT** re-review the independently cleared native Beam/PlaneGlass/Mirror optical algorithms, v26 physics correction, previous JEE J08 source/answers, J11 escape disc or older optics libraries. The goal is **new v27 numerical-safety, authoring composition and exact native evidence**, preserving one focused review per completed capability.

**Mandatory deliverable:** commit a complete independent Markdown report to `physicsvigilante/review_sandbox` default branch:

`projects/opticsim/pr-195/reviews/review-01-chat-b.md`

Include exact reviewed HEAD **`e7e2d199b6be25265decb6f7ec7826a3477ab24f`**, Git tree **`83e3dc418784c9c233267527b0e0dd99576899a5`**, synthetic merge **`3194bb332531a37950b6c6d6634951f4b1513e8c`**, actual source/frozen protocol, observations, any physics/integration blockers and explicit verdict **CLEARED FOR OWNER DECISION** or **CHANGES REQUESTED**. Read back the committed report; return its immutable link and review commit SHA. A chat-only verdict does NOT satisfy the gate. **Reviewer must NOT edit/merge/deploy Opticsim source or rewrite JEE evaluations.**

**Release HOLD:** PR #195 remains DRAFT/UNMERGED until this independent report has been published, checked against the exact unchanged source and cleared. Then the standing owner release gate applies, followed by post-merge CI on the actual production commit.
