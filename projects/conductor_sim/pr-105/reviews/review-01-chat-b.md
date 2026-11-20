# Independent review #01 — conductor_sim M40c PR #105

**VERDICT: PASS — tightly scoped to exact candidate source. NOT MERGE AUTHORIZATION.**

Reviewer-owned science/browser probes, hosted real workflow and evidence. No changes to production, previous source audits or original workbook files.

## Exact source identity, ancestry and final CI

- Production PR: https://github.com/physicsvigilante/conductor_sim/pull/105
- Exact reviewed HEAD: **33a1c677fd9c68404fc64b44496c08fb2c3cee7b**
- Actual native Git TREE: **02688024e08f8f0726b5399233e50daa0744c855**, independently checked both via git rev-parse HEAD^{tree} and git write-tree after checkout.
- Live PR was rechecked after independent execution: unchanged HEAD, base **337001f2e0d1ce62c87fa4352993c4a074cfbde6**, **DRAFT / OPEN / UNMERGED**.
- Historical audited main, frozen charter commit **5fb0294ac8a1317d61524d1b0a9ba63edf66a354** and ancestry-preserving integration commit **d3e77511ab1920393eb457da39561c0849926a7e** passed native ancestry tests. Original charter blob matched the separate charter-first commit; both original PDFs passed declared SHA256 validations.
- Actual git diff from audited main contains exactly the nine declared **new** M40c files and **no edits to released M39a/M40a/M40b physics/viewer, FEMM, old Chromium, PDFs or old evidence**.
- GitHub returned **32/32 complete successful exact-head workflow runs** (30 pull_request plus 2 push), and independently returned **51/51 completed successful exact-head check runs**. This includes complete Python 3.10/3.12, actual FEMM, original and new actual Chromium, dedicated M40c push and PR workflows (three successful jobs each). The formerly pending full CI gate is now verified, not inferred.

## New independent physical experiment

Original reviewer Python probe: [review-01-chat-b-probes.py](review-01-chat-b-probes.py).

Constructed a genuinely new **translated, nonconcentric four-cavity, six-source** physical assembly: outer sphere center (13.2, −8.1, 4.7) m, radius 9 m. Cases include a signed-neutral nonempty cavity, net-negative cavity, actually empty cavity and net-positive cavity with a centered source. The first two have overlapping **XY** projected circles (center XY separation approximately 0.474 m) but remain **disjoint in 3D** (center separation approximately 2.251 m, combined radii 1.8 m). One existing source **P_oblique** is relocated within its original neutral cavity, with oblique nonzero-Z coordinates and close but qualified wall clearance.

The reviewer separately calculated real and exterior-Kelvin-image normal electric fields at true 3D spherical boundaries using **mpmath at 125 decimal digits**, not the production comparison kernel. For six new raw signed oblique physical rays × four faces × two separately authored **isolated and grounded** constraints, all **48 face/ray/constraint cases** independently verified both before and after signed sigma against the reference with strict relative tolerance **5e-11** for nonzero values and exact zero for empty faces. Sign, Gauss face totals, unchanged unmoved cavity point-sigma, unchanged isolated uniform outer sigma, zero grounded outer sigma, original source IDs, charge/positions/order and baseline immutability passed.

The original high-sensitivity raw near-unit ray was preserved. Independent substitution of its binary64-rounded display normal would change the near-wall physical result by relative **1.968976567845377e-09** — materially above the 5e-11 comparison threshold. A second reviewer-authored symmetric near-cancellation produced **unresolved_numerical_difference** and a null numeric difference, not a misleading physically exact zero.

All **40/40 adversarial refusal cases passed**: wrong/unknown/no-op ownership, bool/nonfinite source/coordinates, wall contact, overlapping voids; forged original or revised XYZ and source IDs/charges/signs; altered cavity centers/radii, Gauss totals/outer SI, original raw ray or display-only normal, local sigma/delta/status, Boolean-as-zero; forged source role/time/force/field/current/workbook claims; deleted, duplicated and reordered late empty/charged face rows or inner/outer witnesses. The independent checker rejected altered records on declared type/physical consistency grounds.

## Actual reviewer-authored offline Chromium

**Four real Playwright Chromium modes PASS:** JS on and off × 1280 px desktop and 390 px mobile. HTML was built from the new reviewer-authored model, not the developer's original example. Independently inspected both SVG panels, **all four cavity circles and six source markers in each panel**, their exact projected centers/radii, one common metre scale, all actual original/revised source XYZ, 24 signed before/after/delta sample rows, unique SVG/DOM IDs across panels, Gauss-vs-point-language, static-only notices, narrow-screen table overflow CSS, and absence of external network requests and page errors. Four real screenshots and per-mode browser/console/network observations were archived.

Actual inline-script injection was **blocked by CSP**. An important *documented trust limitation* was demonstrated: deliberately modified HTML can show a false new position, and injected inline CSS (allowed by style-src unsafe-inline) can **hide the truthful static/nonchronology notice**, while the untouched detached scientific JSON passes its internally consistent checker. Neither JSON nor separate HTML bytes have cryptographic historic teacher-origin authentication. This is within the explicitly stated security boundary, **not an unreported pass-through integrity certification**.

## Source-pinned reviewer execution and first evidence

- Reviewer-owned draft PR: https://github.com/physicsvigilante/review_sandbox/pull/28
- **Actual first reviewer workflow run (PASS, attempt 1):** https://github.com/physicsvigilante/review_sandbox/actions/runs/44676890465
- **19-file, genuine first-attempt evidence artifact:** https://github.com/physicsvigilante/review_sandbox/actions/runs/44676890465/artifacts/14602956141
- Run summary: physical_probes=48, adversarial_rejections=40, browser_modes=4, oracle_dps=125, raw_vs_display_relative_error=1.968976567845377e-09, CSS truth-hiding possible=true.
- Evidence archive contains reviewer script digest, real novel physical JSON, individual numerical oracle records, comparison HTML, four screenshots, JS injection/CSS/altered-HTML exemplars, browser console/network data in the JSON summary, real stdout log, native HEAD/TREE, PDF/charter hashes and actual file allowlist. Hosted upload succeeded.
- No actual failed first CI run occurred. Before creating the first executable reviewer workflow, two reviewer-script authoring mistakes (an unused malformed scratch-ray expression and eagerly constructed invalid-input cases) were corrected in the reviewer branch; both commits remain visible. They were **not** executed as CI, not hidden runtime failures, and not production defects.

## Verdict limits and next gate

**PASS for the exact reviewed production HEAD/TREE and the narrow M40c static source-reposition/comparison/HTML truth contract.** No reproduced scientific, source identity, Gauss, numerical delta, verifier or real rendered two-panel geometry blocker.

This review does **not** certify arbitrary 3D electric fields/potentials, irregular cavities, forces/energy/current, trajectories, scanned-source JEE solutions, FEMM 3D, historical teacher authenticity or hostile post-export HTML bytes. Historical M40a spherical Kelvin and M40b foundational audits were retained rather than needlessly repeated.

**Do not merge automatically.** Separate explicit owner approval is required; protect any subsequent merge by expected production HEAD, verify the reviewed Git TREE on main, and confirm fully successful *actual postmerge main-push* checks. Any changed production source HEAD/TREE invalidates this scoped review and requires targeted requalification.
