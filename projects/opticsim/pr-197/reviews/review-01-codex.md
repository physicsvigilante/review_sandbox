# Independent Codex review of Opticsim PR #197

**Verdict — CLEARED FOR OWNER DECISION.** I found no outstanding blocker for the bounded v29 sampled fan. The result covers the source, native simulation, evidence consumers and browser behavior at the following identities.

| Identity | Reviewed value |
| --- | --- |
| Reviewer | Codex, independently assigned by the owner |
| PR head | `e402f984401be63bee4c84b5cde93819210ed912` |
| Git tree | `1f35bb05c188eaab9c08ecf6e595c56f0d9cc081` |
| Base | `916745f5f64a2a86dc234758437a5fa57d3b9753` |
| Pinned PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251` |

## Independently reproduced

I read the base-to-head changes and ran an isolated export of the reviewed Git blobs under Windows with Node 24.19.0 and the installed pinned core. The seven focused suites covering the frozen study, public fan, composition profiles, v14–v21, v27, v28 and historical v18 integration passed all 59 tests.

- **Authoring and boundaries.** The explicit v29 model selects a single directional point source below one horizontal infinite interface with upward normal. The admission policy checks the entire cone, minimum 1 mm separation, absolute indices from 1 through 4, explicit Fresnel-off policy, brightness, density and a maximum of 100 samples. The tested native angular spacing was (360° / floor(500 × density)), with the upper endpoint omitted by the native angular cutoff. A 100-ray case qualified and a 101-ray case was refused. Existing single-ray J11 inputs keep their historical scope.
- **Independent physics check.** I enumerated expected angles from integer sample indices and observed each actual interface callback on the pinned tracer. A grid of 180 admitted scenes covered five signed directions, four pairs of material indices, three densities and three translations or separations. This included reversed component order and a source-to-plane separation of 18,299 mm. I checked every hit against a tangent projection and every outgoing unit vector against signed Snell transmission or specular total internal reflection (TIR). All 660 callbacks agreed, including 483 transmissions and 177 TIRs. Maximum absolute horizontal hit error was (7.82 × 10⁻⁹) mm rounded up. Both outgoing components agreed within (10⁻⁸). The public aggregate counts and first-event classifications also agreed.
- **Critical boundary.** On both sides of the surface normal, offsets of ±0.9 × 10⁻⁶ in the absolute Snell residual were refused. Offsets of ±1.1 × 10⁻⁶ qualified with the expected transmission or TIR. The frozen 41° and 50° pair yielded two emitted rays, two incidences and one TIR. The frozen fan containing the represented critical sample withheld the entire accepted result despite a raw native transmission for that sample.
- **Native audit and downstream consumers.** I injected omitted, duplicate and cloned roots, incorrect incident geometry, native warnings, wrong outgoing geometry, absorption and unexpected children in the delegate's return. Invalid evidence withheld qualification. A fabricated historical summary carrying a v28 success flag without the v29 proof failed snapshot, comparison, notebook creation and replay. A two-sample sweep retained the failed sample and qualified the fresh run. Changed scene bytes suppressed stale observables. The marker assumes the application's own observer and immutable run inputs. Arbitrary code altering a callback result after the owning observer returns is outside that trust boundary.
- **Real browser.** I ran the public CLI and Chrome 158.0.8127.37 using a Windows-specific launcher in the disposable export. I observed the baseline, refusal and cleared prior results at a critical edit, qualified save disabled, both rays transmitting after changing the upper index to 1.4, and a fresh retrace of the downloaded qualified edit. I also directly asserted the angular sampling guidance and incomplete-run wording in the DOM. The seven-check run produced two screenshots. The local qualified browser export matched CI's bytes.
- **Historical controls.** I reran the original twelve-case J11 control and the frozen study's three fan configurations and eight matched single-ray controls. The protocol retained Git blob `46ff01445a55882d9bdd4f9254122a0bc58afc4a` and SHA-256 `e4fb5230ca74bb1fdf4ddbec823224e0f5de6b0afaac72db3cf45e0a3bc0b91b`. Its earlier commit establishes repository chronology. My rerun establishes reproducibility. The v29 UI provenance fixture extends the previous app blob chain, and the unchanged historical identities passed on the final head.

## CI and builder evidence inspected

All 11 pull-request workflows returned success on the reviewed head. The first unified workflow attempt timed out waiting for an exploration-context browser download after 19 checks. Its retry passed on the same source commit. The earlier candidate's historical browser-blob failure is superseded by the reviewed append-only provenance correction. [Optical workflow and v29 real-Chrome step](https://github.com/physicsvigilante/opticsim/actions/runs/44850100381/job/136679156163) · [Unified workflow retry](https://github.com/physicsvigilante/opticsim/actions/runs/44850100321/attempts/2)

I independently downloaded both CI evidence ZIPs and verified their full SHA-256 digests. The six public CLI files matched the independently generated files byte for byte. All 25 study manifest digests validated, and 24 members matched my local run byte for byte. The remaining member was the timing-dependent test log. CI recorded seven browser checks, two screenshots and Chrome for Testing 158.0.8127.36.

| Workflow artifact | SHA-256 |
| --- | --- |
| [Public authoring evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44850100381/artifacts/14684668935) | `db14901a8071c752205a1518014d237ee9f7773f06de2391ea90ec733940b23d` |
| [Study and browser evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44850100381/artifacts/14684538274) | `5c7f79a5a8637fd6b48b9e88f1b51b558d9778c8b67766adf0e68b6d7cb58565` |

This clearance applies to sampled 2D observations under the declared model. Continuous escape fractions, a three-dimensional solid angle, interpretation accuracy, and independent classroom outcomes remain outside the demonstrated result. The owner retains the merge decision.
