# Independent review of SIM_HEAT #175

**Verdict: accept for the bounded R1 CI change.** No blocking findings. [Draft source PR](https://github.com/physicsvigilante/sim_heat/pull/175) · [Pinned workflow](https://github.com/physicsvigilante/sim_heat/blob/db59710a2c2962b49efbc9c9555293d768c55ba8/.github/workflows/calorimeter-prediction-ci.yml) · [Review request](https://github.com/physicsvigilante/review_sandbox/blob/124bb77910bbc2e5b19cafba0e4091f436f398eb/projects/sim_heat/pr-175/REQUEST.md).

I compared base `b19119e49ee4102acfc82dd766641529778c000b` with head `db59710a2c2962b49efbc9c9555293d768c55ba8`. The sole changed file is the workflow. GitHub reports the PR targets `codex/radial-film-calibration`, absent from the old seven-name allowlist. The new pull-request base filters admit this target, nested `codex/**` targets, and `main`. The workflow explicitly checks out the PR head with credential persistence disabled and contents-read permission. Checkout, setup-python and upload-artifact use full commit pins. Python 3.13.5 and the three Python package versions are fixed. Ubuntu 24.04 is a moving hosted image, and the Node executable comes from that image.

## Evidence

[Job 136860012517](https://github.com/physicsvigilante/sim_heat/actions/runs/44908815360/job/136860012517) succeeded on the reviewed head. I downloaded [artifact 14708683843](https://github.com/physicsvigilante/sim_heat/actions/runs/44908815360/artifacts/14708683843), independently hashed its bytes and obtained `8ebb610c23cf663d929155b91a2458e447e8e02e63722b5b84473d2959c6ae55`. Its head.txt matches the reviewed head. I parsed all seven retained replay JSON files and read all five suite summaries.

| Archived suite | Passed | Skipped |
| --- | ---: | ---: |
| Top-level Python | 249 | 0 |
| H1 Python | 152 | 0 |
| Analytical Python | 4 | 0 |
| Network adapter Python | 62 | 1 |
| Node viewer | 42 | 0 |

The adapter skip is the optional original native archive and rehashed-mutant test. Its log records the missing external artifact. The controls that use synthetic inputs ran.

The four Python discovery roots and the three Node file globs select the intended offline suites. Each piped test command runs with Bash errexit and explicit pipefail. In an independent Bash control, a producer returning 7 piped to a successful tee returned 7 and prevented a subsequent marker command. The first attempt to start local Bash was blocked by the Windows sandbox before the probe executed. The retry produced the stated result. On a suite failure, later commands can be skipped and the always-run upload can retain partial evidence while the job stays failed.

## Limits

This review covers the exact-head offline job, including its discovery and archive behavior. The job does not test the synthetic merge commit, run separate qualification suites or browser smoke scripts, or establish native simulator or physical qualification. I inspected the CI logs rather than rerunning the full suite locally. The PR remained draft at review time.