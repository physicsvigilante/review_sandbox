# Chat B — SIM_HEAT PR57 independent focused R1 correction review 02

Original [Chat B review-01](reviews/review-01-chat-b.md) returned **SCOPED PASS for original source** but found F-01 duplicate Host headers not refused (minor, genuinely reproduced) and F-02 lack of same-machine privacy warning (minor). Preserve its original verdict and exact old head; do not rewrite reviewer history.

**New corrected source PR:** https://github.com/physicsvigilante/sim_heat/pull/57 — remains **draft and unmerged**.
**Review exact NEW HEAD:** `a663c4c8c37494c1db6ef5fcaf32da0d4ba4fcba`
**Git tree:** `0c44961b473d23737b0c9f3b3f2cd3db65b9f264`
**Old reviewed HEAD:** `e8a9696c8f14bc59c2d3918e65c987a8c4230bf0`.
**Base main:** `20f5605d28f22d4a7dc86ad478a4cf44347157d4`.
**Diff from old head:** exactly three modified files (workbench Python, workbench tests, local guide). Full PR remains five added files. No changes to physics, H1 parser, generic source viewer, native runner, archived originals or C1.

**Read full targeted central request FIRST:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-57/CORRECTION-REQUEST-02.md

Independently verify strict **exactly-one Host** handling: raw HTTP/1.1 to actual loopback with valid+evil, evil+valid, same+same duplicate headers, HEAD duplicate and missing Host must all refuse 421 with no source JSON; one proper `Host: 127.0.0.1:port` must still load real admitted source. Challenge case/port/path behavior and missing information leakage. The new regression test was **actually run against the old source first** and failed three cases (old implementation gave 200); the exact same test now passes on corrected source. Do not call the first failed attempt a pass.

Verify privacy warning **in both the local help page and canonical guide**: another process on the same computer can GET admitted source if it learns the port, no local authentication, no secrets in notes, avoid shared/untrusted machines, stop with Ctrl+C. No general public-server security claims. Verify unchanged source-only `not_computed` statuses, H1 admission/refusal and all six original diagnostic-only archived bundles.

Inspect exact-head:
- [Push CI 44312686935](https://github.com/physicsvigilante/sim_heat/actions/runs/44312686935), artifact [14431216832](https://github.com/physicsvigilante/sim_heat/actions/runs/44312686935/artifacts/14431216832), SHA256 `53a201c4561bbca3668409fddbf850381ff5ad4551c91622653678651238d0c5`, **56 distinct CRC-valid entries**.
- [PR CI 44312700673](https://github.com/physicsvigilante/sim_heat/actions/runs/44312700673), synthetic merge `d99773ed095a1b2809be60992eecd619109d7ffb` same tree as exact source, artifact [14431251686](https://github.com/physicsvigilante/sim_heat/actions/runs/44312700673/artifacts/14431251686), SHA256 `0be4a67e13d723a153f1aabfff9c7d83a94f527c7c43f9285c233869d397f6c1`, 56 distinct CRC-valid entries.
- [Audit core 44312700604](https://github.com/physicsvigilante/sim_heat/actions/runs/44312700604) SUCCESS.
- Both workbench runs: **300 tests passed, one optional skip**, all six original archive cases BYTE_IDENTICAL with nativeExecutedByReplay=false, current source-only output and comparison byte-identical, real HTTP Chromium workbench and all original explorer/source/docs routes PASS. Distinguish your personal executions from hosted evidence.

Read `AGENTS.md`, the central review protocol/policy/template and original report. R1 source-only HTTP hardening, no new physical/numerical/native meaning; escalate only if you uncover a real result/evidence semantic change. Author and commit **your own NEW report** to:
`physicsvigilante/review_sandbox/projects/sim_heat/pr-57/reviews/review-02-chat-b.md`.

Report concrete defects if any and one verdict **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, exact head/tree and first-failure evidence, privacy limitations and personally run vs hosted tests. **Stop before any source merge, deployment, OpenModelica install/query/build/launch, native runner, frozen-reference regeneration, historical C1 integration or qualification promotion**. A new reviewer pass is **not** owner merge authorization.
