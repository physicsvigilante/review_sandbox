"""Chat B R2 adversarial probes, NOT executed against native library by reviewer.

Run from pinned conductor_sim source checkout after install:
  python -m pip install -e .
  python /path/to/review_01_chat_b_probes.py
This file uses only public/native source APIs, makes no edits and writes no files.
"""
from dataclasses import replace
from math import sqrt

from conductor_sim import (
    CoupledPropertyEdit, CoupledHypothesis, CoupledPhysicalPlan,
    CoupledEventPlan, CoupledEventRun, run_coupled_event_family,
)
from conductor_sim.motion_events import EventPolicy, PlaneEvent
from examples.m29a_structural_family import model
from examples.m31b_rod_reference import make_plan


def independent_gravity_field_case():
    # Novel Chat B two-property hypothesis and signed y-detector, not the
    # developer's source/mass or rod example. Both modifications affect a_y.
    physical = CoupledPhysicalPlan('chatb:m31b-gravity', model('uniform-edits'), (
        CoupledHypothesis('gravity-field', 'add-gravity',
            'Joint edit: newly assembled downward gravity and existing y-field.', (
                CoupledPropertyEdit('gravity', 'acceleration_m_s2', (0., -3.3, 0.)),
                CoupledPropertyEdit('field:Ey', 'field_v_m', (0., 1750., 0.)),
            )),
    ))
    detector=PlaneEvent('chatb:y-neg', (0., -0.003, 0.), (0., 1., 0.),
                        'Signed downward crossing of y=-3 mm', direction=-1)
    data=run_coupled_event_family(CoupledEventPlan(
        physical,(detector,),EventPolicy(.001, 1e-8, 1e-9, 1e-7)))
    parent,child=data.parents[0],data.children[0]
    assert parent.status==child.status=='complete'
    assert child.physical_entry.scenario.parent_revision_id==parent.parent_scenario.revision_id
    assert child.physical_entry.scenario.source_annotations==parent.parent_scenario.source_annotations
    # Original E_y=50 V/m; q=1 nC, m=1e-5 kg, g_y original absent.
    # Structural parent newly adds g_y=-2 m/s^2. Child jointly changes it to
    # -3.3 m/s^2 and E_y from 50 to 1750 V/m. x field does not affect y.
    expected_parent=sqrt(2*.003/(2.-1e-9*50./1e-5))
    expected_child=sqrt(2*.003/(3.3-1e-9*1750./1e-5))
    for label,run,expected in [('parent',parent.event_run,expected_parent),
                               ('child',child.event_run,expected_child)]:
        roots=[e for e in run.events if e.event_id=='chatb:y-neg']
        assert run.trajectory.termination=='duration'
        assert len(roots)==1 and roots[0].direction==-1
        assert abs(roots[0].sample.time_s-expected)<1e-7,(label,expected,roots[0].sample.time_s)
        print('NOVEL-NATIVE',label,'t_s=',roots[0].sample.time_s,'analytic_s=',expected)
    pair=data.as_dict()['coupled_events'][0]['parent_event_time_comparisons'][0]
    assert pair['status']=='one-resolved-pair'
    assert data.original_event_run.as_dict()['outcomes']['chatb:y-neg']=='not-found-at-requested-resolution'
    print('NOVEL NATIVE CASE: PASS')


def expect_rejection(label, construct):
    try:
        forged=construct()
        evidence=forged.as_dict()
    except (TypeError,ValueError) as exc:
        print(label,'REJECTED:',type(exc).__name__,str(exc)[:120])
        return
    print(label,'POTENTIAL INTEGRITY BYPASS:',
          [(c['case_id'],c['parent_event_time_comparisons']) for c in evidence['coupled_events']])
    raise AssertionError(label+': fabricated native evidence was accepted')


def forged_evidence_probes():
    authentic=run_coupled_event_family(make_plan())
    c=authentic.children[0]
    e=c.event_run.events[0]
    delta=.03
    # Attack A: retain original physical root state but re-label its clock and
    # whole bracket 30ms later. The event plane equation still evaluates zero
    # at the old state, but the true trajectory is elsewhere at the new time.
    shifted=replace(e,time_bracket_s=tuple(t+delta for t in e.time_bracket_s),
                    sample=replace(e.sample,time_s=e.sample.time_s+delta))
    shifted_child=replace(c,event_run=replace(c.event_run, events=(shifted,)))
    expect_rejection('FORGED-ROOT-TIME',lambda: CoupledEventRun(
        authentic.plan,authentic.physical_family,authentic.original_event_run,
        authentic.parents,(shifted_child,)))
    # Attack B: replace a successful, physically eligible structural-parent
    # event run by a fabricated refusal. Would suppress a true parent pairing.
    fake_parent=replace(authentic.parents[0],event_run=None,
                        status='rejected-event-study',reason='invented refusal')
    expect_rejection('FORGED-PARENT-REFUSAL',lambda: CoupledEventRun(
        authentic.plan,authentic.physical_family,authentic.original_event_run,
        (fake_parent,),authentic.children))
    print('ADVERSARIAL CONSTRUCTOR PROBES: PASS')


if __name__=='__main__':
    independent_gravity_field_case()
    forged_evidence_probes()
