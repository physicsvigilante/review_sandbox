# Independent R3 review request — Opticsim PR #148 grazing-ingress P1 correction

**RESEARCH ONLY, DO NOT MERGE.** Chat B's [independent PR #146 R2 report](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-146/reviews/review-01-chat-b.md) returned CHANGES REQUESTED on a reproduced P1 ingress-grazing defect. Review the new child source, not the old frozen #146 tree.

## Exact identity, ancestry and evidence

- [Draft PR #148](https://github.com/physicsvigilante/opticsim/pull/148), source HEAD **6091256df8d22e62f6f9d502a9609e3f139e49cd**, source Git tree **e4a973c191562848345b9306293987b33809b9ff**.
- True base is frozen PR #146 HEAD **2621c08812eb389b70a3e4fa246537ca50b3bc4d**. PR #146 descends from #145, which originated at main d3509e82fb65d81aabe336666851f8f2962623f4.
- Temporary main-target [CI-only PR #149](https://github.com/physicsvigilante/opticsim/pull/149), synthetic merge **ab180839eb6fcae09aca4783a5129ccff70dc057**, verified by builder to have identical tree **e4a973c191562848345b9306293987b33809b9ff** with parents [main, exact reviewed source]. Independently inspect Git commit objects, not just PR prose.
- Diff from PR #146 changes only test/jee-observer-native-feasibility.test.mjs and docs/JEE-OBSERVER-REFRACTION-NATIVE-RESEARCH.md. No production physics, PhyDemo source, adapter, schema, browser, or previously reviewed PR source changes.
- [PR #145 R1](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-145/reviews/review-01-chat-b.md) and PR #146 R2 remain historical CHANGES REQUESTED for their different SHAs. No review inheritance or owner release implied.

## Independently established R2 P1

Single ideal infinite planar interface through P=(0,0), oriented normal 135 degrees, indices ns=1 and no=2. Source S=(9758.080722152847,9758.066438595866) mm and observer O=(-9616.652224137046,-9475.230867899736) mm. Both coordinates and the 20 mm observer-centered finite detector are within +/-10000 mm. Source normal clearance is approximately 0.0101 mm; observer clearance approximately 100 mm. Tangent span is +27300 mm.

The test-only inverse oracle solves stationary optical path in local tangent offset v=q-us, with Snell residual:
  ns*v/hypot(ds,v) - no*(span-v)/hypot(do,span-v) = 0.
Existing local/world residual checks passed (approximately +1.5765e-14 and +3.4639e-14), while the incoming cosine of the normal is only around 3.70747e-7. Outgoing cosine is around 0.866. R2's outgoing-only grazing guard therefore marked this physically valid but extremely ill-conditioned *shooting representation* available. Independent forward evaluation of a rounded authored heading misses the observer by more than the test's 1e-5 mm coordinate tolerance. That was independent reference math, NOT a native PhyDemo execution of the extreme case. No proven native solver defect or physical nonexistence claim follows.

## R3 patch and focused review questions

1. The child separately computes incoming and outgoing normal cosines AFTER independently checking local and represented-world Snell residuals. It conservatively withholds incoming cosine less than 0.02 as **numerically-unstable / NEAR_GRAZING_INGRESS**, with null predicted crossing Q, incoming vector, authored heading and apparent point. Existing NEAR_GRAZING_EXIT for outgoing cosine less than 0.02 remains. Ensure no native SingleRay can be authored for either unstable geometry.
2. The 0.02 criterion is **test-only research admission**, not a physical critical angle, universal quantization certificate, proof of visibility, or native ray repair. Real solutions may be conservatively withheld. Check reason/status precedence and whether this guarded scope is appropriate.
3. New exact-source regression uses the supplied original P1 geometry AND reflection across the oriented normal, preserving source/observer sides while reversing tangent span to **-27300 mm**. Both must have specific ingress withholding despite locally valid Snell residual. Independently recompute the positive and negative spans, source clearance, residuals and incoming/outgoing normal cosines.
4. Ensure original moderate native source (-60,0) to observer (100,40), indices 1.5 to 1, still gives actual pinned native detector hit at (100,40) and measured refracted direction; its axis depth and interface crossing are only analytical. Earlier world-y=9000 scenario must still be WORLD_COORDINATE_ROUNDING, near-critical outgoing case NEAR_GRAZING_EXIT, near-axis case NEAR_AXIAL_INFERENCE; stale/incomplete native results suppressed.
5. Inspect actual CI jobs and Git tree identity. No independent rerun claim unless you genuinely execute pinned native PhyDemo. Do not assert native interface point is measured or that source-object ancestry/real image is established.

## Exact-head builder CI

All **11/11 standard GitHub Actions workflows** completed SUCCESS, and **800/800 Node tests** passed for source HEAD above, via identical-tree synthetic merge. [Optical composition run #44295048428](https://github.com/physicsvigilante/opticsim/actions/runs/44295048428) and [plane-mirror run #44295048389](https://github.com/physicsvigilante/opticsim/actions/runs/44295048389), job 134769809900, have logged tests. The named new marker JEE_OBSERVER_GRAZING_INGRESS_WITHHELD records normal 135 degrees, positive/negative tangent spans +/-27300 mm, NEAR_GRAZING_INGRESS, nativeRayAuthored:false and nativeImageDetected:false. Prior JEE_OBSERVER_LOCAL_ROOT_WITHHELD, JEE_OBSERVER_NATIVE_ARRIVAL and JEE_OBSERVER_NATIVE_SUPPRESSION markers still appear. These are builder-CI Node/native/browser results, not an independent reviewer native rerun.

Publish independent R3 report at **projects/opticsim/pr-148/reviews/review-01-chat-b.md**, with exact SHA/tree, independent math, source/CI evidence, P0/P1/nonblocking findings, and one verdict **CLEARED FOR NEXT SCOPED DEVELOPMENT / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. This is test-only feasibility: do not merge, approve release, change reviewed source, rewrite old reviews, or claim issue #123 branch protection is resolved.