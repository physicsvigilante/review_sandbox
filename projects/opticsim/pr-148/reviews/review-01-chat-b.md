# Independent R3 — Opticsim PR #148: grazing-ingress admission correction

**Review date:** 2026-11-18  
**Reviewer:** Chat B — independent Git-object/source/CI inspection, standalone binary64 reference arithmetic, and separate 90-digit optical calculations.  
**Verdict: CLEARED FOR NEXT SCOPED DEVELOPMENT.**

The incoming-grazing P1 identified in the frozen PR #146 R2 review is corrected on the exact child source below. The original geometry and its negative-tangent-span reflection are now withheld before native authoring. The ordinary native positive control and earlier numerical/suppression controls remain supported by the inspected builder evidence. **P0: none found. P1: none found in this scoped correction. No required correction blocks this research gate.** This is not release approval, merge authorization, a general forward-error certificate, or retroactive approval of PR #145/#146.

## 1. Exact identity, ancestry and diff — verified

| Item | Independently checked identity |
|---|---|
| Research PR | [#148](https://github.com/physicsvigilante/opticsim/pull/148), open, draft, unmerged; exact head rechecked before publication |
| Source HEAD | `6091256df8d22e62f6f9d502a9609e3f139e49cd` |
| Source Git tree | `e4a973c191562848345b9306293987b33809b9ff` |
| Frozen true base | PR #146 HEAD `2621c08812eb389b70a3e4fa246537ca50b3bc4d` |
| CI-only PR | [#149](https://github.com/physicsvigilante/opticsim/pull/149), already **closed without merging** |
| CI synthetic merge | `ab180839eb6fcae09aca4783a5129ccff70dc057` |
| CI Git tree | `e4a973c191562848345b9306293987b33809b9ff` — identical to reviewed source |
| CI ordered parents | `d3509e82fb65d81aabe336666851f8f2962623f4`, then exact reviewed source `6091256df8d22e62f6f9d502a9609e3f139e49cd` |

The [source Git commit object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/6091256df8d22e62f6f9d502a9609e3f139e49cd) and [synthetic merge Git commit object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/ab180839eb6fcae09aca4783a5129ccff70dc057) establish tree equality and merge parents independently of PR prose. GitHub compare reports **3 commits ahead, 0 behind**, with the frozen #146 head also the merge base.

Exactly two files differ from #146: [test/jee-observer-native-feasibility.test.mjs](https://github.com/physicsvigilante/opticsim/blob/6091256df8d22e62f6f9d502a9609e3f139e49cd/test/jee-observer-native-feasibility.test.mjs) (+57/-4) and [docs/JEE-OBSERVER-REFRACTION-NATIVE-RESEARCH.md](https://github.com/physicsvigilante/opticsim/blob/6091256df8d22e62f6f9d502a9609e3f139e49cd/docs/JEE-OBSERVER-REFRACTION-NATIVE-RESEARCH.md) (+16/-0). No production engine, PhyDemo source/pin, adapter, canonical schema, browser code or workflow changes are included in this child diff.

The [PR #146 R2 report](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-146/reviews/review-01-chat-b.md) remains historically **CHANGES REQUESTED** at its different SHA/tree, as does [PR #145 R1](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-145/reviews/review-01-chat-b.md). This report does not alter either record.

## 2. Independent mathematics — physical root and numerical shooting are different questions

For an oriented unit normal `n` from source medium to observer medium and tangent `t=(-n_y,n_x)`, define

`d_s=-(S-P)·n`, `d_o=(O-P)·n`, `u_s=(S-P)·t`, `span=(O-P)·t-u_s`, and `v=q-u_s`.

The stationary optical path condition is

`F(v)=n_s*v/hypot(d_s,v)-n_o*(span-v)/hypot(d_o,span-v)=0`.

For positive indices and positive normal clearances,

`F'(v)=n_s*d_s²/(d_s²+v²)^(3/2)+n_o*d_o²/(d_o²+(span-v)²)^(3/2)>0`.

Thus the ordered interval `[min(0,span),max(0,span)]` brackets a unique physical stationary solution for either tangent sign. At zero span the stationary ray is axial. None of this proves that converting its direction to a binary64 degree value and then to native endpoints will reproduce the desired observer coordinate within a fixed absolute tolerance.

### Exact R2 counterexample and reflected twin

The supplied original uses `P=(0,0)`, normal `135°`, `n_s=1`, `n_o=2`,

`S=(9758.080722152847,9758.066438595866)` mm,

`O=(-9616.652224137046,-9475.230867899736)` mm.

I independently executed standalone Node.js arithmetic with the inspected normal/projection/bisection operation ordering; it imported **no Opticsim code** and executed **no native engine**. The reflection used by the regression, `R(p)=2*n*(n·p)-p`, is correct for this plane through the origin: it preserves normal side and reverses tangent sign. Its binary64 points are

`S'=(-9758.066438595868,-9758.080722152845)` mm,

`O'=(9475.230867899738,9616.652224137044)` mm.

| Independently recomputed binary64 diagnostic | Original | Reflected |
|---|---:|---:|
| Source clearance, mm | `0.010099999998601561` | `0.010099999998601561` |
| Observer clearance, mm | `99.99999999999909` | `99.99999999999909` |
| Signed tangent span, mm | `27300` | `-27300` |
| Local root offset v, mm | `27242.264973081044` | `-27242.264973081044` |
| Local Snell residual | `+1.5765166949677223e-14` | `-1.5765166949677223e-14` |
| Represented-world Snell residual | `+3.4638958368304884e-14` | `-1.587618925213974e-14` |
| Incoming normal cosine | `3.7074743991505343e-7` | `3.7074744013709804e-7` |
| Outgoing normal cosine | `0.8660254037844631` | `0.8660254037844630` |
| R3 admission decision | `NEAR_GRAZING_INGRESS` | `NEAR_GRAZING_INGRESS` |

Both sources/observers and both endpoints of each 20-mm observer-centered tangent detector remain within +/-10000 mm and on the required sides. The mirrored case is not accidentally reversing the medium ordering or triggering a different invalid-geometry guard.

Separate **90-digit** calculations using the exact represented binary64 source/observer coordinates and an exact mathematical 135-degree normal confirm a physical root in both cases. For the original, `d_s≈0.0101000000003368943` mm, `v≈27242.2649730810425` mm, incoming cosine `≈3.707474400647793e-7`, and outgoing cosine `≈0.8660254037844585`. The small difference from the table is expected: the table deliberately reproduces binary64 trigonometry and cancellation in the dot products, while this calculation uses an exact mathematical normal. Both conclusions are far from the 0.02 admission boundary.

As an additional independent sensitivity check, I propagated the original unguarded binary64 heading `-135.000021242263557041951571591198444366455078125°`, treated as an exact number, through the ideal mathematical plane with 90-digit Snell arithmetic. The resulting observer-line miss is approximately **3.0714602257e-5 mm**, with each Cartesian coordinate wrong by **2.1718503537e-5 mm**, exceeding the test's per-coordinate `1e-5 mm` tolerance. These figures specify this calculation's exact floating-point interpretation; they are not a native PhyDemo result or a replacement for the earlier R2 calculation record.

The reflected heading happens to give a smaller miss under this particular idealized evaluation. It is still correctly withheld: the conservative ingress rule does **not** claim every rejected input must fail one specific rounded forward evaluation. Physical reflection symmetry does not require floating-point heading errors to be mirror-symmetric.

## 3. Source and regression audit — P1 corrected within the declared scope

The exact-head `shootingReference` retains the following precedence:

1. Invalid stated side/clearance rejects the geometry.
2. Nonfinite or excessive local residual yields `LOCAL_ROOT_UNRESOLVED`.
3. Nonfinite or excessive reconstructed-world residual yields `WORLD_COORDINATE_ROUNDING`.
4. Nonfinite incoming normal cosine or a value **strictly below 0.02** yields `NEAR_GRAZING_INGRESS`.
5. Nonfinite outgoing normal cosine or a value **strictly below 0.02** yields the retained `NEAR_GRAZING_EXIT`.
6. A nonzero, too-small tangent displacement yields `NEAR_AXIAL_INFERENCE`; an exactly axial admitted ray retains null one-ray depth.

The ingress/exit checks occur before calculating or returning an authorable heading. The common unstable result sets **Q, incoming, outgoing, incidentHeading, apparentDepth and apparentPoint to null**, retains only the stated diagnostics/reason, and sets `nativeImageDetected:false`.

`nativeWitness` asserts `ref.status==='available'` **before** `sceneFor`, canonical preparation or native evaluation. The new regression invokes the reference only, checks the specific ingress reason for both tangent signs, and checks null crossing/incoming/heading/apparent point together with small finite local/world residuals. The inspected call path therefore cannot turn either withheld case into a native SingleRay. The logged `nativeRayAuthored:false` is a descriptive marker, not independently instrumented native-call telemetry; the control-flow inspection and passing assertions are the supporting evidence.

The documentation accurately treats 0.02 as a **test-only numerical admission rule**, not a physical critical angle, visibility theorem, new Snell law, or guarantee for all admitted inputs. No native ray is redirected, repaired, or supplied with a prescribed interaction route. This is a sufficient scoped response to the earlier requested fail-closed ingress correction; a universal error certificate is not silently being claimed.

I also independently checked an equal-index case with both cosines about `0.001999996`: ingress correctly has priority. This was a standalone arithmetic check, not a new repository test or native run.

## 4. Original positive and earlier refusal controls — preserved

For `S=(-60,0)`, `O=(100,40)`, `n_s=1.5`, `n_o=1`, independent 90-digit calculation gives

- `Q=(0,11.2461557712092301127...)` mm;
- incidence `10.61610894130495294...°`, transmission `16.04197770835092774...°`;
- outgoing unit vector approximately `(0.9610594924712145,0.2763415494111802)`;
- conditional source-axis intercept depth `39.1118338185494934...` mm.

Both normal cosines are comfortably above 0.02. The builder job's actual `JEE_OBSERVER_NATIVE_ARRIVAL` log records the detector hit **`(100.00000000000001,40)`**, with `nativeImageDetected:false`. The passing exact-source assertions additionally require a transmitted interface event, correct medium indices, one emitted ray, one complete detector crossing, observer coordinates within `1e-5 mm`, and the measured detector incoming direction within `1e-7` of the independent outgoing reference. The log does not separately print that measured direction vector; its agreement is supported by the passing assertion, not by an invented raw measurement.

The independent binary64 reproduction also preserves:

| Control | Independently checked result |
|---|---|
| Observer reflected to `(100,-40)` | Opposite signed Q/heading, same positive conditional depth |
| Equal indices 1 to 1 | Admitted; conditional depth 60 mm |
| Reversed index contrast 1 to 1.5 | Admitted; conditional depth approximately 92.53084858 mm |
| R1 large-world case near y=9000 | `WORLD_COORDINATE_ROUNDING`; local residual 0, world residual `-4.1488867896788406e-11` |
| Outgoing grazing `O=(100,9000)` | `NEAR_GRAZING_EXIT`; outgoing cosine approximately `0.011177056648940552` |
| Nonzero near-axis `O=(100,1e-11)` | `NEAR_AXIAL_INFERENCE` |
| Exact axial `O=(100,0)` | Admitted native-control geometry, null one-ray apparent depth |

The exact-head builder log also shows the existing reflection, equal/reversed-index, rotated/translated, axial, and stale/incomplete tests passing. `JEE_OBSERVER_NATIVE_SUPPRESSION` records both stale and incomplete suppression.

Targeted inspection of unchanged [adapter.js](https://github.com/physicsvigilante/opticsim/blob/6091256df8d22e62f6f9d502a9609e3f139e49cd/src/adapter.js), [planar-media.js](https://github.com/physicsvigilante/opticsim/blob/6091256df8d22e62f6f9d502a9609e3f139e49cd/src/planar-media.js) and [observables.js](https://github.com/physicsvigilante/opticsim/blob/6091256df8d22e62f6f9d502a9609e3f139e49cd/src/observables.js) confirms that this remains native SingleRay/PlaneGlass/Detector composition. Detector capture snapshots the actual incident point and direction before delegating once to the native detector callback. Observable qualification still requires matching canonical hash, completed successful execution and complete count-matched event evidence, with explicit Fresnel-omission warnings. The stale/incomplete cases suppress values rather than borrowing mathematical success.

**Interpretation boundary:** Q is an analytical crossing. Extending a measured outgoing line back to the plane is a derived consistency check, not a measured planar interface point. The apparent-axis intercept is not a perceived or detected image. This experiment does not establish source-object ancestry, a real eye, continuous visibility, multiple-interface inversion or general image reconstruction.

## 5. Builder CI — verified with explicit evidence limits

The GitHub Actions listing filtered to exact source HEAD returns **11 workflow runs**; the same listing filtered to successful conclusions also returns **11**. Thus **11/11 exact-source workflow runs succeeded** at inspection. This is current API evidence, not an inference from a green PR description.

I inspected the decoded [plane-mirror job log, job 134769809900](https://github.com/physicsvigilante/opticsim/actions/runs/44295048389/job/134769809900). It explicitly shows checkout of `refs/remotes/pull/149/merge` at **`ab180839eb6fcae09aca4783a5129ccff70dc057`**, setup of pinned PhyDemo **`811f508d2b070898c241a568b0c167dcb8645251`**, construction of its headless test core, and **800 tests / 800 pass / 0 fail / 0 skipped**. The log includes the new named R3 P1 regression and all four relevant markers:

`JEE_OBSERVER_GRAZING_INGRESS_WITHHELD`, `JEE_OBSERVER_LOCAL_ROOT_WITHHELD`, `JEE_OBSERVER_NATIVE_ARRIVAL`, and `JEE_OBSERVER_NATIVE_SUPPRESSION`.

The new marker contains normal 135 degrees, spans +27300/-27300 mm, ingress withholding and false native-ray/image flags. The original positive marker contains the actual detector hit reported above.

For [optical-composition run #44295048428, job 134769809279](https://github.com/physicsvigilante/opticsim/actions/runs/44295048428/job/134769809279), I verified the exact source association, completed/success job status and successful setup, test, build, browser acceptance and hosted-path browser acceptance step records. **I did not separately inspect that second job's decoded full log or its screenshots.** Consequently this report does not invent screenshot counts, a Chrome version, or an independent visual verdict.

Run metadata's source `head_sha` and the actual merge checkout are different objects; this is normal for pull-request CI. Here the raw checkout log plus independently verified identical trees establishes the necessary source-to-CI linkage. Tree equality does not convert builder execution into independent reviewer execution.

## 6. Nonblocking improvements and next development boundary

**N1 — Make numerical refusal evidence more self-describing.** A follow-up may retain incoming/outgoing normal cosines and threshold in diagnostics, explicitly test null outgoing/depth as well as the already-asserted fields, and exercise the guarded native-witness refusal with zero-call instrumentation. Adding near-threshold and both-grazing precedence regressions would make future changes easier to audit. These are coverage/diagnostic improvements, not a demonstrated bypass or blocker in R3.

**N2 — Keep the future public contract separate from this helper.** A separately reviewed typed source-observer-one-plane query still needs closed input validation, declared units/frame/indices and bounds, distinct physical/numerical/native-evidence statuses, and an explicit accuracy policy. The 0.02 checks must not become a promise of observer-point accuracy throughout the full coordinate envelope. Native success must still be measured and freshness-gated; optional native verification must not silently invent brightness, Fresnel policy, numerical settings or apparatus.

Recommended next scope: design that bounded analytical query and its result/provenance contract using this corrected study, without treating the private test helper as a release-ready inverse API. Broader native boundary qualification remains future work.

## 7. Evidence provenance and final boundary

**Independently performed here:** Git commit/PR/diff inspection; targeted exact-source audit; exact-source Actions status and job-step inspection; one decoded builder job-log inspection; 12 standalone Node.js scalar reference/control cases; and separate 90-digit stationary/rounded-heading calculations for selected cases. The independent arithmetic used Node.js v22.16.0 and Python with mpmath 1.3.0, not the builder's Node runtime.

**Not performed here:** Opticsim installation/build/full test-suite execution, native PhyDemo replay, Chrome/browser execution, screenshot review, or an exhaustive proof over the coordinate/material envelope. Neither extreme ingress case was executed in native PhyDemo by this reviewer. No native solver defect follows from the idealized rounded-heading calculation.

Only this new review report is published to review_sandbox. No Opticsim source or earlier review is changed, no PR is merged or approved for release, and no release/deployment permission is granted. CI-only #149 was already closed unmerged; #148 remains draft/unmerged at the checked head. Branch-protection issue #123 is neither evaluated nor resolved by this review, and unrelated held feature/release gates are unchanged.

**Final verdict: CLEARED FOR NEXT SCOPED DEVELOPMENT — the R2 incoming-grazing P1 is corrected at source HEAD `6091256df8d22e62f6f9d502a9609e3f139e49cd`, within the explicitly conservative, test-only scope.**
