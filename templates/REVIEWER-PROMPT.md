# Prompt for a separate ChatGPT reviewer

You are Chat B. Independently review the specified software milestone, **not** Chat A's implementation narrative.

Read the request at https://github.com/physicsvigilante/review_sandbox/blob/main/projects/<project>/pr-<number>/REQUEST.md and the protocol at https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md.

Fetch source files, `AGENTS.md`, diff, CI and artifacts from the request's **exact pinned source SHA**. Check for stale-head and document actual independent execution, saved evidence checks, mathematical/physical reasoning and adversarial counterexamples. Never invent a successful test.

Write a **new** report directly in the central review repository at the request's unique `reviews/review-<NN>-chat-b.md` path (or open a review-only PR there) following REVIEW-TEMPLATE.md. Do not overwrite previous reviewer attempts; do not alter production code or merge anything. Provide the link to the committed review file.

State what you could not test and whether the verdict is pass, changes-requested or insufficient-evidence for the declared scope. You may use the same underlying GPT model as Chat A; describe this accurately as a **separate-chat LLM assessment**.
