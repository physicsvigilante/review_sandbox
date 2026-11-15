# PR #75 — targeted follow-up request (cross-repository handoff)

**Read** [STATUS.md](STATUS.md), [hub protocol](../../../PROTOCOL.md), [risk policy](../../../REVIEW-RISK-POLICY.md) and [first Chat B report](reviews/review-01-chat-b.md).

- Project: opticsim
- Source PR: https://github.com/physicsvigilante/opticsim/pull/75
- Reviewed implementation head: **`f4fddec213e04d733920399dc0eeea0b29a60dac`**
- Base SHA: `c0d4e3048b9e0935cfd567e5f3c81aab23ddd823`
- Frozen implementation tree: `d8d70b08bddd3c07aa1f50247341423f124818b0`
- Class: **R2**, but **this is a targeted follow-up**, not another whole-implementation review
- Source review PR #77: https://github.com/physicsvigilante/opticsim/pull/77
- Chat A developer triage: https://github.com/physicsvigilante/opticsim/pull/77#issuecomment-6894596523
- Source full-CI: https://github.com/physicsvigilante/opticsim/actions/runs/43700823059
- Source refraction-CI: https://github.com/physicsvigilante/opticsim/actions/runs/43700823106

## Evidence gap G-01: published review instruction location

The first reviewer correctly observed that the **original collaboration protocol, request and template were absent** from the floating `main` and frozen source head. These files were ALREADY published on a **separate draft Opticsim PR #76 branch**, not in source `main`. The immutable original protocol/packet/template links are in [ORIGINS.md](ORIGINS.md) and can be compared with the first report. Do not rewrite the first review's true 404 observation. Check whether the exact originally published instructions are consistent with the reviewed claim. The central protocol is a **later coordination improvement**, not a retroactive first-pass acceptance condition.

## Evidence gap E-02: new actual adversarial native/browser verification

Chat B should prioritize genuinely new test-only controls for the existing bounded detector-hit feature, without modifying PR #75 implementation:

1. Native detector orientation/endpoint challenge: reversed orientation and/or 0.009 vs 0.011 mm actual endpoint clearance. Check actual native completion, event geometry and classification; distinguish model preflight rejection from measurement qualification.
2. Mixed two-detector overflow: one detector records more than 32 native callbacks, the second stays under the cap and remains available, without clipped first-detector list or corrupting old counts.
3. One representative stale revision, native failed callback, or incoming-ray/point inconsistency case. Check that accepted observations are withheld when their runtime source is not qualified.

Where feasible, write **test-only** adversarial code on a new Opticsim branch rooted at `f4fddec...`; open a draft PR to trigger pinned-source GitHub CI, and record exact new test SHA, modified paths, run IDs and actual outputs. Never change PR #75 head or production code. If the sandbox's contractual geometry makes a case impossible, report that, do not invent a successful trace. If independent execution is still blocked, state **insufficient-evidence** rather than transforming saved artifact inspection into new native execution. A test-only branch produces its own distinct source tree; prove production file blobs are unchanged.

## Other findings

- **H-03:** legacy public executor projections are trusted internal native evidence, not externally authenticated result ingestion; scene hashes are integrity checks, not signatures. This is a documented boundary, **not a reproduced external injection route**.
- **U-04/O-05:** optional teacher UX or storage granularity; do not expand feature scope on their own.
- Review must distinguish captured CI results from tests genuinely authored/executed by Chat B.
- No merge, no forced sign-off and no retesting broad unchanged functionality merely to inflate the review count.

## Output

Create a **new** file **`projects/opticsim/pr-75/reviews/review-02-chat-b.md`** in `physicsvigilante/review_sandbox`, preferably directly on main with this unique path (or in a separate review branch/PR). Keep original review-01 unchanged. Include exact implementation and test SHAs, run URLs, negative results and verdict for the remaining gaps. The owner then says "Review complete" to Chat A, which reads the report from central GitHub.

If the implementation head moves, identify it as stale and do not transfer an old pass to a new SHA.
