# SIM_HEAT H3-07 PR #25 — targeted independent R2 review: shared-run SHA and refused-comparison hygiene

**projectId:** `sim_heat`  
**sourceRepo:** `physicsvigilante/sim_heat`  
**sourcePR:** [draft PR #25](https://github.com/physicsvigilante/sim_heat/pull/25) — open and unmerged.  
**baseSha:** `8aa18488f949c6d1b506d80e44afc2a25e71b2c7` — independently reviewed and merged H3-06 source-pair provenance.  
**headSha:** **`d5be85cb4c0b3bc079a12bb5ccea0a7c143ebf9c`** — exact pinned review candidate, not floating branch.  
**gitTree:** **`05fa0292e0ad049dd7c3bcee242087ea71459425`**.  
**reviewClass:** **R2**, targeted correction of native source-evidence interpretation and user-visible refused-state behavior.  
**reviewDestination:** `projects/sim_heat/pr-25/reviews/review-01-chat-b.md` — independent Chat B only.  
**status:** awaiting targeted independent R2 review. Standing owner approval for review-passed routine merge **does not** waive this review; PR #25 remains unmerged.

## Origin and bounded scope

Independent [Chat B PR #23 Review 01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-23/reviews/review-01-chat-b.md), original Git blob `40348889573386b135dbf847fdd53b0ffabcff71`, returned **scoped R2 PASS** on source `439c02ae3157f01c8ccc7ab5eb58297af0c17d92`. It found **two nonblocking minor future-comparison issues**, not any defect in the current authenticated D2→D2-K2 physical/numeric result:

- **F-01:** coherently repinned pair source fields may claim **one GitHub Actions run** with **different per-side executed commit SHAs**, even while selecting different valid original archived output slots. The reviewer requested an explicit same-run `compiledSourceCommit` policy and negative tests before introducing new shared-run native pairs.
- **F-02:** a refused comparison already hides its inspector and chart, but stale native numeric/source-label **DOM text** could remain *inside the hidden inspector*. The old browser tests covered a fresh-page refusal, page reload or delayed return, not a **same-page valid→refused→valid selection**. No stale visible values were demonstrated; reviewer requested stronger hygiene and actual browser regression.

This PR addresses only F-01/F-02, tracked in [Issue #24](https://github.com/physicsvigilante/sim_heat/issues/24). It is **not** a new physics law, new native archive, second published what-if pair, new component, H1-C1 transfer or broad re-review of original MAT/calculation.

## Exact source diff and intended meaning

Compare [base → exact candidate](https://github.com/physicsvigilante/sim_heat/compare/8aa18488f949c6d1b506d80e44afc2a25e71b2c7...d5be85cb4c0b3bc079a12bb5ccea0a7c143ebf9c). Exactly **8 changed paths**:

- **Generic source-consistency:** `viewer/network/tools/build_compare_index.py` and `viewer/network/compare_core.mjs` now explicitly require that `baseline.runId == successor.runId` implies `baseline.compiledSourceCommit == successor.compiledSourceCommit`. A GitHub Actions run has one `GITHUB_SHA`; regardless of one versus multiple archive ZIPs, the two source strings must match. A run may still carry distinct case output slots. The existing same-artifact ID + identical run/whole-ZIP policy and refusal of repeated exact `runId/artifactId/archiveEntry` slots remains. Different authentic GitHub runs may have different source commits.
- **Generic refused UI:** `viewer/network/compare.mjs` `clear()` now empties all cached native values, source links, model labels, chart/time/gap text, disabled slider and observation selector state, while preserving an enabled pair selector for recovery. It does **not** change display arithmetic, native K/J/W, H1 laws, actual source-case data or original time-grid policy.
- **Adversarial tests:** `viewer/network/tests/test_compare_source_pairs.py` adds a coherent SHA-repin **test-only** source-plan + child source-case/catalog mismatch: same run ID, **divergent** commit strings must yield typed `pair_provenance` refusal from the **real production** `compile_pair_index`, not just a surrogate validator. Additional positive test-only structurally coherent repin demonstrates that same run/commit with distinct original artifacts can internally pass; **not independently GitHub-attested native evidence**. `viewer/network/tests/compare.test.mjs` adds JS pure-validator same-run same/different artifact/slot and divergent-commit negatives. `viewer/network/tests/browser_smoke.py` adds actual Chromium **same-page valid→refused→valid** regression using a *test-only second menu label of the exact same approved D2→D2-K2 source pair* with a wrong expected successor commit: after displayed actual +12/+24 W and original run links, selection must refuse and clear chart, purge **hidden DOM text via `text_content()`**, reset/disable controls and allow recovery to the original authentic source pair on the same page.
- **Documentation/CI only:** `docs/H3_07_SHARED_RUN_REFUSAL_SCOPE.md` and one branch-only `.github/workflows/h3-shared-run-ci.yml`. No new OpenModelica execution or source-evidence trust class.

**Preservation:** H1 `model.py`, `study.py`, original library, native runner, checking reference/verdict, numerical/time policy, all six previously published source-native case JSON files, `viewer/network/data/compare_sources.json` / `compare_index.json`, default standalone `app.mjs` / `core.mjs`, original native ZIP files and H1-C1-F0 frozen packet are unchanged. Original failed older CI and historical reviewed PR #23 remain preserved. Only the eight paths listed above differ.

## Authentic original source boundary, never upgraded

Current single published teacher comparison remains **H1_D2 → H1_D2_K2**, already independently reviewed in PR #19 and PR #23. Parent two-body insulated system uses original `rod.k=100 W/(m K)`, successor hypothetical `rod.k=200`, with every other physical value/topology/initial condition unchanged. Time is genuine 0..9375 **seconds**, 1001 distinct native saved times with 21 matching preview samples. Signed native rod power flows from `port_a` to `port_b`; original body temperatures K, relative energies J and heat flows W remain as archived, not browser computed. Asymptotic equilibrium 308.15 K does **not** imply finite-time arrival.

- Original D2 run [43691263273](https://github.com/physicsvigilante/sim_heat/actions/runs/43691263273), artifact **14152886226**, full original ZIP SHA-256 **`8fc38b9e2f040b48ab5cbeab34e8698b7c99c4d462a1e31e8bc33b0395185379`**, original executed commit `1b68b14dd05c5eb8f148b02055890563cdc32095`.
- Original D2-K2 run [43693191224](https://github.com/physicsvigilante/sim_heat/actions/runs/43693191224), artifact **14153251022**, full original ZIP SHA-256 **`dc32a0a36a27f031ce7a13da83ebdd26a3dd6ac1d14612fa597b36cb439f4843`**, original executed commit `52b1635932a3e4519b91f3bf093c0c21b0248d91`. Its four-batch source history stays intact.
- Each output remains `diagnostic_only`, `nativeQualified=false`. **Internal metadata consistency cannot independently authenticate an arbitrary fully self-pinned forged ZIP/run/commit**; separately trusted GitHub run/commit/artifact/original full-ZIP digest remains mandatory before another real native pair.

No native run or real numeric reference recomputation was needed for this targeted semantics/DOM work. No claimed new sensor/physical measurement, R3 qualification, unrestricted LLM authoring, symbolic/inverse simulation, physical rod geometry or classroom efficacy.

## Exact-head CI, artifacts, executed and skipped checks

[**Final CI #43876894794**](https://github.com/physicsvigilante/sim_heat/actions/runs/43876894794) is `completed/success` on the **exact HEAD `d5be85cb4c0b3bc079a12bb5ccea0a7c143ebf9c`**. It performed:

- H1 offline regression **151/151**, analytics **4/4**.
- Python adapter/test methods **33 discovered: 32 executed/passed, one optional authentic historical campaign ZIP replay deliberately SKIPPED** because normal source CI does not ship expiring GitHub original artifacts. Do not count that skipped test as a CI pass; previous H3-05 authentic-original replay was separate author-local test, not reviewer-owned new native evidence.
- Node JavaScript comparison/adapter **24/24 passed**.
- Real desktop/mobile Chromium smoke covering six historical native cases, original steady mode/refusals, normal D2→D2-K2 comparison, invalid metadata, delayed async pair response, new same-page valid→refused→valid DOM purge and recovered original native readings. This is **author CI**, not independently rerun browser by Chat B.
- [Final CI artifact 14230601766](https://github.com/physicsvigilante/sim_heat/actions/runs/43876894794/artifacts/14230601766), original ZIP **5,880,269 bytes**, SHA-256 **`2f9e5e110c90304e2577a6e10f057c261d216a29be42600fbe00f0a15658c40a`**; Chat A downloaded original ZIP, independently rehashed bytes/CRC, confirmed **33 members** and `head-sha.txt` equals exact candidate, and inspected the original screenshots `whatif-samepage-refusal-cleared.png` and `whatif-samepage-recovered.png` (not independent Chat B findings).
- Source CI changed no native files and executed **zero** OpenModelica model builds or launches; no historical failed CI is relabeled passing.

## Independent R2 reviewer questions

1. **Same-run SHA:** Does the exact production Python/JS guard reject coherent same-run claims with `compiledSourceCommit` mismatch when artifacts differ **or** agree? Does it permit distinct case slots from one actually authenticated run with one SHA, refuse identical slots, and retain valid different-run/different-SHA native pairs? Is metadata mismatch checked before reading/displaying source values? Test actual functions, not mock assumptions.
2. **External trust:** Confirm the deliberately admitted **test-only coherent fake same-run source** does not get presented as independently authenticated GitHub execution, and no source-manifest mutation/ZIP repin bypasses the separate run/artifact/ZIP external attestation. The old reviewed D2 and D2-K2 identities must remain untouched.
3. **Same-page refusal:** Inspect the real `compare.mjs` `clear` and `fail` functions. Independently test or inspect real Chromium valid→refused→valid using the **same page**; verify DOM text is removed (not merely hidden), source links and numeric values purged, chart cleared, sliders/options disabled, and valid selection recovery shows original actual values. Inspect hidden DOM using `textContent`, not only screenshots if possible. Confirm stale async fetch isolation remains.
4. **Regression and preservation:** Check exact eight-file diff, no change to H1 physics/source/runner/checker/thresholds, six native case data JSONs, v2 source manifest/index, original native MAT/CSV/ZIP and earlier reviewed history. Check exact-head CI and original artifact SHA/CRC/logs; distinguish author CI evidence from reviewer-direct execution.
5. **Scope verdict:** Targeted **R2** on two prior nonblocking minor findings; do not expand into a blanket R3/numeric/model architecture review without a new reason. Report pass/changes-requested/insufficient evidence with reproducible defects. Any future new native pair separately requires GitHub-run original-host attestation, and no full native qualification is claimed.

**Chat B review output:** Write a **new independent** report `review_sandbox/projects/sim_heat/pr-25/reviews/review-01-chat-b.md` following the central [REVIEW-TEMPLATE.md](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-TEMPLATE.md), with exact source head/tree and clear independent-versus-author checks. Do **not** change source, overwrite historical Review 01 for PR #23, or merge PR #25. Standing owner authorization allows a reviewed PASS to merge later without additional routine approval, followed by post-merge verification.
