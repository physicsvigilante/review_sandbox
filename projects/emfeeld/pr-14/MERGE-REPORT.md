# EM Fields PR #14 — approved merge and final post-merge qualification

**Final status: MERGED with explicit owner approval, POST-MERGE CI PASSED (2026-11-15 UTC).** This is a new append-only release record; the independently authored review and all older evidence are preserved.

## Source, authorization and identity

- Project: [physicsvigilante/emfeeld](https://github.com/physicsvigilante/emfeeld), source [PR #14](https://github.com/physicsvigilante/emfeeld/pull/14), now merged.
- The owner explicitly approved **PR #14** after reviewing Chat B's R2 scoped pass. No approval for subsequent milestones or new physics is implied.
- Source base: `7e6bd8c72cac7708ab3c2355cc1a98db09762133`.
- **Exact approved/reviewed head:** `d46d04e23a142ea1c969b964ae5e1780110264c9`.
- **Merge commit/current main:** `8fe6331aefa252585b3b90f54b8ee7cbbac5e605` — [view source commit](https://github.com/physicsvigilante/emfeeld/commit/8fe6331aefa252585b3b90f54b8ee7cbbac5e605).
- Merge parents: the source base and the exact approved head above.
- **Exact source Git tree:** `c274d94dd2185dcecdfca735e2951edae3e3d835`. The merge tree equals the approved, reviewed and pre-merge qualified candidate tree byte-for-byte; the merge introduced no additional source changes.

The bounded feature adds/removes one independent nonrelativistic test particle in an immutable, exact-parent model revision. It does **not** introduce particle–particle forces, source backreaction, coupled electric/gravitational dynamics, material collision handling, a new solver or a new viewer.

## Preserved independent-context R2 review and limitations

- Original [Chat B review 01](reviews/review-01-chat-b.md): **scoped PASS at `d46d04e23a142ea1c969b964ae5e1780110264c9`**, Git blob `3b115f30ef1b17f350103eb21c67ba1c6a012d5b`; no demonstrated production blocker or major code defect. The reviewer independently reran 165 existing tests, authored a three-particle electric composition with middle-particle removal/reindexing and initially particle-free gravity case, tested identity collisions/dependencies and one local writer race, and performed independently expressed source-field and trajectory calculations against archived native traces. Review first attempts remain in that report.
- [Chat A response 01](responses/response-01-chat-a.md), separately attributed, did not alter the Chat B review and did not claim another independent reviewer.
- Reviewer F-01 was a **minor evidence clarification**: OS-local Python-file raw SHA-256 may differ because of LF/CRLF; canonical Git tree and blob provenance match.
- Reviewer F-02 was an **unresolved scope question, not a demonstrated code bug**: one successful local concurrent-write challenge is not exhaustive crash recovery, cross-process, distributed-filesystem or hostile-writer qualification.
- Independent-context ChatGPT review does not constitute independent human physics adjudication, novel held-out source interpretation or classroom teaching validation.

## Accepted pre-merge evidence

- [Original PR Linux/Windows clean-install release qualification](https://github.com/physicsvigilante/emfeeld/actions/runs/43740900095): success per OS, 1,308 headless + 18 historical behavioral + 33 real-PyVista tests. One historical all-file-freeze assertion remained unchanged and explicitly deselected.
- [Separate pre-merge real-PyVista workflow](https://github.com/physicsvigilante/emfeeld/actions/runs/43740899982): success.
- Exact pre-merge CI checkout `014d74123551cd1ab0ce5fbc335082663d160352` carried the exact approved Git tree.
- Pre-merge Linux ZIP ID `14172094227`, SHA-256 `a56b4b1352fcdcc31089ceca9b54ffb3e23910587f828ecc66b48b2e6830fed1`. Pre-merge Windows ZIP ID `14172751162`, SHA-256 `aa975b9ff5cd309df360b2f618c6b6b4163b6d1ca41b5a05612fa33baee29d08`.

## Fresh merged-main CI — PASS

- [Post-merge Linux/Windows clean-install release workflow](https://github.com/physicsvigilante/emfeeld/actions/runs/43746291562) **completed SUCCESS** on **Ubuntu 24.04** and **Windows 2022**, checking out merge SHA `8fe6331aefa252585b3b90f54b8ee7cbbac5e605`.
- [Post-merge separate real-PyVista workflow](https://github.com/physicsvigilante/emfeeld/actions/runs/43746291552) **completed SUCCESS**.
- **Per operating system:** 1,308 headless tests passed, 18 historical behavioral tests passed (one unchanged obsolete file-freeze guard deselected), and 33 real-PyVista tests passed. This equals **1,359 tests by suite membership per platform**. The same suite run on both OSs is not 2,718 distinct test definitions. The full workflow additionally executed the E1/G1/T1 particle-revision native and separate-reference qualification.
- Both original downloaded post-merge ZIP archives were SHA-256 checked against GitHub's artifact digest, with **1,451 ZIP entries and no CRC errors each**:

| Platform | Post-merge artifact ID | Verified SHA-256 |
|---|---|---|
| Linux | `14174408661` | `e8877dd69abe0cdf56d39b7fa447988b27f53ea103ecfe5e4b5c001ad833110d` |
| Windows | `14175016636` | `46bc735bb61cdbf49439a53dc8bf95bece292ce26e01a648145c650a27b7e92a` |

- Each ZIP's `head-sha.txt` equals the **exact merged commit**. Each `headless-tests.log` records **1,308 passed** and `viewer-tests.log` records **33 passed**. Full GitHub job success covers all required remaining gates.
- Read-only inspections of archived `particle-revisions/qualification.json` and `particle-revisions-reference.json` on both platforms found aggregate **`complete`** and reference **`passed`**; every case preserved its baseline. The native statuses were identical on both OSs:
  - **E1:** complete baseline and complete added-particle revision; original particle unchanged.
  - **G1:** complete baseline, an **intentionally rejected** old investigation requesting the removed body, and complete revised run for the surviving particle after native reindexing. That refusal is expected correct behavior, not a CI failure.
  - **T1:** three complete **static electric** source-field runs (baseline, added, removed); no unsupported shell/plane motion is claimed.
- The separate reference checker confirmed **34 static checks and six checked trajectories**. It is same-author verification; it is not a new reviewer-controlled integration. The original static inputs, source identities and preserved negative evidence have not been overwritten.

## Final disposition

**PR #14 is integrated and post-merge qualified.** The implementation preserves source laws, native solver/integrator, physical evidence and viewer behavior within the stated bounded regime. No new defect was observed at the post-merge CI gate.

The user's Windows/Conda installation and original saved model stores/runs were not changed by these GitHub actions. Windows offscreen CI does not independently prove Windows desktop mouse behavior. Teaching evaluation remains paused. Any further physics/evidence feature requires a new risk classification, exact-head CI, an appropriately scoped independent-context review under [the central protocol](../../../PROTOCOL.md), and **separate owner merge approval**.
