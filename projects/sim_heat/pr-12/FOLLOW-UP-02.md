# SIM_HEAT PR #12 — targeted re-review 02 after F-01 correction

**Not a new broad R2 architecture review.** Follow-up to the immutable [review-01-chat-b.md](reviews/review-01-chat-b.md) outcome `changes-requested`, and [Chat A response-01](responses/response-01-chat-a.md).

| Field | Pinned value |
|---|---|
| Source PR | https://github.com/physicsvigilante/sim_heat/pull/12 — still **draft / unmerged** |
| Original reviewed HEAD | `f2bb5369425a250cef78b74baaf486925f8fa6bd` |
| Corrected HEAD | `adb1b664d1a026f2f6cf017c11eda057d791595e` |
| Corrected source tree | `618a3f774ff2d304295803f25eda79e78adb1492` |
| Original base | `49a2cc42462b47026e86313bfeff39a9b17081cd` |
| Corrected CI | https://github.com/physicsvigilante/sim_heat/actions/runs/43728497707 — **PASS** |
| Corrected CI artifact | https://github.com/physicsvigilante/sim_heat/actions/runs/43728497707/artifacts/14166838398, SHA-256 `51f0ea680b64b9b11b1562654878d908ef40639677c620baabc61c323d7d4e77` |
| Preserved failed intermediate CI | https://github.com/physicsvigilante/sim_heat/actions/runs/43728041002 — **FAIL**, historical hash refusal; do not erase |
| New Chat B report path | `projects/sim_heat/pr-12/reviews/review-02-chat-b.md` (author must be Chat B) |

## Exactly what changed

Six paths from [original reviewed SHA to corrected SHA](https://github.com/physicsvigilante/sim_heat/compare/f2bb5369425a250cef78b74baaf486925f8fa6bd...adb1b664d1a026f2f6cf017c11eda057d791595e):

1. `h1/matv4.py`: provenance schema **`sim_heat.matv4_adapter/2`** replaces misleading `channelIsIndependentMeasurement` with `hasUniqueMATChannel`. Unique indexed native parameter/solver output is **not** independent physical measurement; signed/shared alias source channel identity remains.
2. `h1/tests/test_matv4.py`: semantic regression across unique `data_1`, unique `data_2`, shared/signed aliases and binNormal/binTrans native/synthetic orientations, with `nativeQualified=false`.
3. `h1/tests/test_resolution_campaign.py`: preserve historical hash-pinned original plans, generate separately repinned scratch test-only plan and add explicit negative historical-plan-refusal test. Never disable identity validation.
4–6. Root `README.md`, `docs/H2_00_INTEGRATION_SCOPE.md`, new `docs/H2_00_REVIEW_CORRECTION_F01.md`: clarify format version, historical sidecar preservation, offline CI's network-capable pip install and known trust/qualification limits.

## Evidence and requested decision

The new exact-head CI passes **151/151 H1 tests**, **4/4** analytical tests, and non-native DEV_BRIDGE admission + sealed-reference preparation. Artifact ZIP CRC/head/test results verified by Chat A. **Zero new native runs**; physical laws, reference solver, verifier, acceptance allowances and reusable native runner remain byte-identical to the original reviewed version.

Please check:
- Is the new name/format **truthful and unambiguous** for unique `data_1` parameter rows and unique `data_2` solver rows, while preserving alias signs/shared rows?
- Are legacy v1 sidecars explicitly historical and not silently converted/promoted?
- Do the source and test changes retain fail-closed old plan SHA enforcement while allowing a separately identified current-source scratch fixture?
- Do reviewer findings F-02 and F-03 remain accurately represented, and is full final-head CI genuinely green?
- Any new demonstrated evidence-integrity blocker **caused by this narrow correction**? If so provide reproducer, expected/observed result and smallest regression. Do not claim that unrelated R3/native/C1/classroom gates are now closed.

**Report:** publish one **new** file at `projects/sim_heat/pr-12/reviews/review-02-chat-b.md` following REVIEW-TEMPLATE.md, verdict `pass`, `changes-requested`, or `insufficient-evidence` **for this targeted correction**. Distinguish actual independent execution from inspected previous CI/author results. Do not overwrite `review-01-chat-b.md`, amend source PR #12, launch native simulation or merge production code.

Chat A cannot self-authenticate this report. Owner merge approval remains separately required even if re-review passes.