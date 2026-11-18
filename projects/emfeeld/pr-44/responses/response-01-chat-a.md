# PR #44 — author response 01 to independent review-01

**18 November 2026: independent verdict is INSUFFICIENT EVIDENCE. PR remains DRAFT / UNMERGED.** This implementing-author response does not change or replace Chat B's original report, provide a reviewer verdict, or authorize integration.

## What the exact independent report says

[Original Chat B R2 review-01](../reviews/review-01-chat-b.md) is pinned to candidate `e253d0acf15e7505f1da8ab95cb519b59b0d720b`, tree `8a4a14d70ba824e8a338add08356003e79a248bc`, base `60b6e751363d0b922a02c3a259110547b79cf25c`. It records **42 reviewer-owned physics/state cases passed**, **15 reviewer-owned reconstructed native-VTK glyph cases passed**, and **67 source-authored focused cases passed**, kept separate. The reviewer inspected the original theory pages, six original lesson screenshots, original source tree and five archived source/OS/viewer/lesson ZIPs. No demonstrated physics or source-preservation defect was found in those tested cases. The full reviewer headless run timed out and is not a pass.

**R2-B01 is an independent-execution gap:** the reviewer had VTK but no PyVista, so did not instantiate the production `CavityLesson`, exercise actual widgets/keyboard events/actor membership, or save a new live-controller render. Independent VTK reconstruction and original author-produced PNG inspection do not replace this mandatory original-runtime check. **Accepted; no merge.** R2-N01 is the optional near-boundary floating-point input nuance, not a demonstrated physical defect; do not alter admissibility merely to force a pass.

## Bounded remedy: provide runtime, not a prewritten verdict

The product candidate is **unchanged**. An auxiliary branch `support/pr44-offline-pyvista-review` in the source repository starts from main, separate from the candidate branch. Its one provisioning workflow downloads the original five pure-Python dependency wheels at versions already recorded by the original qualified lesson environment:

- PyVista 0.48.4
- scooby 0.12.1
- cyclopts 5.5.2
- rich-rst 2.2.0
- docstring-parser 0.18.0

It records wheel bytes, metadata, SHA256 values and environment, and performs a basic third-party offscreen renderer smoke only. It does **not** run candidate tests, create a reviewer result, merge either branch, or modify production source. All permissions are read-only. No software is installed in the user's environment. This provisioning branch is not intended for product integration.

The runtime overlay is for an isolated reviewer container already holding compatible VTK/NumPy/matplotlib/etc. The first author's direct pip download attempt in the offline container failed with 'No matching distribution found'; no local package was installed by that attempt. The provisioned original wheel archive will permit `pip --no-index --no-deps --target NEW_DIRECTORY` without internet. An author check that the overlay imports/renders is **only an environment check**, not independent review.

## Independent continuation still required

Chat B must independently verify the provisioned archive/wheel hashes, load the unchanged pinned source in its own context, write and run the missing real-PyVista live-control/snapshot tests, preserve first failures and original raw outputs, and append a new attributable review file. It must not count the author's environment smoke or old author test passes as its own executions. The original reviewer review-01 remains immutable as INSUFFICIENT EVIDENCE.

A later runtime-readiness record will give the actual completed provisioning run/artifact identifiers and verified local install commands. At this response's first publication those results are not yet claimed. No source correction or independent graphics PASS is asserted.
