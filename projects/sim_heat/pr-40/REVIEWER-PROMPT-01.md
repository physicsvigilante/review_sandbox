# Chat B — independent SIM_HEAT PR #40 external-CAS contract FAKE R2

Review historical [draft SIM_HEAT PR #40](https://github.com/physicsvigilante/sim_heat/pull/40) at **exact source SHA `ebe203781e87ba108e8dec845074ca7ca47972ef`**, tree `ca0254a94bb2f6785608c0ad8700a693a00f647e`, independently scoped-PASS base PR39 `ffc96e743a78cb3c63c01d6bf292d1fa84c6164f`.

Read the central full [R2 request](REQUEST.md): https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-40/REQUEST.md

This source adds **four new files only**. `offline_external_cas_contract.py` defines a permanently **default-denying** native authority interface and an **UNTRUSTED in-memory fake**. There is NO real external provider, owner approval, connected secrets, OpenModelica, executable native adapter, global reservation or launch.

Independently test/inspect:
- zero-budget snapshot and refusal of forged owner source/release/OMC-query/build/launch flags; `require_native_permission`, `ExternalAuthorityUnavailable` always refuse;
- **same fake instance** thread contention allowing one fake first claim, **two distinct fake instances** each allowing one first claim for the same campaign (split-brain), and reset/recreation allowing another fake first claim;
- arbitrary valid-shape nonce is NOT owner authenticated, and fake receipts keep `nativeAllowed=false`, `realAcrossRunReservationAllocated=false`, `crossHostAtomicityProved=false`, `externalStoreConnected=false`;
- exact source SHA/tree and four-addition-only diff, original F0 physical/source pins and saved PR31 V2 scientific raw SHA/seal; original F0 80× accuracy **FAIL** and PR32 reference bitwise regeneration **FAIL** unchanged.

Inspect exact-head [CI #44039595352](https://github.com/physicsvigilante/sim_heat/actions/runs/44039595352), [artifact #14308567981](https://github.com/physicsvigilante/sim_heat/actions/runs/44039595352/artifacts/14308567981), whole ZIP SHA-256 **`9c1b5d893d4f579d1efbf80475efb4244d76e6ec349e7adfab693ea3bf1fb3c8`**, 38 ZIP members CRC valid, **260/260 OFFLINE test methods**, default-deny/split-brain/reset receipts and zero native operations. Distinguish personally executed probes from hosted source tests. Assess whether the interface is accurately labeled **not a real cross-host/owner-controlled one-shot gate**.

Commit a NEW independent `projects/sim_heat/pr-40/reviews/review-01-chat-b.md` in `physicsvigilante/review_sandbox` with **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, concrete findings and outstanding real release/native/atomic-store gates.

**Do not** edit original source, merge historical PRs, invoke/install OpenModelica, change numerical tolerances, adopt regenerated reference, create a real launch permit or treat the fake as a native gate. Any actual native version/build/single launch still requires a distinct owner authorization and separately reviewed real trusted source/host/plan/atomic store.