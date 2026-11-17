# EM Fields PR #40 — independent Chat B targeted R2 re-review 02

**Date:** 2026-11-17 UTC  
**Independent technical verdict: PASS — for the exact corrected source identified below.**  
**No merge performed or authorized.** This is a targeted correction/evidence-integrity review, not general scientific certification, teacher acceptance, or a human Windows usability review.

## 1. Immutable identity, scope, and preservation of review-01

| Identity | Independently checked value |
| --- | --- |
| Corrected candidate HEAD | `f56ce83e791e3fcd3b1f17609c38a2f98a999c41` |
| Corrected candidate Git tree | `48baa0d760a2e99d0e953d6df5d7b999801d48cd` |
| Existing released main/base | `066c94e4953c3ef29302c0bb6d0ee2f6cb8b8ca0` |
| Rejected old HEAD, comparison only | `9fa09dec92b8925591505d1da0bc2639a53a30d9` |
| Rejected old tree | `9491d39d3f0415a5e90f1848173cf73af5d02584` |
| Source-equivalent CI preview | `392ce9330322fd181116553063ae3ca5412134c1` |

GitHub's commit/compare and preview metadata were fetched independently. The corrected commit is one direct child of the rejected head. The preview has the corrected tree and ordered parents **[base, corrected HEAD]**; it is not a post-merge main commit. PR #40 was open, draft, and unmerged at review.

Read the complete [R2 request](../REVIEWER-PROMPT-02.md), [author correction audit](../AUTHOR-CORRECTION-AUDIT-02.md), [original independent review-01](review-01-chat-b.md), [author response](../responses/response-01-chat-a.md), and the relevant pinned source/diff. Request blob: `a2fc264b30a810c5f5ffa3abf5a3ce18bba3025a`; audited author-report blob: `de1f622fcdad14462c860d151e2ba35797f99c75`.

**Review-01 remains CHANGES REQUESTED on its old head.** Its original report blob was rechecked unchanged as `42dac92cbb62974fb182c3dc3d9107ea4372d525`. In particular, preserve its original R2-01 false-overflow failure; four R2-02 tiny-radius failures; and two genuine R2-03 requested-only telemetry failures. Its original reviewer regex/configuration mistakes remain distinguished from source defects. This report does not change those outcomes or relabel old executions as successful.

The prior conversation's reviewer evidence attachment, `emfeeld-pr40-chat-b-evidence.zip`, is referenced by review-01 with SHA256 `86f25e55090fa28e0042f40cc8b54ff808893c092a180acbfc2767344346b2d1`. It was **not available in this execution workspace and is not claimed newly downloaded or rehashed**. Its original report/reference is preserved; all review-02 executions and first failures are separately retained.

Downloaded the original corrected source ZIP, reconstructed all **372 tracked files** into a fresh Git index, obtained the exact corrected tree, and matched archived `git-tree.txt` byte-for-byte. Separately downloaded the original rejected-source snapshot for identity/diff only, reproduced its 371-file old tree, and confirmed exactly these three changes:

- `src/emfeeld/fields.py`, Git blob `dc2d1561abd46d7acfe8ae8b46f82ae55d92c0f0`.
- `src/emfeeld/trajectory_samples.py`, Git blob `ecb5308359bb05b428176dfd850be1ca618c2e9a`.
- Added `tests/test_project_audit_r2_corrections.py`, Git blob `cf02b373bd7396cde36ba95319c74a54ac5ff615`.

The other **369 existing files are byte-identical**. No old-source execution is used to qualify the correction. After all fresh tests, all 372 corrected tracked blobs/modes and all four original corrected ZIPs were rehashed unchanged. No project source, historical source lock, stored result, original review, or original archive was edited.

## 2. Findings disposition on the corrected head

### R2-01 — CLOSED on this head: finite sphere-interior potential no longer falsely overflows

Fresh direct calls and an actual `run_packet` native observation reproduce the original `SolidSphere('electric', 1e298, radius=10)` centre case. Corrected actual potential:

```text
1.3481327679256195e307 V; native status=ok
```

The reference was independently derived from `V = kQ(3-r²/R²)/(2R)`, using **110-digit Decimal arithmetic on the exact supplied float64 inputs**, not the implementation's exponent-splitting algorithm. New probes included negative charge `-7e299` with radius 128, positive `9e300` with radius 2048, noncentral interiors, and the surface. These include cases where a prematurely formed `kQ` itself overflows but the final potential is finite.

The correction in `fields.py:73–106` preserves powers of two until the final physical value is formed; bounded mantissa arithmetic avoids the original intermediate overflow. Piecewise selection is retained. Both physical kinds were exercised through additional scalar/batched interior, boundary, exterior, and continuity cases. Actually overflowing outputs still produce typed native `numerical_error` / `nonfinite_or_invalid_result` with null values; strict direct calls raise rather than silently manufacture finite values.

### R2-02 — CLOSED for the tested domain: tiny-radius exterior and underflowed coefficients

Fresh direct scalar/array calls and native observation evaluation reproduce the original `Q=1e-180`, `R=1e-200`, `position=[1e-170,0,0]` for **both** solid sphere and spherical shell:

```text
potential = 0.8987551786170799 V
field     = [8.987551786170799e169, 0, 0] N/C
native statuses = ok, ok
```

References independently use `V=c/r`, exterior field `c*d/r³`, solid interior field `c*d/R³`, and the applicable interior potential; `c=kQ` or `-GM` is formed at high precision in the reference rather than prematurely rounded to float64 zero/infinity.

New adversarial cases included negative electric charge at different tiny scales; oblique and reversed directions; translated centres; multidimensional mixed inside/outside batches; large distances whose squared norms would overflow; nonzero gravitational strengths `7e-320` and the minimum positive float64; and finite results even when ordinary float64 `-G*M` is zero. One retained oblique gravitational example gives potential `-1.796906918217756e-156` and field `[1.5948877972346944e17, -2.1265170629795926e17, 6.379551188938778e17]`, not an invented zero.

Verified potential continuity around the sphere/shell boundary, the solid-sphere boundary field, the physical zero field inside a shell, exact zero-strength behaviour at a minimum-subnormal radius, and continued refusal of a nonzero shell field on its undefined surface. The code uses stable radial norms and exponent-split physical arithmetic; it introduces no softening, changed physical law, or tolerance relaxation. This closes the reproduced failures and tested extensions, **not a proof for every finite input or singular/unresolved geometry**.

### R2-03 — CLOSED: requested-only and full capture retain no-attempt telemetry

Independently executed both mandatory pairs `(duration=2e-323, samples=31)` and `(5e-324, 2)`, plus a new invalid pair `(4e-323, 23)`. Each packet contained two particles, reversed/repeated particle requests, and multiple requested quantities. Both `capture=None` and full capture were tested against a spy on the actual integration dependency.

Every rejected grid retained exactly two per-particle `trajectory_runs` entries, each with `integration_attempted=false`, `status=numerical_error`, and `error.code=unresolvable_time_grid`. Observation values stayed null, typed failures and `diagnostics_key` were preserved, no saved time/index or fabricated trajectory was reported, and full capture retained `(None, None)`. **Solver calls: zero.** Input packets remained unchanged.

Ordinary exact/nearest off-grid selection-only failures still recorded no trajectory run and invoked no solver. A valid-grid positive control really integrated and reported `integration_attempted=true`. Source inspection confirms the narrow requested-only branch now uses the existing per-particle failure cache (`trajectory_samples.py:170–176`); no solver or event policy changed.

## 3. Fresh independent evidence-preservation challenge

**46 final reviewer-owned tests passed**, separate from the author's tests and from the numerical suite. Fresh fixtures included a real native sealed run and model store; protection was checked by complete before/after file-hash, directory, and symlink inventories.

Fourteen writer paths were challenged with both direct and symlink-parent aliases into a sealed root: native execution, observation CLI, scene CLI, capabilities output, study, question freeze, assessment, model import, model revision application, sweep, derive, compare, ensemble, and replay. All refused without creating nested output/proposal destinations, changing protected bytes, or invalidating the original sealed inventory.

Additional tests covered marker-based sealing without trusting JSON marker content; actual model-store and original frozen question-lock protection; an inspectable rejected analysis with no fabricated native result; renderer non-entry on a protected screenshot destination; and input/output collision through an alias. Legitimate native/capability children of a started-but-unsealed workflow succeeded. Adding its outcome marker then blocked new descendant writes. Ordinary unsealed report replacement remained allowed.

These checks preserve the intended **preflight-before-write** contract; they do not assert that every entrypoint must reject before any read. Nor do they certify protection against malicious concurrent filesystem changes.

## 4. Independent audit of the four ORIGINAL corrected-source CI ZIPs

Live GitHub checks were independently observed completed/success for the corrected head: Ubuntu and Windows in run **44143094109**, separate viewer **44143094009**, source snapshot **44143094100**. Original downloaded ZIP hashes were compared with live artifact metadata, not merely copied from the author report.

| Original artifact | ID | SHA256 of original ZIP bytes | Entries |
| --- | ---: | --- | ---: |
| Ubuntu 24.04 | 14354843906 | `57d94a6846a1b0ec8a5747285b80abafa36d4a9950309bdfb185ba2a07440cd3` | 2,186 |
| Windows 2022 | 14355679247 | `f1b92267c16526505ae182b6ecf92776686b04047530b883101ec5d82201d2f4` | 2,186 |
| Separate real viewer | 14355736801 | `dd3eb764b7c8cbb6d0f3d70ce0ca0ed7674e7e94a7c5162c7a45edc41ee462db` | 22 |
| Exact source snapshot | 14354877974 | `ca8c866c77632ca633af1782a6a6aad3f1cb1c66db57cf52957bb4bec1d40a3e` | 4 |

**All four match.** Every member was decompressed/CRC-read and checked for unsafe paths, links, duplicate names, and casefold duplicates. Source TAR SHA256 is `8487828b3ee21a220716c3e94ac28780a1378cca1a966f388f5a84653cdda193`; the viewer's embedded source TAR is byte-identical. Original OS `head-sha.txt` files correctly name the source-equivalent preview, not main.

### Original CI logs, source receipts, viewer and physics

Each original OS archive records **1,642 headless passes**, **18 historical behavioural passes with one obsolete all-file freeze guard deselected**, and **33 real-PyVista passes**. The separate viewer archive retains **9/9 passing offscreen cases**, **17/17 actual PNG-byte SHA256 receipts**, valid PNG signatures, and its own 1,642-pass headless log. The original report's `visual_inspection=PENDING` remains unpromoted.

Independently rehashed **all 30 engine Python modules in every one of 82 source-receipt sets per OS** against the exact reconstructed source. Windows receipts match ordinary CRLF checkout bytes; no archive bytes or stored hashes were normalized or rewritten. A matching source receipt identifies implementation bytes, not by itself the scientific validity of every result.

Original Physics Demonstration results contain **17/17 native observations with status ok** and **64/64 recorded analytical checks passed** on each OS. In addition to inspecting those checks, independently recomputed all 17 native values using uniform-acceleration position/velocity and field, potential, kinetic/potential/total-energy expressions, without calling engine functions for the reference.

Original signed E1 ensemble remains **complete**, with 10 successful signed comparisons independently recomputed per OS. G1 remains honestly **partial**, with 14 successful signed comparisons, two unavailable rows in the retained comparison files, and one unavailable row in the readout. Recomputed right-minus-left from the archived native operands and verified readout bindings to original comparison hashes. Unknown-operand values remain unavailable/null, not zero-filled or promoted to complete.

### Original source-first developer and public NASA evidence

Rehashed raw source question, frozen/retained question and receipt, authored packet, original native result, assessment binding, canonical packet/scene hashes, requested result IDs, quantities/units, and actual saved contexts/times. Original source files match the corrected source archive.

| Evidence | Developer gravity | Public NASA NON-BLIND |
| --- | --- | --- |
| Raw question SHA256 | `36f56dcc11d6347a1db47adfb103b16472a8e1270641869f52c7220bd086a361` | `cd797751a84d86caa57c2024620215895c1414169c6682b96933e4b4cf25cc23` |
| Packet SHA256 | `6fe25bf6c738ee13fa837793414b343feeb53116737bcfafcf19c56c36adac5d` | `f86211065ec99e3e82181de256d321a6ebb054f9b397440996529a3ec6ccfeda` |
| Ubuntu native SHA256 | `bf11cc7a6abd598bba0ae1746ca934eaf2ebc8c383aff79373676d5b4b06b947` | `ab928b94cbb930d8589352a1ba180f81e4d7dda67997b57473bc35c05242ec20` |
| Windows native SHA256 | `6638d653fdc757a8420d3c04f60c7a5a400ce3176ad88f3d3434afef8fb79145` | `20854e0f07a98af4a6b3eba3b6318b73f9ee8672a4b36175d4239242a16ba038` |
| Actual named native results per OS | 5/5 ok | 1/1 ok |

Each assessment binds its **own OS native bytes**; cross-OS JSON equality is not required or claimed. Developer final contexts retain sample 20/time 2 s. NASA retains the requested exit-speed result at sample 20 and the original requested time. Only `native_measurement_coverage=complete` is established: interpretation remains `not_verified`, independent physics and educational usefulness remain `not_evaluated`. Public NASA is not a blind independent teacher trial.

### Important retained negative fixture — not an integrity pass

An expanded scan checked **173 original integrity inventories / 1,750 referenced file hashes per OS**. **172 inventories are intact; one is intentionally invalid**, at:

```text
derived-001/G1/review-challenge-resealed-native/native/integrity.json
  -> result.json
```

The pinned qualifier `tools/qualify_derived_observations.py:93–107` deliberately changes a native field magnitude to `-2.5` and reseals only the parent. Its child inventory therefore correctly mismatches. The original downstream `review-challenge-rejected-out/result.json` remains partial, with unavailable/null and `operand_unavailable` rather than accepting this as a valid measurement.

The first broad audit assertion that every inventory should match failed here; that original script/log is retained. The final audit explicitly verifies this exact negative fixture and its refusal, labels it `EXPECTED_NEGATIVE_NOT_VALIDATED_EVIDENCE`, and still requires every other inventory match. **It is not silently waived, repaired, or counted as intact evidence.** ZIP CRC cleanliness is not equivalent to validity of an intentionally corrupted physics fixture.

The author's final enumerated source/ZIP/CI/native coverage claims are corroborated within these boundaries. Its earlier WAIT/PENDING statements are preserved chronological snapshots, not substituted for the final corrected-source evidence. Author local tests and author-only mistake descriptions are not counted as reviewer executions.

## 5. Fresh local executions and preserved reviewer mistakes

Environment: isolated Linux x86-64, **CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, pytest 9.0.2**. No local real-PyVista execution or user-machine environment modification is claimed. Hosted original graphics evidence is distinct from this local numerical execution.

| Fresh reviewer execution | Actual final outcome |
| --- | --- |
| New external reviewer numerical/telemetry tests | **36 passed** |
| New external reviewer preservation tests | **46 passed** |
| Exact corrected source full headless suite, warnings as errors | **1,642 passed in 141.51 s** |
| Historical behavioural suite | **18 passed, 1 explicitly deselected** |
| Published V6 replay into new output | **10/10 cases passed** |
| Published discovery replay into new output | **2/2 cases passed** |
| Published physics demonstration replay into new output | **1/1 case passed; 17 native /64 checks** |

The **82 reviewer-owned tests** are separate from the product suite. The author's 13 correction regressions are already included in 1,642, not added again. None of these test counts substitutes for the original archive verification above.

All review-02 first failures were preserved, not overwritten:

- Numerical first run: **33 passed /3 failed**. Two assertions incorrectly assumed the extra pair `(1e-321,17)` was unresolvable; it has strictly increasing saved times and a positive minimum-subnormal maximum step. Replaced only that reviewer datum with `(4e-323,23)`. The third expected successful status `passed` instead of the documented `ok`. Final **36 passed** on unchanged source.
- Preservation first run: **42 passed /4 failed**, all reviewer `AttributeError` from incorrect `freeze_question`/`assess_attempt` names. Actual functions are `freeze`/`assess`. Second run: **44 passed /2 failed**, because a deliberately absent lock prevented assessment from reaching the output guard. Supplied an existing valid original lock/packet read-only. Final **46 passed**. These setup errors do not show a write-protection failure.
- Original-integrity audit first assertion: deliberate negative fixture described above. First script/log and exact mismatched hashes retained separately; final classification is explicit, not a blanket pass.
- A raw-network DNS failure and unavailable streaming-terminal allocation occurred before those requested operations could run; they are recorded as environment/tool limitations, not product test failures.

No product patch, weakened source test, original receipt rewrite, or relaxed engine tolerance was used to obtain the final results.

## 6. Reproducible commands and retained evidence

Execution root: `/mnt/data/r2_review02`; source was reconstructed under `pinned-source`. With that directory current:

```sh
export PYTHONPATH="$PWD/src:$PWD/tests"
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
python -W error -m pytest -q
python -W error -m pytest -q pilots/authorability_v1/test_pilot.py \
  -k 'not test_all_available_parent_files_remain_frozen'
python -m pytest -q /mnt/data/r2_review02/tests/test_reviewer_numerics.py
python -m pytest -q /mnt/data/r2_review02/tests/test_reviewer_preservation.py
python -W error tools/replay_packets.py verification/v6_published.json --output NEW_V6
python -W error tools/replay_packets.py verification/discovery_examples.json --output NEW_DISCOVERY
python -W error tools/replay_packets.py verification/physics_demonstration_v1.json --output NEW_DEMO
```

Reviewer audit scripts: `audit_archives.py`, `compare_old_source.py`, `audit_native_evidence.py`, `capture_reviewer_reproductions.py`, `verify_final_preservation.py`. JSON/XML records include original archive digests/tree reconstruction, old-source diff, actual original native bindings, explicitly invalid fixtures, raw reviewer reproduction values/no-attempt reports, final source preservation, and original/follow-up test results. First test/script versions and logs are retained alongside final versions.

**Chat-delivered execution bundle:** `emfeeld-pr40-review-02-evidence.zip`  
**Whole bundle SHA256:** `f17acd3159674343e3093931d7dec6ae5d7c981f7924b044953ad98be4101d1f`  
**Size:** 38,993,394 bytes; 89 members; bundle CRC check passed.

The bundle contains all four unchanged corrected-source original ZIPs, the old source ZIP marked comparison-only, reviewer scripts/logs/records, and new replay outputs. It is **not a GitHub Actions artifact or a source-repository commit**. This report is published separately to avoid a circular self-hash. The evidence README distinguishes preserved failing harness versions from current passing tests.

## 7. Decision and remaining boundaries

**PASS for the targeted independent R2 correction review of `f56ce83e791e3fcd3b1f17609c38a2f98a999c41` / `48baa0d760a2e99d0e953d6df5d7b999801d48cd`.** No outstanding blocker was found in the three corrected findings, tested evidence-preservation behaviours, or independently checked original corrected-source qualification artifacts. Review-01's old-head CHANGES REQUESTED and genuine first failures remain valid historical evidence.

The field implementation hash legitimately changes. Old implementation-pinned studies may correctly refuse playback under new code; preserve their original environments/receipts, or replay unchanged inputs into **new** evidence. Never re-pin historical hashes to manufacture compatibility.

This does not certify arbitrary-scale arithmetic, all singular geometries, malicious concurrent filesystem security, arbitrary-language interpretation, authenticated independent scientific provenance, an unseen teacher question, classroom usefulness, or manual Windows interaction. Issue #36's independent question/withheld-judge work remains separate. Original viewer image hashes/offscreen success do not establish human visual acceptance.

**No merge was performed.** Owner-controlled integration is a separate decision. Any subsequent merge still requires fresh **actual-main-push** Linux/Windows/viewer runs and new original post-merge archive audits; these pre-merge preview artifacts cannot be relabelled as that release evidence.
