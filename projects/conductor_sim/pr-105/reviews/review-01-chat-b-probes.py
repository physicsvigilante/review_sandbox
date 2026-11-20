"""Independent Chat B M40c PR105 reviewer-owned novel scientific and browser probes.

Reviewer authored; not production tests. Execution is pinned by reviewer workflow to
literal conductor_sim HEAD 33a1c677... and Git tree 02688024...
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from dataclasses import replace
import json
import math
from pathlib import Path
import re

import mpmath as mp
from playwright.sync_api import sync_playwright

from conductor_sim.cavity_gauss import GaussCavityAssembly, SealedCavity, CavityCharge
from conductor_sim.model import EPSILON_0, FixedNetCharge, Grounded
from conductor_sim.solver import UnsupportedProblem
from conductor_sim.spherical_multicavity import (
    SphericalSigmaModel, SphericalMetalGeometry, SphericalVoid, NamedSourcePosition,
)
from conductor_sim.spherical_sigma_relocation import (
    StaticSourceRelocation, compare_static_spherical_relocation, relocate_spherical_source,
)
from conductor_sim.spherical_sigma_relocation_viewer import render_static_sigma_comparison
from conductor_sim.spherical_sigma_atlas import _si, _xyz
from tools.m40c_static_reference import check_static_comparison

mp.mp.dps = 125
HEAD = "33a1c677fd9c68404fc64b44496c08fb2c3cee7b"
TREE = "02688024e08f8f0726b5399233e50daa0744c855"
OUTER = (13.2, -8.1, 4.7)
NEUTRAL = (11.0, -8.5, 4.8)
NEGATIVE = (11.45, -8.65, 7.0)   # XY projection overlaps neutral cavity, no 3D overlap
EMPTY = (15.4, -5.7, 3.1)
POSITIVE = (15.2, -9.9, 3.8)
R = .85
base = (.603, -.371, .705)
L = math.hypot(*base)
RAW = tuple((v / L) * (1 + 8e-13) for v in base)
raw_decimal = tuple(mp.mpf(v) for v in RAW)
N = mp.sqrt(sum(v*v for v in raw_decimal))
UNIT = tuple(float(v/N) for v in raw_decimal)
T = (UNIT[1], -UNIT[0], 0.)
T = tuple(v/math.hypot(*T) for v in T)


def p_near(clearance, tangent):
    return tuple(NEUTRAL[i] + R * ((1-clearance)*UNIT[i] + tangent*T[i])
                 for i in range(3))


BEFORE = p_near(1.6e-8, 1e-8)
AFTER = p_near(3.4e-8, 1.5e-8)
# Independent non-axial signed raw rays; normalizer only validates near-unit,
# it must never replace the original input in the near-wall physics.
def normal(x, y, z):
    length = math.hypot(x,y,z)
    return (x/length, y/length, z/length)
RAYS = (RAW, normal(-.45,.35,-.82), normal(.24,-.84,.49),
        normal(-.69,-.22,.69), normal(.52,.18,-.83),
        normal(-.17,.93,.32))


def fixture(grounded=False):
    gauss = GaussCavityAssembly("ReviewedMetal", (
        SealedCavity("SignedNeutral", (
            CavityCharge("P_oblique", 1.7e-9),
            CavityCharge("M_offset", -1.7e-9))),
        SealedCavity("NegativeNet", (
            CavityCharge("M_large", -4e-9),
            CavityCharge("P_small", 1e-9))),
        SealedCavity("EmptyFace"),
        SealedCavity("PositiveNet", (
            CavityCharge("P_center", 2.2e-9),
            CavityCharge("M_lower", -.4e-9))),
    ), Grounded() if grounded else FixedNetCharge(1.3e-9), EPSILON_0)
    geom = SphericalMetalGeometry(OUTER, 9., (
        SphericalVoid("SignedNeutral", NEUTRAL, R, (
            NamedSourcePosition("P_oblique", BEFORE),
            NamedSourcePosition("M_offset", (NEUTRAL[0]-.23,NEUTRAL[1]+.14,NEUTRAL[2]-.11)))),
        SphericalVoid("NegativeNet", NEGATIVE, .95, (
            NamedSourcePosition("M_large",(NEGATIVE[0]+.15, NEGATIVE[1]-.27, NEGATIVE[2]+.16)),
            NamedSourcePosition("P_small",(NEGATIVE[0]-.24, NEGATIVE[1]+.08, NEGATIVE[2]-.17)))),
        SphericalVoid("EmptyFace",EMPTY,.7),
        SphericalVoid("PositiveNet",POSITIVE,.75, (
            NamedSourcePosition("P_center",POSITIVE),
            NamedSourcePosition("M_lower",(POSITIVE[0]+.11,POSITIVE[1]-.26,POSITIVE[2]-.16)))),
    ))
    return SphericalSigmaModel(gauss, geom)


def high_precision_kelvin(Radius, center, sources, ray):
    """Real + exterior Kelvin image normal-E computation, not Poisson kernel."""
    D = mp.mpf
    radius = D(Radius)
    u = [D(v) for v in ray]
    magnitude = mp.sqrt(sum(x*x for x in u))
    u = [x/magnitude for x in u]
    wall = [radius*x for x in u]
    total = D(0)
    for charge, point in sources:
        q = D(charge)
        if q == 0:
            continue
        a = [D(point[i])-D(center[i]) for i in range(3)]
        d2 = sum(x*x for x in a)
        if d2 == 0:
            total += -q/(4*mp.pi*radius**2)
            continue
        d = mp.sqrt(d2)
        real_vector = [wall[i]-a[i] for i in range(3)]
        image = [radius**2 * a[i]/d2 for i in range(3)]
        image_vector = [wall[i]-image[i] for i in range(3)]
        q_image = -q*radius/d
        real_projection = sum(u[i]*real_vector[i] for i in range(3))
        image_projection = sum(u[i]*image_vector[i] for i in range(3))
        real_cube = sum(x*x for x in real_vector)**mp.mpf("1.5")
        image_cube = sum(x*x for x in image_vector)**mp.mpf("1.5")
        total += -(q*real_projection/real_cube + q_image*image_projection/image_cube)/(4*mp.pi)
    return total


def kelvin_face(record, cav, ray):
    byid = {p["source_id"]:p["position_m"] for p in record["source_positions"]}
    charges = {s["source_id"]:s["charge_c"] for s in cav["authored_sources"]}
    sources = [(charge, byid[k]) for k, charge in charges.items()]
    return high_precision_kelvin(record["radius_m"],record["center_m"],sources,ray)


def reject(fn, name, summary):
    try:
        fn()
    except (ValueError, TypeError, UnsupportedProblem, OverflowError, KeyError, AssertionError) as exc:
        summary["rejections"].append({"name":name,"type":type(exc).__name__,"reason":str(exc)[:280]})
        return
    raise AssertionError("UNEXPECTED ACCEPT: "+name)


def scientific_probes(out):
    model = fixture()
    original = model.geometry
    raw = compare_static_spherical_relocation(
        model, StaticSourceRelocation("SignedNeutral","P_oblique",AFTER), rays=RAYS)
    doc = raw.as_dict()
    check_static_comparison(doc)
    assert original == model.geometry
    assert doc["baseline_voids"][0]["source_positions"][0]["position_m"] == list(BEFORE)
    assert doc["revised_voids"][0]["source_positions"][0]["position_m"] == list(AFTER)
    assert doc["baseline_voids"][1:] == doc["revised_voids"][1:]
    assert [r["source_id"] for v in doc["baseline_voids"] for r in v["source_positions"]] == [
        r["source_id"] for v in doc["revised_voids"] for r in v["source_positions"]]
    assert math.hypot(NEGATIVE[0]-NEUTRAL[0], NEGATIVE[1]-NEUTRAL[1]) < R+.95
    assert math.dist(NEGATIVE, NEUTRAL) > R+.95
    assert doc["time_evolution_defined"] is False
    assert doc["original_workbook_items_newly_solved"] == 0
    assert doc["local_3d_fields_or_forces_qualified"] is False
    result = {"reviewer":"fresh standalone Chat B", "head":HEAD,"tree":TREE,
              "geometry":{"cavities":4,"sources":6,"xy_overlapping_disjoint_pair":True,
                          "translated_world_center":list(OUTER), "move_before":list(BEFORE),
                          "move_after":list(AFTER)},
              "oracle_dps":mp.mp.dps,"relative_tolerance":5e-11,
              "rejections":[],"physics":[],"browser":[]}
    for grounded in (False,True):
        candidate = fixture(grounded)
        c = compare_static_spherical_relocation(candidate,
                  StaticSourceRelocation("SignedNeutral","P_oblique",AFTER),rays=RAYS)
        witness = c.as_dict()
        check_static_comparison(witness)
        assert witness["gauss"] == doc["gauss"] if not grounded else witness["gauss"] != doc["gauss"]
        for i, face in enumerate(witness["cavities"]):
            qs = [s["charge_c"] for s in witness["gauss"]["cavities"][i]["authored_sources"]]
            assert abs(face["whole_face_induced_charge_c"]+math.fsum(qs)) < 1e-24
            if i != 0:
                assert all(x["delta_status"]=="unchanged_exact" and x["delta_c_per_m2"]==0
                           for x in face["samples"])
            for j,sample in enumerate(face["samples"]):
                old = kelvin_face(witness["baseline_voids"][i],
                                  witness["gauss"]["cavities"][i],tuple(sample["input_direction"]))
                new = kelvin_face(witness["revised_voids"][i],
                                  witness["gauss"]["cavities"][i],tuple(sample["input_direction"]))
                for actual,expected,label in ((sample["sigma_baseline_c_per_m2"],old,"baseline"),
                                               (sample["sigma_revised_c_per_m2"],new,"revised")):
                    if expected == 0:
                        assert actual == 0, (i,j,label,actual)
                    else:
                        relative = abs((mp.mpf(actual)-expected)/expected)
                        assert relative < mp.mpf("5e-11"),(i,j,label,relative)
                        assert (actual>0) == (expected>0),(i,j,label)
                result["physics"].append({
                    "constraint":"grounded" if grounded else "isolated",
                    "cavity":face["cavity_id"],"ray_index":j,
                    "baseline":sample["sigma_baseline_c_per_m2"],
                    "revised":sample["sigma_revised_c_per_m2"],
                    "delta":sample["delta_c_per_m2"],"delta_status":sample["delta_status"],
                    "independent_baseline":mp.nstr(old,30),
                    "independent_revised":mp.nstr(new,30)})
        if grounded:
            assert witness["outer_uniform_sigma_c_per_m2"]==0
        else:
            assert witness["outer_uniform_sigma_c_per_m2"]!=0
    assert doc["cavities"][0]["whole_face_induced_charge_c"] == 0
    assert doc["cavities"][0]["samples"][0]["sigma_baseline_c_per_m2"] != 0
    assert doc["cavities"][2]["whole_face_induced_charge_c"] == 0
    assert all(s["sigma_baseline_c_per_m2"]==0 for s in doc["cavities"][2]["samples"])
    assert doc["gauss"]["cavities"][1]["induced_inner_face_total_charge_c"] > 0
    assert doc["gauss"]["cavities"][3]["induced_inner_face_total_charge_c"] < 0

    # A binary64 display normal is not an authoritative near-wall physical ray.
    near_face=doc["baseline_voids"][0]; ch=doc["gauss"]["cavities"][0]
    near=kelvin_face(near_face,ch,RAW)
    disp=tuple(doc["cavities"][0]["samples"][0]["unit_normal_display_only"])
    display_near=kelvin_face(near_face,ch,disp)
    raw_vs_display=float(abs((near-display_near)/near))
    assert raw_vs_display>5e-11,raw_vs_display
    result["raw_vs_display_relative_error"]=raw_vs_display
    assert doc["cavities"][0]["samples"][0]["input_direction"]==list(RAW)

    # Separate source revisions are all derived from the unchanged original model.
    alt=p_near(5e-8,-1.4e-8)
    second=relocate_spherical_source(model,StaticSourceRelocation("SignedNeutral","P_oblique",alt))
    assert second.geometry.voids[0].positions[0].position_m==alt
    assert model.geometry==original
    assert raw.revised.geometry.voids[0].positions[0].position_m==AFTER

    for name, cavity, ident, position in (
        ("wrong_owner","NegativeNet","P_oblique",AFTER),
        ("missing_source","SignedNeutral","imaginary",AFTER),
        ("no_op","SignedNeutral","P_oblique",BEFORE),
        ("boolean_coordinate","SignedNeutral","P_oblique",(False,0.,0.)),
        ("nonfinite_coordinate","SignedNeutral","P_oblique",(float("inf"),0.,0.)),
        ("wall_contact","SignedNeutral","P_oblique",(NEUTRAL[0]+R,NEUTRAL[1],NEUTRAL[2])),
    ):
        reject(lambda cavity=cavity, ident=ident, position=position:
            relocate_spherical_source(model,StaticSourceRelocation(cavity,ident,position)),
            name,result)
    reject(lambda:StaticSourceRelocation(False,"P_oblique",AFTER),"boolean_cavity_id",result)
    reject(lambda:StaticSourceRelocation("SignedNeutral",False,AFTER),"boolean_source_id",result)
    # A void that projects as disjoint but touches in 3D must fail at construction.
    reject(lambda:SphericalSigmaModel(model.gauss_assembly,
        replace(model.geometry,voids=(replace(model.geometry.voids[0],radius_m=2.6),)+model.geometry.voids[1:])),
        "unqualified_overlapping_voids",result)

    # Unresolved numerical difference should not masquerade as exact zero.
    c=(2.,-3.,4.); rad=1.
    symmetry=SphericalSigmaModel(
        GaussCavityAssembly("Separate",(
            SealedCavity("Sym", (CavityCharge("Q",2e-9),)),),
            FixedNetCharge(.2e-9),EPSILON_0),
        SphericalMetalGeometry(c,4.,(
            SphericalVoid("Sym",c,rad,(
                NamedSourcePosition("Q",(c[0]+.29,c[1],c[2])),)),)))
    sym=compare_static_spherical_relocation(symmetry,
        StaticSourceRelocation("Sym","Q",(c[0]-.29,c[1],c[2])),
        rays=((0.,1.,0.),(1.,0.,0.))).as_dict()
    assert sym["cavities"][0]["samples"][0]["delta_status"]=="unresolved_numerical_difference"
    assert sym["cavities"][0]["samples"][0]["delta_c_per_m2"] is None
    check_static_comparison(sym)
    result["unresolved_near_cancellation"]=True

    changes=[
        ("source_role",("source_role",),"claimed_source_workbook"),
        ("time_claim",("time_evolution_defined",),True),
        ("original_item_count",("original_workbook_items_newly_solved",),1),
        ("chronology",("no_chronology",),"motion elapsed and current"),
        ("field_claim",("local_3d_fields_or_forces_qualified",),True),
        ("unit",("units","surface_density"),"V/m"),
        ("source_id",("relocation","source_id"),"M_offset"),
        ("owner",("relocation","cavity_id"),"NegativeNet"),
        ("original_xyz",("relocation","original_position_m",0),123.0),
        ("revised_xyz",("relocation","revised_position_m",2),-999.0),
        ("physical_source_charge",("gauss","cavities",0,"authored_sources",0,"charge_c"),-1.7e-9),
        ("baseline_xyz",("baseline_voids",0,"source_positions",0,"position_m",1),555.0),
        ("revised_xyz_witness",("m40a_v2_witness_records","revised",0,"voids",0,"source_positions",0,"position_m",0),-1e2),
        ("radius",("revised_voids",1,"radius_m"),14.0),
        ("center",("baseline_voids",0,"center_m",2),-999.0),
        ("raw_ray",("cavities",0,"samples",0,"input_direction",2),0.3),
        ("display_only_unit",("cavities",0,"samples",0,"unit_normal_display_only",1),0.0),
        ("baseline_sigma",("cavities",0,"samples",0,"sigma_baseline_c_per_m2"),False),
        ("revised_sigma",("cavities",0,"samples",0,"sigma_revised_c_per_m2"),0.),
        ("delta_value",("cavities",0,"samples",0,"delta_c_per_m2"),True),
        ("delta_status",("cavities",0,"samples",0,"delta_status"),"unchanged_exact"),
        ("gauss_face",("cavities",1,"whole_face_induced_charge_c"),999.),
        ("outer_sigma",("outer_uniform_sigma_c_per_m2",),999.),
        ("boolean_zero",("m40a_v2_witness_records","baseline",2,"samples",0,"sigma_c_per_m2"),False),
        ("witness_physical_ray",("m40a_v2_witness_records","baseline",0,"samples",0,"input_direction",0),False),
    ]
    for name,path,value in changes:
        d=deepcopy(doc);node=d
        for key in path[:-1]:node=node[key]
        node[path[-1]]=value
        reject(lambda d=d:check_static_comparison(d),"tamper_"+name,result)
    for name,edit in (
        ("omit_late_empty",lambda d:d["cavities"].pop(2)),
        ("duplicate_late",lambda d:d["cavities"].append(deepcopy(d["cavities"][-1]))),
        ("reorder_rows",lambda d:d["cavities"].reverse()),
        ("omit_outer_witness",lambda d:d["m40a_v2_witness_records"]["revised"].pop()),
        ("duplicate_empty_witness",lambda d:d["m40a_v2_witness_records"]["revised"].insert(2,deepcopy(d["m40a_v2_witness_records"]["revised"][2]))),
        ("extra_current_claim",lambda d:d.update({"grounding_current_c_per_s":1})),
    ):
        d=deepcopy(doc);edit(d)
        reject(lambda d=d:check_static_comparison(d),"tamper_"+name,result)
    out.mkdir(parents=True,exist_ok=True)
    (out/"reviewer-novel-physical-record.json").write_text(json.dumps(doc,indent=2,allow_nan=False)+"\n")
    assert len(result["physics"])==4*6*2
    return raw, doc, result


def browser_probes(comp, doc, result, out):
    html=render_static_sigma_comparison(comp)
    pagepath=out/"reviewer-novel-comparison.html"
    pagepath.write_text(html,encoding="utf-8")
    ids=re.findall(r'\bid="([^"]+)"',html)
    assert len(ids)==len(set(ids)),("duplicate rendered IDs",ids)
    logs=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        for js,width in ((True,1280),(False,1280),(True,390),(False,390)):
            context=browser.new_context(viewport={"width":width,"height":880},
                                         java_script_enabled=js)
            page=context.new_page()
            requested=[];errors=[];console=[]
            page.on("request",lambda r:requested.append(r.url))
            page.on("pageerror",lambda e:errors.append(str(e)))
            page.on("console",lambda e:console.append(e.text))
            page.goto(pagepath.resolve().as_uri(),wait_until="load")
            assert page.title()=="M40c static spherical-source comparison"
            assert page.locator('svg[role="img"]').count()==2
            assert page.locator("body").inner_text().count("one static equilibrium")==2
            assert page.locator("#m40c-source").inner_text()=="P_oblique"
            assert "teacher" in page.locator("#m40c-role").inner_text().lower()
            assert "STATIC" in page.locator("#m40c-no-chronology").inner_text()
            text=page.locator("body").inner_text()
            assert _xyz(BEFORE) in text and _xyz(AFTER) in text
            assert "whole-face Gauss" in text and "point samples" in text
            assert "No arbitrary 3D field" in text
            assert page.locator('tr[id^="m40c-"]').count()==24
            for cav in doc["cavities"]:
                for j,sample in enumerate(cav["samples"]):
                    row=page.locator(f"#m40c-{cav['cavity_id']}-{j}")
                    assert row.count()==1
                    actual=row.inner_text()
                    assert _si(sample["sigma_baseline_c_per_m2"],"C/m²") in actual
                    assert _si(sample["sigma_revised_c_per_m2"],"C/m²") in actual
                    assert repr(tuple(sample["input_direction"])) in actual
                    if sample["delta_c_per_m2"] is None:
                        assert "Unresolved numerical" in actual
                    else:
                        assert _si(sample["delta_c_per_m2"],"C/m²") in actual
            outer=doc["outer_sphere"]
            for panel,label in ((0,"baseline"),(1,"revised")):
                for i,cav in enumerate(doc[label+"_voids"]):
                    circle=page.locator(f"#m40c-panel-{panel}-void-{i}")
                    assert circle.count()==1
                    expected=(425+(cav["center_m"][0]-outer["center_m"][0])*375/outer["radius_m"],
                              425-(cav["center_m"][1]-outer["center_m"][1])*375/outer["radius_m"],
                              375*cav["radius_m"]/outer["radius_m"])
                    actual=tuple(float(circle.get_attribute(k)) for k in ("cx","cy","r"))
                    assert all(abs(x-y)<1e-9 for x,y in zip(expected,actual)),(panel,i,actual,expected)
                    positions={s["source_id"]:s["position_m"] for s in cav["source_positions"]}
                    for j,s in enumerate(doc["gauss"]["cavities"][i]["authored_sources"]):
                        marker=page.locator(f"#m40c-panel-{panel}-source-{i}-{j}")
                        assert marker.count()==1
                        assert s["source_id"] in marker.locator("title").text_content()
                        pos=positions[s["source_id"]]
                        expectx=425+(pos[0]-outer["center_m"][0])*375/outer["radius_m"]
                        expecty=425-(pos[1]-outer["center_m"][1])*375/outer["radius_m"]
                        assert abs(float(marker.get_attribute("cx"))-expectx)<1e-9
                        assert abs(float(marker.get_attribute("cy"))-expecty)<1e-9
            assert all(url.startswith("file://") for url in requested),requested
            assert not errors,errors
            mobile_scroll=False
            if js and width==390:
                info=page.locator(".table-wrap").evaluate_all(
                    "(els)=>els.map(e=>({overflow:getComputedStyle(e).overflowX,scroll:e.scrollWidth,client:e.clientWidth}))")
                assert all(r["overflow"]=="auto" for r in info),info
                mobile_scroll=any(r["scroll"]>r["client"] for r in info)
                if mobile_scroll:
                    page.locator(".table-wrap").first.evaluate("(e)=>e.scrollLeft=e.scrollWidth")
            filename=f"reviewer-novel-{'js-on' if js else 'js-off'}-{width}px.png"
            page.screenshot(path=str(out/filename),full_page=True)
            entry={"js":js,"viewport_width":width,"all_original_ids_unique":True,
                   "both_panels_geometry_checked":True,
                   "source_markers":6,"sample_rows":24,
                   "external_requests":0,"mobile_overflow_scroll_present":mobile_scroll,
                   "console":console,"page_errors":errors,"requests":requested}
            result["browser"].append(entry)
            context.close()
        # script-src 'none' rejects hostile inline JavaScript in amended HTML
        hostile=out/"reviewer-csp-script-attack.html"
        hostile.write_text(html.replace("</body>",
             '<script>window.__M40C_SCRIPT_ATTACK=true</script></body>'),encoding="utf-8")
        ctx=browser.new_context(java_script_enabled=True)
        page=ctx.new_page();csp_console=[]
        page.on("console",lambda e:csp_console.append(e.text))
        page.goto(hostile.resolve().as_uri(),wait_until="load")
        assert not page.evaluate("!!window.__M40C_SCRIPT_ATTACK")
        result["script_injection_blocked"]=True
        result["script_console"]=csp_console
        ctx.close()
        # Edited HTML and malicious inline CSS are NOT authenticated by a JSON checker.
        css_edit=out/"reviewer-edited-css-hides-notice.html"
        css_edit.write_text(html.replace("</head>",
            "<style>#m40c-no-chronology{display:none!important}</style></head>"),
            encoding="utf-8")
        ctx=browser.new_context(java_script_enabled=True)
        page=ctx.new_page();page.goto(css_edit.resolve().as_uri(),wait_until="load")
        assert not page.locator("#m40c-no-chronology").is_visible()
        result["css_tamper_can_hide_truthful_notice"]=True
        ctx.close()
        source_text=_xyz(AFTER)
        assert source_text in html
        false_html=html.replace(source_text,"(999, 888, 777) m")
        edited=out/"reviewer-edited-html-false-position.html"
        edited.write_text(false_html,encoding="utf-8")
        ctx=browser.new_context(java_script_enabled=False)
        page=ctx.new_page();page.goto(edited.resolve().as_uri(),wait_until="load")
        assert "(999, 888, 777) m" in page.locator("body").inner_text()
        assert check_static_comparison(doc)["status"]=="PASS"
        result["edited_html_not_authenticated_by_json_checker"]=True
        ctx.close()
        browser.close()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    comparison,doc,result=scientific_probes(args.out)
    (args.out/"reviewer-science-summary.json").write_text(
        json.dumps(result,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    browser_probes(comparison,doc,result,args.out)
    result["status"]="PASS"
    (args.out/"reviewer-results.json").write_text(
        json.dumps(result,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"reviewed":HEAD,
        "oracle_dps":result["oracle_dps"],"physical_probes":len(result["physics"]),
        "adversarial_rejections":len(result["rejections"]),
        "browser_modes":len(result["browser"]),
        "raw_vs_display_relative_error":result["raw_vs_display_relative_error"],
        "css_truth_hiding_possible":result["css_tamper_can_hide_truthful_notice"]},
        sort_keys=True))


if __name__=="__main__":main()
