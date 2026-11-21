# Independent Chat B review of SIM_HEAT #172

**Verdict — accept for frozen-input checkout preservation.** I found no blocking issue in the diff from `2ae5fe77b3b9befe609d88f956507501dfa99af4` to `8b1df407721fdc242626ae85acc81490ca8eed8b`. The review packet is pinned at `e3e002f2213312ddf4edd9937e6a30adbe060180`. [Source PR](https://github.com/physicsvigilante/sim_heat/pull/172)

The source diff adds four exact LF attribute rules and a read-only two-platform workflow. No tracked original, hash manifest, physics implementation or test changed. The workflow checks out the PR head SHA, uses commit-pinned actions, hashes the three original inputs and runs offline N4 discovery.

## Independent Windows experiment

I cloned the local source repository into two new temporary directories with checkout disabled, set repository-local `core.autocrlf=true` before the first checkout, and checked out the base and head separately. The first sandboxed clone could not initialize Git's shell. The subsequent authorized clones succeeded. On the base, Git reported working-tree CRLF for all four paths. Python 3.10.6 N4 discovery failed at the original input SHA-256 assertion in class setup and ran zero tests. On the candidate, Git reported working-tree LF on all four paths while neighboring unprotected files had CRLF. All 15 offline N4 tests passed, including mutated-source refusal. The head checkout was clean after testing.

For each of the three author files I matched its raw checkout SHA-256 against `qualification/h1_n1/SOURCE-PINS.json`. I also compared Git blob IDs at the original source commit `7234a53a5022441a912eb09240138e9c6c5945d8` under `experiments/h1_t1_unsealed/T/` and at the reviewed base and head under `qualification/h1_n1/inputs/T/`.

| File | Identical original, base and head blob |
| --- | --- |
| AUTHOR_NOTES.md | `3f1a796b3e222d710c0eb43e554b44bb74329a01` |
| model.mo | `849eaa197a5e8c1a1a2a019f044c2d7e05ade722` |
| study.json | `5af21bc6f80c0b28602edf2c50b91c4022d93d5a` |

For the fourth path, `qualification/h1_n1/reference-facts.json`, the base blob, head blob and unfiltered checkout hash-object result all equaled `fc60b81155f80ea2ccd0b2df2014292aaf872801`.

## Hosted verification and scope

I queried the run and job endpoints. Run `44908020960` and both jobs reported the reviewed head SHA and completed successfully. [Ubuntu job 136857664871](https://github.com/physicsvigilante/sim_heat/actions/runs/44908020960/job/136857664871) and [Windows job 136857665134](https://github.com/physicsvigilante/sim_heat/actions/runs/44908020960/job/136857665134).

This review establishes byte preservation on fresh checkouts. Native operations performed by this reviewer totaled zero. Source integration remains an owner decision.
