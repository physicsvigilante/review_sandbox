#!/usr/bin/env python3
"""Fresh reviewer-authored M36d native physics and detached provenance attacks.

This script is NOT an author test; it uses separately chosen 3D configurations,
separately calculated SI values, real public production APIs, and real browser
output. It deliberately does not modify any production source file.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from math import isclose, pi, sqrt
from pathlib import Path
import traceback

from conductor_sim import (
    ElectrostaticProblem, FixedNetCharge, Grounded, MixedRadialBackend,
    PointCharge, SolidSphere, SphericalShell,
)
from conductor_sim.geometry import contains_metal, physical_boundaries
from conductor_sim.solver import SingularField, UnsupportedProblem
from tools.m36d_true_solid_sphere import run_all
from tools.m36d_solid_reference import check as detached_reference_check

OUT = Path("review-artifacts/conductor-m36d-chat-b-01")
OUT.mkdir(parents=True, exist_ok=True)
K_SI = 1.0 / (4.0 * pi * 8.8541878128e-12)
LOG = []

def persist():
    (OUT / "reviewer-events.json").write_text(
        json.dumps(LOG, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )

def event(kind, item, details):
    LOG.append({"kind": kind, "item": item, "details": details})
    persist()

def checked(value, prediction, label, *, abs_tol=1e-10, rel_tol=4e-11):
    assert isclose(value, prediction, abs_tol=abs_tol, rel_tol=rel_tol), (
        f"{label}: backend={value!r}, independent Gauss={prediction!r}"
    )

def vec3(actual, predicted, label):
    assert len(actual) == 3, (label, actual)
    for axis in range(3):
        checked(actual[axis], predicted[axis], label + f"[{axis}]", abs_tol=1e-8)

def translated(c, displacement):
    return tuple(c[i] + displacement[i] for i in range(3))

def actual_new_models():
    # NONE of these physical inputs appears in the developer's 3 source states.
    # The non-axial 3D tests also differ from the developer's x-only probes.
    cases = (
        ("reviewer-positive-translated", .073, 3.7e-9,
         (.17, -.09, .23), FixedNetCharge(3.7e-9)),
        ("reviewer-negative-translated", .155, -4.6e-9,
         (-.065, .12, -.31), FixedNetCharge(-4.6e-9)),
        ("reviewer-grounded-translated", .065, 0.,
         (.41, -.2, .11), Grounded()),
        ("reviewer-isolated-zero", .215, 0.,
         (-.07, -.15, .09), FixedNetCharge(0.)),
    )
    backend = MixedRadialBackend()
    independent_observations = []
    diagonal = (2/3, -1/3, 2/3)  # a genuinely 3D unit direction
    other = (-1/sqrt(3), -1/sqrt(3), 1/sqrt(3))
    for name, radius, q, center, constraint in cases:
        solid = SolidSphere(radius, constraint, center_m=center, name="Sphere A")
        model = ElectrostaticProblem(conductors=(solid,))
        assert backend.supports(model), f"legitimate single solid refused: {name}"
        native = backend.solve(model)
        assert len(native.radial_shells) == 1
        assert native.radial_shells[0].inner_radius_m == 0
        assert len(physical_boundaries(solid)) == 1
        result = native.conductor_by_name("Sphere A")
        assert result.name == "Sphere A"
        for key in ("net_charge_c", "outer_surface_charge_c"):
            checked(getattr(result, key), q, f"{name}/{key}", abs_tol=1e-20)
        checked(result.inner_surface_charge_c, 0., f"{name}/no-inner-face", abs_tol=1e-20)
        inside_v = K_SI * q / radius
        checked(result.potential_v, inside_v, f"{name}/equipotential")
        samples = []
        for frac in (0.0, .37, .77):
            where = translated(center, tuple(frac * radius * x for x in diagonal))
            assert contains_metal(solid, where), (name, where)
            checked(native.potential_at(where), inside_v,
                    f"{name}/V-inside-{frac}")
            vec3(native.electric_field_at(where), (0., 0., 0.),
                 f"{name}/E-inside-{frac}")
            samples.append({"r_over_R": frac, "native_potential_v": native.potential_at(where),
                            "native_e_v_m": native.electric_field_at(where)})
        for direction_label, direction, r_over_R in (
            ("3D-positive", diagonal, 2.35),
            ("3D-reversed", tuple(-d for d in diagonal), 1.71),
            ("3D-oblique", other, 3.4),
        ):
            displacement = tuple(r_over_R * radius * t for t in direction)
            where = translated(center, displacement)
            sep = radius * r_over_R
            predicted_v = K_SI * q / sep
            predicted_field = tuple(K_SI * q * t / (sep * sep) for t in direction)
            observed_v = native.potential_at(where)
            observed_e = native.electric_field_at(where)
            checked(observed_v, predicted_v, f"{name}/{direction_label}/V")
            vec3(observed_e, predicted_field, f"{name}/{direction_label}/E")
            samples.append({
                "point_m": where, "native_potential_v": observed_v,
                "Gauss_potential_v": predicted_v,
                "native_e_v_m": observed_e, "Gauss_e_v_m": predicted_field,
            })
        outer_sigma = q / (4*pi*radius**2)
        for axis in (0,1,2):
            where = list(center)
            where[axis] += radius
            measured = native.surface_charge_density_at("Sphere A","outer",tuple(where))
            checked(measured,outer_sigma,f"{name}/outer-sigma-axis-{axis}",abs_tol=1e-20)
        assert outer_sigma == 0. or (outer_sigma > 0.) == (q > 0.)
        for boundary in (translated(center, (radius,0.,0.)),
                         translated(center,(0.,0.,-radius))):
            try:
                native.electric_field_at(boundary)
            except SingularField:
                pass
            else:
                raise AssertionError(f"{name}: metal-boundary E not refused")
        try:
            native.surface_charge_density_at("Sphere A","inner",
                                             translated(center,(radius,0.,0.)))
        except ValueError as exc:
            assert "no inner surface" in str(exc)
        else:
            raise AssertionError(f"{name}: imaginary inner surface accessible")
        case = {
            "scenario": name, "radius_m":radius,"Q_c":q,"center_m":center,
            "native_metal_V":result.potential_v,
            "independent_metal_V":inside_v,
            "native_net_c":result.net_charge_c,
            "native_inner_bookkeeping_c":result.inner_surface_charge_c,
            "native_outer_c":result.outer_surface_charge_c,
            "Gauss_uniform_outer_sigma":outer_sigma, "samples":samples,
            "outer_only_surface_count":len(physical_boundaries(solid)),
        }
        independent_observations.append(case)
        event("positive",name,{"R":radius,"Q":q,"Vmetal":result.potential_v,
                               "sigma":outer_sigma})
    (OUT/"novel-native-vs-independent-gauss.json").write_text(
        json.dumps(independent_observations,indent=2,allow_nan=False)+"\n",
        encoding="utf-8"
    )
    return len(cases)

def rejected_nearby_models():
    b=MixedRadialBackend()
    fixed=FixedNetCharge(1.9e-9)
    solid=SolidSphere(.093,fixed,name="Sphere A")
    bad = {
        "lone-hollow-shell": ElectrostaticProblem(conductors=(
            SphericalShell(.04,.093,fixed,name="hollow"),)),
        "interior-point-source": ElectrostaticProblem(
            conductors=(solid,),charges=(PointCharge(2.1e-9,(0.,0.,.02)),)),
        "exterior-point-source": ElectrostaticProblem(
            conductors=(solid,),charges=(PointCharge(-2.1e-9,(0.,0.,.24)),)),
        "two-solids": ElectrostaticProblem(conductors=(
            solid,SolidSphere(.29,FixedNetCharge(0.),name="other"))),
        "eccentric-solid-and-shell": ElectrostaticProblem(conductors=(
            solid,SphericalShell(.19,.23,FixedNetCharge(0.),
                                 center_m=(.031,0.,0.),name="outer"))),
        "intersecting-solid-and-shell": ElectrostaticProblem(conductors=(
            solid,SphericalShell(.07,.21,FixedNetCharge(0.),name="outer"))),
    }
    for title,model in bad.items():
        assert not b.supports(model), f"invalid model unexpectedly supported: {title}"
        try:
            b.solve(model)
        except UnsupportedProblem as exc:
            event("refused",title,str(exc))
        else:
            raise AssertionError(f"{title}: invalid model was SOLVED")

    # An unfamiliar real mixed M14b model must still be intact.
    concentric=ElectrostaticProblem(conductors=(
        SolidSphere(.067,FixedNetCharge(1.3e-9),name="core"),
        SphericalShell(.21,.25,FixedNetCharge(-.4e-9),name="shell"),
    ))
    assert b.supports(concentric)
    solved=b.solve(concentric)
    core=solved.conductor_by_name("core")
    shell=solved.conductor_by_name("shell")
    checked(core.outer_surface_charge_c,1.3e-9,"old-mixed-core",abs_tol=1e-20)
    checked(shell.inner_surface_charge_c,-1.3e-9,"old-mixed-inner",abs_tol=1e-20)
    checked(shell.outer_surface_charge_c,.9e-9,"old-mixed-outer",abs_tol=1e-20)
    checked(shell.potential_v,K_SI*.9e-9/.25,"old-mixed-shell-V")
    checked(core.potential_v,
            K_SI*(1.3e-9*(1/.067-1/.21)+.9e-9/.25),"old-mixed-core-V")
    event("regression","historical-mixed-sphere-shell",
          {"core_V":core.potential_v,"shell_V":shell.potential_v})
    return len(bad)

def set_path(data, tokens, replacement):
    obj=data
    for token in tokens[:-1]:
        obj=obj[token]
    obj[tokens[-1]]=replacement

def fresh_detached_attacks():
    folder=OUT/"fresh-native-p26"
    native=run_all(folder)  # ACTUAL exported production, not handwritten mock JSON
    positive=detached_reference_check(native)
    assert positive["qualified_original_jee_solid_sphere_apparatus"] == 1
    event("reference-positive","fresh-export",
          {"observations":positive["actual_solid_source_states_independently_checked"]})
    manipulations = (
        ("fake-notes-page",("printed_source","page"),22),
        ("fake-printed-illustration",("printed_source","question"),"Illustration 99"),
        ("invented-source-numeric-givens",("printed_source","original_parameters"),
         "printed Q=1 nC, R=0.10 m"),
        ("fake-original-count",("original_source_apparatus_count",),3),
        ("claimed-charge-current-time",("physical_time_evolution",),True),
        ("fake-source-name",("native_states",0,"physical_source_id"),"Sphere Z"),
        ("false-shell-geometry",("native_states",0,"physical_shape_type"),"SphericalShell"),
        ("fictitious-solid-inner-radius",("native_states",0,"physical_geometry",
                                          "inner_radius_m"),.025),
        ("hollow-rendered-ring",("actual_rendered_geometry",0,"inner_radius_m"),.045),
        ("forged-draw-name",("actual_rendered_geometry",0,"name"),"Other metal"),
        ("mismatched-rendered-outer-radius",("actual_rendered_geometry",1,
                                            "outer_radius_m"),.105),
        ("fake-inner-face-charge",("native_states",0,
                                  "observed_conductor_results",0,
                                  "inner_surface_charge_c"),.35e-9),
        ("outer-face-charge-reversal",("native_states",0,
                                     "observed_conductor_results",0,
                                     "outer_surface_charge_c"),-1e-9),
        ("invalid-net-Q",("native_states",1,
                         "observed_conductor_results",0,"net_charge_c"),+2e-9),
        ("signed-outside-field-flipped",("native_states",1,"native_samples",
                                         "external_pos_x_e_v_m",0),+100.),
        ("invalid-outer-sigma",("native_states",0,"native_samples",
                                "outer_sigma_c_m2"),0.0),
        ("source-hypothetical-role-confused",("native_states",1,"case_role"),
                                            "source_original_shape_teacher_numeric_example"),
        ("teacher-title-as-original",("native_states",1,"state_title"),
                                     "PRINTED p26 SOLID sphere; not teacher"),
        ("falsified-ground-net-Q",("native_states",2,
                                  "observed_conductor_results",0,
                                  "net_charge_c"),.2e-9),
        ("ground-fabricated-as-isolated",("native_states",2,"constraint_type"),
                                        "FixedNetCharge"),
        ("forged-source-time-axis",("native_states",0,"source_time_axis"),True),
    )
    refusals=[]
    for label,path,wrong in manipulations:
        altered=deepcopy(native)
        set_path(altered,path,wrong)
        try:
            detached_reference_check(altered)
        except AssertionError as exc:
            refusals.append({"attack":label,"field":list(path),
                             "replacement":wrong,"rejection":str(exc)})
            event("tamper-refused",label,str(exc))
        else:
            raise AssertionError(f"source-free checker FALSELY ACCEPTED {label}")
    (OUT/"fresh-hostile-mutations.json").write_text(
        json.dumps(refusals,indent=2,allow_nan=False)+"\n",encoding="utf-8"
    )
    return len(manipulations)

def pdf_and_browser_evidence():
    from playwright.sync_api import sync_playwright
    import fitz
    doc=fitz.open("source/POTENTIAL_CONDUCTORS1.pdf")
    assert len(doc) >= 26
    page=doc[25]  # physical p26, 1-based
    pix=page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False)
    pix.save(str(OUT/"p26-printed-page.png"))
    extracted=page.get_text(sort=True)
    (OUT/"p26-printed-page-text.txt").write_text(extracted,encoding="utf-8")
    event("source-pdf","p26",{"page_count":len(doc),
                               "p26_text_chars":len(extracted),
                               "p26_render_width_px":pix.width,
                               "p26_render_height_px":pix.height})
    doc.close()
    native_dir=OUT/"fresh-native-p26"
    manifest=json.loads((native_dir/"native-solid-sphere.json").read_text())
    url=(native_dir/manifest["viewer_file"]).resolve().as_uri()
    browser_records=[]
    with sync_playwright() as playwright:
        browser=playwright.chromium.launch(headless=True)
        try:
            tab=browser.new_page(viewport={"width":1400,"height":900})
            net=[]
            js=[]
            tab.on("pageerror",lambda e:js.append(str(e)))
            tab.on("request",lambda r:net.append(r.url)
                   if r.url.startswith(("http://","https://")) else None)
            tab.goto(url,wait_until="load",timeout=45000)
            assert tab.evaluate("window.conductorViewer.frameCount")==3
            assert tab.evaluate("window.conductorViewer.mode")=="static"
            assert tab.locator("#m36d-source-authentic-solid").is_visible()
            disclaimer=tab.locator("#m36d-source-authentic-solid").inner_text()
            for phrase in ("symbolic","teacher","solid","no physical inner face",
                           "precomputed static"):
                assert phrase in disclaimer.lower(),phrase
            assert tab.locator("canvas#scene").is_visible()
            screenshots=OUT/"independent-browser"
            screenshots.mkdir(exist_ok=True)
            for index,world in enumerate(manifest["native_states"]):
                tab.locator("#frame").evaluate(
                    "(el, i) => {el.value=String(i); el.dispatchEvent(new Event('input',{bubbles:true}));}",
                    index
                )
                shown=tab.locator("#case").inner_text()
                assert shown==world["state_title"],(index,shown)
                options=tab.locator("#density option").all_inner_texts()
                assert len(options)==1 and "Sphere A / outer" in options[0],options
                frame=tab.evaluate("""i => {
                    const raw=JSON.parse(document.querySelector('#simulation-data').textContent);
                    return raw.frames[i];
                }""",index)
                assert len(frame["geometry"])==1
                shape=frame["geometry"][0]
                assert shape["kind"]=="sphere" and shape["name"]=="Sphere A"
                assert shape["inner_radius_m"]==0
                assert isclose(shape["outer_radius_m"],
                               world["physical_geometry"]["radius_m"])
                assert len(frame["profiles"])==1
                assert frame["profiles"][0]["surface"]=="outer"
                assert len(frame["conductor_results"])==1
                assert len(frame["source_masks"])==0
                assert any(str(cell).lower()=="metal"
                           for row in frame["grid"]["region"] for cell in row)
                saved=screenshots/f"independent-p26-state-{index}.png"
                tab.screenshot(path=str(saved),full_page=True,animations="disabled")
                data=saved.read_bytes()
                browser_records.append({
                    "frame":index,"on_screen_title":shown,
                    "sphere_inner_radius_m":shape["inner_radius_m"],
                    "sphere_outer_radius_m":shape["outer_radius_m"],
                    "density_options":options,"screenshot":str(saved),
                    "screenshot_sha256":hashlib.sha256(data).hexdigest(),
                    "screenshot_bytes":len(data)
                })
                event("browser-frame",f"frame-{index}",browser_records[-1])
            assert not net,f"offline HTTP/network activity: {net}"
            assert not js,f"JavaScript errors: {js}"
            tab.close()
        finally:
            browser.close()
    assert len(set(r["screenshot_sha256"] for r in browser_records))==3
    (OUT/"independent-browser-observations.json").write_text(
        json.dumps(browser_records,indent=2,allow_nan=False)+"\n",encoding="utf-8"
    )
    return len(browser_records)

def main():
    event("identity","independent-GPT-6-chat-B",{
        "source_expected_head":"e5fa85abe990abe8fdedc555e9313ac0420a56a7",
        "source_expected_tree":"523d02e95dbb4791acd630f9c535eb552262c606",
        "note":"Execution data is reviewer-owned, not independent laboratory measurement."
    })
    summary={
        "novel_native_cases":actual_new_models(),
        "unsupported_refusals":rejected_nearby_models(),
        "detached_attacks_rejected":fresh_detached_attacks(),
        "actual_browser_frames":pdf_and_browser_evidence(),
    }
    (OUT/"reviewer-summary.json").write_text(
        json.dumps(summary,indent=2)+"\n",encoding="utf-8"
    )
    print("REVIEWER INDEPENDENT SUCCESS",json.dumps(summary,sort_keys=True))

if __name__=="__main__":
    try:
        main()
    except Exception:
        (OUT/"first-failure.txt").write_text(traceback.format_exc(),encoding="utf-8")
        raise
