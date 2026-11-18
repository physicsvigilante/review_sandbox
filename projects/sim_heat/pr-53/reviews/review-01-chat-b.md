# SIM_HEAT PR #53 — Chat B independent focused review 01

**Outcome: SCOPED PASS (R1).** The six-file change is a bounded navigation/evidence-presentation increment. No blocker, major defect, physical-contract alteration, result promotion, or provenance-semantics change was demonstrated. Two **minor** documentation/navigation follow-ups are recorded below; neither establishes a failed solver, a false native reading, or a release qualification.

## Identity and review boundaries

- **Project / source:** [physicsvigilante/sim_heat](https://github.com/physicsvigilante/sim_heat), [draft PR #53](https://github.com/physicsvigilante/sim_heat/pull/53).
- **Exactly reviewed head:** `86c8c146ec025ca62a4484a7e20eb76b5530f29d`.
- **Reviewed tree:** `c73f86e58be8b9eb55756432aae064f00719487f`.
- **Base (merged main):** `4162c3d47016150076b226ebe2585073a785547a`, tree `2ad10a1679d528f88030494f0349171502ef8e0f`.
- **Pinned diff:** [commit 86c8c146](https://github.com/physicsvigilante/sim_heat/commit/86c8c146ec025ca62a4484a7e20eb76b5530f29d). One parent is exactly the stated base; exactly six paths changed: `.github/workflows/product-entry-ci.yml`, `README.md`, `docs/CAPABILITIES.md`, `index.html`, `tests/browser_product_entry.py`, `tests/test_product_entry.py`. Five additions and one README modification.
- **Reviewer:** Chat B, GPT-6, separate ChatGPT conversation (independent context, not human specialist certification or proven different underlying model).
- **Date:** 2026-11-18.
- **Scope:** R1 independent review of start-page UX, capability/evidence statements, links/keyboard/mobile behavior, navigation regression checks, protected-source preservation and exact-head CI. Not another H1 numerical/physics audit.
- **Source files altered by this reviewer:** **None**. No change to the source PR, historical evidence or frozen references; this is a new report in `review_sandbox`.

## Findings

### F-01 — Minor / registry navigation coverage; **no confirmed broken route**

**Source:** [index.html:45](https://github.com/physicsvigilante/sim_heat/blob/86c8c146ec025ca62a4484a7e20eb76b5530f29d/index.html#L45); [tests/browser_product_entry.py:55-58](https://github.com/physicsvigilante/sim_heat/blob/86c8c146ec025ca62a4484a7e20eb76b5530f29d/tests/browser_product_entry.py#L55-L58).

**Observed in source:** The teacher-facing registry link targets `docs/CAPABILITIES.md`, and the hosted browser smoke calls `page.request.get(...)` and checks the response body; it **does not navigate the page into the registry or check that its Markdown tables and source links are rendered and clickable**. The local-server instructions use Python `http.server`, without a Markdown-to-HTML renderer. The source Markdown itself is readable and its relative targets resolve, so this is a coverage/UX uncertainty, not an established 404 or incorrect evidence statement. The independent environment blocked all Chromium network navigations (`net::ERR_BLOCKED_BY_ADMINISTRATOR`), preventing a firsthand browser assessment of this link.

**Expected for a polished browser-first registry:** A user can open and navigate the registry's source references without needing to interpret raw Markdown. **Suggested follow-up:** explicitly choose whether raw Markdown is intended; if not, offer a static HTML rendering of the registry and add a browser click/readability/link smoke. Not a blocker for the present bounded R1 increment.

### F-02 — Minor / historical contract label can confuse new authors

**Source:** [index.html:54](https://github.com/physicsvigilante/sim_heat/blob/86c8c146ec025ca62a4484a7e20eb76b5530f29d/index.html#L54); [docs/CAPABILITIES.md:19](https://github.com/physicsvigilante/sim_heat/blob/86c8c146ec025ca62a4484a7e20eb76b5530f29d/docs/CAPABILITIES.md#L19); [existing H1 contract:8](https://github.com/physicsvigilante/sim_heat/blob/86c8c146ec025ca62a4484a7e20eb76b5530f29d/docs/H1_IMPLEMENTATION_CONTRACT.md#L8).

The new entry point recommends the “H1 authoring contract” as an authoring starting point, while the existing linked document still labels itself a **local proposed contract not published, adopted or implemented**. This older header is historical; it does **not** overturn the implemented restricted authoring paths evidenced elsewhere. However, a reader arriving from the new “current capabilities” page can reasonably misread the lifecycle status. **Suggested follow-up:** label this link a historical/foundation design contract or point to clearly current authoring instructions. No physical behavior or original evidence is changed.

**No demonstrated code defect** in the new start page or six published case identities. No R2 escalation is justified by the inspected diff.

## Personally executed independent checks (Chat B)

1. **Pinned source/structure:** Read the six modified/additional files, the source `AGENTS.md`, H1 documents, dated audit, original C1 freeze and viewer guide. Git commit/tree APIs independently showed the exact parent, tree and six-path diff. Compared base/head Git subtree SHA-1s: `h1` = `124919a7b42547017dd974840505e42fa4d68df5`; `experiments` = `522ca2a4c6e757aaeca3724e9305836a5908e890`; `qualification` = `9409d5c2d31c1bd83d2dd2cf6ba64ed0730471d9`; `viewer` = `e767a05ff63a7374206604df578bd88f54a23c3d`. Each matches the exact base. Original model/engine, result archives, viewer and C1 paths are untouched.
2. **Links and factual registry:** Independently parsed the start page and registry links and fetched all **18 distinct local target files at the pinned source SHA** via GitHub; **18/18 resolved**. Checked the `#main` anchor is present/focusable. Independently read all six published case JSON sources and confirmed `publicRequestStatus=diagnostic_only`, `nativeQualified=false` and `evidenceKind=historical_native_diagnostic` in each. Catalog IDs agree with the registry rows. The registry keeps archived native readings, separate analytical calculations, and C1 source-only/uncomputed expectations distinct. S1 is described as steady, not transient; Ring4 remains developer-authored and D2_K2's input revision is explicitly hypothetical.
3. **Artifact re-inspection:** Downloaded both exact run-44238734097 ZIPs and independently hashed their bytes, validated CRCs/no duplicate ZIP member names, read their checkout/diff receipts, logs, replay JSON and comparison output:
   - Candidate artifact **14398477224**: **6,454,848 bytes**, SHA-256 `6e8ce7d23eda335e12083d60098974953d3f212a38a746897a2e5e023f573347`, **38** distinct CRC-valid entries including **23 PNGs**. Internal head/tree `86c8c146…` / `c73f86e5…`; its source diff is exactly six paths.
   - Baseline artifact **14398721933**: **5,873,775 bytes**, SHA-256 `27fc39b8971cc7525ae5cf2e97750c68a37d468435d91291cfd2738f0c15b0cd`, **33** distinct CRC-valid entries including **21 PNGs**. Internal head/tree **`4162c3d47016150076b226ebe2585073a785547a` / `2ad10a1679d528f88030494f0349171502ef8e0f`**, and **empty source diff**. I separately inspected GitHub job logs showing an actual checkout of main4162, not merely an artifact name. The baseline artifact's name carries the **candidate event SHA**; its own checkout receipt is decisive.
   - Both `archive-replay.json` files are byte-identical, with six `BYTE_IDENTICAL` records and `nativeExecutedByReplay=false`; the replay preview hashes match the unchanged catalog. Both `compare-replayed.json` outputs are also byte-identical. This is evidence-preserving replay, **not a fresh native execution**.
4. **Independent Chromium static-page probe:** Reconstructed the exact pinned `index.html` locally and checked its SHA-256 `b06a77b83e507d189b07f658dcad1ab2664dfb23f93ad0b098d44767e1bf64bc` against the candidate artifact's `entry-sources.sha256`; **matched**. Personally ran Playwright/Chromium `page.set_content` on this exact HTML at **320×720, 390×844, 768×900 and 1440×1000**. All four widths had zero horizontal overflow, three visible evidence cards with 1-column mobile / 3-column desktop layout, no scripts/frames/forms, no JS page errors, and focus sequence **skip-link → main → enter-explorer** after Tab, Enter, Tab; focus outline appeared. This check did **not** load target HTTP routes.
5. **Visual inspection:** Personally opened the candidate CI's actual **1440 px desktop** and **390 px mobile** full-page screenshots. Content and status distinctions remain visible, mobile buttons/cards stack without apparent clipping, and there is no obvious layout overlap.

**Execution limitations:** My independent attempts to navigate even a small localhost page with Chromium were blocked by the current environment's network policy (`net::ERR_BLOCKED_BY_ADMINISTRATOR`); a separate Git clone also failed DNS resolution. I did **not** independently rerun the complete source repository's unit tests, the actual HTTP navigation, the full existing explorer smoke, original archive replay script, or any OpenModelica/native runner. Hosted tests below must not be misreported as my local executions.

## Inspected hosted CI evidence (not personally executed suites)

[Run **44238734097**, push event, attempt 1](https://github.com/physicsvigilante/sim_heat/actions/runs/44238734097): event HEAD `86c8c146ec025ca62a4484a7e20eb76b5530f29d`, completed **success**. I examined GitHub run/job metadata, both checkout job logs and the downloaded artifacts rather than relying on the PR summary.

| Job | **Actual source checkout** | Evidence read in logs/artifact |
|---|---|---|
| Candidate **134581099995** | `86c8c146ec025ca62a4484a7e20eb76b5530f29d` | **257 passes, one optional unittest skip**: H1 152, analytical arithmetic 4, adapter 62 pass/1 skip, Node 31, entry 8. Original six-archive replay and saved comparison unchanged; existing explorer browser smoke **PASS**; new real-localhost desktop/mobile keyboard, six-case explorer, ready comparison and registry HTTP smoke **PASS**. |
| Postmerge baseline **134581100335** | `4162c3d47016150076b226ebe2585073a785547a` | **249 passes, one optional unittest skip**: H1 152, arithmetic 4, adapter 62 pass/1 skip, Node 31; six-archive replay, comparison and existing browser smoke **PASS**. New navigation CI step intentionally **skipped** because its files are absent on main4162. |

The 249 baseline passes overlap the candidate's inherited 249; **do not sum the jobs' test totals**. The optional skipped unittest is `test_optional_original_native_archive_and_fully_rehashed_test_only_mutants` (“Original external artifact not supplied”); that is separate from the baseline workflow-step skip. The candidate HTTP log contains a harmless `/favicon.ico` 404; the claimed “no page errors” refers to captured JavaScript page errors, not proof of zero HTTP errors.

Hosted browser smoke tests exercised the existing explorer and comparison routes; I inspected their PASS records and source code. The hosted evidence is credible for the specified paths but does not prove cross-browser accessibility certification, every viewport, teacher use, or independent scientific accuracy.

## Separate scope judgments

| Dimension | Judgment | Basis |
|---|---|---|
| Source-interpretation fidelity | **SCOPED PASS** | Source and registry accurately distinguish six diagnostic outputs, analytical checking data, steady S1 and separate expected-only/uncomputed C1; no new physical input interpretation. |
| Physical / numerical correctness | **UNCHANGED; not independently requalified** | Relevant engine and results subtrees byte-identical by Git tree identity. No new calculation, solver or reference authored; new numerical qualification cannot be inferred. |
| Native simulation / observable coverage | **UNCHANGED / LIMITED** | Historical native diagnostics remain available and `diagnostic_only`; all six replays non-native. C1's nine native readings remain uncomputed; no new OpenModelica operation. |
| Evidence integrity / provenance | **SCOPED PASS** | Exact HEAD/tree, both distinct checkout identities, ZIP hashes, original replay parity, catalog/status flags and six-file diff verified. Not certification of upstream native measurement. |
| Teacher-facing usefulness | **BOUNDED POSITIVE, classroom validation UNKNOWN** | Clear two-route entry, responsive/keyboard behavior and understandable disclaimers. Minor Markdown-rendering/test and contract-label caveats above; no teacher study. |
| Textbook-answer completeness | **N/A** | Not part of this navigation/evidence-presentation change. |

## Recommendation and release boundary

**SCOPED PASS for R1 review of head `86c8c146…` only.** No blocking change or re-review is required on the inspected diff. Track F-01/F-02 as modest teacher-facing polish; if changing links, renderers, source semantics or tests, obtain updated source/head and proportionate CI. Escalate to R2 **only if** a later change alters physical values, admitted source interpretation, qualification status or provenance meanings. This review **does not authorize a source merge, deployment or native execution**. Owner approval and the repository's remaining merge gates remain separate. Preserve PR51/52 reviews, C1 history and original archived artifacts without mutation.
