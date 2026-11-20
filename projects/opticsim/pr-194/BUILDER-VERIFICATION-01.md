# Opticsim PR #194 — FINAL BUILDER VERIFICATION and ONE focused Chat B v26 engine review request

**2026-11-20 (IST).** Builder/CI evidence; **not** an independent physics review or release authorization. The project owner has asked for one focused independent review per final capability, preserving previously accepted native physics and numerical safeguards. **PR #194 must stay draft/unmerged until this review covers the unchanged exact tree.**

## 1. Exact final tested source, ancestry and source freeze

- [Draft PR #194](https://github.com/physicsvigilante/opticsim/pull/194) HEAD commit **`9a2887f7cc5396387575fca1d6600e7a20b7f825`**, Git tree **`f142c0f22b7372d80b4381d68effb143f5cc5412`**.
- GitHub synthetic CI-tested merge **`5bbfa8fb5386c52301d65c544dd8972405adbc4b`** independently retrieved by builder with **exact same tree `f142c0f22b7372d80b4381d68effb143f5cc5412`**, ordered parents [production `main` `34a85e21985d13b4663473c20d7adc1d93fc4953`, exact feature head `9a2887f7cc5396387575fca1d6600e7a20b7f825`].
- Baseline `main`: independently reviewed J11 source (PR #193) merged at `34a85e21985d13b4663473c20d7adc1d93fc4953` and **11/11 post-merge CI workflows passed**. Verified main unmodified while preparing this report.
- Frozen **pre-execution** v26 protocol committed first at `9c539084a56d5c533b3e8e93916315528222bb39`. Blob SHA `a61a35ead739014d2124215a3aa77f2235e3a5c7` remains byte-identical in final HEAD, with ten unchanged prospective native experiment controls.
- Upstream PhyDemo pinned to **`811f508d2b070898c241a568b0c167dcb8645251`**, unchanged. There is **no new native propagation kernel**, no synthetic ray injection, no silent exterior-index default, no historical JEE answer/review/attempt rewrite.
- **Exactly 14 total changed files: 8 added and 6 modified.** Added: frozen protocol, v26 native admission module, explicit JSON example, raw-native test, public Node test, public JSON acceptance script, real Chrome acceptance script, and v26 documentation. Modified: `src/composition-profiles.js`, `src/contract.js`, `src/authoring.js`, `test/composition-profiles.test.mjs`, `test/native-v14-v21-integration.test.mjs`, and `.github/workflows/opticsim-ci.yml`. **No existing native Beam, PlaneGlass or Mirror propagation code was modified.**
- Importantly, **existing native Beam, PlaneGlass and Mirror implementations, event observers, old optical validation rules, old v19 profiles and pinned source are unchanged**. The two historical profile test files were only changed to assert the **original 31 remain** plus **exactly one new v26 profile**, instead of a brittle full-catalog count of 31.

## 2. Why this is an engine capability, not a case-specific answer

The 20-problem JEE first-draft audit plus later J08 source analysis showed: v5 can author actual **SingleRay + PlaneGlass + Mirror**, while v19 can author actual **finite deterministic Beam + PlaneGlass** but not Mirror. This is a true composition gap for multi-ray refract → reflect → refract systems. PR #194 adds a new JEE-first public v26 **`native-parallel-planar-mirror-tracing`** composition, not a numerical answer solver or conditional fabricated optical path.

**Strict new whole-system scope:** exactly one pinned native `Beam`, one vertical `PlaneGlass`, one independently finite vertical `Mirror` entirely in the second positive-index medium, and 0–2 passive vertical source-side `Detector` objects. No lenses, second plane, blockers, arbitrary mirror tilt, reverse Beam, point source mixtures or general optical graph. Beam width 10–100 mm, finite whole emitting segment left of the interface, forward incidence 0° through 60°, density .048–1, 1–100 true deterministic samples, brightness ≤density (native per-ray brightness saturation refused). Both indices are explicit [1,4], **second index ≥ first**; `partialReflection:false` is mandatory and accurately described as transmitted-only Fresnel approximation. Native TIR is retained but this simple forward-entry/return family does not require an entry TIR.

The new `src/native-beam-planar-mirror-v26.js` uses an independent *necessary* first-surface Snell geometry to screen **all actual deterministic starting samples** for safe real mirror interception, **more than 0.1 mm** from each finite mirror endpoint, while all world coordinates are bounded. Source, planar boundary, mirror and detector x planes are strictly ordered and separated. For each detector its finite endpoints are screened against the first inbound and single-return beam positions to within 0.1 mm, without prescribing a ray itinerary. **All actual refraction/reflection/intersection decisions remain those of pinned PhyDemo.** No new ray tracer or component adapter replaces native objects. Incomplete, stopped or stale run still suppresses accepted readings. A detector's actual missing/zero hit is not inferred illumination or physical darkness.

The public JSON example is `examples/native-parallel-planar-mirror-v26.json`, using normal `opticsim-problem-v1` authoring and existing requested `source-emissions`, `interface-interactions`, `interface-first-event`, `mirror-reflections`, `detector-crossings`, `detector-hit-events`. No 3D image/irradiance/ray source-parentage claim is added, and no original J08 source-complete numeric simulation is claimed (its exterior index and source apparatus are absent from original source).

## 3. Independent analytic reference and *genuine pinned-native* test-only feasibility

Frozen **synthetic** apparatus: Beam center (−100,0) mm, width 40 mm, forward +30°, native relative brightness .08, density .2; PlaneGlass x=0 with explicit exterior index 1 and second medium 1.5, Fresnel-off; vertical Mirror x=60 mm, length 420 mm; vertical Detector x=−10 mm, length 420 mm; max native depth 8, processed limit 10000. None of these are original J08/JEE data, except as a deliberate generic teaching apparatus.

Independently evaluable necessary relations:

```
r = asin((n0/n1) sin(i)) = 19.47122063449069° for n0=1,n1=1.5,i=30°.
front-face shift after mirror return = 2*60*tan(r) = 42.426406871192846 mm.
source-side detector inbound/outbound pair spacing = front-face shift + 20*tan(30°)
   = 53.97341225498536 mm (for detector x=-10 mm).
```

Note that *detector* spacing is not the displacement between front-face entry and exit. Actual callback geometry, sample count and direction are checked independently; equations are only guards/comparisons, never ray steering.

**Raw pinned research evidence** from the ten frozen cases was executed at final head. The research code compiles a legal v19 Beam+PlaneGlass+Detector canonical scene and appends a raw native Mirror **only to a clone**, clearly marked unqualified test-only. Log excerpt from exact [optical composition run 44705604222](https://github.com/physicsvigilante/opticsim/actions/runs/44705604222):

| Raw synthetic scenario | Native emitted | Glass callbacks | Mirror callbacks | Detector callbacks | Native completion |
|---|---:|---:|---:|---:|---|
| Baseline, translated, normal, higher-index | 8 | 16 | 8 | 16 | complete, 0 truncation |
| Denser density .4 | 16 | 32 | 16 | 32 | complete, 0 truncation |
| Mirror absent (valid v19 control) | 8 | 8 | 0 | 8 | complete, no return |
| Too-short mirror, raw test | 8 | 8 | 0 | 8 | complete; misses rather than true rim collisions; **not a v26 admitted scene** |
| Fresnel-on RAW only | 8 | 24 | 16 | 32 | **INCOMPLETE**, native truncation **0.0060300013751256746** |
| Zero ray depth | 8 | 0 | 0 | 0 | **INCOMPLETE**, truncation >0 |
| Processed-ray limit one | 8 | 0 | 0 | 2 | **STOPPED**, no qualified return |

Do **not** relabel a raw, complete but clipped/missed mirror as qualified v26; the strict *public* v26 validator separately rejects unsafe too-short and near-rim mirror configurations. This test only establishes pinned native feasibility and tracks original input/report bytes with SHA-256, while retaining uncertainty and failures.

## 4. Public end-to-end authoring, numerical guards and actual browser

At the final source HEAD, **11/11 GitHub PR workflows passed and Node 24 suite reports 1,125/1,125 tests passing, 0 failed.** All older native/Chrome regressions passed. [Exact optical composition CI run 44705604222](https://github.com/physicsvigilante/opticsim/actions/runs/44705604222), job `136184301107`, shows these new additional steps **both SUCCESS**:

- `v26 native Beam with PlaneGlass and finite Mirror public qualified authoring`
- `v26 real Chrome Beam refraction return, physical edit, corner refusal and reopen`

**Public acceptance** `scripts/native-parallel-planar-mirror-v26-acceptance.mjs` used the ordinary JSON problem runner and real pinned optical engine; baseline **8 genuine Beam emissions, 16 genuine PlaneGlass incidents, 8 finite Mirror reflections and 16 real detector crossings**, with a complete, qualified Fresnel-off native run. Public acceptance also verifies width/index revisions and physically refused native-not-run cases (short mirror, Fresnel-on, missing exterior index, tilted mirror), preserving input bytes, original SHA and portable qualified export without cached readings. **Seven cases: three native-complete and four refused before native**.

**Public Node tests** verify v19 saves still reject a silent Mirror addition; v26 captures true objects `Beam, PlaneGlass, Mirror, Detector`, test-only independent signed Snell and mirror reflection invariants, whole source/mirror/detector endpoint guards, source/medium/geometry revisions, no fallback, invalid version/mixtures and incomplete/stopped suppression. Density .4 produces **32** detector hits, the position list is available. Density 1 produces **80** genuine detector callbacks, but **`detector-hit-events` withholds the entire list** under the existing 32-hit cap (not silently clipped); numeric total crossings remain native counts.

**Actual real Chrome** `scripts/native-parallel-planar-mirror-v26-browser.mjs` ran against the existing static viewer and downloaded a qualified scene. Its log states **PASS with eight checks and five screenshots**, covering real native initial counts, editable Beam/index/Mirror controls, Beam-width edit, refractive-index edit, valid qualified save/export, clipped-Mirror refusal that clears stale readings, and reopening the qualified package with retraced native readings. Browser network/runtime error checks passed. This is builder-run Chrome, NOT independently rerun by Chat B.

**First integrated public CI attempt at commit `e63d4699...` failed** because two old catalog tests asserted an **overall 31-profile total**, whereas adding v26 gives 32. The new v26 physics/native tests themselves passed in that attempt. The old test assertions were **surgically strengthened**, not relaxed: they now require precisely the original 31 profiles **plus exactly one new v26 profile**. Current final source `9a2887f7cc5396387575fca1d6600e7a20b7f825` passed **all 11/11 workflows and 1,125/1,125 Node tests**, with new browser evidence. Do not present this as clean first-attempt success or conceal historical test edits.

## 5. Evidence and hash boundaries

Exact [optical composition run 44705604222](https://github.com/physicsvigilante/opticsim/actions/runs/44705604222) uploaded:
- `llm-authoring-evidence` ID **14615111272**, GitHub-declared SHA-256 `a8f780979c8d119a74cc8fb51f103486fe13d46b7944b032c3120d6c5306b9d6`.
- `opaque-blocker-evidence` ID **14615061344**, SHA-256 `13d4e2d7d757d63d622d824778725d44a7da25e0abdc456174d8a4bdf0a4e1d2` (includes the new v26 real-Chrome evidence directory).
- `browser-acceptance-evidence` ID **14614054001**, SHA-256 `c2a1f97715d46c6134c10ec5b2cd627091fa5d72a13826b82521a63197525697`.
- `hosted-browser-evidence` ID **14614053987**, SHA-256 `4dc879869043765c3b12bec864d1d1a90fabf5ec964e2e37eeafb100226a4d10`.

**Builder did not independently redownload/recompute these ZIP bytes**; above are official GitHub artifact digests plus actual CI/job logs. Reviewer should independently retrieve and check exact source artifacts, raw ten-case input/report hashes, public seven-case outputs, v26 real Chrome screenshots/report and the unchanged v19 source physical fingerprints; document any evidence that was only metadata/log-based.

## 6. One focused independent Chat B review — mandatory deliverable and release hold

**Reviewer tasks:**
1. Independently inspect final source and compare; check exact new v26 registry/selector/validator path does not allow unsupported beam/mirror mixtures to **downgrade** to v19 or mutate historical saved v5/v19. Verify **original 31** remain identical and new v26 is one additional profile; check the two old test modifications preserve rather than rewrite physics expectations.
2. Derive independently the actual finite Beam sample emission positions, signed Snell refraction, finite-Mirror return and detector first/return locations. Challenge the **first-hit mirror rim** clearance and detector endpoint guard for rounding, wrong-side origins, complete source-segment placement, equal indices, out-of-range source direction, Fresnel-on refusal and corner/near-critical hazards. Verify the paper formula is used only to **reject ambiguous geometry**, never to produce native ray paths or native claims.
3. Independently examine actual archived pinned native callbacks, completeness/truncation/undefined and missed mirror controls; check the full public JSON-to-PhyDemo path, actual sampled readouts, 32-hit cap and invalid/stale suppression.
4. Read real Chrome report and PNGs and browser CI, including field edits, genuine simulation updates, qualified save, clipped-mirror refusal and reopened source. Distinguish builder Chrome from your independent rerun. Preserve 'native 2D only', Fresnel-off approximation, no power/image/PSF/observer JEE grading.
5. Independently verify exact final HEAD `9a2887f7cc5396387575fca1d6600e7a20b7f825`, tree `f142c0f22b7372d80b4381d68effb143f5cc5412`, synthetic merge `5bbfa8fb5386c52301d65c544dd8972405adbc4b`, the unchanged frozen protocol blob, all eleven CI runs, relevant artifact/member hashes and precise modifications. Review **this new v26 composition and integration**, **not** unchanged upstream PhyDemo v5/v19 ray laws, J11 3D disc or older optics domains.

**Independent reviewer required GitHub deliverable:** commit a complete markdown report to `physicsvigilante/review_sandbox` default branch at

`projects/opticsim/pr-194/reviews/review-01-chat-b.md`

Report must identify reviewed **source SHA `9a2887f7cc5396387575fca1d6600e7a20b7f825`**, Git tree **`f142c0f22b7372d80b4381d68effb143f5cc5412`**, synthetic merge **`5bbfa8fb5386c52301d65c544dd8972405adbc4b`**, any blocking physics/code/evidence issues, nonblocking limitations, and explicit final verdict **CLEARED FOR OWNER DECISION** or **CHANGES REQUESTED**. Read back the committed review; give immutable review GitHub URL and commit SHA. A Chat-only verdict is not release evidence. Reviewer must not edit/merge/deploy Opticsim source or rewrite JEE evaluations.

**Release gate:** Keep [PR #194](https://github.com/physicsvigilante/opticsim/pull/194) **draft, unmerged** until exact-source independent review is complete and verified, then apply standing owner authorization. One focused final review only — no redundant independent review of test-only feasibility or unchanged prior optics.
