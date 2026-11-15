# <project> PR #<number>: review request

- projectId:
- sourceRepo: `owner/repo`
- sourcePR: https://github.com/owner/repo/pull/...
- baseSha: **40-character SHA**
- headSha: **40-character SHA**
- sourceTreeSha:
- reviewClass: R0 / R1 / R2
- scope: new capability / specific correction / other
- known limitations:
- current CI runs and artifact names + SHA-256:
- files and contracts to inspect:
- preserved previous reviews, if any:
- review report destination: `projects/<project>/pr-<number>/reviews/review-01-chat-b.md`

## Expected source-backed behavior

Describe physical input, output qualification, completion, refutation cases and strict non-goals. Never substitute invented facts.

## Reviewer acceptance questions

Identify concrete failure modes that are valuable to test, not a desired verdict. For R2, include independent numerical/geometry references and native implementation boundaries. Disclose which cases have not yet been run.

## Status

Report `awaiting-review`, `changes-requested`, `insufficient-evidence`, `pass`, or `superseded-by-new-head`. These are review states, **not production merge authorizations**.
