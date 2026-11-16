# EM Fields PR #17 — final approved merge and post-merge release qualification

**Final disposition: MERGED WITH EXPLICIT OWNER APPROVAL; FRESH POST-MERGE CI PASSED ON BOTH OSs (2026-11-16 UTC).** This is a new release report; the original source qualification evidence, independently authored review and first failures remain unchanged.

## Source identity and merge authorization

- Source: [physicsvigilante/emfeeld PR #17](https://github.com/physicsvigilante/emfeeld/pull/17), closed/merged following distinct owner approval given **after** the independent R2 report and Chat A triage. Approval covered the exact source PR #17 head, not unrelated milestones.
- Parent pre-merge main/base: **8fe6331aefa252585b3b90f54b8ee7cbbac5e605** (qualified PR #14).
- Frozen, independently reviewed and owner-approved head: **62121252c6526c53c29440dcd8f41b6109f70e04**.
- Merged-main commit: **1b7d5c652bb635723746b3c6ce77baee536b997e** — [view merge](https://github.com/physicsvigilante/emfeeld/commit/1b7d5c652bb635723746b3c6ce77baee536b997e). Merge parents are the exact base and approved head above.
- **Exact canonical Git tree: 339224f69e5c671dea83678cdb00845887ce27b4**, identical at the approved head, pre-merge CI merge-preview (6d1c219e67cf300df7044f24690edf779270ac8f) and final merged main. No additional source variation was introduced.
- Scope: one bounded proposal-version-3 atomic scenario transaction, 2–4 distinct target entities, exact pinned parent, one immutable accepted descendant after final-snapshot validation, retained failed attempts and explicit computed-dependency and identity guards. The change does **not** add field laws, particle-particle coupling, source backreaction, a new integrator or viewer, crash-safe ACID semantics or time-dependent physical changes.

## Original separate-context independent R2 review preserved

- Original [Chat B review 01](reviews/review-01-chat-b.md): **scoped PASS** at the exact source head/tree; no demonstrated blocker/major source defect. Original Git blob **5f6ecd63e2f0dc5df51abb1db355a5cb976c8755** remains unedited. Independent-context reviewer reports 199 rerun relevant tests, 14 reviewer-authored adversarial groups (including eight two-process local-writer trials), independently written physical calculations and direct Linux/Windows evidence audits. This is not independent human physics certification.
- [Chat A response 01](responses/response-01-chat-a.md) separately triages nonblocking F-01–F-04: controlled interrupted-reference write/incomplete-history refusal, LF/CRLF raw source hash differences despite identical canonical Git tree, bounded physics/evidence meaning, and retained first failing CI attempts. Neither report licenses distributed/crash-recovery claims or edits prior evidence.
- No post-review source correction was required. The source remained frozen through owner authorization and merge.

## Qualified pre-merge evidence

- [Linux/Windows clean-install workflow 43751887519](https://github.com/physicsvigilante/emfeeld/actions/runs/43751887519) and [separate real-PyVista workflow 43751887558](https://github.com/physicsvigilante/emfeeld/actions/runs/43751887558): **SUCCESS** at exact reviewed head.
- The pre-merge author E1/G1/T1 checker compared 36 authored static field/potential probes and seven full trajectories with separately implemented ideal-source expressions and RK4; these are same-author transfer references, not an independent Chat B verdict. The original failed attempts remain in source PR #17 and its retained workflow history.

## Fresh merged-main CI — passed, exact merge commit

- [Full Linux+Windows clean-install workflow #43820500320](https://github.com/physicsvigilante/emfeeld/actions/runs/43820500320): **completed SUCCESS** on Ubuntu 24.04 and Windows 2022, checking out exact merged-main commit **1b7d5c652bb635723746b3c6ce77baee536b997e**. Every job step including static/trajectory/atomic-native reference checks completed successfully.
- **Per OS:** **1,342 headless + 18 historical behavioral + 33 real-PyVista = 1,393 tests by suite membership**. The unchanged obsolete historical whole-file freeze guard remains explicitly deselected. The 34 focused atomic tests are separately rerun but already included among the 1,342 headless definitions; running the same test definitions on two OSs does not create 2,786 distinct tests.
- [Separate merged-main real-PyVista workflow #43820500338](https://github.com/physicsvigilante/emfeeld/actions/runs/43820500338): **completed SUCCESS**, including **1,342 cumulative tests** and real offscreen rendering/slider-event checks on the exact merged commit. This is not manual Windows desktop interaction.
- Fresh release ZIPs were downloaded independently of source CI. For **each archive**, original compressed file SHA256 matched GitHub's published artifact digest, its **1,629 ZIP entries passed CRC with no duplicate names**, saved head-sha.txt was the **exact merge commit**, and the recorded test logs had 1,342 headless, 33 real-PyVista and 34 focused atomic passes.

| Platform | GitHub release artifact ID | Independently rehashed original ZIP SHA-256 |
|---|---|---|
| Ubuntu 24.04 | **14204053864** | **938443ff04644297fb0fc693ea725c1a5c510929ad3c1e2d9d8e565c2a4b5a9f** |
| Windows 2022 | **14204677732** | **c87679f4df03d51456319b668789f9d8f1434911a6a81e672bdfe051bcc90a2b** |

- Separate merged-main viewer artifact: ID **14204960213**, GitHub-reported SHA-256 **0277d953566436aa825c09700b55eb370c2d430aebb37bc7e009491865852f40**. Its workflow was green; unlike the two release ZIPs, this additional artifact was not separately downloaded and CRC-audited here.

## Read-only saved atomic E1/G1/T1 audit on both OSs

- Each release ZIP contains native atomic qualification status **complete** and separate same-author reference checker status **passed**, with **36 static field/potential instances** and **seven checked trajectories**. The same three authored arrangements are E1 electric line replacement, G1 changed gravitational source plus new independent body and T1 static electric shell/point charge edits. No unsupported motion was claimed for T1.
- **Each OS:** **three accepted single-descendant atomic revisions**, **six complete native baseline/final runs**, and **one deliberately rejected E1 old-presentation request**. Every case's qualification record declared baseline preservation. No old physical source entity, test-particle identity or saved run was silently retargeted.
- A separate **read-only Python/zipfile audit of the original ZIP bytes**, without altering source or saved runs, verified **seven top-level sealed run file inventories**, **six nested native file inventories**, all seven run input SHA-256 bindings and run/revision exact-reference SHA-256 checks per OS. All passed; the deliberately rejected attempt was checked for its recorded status rather than mistaken for a numerical failure.
- Checks were against the saved, same-author reference results; this audit does not constitute new, independently authored physics reference calculations. The separate Chat B report includes its own earlier independent analytic/RK4 work on the exact source head.

## Final disposition and retained scope limits

**PR #17 is fully integrated and post-merge qualified for its bounded reviewed regime.** No blocking defect was observed in fresh merged-main CI or the audited post-merge release artifacts. The exact reviewed Git source tree is preserved. Original Chat B text, Chat A responses, early failed CI attempts, historical native runs and old model roots remain untouched.

Atomicity means one validated *physical descendant* is accepted only after whole-candidate validation; the local filesystem store and writer lock are **not** authenticated, hostile-writer-safe, distributed or crash-proof ACID. A partial interrupted publication may reserve an ID and require inspection. Linux/Windows offscreen PyVista does not establish manual Windows desktop mouse behavior. Separate-chat GPT-6 review is not independent human certification; classroom usefulness, source-interpretation fidelity on unseen problems and textbook-answer completeness were not assessed. Prescribed field sources and independent nonrelativistic test bodies remain the only qualified dynamics; no collision, conductor response, shell/plane motion, source feedback or multi-domain coupling was added.

The GitHub merge and CI did not install packages on the user's local Conda computer or modify the user's saved physical model stores. Teaching evaluation remains paused. Future capabilities require a separate scoped design, risk classification, CI, independent-context review where appropriate and distinct owner merge authorization.
