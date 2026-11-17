# SIM_HEAT PR51 — independent R2: active-main audit corrections

**Source PR:** [physicsvigilante/sim_heat #51](https://github.com/physicsvigilante/sim_heat/pull/51), DRAFT, target `main`. **No source merge or new native execution is authorized by this packet.**

| Identity | Exact value |
|---|---|
| Candidate head | `52d693a748ad3709c99215bac0a5840a236937a6` |
| Candidate tree | `7dcbb52c40f5b431ccdfe5dd4d2329fa21463829` |
| Base main | `c06fb5395781482bd6bbe055d10bc10cdf3bba8d` |
| Base tree | `053da2caa4ab86b84eb9a03a77c1f9c173a4486b` |
| Branch | `audit/2026-11-17-core-corrections` |
| Risk | **R2** — shared input parsing, source-graph identity and archived diagnostic evidence semantics |
| Independent output | NEW `projects/sim_heat/pr-51/reviews/review-01-chat-b.md` |

Chat B must independently author the report in a separate context; Chat A must not write its verdict. Use **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, with exact source and distinctions between personally executed probes and inspected hosted evidence. Read central [PROTOCOL](../../../PROTOCOL.md), [risk policy](../../../REVIEW-RISK-POLICY.md), [template](../../../REVIEW-TEMPLATE.md) and the pinned source `AGENTS.md`, H1 implementation contract, offline amendment and historical C1 freeze.

## Why this candidate exists

The user requested a project-wide audit, actual corrections and a capability/forward-plan summary. This is the **active-main correction set**, recovered from that audit and retested, not another C1 mock-lock or denial demonstration. The separate historical schematic correction [PR50](https://github.com/physicsvigilante/sim_heat/pull/50) has independently passed its targeted visual review; **none of that historical branch chain is merged into this candidate**.

Active main already has six archived native **diagnostic-only** examples and a working generic explorer. C1's uncomputed native transfer and declared missing prerequisites are a distinct experiment, not evidence that the entire project lacks native results. This correction must retain that distinction and must not promote diagnostic results into independently qualified physics.

## Exact source scope: 11 paths, 7 modified / 4 added

Modified: `h1/study.py`, `h1/tests/test_resolution_campaign.py`, `viewer/network/tools/build_case.py`, `viewer/network/tools/build_steady_case.py`, `viewer/network/tools/build_campaign_case.py`, root `README.md`, and `viewer/network/README.md`.

Added: `.github/workflows/project-audit-core.yml`, `viewer/network/tests/test_project_audit.py`, `viewer/network/tools/replay_published_archives.py`, and `docs/PROJECT_AUDIT_2026_11_17.md`.

**Preserved:** physical component equations, original authored Modelica/studies, reference specifications and saved bundles, verification error thresholds, native runner, tracked historical plans, published case JSON/catalog/comparison data, and prior failed records. The shared parser **does** change prospectively; do not claim its hash still equals an old frozen execution pin. Historical source-pinned plans correctly refuse the successor. Only disposable test fixtures are explicitly repinned to exercise existing analysis-companion logic. No historical plan, C1 reference or actual execution budget is updated.

The developer audit document is a dated implementation/self-check record, **not** an independent review. Its earlier local-browser limitation and separate schematic status should be read alongside the current evidence below.

## Changes to scrutinize

### 1. Shared JSON refusal and representation

`h1.study.strict_json` adds a finite `parse_float` hook for legal JSON exponent overflow (`1e999`, negative/uppercase/nested variants), bounds integer-token length and converts malformed/too-large/deep input failures into typed `Refusal('descriptor', ...)`. Duplicate keys and nonstandard NaN/Infinity still refuse. Finite numbers, literal booleans and null retain their original representations.

Adversarially test nested overflow, large integers, recursion, duplicate keys, finite controls, unchanged admitted original studies and whether malformed input can escape as an uncontrolled error. Check that no numeric tolerance or physical-law meaning has changed.

### 2. Generic generated-junction identity

`owner_graph` reserves **all authored component names before generating junction IDs**, including owners encountered later and rod names. A valid authored component called `junction_2` must not collide with an ownerless ideal junction, produce duplicate node IDs or create a false self-loop. Deterministic suffixes avoid collisions; the change is generic, not apparatus-ID dispatch.

Independently author a valid unseen collision case; test suffix collisions and future component-name reservations. Confirm all six existing published graphs retain exact IDs, endpoints and bundle bytes.

### 3. Report/counter type integrity across adapters

The steady and campaign adapters compare entire saved candidate receipts and recomputed verification reports by deterministic serialized JSON, rather than Python dictionary equality (`0 == False`, `1 == True`, integer/float ambiguity). Command counters and changed check-count checks require actual integers.

Mutate saved report flags to numeric zero/one, command counts to booleans/floats, public values or checks beneath a success status; recompute synthetic member/outer hashes and confirm the intended consistency guards refuse. Exact serialization is source/report binding, **not a signature or external owner attestation**.

### 4. Transient original-archive consistency

`build_case.py` now checks the complete selected-attempt manifest/member coverage and hashes, bounded ZIP inspection, original source library/model/study bytes, preflight return records, saved reference file hash/seal/canonical fingerprint, complete recomputed checking report and original candidate receipt, and MAT/CSV provenance/grid fields. It uses the existing checker and saved reference, **not `reference.prepare`** in archive replay. The recorded MAT bytes are hashed; normalized CSV is decoded; no stored binary is executed.

The transient adapter's API/CLI now requires separately checked `expected_run_id` and `expected_commit_sha`, like the existing steady/campaign adapters. Check call sites/documentation, external run mismatch and missing identity inputs. A caller who invents a new ZIP and supplies matching invented identities has not authenticated a native run: independently trusted original ZIP/run/commit custody remains an external prerequisite.

Synthetic positive controls deliberately contain a fake MAT marker and analytical test-only CSV. Their internal-consistency acceptance is **not** native provenance and must never publish fake results. Synthetic repacked attacks expose checking weaknesses, **not corruption of the original authenticated archives**. Ordinary D1/S1 analytical preparation in isolated tests is allowed checking-fixture work; no frozen/adopted C1 PR31 reference is regenerated.

### 5. Capability documentation and read-only replay

The current root README now describes the implemented thermal library, restricted authoring contract, actual generic explorer, six archived diagnostic cases and saved conductivity comparison. It separates these from the unmerged C1 expected-only tools and unqualified native-transfer claim. It does not claim symbolic/inverse solving, unrestricted thermodynamics, browser-launched simulation or proven classroom effectiveness.

`replay_published_archives.py` is a reproduction inventory of six existing artifacts, not arrangement-specific engine logic. Each original full-ZIP SHA and case identity must match the unchanged published data, and regenerated viewer bundle bytes must be exactly equal. No public data is rewritten.

## Exact-head hosted evidence

[Push run **44148890246**](https://github.com/physicsvigilante/sim_heat/actions/runs/44148890246), job **134271418151**, completed **SUCCESS** at exact head `52d693a748ad3709c99215bac0a5840a236937a6`.

[Original artifact **14358266358**](https://github.com/physicsvigilante/sim_heat/actions/runs/44148890246/artifacts/14358266358): **5,873,728 bytes**, whole ZIP SHA-256 **`c0acc90ef3153625e4f480201d12a6ab43d79bfff433d2cd546fe1d22d746282`**, **33 unique CRC-valid members**. Chat A downloaded and independently hashed/tested the ZIP, checked `head-sha.txt`, `head-tree.txt`, the 11-path diff, test logs and archive replay, and personally opened the hosted comparison and refusal screenshots. This is developer verification, not an independent reviewer result.

| Hosted evidence | Observed result |
|---|---|
| `h1.log` | 152 Python tests passed |
| `arithmetic.log` | 4 tests passed |
| `adapters.log` | 54 collected: **53 passed, 1 optional skipped** |
| `node.log` | 31 JavaScript tests passed |
| Total unit outcomes | **240 passed, 1 skipped, zero failures**; do not report 241/241 passed |
| `archive-replay.json` | Six original published bundles **BYTE_IDENTICAL** |
| `compare-replayed.json` | Byte-identical to the tracked comparison index |
| `browser.log` and 21 PNG screenshots | Existing full explorer Chromium smoke completed successfully |
| Native operations during candidate verification | **0** |

Hosted browser checks exercise six-case switching, saved timestamps, steady versus transient controls, keyboard/playback, flow-reversal selection, original CSV acceptance/refusal, async import/race guards, saved comparison and desktop/mobile layouts. Inspect the actual existing `viewer/network/tests/browser_smoke.py`, not just the one-line success message. It navigates an ordinary local HTTP server; no independent cross-browser, assistive-tech or classroom certification is implied. CI provisioning downloads Python/browser dependencies and original archives; **offline** means no fresh physical/native simulation, not air-gapped installation.

The earlier developer-local localhost smoke was blocked with `ERR_BLOCKED_BY_ADMINISTRATOR`; it is **not a pass or a demonstrated project defect**. Hosted CI subsequently ran that normal browser path successfully. Do not conflate developer screenshot inspection with personal execution of hosted browser code.

The optional skipped method is `test_optional_original_native_archive_and_fully_rehashed_test_only_mutants`; `SIMHEAT_ORIGINAL_CAMPAIGN_ZIP` was not set in the hosted unit-test step. CI separately downloads/replays the original campaign archive later. Chat A additionally reran that single optional method locally with the authentic campaign ZIP supplied: it passed, including seven separately repacked synthetic negative variants, leaving the original ZIP unchanged. That supplemental local result does not retroactively turn the hosted skip into a pass. Reviewer can reproduce it using the named environment variable and original artifact.

## Original six-bundle replay identities

| Case | Original artifact ID | Required original whole-ZIP SHA-256 | Unchanged published bundle SHA-256 |
|---|---:|---|---|
| D1 | 14152886226 | `8fc38b9e2f040b48ab5cbeab34e8698b7c99c4d462a1e31e8bc33b0395185379` | `49c605d5a23da7d521da6c8db186dbd2d435facb60c31289822322e20a6dfebf` |
| D2 | 14152886226 | same original ZIP as D1 | `c0fc143db30278898d13340faa7f60baf62185b40296767a6114e359d3c705ea` |
| DEV_BRIDGE | 14155084346 | `f16975a25eea79f61f7819fb9e704ab04a33630044a51a0d062b8399c1c9ce38` | `07dbe0987b99c89d9a20f0a1317b3699cddbf85186dcee3ae71d6d0005c364d8` |
| S1 | 14204656273 | `82b4a87b66e0022d582da931253649b3829f6633119a57081c02dc253dc5dbd9` | `eacab37b499a47c094cbd642acfee269a1bea7c82d16b15b9217a8c13ef1e4e7` |
| TEACH_RING4 | 14215520616 | `0bc1433be66df2827f8907d100ca264f6a721fe8ad40644b962500b97fa9b8b2` | `b4f46b2953409980ea5d5ed1b41cafaf5a7504003da44038d9d51286bb6e8a34` |
| D2_K2 | 14153251022 | `dc32a0a36a27f031ce7a13da83ebdd26a3dd6ac1d14612fa597b36cb439f4843` | `a057e076aa31971c82509b70566892f9be60850046231104feac5d9e6365748b` |

Replay must inspect the original run/commit/artifact identities stored in tracked source and independently retrieve original GitHub artifacts where feasible. All results remain `diagnostic_only`, `nativeQualified=false`. Byte-identical selection from previously recorded data is not a fresh physical simulation or new independent numerical qualification.

## Acceptance and preservation boundaries

Independently verify the five correction areas, full 11-path diff, changed parser versus immutable old plan pins, complete saved-report replay, six unmodified published bundle hashes and evidence labels. Perform new adversarial probes where tools allow and distinguish direct source execution, independent re-expression and inspected hosted results. Identify any API regressions, incomplete malformed-input handling or broader evidence claims rather than assuming all errors were found by this audit.

Do not alter old scientific records, auto-repin historical execution plans, merge the C1 branch chain, regenerate/reseal adopted C1 references, execute native model binaries, run/install/query OpenModelica, loosen numerical thresholds or approve a source merge. The C1 F0 and PR32 failures remain their own historical failures; the active-main archive capabilities remain genuine diagnostic data, not C1 qualification.

**Required deliverable:** one new independently authored report at `projects/sim_heat/pr-51/reviews/review-01-chat-b.md`, pinned to this exact head/tree, verdict SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE. A positive review can support these prospective main corrections, but only separate owner approval can authorize integration and post-merge verification.
