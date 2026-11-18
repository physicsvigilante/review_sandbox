"""Independent Chat B R2-02: reviewer-authored, source-pinned conductor science.
No original production file is changed. Numbers are new; native outputs are not
used as reference values. Browser checks inspect the actual generated HTML.
"""
from __future__ import annotations
from copy import deepcopy
from pathlib import Path
import json
import math
import re

from conductor_sim import (
    ConnectedShellBackend, ConnectionPlan, ElectricalLink, ElectrostaticProblem,
    ExternalSphereBackend, FixedNetCharge, NestedShellBackend, PointCharge,
    SolidSphere, SphericalShell,
)
from conductor_sim.solver import UnsupportedProblem
from tools.m36c_jee_conductor_replay import run_all
from tools.m36c_jee_conductor_reference import verify

EPS = 8.8541878128e-12
K = 1.0 / (4.0 * math.pi * EPS)
ROOT = Path("review-artifacts/conductor-m36c-chat-b-02")
scalar_checks = []

def check(label, observed, reference, rtol=2e-8, atol=2e-13):
    a=float(observed)
    e=float(reference)
    if not (math.isfinite(a) and math.isfinite(e)
            and math.isclose(a,e,rel_tol=rtol,abs_tol=atol)):
        raise AssertionError(f"{label}: native={a!r}, reviewer-SI={e!r}")
    scalar_checks.append({"name":label,"native":a,"reviewer_SI":e})

def connected_world():
    """New positive core / negative shell: actual floating connection energy."""
    core_q, coat_q = 4.2e-9, -1.3e-9
    core_r, coat_inner, coat_outer = .075, .235, .26
    problem = ElectrostaticProblem(conductors=(
        SolidSphere(core_r,FixedNetCharge(core_q),name="core"),
        SphericalShell(coat_inner,coat_outer,FixedNetCharge(coat_q),name="coat"),
    ))
    plan=ConnectionPlan(problem,(ElectricalLink(("core","coat")),))
    out=ConnectedShellBackend().solve(plan)
    total=core_q+coat_q
    core_before=out.before.conductor_by_name("core")
    coat_before=out.before.conductor_by_name("coat")
    core_after=out.after.conductor_by_name("core")
    coat_after=out.after.conductor_by_name("coat")
    gap=.5*K*core_q**2*(1/core_r-1/coat_inner)
    outside=.5*K*total**2/coat_outer
    check("connection core before",core_before.net_charge_c,core_q)
    check("connection coat before",coat_before.net_charge_c,coat_q)
    check("connection coat inner before",coat_before.inner_surface_charge_c,-core_q)
    check("connection coat outer before",coat_before.outer_surface_charge_c,total)
    check("connection core after",core_after.net_charge_c,0.)
    check("connection coat inner after",coat_after.inner_surface_charge_c,0.)
    check("connection coat outer after",coat_after.outer_surface_charge_c,total)
    check("connection signed gap E before",out.before.electric_field_at((.19,0.,0.))[0],
          K*core_q/.19**2,atol=1e-8)
    check("connection signed gap E after",out.after.electric_field_at((.19,0.,0.))[0],
          0.,atol=1e-8)
    check("connection initial whole-space U",out.radial_field_energy_before_j,gap+outside)
    check("connection final whole-space U",out.radial_field_energy_after_j,outside)
    check("connection released U",out.released_field_energy_j,gap)
    return {"family":"positive solid core/negative shell, floating wire",
            "source_independent_inputs":[core_q,coat_q,core_r,coat_inner,coat_outer],
            "expected_energy_release_J":gap}

def nested_central_reprobe():
    """New signed shells, central negative q, two CHANGED original A/B positions."""
    q,q1,q2=-1.8e-9,.6e-9,-2.7e-9
    a,b,w=.13,.30,2e-6
    first_r,second_r=.061,.23
    a_in,b_in=a-w,b-w
    p=ElectrostaticProblem(
        charges=(PointCharge(q,(0.,0.,0.)),),
        conductors=(
            SphericalShell(a_in,a,FixedNetCharge(q1),name="one"),
            SphericalShell(b_in,b,FixedNetCharge(q2),name="two"),
        ))
    backend=NestedShellBackend()
    assert backend.supports(p), "new signed concentric model rejected unexpectedly"
    s=backend.solve(p)
    flux1=q+q1
    flux2=q+q1+q2
    one=s.conductor_by_name("one")
    two=s.conductor_by_name("two")
    check("new central first inner C",one.inner_surface_charge_c,-q)
    check("new central first outer C",one.outer_surface_charge_c,flux1)
    check("new central second inner C",two.inner_surface_charge_c,-flux1)
    check("new central second outer C",two.outer_surface_charge_c,flux2)
    check("new central first V",one.potential_v,
          K*(flux1*(1/a-1/b_in)+flux2/b),atol=1e-8)
    check("new central second V",two.potential_v,K*flux2/b,atol=1e-8)
    ref_A=K*(q/first_r-q/a_in+flux1/a-flux1/b_in+flux2/b)
    ref_B=K*(flux1/second_r-flux1/b_in+flux2/b)
    check("NEW physical V(A) at r=0.061m",s.potential_at((first_r,0.,0.)),
          ref_A,atol=1e-8)
    check("NEW physical V(B) at r=0.23m",s.potential_at((0.,second_r,0.)),
          ref_B,atol=1e-8)
    new_A=.079
    ref_A2=K*(q/new_A-q/a_in+flux1/a-flux1/b_in+flux2/b)
    check("changed real cavity probe r=0.079m",s.potential_at((0.,0.,new_A)),
          ref_A2,atol=1e-8)
    if not abs(ref_A-ref_A2)>10.:
        raise AssertionError("changing A should produce a measurable potential change")
    check("new signed gap E",s.electric_field_at((0.,second_r,0.))[1],
          K*flux1/second_r**2,atol=1e-8)
    return {"family":"new central negative cavity q + opposite signed nested shells",
            "teacher_original_q_C":q, "A_reference_V":ref_A,
            "B_reference_V":ref_B, "changed_A_reference_V":ref_A2}

def shifted_kelvin():
    """Different shifted positive source and net-negative single spherical shell."""
    q,net=.0024e-6,-1.1e-9
    a,b,d=.074,.093,.031
    p=ElectrostaticProblem(
        charges=(PointCharge(q,(0.,0.,d)),),
        conductors=(SphericalShell(a,b,FixedNetCharge(net),name="metal"),))
    backend=NestedShellBackend()
    assert backend.supports(p),"new shifted Kelvin model unexpectedly unsupported"
    s=backend.solve(p)
    metal=s.conductor_by_name("metal")
    check("new shifted negative inner total",metal.inner_surface_charge_c,-q)
    check("new shifted exterior total",metal.outer_surface_charge_c,q+net)
    check("new shifted conductor V",metal.potential_v,K*(q+net)/b,atol=1e-8)
    front=-q*(a*a-d*d)/(4*math.pi*a*(a-d)**3)
    back=-q*(a*a-d*d)/(4*math.pi*a*(a+d)**3)
    check("new Kelvin physical near density",
          s.surface_charge_density_at("metal","inner",(0.,0.,a)),front,atol=1e-12)
    check("new Kelvin physical far density",
          s.surface_charge_density_at("metal","inner",(0.,0.,-a)),back,atol=1e-12)
    assert front<back<0. and abs(front)>abs(back)
    check("new Kelvin zero metal E",s.electric_field_at((0.,0.,.08))[2],0.,atol=1e-8)
    return {"family":"shifted positive cavity point and negative-net shell",
            "near_sigma_C_m2":front,"far_sigma_C_m2":back}

def neutral_external_kelvin():
    """New +source on the x-axis; isolated neutral conductor, not a time sweep."""
    q,a,d=2.6e-6,1.15,4.1
    p=ElectrostaticProblem(
        charges=(PointCharge(q,(d,0.,0.)),),
        conductors=(SolidSphere(a,FixedNetCharge(0.),name="neutral"),))
    b=ExternalSphereBackend()
    assert b.supports(p), "new positive Kelvin external problem rejected"
    s=b.solve(p)
    image=-q*a/d
    center=-image
    image_x=a*a/d
    expected_V=K*q/d
    check("new external neutral metal net",s.conductor_by_name("neutral").net_charge_c,0.)
    check("new external neutral metal V",s.conductor_by_name("neutral").potential_v,
          expected_V,atol=1e-8)
    for pos in [(a,0.,0.),(0.,a,0.),(-a,0.,0.)]:
        check("new external equipotential "+str(pos),s.potential_at(pos),expected_V,atol=1e-8)
    actual_induced=s.potential_at((0.,a,0.))-K*q/math.hypot(a,d)
    expected_induced=K*(image/math.hypot(a,image_x)+center/a)
    check("new external equator induced-only V",actual_induced,
          expected_induced,atol=1e-8)
    check("new external metal interior E",s.electric_field_at((0.,0.,0.))[0],0.,atol=1e-8)
    return {"family":"positive external Kelvin point to isolated neutral solid",
            "source_charge_C":q,"surface_reference_V":expected_V}

def forbidden_worlds():
    nested=NestedShellBackend()
    models=[
        ("nonconcentric-shell-refusal",ElectrostaticProblem(conductors=(
            SphericalShell(.07,.09,FixedNetCharge(1e-9),name="x"),
            SphericalShell(.2,.25,FixedNetCharge(-2e-9),
                           center_m=(.008,0.,0.),name="y"),
        ))),
        ("overlapping-shell-refusal",ElectrostaticProblem(conductors=(
            SphericalShell(.05,.16,FixedNetCharge(0.),name="x"),
            SphericalShell(.14,.22,FixedNetCharge(0.),name="y"),
        ))),
        ("charge-buried-in-metal-refusal",ElectrostaticProblem(
            charges=(PointCharge(7e-10,(0.,0.,.075)),),
            conductors=(SphericalShell(.07,.09,FixedNetCharge(0.),name="x"),))),
    ]
    names=[]
    for label,p in models:
        if nested.supports(p):
            raise AssertionError("unqualified native geometry admitted: "+label)
        try:
            nested.solve(p)
        except UnsupportedProblem:
            names.append(label)
        else:
            raise AssertionError("unqualified geometry solved: "+label)
    ext=ExternalSphereBackend()
    buried=ElectrostaticProblem(
        charges=(PointCharge(1.2e-9,(.4,0.,0.)),),
        conductors=(SolidSphere(1.,FixedNetCharge(0.),name="sphere"),))
    assert not ext.supports(buried)
    try:
        ext.solve(buried)
    except UnsupportedProblem:
        names.append("source-inside-solid-refusal")
    else:
        raise AssertionError("external Kelvin accepted source inside metal")
    return names

def falsifications(m):
    assert verify(m)["checked_distinct_source_apparatus"]==7
    mutations=[
      ("old-near-far-angle-swap", "p69-cavity-central-vs-shifted",
       ("native_observations",5,"theta_rad"),math.pi),
      ("old-far-near-angle-swap", "p69-cavity-central-vs-shifted",
       ("native_observations",6,"theta_rad"),0.),
      ("old-inner-shell-labelled-outer", "p27-cavity-two-shells",
       ("native_observations",2,"conductor"),"outer"),
      ("old-forged-illustration", "p27-cavity-two-shells",
       ("source_anchor",),"Unrelated illustration"),
      ("new-wrong-A-world-point", "p27-cavity-two-shells",
       ("native_observations",0,"point_m"),[.052,0.,0.]),
      ("new-B-point-relabeled-as-A", "p27-cavity-two-shells",
       ("native_observations",0,"label"),"Printed original V(B), intershell gap"),
      ("new-original-source-displaced", "p27-cavity-two-shells",
       ("authored_states",0,"charges",0,"position_m"),[0.,0.,.012]),
      ("new-original-charge-sign-reversed", "p27-cavity-two-shells",
       ("authored_states",0,"charges",0,"charge_c"),-1e-9),
      ("new-original-second-shell-charge-wrong", "p27-cavity-two-shells",
       ("authored_states",0,"native_conductor_results",1,"net_charge_c"),-3e-9),
      ("new-incorrect-original-page", "p27-cavity-two-shells",
       ("source_pdf_page",),26),
      ("new-p69-Kelvin-nonphysical-theta", "p69-cavity-central-vs-shifted",
       ("native_observations",5,"theta_rad"),.2),
      ("new-p26-fake-literal-solid", "p26-conductor-potential",
       ("source_shape_fidelity",),"literal SOLID sphere, geometry exact"),
    ]
    rejected=[]
    for name,case,path,value in mutations:
        forged=deepcopy(m)
        target=forged["native_source_apparatus"][case]
        for step in path[:-1]:
            target=target[step]
        target[path[-1]]=value
        try:
            verify(forged)
        except (AssertionError,KeyError,ValueError,TypeError) as exc:
            rejected.append({"attack":name,"rejected":True,"message":str(exc)[:250]})
        else:
            raise AssertionError("SOURCE-FREE VERIFIER ACCEPTED FORGERY: "+name)
    return rejected

def browser_originals(m,generated):
    from playwright.sync_api import sync_playwright
    shots=ROOT/"browser-screenshots"
    shots.mkdir(exist_ok=True)
    names=list(m["native_source_apparatus"])
    results={}
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        try:
            for case in names:
                page=browser.new_page(viewport={"width":1280,"height":800})
                requests=[];errors=[]
                page.on("request",lambda req: requests.append(req.url)
                        if req.url.startswith(("http://","https://")) else None)
                page.on("pageerror",lambda e: errors.append(str(e)))
                try:
                    url=(generated/m["native_source_apparatus"][case]["viewer_file"]).resolve().as_uri()
                    page.goto(url,wait_until="load",timeout=45000)
                    body=page.locator("body").inner_text(timeout=15000)
                    if not (len(body)>120 and page.locator("canvas,svg").count()>0):
                        raise AssertionError("missing physical graphic: "+case)
                    if requests or errors:
                        raise AssertionError("offline/JS error "+case+" "+repr((requests,errors)))
                    if case=="p26-conductor-potential":
                        notice=page.locator("#original-solid-sphere-proxy-disclosure")
                        assert notice.is_visible(), "p26 caveat must be actually visible"
                        assert "SOLID" in notice.inner_text() and "HOLLOW SHELL PROXY" in notice.inner_text()
                    if case=="p27-cavity-two-shells":
                        readout=page.locator("#p27-original-A-B")
                        assert readout.is_visible(), "p27 first state A/B readout not visible"
                        txt=readout.inner_text()
                        found=re.search(r"Actual finite-metal V\(A\) = ([0-9eE.+-]+) V, V\(B\) = ([0-9eE.+-]+) V",txt)
                        if not found:
                            raise AssertionError("original V(A), V(B) not legibly shown in browser: "+txt[:350])
                        obs=m["native_source_apparatus"][case]["native_observations"]
                        check("browser p27 visible original A V",float(found.group(1)),obs[0]["native_value"],
                              rtol=3e-8,atol=1e-5)
                        check("browser p27 visible original B V",float(found.group(2)),obs[1]["native_value"],
                              rtol=3e-8,atol=1e-5)
                        assert "TEACHER EXTENSION ONLY" in txt
                    page.screenshot(path=str(shots/(case+"-first.png")),full_page=True)
                    changed=None
                    if case in ("p03-single-27","p27-cavity-two-shells",
                                "p69-cavity-central-vs-shifted","p09-multiple-27"):
                        sliders=page.locator('input[type="range"]')
                        assert sliders.count()>0,"two static frames should be navigable "+case
                        sliders.first.evaluate("""el => {
                            el.value=el.max;
                            el.dispatchEvent(new Event('input',{bubbles:true}));
                            el.dispatchEvent(new Event('change',{bubbles:true}));
                        }""")
                        page.wait_for_timeout(350)
                        after=page.locator("body").inner_text()
                        if body==after:
                            raise AssertionError("static scene did not switch visibly "+case)
                        page.screenshot(path=str(shots/(case+"-last.png")),full_page=True)
                        changed=True
                    results[case]={"visible_characters":len(body),
                                   "real_graphics":page.locator("canvas,svg").count(),
                                   "first_frame_screenshot":case+"-first.png",
                                   "second_static_frame_changed":changed,
                                   "network_requests":len(requests),"js_errors":errors}
                finally:
                    page.close()
        finally:
            browser.close()
    return results

def main():
    ROOT.mkdir(parents=True,exist_ok=True)
    generated=ROOT/"native-originals"
    original=run_all(generated)
    positive=verify(original)
    assert positive["checked_distinct_source_apparatus"]==7
    assert original["historical_anchors_used"][1:3]==["p10-linked-13","p10-linked-14"]
    p27=original["native_source_apparatus"]["p27-cavity-two-shells"]
    assert p27["source_pdf_page"]==27 and p27["source_anchor"]=="Illustration 4"
    assert p27["authored_states"][0]["charges"][0]["position_m"]==[0.,0.,0.]
    assert p27["authored_states"][1]["charges"][0]["position_m"]==[0.,0.,.02]
    assert original["non_success_controls"][0]["kind"]=="PARTIAL"
    assert original["non_success_controls"][1]["kind"]=="UNSUPPORTED"
    novel=[connected_world(),nested_central_reprobe(),shifted_kelvin(),
           neutral_external_kelvin()]
    refusals=forbidden_worlds()
    rejected=falsifications(original)
    browser=browser_originals(original,generated)
    result={"reviewer":"Chat B independent R2-02 on corrected fixed HEAD",
      "candidate_HEAD":"82de04484006d61f691e1e3a1344f5707729a821",
      "candidate_TREE":"c43134db1726dc2f1ff48b0b9a560dff090bf56d",
      "original_verified_positive":True,
      "novel_native_families":novel,
      "physical_scalar_checks":scalar_checks,
      "unqualified_refusals":refusals,
      "fresh_source_attribution_falsifications":rejected,
      "real_offline_browser":browser}
    (ROOT/"independent-results.json").write_text(json.dumps(result,indent=2,
        allow_nan=False)+"\n",encoding="utf-8")
    print("REVIEWER-OWNED R2-02 PASS:",len(novel),"new native arrangements,",
          len(scalar_checks),"independent SI/browser scalar checks,",
          len(refusals),"refusals,",len(rejected),"hostile forgeries rejected,",
          len(browser),"real offline Chromium viewers")
if __name__=="__main__":
    main()
