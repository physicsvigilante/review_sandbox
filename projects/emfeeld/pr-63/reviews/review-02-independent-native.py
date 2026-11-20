"""Independent reviewer-authored PR #63 R2 real native PyVista/VTK challenge."""
from dataclasses import replace
from pathlib import Path
import hashlib, json, math, os
import numpy as np
from PIL import Image
from scipy.constants import mu_0
import pyvista as pv
from emfeeld.circular_loop_magnetism import CircularLoopState
from emfeeld.circular_loop_view import CircularLoopLesson, save_snapshot

OUT=Path(os.environ["R2_OUTPUT"])
OUT.mkdir(parents=True, exist_ok=True)
checks=[]
def ck(name, condition):
    if not bool(condition): raise AssertionError(name)
    checks.append(name)
def key(view, name):
    interactor=view.plot.iren.interactor
    interactor.SetKeySym(name)
    interactor.InvokeEvent("KeyPressEvent")
    view.plot.render()
def slider(widget, value):
    widget.GetRepresentation().SetValue(value)
    widget.InvokeEvent("EndInteractionEvent")
def must_refuse(fn, path):
    try: fn()
    except ValueError: return not path.exists()
    return False

initial=CircularLoopState(centre_m=(.13,-.27,.19), normal_direction=(2.,-3.,4.),
                          current_A=6.25, radius_m=.37, probe_z_m=-.17,
                          samples_per_loop=91)
view=CircularLoopLesson(initial, off_screen=True, window_size=(1050,710))
try:
    view.plot.show(auto_close=False, interactive=False)
    u=np.array(initial.normal_direction)
    ck("real installed PyVista and VTK interactor", isinstance(view.plot,pv.Plotter) and view.plot.iren.interactor is not None)
    ck("blue positive normal initial", np.allclose(view.positive_normal_arrow_direction,u))
    ck("initial orange signed tangent", np.dot(view.current_arrow_direction,view.prepared.positive_current_tangent[0])>0)
    ck("initial green positive field", np.dot(view.field_arrow_direction,u)>0)
    count=view.preparation_count
    key(view,"2")
    ck("KeyPressEvent 2 reverses centre and rebuilds",view.state.current_A==-6.25 and view.state.probe_z_m==0 and not view.show_values and view.preparation_count==count+1)
    ck("orange green reversed, blue invariant",np.dot(view.current_arrow_direction,view.prepared.positive_current_tangent[0])<0 and np.dot(view.field_arrow_direction,u)<0 and np.array_equal(view.positive_normal_arrow_direction,u))
    count=view.preparation_count
    key(view,"v")
    ck("KeyPressEvent v reveals without rebuild",view.show_values and view.preparation_count==count)
    key(view,"1")
    ck("KeyPressEvent 1 positive centre",view.state.current_A==6.25 and view.state.probe_z_m==0)
    key(view,"3")
    ck("KeyPressEvent 3 doubles visible radius",math.isclose(view.state.radius_m,.74) and math.isclose(view.prepared.loop_radius_display_reference_units,2.) and not view.show_values)
    key(view,"n")
    ck("KeyPressEvent n reverses live current",view.state.current_A==-6.25)
    key(view,"k")
    ck("KeyPressEvent k zero omits orange and green",view.state.current_A==0 and view.current_arrow_actor is None and view.field_arrow_actor is None and view.probe_field_arrow_actor is None and np.array_equal(view.positive_normal_arrow_direction,u))
    key(view,"p")
    ck("KeyPressEvent p positive recovery",view.state.current_A==6.25 and view.current_arrow_actor is not None and view.field_arrow_actor is not None)
    key(view,"0")
    ck("KeyPressEvent 0 restores initial",view.state==initial and view.show_values and math.isclose(view.radius_slider.GetRepresentation().GetValue(),1.))
    count=view.preparation_count
    slider(view.radius_slider,1.65)
    ck("real radius EndInteractionEvent re-prepares",math.isclose(view.state.radius_m,.37*1.65,rel_tol=1e-14) and view.preparation_count==count+1)
    count=view.preparation_count
    slider(view.z_slider,-.8)
    ck("real z EndInteractionEvent re-prepares",math.isclose(view.state.probe_z_m,-.37*.8,rel_tol=1e-14) and view.preparation_count==count+1)
    B=mu_0*view.state.current_A*view.state.radius_m**2/(2*(view.state.radius_m**2+view.state.probe_z_m**2)**1.5)
    ck("independent SI field after physical sliders",np.allclose(view.prepared.field_probe_T,B*u,rtol=2e-14,atol=1e-18))
    raw=(json.dumps(initial.to_dict(),indent=3,sort_keys=True)+"\n").encode()
    other=replace(initial,current_A=-6.25)
    other_raw=(json.dumps(other.to_dict())+"\n").encode()
    bad=OUT/"wrong_live"
    ck("mismatched live lesson refused before directory",must_refuse(lambda:save_snapshot(other,bad,lesson=view,source_bytes=other_raw),bad))
    bad=OUT/"wrong_source"
    ck("mismatched raw original refused before directory",must_refuse(lambda:save_snapshot(initial,bad,lesson=view,source_bytes=other_raw),bad))
    view.plot.subplot(0,0)
    old_camera=view.plot.camera_position
    old_data=view.prepared
    count=view.preparation_count
    view.plot.camera.azimuth+=18
    view.redraw()
    key(view,"v")
    ck("camera/reveal do not reprepare",view.prepared is old_data and count==view.preparation_count)
    ck("real camera orbit changed viewpoint",view.plot.camera_position!=old_camera)
    view.plot.render()
    report=save_snapshot(initial,OUT/"reviewer_scene",lesson=view,source_bytes=raw)
    scene=OUT/"reviewer_scene"
    ck("snapshot source exact raw bytes",(scene/"authored-input.json").read_bytes()==raw and report["current_state"]!=report["authored_state"])
    png=scene/"view.png"
    ck("new reviewer-owned native PNG",png.is_file())
    rgb=np.asarray(Image.open(png).convert("RGB"))
    h,w=rgb.shape[:2]
    ck("PNG size and real pixel variation",(w,h)==(1050,710) and rgb.std()>10)
    roi=rgb[int(.60*h):int(.97*h),int(.67*w):int(.97*w)]
    dark=np.max(roi,axis=2)<210
    ylist=[i+int(.60*h) for i,row in enumerate(dark) if int(row.sum())>round(roi.shape[1]*.38)]
    bands=[]
    for y in ylist:
        if not bands or y>bands[-1][-1]+2:bands.append([y])
        else:bands[-1].append(y)
    ck("two independently visible slider rails after redraw",len(bands)>=2 and bands[1][0]-bands[0][-1]>=12)
    left=rgb[:,int(.05*w):int(.6*w),:3].astype(int)
    orange=(left[:,:,0]>170)&(left[:,:,1]>60)&(left[:,:,1]<180)&(left[:,:,2]<130)
    green=(left[:,:,1]>92)&(left[:,:,1]>left[:,:,0]*1.2)&(left[:,:,2]<left[:,:,1]*1.4)
    blue=(left[:,:,2]>130)&(left[:,:,2]>left[:,:,0]*1.2)&(left[:,:,0]<140)
    ck("native orange green blue glyph pixels",orange.sum()>6 and green.sum()>6 and blue.sum()>6)
    receipt=json.loads((scene/"integrity.json").read_text())["files"]
    for filename,digest in receipt.items():
        ck("reviewer output hash "+filename,hashlib.sha256((scene/filename).read_bytes()).hexdigest()==digest)
    results={"status":"PASS","native_checks":checks,"check_count":len(checks),
             "pyvista_version":pv.__version__,"vtk_version":pv.vtk_version_info.__str__(),
             "reviewer_png_sha256":hashlib.sha256(png.read_bytes()).hexdigest(),
             "reviewer_png_dimensions":[w,h],
             "slider_rail_pixel_bands":[[v[0],v[-1]] for v in bands],
             "color_pixel_counts":{"orange":int(orange.sum()),"green":int(green.sum()),"blue":int(blue.sum())},
             "initial_state":initial.to_dict(),"final_state":view.state.to_dict(),
             "native_preparation_count":view.preparation_count}
    (OUT/"results.json").write_text(json.dumps(results,indent=2,sort_keys=True)+"\n")
    print(json.dumps(results,sort_keys=True))
finally:
    view.plot.close()
