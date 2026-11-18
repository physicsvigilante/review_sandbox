# Opticsim PR #150 — independent source/physics R1 request

**Draft analytical engine candidate, NOT a release or merge approval.** The user prioritizes a JEE-focused first draft; this feature supports a one-plane source-to-observer optical question without claiming native inverse tracing, image detection or general optical composability. Chat B must review this **new source** independently. Earlier research PR #148's clearance does not transfer to this API.

## Exact source, base and CI provenance

- [Draft PR #150](https://github.com/physicsvigilante/opticsim/pull/150): head commit **0fb738f69b3257113c73dbf9d1f2917037daa5cc**, source Git tree **8cd6b5df7cceaf68d04deca4926eb91245986216**.
- Base is production `main` at **d3509e82fb65d81aabe336666851f8f2962623f4**; PR is independently main-based, not a descendant of held PRs #141/#143/#144/#145/#146/#148.
- GitHub synthetic PR CI merge **4ff6dd2ff4b8cf85a2ecc59c3836cca1df2ffcfc** has identical tree **8cd6b5df7cceaf68d04deca4926eb91245986216** and ordered parents [production main, exact source HEAD]. Verify this by reading the actual Git commit objects.
- Four added files and no pre-existing modified files:
  1. `src/planar-observer-point-query.js` — new deterministic typed analytical contract;
  2. `scripts/planar-observer-point-query.mjs` — original-byte SHA-256 evidence CLI;
  3. `test/jee-observer-point-query-v1.test.mjs` — physical, numerical, CLI and separate native cross-checks;
  4. `docs/JEE-OBSERVER-POINT-QUERY-V1.md` — exact scope and evidence provenance.
- Existing production native simulator, schema, adapter, browser and all held older feature branches remain unchanged.
- **800/800 Node tests, 11/11 standard Actions workflows SUCCESS** at the exact source tree. Key native/Chrome composition workflow [#44300152212](https://github.com/physicsvigilante/opticsim/actions/runs/44300152212) and planar-angular workflow [#44300152211](https://github.com/physicsvigilante/opticsim/actions/runs/44300152211), job **134787468431**. Inspect actual job logs and the source/CI tree identity. These runs are **builder CI**, not an independent reviewer rerun of PhyDemo/Chrome/Node.

## Supported user-facing question and contract

This is *not* the separately reviewed but unmerged PR #144, which requires an explicit incident angle. PR #150 accepts a **known source point S** and a **known observer-side point O**, plus one oriented infinite planar refracting boundary point P, normalDeg pointing from source to observer side, explicit sourceIndex and observerIndex and lengthUnit. It returns the mathematically conditional one-interface transmitted direction/crossing and apparent-axis intercept when identifiable. A provided observer point is **not** a detector/eye, and the calculation does not author any native ray.

Explicit example:
```json
{
  "format":"opticsim-planar-observer-point-query-v1",
  "kind":"source-to-observer-transmission",
  "lengthUnit":"mm",
  "source":{"x":-60,"y":0},
  "observer":{"x":100,"y":40},
  "interface":{"x":0,"y":0,"normalDeg":0,
    "sourceIndex":1.5,"observerIndex":1}
}
```

Strict: finite coordinates inside +/-10000 mm after mm/cm/m conversion; source and observer require >=0.01-mm normal clearance on **opposite declared sides**, no silently reversed normal or index assignment; explicit indices in [1,4], normalDeg [-180,180], no extra/unknown fields, no invented brightness, Fresnel choice or detector.

## Physics to audit independently

Set `n=(cos φ,sin φ)`, `t=(-n_y,n_x)`, `d_s=-(S-P)·n>0`, `d_o=(O-P)·n>0`, `u_s=(S-P)·t`, `u_o=(O-P)·t`, `span=u_o-u_s`, `v=q-u_s`. The one-interface stationary-path equation is:

`F(v)=n_s*v/hypot(d_s,v) - n_o*(span-v)/hypot(d_o,span-v)=0`.

For finite positive indices and normal distances the derivative is positive, so the ordered local bracket [min(0,span),max(0,span)] contains a unique stationary solution. The predicted interface crossing is `Q=P+(u_s+v)t`. The incoming/outgoing directions come from the normalized *local* combinations `d_s n+v t` and `d_o n+(span-v)t`. Incident and refracted angles are signed with respect to the **source-to-observer** normal. The headingDeg is world y-up. No native ray path is prescribed.

The nonaxial conditional apparent-axis intercept depth is `v*d_o/(span-v)`, apparent point `F_s-depth*n` where `F_s=P+u_s t`. It is a mathematical backward extension, **not** a physical image or native detector reading. For exact axial span=0, the **ray is still determined** but one-ray apparent depth is not: `axisInterceptStatus='not-identifiable'`, no apparent-axis point/depth. Paraxial `d_s*n_o/n_s` is reported **as a separate comparison**, not mislabelled as every finite-angle image.

Independently recompute example: crossing `Q=(0,11.24615577120923)` mm, initial incidence/source heading `10.616108941304955°`, refracted `16.041977708350927°`, finite-angle apparent depth `39.11183381854949 mm`, paraxial limit `40 mm`. Verify reversed tangent observer y=-40, 90°/180° rotation, lateral representation of plane point, units and 1→1 / 1→1.5 contrasts (the latter conditional depth ~92.53084858 mm).

## Numerical admission — do not accept unreviewed physical claims

- Root solved in the *local* v coordinate. Check real-world geometry and unique root for BOTH tangent signs. Require finite local Snell residual <=1e-12; if not, `numerically-unstable/LOCAL_ROOT_UNRESOLVED`, value null.
- Reconstruct world Q, compare world-coordinate Snell residual <=1e-12; withhold `WORLD_COORDINATE_ROUNDING` when local root cannot be faithfully represented in world binary64. The high-world-y research case S=(-.02,9000), O=(.02,9000.01), plane x=0, n1=1.5→n2=1 is the required negative control; do not claim the physical root ceases to exist.
- Check incoming/outgoing normal cosine <0.02 both fail closed with distinct `NEAR_GRAZING_INGRESS`/`NEAR_GRAZING_EXIT`. This is a **conservative heuristic**, not a physical critical angle or proved universal heading-rounding certificate. Exact [PR #146 R2 counterexample](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-146/reviews/review-01-chat-b.md): plane normal135°, ns=1/no=2; S=(9758.080722152847,9758.066438595866), O=(-9616.652224137046,-9475.230867899736) and its mirrored negative tangent span must withhold.
- Near but nonzero axial projection under 1e-10 mm returns `NEAR_AXIAL_INFERENCE`. Exactly axial returns a valid conditional source-to-observer ray, with null single-ray virtual image inference.
- Unrepresentable crossing, nonfinite or out-of-bounds apparent point must withhold instead of inventing a value. Invalid input is rejected, distinct from a physically valid but numerically withheld conditional calculation.
- The source/observer endpoint-conditioned one-boundary mathematical solution exists for any declared positive indices/sides and is **not** a user-supplied arbitrary incident ray; ordinary forward TIR/no-transmission does not directly become an outcome category in this inverse endpoint-conditioned scope. Verify that interpretation, including near-critical outgoing grazing.

A crucial challenge for review: the tests guard **some** extreme geometries but the 0.02 heuristic does **not** guarantee a rounded heading will hit a specified observer within a particular tolerance throughout the entire bounded coordinate envelope. Scrutinize the public response's wording and whether the scope is acceptable without optional native verification; do not let passing internal mathematical residuals imply a native achieved hit.

## Evidence handling and separation of native tests

The CLI requires fresh output and preserves unchanged input JSON bytes and SHA-256; a valid request writes an analytical result, invalid JSON/fields a rejection report without a result. It **always** labels `native:{status:'not-run',observations:null,nativeImageDetected:false}`, never creates a native scene or detector, and uses exclusive writes **not** tamper-proof storage.

In **tests only**, the code authors a *separately complete* canonical v5 scene with brightness, `single-ray` heading from analytical result, `partialReflection:false` and a finite detector at O. Standard pinned PhyDemo then independently propagates a real sampled ray. Assertions check true native detector hit point/direction, first refraction event, explicit Fresnel-omission warning, completed/hash-matched source and count-matched hit events. The analytical query itself does not borrow that evidence. Stale/incomplete native runs are suppressed separately.

## Required verdict

Inspect all four new source/test/doc files, relevant unchanged `src/planar-media.js`, `src/angular-math.js`, `src/observables.js`, `scripts/authoring-evidence.mjs`, exact Git trees and actual CI logs. Independently reproduce critical numerical cases, identify any P0/P1 blocker and list nonblocking hardening, preserving observed-vs-inferred and native-vs-analytic distinctions.

Publish **projects/opticsim/pr-150/reviews/review-01-chat-b.md** with exact HEAD/tree, evidence provenance and verdict **CLEARED FOR OWNER DECISION / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. Do not edit code, run merges, claim a native image or modify previous reviews. PR #150 remains draft/unmerged pending a **separate owner release decision**; other reviewed/held branches and issue #123 branch protection are outside this source gate.
