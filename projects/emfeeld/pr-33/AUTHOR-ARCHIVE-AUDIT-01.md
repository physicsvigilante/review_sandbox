# PR #33 — author original-artifact verification, corrected exact source (2026-11-17)

**Verdict: AUTHOR SOURCE/CI QUALIFIED; independent Chat B R1 review NOT yet conducted.** This is a reproducible author audit of actual GitHub archives, never a new human physics certification or evidence that a teacher used the system.

## Exact source and historical first failure

[Draft source PR #33](https://github.com/physicsvigilante/emfeeld/pull/33) head `ee54e96488e5cd9d2eb904abf65811627bfcc006`, original Git tree `b8581afb8816052980dc03be27a3ad8acf1dd447`, qualified PR #29 parent `3f1ec44a54b24b9f8275a98abf81126a9386bf61` / tree `3d9fa4c8b594e46837e6825590e4e5d72db9a030`. Exact-source GitHub PR CI preview `821a1ffb85cdf1c57113531e70cb26f5b77ae5c1` has **identical tree** `b8581afb...` and exact ordered parents [qualified parent, head]. The source introduces only four files (test fixture, frozen questions, read-only ZIP evaluator, bounded scope document); production `src/emfeeld` remains unchanged. The later separately released PR #32 main commit `a18c26f050f5320ce8a9d61f7169e32cd6e31f38` is **not** part of this earlier original PR preview; any eventual merge must preserve it and require fresh combined post-merge CI.

Preserved failed original older-head [Windows #44024622664](https://github.com/physicsvigilante/emfeeld/actions/runs/44024622664) is **not** called a pass. The old test incorrectly expected a backslash ZIP fixture to remain raw under Windows `zipfile`, which canonicalized it. Corrected commit changes the test only (+13/-1); frozen question fixture and original evaluator bytes unchanged. Corrected exact-source 109 focused tests passed locally and from original source snapshot.

## Original corrected-head GitHub qualification

- [Linux/Windows clean-install #44025432673](https://github.com/physicsvigilante/emfeeld/actions/runs/44025432673) **completed SUCCESS**: original Ubuntu job `133844496365` and Windows 2022 job `133844496758`, **1,511 headless +18 historical behavioral passed (one obsolete all-file freeze guard deselected) +33 real-PyVista per OS**, original logs inspected. Separate 96 focused ensemble tests rerun but already included within 1,511 headless definitions; do **not** add them.
- [Real-PyVista #44025432632](https://github.com/physicsvigilante/emfeeld/actions/runs/44025432632) **SUCCESS**, 9 original offscreen cases PASS.
- [Source snapshot #44025432672](https://github.com/physicsvigilante/emfeeld/actions/runs/44025432672) **SUCCESS**, original downloaded `tested-source.tar` SHA256 `b50e944c7025b1c9b748b575fd247207350d3d27b4413a9f4daf1f7123c6e914`; 352 original Git-tracked files independently extracted and `git write-tree` exactly equals `b8581afb8816052980dc03be27a3ad8acf1dd447`.

| Original ZIP artifact | GitHub artifact ID | Independently computed raw ZIP SHA256 | Verified inventory |
|---|---:|---|---|
| Current-head Ubuntu release | `14303630672` | `73e420e2e0a1993d1f96c429c7db5836106df3acd28eceb25e2bf807bf0ea1b4` | 2,161 entries |
| Current-head Windows release | `14302868857` | `4132455d5a0c0b8491ff236b15105a012d16720dbe3354fb9c9f01dc48979278` | 2,161 entries |
| Current-head source snapshot | `14302339387` | `36daa3b71f09a7482e2c76555293bafce426e62cda12e2d4b0bb07fba3ad7eee` | 4 entries |
| Current-head real-PyVista | `14302244999` | `509f2920e25c0aa88db921c50a79ec21bb952123e088b50a073e907da1ce3fd3` | 22 entries, 17 PNGs |

All four raw ZIP hashes were independently recomputed from the **actual original downloaded GitHub ZIPs** and match the GitHub artifact digest metadata. Each original archive passed CRC/read, duplicate, case-insensitive filename collision and unsafe path checks. The viewer original `report.json` binds preview `821a1ff...`, has nine PASS cases, and all **17 original PNG SHA256 filename receipts** match the actual PNG bytes. Original CI `head-sha.txt` on each OS is `821a1ff...`. Offscreen success is not a manual Windows desktop/mouse or classroom acceptance.

## Exact original PR #29 frozen sources and pilot execution

The evaluator deliberately reads **previously released PR #29 saved E1/G1/T1**, not current-head synthetic fresh physics. Its frozen 3-question fixture SHA256 is `536ada6775aa3effb7abafaef742f7cb0030ce4428bcecf1d4664e1025436008`. Original *actual PR #29 merged-main* archive ZIPs independently downloaded, SHA/CRC-verified:

- Linux artifact `14300302937` original SHA256 `0654fa7d39249c4026945295ce15a18eae46a8598325e66d321cd515aa1e7f55`.
- Windows artifact `14301401780` original SHA256 `be72aef030afef113758a671aa93363b7e01af51ad9e79d942b91ea508c9a27e`.

Both originals have 2,161 CRC-clean entries, preserved under read-only analysis. Running the **exact corrected-source** `PYTHONPATH=src python verification/teacher_transfer_pilot_v1.py ORIGINAL_ZIP --platform linux|windows` against those original archives gave exit 0 and the original previously recorded stdout JSON SHA256 **Linux `0e0d0db21e19b5075df9be3069937f88156dbe914cd1cd0e987a0ba7cba3aab7`**, **Windows `20615a519c9f674387ce6d9e29f307f8227c5e1f372441f077f2877a09e483bb`**. Three retrospective questions, **four source-bound signed physical measurements and exactly one honest `unavailable/unknown_operand/null`** per OS; E1/T1 global complete, G1 global partial. Original values remain E1 A `-0.05458851160751549 N/C`, B `+0.18513207463551812 N/C`; T1 A `+1.1741058461436236 V`, B `+1.513997527981914 V`. G1 newly added body had no baseline counterpart, **not** a numeric zero.

Original corrected source `PYTHONPATH=src python -m pytest -q -W error tests/test_teacher_transfer_pilot_v1.py tests/test_scenario_ensembles.py` **109 passed** in this separate audit. A one-byte corruption of a *copy* of the pinned original ZIP and passing a genuine Linux ZIP with `--platform windows` both refused exit **2**, zero result stdout, before sealed source extraction, and did not mutate original archived input bytes. CI original E1 complete and G1 partial readout files were inspected as additional compatibility evidence (not a second independent physical solve).

## Honest bounds and next gate

These are **author-side executed checks of exact-source artifacts**. The pilot is an author-selected retrospective transfer from sealed measurements, not an unseen teacher task, automatic natural-language physics interpretation, independent experiment, teacher acceptance, or textbook-answer-completeness evaluation. No changed field law, solver, native comparator, model history or already sealed originals. Original ZIP hashes and stored unkeyed SHA receipts are integrity checks, not proof against an attacker able to rewrite and fully re-seal every unkeyed hash. The prior bad Windows fixture remains preserved as first failure.

**Independent separate-conversation focused R1 review is the next mandatory gate.** Do not merge/source-approve solely from this author audit. Reviewer must independently re-execute adversarial tests and publish a new attributable finding. The exact PR preview is based on PR #29; because actual `main` later advanced via PR #32, verify final main/source composite and fresh actual main-push release evidence before claiming integration.
