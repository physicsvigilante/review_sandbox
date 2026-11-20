# Opticsim PR #192 — FINAL BUILDER VERIFICATION and ONE focused Chat B review instructions

**20 November 2026 (IST)** — builder-side verified **source-bound JEE J08 mirror-backed slab** analytical model and a *separate* authorable genuinely-native synthetic illustration. **NOT independent physics review, JEE original solved-question scoring, a new native solver or release authorization.** [Draft PR #192](https://github.com/physicsvigilante/opticsim/pull/192) stays unmerged until one focused independent review applies to the exact unchanged candidate.

## 1. Exact final tree, source freeze and CI

- Final tested PR source commit **`b4eef0bf4be2ad46eb007573ff994e14e147d595`**, source Git tree **`cb7b75df5ac4a2e4e6b1dc7283887da49135db47`**.
- GitHub synthetic merge **`60ea446db3ffcdadf999a4716bd62c85358ae2fd`**, same Git tree **`cb7b75df5ac4a2e4e6b1dc7283887da49135db47`**, parents [production main `cf0366d2b46a0cb88e97bc8d9ec94a29e556ed83`, exact PR head `b4eef0bf4be2ad46eb007573ff994e14e147d595`]; no unreviewed source composition or base drift.
- Stable production `main` `cf0366d2b46a0cb88e97bc8d9ec94a29e556ed83`, independently reviewed J02 release with **11/11 post-merge workflows passed**. Main has not been changed by this PR.
- Frozen source/physics/7-case protocol committed BEFORE model/native tests at **`20f0a67a348c554c4d5ede4cc6aa882e05469e6c`**, blob `40187325c1b05a4c96880f7b4e59290aa9af1149`, identical in final tested source tree.
- Pinned unmodified PhyDemo **`811f508d2b070898c241a568b0c167dcb8645251`**. No existing engine, native physical algorithm, canonical schema/profile, workflow, renderer, old tests or historical JEE source attempts changed.
- GitHub compare: **11 added files only** — frozen J08 protocol, source-only/synthetic-index/native authorable JSON examples, pure analysis `src/mirror-backed-slab-displacement.js`, raw-byte CLI `scripts/mirror-backed-slab-query.mjs`, three J08 tests (analysis, raw native, complete public authoring), J02 nonblocking centroid regression and J08 documentation.

## 2. Original JEE J08 source-fact boundary — reviewer must inspect original Problems PNG

- Original J08 held source-audit record: `evaluation/jee-post164-coverage-v1/source-review.json` at held PR #165 source commit `6a72bd67e58e9a3fd94a6bf33d88d1f20295b4c2`. Historical source image `08_Ray_Optics_Explanations/03_General_Refraction/Problems/006.png`. The auditor reported plate refractive index **1.8**, thickness **6 cm**, **resting on a plane mirror**, external incident angle **60° from normal**, and asks separation between front-face entry and eventual exit after mirror reflection.
- Crucial source audit limitation: **no numeric exterior refractive index**; no finite plate/mirror extents, source launch coordinates/brightness, detector, sampling/partial-reflection policy. Source archive originally `08_Ray_Optics_Explanations.zip`, historical SHA-256 `03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939`; historical source-image artifact **14454755556** from run **44360693719**. No Solutions file was opened by builder.
- Reviewer: independently inspect **only the original Problems PNG**, confirm the geometry and whether the source states the exterior medium anywhere (including figure words), and do NOT infer numeric n=1 from a convention, numerical textbook result, diagram scale or imagined "air" fact.
- Standalone input `examples/jee-j08-mirror-backed-slab-source-only-v1.json` deliberately omits `outsideIndex`; the API reports **`needs-information`**, code `MISSING_OUTSIDE_INDEX`, `value:null`, `native:not-run`. **It does not make a numeric original-answer claim.**

## 3. Independent conditional Snell/specular physics review target

For a plane-parallel plate of thickness t, front face at x=0 (normal +x into material), ideal specular mirror immediately backing slab at x=t, positive-y incident angle i, explicit absolute exterior index n0 and plate index n1:

```
n0*sin(i) = n1*sin(r)
D = 2*t*tan(r)
  = 2*t*n0*sin(i)/sqrt(n1^2 - (n0*sin(i))^2)
outgoing exterior direction relative to +x = 180deg - i.
```

The two separate traversals inside plate contribute `t*tan(r)` each to **front-surface entry-to-exit** displacement D. On the synthetic **explicitly added** exterior index n0=1, n1=1.8, t=60 mm, i=60°, the conditional r is **28.7589180039507°**, D is **65.85855599381419 mm = 6.58585559938142 cm**. This is **not** the original source's unconditional numeric answer: outside index=1 is an additional teaching choice.

The pure `src/mirror-backed-slab-displacement.js` requires strict format/kind/model/branch/coordinate convention/units, thickness [1,10000] mm, indices [1,4], and incidence [0,89] degrees. It refuses unknown/malformed fields, unsupported apparatus/claims, native-readout assertions, excessive/unbounded displacement and nonfinite numbers. For absent n0, answer `needs-information`. For n0*sin(i)>n1 with a sufficient margin, TIR makes the requested transmitted mirror return **unavailable**. Within 1e−7 of critical sine ratio, outcome **numerically-indeterminate** (not guessed exact critical ray). A reflected exit without entry propagation is never synthesized. This is an engineering numerical cutoff, not a proven universal floating-point error envelope.

Independently compare the model against scalar Snell and specular geometry for unit changes, equal index, normal incidence, doubling thickness, high-to-low index, near critical and actual declared `n0=1.33`. The standalone model never runs native rays or creates a scene; **its `native.status` stays `not-run`**.

## 4. Genuine pinned-native and public v5 evidence — separate from source facts

The new **synthetic fully authored** public native scene `examples/jee-j08-mirror-backed-slab-native-v1.json` uses existing canonical **v5** with actual native **SingleRay, PlaneGlass, Mirror, Detector**, with explicit extra exterior index=1, finite 420-mm mirror and detector, source launch position and brightness .08, front boundary x=0, mirror x=60 mm and detector x=−10 mm. `partialReflection:false` explicitly **omits Fresnel partial reflections** but retains native TIR; this is not full light power/radiometry.

Test-only raw `test/jee-j08-slab-native-witness.test.mjs` wraps genuine pinned methods and delegates once, records actual real incident and outgoing directions/points. Actual exact-head CI on [run 44693880613](https://github.com/physicsvigilante/opticsim/actions/runs/44693880613) logs:

| Synthetic native case | Real callback sequence | Native classification |
| --- | --- | --- |
| n0=1/n1=1.8, t=60 mm | Detector → entry PlaneGlass → Mirror → exit PlaneGlass → Detector | **completed, truncation 0** |
| Translated | identical event order | **completed** |
| Explicit exterior n0=1.33 | identical event order, changed refraction/hit coordinate | **completed** |
| Half thickness 30 mm | identical order, half front-face displacement | **completed** |
| Normal incidence | identical order, zero front-face displacement | **completed** |
| Removed mirror | Detector → single PlaneGlass entry, **no return** | **completed no-return** |
| Native max depth 0 | no completed path | **incomplete, truncation 0.08** |
| Processed-ray limit 1 | Detector → PlaneGlass partial | **stopped**, no qualified return |

The baseline real native entry and exit at x=0 are 65.85855599381419 mm apart in y, matching independent conditional analytic D. The mirror reflection occurs at x=60 and at half that y-shift. **This is actual native evidence in an explicitly completed synthetic apparatus, NOT a source-complete JEE run or detected image.**

`test/jee-j08-slab-public-native.test.mjs` independently uses existing **`prepareScene` → `evaluateDocument` → `evaluateObservables`** on the explicit native example. It returns completed, **qualified** (transmitted-only disclosed) results for **2 real glass interactions**, **1 real mirror reflection**, **2 detector crossings**, and both actual detector hit positions/directions. Detector x=−10 is not on the slab surface: its inbound/outbound **detector hit spacing** is **`D+20*tan(i)`**, *not* D. The test checks this distinction, invalid missing exterior material, no-mirror behavior and stale-hash suppression. There is no custom ray steering, image reconstruction, native schema change or new J08-specific Chrome scene test.

## 5. J02 reviewer recommendation without second full physics review

In [Chat B's independent review of PR #191](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-191/reviews/review-01-chat-b.md), nonblocking item N1 requests exact centroid/on-median and nearly symmetric object numerical controls for the earlier formal equilateral three-mirror orbit. This candidate adds only `test/jee-j02-centroid-median-review-followup.test.mjs` using the **unchanged independently reviewed J02 module**. CI confirms the nonzero formal translation for those source positions, no native visibility or original question answer claim. **Do not re-review the full J02 physics; review only the new test assertions/coverage.**

## 6. Final exact-head CI and evidence integrity

The full final source `b4eef0bf4be2ad46eb007573ff994e14e147d595` passed **11/11 pull-request workflows**; Node24 suites report **1,105 tests passed, zero failed**, including the new J08 and J02 tests. All previous PhyDemo/Chrome regression workflows passed; this is not a claim of a new J08-specific browser UI screenshot.

- Parameter experiment checks: run 44693880732 — success
- Plane-mirror angular inverse checks: run 44693880686 — success
- Deterministic planar angular query checks: run 44693880613 — success
- Numerical ray reliability diagnostics: run 44693880662 — success
- Curved mirror checks: run 44693880682 — success
- Original refraction problem pair: run 44693880675 — success
- Unified problem workflow checks: run 44693880793 — success
- Qualified authoring checks: run 44693880621 — success
- Quasi-static source motion checks: run 44693880625 — success
- Optical composition checks: run 44693880676 — success
- Planar refraction checks: run 44693880817 — success

Optical composition run [44693880676](https://github.com/physicsvigilante/opticsim/actions/runs/44693880676) lists:
- **`llm-authoring-evidence`** artifact **14610375926**, GitHub-declared digest `sha256:a19fc643615f683bde66b52053807bac23e335618e232a60f5e105501a20cfee`.
- `browser-acceptance-evidence` artifact **14609383953**, GitHub-declared digest `sha256:544128fe3c575471b66861d9111c264920c47ce4bd5dc06704540afc75775227`.
- `hosted-browser-evidence` artifact **14610375897**, GitHub-declared digest `sha256:42cf910e0880004a7b9443bbb92ba68d239a4c5e6de51cd7ad540ade974bf187`.

**Integrity caveat:** Builder retrieved GitHub metadata and actual CI logs; the artifact ZIPs were **not independently downloaded/rehashed** in this builder pass. Reviewer should inspect raw `input.json` / analytical reports, research native input/report SHA pairs and emitted/qualified evidence, recompute ZIP hashes, and independently check the original J08 Problems image if feasible. Original input bytes are saved before parsing under exclusively reserved fresh `test-artifacts/llm-authoring` directories. The pre-existing shared output helper's hostile-concurrent-filesystem race and ordinary `JSON.parse` duplicate-key behavior are **not** new security guarantees.

## 7. ONE focused Chat B review due — mandatory committed report

Reviewer Chat B should:

1. Inspect original **J08 Problems image only**, checking the unstated outside index and actual mirror/plate setup; avoid Solutions. Independently derive signed front-surface D, two-pass Snell and mirror-reflected directions, compare 65.85856 mm only with the **added** exterior n0=1.
2. Review strict pure standalone model, missing-index `needs-information`, TIR/near-critical/nonfinite refusal and unit conversion, separate raw-byte/SHA CLI evidence.
3. Audit actual pinned native **entry → mirror → exit** events; qualified public v5 source/Detector observables, including the distinction between front-surface separation and spacing of the two external detector hits. Verify raw stopped/incomplete/absent-mirror suppressions. No new native ray tracer, detected image or physical power claims.
4. Review **only** the new J02 centroid/median test follow-up; old PR #191 physics was independently cleared and is unchanged.
5. Verify exact final source commit/tree vs tested synthetic merge, all eleven CI runs, frozen protocol blob, unmodified upstream and no historical source changes; independently hash exact relevant artifacts if available.

**Do not review unchanged v5/native refraction core, old mirror geometry, J02 theory or other independently reviewed v20–v25 capabilities from scratch.**

**Required review deliverable:** a complete independent Markdown review committed to `physicsvigilante/review_sandbox` default branch at

`projects/opticsim/pr-192/reviews/review-01-chat-b.md`

Include the exact source **`b4eef0bf4be2ad46eb007573ff994e14e147d595`**, Git tree **`cb7b75df5ac4a2e4e6b1dc7283887da49135db47`**, tested synthetic merge **`60ea446db3ffcdadf999a4716bd62c85358ae2fd`**, original J08 source limitations, independent physical/math/numerical conclusions, blockers if any, and final verdict **CLEARED FOR OWNER DECISION** or **CHANGES REQUESTED**. Read back the committed review and provide immutable link and review commit SHA. **A chat-only verdict is not sufficient.**

**Release hold:** PR #192 stays draft/unmerged until the published focused independent review covers this unchanged exact tested tree, followed by standing owner release authorization. Do not rewrite JEE original-coverage scores or claim source-complete ray simulation.
