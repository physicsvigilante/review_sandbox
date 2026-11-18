"""Chat B independent conductor R2 experiment; source checkout pinned by workflow.

Uses public analytical backends for THREE genuinely new apparatus. References are
derived here from SI electrostatics, not source saved "expected" values.
Also attacks source-only saved native evidence and reports semantic verifier holes.
"""
from __future__ import annotations

from copy import deepcopy
import json
import math
from pathlib import Path

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
checks = []

def near(label, measured, expected, *, rtol=2e-8, atol=1e-17):
    if not math.isfinite(float(measured)) or not math.isclose(
        float(measured), float(expected), rel_tol=rtol, abs_tol=atol
    ):
        raise AssertionError(
            f"{label}: public engine/measured={measured!r}, reviewer SI={expected!r}"
        )
    checks.append({"check":label,"observed":measured,"reviewer_reference":expected})

def original_cases(m):
    cases = m["native_source_apparatus"]
    assert len(cases) == 7
    assert len(m["historical_anchors_used"]) == 8
    # Workbook p3: solid sphere, real shell and BOTH gap and outer vacuum field.
    c = cases["p03-single-27"]
    q, a, b, B = 20e-6, 0.1, 0.199999, 0.2
    near("p03 energy release J",c["released_energy_j"],K*q*q*(1/a-1/b)/2)
    near("p03 initial whole space energy J",c["radial_energy_before_j"],
         K*q*q*(1/a-1/b+1/B)/2)
    near("p03 shell before inner C",c["before"][1]["inner_surface_charge_c"],-q)
    near("p03 shell before outer C",c["before"][1]["outer_surface_charge_c"],q)
    near("p03 solid after zero C",c["after"][0]["net_charge_c"],0.)
    near("p03 exterior energy AFTER J",c["radial_energy_after_j"],K*q*q/(2*B))
    near("p03 gap signed x field",c["gap_field_before_v_m"][0],K*q/(.15*.15),
         atol=1e-8)
    # Workbook p10 linked Q13 and Q14: one apparatus, opposite shell nets.
    c = cases["p10-linked-13+p10-linked-14"]
    q = 4*math.pi*EPS*(.10**2)*1.8e6
    near("p10 actual initial inner charge",c["before"][0]["net_charge_c"],q)
    near("p10 actual outer net",c["before"][1]["net_charge_c"],-q)
    near("p10 gap-only E energy J",c["released_energy_j"],
         K*q*q*(1/.10-1/.199999)/2)
    near("p10 exterior initially zero J",c["radial_energy_before_j"],
         K*q*q*(1/.10-1/.199999)/2)
    near("p10 final equilibrium zero J",c["radial_energy_after_j"],0.)
    # Workbook p14: q and 2q on independent shells, total 3q exterior stays.
    c = cases["p14-numerical-07"]
    V = K*3e-9/.20
    near("p14 before outer V",c["before"][1]["potential_v"],V,atol=1e-9)
    near("p14 after outer V",c["after"][1]["potential_v"],V,atol=1e-9)
    near("p14 postwire gap field",c["gap_field_after_v_m"][0],0.,atol=1e-9)
    # Notes p26: E in cavity/metal is zero, exterior V = kQ/r.
    c = cases["p26-conductor-potential"]["native_observations"]
    near("p26 V at R/2",c[0]["native_value"],K*1e-9/.1,atol=1e-8)
    near("p26 V at 3R/2",c[1]["native_value"],K*1e-9/.15,atol=1e-8)
    near("p26 internal E",c[2]["native_value"],0.,atol=1e-8)
    # Notes p27: one charge in innermost cavity and TWO concentric metals.
    c = cases["p27-cavity-two-shells"]["authored_states"][0]["native_conductor_results"]
    near("p27 first inner face",c[0]["inner_surface_charge_c"],-1e-9)
    near("p27 first outer face",c[0]["outer_surface_charge_c"],3e-9)
    near("p27 second inner face",c[1]["inner_surface_charge_c"],-3e-9)
    near("p27 second outer face",c[1]["outer_surface_charge_c"],6e-9)
    near("p27 outer V",c[1]["potential_v"],K*6e-9/.20,atol=1e-8)
    # Notes p69: Kelvin density, near/centre/far versus ANGLE.
    c = cases["p69-cavity-central-vs-shifted"]["native_observations"]
    radius, offset, q = .08, .04, 1e-9
    centered = -q/(4*math.pi*radius*radius)
    front = -q*(radius*radius-offset*offset)/(4*math.pi*radius*(radius-offset)**3)
    back = -q*(radius*radius-offset*offset)/(4*math.pi*radius*(radius+offset)**3)
    near("p69 centred sigma",c[4]["native_value"],centered)
    near("p69 near sigma at 0 rad",c[5]["native_value"],front)
    near("p69 far sigma at pi rad",c[6]["native_value"],back)
    assert c[5]["theta_rad"] == 0 and math.isclose(c[6]["theta_rad"],math.pi)
    assert abs(front)>abs(centered)>abs(back)
    # Workbook p9: neutral isolated sphere 3-4-5 tangent.
    c = cases["p09-multiple-27"]
    assert c["source_givens"]["point_source_position_m"] == [3.,4.,0.]
    near("p09 neutral sphere net C",c["source_givens"]["sphere_net_charge_c"],0.)
    near("p09 neutral metal V",c["native_sphere_potential_v"],K*1e-6/5,
         atol=1e-8)
    near("p09 induced-only tangent V",c["native_induced_only_at_tangent_v"],
         -K*1e-6/20,atol=1e-8)
    near("p09 direct plus induced tangent V",c["native_total_potential_at_tangent_v"],
         K*1e-6/4-K*1e-6/20,atol=1e-8)

def unfamiliar_connected():
    # New, negatively charged SOLID core plus positively charged metal coat.
    q1, q2, a, b, c = -3.7e-9, .8e-9, .12, .27, .28
    p = ElectrostaticProblem(conductors=(
        SolidSphere(a, FixedNetCharge(q1),name="core"),
        SphericalShell(b,c,FixedNetCharge(q2),name="coat"),
    ))
    plan = ConnectionPlan(p,(ElectricalLink(("core","coat")),))
    s = ConnectedShellBackend().solve(plan)
    qtot = q1+q2
    before=s.before;after=s.after
    near("NEW core initial charge",before.conductor_by_name("core").net_charge_c,q1)
    near("NEW coat inner before",-0.0+before.conductor_by_name("coat").inner_surface_charge_c,-q1)
    near("NEW coat exterior before",before.conductor_by_name("coat").outer_surface_charge_c,qtot)
    near("NEW core postwire charge",after.conductor_by_name("core").net_charge_c,0.)
    near("NEW coat postwire exterior",after.conductor_by_name("coat").outer_surface_charge_c,qtot)
    near("NEW signed gap field",before.electric_field_at((.20,0.,0.))[0],
         K*q1/.20**2,atol=1e-8)
    near("NEW gap field extinguished",after.electric_field_at((.20,0.,0.))[0],
         0.,atol=1e-8)
    near("NEW initial gap+outside energy",s.radial_field_energy_before_j,
         .5*K*(q1*q1*(1/a-1/b)+qtot*qtot/c))
    near("NEW final external-only energy",s.radial_field_energy_after_j,
         .5*K*qtot*qtot/c)
    near("NEW released energy",s.released_field_energy_j,
         .5*K*q1*q1*(1/a-1/b))
    return {"family":"mixed solid-shell floating connection",
            "core_charge_c":q1,"shell_initial_charge_c":q2,
            "released_energy_j":s.released_field_energy_j}

def unfamiliar_nested():
    # New sign, displacement and dimensions, TWO shells; cavity field is nonradial.
    q, Q1, Q2, d = -1.25e-9, 2.1e-9, -.4e-9, .029
    a,b,c,e = .072,.085,.17,.19
    p = ElectrostaticProblem(charges=(PointCharge(q,(0.,0.,d)),),
        conductors=(
            SphericalShell(a,b,FixedNetCharge(Q1),name="inner"),
            SphericalShell(c,e,FixedNetCharge(Q2),name="outer"),
        ))
    backend=NestedShellBackend()
    assert backend.supports(p)
    s=backend.solve(p)
    first=s.conductor_by_name("inner"); second=s.conductor_by_name("outer")
    flux=q+Q1
    outerflux=q+Q1+Q2
    near("NEW nested inner inner charge",first.inner_surface_charge_c,-q)
    near("NEW nested first outer charge",first.outer_surface_charge_c,flux)
    near("NEW nested second inner charge",second.inner_surface_charge_c,-flux)
    near("NEW nested second exterior charge",second.outer_surface_charge_c,outerflux)
    near("NEW nested outer metal V",second.potential_v,K*outerflux/e,atol=1e-8)
    near("NEW nested inner metal V",first.potential_v,
         K*(outerflux/e + flux*(1/b-1/c)),atol=1e-8)
    near("NEW nested radial gap E",s.electric_field_at((0.,0.,.12))[2],
         K*flux/.12**2,atol=1e-8)
    near("NEW nested metal zero E",s.electric_field_at((0.,0.,.18))[2],
         0.,atol=1e-8)
    near_sig=-q*(a*a-d*d)/(4*math.pi*a*(a-d)**3)
    far_sig=-q*(a*a-d*d)/(4*math.pi*a*(a+d)**3)
    near("NEW nested near Kelvin sigma",
         s.surface_charge_density_at("inner","inner",(0.,0.,a)),near_sig)
    near("NEW nested far Kelvin sigma",
         s.surface_charge_density_at("inner","inner",(0.,0.,-a)),far_sig)
    assert near_sig>far_sig>0
    return {"family":"displaced negative cavity charge in two shells",
            "near_sigma_c_m2":near_sig,"far_sigma_c_m2":far_sig}

def unfamiliar_external():
    # Neutral ISOLATED sphere, negative point, new radius/distance/axis.
    q, a, d = -2.3e-6, 1.6, 4.3
    p=ElectrostaticProblem(charges=(PointCharge(q,(0.,0.,d)),),
        conductors=(SolidSphere(a,FixedNetCharge(0.),name="neutral"),))
    s=ExternalSphereBackend().solve(p)
    image=-q*a/d; center=-image; zi=a*a/d
    near("NEW external sphere charge C",s.conductor_results[0].net_charge_c,0.)
    near("NEW external sphere metal V",s.conductor_results[0].potential_v,
         K*q/d,atol=1e-8)
    near("NEW external nearest surface V",s.potential_at((0.,0.,a)),
         K*q/d,atol=1e-8)
    near("NEW external equatorial surface V",s.potential_at((a,0.,0.)),
         K*q/d,atol=1e-8)
    equatorial_induced=K*(image/math.sqrt(a*a+zi*zi)+center/a)
    near("NEW external Kelvin induced equator potential",
         s.potential_at((a,0.,0.))-K*q/math.sqrt(a*a+d*d),
         equatorial_induced,atol=1e-8)
    near("NEW external center zero electric field",
         s.electric_field_at((0.,0.,0.))[2],0.,atol=1e-8)
    return {"family":"negative external source at isolated neutral sphere",
            "metal_potential_v":K*q/d,
            "kelvin_image_charge_c":image,"central_image_charge_c":center}

def invalid_geometry_controls():
    b=NestedShellBackend()
    bad=[
        ("nonconcentric",ElectrostaticProblem(conductors=(
            SphericalShell(.07,.09,FixedNetCharge(1e-9),name="a"),
            SphericalShell(.2,.23,FixedNetCharge(-1e-9),center_m=(.01,0.,0.),name="b")
        ))),
        ("intersecting",ElectrostaticProblem(conductors=(
            SphericalShell(.07,.14,FixedNetCharge(1e-9),name="a"),
            SphericalShell(.13,.23,FixedNetCharge(-1e-9),name="b")
        ))),
        ("source_inside_metal",ElectrostaticProblem(
            charges=(PointCharge(1e-9,(0.,0.,.08)),),
            conductors=(SphericalShell(.07,.09,FixedNetCharge(0.),name="a"),)
        )),
    ]
    for label,p in bad:
        if b.supports(p):
            raise AssertionError("invalid nested geometry admitted: "+label)
        try:b.solve(p)
        except UnsupportedProblem:checks.append({"check":"refused "+label,"result":"pass"})
        else:raise AssertionError("invalid nested solved: "+label)
    ext=ExternalSphereBackend()
    p=ElectrostaticProblem(charges=(PointCharge(2e-9,(0.,0.,.9)),),
        conductors=(SolidSphere(1.,FixedNetCharge(0.),name="neutral"),))
    assert not ext.supports(p)
    try:ext.solve(p)
    except UnsupportedProblem:checks.append({"check":"refused source inside solid","result":"pass"})
    else:raise AssertionError("source inside solid admitted")
    return ["nonconcentric","intersecting","source_inside_metal","source_inside_solid"]

def forge(m,name):
    s=m["native_source_apparatus"]
    if name=="net_preserving_inner_outer_faces":
        x=s["p03-single-27"]["before"][1]
        x["inner_surface_charge_c"]+=1e-6
        x["outer_surface_charge_c"]-=1e-6
    elif name=="reverse_signed_gap_field":
        s["p03-single-27"]["gap_field_before_v_m"][0]*=-1
    elif name=="false_initial_field_energy":
        s["p10-linked-13+p10-linked-14"]["radial_energy_before_j"]*=.75
    elif name=="false_postwire_energy":
        s["p03-single-27"]["radial_energy_after_j"]*=2.
    elif name=="false_outer_potential":
        s["p14-numerical-07"]["after"][1]["potential_v"]+=11.
    elif name=="flat_near_far_sigma":
        x=s["p69-cavity-central-vs-shifted"]["native_observations"]
        x[5]["native_value"]=x[4]["native_value"]
        x[6]["native_value"]=x[4]["native_value"]
    elif name=="false_neutral_net":
        s["p09-multiple-27"]["source_givens"]["sphere_net_charge_c"]=1e-9
    elif name=="invalid_source_body_shape":
        s["p03-single-27"]["source_input_bodies"][0]["kind"]="SphericalShell"
    elif name=="split_linked_questions":
        x=s.pop("p10-linked-13+p10-linked-14")
        s["p10-linked-13"]=x
        s["p10-linked-14"]=deepcopy(x)
        m["source_case_count"]=8
    elif name=="fake_wire_time":
        s["p03-single-27"]["kind"]="wire_current_in_time"
    elif name=="false_current_success":
        m["non_success_controls"][0]["native"]=True
    elif name=="false_3d_success":
        m["non_success_controls"][1]["native"]=True
    elif name=="swap_sigma_angles_but_keep_values":
        x=s["p69-cavity-central-vs-shifted"]["native_observations"]
        x[5]["theta_rad"]=math.pi
        x[6]["theta_rad"]=0.0
    elif name=="reassign_nested_shell_observable":
        s["p27-cavity-two-shells"]["native_observations"][3]["conductor"]="outer"
    elif name=="change_source_anchor_string":
        s["p27-cavity-two-shells"]["source_anchor"]="Completely different source"
    else:raise ValueError(name)

def adversarial(m):
    physical=[
        "net_preserving_inner_outer_faces","reverse_signed_gap_field",
        "false_initial_field_energy","false_postwire_energy","false_outer_potential",
        "flat_near_far_sigma","false_neutral_net","invalid_source_body_shape",
        "split_linked_questions","fake_wire_time","false_current_success",
        "false_3d_success",
    ]
    semantic=["swap_sigma_angles_but_keep_values",
              "reassign_nested_shell_observable","change_source_anchor_string"]
    result={}
    for name in physical+semantic:
        bad=deepcopy(m)
        forge(bad,name)
        try:verify(bad)
        except (AssertionError,ValueError,TypeError,KeyError) as exc:
            result[name]={"rejected":True,"message":str(exc)[:240]}
        else:
            result[name]={"rejected":False,"message":"ACCEPTED altered physical/evidence metadata"}
    failed=[x for x in physical if not result[x]["rejected"]]
    if failed:
        raise AssertionError("independent hostile physical mutation escaped: "+str(failed))
    return result

def browser_second_states(root,original_dir):
    from playwright.sync_api import sync_playwright
    checks={}
    shotdir=root/"second-state-screenshots"
    shotdir.mkdir(exist_ok=True)
    names=["p03-single-27","p69-cavity-central-vs-shifted","p09-multiple-27"]
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        try:
            for name in names:
                html=original_dir/(name+".html")
                assert html.exists()
                page=browser.new_page(viewport={"width":1280,"height":800},device_scale_factor=1)
                urls=[];errors=[]
                page.on("request",lambda r: urls.append(r.url)
                        if r.url.startswith(("http://","https://")) else None)
                page.on("pageerror",lambda e:errors.append(str(e)))
                try:
                    page.goto(html.resolve().as_uri(),wait_until="load",timeout=45000)
                    before=page.locator("body").inner_text()
                    page.screenshot(path=str(shotdir/(name+"-first.png")),full_page=True)
                    ranges=page.locator('input[type="range"]')
                    assert ranges.count()>0
                    ranges.first.evaluate("""el => {
                        el.value=el.max;
                        el.dispatchEvent(new Event('input',{bubbles:true}));
                        el.dispatchEvent(new Event('change',{bubbles:true}));
                    }""")
                    page.wait_for_timeout(350)
                    after=page.locator("body").inner_text()
                    page.screenshot(path=str(shotdir/(name+"-last.png")),full_page=True)
                    assert before!=after, "static frame slider did not alter visible state "+name
                    assert not urls and not errors,(name,urls,errors)
                    checks[name]={"frame_changes_visible":True,
                                  "before_header":before[:240],
                                  "after_header":after[:240],
                                  "network_request_count":len(urls),
                                  "page_errors":errors}
                finally:page.close()
        finally:browser.close()
    return checks

def main():
    root=Path("review-artifacts/conductor-m36c-chat-b")
    root.mkdir(parents=True,exist_ok=True)
    originals=root/"original"
    m=run_all(originals)
    verify(m)  # author checker is challenged separately, never sole scientific oracle.
    original_cases(m)
    variants=[unfamiliar_connected(),unfamiliar_nested(),unfamiliar_external()]
    refusals=invalid_geometry_controls()
    hostile=adversarial(m)
    browser=browser_second_states(root,originals)
    result={"reviewer":"Chat B GPT-6, independent R2",
        "source_head":"1f5bd9fcee30f534e15f874c87f8ff0441a62fe8",
        "source_tree":"b31fd1843b57de5403d2a36b2cb86fa1385f659a",
        "original_source_apparatus":7,"original_question_anchors":8,
        "reviewer_si_scalar_checks":checks,"new_native_variants":variants,
        "refused_unsupported":refusals,
        "saved_evidence_hostile_controls":hostile,
        "reviewer_second_state_browser":browser}
    (root/"independent-results.json").write_text(
        json.dumps(result,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    print("REVIEWER SCIENCE PASS: 3 new families,",len(checks),"explicit SI/refusal checks")
    print("ADVERSARIAL controls",json.dumps(hostile,indent=2))
    print("SECOND STATE BROWSER",json.dumps(browser,indent=2))
    if any(not hostile[x]["rejected"] for x in (
        "swap_sigma_angles_but_keep_values","reassign_nested_shell_observable")):
        print("REVIEW FINDING: saved physical observation semantics can be forged "
              "without rejection; report must request correction, not PASS.")
if __name__=="__main__":main()
