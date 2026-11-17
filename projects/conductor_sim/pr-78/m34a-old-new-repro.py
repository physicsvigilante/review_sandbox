"""Developer-owned M34a exact OLD vs NEW native model-admission regression.

Use the SAME original source/field/plane code under two separately checked-out
Python source trees, old released M33b and corrected M34a draft. No source
modules are copied or code-under-test monkeypatched.
"""
from __future__ import annotations

import argparse
import json
from math import hypot, ulp

from conductor_sim import (
    PointCharge, PrescribedField, TestChargeMotionSpec,
    UniformElectricField, UniformGravity,
)
from conductor_sim.scenarios import PrescribedScenario
from conductor_sim.structural_scenarios import NamedSource, reassemble_scenario


def run(expected):
    original=PrescribedScenario(
        "m34a:side-by-side-root",
        TestChargeMotionSpec(
            PrescribedField((UniformElectricField((320.,-80.,160.)),)),
            PointCharge(2e-9,(.003,.012,.06)),1.6e-6,
            (.25,-.125,0.),.6,.01,
            plane_normal=(1.,2.,-1.),
            gravity=UniformGravity((.16,-.04,.08))),
        (("field:base","Original held oblique source"),),
        "Exact same teacher-authored physical source input on both Git trees.")
    normal=original.spec.plane_normal
    assert hypot(*normal)==1.+ulp(1.), "precondition non-dyadic root must expose 1ULP"
    before=original.as_dict()
    kwargs=dict(
        scenario_id="m34a:side-by-side-child",
        note="Add one physically in-plane held source with unmodified analysis.",
        add_sources=(NamedSource(
            "field:aux","New physically in-plane held source",
            UniformElectricField((90.,35.,160.))),))
    if expected=="refusal":
        try:
            reassemble_scenario(original,**kwargs)
        except ValueError as exc:
            assert "structural operation cannot edit particle, analysis or numerical controls" in str(exc),str(exc)
            accepted=False
            diagnostic=str(exc)
        else:
            raise AssertionError("released source unexpectedly admitted old oblique reassembly")
        child=None
    elif expected=="admitted":
        child=reassemble_scenario(original,**kwargs)
        accepted=True
        diagnostic="complete native M22a source reassembly with exact analysis retention"
        assert child.parent is original
        assert child.scenario.spec.plane_normal==normal
        assert tuple(x.hex() for x in child.scenario.spec.plane_normal)==tuple(x.hex() for x in normal)
        assert child.scenario.spec.field.sources[-1].field_v_m==(90.,35.,160.)
        assert child.as_dict()["parent_revision_id"]==original.revision_id
        assert child.scenario.source_annotations[-1][0]=="field:aux"
    else:
        raise ValueError("unknown expected result")
    assert original.as_dict()==before
    return dict(verdict="PASS", expected=expected, accepted=accepted,
        root_revision_id=original.revision_id,
        original_normal=normal, candidate_child_revision_id=(
            None if child is None else child.scenario.revision_id),
        original_preserved=True, diagnostic=diagnostic)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--expect",choices=("refusal","admitted"),required=True)
    args=parser.parse_args()
    print(json.dumps(run(args.expect),sort_keys=True,allow_nan=False))


if __name__=="__main__":
    main()
