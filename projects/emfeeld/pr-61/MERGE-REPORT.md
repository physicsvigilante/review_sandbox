# EMFEELD PR #61 — final actual-main technical release (2026-11-20)

**STATUS: MERGED and technically release-qualified.** The narrow ideal infinite straight current-wire magnetic-field 3D lesson was merged through [PR #61](https://github.com/physicsvigilante/emfeeld/pull/61) after original independent review-01 **CHANGES REQUESTED** and new [independent review-02 scoped PASS](reviews/review-02-chat-b.md). The original [review-01](reviews/review-01-chat-b.md) remains unchanged; neither the reviewer's original blocker nor first reviewer-harness failures are retrospectively relabelled. No new general EM/Maxwell/Biot–Savart solver or modification to old electrostatic/gravitation source code.

## Git identities

| Role | Git commit | Source tree |
|---|---|---|
| Original qualified main base | `d2f90afbf6c8910c410c41147925e311320f96b0` | `95f6f0b09cb24daaa0c9b1dd064fc68e3d09dced` |
| First independently rejected candidate | `d7151a35ecddace3f79786315fb4f07858e398cc` | `9886308b8a036eb65ca8e37dc86ef173c6e91e12` |
| **Independently scoped-accepted corrected HEAD** | **`76edda620213710e80860c3ee8abe312228b6c10`** | **`047eca847cfc6bacfc3afebd51cf912a2f9deb18`** |
| Premerge synthetic CI commit (not actual main) | `240c00931426198775e3f7910e0c8aa3923aaf3a` | same accepted source tree |
| **Actual production `main` merge** | **`52aecd34338662e269fba091c0ff6664e8e1eca7`** | **same accepted source tree** |

Actual merge parents are exactly [original base, accepted HEAD]. GitHub was re-read after integration; `main` points to that merge commit. The **452 original source files/regular Git blobs and modes** reconstructed from the actual-main source TAR equal the independent accepted Git tree. The TAR container hash differs from premerge for archive metadata, but all **452 actual tracked source file contents/modes** are identical; no source drift or physics changes.

## Independent review disposition

- Initial [review-01](reviews/review-01-chat-b.md): **CHANGES REQUESTED** because the blue Ampère loop did not visibly mark the positive circulation orientation; separate advisory about raw mixed Boolean/numeric direct Python probe validation. The math and SI signed integral had passed that independent science challenge.
- Corrected six-path source commit addressed both without altering physical B law or integral. Blue positive loop arrow is a separately identified 3D actor derived from positive SI loop tangents; green B arrows reverse or vanish with current.
- [Review-02](reviews/review-02-chat-b.md): **SCOPED PASS**. Reviewer authored **51 passing checks** and genuine Linux EGL PyVista0.48.4/VTK9.6.2 actor/keyboard/current/sign/zero/camera/reveal challenges; four new reviewer-owned state-bound screenshots (distinct from hosted author evidence). Author-owned hosted/local tests are not counted as independent reviewer runs. No human Windows GUI or JEE teacher outcome claimed.

## Actual-main push workflows (not reused premerge CI)

All **seven** fresh workflows completed **SUCCESS** for actual production main `52aecd34338662e269fba091c0ff6664e8e1eca7`:

| Workflow | Run | Outcome |
|---|---:|---|
| [Wire magnetostatics 3D](https://github.com/physicsvigilante/emfeeld/actions/runs/44669314204) | 44669314204 | SUCCESS, **108 focused tests**, 7 native scenes |
| [General real PyVista](https://github.com/physicsvigilante/emfeeld/actions/runs/44669313981) | 44669313981 | SUCCESS, 17 native viewer PNGs |
| [Gauss 3D](https://github.com/physicsvigilante/emfeeld/actions/runs/44669314024) | 44669314024 | SUCCESS, 22 current-state screenshots |
| [Conductor cavity](https://github.com/physicsvigilante/emfeeld/actions/runs/44669314089) | 44669314089 | SUCCESS, 6 native scenes |
| [Electric dipole](https://github.com/physicsvigilante/emfeeld/actions/runs/44669314020) | 44669314020 | SUCCESS, 14 native scenes |
| [Ideal capacitor](https://github.com/physicsvigilante/emfeeld/actions/runs/44669313994) | 44669313994 | SUCCESS, 9 native scenes |
| [Clean-install Linux + Windows](https://github.com/physicsvigilante/emfeeld/actions/runs/44669314074) | 44669314074 | **Both OS SUCCESS**; **2,173 headless + 98 genuine PyVista tests PER OS** |

Counts overlap rather than representing additive unique tests; warnings treated as errors. The original Windows suite completed after all other workflows; neither early pending status nor premerge success was promoted to final release success.

## Original complete artifact integrity and physics audit

Original GitHub Actions artifacts, **not reconstructed copies**, were downloaded and audited by whole ZIP SHA-256, ZIP CRC, path uniqueness, source-provenance identities, relevant scene receipt digests and physical samples.

| Exact actual-main artifact | Artifact ID | Original complete ZIP SHA-256 | Verification |
|---|---:|---|---|
| Wire native | **14599585276** | `706472aca25d45ea4ff41d11cf18ab27afb4d36b1378c73ba36b74eafe9d2c9e` | 7 current scenes, **49/49** receipt hashes |
| Gauss native | **14599825339** | `ee85b905f313abb0b46323e5a30c94121cb0f71a7a267cd2e3cc6627955b56c5` | **148/148** receipt hashes |
| Cavity native | **14598259805** | `27c5c4ad1d6f8d24d9666be7b07cd27a691b1742ca9c5478f1378f608fd12a52` | **36/36** |
| Dipole native | **14599307823** | `8387c87934eac32db0159c9667444efce00b90ce97217d86c5f965a58e502aeb` | **239/239** |
| Capacitor native | **14599517304** | `24192c94ff9e131a5f21fca9b78057f2e663c4e133a700d251a5cc3d65b676ea` | **63/63** |
| General viewer native | **14599288177** | `bd9aa15b79e61b1766605aa1bee333018b01524d31cc14ff6be5a87500c46807` | source matches, 17 PNGs, report PASS |
| **Linux complete RC** | **14599039781** | `b185cdc32e3fcdd5faec167e3216a1fc095e856e7f2dc26de331a6caf85f9915` | **2,173 headless + 98 native PASS** |
| **Windows complete RC** | **14599808663** | `881e5fbe16d3bf34735da9203d8ff8a12c26068d50a2b2e5c9b9b9b896e4f0b8` | **2,173 headless + 98 native PASS** |

Each full OS artifact has **2,186 unique members, 173 actual integrity manifests, 1,749 matching SHA-256 file references, and exactly one deliberately corrupted historical negative receipt** at `derived-001/G1/review-challenge-resealed-native/native/result.json`, correctly detectable. The negative is intentionally not mislabelled as an unexplained product regression. Both `head-sha.txt` refer to **actual main `52aecd34338662e269fba091c0ff6664e8e1eca7`**, rather than synthetic premerge. Entire original ZIPs have clean CRC and match their GitHub-advertised SHA digests.

The actual-main wire archive field_samples.npz was independently evaluated using `scipy.constants.mu_0` and raw SI B·positive-tangent·physical arc weights: centre +5 A, doubled radius +5 A, reversed −5 A, zero current and tilted axis −8 A produce the expected `mu0 I` within ordinary float64 rounding; R doubling halves local B while preserving integral; the current-independent blue positive arrow is present when B vanishes. The archive's field/geometry/presentation metadata agrees with the actual scene captures. No fake current-dependent integral normalization.

## Final scope and next steps

**Technically released:** exact static analytic magnetic field of one ideal infinitesimally thin infinitely long steady current wire, 3D right-hand rule, signed Ampère loop and direction-only field arrows, with strict input refusal and original/current source provenance.

**Not certified:** finite wires or ends, circular-current-loop physics, solenoids, Lorentz dynamics, time dependence, arbitrary Biot–Savart, current material effects, human Windows GUI operation, actual classroom usefulness or any new examination score. **[Issue #60](https://github.com/physicsvigilante/emfeeld/issues/60)** is technically complete; a separate prospective small circular-current-loop axis-only analytic teaching scope is [Issue #62](https://github.com/physicsvigilante/emfeeld/issues/62). Never conflate that future issue with this qualified source.
