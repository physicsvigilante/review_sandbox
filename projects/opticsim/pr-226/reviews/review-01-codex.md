# Independent Codex review of Opticsim PR #226

**Outcome: pass. No unresolved blockers or demonstrated defects within the test-only study.**

- Source [PR #226](https://github.com/physicsvigilante/opticsim/pull/226), production base `c3913e3a8faaaf38e9fd4db4f04fe77fee8f2abc`.
- Exact head `fc8c8cd3ab3f58b01bef44e3b13a92978e13c16a`, Git tree `6d7be96d5ed57da9e8bd7fe25837477b73dd68dd`. Reviewer: independent-in-context Codex agent, 2026-11-21. [Exact source](https://github.com/physicsvigilante/opticsim/tree/fc8c8cd3ab3f58b01bef44e3b13a92978e13c16a)
- Scope: source provenance, frozen synthetic geometry, pinned native ray histories, numerical boundary withholding, evidence integrity and production compatibility. The diff changes only the frozen inputs, study notes and one test file. Production source was untouched by this review.

## Source and results

I opened only the original A19 Problems crop and verified SHA-256 `6f55569c754d61d285817f631a263321f9d345c2b1ae459f29e97ac4217b9cc7`. A19 supplies a cylindrical guide, core index 1.36, external air and a meridional launch-angle question. Guide and source dimensions are unspecified. Freeze commit `ddb4b0aa60346f749a987029f6d3ef46b6590dfa` predates the test implementation and its JSON blob is byte-identical to the reviewed head. The rectangle, emitter, finite passive detector and sampling choices are explicitly synthetic. No Solutions material was opened.

Rebuilt the pinned PhyDemo core at `811f508d2b070898c241a568b0c167dcb8645251`. All nine focused tests passed, covering the three genuine native AngleSource fans, ten individual pinned SingleRay replays and six existing analytical/native two-face checks. The test delegates to native Glass and Detector callbacks and matches isolated launch histories against the rays emitted by each fan.

Independently unfolded the two noncritical fan histories into straight trajectories inside the 2D rectangle. Compared forty actual Glass callbacks and ten Detector callbacks against the analytical intersections and normalized incoming/outgoing directions. All six guided rays exited the right end after three or four sidewall reflections, and all four leakers left through a sidewall and subsequently reached the same downstream detector in exterior air. Maximum position and direction-component residuals were `8.03e-13 mm` and `1.18e-14`. The minimum ground-truth face-end clearance was 4.109 mm and the minimum dimensionless distance from the sidewall critical threshold was 0.01007. The largest numerical difference between native fan records and their corresponding native SingleRay records across the compared positions and unit directions was `1.71e-13`.

For the declared equal exterior index, the meridional threshold is `asin(sqrt(1.36² − 1)) = 67.18142753797471°`. The first critical sample differed from the dimensionless sidewall threshold by `2.22e-16`. Its native callback faces were left, top and bottom. Both exact-head hosted and independent records preserve that represented history and label the fan `withheld-critical-sample`. The qualified claims cover sampled histories in the frozen 2D surrogate. Continuous guided acceptance, skew rays and transmitted optical power are outside the study.

## CI and archive

All 11 exact-head PR workflows passed. Hosted Unified workflow ran 1,325 tests with zero failures/skips, including all three study cases, on synthetic merge checkout `5808f2989219fd65174e46122a5f76cd7d050dd6`. I verified that applying the cited base to the reviewed commit gives the same tree with Git. Hosted optical composition completed the incumbent real Chrome suites. This study adds no browser UI. [Unified CI run](https://github.com/physicsvigilante/opticsim/actions/runs/44880227548) · [Optical composition CI run](https://github.com/physicsvigilante/opticsim/actions/runs/44880227425)

Downloaded the exact-head authoring archive `14697717122` and verified its SHA-256 `667e1a0cb1d8dfe1788f6540bdffbb2f1bf0b98002ed774c507e9aed7918625c`. All thirteen study JSON records matched the independent Windows replay byte for byte, including the two noncritical fans, ten single rays and the withheld critical record. [Hosted archive](https://github.com/physicsvigilante/opticsim/actions/runs/44880227425/artifacts/14697717122)

The independent full Windows suite ran 1,325 tests with 1,321 passing, one symlink privilege skip, and three CLI tests failing on duplicated drive prefixes in test paths. The same three failures reproduced on the unmodified production-base tree. The new tests passed on Windows, and the exact-head hosted Linux suite passed all tests.

The remaining passing workflow run IDs are `44880227351`, `44880227378`, `44880227386`, `44880227407`, `44880227417`, `44880227419`, `44880227437`, `44880227466` and `44880227500`. This clears the exact test-only source for owner-authorized integration. A future public guide capability requires its own scope and review.
