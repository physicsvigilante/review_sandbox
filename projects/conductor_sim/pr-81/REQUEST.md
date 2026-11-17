# M35a PR #81 — Audit corrections and bounded multi-stage physical exploration

**Developer-authored request, not an independent PASS. PR #81 is draft and unmerged. Recheck live source and CI; preliminary evidence below does not authorize merge.**

## Immutable review target

- Production PR: https://github.com/physicsvigilante/conductor_sim/pull/81
- Candidate HEAD: `81304609f04f87a54a689486ece5b2d3b5f3a963`
- Actual Git tree: `0f3272a0094e2572d96882f8c151460c4ce77965`
- Released M34b base: `a5113fa4cc924ac10cbb35b2f2d7ac80e11f1bde`, tree `d0646c9e4d518008784c42c1fec1c48c81901a09`
- Original charter-only commit: `ba19e12c519df2338df5dbb9293e9fa7ebd611a8`
- Branch: `m35a-multistage-exploration-audit`
- Required new independent report: `projects/conductor_sim/pr-81/reviews/review-01-chat-b.md`

Read repository-root PROTOCOL.md, REVIEW-RISK-POLICY.md and REVIEW-TEMPLATE.md; production root AGENTS.md if present; pinned `docs/m35a_charter.md`, `docs/m35a_audit.md`, `docs/m35a.md`, and `docs/current_capabilities.md`. Exact diff: https://github.com/physicsvigilante/conductor_sim/compare/a5113fa4cc924ac10cbb35b2f2d7ac80e11f1bde...81304609f04f87a54a689486ece5b2d3b5f3a963 . A changed source HEAD/tree makes this request stale.

## What changed and why it requires R2

The user requested a thorough project audit, errors corrected or planned, then M35a. Audit corrections and feature work are separate commits. The candidate fixes two related nested-request validation defects and an extreme-scale direction-normalization defect; the full audit documents additional risks and a genuinely open legacy result-wrapper problem.

1. **Current nested request invariants:** a valid native WorldComparison mutated to reference the same world on both sides used to pass a surrounding fork plan and produce an issued `compared` record. A mutated unknown observation mode could enter event-study refusal rather than fail authoring validation. Candidate revalidates nodes, structural cases, physical edits, pairs, typed questions and policy before numerical action and at export. Validation must not renormalize or mutate caller-owned native objects.
2. **Subnormal direction:** `(ulp(0),ulp(0),0)` previously normalized to `(1,1,0)` because its norm was under-resolved. Candidate scales only the subnormal norm path; normal finite arithmetic and the M34a one-ULP retention rule stay unchanged. Genuine off-plane forces/launch/gravity, zero and nonfinite vectors remain refusals.
3. **M35a:** GraphWorldForkPlan can continue from an authentic prior GraphWorldForkRun. Graph event inquiries can target authentic fork history. Shared iterative per-call history validation checks root and each ancestor receipt/native binding, detects cycles before work, retains exact old objects, and integrates only newly admitted worlds. No mutable validation cache persists across calls.
4. Multi-stage fork/inquiry opt into v2 schemas binding immediate source digest, original root digest, ordered prior stages and cumulative scope. Original graph v1/v2/v3, direct M34b fork v1 and original graph inquiry v1 remain unchanged on tested legitimate inputs. At most 8 fork stages, 32 cumulative requested nonbaseline worlds (including refusals), depth 12, 1..5 new worlds and 12 physical edits per stage; direct first-fork bounds remain 12 total/depth 6. No ID/retired-source/history reset.
5. New read-only dependency-aware PR/main scientific aggregate runs historical M32a–M34b references and the new audit/multistage transfer on broad source/test/example/tool changes. Old FEMM and Chromium workflows are retained. Temporary transfer blobs/write-enabled staging workflow were removed from the candidate tree; the published tree exactly equals locally tested source plus charter/final CI.

**Boundary:** repeated exploration calls within one Python process. No durable process-restart restoration, trusted JSON importer, merge of divergent histories, concurrent editing, arbitrary 3D solver, new field law/FEMM backend, moving-source dynamics or scene graph.

## Explicit open finding — do not conceal it

Issue #80 https://github.com/physicsvigilante/conductor_sim/issues/80 reproduces legacy EventSweepRun/TrajectorySweepRun accepting `complete` with missing model/native data after public dataclass replacement. It is not fixed by M35a and must not be described as fixed. Those weaker result types are not accepted as M35a source histories; evaluate that containment and whether the documented separate migration is adequate. No generic claim that every historical export has the newer receipt guarantee.

## Developer evidence, distinct from your review

- Original audit run 44098354148 and exact-source snapshot run 44108932124 in review_sandbox retain released reproduction/source. Downloaded artifact ZIP/file digests were actually checked locally, and reconstructing the Git tree matched released M34b exactly.
- Local Python **3.13.5** baseline: 1,991 passed, 97 real-FEMM deselected. Candidate final local suite: **2,030 passed, 97 deselected, 13 warnings**. These are not the 3.10/3.12 CI results.
- Retained local fixture failures: duplicate source display label, then expanded depth test repeating the same mass (correct no-op refusal, 2,029 passed plus one test failure). Fixture corrected; final whole suite passed. No source physics guard was weakened to make the fixture pass. An interrupted test process was not counted as PASS.
- New example/reference: three stages, ten admitted physical worlds, 210 actual saved three-component samples, 126 literal comparison rows, four fresh M24a inquiries and seven intentional detached-evidence tamper controls. `tools/m35a_independent_multistage.py` imports **no conductor_sim**.
- `tools/m35a_audit.py` obtains actual values from production but independently calculates E=-grad(V), 16,000-element rod/ring Coulomb quadrature, and a full-period nonuniform Coulomb circular orbit. Finite selected cases passed; no exhaustive field-law theorem claimed.
- Fifteen aggregate historical/new native/reference commands passed locally. Five complete legacy source-native output files were byte-identical to released M34b.
- Actual exact-source PR CI (Python 3.10/3.12, 97 real FEMM, historical Chromium and new aggregate) was still running at first packet publication. See STATUS.md and query current GitHub conclusions. No independent separate-context report yet.

## Mandatory independent reviewer challenges

Reproduce original defects on the exact released source and their rejection/correction on the candidate. Independently author a physically unfamiliar non-dyadic oblique qE+mg graph and at least three successive stages, including structural→physical→replacement/removal, a rejected retired-ID resurrection, an unaffected sibling and fresh event inquiries on later-stage worlds. Independently compute saved SI states/forces/roots, not from developer oracle. Add a nonuniform field reference where practical.

Instrument native assembly/revision/integration to prove old model/assembly/trajectory/event objects remain identical and old output bytes remain unchanged; only new worlds integrate. Test mismatched full event geometry/policy, guards, terminal/multiple/opposite roots and missing physical models. Test stages/world/depth/edit limits without budget resets, duplicate stage/world IDs, cycles, source-run substitution, mutated ancestor model/receipt/native time/root/status and detached JSON isolation. Verify validation does not silently modify numerical evidence.

Compare all five old output forms against released M34b byte-for-byte on an independent valid fixture. Assess nonrecursive history work without claiming constant time in sample count. Inspect the new aggregate workflow's PR/main triggers, explicit read-only permission and pipe-failure propagation. Confirm temp transfer/write workflow absent. Preserve reviewer first failures and distinguish fixtures from production defects.

Publish original report with exact HEAD/tree, reproducible probes, results/limits and **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE**. Do not change production, mark ready or merge. Separate owner expected-head authorization, still-green CI, exact reviewed merge tree and successful actual main postmerge checks are required for release.
