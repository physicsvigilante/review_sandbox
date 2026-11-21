# SIM_HEAT #166 independent Chat B review

**Verdict. Accept the R1 direct-script import bootstrap at the pinned head.** The candidate fixes a reproduced base failure and launches a real workbench from an unrelated directory. The normal module entry point retains the behavior observed on the base. The documented nested case layout still fails on Windows with either entry point. This limits any Windows launch claim and warrants a separate correction.

Reviewed base `6ebfc50574a61a49b7e4f645ab82f727af127b30`, head `0485355c9669e8943210b1f6f009e1f0fbe734a1`, and packet `2544e64f05fef8d8e88a79adc273029b8544820d`. The candidate prepends the resolved checkout root only for direct execution. The remaining changes add a help-mode regression and a CI workflow. [Pinned comparison](https://github.com/physicsvigilante/sim_heat/compare/6ebfc50574a61a49b7e4f645ab82f727af127b30...0485355c9669e8943210b1f6f009e1f0fbe734a1)

## Independent launch checks

I ran the direct script with `python -I -B <absolute-script>` from an unrelated temporary directory and the module with `python -B -m tools.authoring_workbench` from its checkout. Both received the absolute S1 descriptor. I repeated base controls using files from a disposable git archive.

| Windows launch | Base | Candidate |
| --- | --- | --- |
| Direct, root at S1 | Missing h1 import | Admitted and served S1 |
| Module, root at S1 | Admitted S1 | Admitted and served S1 |
| Direct, root at h1/cases | Missing h1 import | Exit 2, portable relative path required |
| Module, root at h1/cases | Refused, portable relative path required | Exit 2, same refusal |

Both candidate positive controls served the viewer HTML and JSON over loopback. The payload represented four steady S1 components. The source hashes matched the actual study and model bytes, nativeExecuted and nativeQualified were false, and all request statuses were not_computed. My first positive-control attempt with base Miniconda reached the dependency_missing refusal for NumPy. The paired results above used the NumPy-enabled environment. I stopped the processes after the probes.

## Windows nested-root limitation

The documented command places the trusted root one directory above the case. The inherited loader converts the internally computed relative Path with str(), producing a backslash on Windows. Its portable-input validation then rejects that string before reading the study. The admission file has the same blob on both revisions, `545fad71c467adf300c01ba357d5fc77d7eb85e0`. A separate fix should normalize that internally derived path and exercise actual nested-root admission on Windows while retaining validation for descriptor-supplied paths. [Loader](https://github.com/physicsvigilante/sim_heat/blob/0485355c9669e8943210b1f6f009e1f0fbe734a1/h1/study.py#L122-L129) · [Documented layout](https://github.com/physicsvigilante/sim_heat/blob/0485355c9669e8943210b1f6f009e1f0fbe734a1/docs/LOCAL_AUTHORING_WORKBENCH.md#L6-L12)

## CI

I verified workflow run 44906429999 against the exact candidate SHA. Both jobs passed the isolated help and preview identity tests. Linux also passed full unittest discovery. The workflow skips full discovery on Windows. The Windows help check exits before real admission. This review covers offline entry-point behavior and source preview only. [Linux job](https://github.com/physicsvigilante/sim_heat/actions/runs/44906429999/job/136852892519) · [Windows job](https://github.com/physicsvigilante/sim_heat/actions/runs/44906429999/job/136852892738)
