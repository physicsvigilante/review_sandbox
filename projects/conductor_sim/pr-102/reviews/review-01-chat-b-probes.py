"""Reviewer-owned M40b experiment; independent Kelvin field, original geometry and Chromium."""
from __future__ import annotations

import argparse
from copy import deepcopy
from dataclasses import replace
from decimal import Decimal, localcontext
from html import escape
import json
from math import atan2, cos, degrees, fsum, hypot, isclose, pi, sin
from pathlib import Path
import re
import sys
import traceback

PI_110 = Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651")
EXPECTED_HEAD = "0191ced5c49a1a5d02c9a897867ceca951fb9aca"
EXPECTED_TREE = "5ea6098d463eec12fbc184ab3a6fca2f27699e9a"


def independent_kelvin_sigma(radius, center, charged_points, input_ray):
    """100-digit real point-charge plus independently constructed Kelvin image E_n.

    The physical metal boundary faces *into* its cavity, hence sigma=-eps E.n.
    Input direction is normalized from the original exact binary64 coordinates.
    Does not call M40a, M40b or bundled independent oracle.
    """
    with localcontext() as ctx:
        ctx.prec = 110
        D = Decimal.from_float
        R = D(radius)
        raw = [D(x) for x in input_ray]
        norm = sum((x*x for x in raw), Decimal(0)).sqrt()
        n = [x / norm for x in raw]
        x = [R * v for v in n]
        total = Decimal(0)
        for charge, world_position in charged_points:
            p = [D(world_position[i])-D(center[i]) for i in range(3)]
            rr = sum((z*z for z in p), Decimal(0))
            if rr == 0:
                total -= D(charge) / (4*PI_110*R*R)
                continue
            distance = rr.sqrt()
            image_pos = [R*R*z/rr for z in p]
            image_q = -D(charge)*R/distance
            a = [x[i]-p[i] for i in range(3)]
            b = [x[i]-image_pos[i] for i in range(3)]
            a2 = sum((v*v for v in a), Decimal(0))
            b2 = sum((v*v for v in b), Decimal(0))
            electric = [D(charge)*a[i]/(a2*a2.sqrt()) +
                        image_q*b[i]/(b2*b2.sqrt()) for i in range(3)]
            total -= sum((n[i]*electric[i] for i in range(3)), Decimal(0))/(4*PI_110)
        return float(total)


def display_normal_independent(raw):
    with localcontext() as ctx:
        ctx.prec = 110
        r = [Decimal.from_float(x) for x in raw]
        norm = sum((x*x for x in r), Decimal(0)).sqrt()
        return tuple(float(x/norm) for x in r)


def expected_si(x, unit):
    assert type(x) in (int, float)
    if x == 0:
        return "0 " + unit
    return ("+" if x > 0 else "−") + repr(abs(x)) + " " + unit


def approx_exact(a, b, label, rel=5e-11, absolute=1e-23):
    if abs(a-b) > max(absolute, rel*abs(b)):
        raise AssertionError(f"{label}: actual {a!r} versus independent {b!r}, rel {abs(a-b)/max(abs(b),1e-300):.4g}")


def independent_geometry_check(doc):
    outer = doc["outer_sphere"]
    outer_c, outer_r = outer["center_m"], outer["radius_m"]
    all_ids = set()
    centers = []
    for row in doc["cavities"]:
        assert row["cavity_id"] not in all_ids
        all_ids.add(row["cavity_id"])
        center, rad = row["center_m"], row["radius_m"]
        assert hypot(*(center[i]-outer_c[i] for i in range(3)))+rad < outer_r
        assert all(hypot(*(center[i]-prev[0][i] for i in range(3))) > rad+prev[1] for prev in centers)
        centers.append((center,rad))
        for source in row["sources"]:
            assert source["source_id"] not in all_ids
            all_ids.add(source["source_id"])
            assert hypot(*(source["position_m"][i]-center[i] for i in range(3))) < rad*(1-1e-8)
    return len(all_ids)


def build_new_model():
    from conductor_sim.cavity_gauss import CavityCharge, SealedCavity, GaussCavityAssembly
    from conductor_sim.model import FixedNetCharge, EPSILON_0
    from conductor_sim.spherical_multicavity import (
        SphericalMetalGeometry, SphericalVoid, NamedSourcePosition, SphericalSigmaModel
    )
    c1 = (1.6, -.2, -1.9)
    c2 = (1.6, -.2, 1.7)  # XY coincidence, but 3D cavity separation 3.6m
    c3 = (-1.4, -1.5, .7)
    basis = (.37, -.52, .77)
    n = tuple(v/hypot(*basis) for v in basis)
    tangent = (-n[1],n[0],0.)
    t = tuple(v/hypot(*tangent) for v in tangent)
    radius = .9
    near = tuple(c1[i] + radius*((1-1.5e-8)*n[i] + .7e-8*t[i]) for i in range(3))
    far = tuple(c1[i]+v for i,v in enumerate((-.34,.22,-.23)))
    g = GaussCavityAssembly(
        "Metal_Translated_3D", (
            SealedCavity("StackedLower",(
                CavityCharge("lower_plus_nearwall", 3.1e-9),
                CavityCharge("lower_minus_offaxis", -3.1e-9),
            )),
            SealedCavity("StackedUpper",(
                CavityCharge("upper_plus", 1.7e-9),
                CavityCharge("upper_minus", -4.0e-9),
            )),
            SealedCavity("OffAxisEmpty"),
        ), FixedNetCharge(8.1e-10), EPSILON_0,
    )
    geom = SphericalMetalGeometry((1.2,-.9,.4),6.5,(
        SphericalVoid("StackedLower",c1,radius,(
            NamedSourcePosition("lower_plus_nearwall",near),
            NamedSourcePosition("lower_minus_offaxis",far),
        )),
        SphericalVoid("StackedUpper",c2,.85,(
            NamedSourcePosition("upper_plus",(1.79,-.39,1.95)),
            NamedSourcePosition("upper_minus",(1.26,.02,1.53)),
        )),
        SphericalVoid("OffAxisEmpty",c3,.5),
    ))
    return SphericalSigmaModel(g,geom)


def raw_directions():
    # Authored rays include north/south, full-hemisphere quadrature, and an
    # almost-unit oblique near-wall ray with meaningful +z contribution.
    directions = []
    for row in range(4):
        for col in range(6):
            theta = pi * (row+.5) / 4
            phi = 2*pi*(col+.5)/6
            directions.append((sin(theta)*cos(phi),sin(theta)*sin(phi),cos(theta)))
    nearwall_raw = (.36996300554937117,-.5199480077991163,.7699230115486914)
    assert abs(hypot(*nearwall_raw)-1) < 1e-12
    directions.append(nearwall_raw)
    return tuple(directions)


def physics_and_integrity(out):
    from conductor_sim.model import Grounded, FixedNetCharge
    from conductor_sim.cavity_gauss import CavityCharge
    from conductor_sim.spherical_multicavity import NamedSourcePosition, solve_spherical_sigma
    from conductor_sim.spherical_sigma_atlas import surface_atlas_manifest, render_surface_atlas
    from tools.m40b_spherical_atlas_reference import check_manifest

    original = build_new_model()
    grounded = replace(original, gauss_assembly=replace(original.gauss_assembly,constraint=Grounded()))
    ia = solve_spherical_sigma(original)
    ga = solve_spherical_sigma(grounded)
    directions = raw_directions()
    doc = surface_atlas_manifest(ia,ga,directions=directions)
    html = render_surface_atlas(ia,ga,directions=directions)
    assert doc["source_role"] == "teacher_hypothetical_spherical_multicavity_only"
    assert doc["original_workbook_items_newly_solved"] == 0
    assert doc["time_evolution_defined"] is False
    assert len(doc["cavities"]) == 3
    assert len(doc["cavities"][0]["samples"]) == 25
    assert all(len(row["samples"]) == 25 for row in doc["cavities"])
    assert doc["cavities"][0]["center_m"][:2] == doc["cavities"][1]["center_m"][:2]
    assert doc["cavities"][0]["center_m"][2] != doc["cavities"][1]["center_m"][2]
    # The 3D distance is much larger than either radius sum.
    assert abs(doc["cavities"][0]["center_m"][2]-
               doc["cavities"][1]["center_m"][2]) > sum(
               row["radius_m"] for row in doc["cavities"][:2])
    count_ids = independent_geometry_check(doc)
    assert count_ids == 7  # 3 cavities and 4 separately named charges

    samples_checked, worst_relative = 0, 0.0
    signs = {}
    numeric_evidence = []
    for row in doc["cavities"]:
        rho = [sample["isolated_sigma_c_per_m2"] for sample in row["samples"]]
        signs[row["cavity_id"]] = {"positive":sum(v>0 for v in rho),
                                   "negative":sum(v<0 for v in rho),
                                   "zero":sum(v==0 for v in rho)}
        charges = [(src["charge_c"],src["position_m"]) for src in row["sources"]]
        total = fsum(q for q,_ in charges)
        approx_exact(row["source_total_charge_c"],total,"authored cavity charge",rel=1e-14)
        approx_exact(row["whole_inner_face_charge_c"],-total,"whole face Gauss",rel=1e-14)
        for j,sample in enumerate(row["samples"]):
            direction = tuple(sample["input_direction"])
            ref = independent_kelvin_sigma(row["radius_m"],row["center_m"],charges,direction)
            for state in ("isolated","grounded"):
                measured = sample[f"{state}_sigma_c_per_m2"]
                approx_exact(measured,ref,f"{row['cavity_id']} point {j} {state}")
                if ref:
                    worst_relative = max(worst_relative,abs(measured-ref)/abs(ref))
                samples_checked+=1
            dn = display_normal_independent(direction)
            assert list(dn) == sample["unit_normal"]
            th = degrees(atan2(hypot(direction[0],direction[1]),direction[2]))
            ph = degrees(atan2(direction[1],direction[0])) % 360
            approx_exact(sample["theta_deg_display"],th,"theta",rel=1e-13,absolute=1e-12)
            approx_exact(sample["phi_deg_display"],ph,"phi",rel=1e-13,absolute=1e-12)
            numeric_evidence.append({"surface":row["cavity_id"],"ray":j,
                "sigma_from_100digit_kelvin":ref,
                "rendered_manifest_sigma":sample["isolated_sigma_c_per_m2"],
                "raw_direction":direction})
    assert signs["StackedLower"]["negative"] > 0 and signs["StackedLower"]["positive"] > 0
    assert signs["OffAxisEmpty"]["zero"] == 25
    assert signs["StackedUpper"]["positive"]>0 or signs["StackedUpper"]["negative"]>0
    qout = fsum([8.1e-10, 3.1e-9,-3.1e-9,1.7e-9,-4.0e-9])
    approx_exact(doc["outer"]["isolated_whole_face_charge_c"],qout,"isolated outer Gauss",rel=1e-14)
    assert doc["outer"]["grounded_whole_face_charge_c"] == 0
    assert doc["outer"]["grounded_uniform_sigma_c_per_m2"] == 0
    approx_exact(doc["outer"]["isolated_uniform_sigma_c_per_m2"],
                 qout/(4*pi*6.5**2),"uniform isolated outer sigma",rel=1e-14)
    assert doc["outer"]["isolated_whole_face_charge_c"] != 0

    near = doc["cavities"][0]["samples"][-1]
    assert near["input_direction"] != near["unit_normal"]
    charges = [(s["charge_c"],s["position_m"]) for s in doc["cavities"][0]["sources"]]
    raw_sigma = independent_kelvin_sigma(.9,doc["cavities"][0]["center_m"],charges,near["input_direction"])
    rounded_sigma = independent_kelvin_sigma(.9,doc["cavities"][0]["center_m"],charges,near["unit_normal"])
    rounded_relative_delta = abs(raw_sigma-rounded_sigma)/abs(raw_sigma)
    assert rounded_relative_delta > 1e-11, rounded_relative_delta
    approx_exact(near["isolated_sigma_c_per_m2"],raw_sigma,"oblique almost-unit raw near-wall",rel=5e-11)

    # Requalify genuine source relocation as another independently solved static case.
    lower = original.geometry.voids[0]
    p0 = lower.positions[0]
    new_pos = tuple(lower.center_m[i] + .78*(p0.position_m[i]-lower.center_m[i]) for i in range(3))
    moved = replace(lower,positions=(replace(p0,position_m=new_pos),)+lower.positions[1:])
    moved_model = replace(original,geometry=replace(
        original.geometry,voids=(moved,)+original.geometry.voids[1:]))
    relocated = solve_spherical_sigma(moved_model)
    measured_relocated = relocated.inner_surface_charge_density("StackedLower",directions[-1])
    baseline = near["isolated_sigma_c_per_m2"]
    assert abs(measured_relocated-baseline) > abs(baseline)*.01
    moved_grounded = replace(moved_model,gauss_assembly=replace(moved_model.gauss_assembly,constraint=Grounded()))
    moved_doc = surface_atlas_manifest(relocated,solve_spherical_sigma(moved_grounded),directions=(directions[-1],))
    check_manifest(moved_doc)
    assert moved_doc["cavities"][0]["samples"][0]["isolated_sigma_c_per_m2"] == measured_relocated

    checked = check_manifest(doc)
    assert checked["cavities_checked"] == 3
    assert checked["signed_inner_samples_verified_by_images"] == 150
    out.joinpath("new-arrangement.json").write_text(json.dumps(doc,indent=2,ensure_ascii=False,allow_nan=False),encoding="utf-8")
    out.joinpath("new-arrangement.html").write_text(html,encoding="utf-8")
    out.joinpath("relocation.json").write_text(json.dumps(moved_doc,indent=2,allow_nan=False),encoding="utf-8")
    out.joinpath("independent-kelvin-numeric.json").write_text(json.dumps(
        numeric_evidence,indent=2,allow_nan=False),encoding="utf-8")

    # Independent refusal checks, including original and witness-layer attacks.
    cases = [
        ("visible source id",("cavities",0,"sources",0,"source_id"),"forged"),
        ("visible source charge Boolean",("cavities",0,"sources",0,"charge_c"),False),
        ("visible source z",("cavities",0,"sources",0,"position_m",2),71.0),
        ("visible cavity xy",("cavities",0,"center_m",0),3.5),
        ("visible cavity z",("cavities",1,"center_m",2),-1.9),
        ("visible cavity radius",("cavities",1,"radius_m"),.45),
        ("visible whole face Gauss",("cavities",0,"whole_inner_face_charge_c"),1e-9),
        ("visible sigma",("cavities",0,"samples",24,"isolated_sigma_c_per_m2"),0.0),
        ("visible raw ray",("cavities",0,"samples",24,"input_direction",0),1.0),
        ("visible normal",("cavities",0,"samples",24,"unit_normal",0),.123),
        ("visible theta",("cavities",0,"samples",0,"theta_deg_display"),99.0),
        ("visible phi",("cavities",0,"samples",0,"phi_deg_display"),212.0),
        ("outer whole face",("outer","isolated_whole_face_charge_c"),False),
        ("outer grounded sigma",("outer","grounded_uniform_sigma_c_per_m2"),2.0),
        ("unit",("units","surface_density"),"C"),
        ("source role",("source_role",),"original_JEE"),
        ("no-time role flag",("time_evolution_defined",),True),
        ("no 2D field role",("projection_is_2d_field_or_cross_section",),True),
        ("v2 raw ray",("native_m40a_v2_witness_records","isolated",0,"samples",24,"input_direction",2),False),
        ("v2 source position z",("native_m40a_v2_witness_records","isolated",0,"voids",0,"source_positions",0,"position_m",2),99.),
        ("v2 sigma",("native_m40a_v2_witness_records","isolated",0,"samples",24,"sigma_c_per_m2"),0.0),
        ("v2 unit normal",("native_m40a_v2_witness_records","isolated",0,"samples",24,"unit_normal",0),0.123),
        ("nonfinite visible sigma",("cavities",0,"samples",24,"isolated_sigma_c_per_m2"),float("nan")),
        ("cancelled charged source",("cavities",0,"sources",0,"charge_c"),-3.1e-9),
    ]
    refusals = []
    for name,path,value in cases:
        tampered = deepcopy(doc)
        field = tampered
        for key in path[:-1]:
            field = field[key]
        field[path[-1]] = value
        try:
            check_manifest(tampered)
        except (ValueError,TypeError,KeyError,ArithmeticError) as err:
            refusals.append({"attack":name,"refused":True,"exception":type(err).__name__,"detail":str(err)[:180]})
        else:
            raise AssertionError(f"manifest checker wrongly accepted attack {name}")

    bad = deepcopy(doc)
    bad["native_m40a_v2_witness_records"]["isolated"][0] = deepcopy(
        bad["native_m40a_v2_witness_records"]["grounded"][0])
    try:
        check_manifest(bad)
    except (ValueError,TypeError,KeyError,ArithmeticError) as err:
        refusals.append({"attack":"constraint-swapped witness","refused":True,"detail":str(err)[:180]})
    else:
        raise AssertionError("wrong state witness accepted")

    other_invalid = [
        ("boolean ray",lambda:surface_atlas_manifest(ia,ga,directions=((False,0.,0.),))),
        ("nan ray",lambda:surface_atlas_manifest(ia,ga,directions=((float("nan"),0.,0.),))),
        ("unqualified ray",lambda:surface_atlas_manifest(ia,ga,directions=((2.,0.,0.),))),
        ("oversized rays",lambda:surface_atlas_manifest(ia,ga,directions=((1.,0.,0.),)*49)),
        ("HTML source identity",lambda:CavityCharge("<script>alert(1)</script>",1e-9)),
        ("HTML geometry identity",lambda:NamedSourcePosition("x<svg>",(0.,0.,0.))),
        ("Boolean charge",lambda:CavityCharge("new",False)),
        ("nonfinite charge",lambda:CavityCharge("new",float("inf"))),
        ("impossible source containment",lambda:replace(original.geometry.voids[0],
          positions=(replace(original.geometry.voids[0].positions[0],position_m=(100.,100.,100.)),)+
          original.geometry.voids[0].positions[1:])),
    ]
    # Last entry constructs a void but does not validate placement until model
    # rebuild; handle it as a full model constructor below.
    other_invalid.pop()
    for name,action in other_invalid:
        try:
            action()
        except (ValueError,TypeError,ArithmeticError,Exception) as err:
            refusals.append({"attack":name,"refused":True,"exception":type(err).__name__,"detail":str(err)[:160]})
        else:
            raise AssertionError(f"native M40b admitted invalid {name}")
    bad_void = replace(original.geometry.voids[0],
        positions=(replace(original.geometry.voids[0].positions[0],position_m=(100.,100.,100.)),)+original.geometry.voids[0].positions[1:])
    try:
        replace(original,geometry=replace(original.geometry,voids=(bad_void,)+original.geometry.voids[1:]))
    except (ValueError,TypeError,Exception) as err:
        refusals.append({"attack":"impossible source containment","refused":True,"exception":type(err).__name__})
    else:
        raise AssertionError("outside-cavity source accepted")

    overlap_void = replace(original.geometry.voids[1],center_m=(1.6,-.2,-1.6))
    try:
        replace(original,geometry=replace(original.geometry,
            voids=(original.geometry.voids[0],overlap_void,original.geometry.voids[2])))
    except (ValueError,TypeError,Exception) as err:
        refusals.append({"attack":"physically overlapping voids","refused":True,"exception":type(err).__name__})
    else:
        raise AssertionError("overlapping true 3D cavities accepted")

    # Static HTML tamper remains outside JSON-only stdlib verifier's input contract:
    # explicitly record and report it; do not mislabel as a refusal.
    original_number = expected_si(near["isolated_sigma_c_per_m2"],"C/m²")
    forged_html = html.replace(escape(original_number), "9999 C/m²",1)
    assert forged_html != html and "9999 C/m²" in forged_html
    out.joinpath("forged-visible-html.html").write_text(forged_html,encoding="utf-8")
    assert check_manifest(doc)["signed_inner_samples_verified_by_images"] == 150
    out.joinpath("hostile-refusals.json").write_text(json.dumps(refusals,indent=2),encoding="utf-8")
    return {"source_identities_verified":count_ids,"samples_scientifically_checked":samples_checked,
            "worst_kelvin_relative_error":worst_relative,
            "nearwall_raw_relative_change_if_display_normal_substituted":rounded_relative_delta,
            "nearwall_raw_sigma":raw_sigma,
            "nearwall_display_normal_sigma":rounded_sigma,
            "signed_observation_counts":signs,
            "native_requalified_source_relocation":True,
            "manifest_hostile_refusals":len(refusals),
            "externally_forged_html_is_not_checked_by_json_only_verifier":True,
            "outer_isolated_charge_c":qout}


def browser_tests(out, science):
    from playwright.sync_api import sync_playwright
    doc = json.loads(out.joinpath("new-arrangement.json").read_text(encoding="utf-8"))
    url = out.joinpath("new-arrangement.html").resolve().as_uri()
    checks = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        for js,width,height in ((True,1280,820),(False,1280,820),(True,390,844),(False,390,844)):
            ctx = browser.new_context(viewport={"width":width,"height":height},
                                      java_script_enabled=js,device_scale_factor=1)
            page = ctx.new_page()
            requests = []
            page.on("request",lambda request:requests.append(request.url))
            page.goto(url,wait_until="load")
            assert page.locator("#m40b-warning").is_visible()
            assert "XY OVERLAP DOES NOT PROVE 3D CONTACT" in page.locator("#m40b-warning").inner_text()
            assert "0 newly solved original JEE" in page.locator("#m40b-role").inner_text()
            assert "two independent static equilibria" in page.locator("header").inner_text()
            assert page.locator('svg[role="img"]').count() == 1
            assert page.locator("circle[id^=m40b-void-]").count() == 3
            assert page.locator("circle[id^=m40b-source-]").count() == 4
            assert page.locator('[id^=m40b-tile-]').count() == 75
            assert page.locator("#m40b-q-outer-isolated").inner_text() == expected_si(
                   doc["outer"]["isolated_whole_face_charge_c"],"C")
            assert page.locator("#m40b-q-outer-grounded").inner_text() == "0 C"
            outer=doc["outer_sphere"]
            for i,cav in enumerate(doc["cavities"]):
                block = page.locator(f"#m40b-cavity-{i}")
                assert cav["cavity_id"] in block.inner_text()
                for v in cav["center_m"]:
                    assert repr(v) in block.inner_text()
                scale = 375/outer["radius_m"]
                x = 425+(cav["center_m"][0]-outer["center_m"][0])*scale
                y = 425-(cav["center_m"][1]-outer["center_m"][1])*scale
                svg = page.locator(f"#m40b-void-{i}")
                assert abs(float(svg.get_attribute("cx"))-x) < 1e-10
                assert abs(float(svg.get_attribute("cy"))-y) < 1e-10
                assert abs(float(svg.get_attribute("r"))-cav["radius_m"]*scale) < 1e-10
                assert svg.get_attribute("stroke-dasharray") is not None
                for j,src in enumerate(cav["sources"]):
                    circle=page.locator(f"#m40b-source-{i}-{j}")
                    xx=425+(src["position_m"][0]-outer["center_m"][0])*scale
                    yy=425-(src["position_m"][1]-outer["center_m"][1])*scale
                    assert abs(float(circle.get_attribute("cx"))-xx) < 1e-10
                    assert abs(float(circle.get_attribute("cy"))-yy) < 1e-10
                    assert src["source_id"] in block.inner_text()
                    assert expected_si(src["charge_c"],"C") in block.inner_text()
                    assert repr(src["position_m"][2]) in block.inner_text()
                for j,sample in enumerate(cav["samples"]):
                    tile = page.locator(f"#m40b-tile-{i}-{j}")
                    text = tile.inner_text()
                    assert expected_si(sample["isolated_sigma_c_per_m2"],"C/m²") in text
                    assert "Grounded: "+expected_si(sample["grounded_sigma_c_per_m2"],"C/m²") in text
                    assert "θ≈{:.3f}°, φ≈{:.3f}°".format(
                        sample["theta_deg_display"],sample["phi_deg_display"]) in text
                    for v in sample["input_direction"]:
                        assert repr(v) in text
                    klass=tile.get_attribute("class")
                    signed=sample["isolated_sigma_c_per_m2"]
                    expected_class="negative" if signed<0 else "positive" if signed>0 else "zero"
                    assert expected_class in klass.split()
            assert float(page.locator("#m40b-void-0").get_attribute("cx")) == float(
                         page.locator("#m40b-void-1").get_attribute("cx"))
            assert float(page.locator("#m40b-void-0").get_attribute("cy")) == float(
                         page.locator("#m40b-void-1").get_attribute("cy"))
            assert page.locator("#m40b-cavity-0").is_visible()
            assert all(u.startswith("file://") for u in requests),requests
            if width<500:
                first_wrap = page.locator("#m40b-cavity-0 .atlas-wrap")
                dimensions = first_wrap.evaluate("(el)=>({sw:el.scrollWidth,cw:el.clientWidth,overflow:getComputedStyle(el).overflowX})")
                assert dimensions["sw"]>dimensions["cw"]
                assert dimensions["overflow"]=="auto"
                tile = page.locator("#m40b-tile-0-24")
                tile.scroll_into_view_if_needed()
                assert tile.is_visible()
            page.screenshot(path=str(out/f"reviewer-js-{'on' if js else 'off'}-{width}.png"),full_page=True)
            checks.append({"js":js,"width":width,"height":height,"visible_tiles":75,
                           "projected_cavities":3,"projected_sources":4,
                           "remote_requests":len([u for u in requests if not u.startswith("file://")])})
            ctx.close()

        context = browser.new_context(java_script_enabled=True)
        page = context.new_page()
        source=out.joinpath("new-arrangement.html").read_text(encoding="utf-8")
        forged=source.replace("</body>",'<script>window.__m40b_hacked__=true;</script></body>')
        pth=out/"forged-csp-script.html"
        pth.write_text(forged,encoding="utf-8")
        page.goto(pth.resolve().as_uri(),wait_until="load")
        assert page.evaluate("window.__m40b_hacked__===true") is False
        assert page.locator("script").count()==1
        context.close()

        # A copy of the generated HTML with static SI text changed will display
        # the adversary's text: CSP cannot authenticate static HTML. This is
        # a documented evidence limitation, not a native renderer defect.
        context = browser.new_context(java_script_enabled=False)
        page = context.new_page()
        page.goto((out/"forged-visible-html.html").resolve().as_uri(),wait_until="load")
        assert "9999 C/m²" in page.locator("#m40b-tile-0-24").inner_text()
        context.close()
        browser.close()
    return {"actual_chromium_desktop_mobile_js_on_off":checks,
            "CSP_blocks_injected_script":True,
            "forged_external_HTML_can_display_unverified_static_text":True}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output-dir",type=Path,required=True)
    args=parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    try:
        science=physics_and_integrity(args.output_dir)
        browser=browser_tests(args.output_dir,science)
        result={"verdict":"EXPERIMENT_PASS_WITH_RECORDED_HTML_PROVENANCE_LIMITATION",
                "reviewed_head":EXPECTED_HEAD,"reviewed_tree":EXPECTED_TREE,
                "science":science,"browser":browser}
        args.output_dir.joinpath("reviewer-results.json").write_text(
            json.dumps(result,indent=2,allow_nan=False),encoding="utf-8")
        print(json.dumps(result,indent=2,allow_nan=False),flush=True)
    except BaseException:
        (args.output_dir/"reviewer-error.log").write_text(traceback.format_exc(),encoding="utf-8")
        traceback.print_exc()
        raise


if __name__=="__main__":
    main()
