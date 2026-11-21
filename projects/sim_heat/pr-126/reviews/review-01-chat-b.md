# Independent Chat B review of SIM_HEAT PR 126

**Verdict — accept the offline Windows and Linux replay candidate.** No blocking findings for head `1c8581115b4c229088ce93d2cc671f7334a62231` against base `b16004ff5f84a6d67b24e8681071d969cf83921e`. I served as the independently dispatched Codex reviewer. [Pinned request](https://github.com/physicsvigilante/review_sandbox/blob/84ed1b8481fdb53a890381a0b325e72d2a0c1f6b/projects/sim_heat/pr-126/REQUEST.md) · [Source comparison](https://github.com/physicsvigilante/sim_heat/compare/b16004ff5f84a6d67b24e8681071d969cf83921e...1c8581115b4c229088ce93d2cc671f7334a62231)

## Native paths and portable descriptors

On the pinned Windows checkout I called the loader with a relative native backslash path to D2_K2. It followed the parent revision successfully and returned study SHA-256 `ab3741a80e94b32a8f6d050f34baf9c773763fdd3ed6df71ccdcdbe2214a0d87`. An existing file outside the root and a missing study both produced a controlled path refusal. In a temporary D1 descriptor, I changed only the model path. Both a backslash-relative spelling and a drive-qualified spelling produced path refusals. The portable spelling loaded successfully. The source checks for symbolic links before resolving the caller path, verifies containment, and passes a POSIX-form relative spelling into the existing descriptor path validator.

## Fixture bytes, scratch pins and preservation

I compared 53 checked-out case, generated viewer/document and H1 Python files against their Git blob IDs, with every raw byte comparison passing. The changed scratch fixtures write the UTF-8 bytes used by their digest calculations. The campaign test copies its inputs to a resolved temporary directory and refreshes the additional verification-test pin there. The checked-in campaign and base plans have the same blob IDs as the base revision. Historical identity-refusal tests passed on both hosts.

The complete six-file diff changes the loader, three test files and checkout attributes, and adds one workflow. The original workflows, studies and qualification tree match the base. I separately checked the older H1/qualification baseline against the base with the held-out exception and the held-out subtree against its own frozen commit, obtaining empty diffs. The new workflow checks out the explicit PR head, restricts execution to this branch pair and executes the offline suites.

## Hosted replay archives

I downloaded both archives, computed SHA-256 on the ZIP bytes, verified their CRCs and read every transcript. Both contain only the head record and the two requested transcripts. Both head records match the reviewed SHA. All listed tests finished with individual ok results and both suite summaries reported OK. I compared the test identities between platforms and they match for each suite.

| Platform and archive | ZIP SHA-256 | Product | H1 core |
|---|---|---:|---:|
| [Windows 2022](https://github.com/physicsvigilante/sim_heat/actions/runs/44871668314/artifacts/14693937849) | `106cd8f90e7ef7e25c4db401d1a117d613f30981ba5b8d790436163229b9d9a9` | 147 in 34.079 s | 152 in 8.494 s |
| [Ubuntu 24.04](https://github.com/physicsvigilante/sim_heat/actions/runs/44871668314/artifacts/14694635202) | `45f1d305ae29eec0905118adec08eec52aff6cad6b0c3de015ea58d409aa2e33` | 147 in 22.381 s | 152 in 2.513 s |

The hosted evidence covers offline replay on these two runners. The local checks exercised Windows directly. This verdict grants no new physical or native-solver qualification. The owner controls source merge approval.
