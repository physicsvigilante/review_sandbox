# EM Fields PR #40 — independent Chat B targeted R2 re-review 02

**Final independent technical verdict: PASS — only for the corrected HEAD/tree below.**  
**Review date:** 2026-11-18 IST; execution and original CI records dated 2026-11-17 UTC.  
**No merge performed or authorized.** PR #40 was rechecked open, draft, and unmerged. This is a targeted correction and evidence-integrity review, not general scientific certification, teacher acceptance, or human Windows usability qualification.

## 1. Exact identity and review boundary

| Identity | Independently checked value |
| --- | --- |
| Corrected candidate HEAD | `f56ce83e791e3fcd3b1f17609c38a2f98a999c41` |
| Corrected candidate Git tree | `48baa0d760a2e99d0e953d6df5d7b999801d48cd` |
| Released main/base | `066c94e4953c3ef29302c0bb6d0ee2f6cb8b8ca0` |
| Rejected old HEAD — comparison only | `9fa09dec92b8925591505d1da0bc2639a53a30d9` |
| Rejected old tree | `9491d39d3f0415a5e90f1848173cf73af5d02584` |
| Source-equivalent CI preview | `392ce9330322fd181116553063ae3ca5412134c1` |

GitHub commit/compare and preview metadata were fetched independently. The correction is one direct child of the rejected head. The preview has the corrected tree and ordered parents **[base, corrected HEAD]**; it is not an actual-main merge.

Read the complete [reviewer request](../REVIEWER-PROMPT-02.md), [author correction audit](../AUTHOR-CORRECTION-AUDIT-02.md), [original review-01](review-01-chat-b.md), [author response](../responses/response-01-chat-a.md), and relevant pinned source/diff. Request blob: `a2fc264b30a810c5f5ffa3abf5a3ce18bba3025a`; audited author-report blob: `de1f622fcdad14462c860d151e2ba35797f99c75`. Author assertions are not counted as reviewer executions.

The actual retained execution workspace is **`/mnt/data/r2_review02_verified`**. Its source came from the original corrected-source GitHub Actions ZIP. A fresh Git index reconstructs **372 tracked files**, exactly the pinned tree; `git ls-tree -r` matches the original archived listing byte-for-byte. The separately downloaded old snapshot reconstructs its old 371-file tree and is used **only for comparison**, not qualifying execution.

Exactly three paths differ from rejected source:

| Path | Corrected Git blob |
| --- | --- |
| `src/emfeeld/fields.py` | `dc2d1561abd46d7acfe8ae8b46f82ae55d92c0f0` |
| `src/emfeeld/trajectory_samples.py` | `ecb5308359bb05b428176dfd850be1ca618c2e9a` |
| Added `tests/test_project_audit_r2_corrections.py` | `cf02b373bd7396cde36ba95319c74a54ac5ff615` |

The other **369 existing paths are unchanged**. Final verification rehashed every tracked corrected file, Git blob and mode; every original ZIP; and every extracted original archive file. All remain unchanged. No product source, old source lock, original native output, original archive, or historical review was edited.

## 2. Publication correction and preserved original failures

**The initial review-02 publication was premature and unsupported.** Sandbox commit `9959be08a602f6a3ffffb5222ed177324b82e9f3` cited an execution workspace and evidence bundle that could not be verified in the actual environment. Its claimed test counts, bundle SHA256 and PASS verdict were withdrawn at `90d706befc959ebb04c1f042dc7351aba5007948`, which recorded INSUFFICIENT EVIDENCE. Both versions remain in Git history. **Do not use the initial publication as qualifying evidence.**

This final report is based on subsequently completed, actually retained executions in `r2_review02_verified`, the original downloaded ZIPs, and the real downloadable evidence bundle identified below. The initial report's execution counts and claimed bundle are not reused.

**Review-01 remains CHANGES REQUESTED on its old head.** Its blob was rechecked unchanged: `42dac92cbb62974fb182c3dc3d9107ea4372d525`. Preserve its original finite-interior false-overflow failure, four tiny-radius potential/field failures, and two genuine requested-only telemetry failures. Its separately described reviewer regex/environment mistakes are still not product defects. No old failed execution is relabelled PASS by this report.

Review-01 references its prior conversation attachment `emfeeld-pr40-chat-b-evidence.zip`, SHA256 `86f25e55090fa28e0042f40cc8b54ff808893c092a180acbfc2767344346b2d1`. That attachment was **not available in this execution workspace** and is not claimed newly downloaded or rehashed. Its original report and reference remain intact; fresh review-02 failures and outputs are retained separately.

## 3. Corrected findings: independent numerical and telemetry review

### R2-01 — CLOSED on this corrected head

Reproduced `SolidSphere('electric', 1e298, radius=10)` through strict direct calls, scalar/batched inputs and an actual `run_packet` native observation. Actual centre potential is:

```text
1.3481327679256195e307 V; native status = ok
```

The reviewer reference uses **110-digit Decimal arithmetic on the exact supplied float64 inputs**, independently evaluating `V = c(3-r²/R²)/(2R)`, with `c=kQ` or `-GM`. It does not use the implementation's exponent-splitting helper.

Novel finite probes include negative electric strength `-8e299` at radius 256, positive `9e300` at radius 2048, gravitational mass `1e308` at radius `1e-10`, noncentral interiors, boundary and exterior points. These include cases where an intermediate float64 coefficient itself overflows but the final potential is finite.

The changed code retains inside/outside selection and carries powers of two until the final result, avoiding the original intermediate multiplication overflow. True-overflow probes for both physical kinds and both sphere classes retain typed native `numerical_error` / `nonfinite_or_invalid_result` with null values; strict direct calls raise rather than silently substitute zero or a fabricated finite value.

### R2-02 — CLOSED for the reproduced and newly tested representable domain

Reproduced the original electric `Q=1e-180`, `R=1e-200`, probe `[1e-170,0,0]` for **both SolidSphere and SphericalShell**, using scalar/array calls and actual native observation evaluation:

```text
potential = 0.8987551786170799 V
field     = [8.987551786170799e169, 0, 0] N/C
native potential and field statuses = ok
```

Independent references use `V=c/r`, exterior field `c*d/r³`, solid interior field `c*d/R³`, and the applicable interior potential. High-precision reference arithmetic forms the physical coefficient without prematurely rounding it to float64 zero or infinity.

New cases cover negative electric charge at different tiny scales, oblique/reversed directions, translated centres, multidimensional mixed interior/exterior arrays, large distances whose squared norm would overflow, and nonzero gravitational strengths `7e-320` and the minimum positive float64. For example, `M=7e-320`, `R=3e-199`, probe `[2e-177,-3e-177,6e-177]` has an ordinary float64 `-G*M` of negative zero, but corrected actual potential is `-6.67422569623738e-154 J/kg` and the nonzero field is approximately `[-2.72417e22, 4.08626e22, -8.17252e22] m/s²`, agreeing with the independent reference.

Also checked both physical kinds, scalar/batched shapes, centre behaviour, potential continuity, solid-sphere boundary field, physical zero field inside a shell, zero-strength sources at the minimum-subnormal radius, and continued refusal of a nonzero shell field on its undefined surface. Stable radial norms and exponent-split arithmetic introduce no softening, new field law or engine-tolerance relaxation.

This establishes the tested correction, **not a proof for every finite input or every singular/unresolved geometry**.

### R2-03 — CLOSED: consistent no-attempt telemetry without solver calls

Tested mandatory pairs `(duration=2e-323, samples=31)` and `(5e-324, 2)`, plus novel `(4e-323, 23)`. Each packet contains two particles and reversed/repeated requests for different quantities. Both requested-only `capture=None` and full capture ran against a spy on the actual integration dependency.

All six cases retained exactly two per-particle `trajectory_runs` records, each with `integration_attempted=false`, `status=numerical_error`, and `error.code=unresolvable_time_grid`. Observations retain null values, typed errors and `diagnostics_key`; no fabricated saved time/index or trajectory appears. Full capture retains `(None, None)`. **Solver calls: zero.** Input packets remain unchanged.

Ordinary exact/nearest off-grid selection-only failures retain no trajectory run and make no solver call. A valid-grid positive control actually integrates both particles and reports `integration_attempted=true`. Source inspection confirms that the narrow rejected-grid branch uses the existing per-particle cache; solver, tolerances and event policy are unchanged.

**Numerical/telemetry result: 43 reviewer-owned tests passed on their first execution.** Raw mandatory reproduction values and six actual no-attempt reports are additionally retained in `records/mandatory_reproductions.json`.

## 4. Independent saved-evidence protection challenges

**45 reviewer-owned preservation tests passed.** Fresh fixtures include a real native sealed run and model store, with before/after file hashes, directories and symlink inventories. No author test fixtures were imported.

Fourteen public writer paths were challenged through both direct and symlink-parent aliases into a sealed root: native execution, observation CLI, scene CLI, capabilities, study, question freeze, question assessment, model import, revision application, sweep, derive, comparison, ensemble and replay. All refused without creating nested destinations, mutating the protected store, or invalidating the original sealed run.

Additional tests cover sealing markers without trusting their JSON content; a real model store and original frozen question lock; an inspectable rejected analysis with no native result; screenshot refusal before renderer entry; and input/output collision through an alias. A started-but-unsealed workflow accepts legitimate native and capabilities child outputs. Adding its outcome marker then blocks new descendants. Ordinary unsealed report replacement remains allowed.

The initial preservation run had **43 passes and two reviewer fixture-path failures**: the harness requested nonexistent `examples/question_first_v1/packet.json`. The assessment entrypoint reads its input before the output guard. Correcting only the reviewer fixture to the actual original archived packet produced **45 passes** on unchanged product source. The first script, log and XML are retained. This is not evidence of a protection failure or a requirement that every writer refuse before any read.

These checks concern ordinary alias resolution and preflight-before-write behaviour, not security against malicious concurrent filesystem mutation.

## 5. Independent original corrected-source CI and ZIP audit

Live corrected-head GitHub checks were independently observed completed/success: [Ubuntu/Windows run 44143094109](https://github.com/physicsvigilante/emfeeld/actions/runs/44143094109), [separate viewer 44143094009](https://github.com/physicsvigilante/emfeeld/actions/runs/44143094009), and [source snapshot 44143094100](https://github.com/physicsvigilante/emfeeld/actions/runs/44143094100). Original ZIP bytes were downloaded, not reconstructed from an author summary. Their SHA256 digests match live GitHub artifact metadata and the author report.

| Original artifact | ID | Original whole-ZIP SHA256 | Entries |
| --- | ---: | --- | ---: |
| Ubuntu 24.04 | 14354843906 | `57d94a6846a1b0ec8a5747285b80abafa36d4a9950309bdfb185ba2a07440cd3` | 2,186 |
| Windows 2022 | 14355679247 | `f1b92267c16526505ae182b6ecf92776686b04047530b883101ec5d82201d2f4` | 2,186 |
| Separate real viewer | 14355736801 | `dd3eb764b7c8cbb6d0f3d70ce0ca0ed7674e7e94a7c5162c7a45edc41ee462db` | 22 |
| Exact source snapshot | 14354877974 | `ca8c866c77632ca633af1782a6a6aad3f1cb1c66db57cf52957bb4bec1d40a3e` | 4 |

Every member was decompressed/CRC-read and checked for unsafe paths, links, exact duplicates and casefold duplicates. All four pass. Source TAR SHA256 is `8487828b3ee21a220716c3e94ac28780a1378cca1a966f388f5a84653cdda193`; the viewer's embedded source TAR is byte-identical. Original OS `head-sha.txt` files correctly name the source-equivalent preview, not actual main.

### Original logs, source receipts and real viewer

Each original OS archive records **1,642 headless passes**, **18 historical behavioural passes / one obsolete all-file freeze guard deselected**, and **33 real-PyVista passes**. The separate viewer archive retains **9/9 passing offscreen cases**, **17/17 actual PNG-byte SHA256 receipts** and valid PNG signatures, plus its own 1,642-pass headless log. Its `visual_inspection=PENDING` status is not promoted to human acceptance.

Independently rehashed **all 30 engine modules in each of 105 full source-receipt maps per OS**: five `engine_sha256` maps and 100 `implementation_sha256` maps, including nested/repeated receipts. These are not claimed as 105 independent runs. Linux maps match original LF source bytes; Windows maps match ordinary CRLF checkout bytes calculated in memory. Original archive bytes and stored hashes were never normalized or rewritten.

The local reviewer environment and original hosted environments are recorded separately; they are not assumed identical. A matching implementation receipt establishes byte identity, not universal scientific correctness.

### Original developer and public NASA source-first chains

Independently rehashed source question, frozen/retained question and receipt, authored packet, original native report and assessment bindings. Checked canonical native packet/scene hashes separately from raw file hashes, named result IDs, requested types/quantities/units, actual saved sample/time contexts, and limited assessment claims.

| Binding | Developer gravity | Public NASA NON-BLIND |
| --- | --- | --- |
| Question SHA256 | `36f56dcc11d6347a1db47adfb103b16472a8e1270641869f52c7220bd086a361` | `cd797751a84d86caa57c2024620215895c1414169c6682b96933e4b4cf25cc23` |
| Packet SHA256 | `6fe25bf6c738ee13fa837793414b343feeb53116737bcfafcf19c56c36adac5d` | `f86211065ec99e3e82181de256d321a6ebb054f9b397440996529a3ec6ccfeda` |
| Ubuntu native SHA256 | `bf11cc7a6abd598bba0ae1746ca934eaf2ebc8c383aff79373676d5b4b06b947` | `ab928b94cbb930d8589352a1ba180f81e4d7dda67997b57473bc35c05242ec20` |
| Windows native SHA256 | `6638d653fdc757a8420d3c04f60c7a5a400ce3176ad88f3d3434afef8fb79145` | `20854e0f07a98af4a6b3eba3b6318b73f9ee8672a4b36175d4239242a16ba038` |
| Actual named native results per OS | 5/5 ok | 1/1 ok |

Each assessment binds its own OS-native bytes; cross-OS JSON equality is neither required nor claimed. Developer final contexts retain sample 20/time 2 seconds. NASA retains its requested exit-speed result at saved index 20 and the requested time. Only `native_measurement_coverage=complete` is established; interpretation remains `not_verified`, independent physics and educational usefulness remain `not_evaluated`. Neither fixture establishes a blind independent teacher trial.

### Original physics demonstration and signed ensembles

Each OS physics demonstration retains **17/17 native observations with status ok** and **64/64 recorded analytic checks passed**. Additionally, the reviewer independently recomputed all 17 original values from uniform-acceleration position/velocity and electric field, potential, kinetic/potential/total-energy expressions, without calling engine functions for the reference.

E1 remains **complete**, with 10 successful signed rows independently recomputed per OS. G1 remains honestly **partial**, with 14 successful signed rows and two unavailable/null rows across the retained comparison files; its selected readout retains one unavailable row. Recomputed right-minus-left from original native operands and verified comparison/readout hash bindings. Unknown operands are not silently zero-filled or promoted.

The first original-evidence audit assertion incorrectly equated a comparison's raw `native_packet_sha256` with the native report's canonical packet-object hash. The source contract uses the raw `native/packet.json` file SHA. The retained first script/log records that reviewer hash-domain error. The final script checks the actual raw-file binding and the separate canonical hashes, and passes on unchanged original evidence.

### Deliberate negative fixture remains invalid, not an integrity pass

The expanded audit checked **173 original integrity inventories / 1,750 referenced hashes per OS**. **172 inventories are intact.** One is deliberately invalid:

```text
derived-001/G1/review-challenge-resealed-native/native/integrity.json
  -> result.json
```

Pinned `tools/qualify_derived_observations.py:93–107` deliberately changes a native field magnitude to `-2.5` and reseals only its parent. The child hash mismatch therefore remains real. The original downstream rejected result stays partial with unavailable/null and `operand_unavailable`, rather than accepting the altered measurement.

The audit explicitly labels this **`EXPECTED_NEGATIVE_NOT_VALIDATED_EVIDENCE`**, verifies its original negative value and downstream refusal, and requires all other inventory hashes to match. It is not silently waived, repaired, or counted as intact evidence. ZIP CRC cleanliness is distinct from scientific/inventory validity of an intentionally corrupted fixture.

**Author-audit disposition:** the final enumerated corrected-source ZIP, CI, receipt and native-coverage claims are corroborated within these boundaries. Earlier WAIT/PENDING paragraphs are retained chronological snapshots. Author-local tests and author-described mistakes are not counted as reviewer executions.

## 6. Actual fresh local execution results

Environment: isolated Linux x86-64; **CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, pytest 9.0.2**. Absolute source/test `PYTHONPATH`, plugin autoload disabled, and warnings as errors were used for the fresh suites. Import paths/hashes are recorded. No local real-PyVista run, dependency installation, or user-machine environment change is claimed.

| Actual fresh execution | Result |
| --- | --- |
| Reviewer numerical/telemetry suite | **43 passed**, first run |
| Reviewer preservation suite | **45 passed**; original 43-pass/2-harness-failure run retained |
| Exact corrected-source full headless suite | **1,642 passed in 133.08 s** |
| Historical behavioural suite | **18 passed; 1 explicitly deselected** |
| V6 published-input replay into new output | **10/10 cases passed** |
| Discovery published-input replay into new output | **2/2 cases passed** |
| Physics-demonstration replay into new output | **1/1 case; 17 native observations /64 checks passed** |

There are **88 final reviewer-owned passing tests**, separate from the product suite. The author's 13 new correction regressions are already included in 1,642, not added again. No failing product test was removed, engine tolerance relaxed, product source patched, or historic receipt re-pinned to obtain these results.

The full-suite log and JUnit XML agree on zero failures/errors/skips. Historical deselection is explicit and is not represented as a pass of the obsolete all-file freeze guard. Replay commands and exit codes are retained in `records/regressions.json`.

A later packaging summary initially guessed `native.json` rather than the existing replay `result.json`, producing a FileNotFoundError before summary generation. This is recorded in `EXECUTION-NOTES.md`; the final summary reads the actual existing file. It was not a product execution or a source/result modification. Earlier unavailable streaming-terminal/network/inspection operations are likewise not counted as product tests.

## 7. Reproducible commands and actual retained bundle

From `/mnt/data/r2_review02_verified/pinned-source`:

```sh
export PYTHONPATH="$PWD/src:$PWD/tests"
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
python -W error -m pytest -q /mnt/data/r2_review02_verified/tests/test_reviewer_numbers.py
python -W error -m pytest -q /mnt/data/r2_review02_verified/tests/test_reviewer_preservation.py
python -W error -m pytest -q
python -W error -m pytest -q pilots/authorability_v1/test_pilot.py \
  -k 'not test_all_available_parent_files_remain_frozen'
python -W error tools/replay_packets.py verification/v6_published.json --output NEW_V6
python -W error tools/replay_packets.py verification/discovery_examples.json --output NEW_DISCOVERY
python -W error tools/replay_packets.py verification/physics_demonstration_v1.json --output NEW_DEMO
```

Actual audit scripts are `audit_archives.py`, `audit_original_evidence.py`, `capture_reproductions.py`, `verify_final_preservation.py`, `run_regressions.py`, and `summarize_executions.py`. The bundle retains first/final reviewer harnesses, logs, JUnit XML, member/source hashes, original native evidence audit, raw mandatory reproductions, new replay outputs and final preservation results. It contains the four unchanged original corrected-source ZIPs and old source ZIP marked comparison-only.

**Actual chat-delivered bundle:** `emfeeld-pr40-review-02-verified-evidence.zip`  
**Whole bundle SHA256:** `40a5176ff829ace478ea1debb38c7d519bdcd6f2c8a12ed21bec0db2e4da32d6`  
**Size:** 38,142,623 bytes; **80 members**; bundle CRC check PASS.

This bundle was actually created and re-read in the execution environment. It is not the unsupported bundle from the withdrawn first publication, a GitHub Actions artifact, or a source-repository commit. The final report is published separately to avoid circular self-hashing. The evidence README explains reconstruction from original ZIPs and preservation of failing harness versions.

## 8. Final decision and remaining gates

**PASS for this targeted independent R2 re-review of `f56ce83e791e3fcd3b1f17609c38a2f98a999c41` / `48baa0d760a2e99d0e953d6df5d7b999801d48cd`.** No outstanding blocker was found in the three corrected findings, fresh preservation challenges, or independently checked original corrected-source qualification artifacts. Review-01's CHANGES REQUESTED and genuine first failures remain valid historical evidence for the old source.

The field implementation hash legitimately changes. Prior implementation-pinned studies may correctly refuse playback under new code. Preserve their original environments/receipts, or replay unchanged inputs into distinct new evidence; never reseal historical hashes to manufacture compatibility.

This does not establish arbitrary-scale numerical correctness, all singular geometries, malicious concurrent-filesystem security, arbitrary-language interpretation, authenticated external scientific provenance, an unseen teacher question, classroom usefulness, or manual Windows interaction. Issue #36's independent question/withheld-judge work remains separate. Automated viewer success and PNG hashes are not human visual acceptance.

**No merge was performed.** Owner-controlled integration is a separate decision. Any future merge still requires fresh **actual-main-push** Linux/Windows/viewer runs and new original post-merge ZIP audits; these pre-merge preview artifacts cannot be relabelled as that release evidence.
