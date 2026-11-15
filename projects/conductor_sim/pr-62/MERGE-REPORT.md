# M27a — exact-source merge and main post-merge validation

**Status: MERGED and verified.** This record is authored by Chat A after explicit owner approval; it is not an independent reviewer report. No M27a code or review change was made during the merge.

| Evidence | Exact GitHub value |
| --- | --- |
| Source PR | [physicsvigilante/conductor_sim #62](https://github.com/physicsvigilante/conductor_sim/pull/62): closed, merged |
| Original base | `923ac2c49b23439cc9c76604bfd2a945e984d221` (M26a verified `main`) |
| Independently reviewed head | `666e6815390830cb6b70b474648b5b5ec765e380` |
| Reviewed source tree | `72a6dc67383b270b11e639ad81c1e52b693b0565` |
| Merge and verified `main` | `4a967f469df999bc4a97c434dfdd6b69f49893ba` |
| Merge parents | First `923ac2c49b...`, second `666e681539...` |
| Source-tree identity | Merge commit Git tree is **exactly** `72a6dc67383b270b11e639ad81c1e52b693b0565`, identical to reviewed head |
| Merge method | GitHub merge commit, with `expected_head_sha` pinned |
| Owner authorization | Explicit user: “approved and start with next task” |
| Pre-merge PR workflows | **18/18 passed** at reviewed head |
| Post-merge `main` push workflows | **17/17 passed** at exact merge commit |

## Provenance and independent review

The [preimplementation frozen charter](https://github.com/physicsvigilante/conductor_sim/blob/666e6815390830cb6b70b474648b5b5ec765e380/docs/m27a_charter.md) and first reserved R1 execution (PASS on initial physics candidate) remain unchanged. The first static-browser attempt failed a real 390px mobile overflow (399px document), corrected later without changing the ring law; the failure remains visible in GitHub run 43749110967.

[Independent Chat B R2 review-01](reviews/review-01-chat-b.md) gives **PASS for bounded static 3D ring E/V** at exact final reviewed SHA/tree. The reviewer performed novel standalone direct Coulomb quadrature and high-precision equation stress tests, examined source/CI, and identified two nonblocking presentation improvements, not numerical/physical defects. That review did **not** locally execute the production package, rehash the downloaded artifact or visually re-review the original scanned workbook page. Neither limitation has been misrepresented.

[Developer disposition](responses/response-01-chat-a.md) retained **F-01** (symmetric potential colour scale is labeled as observed potential range) and **F-02** (signed normal E and source Q/radius should be more directly legible) as explicit future UI work. They were not silently claimed fixed by merging.

## Actual post-merge CI

All listed runs below are `push` events with the **same exact merged head SHA**, completed successfully:

- [Full Python run 43753557419](https://github.com/physicsvigilante/conductor_sim/actions/runs/43753557419): Python **3.10 and 3.12 each 1,788 passed, 97 live-FEMM-specific skipped, 9 warnings**.
- [Real FEMM 5 run 43753557741](https://github.com/physicsvigilante/conductor_sim/actions/runs/43753557741): **97 passed**. This is legacy conductor nonregression, not a second numerical solver for the new nonconducting ring source law.
- [Full visualization and real Chromium 43753557413](https://github.com/physicsvigilante/conductor_sim/actions/runs/43753557413): all checks successful, including **M27a real Chromium two-ring static E/V acceptance**.
- [M19a fixed-source physics 43753557657](https://github.com/physicsvigilante/conductor_sim/actions/runs/43753557657), [M21b static E/V 43753557439](https://github.com/physicsvigilante/conductor_sim/actions/runs/43753557439), and the other 12 named retained push workflows all reported success. Total **17/17**, counting workflows rather than individual jobs/check-runs.

Post-merge [visualization/source artifact 14176514857](https://github.com/physicsvigilante/conductor_sim/actions/runs/43753557413/artifacts/14176514857) has GitHub-published ZIP SHA-256 `b78d1be6ca4707f106699aa0584cb6a7ba2627a198ec34032f8312f0e52e7d3d`. Chat A did **not** independently download/recompute its archive digest.

## Accepted technical scope

A distinct `UniformRingField` now supports actual **static full 3D E/V**
of an ideal fixed nonconducting thin ring, composed with other supported fixed
sources and uniform fields, including world-oriented rings A/B.
Historical `UniformRingAxisField` remains axis-only. The M27a
static observer stores true world E, signed normal components and
honest 3D projected ring geometry, with singular-wire masks and precomputed
HTML rather than fabricated time evolution. **M27a itself introduced no
particle/dipole time integration**; that requires separate M27b qualification.

Original source, failed CI records, independent review and teacher-display
limitations remain distinct. M27a acceptance does not certify conductor
induction, magnetic forces, unrestricted particle 3D motion, source response,
physical collision, general off-axis disc field maps, automatic PDF ingestion
or statistically representative exam coverage.

**Final disposition:** M27a merged and post-merge verified. The separately
approved next milestone M27b has its own new branch, frozen charter and draft PR.
