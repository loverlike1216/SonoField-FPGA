"""Produce reproducible simulation estimates, comparison tables and standalone plots."""
import argparse
import csv
from dataclasses import replace
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.ndimage import label
from .array_geometry import opposing_arrays, SHAPES
from .field_solver import pressure
from .phase_solver import focus_phases, quantize_phase, dequantize_phase
from .standing_wave import standing_wave_phases
from .particle_model import scenarios
from .phase_lut_generator import phase_map


def write_csv(path,rows):
    with path.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)


def potential_proxy(elements,points,phases,c,h=0.00005):
    """Normalized high-contrast Rayleigh proxy, f1=f2=1, not a measured EPS force.

    U'=|p|^2 - 3/(2*k^2)*|grad p|^2. Common positive scale omitted.
    No mass-support calculation. ka for the actual particle must be assessed separately.
    """
    points=np.atleast_2d(points)
    p=pressure(elements,points,phases,c)
    gradient=np.zeros((len(points),3),complex)
    for axis in range(3):
        delta=np.zeros(3);delta[axis]=h
        gradient[:,axis]=(pressure(elements,points+delta,phases,c)-pressure(elements,points-delta,phases,c))/(2*h)
    k=2*np.pi*elements[0].frequency/c
    return abs(p)**2-1.5/k**2*np.sum(abs(gradient)**2,axis=1)


def trap_proxy(elements,c):
    phase=standing_wave_phases(elements,sound_speed=c)
    axis=np.linspace(-.01,.01,21)
    points=np.stack(np.meshgrid(axis,axis,axis,indexing="ij"),axis=-1).reshape(-1,3)
    u=potential_proxy(elements,points,phase,c).reshape(21,21,21)
    boundary=np.concatenate([u[0].ravel(),u[-1].ravel(),u[:,0].ravel(),u[:,-1].ravel(),u[:,:,0].ravel(),u[:,:,-1].ravel()])
    threshold=float(boundary.min())
    labels,_=label(u<threshold)
    component=labels[10,10,10]
    volume=int(np.sum(labels==component)) if component else 0
    # Local curvature only; positive diagonals alone are not a full stability test.
    h=.0001; origin=np.zeros((1,3)); center=potential_proxy(elements,origin,phase,c)[0]
    hessian=np.zeros((3,3))
    for i in range(3):
        di=np.eye(3)[i]*h
        hessian[i,i]=(potential_proxy(elements,origin+di,phase,c)[0]-2*center+potential_proxy(elements,origin-di,phase,c)[0])/h**2
        for j in range(i):
            dj=np.eye(3)[j]*h
            value=(potential_proxy(elements,origin+di+dj,phase,c)[0]-potential_proxy(elements,origin+di-dj,phase,c)[0]
                   -potential_proxy(elements,origin-di+dj,phase,c)[0]+potential_proxy(elements,origin-di-dj,phase,c)[0])/(4*h*h)
            hessian[i,j]=hessian[j,i]=value
    return {"center_node_pressure_au":float(abs(pressure(elements,origin,phase,c)[0])),
            "proxy_center_U":float(center),"proxy_min_hessian_eigenvalue":float(np.linalg.eigvalsh(hessian).min()),
            "coarse_connected_basin_mm3":volume, "proxy_grid_step_mm":1,
            "proxy_escape_threshold":threshold}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",default="config/acoustic_baseline.json")
    parser.add_argument("--output",default="evidence/model/vn1")
    args=parser.parse_args()
    config=json.loads(Path(args.config).read_text()); out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    c=config["sound_speed_m_s"]; mc=config["monte_carlo"];rng=np.random.default_rng(mc["seed"])
    geometry=config["geometry"]; rows=[]
    for shape in ("planar","concave"):
        for n in SHAPES:
            a=opposing_arrays(**{**geometry,"total":n,"shape":shape})
            phase=dequantize_phase(quantize_phase(focus_phases(a,sound_speed=c)))
            ideal=float(abs(pressure(a,[[0,0,0]],phase,c,config["attenuation_np_m"])[0]))
            values=[]
            for _ in range(mc["trials"]):
                perturbed=[replace(e,relative_amplitude=max(0,float(rng.normal(1,mc["relative_amplitude_std"]))),
                                    intrinsic_phase=float(rng.normal(0,np.deg2rad(mc["phase_error_std_degrees"])))) for e in a]
                values.append(float(abs(pressure(perturbed,[[0,0,0]],phase,c,config["attenuation_np_m"])[0])))
            rows.append({"classification":"SIMULATION_ESTIMATE","shape":shape,"emitters":n,
                         "central_focus_pressure_au":ideal,"error_mean_au":float(np.mean(values)),
                         "error_p05_au":float(np.quantile(values,.05)),"error_p95_au":float(np.quantile(values,.95)),
                         "gap_m":geometry["gap"],"pitch_m":geometry["pitch"],"sound_speed_m_s":c})
    write_csv(out/"emitter_scaling.csv",rows)
    comparisons=[]
    for shape in ("planar","concave"):
        for gap in (.120,.160,.200):
            a=opposing_arrays(**{**geometry,"shape":shape,"gap":gap})
            comparisons.append({"classification":"SIMULATION_ESTIMATE","shape":shape,"emitters":len(a),"gap_m":gap,
                                "central_focus_pressure_au":float(abs(pressure(a,[[0,0,0]],focus_phases(a,sound_speed=c),c)[0])),
                                **trap_proxy(a,c)})
    write_csv(out/"geometry_comparison.csv",comparisons)
    particles=[p.assessment(c) for p in scenarios()]
    write_csv(out/"particle_scenarios.csv",particles)
    write_csv(out/"reference_phase_map.csv",phase_map(opposing_arrays(**geometry),config["mode"],config["target_m"],c))
    channel_rows=[]
    for e in opposing_arrays(128):
        channel_rows.append({"CHANNEL_ID":e.channel_id,"rtl_channel":e.rtl_channel,
                             "serializer_lane":e.rtl_channel//4,"q_output":e.rtl_channel%4,
                             "driver_module_16ch":e.rtl_channel//16,"driver_local_channel":e.rtl_channel%16})
    write_csv(out/"channel_mapping.csv",channel_rows)
    fig,ax=plt.subplots(figsize=(8,4.5),layout="constrained")
    for shape in ("planar","concave"):
        series=[r for r in rows if r["shape"]==shape]
        ax.plot([r["emitters"] for r in series],[r["central_focus_pressure_au"] for r in series],"o-",label=shape+" ideal")
        ax.fill_between([r["emitters"] for r in series],[r["error_p05_au"] for r in series],[r["error_p95_au"] for r in series],alpha=.2)
    ax.set(xlabel="Total emitters",ylabel="Central focus pressure (arbitrary units)",title="SIMULATION ESTIMATE | shaded: mismatch 5–95% interval")
    ax.grid(alpha=.25);ax.legend();fig.savefig(out/"emitter_scaling.png",dpi=160);plt.close(fig)
    axis=np.linspace(-.012,.012,161);x,z=np.meshgrid(axis,axis)
    points=np.stack([x.ravel(),np.zeros(x.size),z.ravel()],axis=1)
    fig,axs=plt.subplots(1,2,figsize=(10,4.5),layout="constrained")
    for ax,shape in zip(axs,("planar","concave")):
        a=opposing_arrays(**{**geometry,"shape":shape})
        p=abs(pressure(a,points,standing_wave_phases(a,sound_speed=c),c)).reshape(x.shape)
        im=ax.imshow(p,origin="lower",extent=[-12,12,-12,12],aspect="equal")
        ax.set(title=f"{shape}, {len(a)} emitters",xlabel="x (mm)",ylabel="z (mm)")
        fig.colorbar(im,ax=ax,label="Pressure magnitude (a.u.)")
    fig.suptitle("SIMULATION ESTIMATE | opposed standing waves, y=0")
    fig.savefig(out/"standing_wave_comparison.png",dpi=160);plt.close(fig)
    (out/"assumptions.json").write_text(json.dumps({"config":config,"monte_carlo_seed":mc["seed"],
        "pressure_units":"arbitrary; no SPL calibration","trap_proxy":"Rayleigh high contrast f1=f2=1; no gravity or finite-size scattering",
        "basin_definition":"6-connected region containing origin below minimum boundary proxy on +/-10mm cube, 1mm grid",
        "limitations":["No multiple scattering or mutual coupling","No measured driver/element transfer functions",
                       "Far-field piston approximation imperfect for TCT40","No temperature/RH absorption fit",
                       "No physical working-volume or mass-support guarantee","50mg example is outside small-particle validity"]},indent=2))
    print(f"Generated {len(rows)} scaling cases, {len(comparisons)} geometry cases, {len(particles)} particle scenarios: {out}")


if __name__=="__main__": main()
