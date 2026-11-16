# Opticsim PR #89 — Stage-1 opt-in finite-hit diagnostic merge and post-merge verification

**FINAL RELEASE STATUS: OWNER-APPROVED MERGE COMPLETE; ALL ELEVEN POST-MERGE WORKFLOWS PASSED.** This is a Chat A-written release record, **not** a new Chat B review, independent physics certification, school-use evaluation or public deployment.

## Source identity and owner merge authorization

- Source [PR #89](https://github.com/physicsvigilante/opticsim/pull/89): **merged into `main` following explicit separate owner approval**.
- Original base/main: `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`; **exact separately reviewed implementation source head**: `e8889ce9a3771d4079d7f50070f341cbe5cddaa9`.
- **GitHub merge commit / main at verification: `50dd0f4d9530d0a61bb4c7064c4326a8ac0ce518`** — [merge commit](https://github.com/physicsvigilante/opticsim/commit/50dd0f4d9530d0a61bb4c7064c4326a8ac0ce518).
- The merge's **two parents** are exactly the original base and reviewed PR head, in that order. Its Git **tree `fde9f16890299eb2bdc8252bf05ff7191c74c946` is identical to the reviewed source head's tree**. No content-conflict resolution, new production code or unintended merge edits.
- Pinned PhyDemo **`811f508d2b070898c241a568b0c167dcb8645251`** and Node **24.19.0**, existing scene schemas, native ray routing, physical material laws, numerical tracer cutoffs, source/detector power and historical no-opt-in output shape remain unchanged.

## Independent review lineage and preserved failures

- The pre-implementation [PR #88 Chat B review-01](../pr-88/reviews/review-01-chat-b.md) requested changes; its [revised design review-02](../pr-88/reviews/review-02-chat-b.md) **PASS applies to DESIGN ONLY**, not a code release.
- [PR #89 independent Chat B full R2 implementation review-01](reviews/review-01-chat-b.md) **CHANGES-REQUESTED** for earlier head `3f2d31aa19a851d92a8d1c46ede2249c52e0e223`: F-01 near-parallel false clean and F-02 malformed source false clean were independently demonstrated in an isolated source harness; F-03 warning precedence clarification requested. This report remains unchanged and valid for that earlier SHA.
- Developer created the explicit **test-only falsification** first, [red unified CI 43832903891](https://github.com/physicsvigilante/opticsim/actions/runs/43832903891), **764/766 Node passes, exactly F-01/F-02 failures**; F-03 already passed. The early implementation test-fixture failures [43825711560](https://github.com/physicsvigilante/opticsim/actions/runs/43825711560) and [43826462305](https://github.com/physicsvigilante/opticsim/actions/runs/43826462305) likewise remain historical and are not recast as successful first attempts.
- [PR #89 independent Chat B targeted R2 implementation review-02](reviews/review-02-chat-b.md) **PASS for F-01/F-02/F-03 corrections**, *at exactly the merged source head* `e8889ce9a3771d4079d7f50070f341cbe5cddaa9`. Independent reviewer executed novel source-function/adversarial mocks, independently rehashed original source-run native/Chrome archives and checked the GitHub synthetic CI merge tree. **No new independent pinned-native PhyDemo or real-Chrome run was executed by Chat B**. This is separate-context LLM review, not independent human optical adjudication.
- [Developer response to second review](responses/response-02-chat-a.md) preserves all finding limitations. Approval was given to **merge PR #89 only**; research-only PRs #87/#88 and mandatory Stage 2 are not merge/release candidates.

## Full CI on the new `main` merge commit

All **11 distinct push-event GitHub Actions workflows completed with conclusion `success`**, each with `head_sha=50dd0f4d9530d0a61bb4c7064c4326a8ac0ce518`.

| Post-merge workflow | GitHub run |
|---|---|
| Unified problem workflow checks | [43839317868](https://github.com/physicsvigilante/opticsim/actions/runs/43839317868) |
| Plane-mirror angular inverse checks | [43839318010](https://github.com/physicsvigilante/opticsim/actions/runs/43839318010) |
| Original refraction problem pair | [43839318027](https://github.com/physicsvigilante/opticsim/actions/runs/43839318027) |
| Deterministic planar angular query checks | [43839317877](https://github.com/physicsvigilante/opticsim/actions/runs/43839317877) |
| Parameter experiment checks | [43839318047](https://github.com/physicsvigilante/opticsim/actions/runs/43839318047) |
| Curved mirror checks | [43839317884](https://github.com/physicsvigilante/opticsim/actions/runs/43839317884) |
| Numerical ray reliability diagnostics | [43839318100](https://github.com/physicsvigilante/opticsim/actions/runs/43839318100) |
| Qualified authoring checks | [43839317905](https://github.com/physicsvigilante/opticsim/actions/runs/43839317905) |
| Optical composition checks | [43839317873](https://github.com/physicsvigilante/opticsim/actions/runs/43839317873) |
| Quasi-static source motion checks | [43839317920](https://github.com/physicsvigilante/opticsim/actions/runs/43839317920) |
| Planar refraction checks | [43839317914](https://github.com/physicsvigilante/opticsim/actions/runs/43839317914) |

**Exact post-merge unified job `133203726817`** logs: **766/766 Node tests passed, zero failures**; **8/8 actual pinned-native synthetic public acceptance cases passed**, **10/10 real Google Chrome acceptance checks passed**, with two screenshots. These tests establish declared software/geometry invariants, not universal physics accuracy or correctness of independent original textbook interpretation.

**Eight actual pinned-native public cases** from retained `acceptance.json`: normal-and-detector (`completed/checked`, 2 Glass incidents), valid-zero-glass-hit (`completed/checked-no-hit`, 0), zero-detectors (`completed/checked`, 2), two-detectors-two-sources (`completed/checked`, 4), four-sources (`completed/checked`, 8), full-Fresnel weak branches (`incomplete`, no accepted advisory), full-Fresnel-matched-index (`completed/checked`, 2), exposed-rotated-computed-critical (`completed/inconsistent`, **4 actual callbacks**). Previous exact-same-input critical CI runs had 5 or 6 callbacks; **the native exact-critical trace is run-to-run variable**, and this software neither repairs it nor prescribes a preferred physical branch.

**Ten actual real-Chrome checks** from archived `report.json`: requested advisory visibility and ordinary detector readouts, qualified export without old ray data, fresh reimport, valid sampled zero-hit, two-source/two-detector behavior, native full-Fresnel incomplete suppression, completed equal-index Fresnel, critical-case caution with native status preserved, raw-import clearing, and A→B→A import/re-execution revision check. Google Chrome **157.0.8103.50**. Nine recorded browser import-to-current-result wall times **28–65 ms** in this CI environment; **not** a proved worst-case cost or a numerical physics performance bound. Separate controlled delayed callback unit test exists; the browser A→B→A import sequence is **not** an independently injected truly delayed old native callback.

### Independently rehashed NEW post-merge artifacts

- [Native public artifact **14211653273**](https://github.com/physicsvigilante/opticsim/actions/runs/43839317868/artifacts/14211653273), GitHub SHA-256 `93ced255ca4df2a29a9e127828bac932c14547d09e4f002b7c43634e0e014be3`.
- [Real-Chrome artifact **14211823710**](https://github.com/physicsvigilante/opticsim/actions/runs/43839317868/artifacts/14211823710), GitHub SHA-256 `380776524e49a0349fa01e23a59359e1306dcdd9ece67d5ea7fb856c9fe85347`.

**Chat A downloaded both *post-merge* ZIPs and computed their SHA-256 independently**, matching GitHub's metadata. Inspected all eight actual public `input.json`/`report.json` pairs, each source request SHA-256 match, `acceptance.json`, real Chrome `report.json`, two screenshots and qualified/raw export file listings. Browser ZIP retained only `report.json`, two screenshots, raw scene and qualified scene, with **no browser profile/cache**. These are independently rehashed evidence *bytes*, but still Chat A-authored CI experiments; no independent Chat B post-merge execution is claimed.

## Exactly what is now on production `main`

The new opt-in `finite-hit-numerical-diagnostic` applies only to existing admitted schema v9, one strictly convex four-vertex Glass, 1–4 explicit SingleRay sources and 0–2 passive external detectors. It snapshots actual native pre-mutation ray/incidence scalars without changing the original native call; bounded exact binary64 math evaluates finite-edge forward and reported-point consistency **after** the run. A robust represented contradiction appears as **`inconsistent`**, while unproved point error, near-parallel conditioning, unknown method coverage, valid shallow uncertainty and 129th callback are **`unknown`** (not a false pass). A valid no-hit is only a sampled `checked-no-hit`, never continuous darkness. A native-incomplete run cannot supply a complete diagnostic. A result `status:'advisory'` is *not* counted as a solved physical measurement or textbook question. A clean subset of necessary checks is **not** a physics-validity certification.

**In Stage 1, existing canonical detector power, interface/detector counts and qualified readouts are *not* suppressed or corrected by the advisory.** A proven discrepancy must display a prominent **NOT independently certified** caution. No existing no-opt-in scene/output changes, new native material law, LLM connection or public deployment occurred.

**Nonblocking limits:** observer behavioral neutrality under unstable critical dynamics is not independently proven; native reported point tolerance envelope is intentionally not invented; legitimate near-parallel hits may conservatively be `unknown`; the 128-event diagnostic cap may make long native full-Fresnel scenes unavailable; exact/near-critical branch correctness is not universally guaranteed; independently measured student or teacher benefit was not assessed.

## Explicit exclusions / next decision

- Research-only [PR #87](https://github.com/physicsvigilante/opticsim/pull/87) and design/research-only [PR #88](https://github.com/physicsvigilante/opticsim/pull/88) remained **open, draft, unmerged** at release verification. Their temporary research workflow steps and historical first failures are not part of this release.
- **Stage 2 mandatory v9 numerical measurement withholding remains UNIMPLEMENTED and UNAUTHORIZED**, requires a separate owner policy/evidence decision, code/Chrome integration and independent R2 review. It may not be inferred from Stage-1 release.
- No public deployment or separate LLM API integration was authorized or performed.

**Release outcome: PR #89 merged, source tree identical to reviewed head, 11/11 post-merge CI green, 766/766 Node, 8/8 actual native public cases, 10/10 real Chrome checks.**
