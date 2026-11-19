"""Chat B independently authored 6-cavity M39b reproduction (review PR #98).

Run from exact pinned production checkout:
    PYTHONPATH=src:. python review-01-chat-b-reproducer.py

For complete 102-check evidence, see the attached review conversation ZIP.
No original JEE item or geometry is claimed.
"""
from copy import deepcopy
from dataclasses import replace
from fractions import Fraction
from math import ulp
from pathlib import Path
import json

from conductor_sim.cavity_gauss import (
    CavityCharge, SealedCavity, GaussCavityAssembly, solve_cavity_gauss
)
from conductor_sim.cavity_topology_viewer import (
    topology_view_manifest, render_cavity_topology
)
from conductor_sim.model import Grounded, FixedNetCharge
from tools.m39a_gauss_reference import check_gauss_record
from tools.m39b_topology_reference import check_topology_view_manifest

def source(s, q):
    return CavityCharge(s, q)

def novel_model():
    return GaussCavityAssembly("ReviewerMetal_R6", (
        SealedCavity("Alpha_Mixed",
            (source("A_positive",4e-9),source("A_negative",-1e-9))),
        SealedCavity("Beta_TrulyEmpty"),
        SealedCavity("Gamma_NetZero",
            (source("C_plus",2.5e-9),source("C_minus",-2.5e-9))),
        SealedCavity("Delta_MixedNegative",
            (source("D_minus",-7e-9),source("D_plus",0.5e-9))),
        SealedCavity("Epsilon_Single",(source("E_solo",1.25e-9),)),
        SealedCavity("Zeta_LongLabel",
            (source("Zeta_signed_teacher_source_with_stable_ID_2026_11_19",4.25e-9),
             source("Zeta_subtract",-0.75e-9))),
    ), FixedNetCharge(-2.25e-9), 8.8541878128e-12)

def expect_refusal(label, call):
    try:
        call()
    except (ValueError,TypeError) as ex:
        print("REFUSED",label,type(ex).__name__,str(ex)[:120])
    else:
        raise AssertionError("unexpectedly accepted "+label)

model=novel_model()
parent=solve_cavity_gauss(model).as_dict()
iso=solve_cavity_gauss(model)
gnd=solve_cavity_gauss(replace(model,constraint=Grounded()))
assert parent==solve_cavity_gauss(model).as_dict()
manifest=topology_view_manifest(iso,gnd)
html=render_cavity_topology(iso,gnd)
assert html==render_cavity_topology(iso,gnd)
assert check_gauss_record(iso.as_dict())["point_source_identities_checked"]==9
assert check_gauss_record(gnd.as_dict())["point_source_identities_checked"]==9
assert check_topology_view_manifest(manifest)["cavities_checked"]==6

tot=Fraction()
for cavity,row in zip(model.cavities,manifest["cavities"]):
    exact=sum((Fraction.from_float(s.charge_c) for s in cavity.sources),Fraction())
    tot+=exact
    for key,target in (("source_charge_sum_c",exact),
                       ("induced_inner_face_total_charge_c",-exact)):
        actual=row[key]
        assert (actual==0)==(target==0)
        if target:
            assert (actual>0)==(target>0)
            assert abs(actual-float(target)) <= 4*ulp(float(target))
    print(cavity.cavity_id,float(exact),float(-exact))

fixed=Fraction.from_float(model.constraint.charge_c)
eps=Fraction.from_float(model.permittivity_f_per_m)
expected_outer=fixed+tot
expected_flux=expected_outer/eps
assert abs(iso.outer_face_charge_c-float(expected_outer))<=4*ulp(float(expected_outer))
assert abs(iso.exterior_electric_flux_v_m-float(expected_flux))<=4*ulp(float(expected_flux))
assert gnd.net_metal_charge_c==float(-tot)
assert gnd.outer_face_charge_c==gnd.exterior_electric_flux_v_m==0.0
print("total",float(tot),"outer",float(expected_outer),"flux",float(expected_flux))

# Pair attacks even where per-cavity net charge is still zero.
c=list(model.cavities)
forged=replace(model,constraint=Grounded(),cavities=(
    c[0],replace(c[1],cavity_id=c[2].cavity_id),
    replace(c[2],cavity_id=c[1].cavity_id),*c[3:]
))
expect_refusal("swap zero-total cavity IDs",
    lambda:topology_view_manifest(iso,solve_cavity_gauss(forged)))
expect_refusal("two isolated",lambda:topology_view_manifest(iso,iso))
expect_refusal("two grounded",lambda:topology_view_manifest(gnd,gnd))
expect_refusal("different epsilon",lambda:topology_view_manifest(
    iso,solve_cavity_gauss(replace(model,constraint=Grounded(),permittivity_f_per_m=1.0))))
for field,val in (("source_role","original_jee"),("geometry_verified",True),
                  ("original_workbook_items_newly_solved",False)):
    modified=deepcopy(manifest)
    modified[field]=val
    expect_refusal("manifest "+field,
        lambda m=modified:check_topology_view_manifest(m))

out=Path("reviewer-six-cavity")
out.mkdir(exist_ok=True)
(out/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n")
(out/"topology.html").write_text(html)
print("novel reviewer case: native math + standalone science + pair attacks PASS")
