"""Nominal radiating-center coordinates and dimensional drawings, not PCB fabrication files."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from .array_geometry import planar_profile, coordinate_rows
from .phase_lut_generator import phase_map
from .visualize_field import write_csv


def geometry_summary(config):
    elements=planar_profile(config)
    points=np.array([e.position for e in elements])*1000
    diameter=config["transducer"]["supplier_claim_body_diameter_m"]*1000
    low,high=np.asarray(config["gap_range_m"])*1000
    gap=config["geometry"]["gap"]*1000
    body_h=config["transducer"]["supplier_claim_body_height_m"]*1000
    return {
        "geometry_status":"USER_DEFINED_NOMINAL_NOT_MEASURED",
        "coordinate_reference":"RADIATING_SURFACE_CENTER", "units":"mm",
        "origin_mm":np.mean(points,axis=0).round(9).tolist(),
        "total_emitters":len(elements),"emitters_per_plane":len(elements)//2,
        "x_coordinates_mm":sorted(set(points[:,0].round(9))),
        "y_coordinates_mm":sorted(set(points[:,1].round(9))),
        "nominal_face_z_mm":{"upper":gap/2,"lower":-gap/2},
        "upper_face_z_range_mm":[low/2,high/2],"lower_face_z_range_mm":[-high/2,-low/2],
        "face_gap_range_mm":[low,high],"total_gap_travel_mm":high-low,
        "symmetric_travel_per_plane_mm":(high-low)/2,
        "center_span_xy_mm":[float(np.ptp(points[:,0])),float(np.ptp(points[:,1]))],
        "nominal_body_envelope_xy_mm":[float(np.ptp(points[:,0])+diameter),float(np.ptp(points[:,1])+diameter)],
        "nominal_neighbor_clearance_mm":config["geometry"]["pitch"]*1000-diameter,
        "body_diameter_mm":diameter,
        "nominal_body_back_z_mm":{"upper":gap/2+body_h,"lower":-gap/2-body_h},
        "body_height_source":"Supplier image nominal; seating and face offset unmeasured",
        "pcb_plane_z_mm":None,"pcb_gap_mm":None,"pcb_outline_mm":None,
        "notes":["PCB plane needs measured mounting standoff and body datum offset",
                 "Body envelope is not a selected PCB outline or drilling pattern",
                 "Both plane exports share global XY; backside viewing does not renumber channels",
                 "10 mm body used as acoustic piston diameter only as an explicit approximation"]}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",default="config/acoustic_baseline.json")
    parser.add_argument("--output",default="build/geometry_10mm")
    args=parser.parse_args()
    config=json.loads(Path(args.config).read_text(encoding="utf-8"));out=Path(args.output)
    out.mkdir(parents=True,exist_ok=True)
    summary=geometry_summary(config)
    (out/"geometry_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    elements=planar_profile(config)
    rows=coordinate_rows(elements)
    g=config["geometry"]["gap"]*1000
    body_d=summary["body_diameter_mm"]
    body_h=config["transducer"]["supplier_claim_body_height_m"]*1000
    lo,hi=summary["face_gap_range_mm"]
    write_csv(out/"coordinates_nominal.csv",rows)
    (out/"coordinates_nominal.json").write_text(json.dumps(rows,indent=2),encoding="utf-8")
    for gap in config["gap_sweep_m"]:
        array=planar_profile(config,gap)
        suffix=f"{gap*1000:g}mm"
        write_csv(out/f"coordinates_{suffix}.csv",coordinate_rows(array))
        for mode in ("STANDING_WAVE","FOCUS"):
            write_csv(out/f"phase_map_{mode.lower()}_{suffix}.csv",
                      phase_map(array,mode,config["target_m"],config["sound_speed_m_s"]))
    fig,axes=plt.subplots(1,2,figsize=(13,6),layout="constrained")
    ax=axes[0]
    for e in elements[:len(elements)//2]:
        x,y,_=np.array(e.position)*1000
        ax.add_patch(Circle((x,y),body_d/2,facecolor="#d9edf7",edgecolor="#176180",lw=.8))
        ax.text(x,y,f"{e.rtl_channel:02d}",ha="center",va="center",fontsize=7)
    ax.add_patch(Rectangle((-47,-47),94,94,fill=False,ls="--",edgecolor="#777777"))
    ax.plot(0,0,"+",color="#b40000",ms=10)
    ax.annotate("12 mm pitch",xy=(-30,42),xytext=(-42,54),arrowprops={"arrowstyle":"->"},fontsize=9)
    ax.annotate("10 mm body; 2 mm nominal edge gap",xy=(18,-42),xytext=(-48,-59),
                arrowprops={"arrowstyle":"->"},fontsize=9)
    ticks=summary["x_coordinates_mm"]
    ax.set(xticks=ticks,yticks=ticks,xlim=(-57,57),ylim=(-65,62),aspect="equal",
           xlabel="Global x (mm)",ylabel="Global y (mm)",title="Both arrays: same global XY\n84 mm center span; 94 mm nominal body envelope")
    ax.tick_params(labelsize=8);ax.grid(alpha=.15)
    ax=axes[1]
    xvalues=summary["x_coordinates_mm"]
    for sign,color in ((1,"#176180"),(-1,"#b35e16")):
        face=sign*g/2
        for x in xvalues:
            bottom=g/2 if sign==1 else -g/2-body_h
            ax.add_patch(Rectangle((x-body_d/2,bottom),body_d,body_h,facecolor=color,alpha=.7))
            ax.plot(x,face,"o",color=color,ms=3)
        ax.hlines(face,-47,47,color=color,lw=2)
        for bound in (lo/2,hi/2):ax.hlines(sign*bound,-49,49,ls="--",color=color,alpha=.45)
    ax.annotate("",xy=(53,-g/2),xytext=(53,g/2),arrowprops={"arrowstyle":"<->"})
    ax.text(55,0,f"{g:g} mm\nFACE GAP",va="center",fontsize=9)
    ax.annotate("normal -Z",xy=(0,37),xytext=(-13,44),arrowprops={"arrowstyle":"->"},fontsize=9)
    ax.annotate("normal +Z",xy=(0,-37),xytext=(-13,-45),arrowprops={"arrowstyle":"->"},fontsize=9)
    ax.plot(0,0,"+",color="#b40000",ms=10);ax.text(3,2,"(0,0,0)",fontsize=9)
    ax.set(xlim=(-60,81),ylim=(-69,69),aspect="equal",xlabel="Global x (mm)",ylabel="Global z (mm)",
           title=f"Side view: face centers at z = +/-{g/2:g} mm\nDashed face travel: +/-{lo/2:g} to +/-{hi/2:g} mm")
    ax.grid(alpha=.15)
    fig.suptitle("128 x 10 mm nominal transmitters | radiating-surface coordinates | not PCB fabrication data",fontsize=12)
    for extension in ("png","svg"):fig.savefig(out/f"array_dimensions.{extension}",dpi=160)
    plt.close(fig)
    print(f"Exported 128 nominal centers, six gap profiles and 12 phase maps: {out}")


if __name__=="__main__":main()
