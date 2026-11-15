# New reviewer report template

Submit this as a **new file authored by Chat B** under `projects/<slug>/pr-<number>/reviews/review-<NN>-chat-b.md`. Do not overwrite the original or copy Chat A's verdict.

- Project / source repo:
- Source PR and base SHA:
- **Exactly reviewed head SHA:**
- Reviewed source tree / diff link:
- Reviewer: Chat B, separate ChatGPT conversation; model if known:
- Date and time:
- Review scope / risk class:
- Were source files changed during the review?
- CI run IDs / actual artifacts inspected:
- **Outcome: pass / changes-requested / insufficient-evidence** (scoped):

## Findings

For each: `F-01`, severity (blocker/major/minor/question), category, source path/lines, independently reproducible inputs, expected versus observed, evidence type, confidence/limitations, proposed regression. Write **no demonstrated code defect** explicitly if that is what evidence supports.

## Tests and independent evidence

State what you ran yourself vs read from Chat A's CI artifacts, independent physical calculations and exact input hashes, outcomes and any test setup failures. Screenshots and browser results are not substitutes for native physics checks. No unperformed test is a pass.

## Separate scope judgments

| Dimension | Pass / Fail / Unknown | Basis |
|---|---|---|
| Source interpretation fidelity | | |
| Physical/numerical correctness | | |
| Native simulation and observable coverage | | |
| Evidence integrity and provenance | | |
| Teacher-facing usefulness | | |
| Textbook-answer completeness (only when relevant) | | |

## Release advice

Report remaining risks, whether further independent review is needed and the smallest next test. **Do not merge production PRs.** A separate-chat LLM review does not prove a different model family or replace independent subject-matter adjudication.
