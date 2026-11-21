# PR #82 targeted independent review of TwinBridge error ratios

**Changes requested for one static-series false acceptance.** At `b96e18a1a988bc323d7bae0eb274a52f4209d4af`, the successor catches the original zero-ratio counterexample and two nonzero understatements. The authentic hosted replay passes. A different sample can cross a binary64 spacing boundary and exceed its reported bound while the standalone successor accepts the series. This affects evidence verification. I found no erroneous value in the authentic replay. [Pinned request](https://github.com/physicsvigilante/review_sandbox/blob/7fce0e811ef8ec4dc398067a130075b3fb40cbeb/projects/sim_heat/pr-82/CORRECTION-REQUEST-02.md)

## Finding 1 · Static-series verification uses the first sample's spacing at later times

The solver's `bounded_centre` divides each static error by `0.64 × ulp(centre)`. The successor precomputes this denominator using `values[0]`. The frozen oracle checks each static sample against a tolerance based on the analytical constant and does not require exact repetition. An accepted value at a later index can therefore have a different ulp. [Solver](https://github.com/physicsvigilante/sim_heat/blob/b96e18a1a988bc323d7bae0eb274a52f4209d4af/qualification/h1_n13/conduction.py#L219-L232) · [Successor](https://github.com/physicsvigilante/sim_heat/blob/b96e18a1a988bc323d7bae0eb274a52f4209d4af/tools/verify_twinbridge.py#L36-L52)

I ran the following probe on a decoded copy of the downloaded fresh output. It also reproduces from the preserved first output.

```python
import gzip, json, math
from fractions import Fraction as F
from qualification.h1_n13.heldout.oracle import HERE
from tools.verify_twinbridge import verify

with gzip.open(HERE / "first-output.json.gz", "rt") as stream:
    data = json.load(stream)
values = data["exports"]["upper.G"]["values"]
values[57] = math.nextafter(2.0, 0.0)
data["maxErrorToBudgetBySeries"]["exports"]["upper.G"] = "1"
actual_ratio = abs(2 - F(values[57])) / (F(64, 100) * F(math.ulp(values[57])))
assert actual_ratio == F(25, 16)
verify(data)  # Returns successfully at the reviewed head.
```

The exact reference is 2 W/K. The modified value is one representable step below 2, with discrepancy and sample ulp both equal to 2⁻⁵² W/K. At unchanged sample zero the ulp is 2⁻⁵¹ W/K. The successor consequently uses twice the proper budget and accepts the reported maximum of 1. Moving precisely the same mutation to sample zero raises the expected error. Both placements passed the frozen oracle's broad check. The workflow's separate comparison to the preserved JSON catches either edit. For the standalone verifier, use the inspected sample's ulp in the static comparison or establish exact static values at every sample before reusing the denominator. Cover the later-sample case with a rejection test.

## Regression, replay and scope

- Git identifies correction parent `7ee5bffb5a251ee75c4dab6ac54aaffccdc59d10` and corrected tree `2ae656dc8fee699d944e4ec4e7e791f749654a9c`. Only the verifier, regression and workflow differ from the parent. I compared the solver/H1 scope to freeze `f05f6a8`, the held-out evidence including controls to `954cf65`, and the five case/oracle inputs to `892e9e4` using Git. All scoped comparisons were empty. I also compared the local verifier, test, solver, oracle, controls, workflow and original gzip to the pinned source blobs, allowing CRLF in text.
- The job log shows seven successful tests, including both new ratio tests. The workflow pipes fresh solver stdout to gzip and invokes `python -B -m tools.verify_twinbridge` on that file before comparing fresh JSON, oracle summary and seven controls against the originals. GitHub reports success for this head in run `44852412541`. [Job log](https://github.com/physicsvigilante/sim_heat/actions/runs/44852412541/job/136686613980) · [Workflow](https://github.com/physicsvigilante/sim_heat/blob/b96e18a1a988bc323d7bae0eb274a52f4209d4af/.github/workflows/h1-general-conduction-ci.yml)
- I downloaded artifact `14686335831` and checked its 316,924 bytes, ZIP CRCs and SHA-256 `daf1531f4a3bf890fe3f6468a886f0378f05d10e006cc1907782837ebe1b275a`. Its source-head member names the corrected head. Decompressed fresh stdout is 860,196 bytes with SHA-256 `94ec9446278fcd530f9902f4540fefbaef2582ee990f5d9551d77f5c63c10de2`. Its decoded JSON equals the preserved first output. My local successor passed all 49,241 sample comparisons on that downloaded output and returned the archived summary. The archived control results equal the preserved control results. [Hosted artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44852412541/artifacts/14686335831)
- I ran the pinned Windows interpreter with `-B -m unittest -v qualification.h1_n13.test_conduction tests.test_twinbridge_ratios`. Seven tests passed. Independently editing only each claimed ratio left the old verifier summary identical. The successor rejected zero for `requests.lowerFlow` at sample 1, half the genuine maximum for `exports.amber.T` at sample 1 and half for `integrals.bath.Q_to_network` at sample 375. The rejection named the intended series and sample in each case. An exact unmodified `upper.G` series with ratio zero passed.
- For K, W and J, the comparison uses exact rational conversion of each emitted float and the Decimal analytical value. Rejection occurs when a discrepancy exceeds the claimed ratio times the applicable budget (10⁻⁸ K, 10⁻⁸ W or 10⁻⁵ J) plus 10⁻⁶⁵ in that unit. Recomputing lower flow with 100 decimal digits, its tightest analytical lower bound on the ratio occurs at sample 6, approximately 7.08487508757 × 10⁻⁷. The recorded ratio exceeds this threshold by about 10⁻⁵⁷. I set the ratio halfway into that gap. The successor accepted the smaller claim. Analytical comparison can disprove an incompatible ratio but cannot recover the maximum distance from the binary64 centre to the solver's outward interval endpoints.

This was an owner-requested fresh reviewer subagent with separate context. I reviewed the published case and its recorded evidence. The testing was offline and case-specific. Native qualification, wider graph coverage and merge approval remain outside this review.
