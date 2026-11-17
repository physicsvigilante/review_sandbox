# Chat B — SIM_HEAT PR #45 finite JSON overflow / same-byte intake R2

Continue as independent Chat B reviewer for historical [draft SIM_HEAT PR #45](https://github.com/physicsvigilante/sim_heat/pull/45), exact source SHA **`278f8224fa23ec20bc6c7342ab433b9be17e4434`**, Git tree **`fc0dbe955a14a73e7e54dd8060cb5d469a6f91e6`**, immediate independently reviewed PR44 source base `331a04c34d465516ffb0ecbb580a334032fa7de2`.

Read the complete central R2 packet:
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-45/REQUEST.md

This corrects the **MINOR PR44 F-06 edge**: JSON `{"value":1e999}` uses legal exponent syntax but Python default float conversion produces infinity. Original PR44 intake still reported BLOCKED and Chat B gave it scoped PASS; the new correction must **reject exponent-overflow floats** using a finite `parse_float` hook. It must still reject duplicate JSON keys (including nested), explicit `NaN`/`Infinity`, malformed/invalid UTF-8, and continue to inventory any finite JSON contents as **UNTRUSTED LOCAL DATA**. The code also parses JSON **from the exact same raw bytes it SHA-256 inventories**, rather than reopening a second path via the previous metadata parser. This does **NOT** authenticate owners, solve malicious concurrent-file TOCTOU, or establish native evidence.

Diff from the old reviewed SHA is precisely **THREE modified PR44 code/test/scope paths + ONE new offline CI workflow**. Verify no inherited frozen first author physics/study, checker, PR31 V2 archive/manifest/reference, source release, original unlaunched plan or historic failure records changed.

Independently inspect/attack:
- `1e999`, `-1e999`, `1E+9999` and nested/list nonfinite exponent JSON: REFUSE.
- Finite `1e308`/small exponents: still UNTRUSTED, release **BLOCKED**, no native promotion.
- Nested duplicate keys and nonstandard JSON `NaN`, `Infinity`: REFUSE.
- Same captured JSON byte sequence used for local hash and parser; **no second pathname reopen** while acknowledging `stat`/symlink/pathname checks remain non-atomic.
- Even all nine forged native-looking files or a fake-CAS approval cannot qualify `model_res.mat`, compute nine native readings or permit any native/owner/CAS action.

Inspect exact-head [CI #44066896537](https://github.com/physicsvigilante/sim_heat/actions/runs/44066896537) **SUCCESS** at pinned HEAD and [artifact #14321730592](https://github.com/physicsvigilante/sim_heat/actions/runs/44066896537/artifacts/14321730592), ZIP **27,486 bytes**, SHA-256 **`b8ab525db9088747ccafdc8bab6e9e25f1c7922894ce9800b82a5bad11230587`**, 41/41 CRC valid and **333/333 OFFLINE tests** (24 intake, 309 inherited). Preserve [initial YAML-prejob failure run #44066782667](https://github.com/physicsvigilante/sim_heat/actions/runs/44066782667) at old interim SHA `77f0ef7d...`; that historical failure is not retroactively a pass.

Write a **NEW independent** `physicsvigilante/review_sandbox/projects/sim_heat/pr-45/reviews/review-01-chat-b.md` with **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, exact SHA/tree, personally executed attacks vs hosted CI, residual trust/TOCTOU limits. Original F0 `hotLead.G` 80×/≥100× scientific FAIL and PR32 original V2 bitwise regeneration FAIL remain; all **11 genuine native release prerequisites** are MISSING.

**Do not** edit frozen science, merge historical PRs, install/query/compile/launch OpenModelica, replace the owner-adopted original PR31 checking reference, waive error thresholds, mint an actual owner release or treat a local SHA as a native signature. Real native actions still require separate explicit owner authorization of a named version-query/build/single-launch budget and an independently reviewed protected release/host/plan/atomic CAS.