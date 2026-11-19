# Independent review #01 — conductor_sim PR #98, M39b topology-only viewer

**Verdict: CHANGES REQUESTED — INDEPENDENT BROWSER EVIDENCE INCOMPLETE. No production source defect was established by the completed checks.**

This verdict is an **evidence-gate blocker**, not a claim that M39b's physics or native renderer failed. The reviewer environment's managed Chromium policy prevents all navigation to local HTML files, including this reviewer's newly generated six-cavity page. Therefore no *independently captured* actual rendered DOM/computed-style/mobile/screenshot evidence exists, and the author's passing browser CI cannot replace it. No PASS or production merge is warranted yet.

## Immutable identity, scope and CI

- Production: https://github.com/physicsvigilante/conductor_sim/pull/98 — checked twice and still **open, DRAFT, unmerged**.
- Literal PR HEAD: **965da98b5079829bd39a370cc660c97b1b9b189f**. Native Git tree verified via GitHub's commit-tree API: **cb9f9822252f982d5691493b7d54b0fae5917049**. Because the reviewer container cannot reach GitHub by git transport, a full checkout and local git rev-parse commands were **not** executed. GitHub metadata, direct source-file hashes and scoped local execution were used instead.
- Released M39a base: edb428ab6574d7861d28a80fcc15309883420448. Remote compare: **7 commits; exactly 8 additions, 0 modifications/deletions**. Therefore existing PDFs, historical physics, FEMM and legacy browser source have zero changes in this PR. No unrelated history was retested.
- At exact HEAD: **24/24** GitHub workflow runs report completed/success (22 pull_request plus 2 push), including historical Python/FEMM/visualization checks.
- Preserved developer first failure: https://github.com/physicsvigilante/conductor_sim/actions/runs/44500155488 at older SHA 0f76def36d0f13a9e359ec21ef3bcda462296ac5 — both Python 3.10 and 3.12 jobs reported **114 passed, 1 failed**, test_smallest_subnormal_is_not_misrepresented_as_visual_zero expected an outer-charge TD without class="charge", which the actual renderer included; first-run Chromium succeeded. Corrected exact-HEAD run https://github.com/physicsvigilante/conductor_sim/actions/runs/44500507965 passed three focused jobs. **Developer CI is preflight, not this review's browser evidence.**
- Executed source modules matched GitHub native blob hashes **byte-for-byte** using git hash-object:
  - src/conductor_sim/cavity_gauss.py: 90ac7bbff6036eca7e0657a594b46d35ca8dcb91
  - src/conductor_sim/cavity_topology_viewer.py: f089969fe5a3ee9eb53429fab9ed9818dcb28d47
  - tools/m39a_gauss_reference.py: 031553923b1b88b6f6cf9520bd1de7c193406985
  - tools/m39b_topology_reference.py: 151f75f9a516e30efcd8e1ff7771896166cdd9d6

For this scoped execution, only unrelated model.FixedNetCharge, model.Grounded, solver.UnsupportedProblem dependencies were supplied using minimal behavior-compatible shims, instead of running a full repository installation. That limits conclusions about the unexecuted package. The four modules named above were unmodified byte-for-byte source.

## Reviewer-created unfamiliar teacher case

One connected metal **ReviewerMetal_R6**, six cavities, nine unique source IDs, isolated fixed metal charge **−2.25e-9 C**, permittivity **8.8541878128e-12 F/m**. Same immutable inventory was re-solved under a separate genuine Grounded() constraint.

| Teacher cavity | Source IDs and signed Coulombs | Enclosed q (nC) | Complete inner face Q (nC) |
|---|---|---:|---:|
| Alpha_Mixed | A_positive +4e-9; A_negative −1e-9 | +3 | −3 |
| Beta_TrulyEmpty | truly no source | 0 | 0 |
| Gamma_NetZero | C_plus +2.5e-9; C_minus −2.5e-9 | 0 | 0 |
| Delta_MixedNegative | D_minus −7e-9; D_plus +0.5e-9 | −6.5 | +6.5 |
| Epsilon_Single | E_solo +1.25e-9 | +1.25 | −1.25 |
| Zeta_LongLabel | Zeta_signed_teacher_source_with_stable_ID_2026_11_19 +4.25e-9; Zeta_subtract −0.75e-9 | +3.5 | −3.5 |

The long source ID has 52 valid characters. Table values above are rounded in nC solely for readability. The exact native HTML uses correctly signed round-trip-safe SI repr, preserving the underlying binary64 input and results.

Using reviewer-authored Fraction.from_float binary64 arithmetic **independently of production math.fsum**:

- Total enclosed source: **+1.2500000000000004e-09 C**, rounded +1.25 nC.
- Isolated whole-metal charge: **−2.25e-9 C**; exterior entire-face charge **−9.999999999999994e-10 C**; exterior Gauss flux **−112.94090673730184 V·m**.
- Grounded equilibrium metal: **−1.2500000000000004e-09 C**, entire exterior face **0 C**, exterior flux **0 V·m**; E(exterior)=0 is stated only under its qualified grounded no-exterior-source boundary.
- Each cavity's entire inner face has precisely opposite *net integral* charge to its declared enclosed sources. Empty cavity and nonempty neutral cavity remain explicitly different; neither implies local sigma(x)=0.
- Genuine topology_view_manifest and render_cavity_topology ran on this original six-cavity pair; independent check_gauss_record for each state and check_topology_view_manifest for the envelope accepted it. Canonical HTML regenerated identically. dataclasses.replace did not mutate the source parent.
- Still **teacher hypothetical**, *not actual cavity shape or source position*. Local E(x), V(x), sigma(x), force, current and original workbook p11/p70 geometry-dependent questions remain **unsupported**. Newly solved original JEE problems: **0**.

## Executed independent adversarial checks

**102 checks passed: 39 positive assertions + 63 expected refusals** on this unfamiliar model and additional extreme-value cases. Representative genuinely executed comparisons:

- Paired native rejection of cavity-name swap with equal neutral totals, two distinct source-ID swap, moved charge to different cavity, epsilon change, charge-sign change, metal-ID change, two isolated/two grounded ledgers, forged cached inner/outer totals and Boolean False as a zero.
- Standalone JSON rejection of false teacher/source provenance, original count (including Boolean false), missing/renamed sources, wrong SI unit, forged inner-face sign/zero, outer charge/flux, false grounded exterior theorem, invented local shape/time/current, and extra geometry fields.
- Smallest positive binary64 subnormal +5e-324 C and its negative induced inner face remained visibly distinct **in generated HTML source** from genuine 0 C; native solver and independent SI oracle accepted it. Nonzero exterior flux underflow refused. Large +1e20/−1e20 signed cancellation preserved +0.75 C aggregate and +0.5 C isolated outer charge.
- Sixteen novel **static canonical HTML** forgery inputs (visible face sign, Boolean zero, SI outer unit, flux, false original-count/role, pseudo-elements, opacity, visibility, clipped text, offscreen transformation, transparency, text stroke, fake wire current/physical shape, remote stylesheet) all differed from native canonical HTML and were rejected by a byte-exact reproduction check. **These are NOT independently verified browser-visible tamper rejections.**
- No script, external URL, remote asset, fake 3D E/sigma picture, or use of old Kelvin/concentric source physics appeared in the generated native topology HTML. Real browser network-request assertion could not run.
- Native methods for local E(x), V(x), sigma(x), force and ground-wire current refused their unsupported use.

## Independent Chromium first-attempt evidence — BLOCKED

Installed Chromium **144.0.7559.96** launched in Playwright. On the real reviewer-generated offline HTML file, page.goto gave:

    JS ON  / 1280×900: net::ERR_BLOCKED_BY_ADMINISTRATOR
    JS ON  / 375×900:  net::ERR_BLOCKED_BY_ADMINISTRATOR
    JS OFF / 1280×900: net::ERR_BLOCKED_BY_ADMINISTRATOR
    JS OFF / 375×900:  net::ERR_BLOCKED_BY_ADMINISTRATOR

The managed browser configuration at /etc/chromium/policies/managed/000_policy_merge.json includes URLBlocklist ["*"]. This restriction was inspected read-only and not bypassed. **Screenshots, browser DOM text, computed CSS/visibility, viewport clipping, horizontal table scrolling, browser network request checks and hostile browser-visible modifications: NOT RUN.**

## Required resolution / release control

**CHANGES REQUESTED for missing independent evidence; no source code change is demanded on the basis of these completed tests.** Rerun the exact newly authored six-cavity HTML in a permitted headless Chromium environment, JS enabled and disabled at 1280×900 and 375×900. Assert *actually visible* source IDs/charges, empty-vs-neutral, induced complete-face sums, both static states, metal charge, outer flux, grounded-only theorem, provenance, warning and zero original count; inspect computed styling, clipping, mobile horizontal scrolling, network absence and actual malicious CSS/HTML overlays/hiding/sign/count/units. Retain first-attempt logs, real screenshots and computed DOM/CSS evidence. Reconfirm exact SHA/tree/CI before any subsequent PASS.

**No production modification or merge is authorized. PR #98 stays DRAFT/UNMERGED pending independent PASS, a separate explicit owner approval, guarded merge and post-merge CI.**

Additional raw reviewer-authored source, six-cavity manifest/HTML, 102-check JSON, attack HTML and blocked-browser logs are retained in the accompanying conversation evidence ZIP; this GitHub report does not falsely claim independent screenshots.