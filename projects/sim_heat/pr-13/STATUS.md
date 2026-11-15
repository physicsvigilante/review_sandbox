# SIM_HEAT H2-01 — PR #13 centralized review status

**Status: `awaiting-focused-review`.** Chat A completed and tested the read-only viewer; **Chat B has not written a review report yet**. No merge approval has been requested or granted.

| Field | Exact identity / state |
| --- | --- |
| Project | `sim_heat` |
| Source repo | https://github.com/physicsvigilante/sim_heat |
| Draft source PR | https://github.com/physicsvigilante/sim_heat/pull/13 — **draft/unmerged** |
| Base SHA | `ecebc38dd3f6eaffd297bd3df97a0883e591c6ac` |
| Final source SHA | `e8449989ba55a972976ebba7e9708bc4e2351a18` |
| Source tree | `c342ace7233dd112fa494be91785f79f23debeca` |
| Risk | **R1, focused separate-chat review** for native-evidence presentation |
| Final CI | https://github.com/physicsvigilante/sim_heat/actions/runs/43736122931 — **SUCCESS** at exact head |
| CI artifact | https://github.com/physicsvigilante/sim_heat/actions/runs/43736122931/artifacts/14169479149 |
| Artifact SHA-256 | `f5100b7f9ab2ddb2e8634eda1b11d4a3f9b1d31c67031aa59c0ebf35c91bf640` |
| Checks | 151/151 H1, 4/4 analytical, 7/7 viewer tests; real desktop/mobile Chromium smoke with clean/refusal screenshots |
| Native builds in viewer CI | **0**, existing native evidence only |
| Preserved first failure | https://github.com/physicsvigilante/sim_heat/actions/runs/43735810229 — incorrect viewer negative-test fixture, never rewritten |
| Current reviewer report | **Not received**; Chat B must write new `reviews/review-01-chat-b.md` |
| Owner merge approval | **Not granted** |
| Merge/post-merge CI | **Not done** |

## Handoff files

- [REQUEST.md](REQUEST.md) specifies physical semantics, historical source/run hashes, screenshot checks and targeted adversarial questions.
- [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md) is ready to paste in a separate ChatGPT review conversation.
- [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md) governs Chat B's newly committed report.

**Next:** User sends the prompt to Chat B. Chat B writes its *own* unique file under this PR #13 central review directory; Chat A must not author or fabricate that report. On the owner's **"Review complete"**, Chat A fetches it directly from GitHub, verifies exact reviewed SHA, reproduces confirmed findings, adds regressions, reruns CI and requests only targeted re-review as needed. Owner must separately approve any merge, and then Chat A verifies post-merge CI and updates the central record.

The first viewer stage does not qualify new physical systems, independent measurements, untested values or classroom effectiveness; `diagnostic_only` and `nativeQualified=false` are preserved.
