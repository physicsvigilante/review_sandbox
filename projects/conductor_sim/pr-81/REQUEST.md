# M35a PR #81 — Audit corrections and bounded multi-stage physical exploration

**Developer-authored request, not an independent PASS. PR #81 is draft and unmerged. Recheck live source and CI; no merge is authorized by this packet.**

## Immutable review target

- Production PR: https://github.com/physicsvigilante/conductor_sim/pull/81
- **Current candidate HEAD:** `49bab64b06cc4594934a27f9ddbb500c454ba150`
- **Actual candidate Git tree:** `f9d14fedd06659f5abf8f822b31bc7e6353f2a37`
- Released M34b base: `a5113fa4cc924ac10cbb35b2f2d7ac80e11f1bde`, tree `d0646c9e4d518008784c42c1fec1c48c81901a09`
- Frozen charter-only commit: `ba19e12c519df2338df5dbb9293e9fa7ebd611a8`
- Branch: `m35a-multistage-exploration-audit`
- Required new independent report: `projects/conductor_sim/pr-81/reviews/review-01-chat-b.md`

Read repository-root PROTOCOL.md, REVIEW-RISK-POLICY.md and REVIEW-TEMPLATE.md; production root AGENTS.md if present; pinned `docs/m35a_charter.md`, `docs/m35a_audit.md`, `docs/m35a.md`, and `docs/current_capabilities.md`. Exact diff: https://github.com/physicsvigilante/conductor_sim/compare/a5113fa4cc924ac10cbb35b2f2d7ac80e11f1bde...49bab64b06cc4594934a27f9ddbb500c454ba150 . A changed source HEAD/tree makes this target stale. Earlier request HEAD `81304609f04f87a54a689486ece5b2d3b5f3a963` is superseded, not silently relabeled as the current validated source.

## What changed and why it requires full R2

The user requested a thorough project audit, errors corrected or planned, then M35a. The audit is a repository-wide inventory plus targeted source, numerical and hostile-data examination, not an exhaustive proof of all ~20,000 production lines. Audit corrections, feature implementation and fixture/CLI corrections are distinct commits. Three demonstrated released-source faults are corrected in this candidate; an important legacy result-wrapper defect is explicitly OPEN.

1. **Current nested request invariants:** a valid native WorldComparison mutated to reference the same world on both sides passed a surrounding fork plan and produced an issued `compared` record. A mutated unknown observation mode could enter event-study refusal instead of failing authoring validation. Candidate revalidates nodes, structural cases, physical edits, pairs, typed questions and policy before numerical action and at export. Validation must not renormalize or mutate caller-owned native objects.
2. **Subnormal direction:** `(ulp(0),ulp(0),0)` previously normalized to `(1,1,0)` because its norm was under-resolved. Candidate scales only the subnormal norm path; ordinary finite arithmetic and the M34a one-ULP retention rule stay unchanged. Actual out-of-plane forces/launch/gravity, zero and nonfinite vectors retain refusal boundaries.
3. **M35a multi-stage composition:** GraphWorldForkPlan accepts an authentic prior completed GraphWorldForkRun. Graph event inquiries can target authentic fork history. Shared iterative per-call history resolution validates the root and each ancestor's native evidence/receipt, detects cycles before work, retains exact old objects and integrates only new admitted worlds. No mutable cross-call validation cache is retained.
4. Continuations opt into fork v2 and inquiries on fork history into inquiry v2. They bind the immediate history digest, original root digest, ordered prior stages and cumulative limits. Original graph v1/v2/v3, direct M34b fork v1 and original graph inquiry v1 are byte-identical on tested unchanged real inputs. Bounds: 8 fork stages, 32 cumulative requested nonbaseline worlds including refusals, physical depth 12, 1..5 new worlds and 12 physical edits per stage. Direct first-fork bounds remain 12 total/depth 6. Stage/world identity and retired-source budgets must not reset.
5. **Documentation/CI:** current capability index distinguishes released M34b from draft M35a. A dependency-aware, read-only PR/main scientific aggregate reruns M32a–M35a references on broad source/test/tool/example changes, retains failed evidence and pins actual source/tree. Historical real FEMM and Chromium checks remain. Temporary publication/transfer files are absent from final candidate tree.
6. **Clean-checkout execution correction:** initial aggregate CI reached command 15 then failed to import checkout-only `examples`. Run candidate audit and legacy snapshot as Python modules from repository root; baseline invocations explicitly select the old source/examples. Three subprocess regressions remove PYTHONPATH. The audit independently asserts the actual imported production/example paths. Its malformed-mode red-before probe now reaches the intended mode gate, and all three red/green outcomes are asserted individually.

**Physical/session boundary:** repeated exploration within one live Python process. No durable process-restart restoration, trusted JSON importer, merging divergent histories, concurrent editing, unrestricted 3D solver, new field law/FEMM backend, moving-source dynamics or scene graph.

## Explicit open finding — do not conceal it

[Issue #80](https://github.com/physicsvigilante/conductor_sim/issues/80) reproduces legacy EventSweepRun/TrajectorySweepRun exporting `complete` with missing model/native data after public dataclass replacement. It is NOT fixed by M35a and must not be described as fixed. Those weaker result types are not accepted as M35a source histories. Evaluate containment and the adequacy of a separate status/native consistency and issued-result migration. Avoid generic claims that every historic output has modern receipt guarantees.

Other audit findings: growing private-module coupling, duplicated CI versus transitive dependency gaps, release-documentation drift and main branch protection absent in the inspected API response. Some are mitigated here; broader service extraction, legacy hardening, measured CI consolidation and owner-side server-enforced release gates remain planned. No branch administration, historical PR closure or production merge was performed.

## Developer evidence — separate from your original review

- Released source archived and downloaded; ZIP and retained file digests actually rehashed. Full source Git tree reconstructed exactly as `d0646c9e4d518008784c42c1fec1c48c81901a09`.
- Corrected candidate aggregate [run #44126201544](https://github.com/physicsvigilante/conductor_sim/actions/runs/44126201544): **SUCCESS on literal current HEAD/tree**, 42 focused tests, all 15 native/separate-form reference commands, and five legacy record comparisons. Artifact #14347851729 ZIP SHA256 `0d8218bd9829125dc54749e13e102c31adc6f670498ce284bcce69bc70c3b7cf` was actually downloaded and rehashed; all 59 files in SHA256SUMS verified. Reconstructing its source archive Git tree gives current `f9d14fedd06659f5abf8f822b31bc7e6353f2a37`, identical to the locally tested tree.
- Same audit script under exact baseline/candidate: released accepts self-pair and malformed mode, and emits nonunit subnormal direction; current candidate rejects both malformed requests and returns genuinely unit `(0.7071067811865475,0.7071067811865475,0)`. No numerical solver was changed to conceal a test failure.
- Supplemental local **Python 3.13.5** complete non-FEMM suite: **2,033 passed, 97 deselected, 17 warnings**. Local all 15 reference commands passed and five native legacy output files are byte-identical. This is not the 3.10/3.12 CI matrix; check those live separately.
- New multi-stage example/reference: three stages, ten admitted worlds, 210 actual three-component saved SI states, 126 literal comparison rows, four genuinely fresh M24a inquiries and seven deliberate detached-evidence tamper controls. `tools/m35a_independent_multistage.py` imports NO conductor_sim.
- Companion audit independently calculates E=-grad(V), 16,000-element finite-rod/tilted-ring Coulomb quadrature, and a full-period nonuniform Coulomb circular orbit with 65 saved native samples. Native production functions supply actual measured values; independent equations supply expectations. Finite selected cases, not an exhaustive field-law theorem.
- Five complete historical graph-v1/v2/v3, direct-fork-v1 and inquiry-v1 JSON records are byte-identical to released M34b. The CI's baseline/candidate imports are explicitly checked to avoid accidentally comparing the candidate to itself.
- Full current-head CI conclusions and individual Python/FEMM/Chromium results are tracked in STATUS.md and must be rechecked live. Developer CI is not independent Chat B science.

## Preserve failure chronology

Initial source aggregate [#44120203390](https://github.com/physicsvigilante/conductor_sim/actions/runs/44120203390) FAILED after its 39 focused tests and first 14 reference commands passed: command 15 could not import the checkout-only examples namespace. Artifact #14345335833, ZIP SHA256 `9dadd210c4f3548cc4fc1b432542cceacb17442993ccd50bdc575996e8429c3f`, was downloaded and its file digests checked. It remains an original failed run; legacy comparisons were skipped then and cannot be claimed as passing on that attempt. Current correction also repairs the latent candidate legacy-snapshot invocation and the audit probe that originally reached an earlier policy gate.

Earlier local fixture failures (duplicate source display label, repeated unchanged mass producing a correct no-op refusal), and an interrupted timed-out local invocation are retained and not counted as fully passing runs. The final completed local validation and corrected CI are distinct later executions. No native physical guard was weakened for those fixtures.

## Mandatory new reviewer-authored challenges

Reproduce all three original faults against the exact released source and their rejection/correction on the current candidate. Check ordinary unit-vector results remain exact, smallest subnormal directions are stable, and real off-plane/source/initial-state failures remain rejected. Confirm nested validation never mutates previously issued normals, questions, models or results.

Independently author an unfamiliar non-dyadic oblique qE+mg source graph and at least three successive stages, structural→physical→replacement/removal, rejected retired-ID resurrection, unaffected sibling and fresh inquiries on later-stage worlds. Compute your own saved SI positions, velocities, forces and signed roots, not from developer oracle. Add a nonuniform field reference where practical.

Instrument native assembly/revision/integration to establish exact earlier model/assembly/native object reuse and unchanged earlier output bytes, only new-world integrations for physical forks, genuinely fresh integrations for new event inquiries. Test geometry/policy mismatches, guards, terminal/multiple/opposite roots and physically absent models.

Exercise cumulative stage/world/depth/edit limits, including refused nodes, duplicate inherited stage/world IDs, cycles, source-history substitution, malformed stage class, forged ancestor model/receipt/native sample/root/status, pre-export mutation and detached JSON isolation. Assess iterative history validation without claiming constant-time work in total sample size.

Independently compare all five old format outputs against released M34b byte-for-byte on your own valid fixture. Inspect clean-environment CLI behavior, explicit root imports, PR/main aggregate triggers, read-only permissions, failed evidence retention and absence of temporary publication workflow. Evaluate issue #80 containment honestly rather than asserting every legacy wrapper is secured.

Publish an original report with exact HEAD/tree, independently authored experiments, evidence and scope limits, reproducible findings and **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE**. Do NOT modify production, mark ready or merge. Separate owner expected-head authorization, still-green CI, exact reviewed merge tree and successful actual main postmerge checks are required for release.
