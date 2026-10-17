# Derivedfrompriorv5audit power_budget_corner.py; unfittedengineeringmodel
import numpy as np,math
from scipy.linalg import expm
def matrices(r,cb,c0,cm,q,fs,dt):
 lm=1/((2*math.pi*fs)**2*cm);rm=2*math.pi*fs*lm/q
 a=np.array([[-1/r/cb,-1/r/cb,0,0],[-1/r/c0,-(1/r+1e-6)/c0,-1/c0,0],[0,1/lm,-rm/lm,-1/lm],[0,0,1/cm,0]])
 b=np.array([1/r/cb,1/r/c0,0,0]);f=expm(a*dt);g=np.linalg.solve(a,(f-np.eye(4))@b)
 return f,g
def periodic(vdd,c0,cm,q,fs,fdrive,rseries,cb,points=128,return_trace=False):
 # Driver resistance and all motional values are assumptions, not bounded OEM models.
 dt=1/fdrive/2/points;rh=rseries+5.;rl=rseries+1.1
 eh,gh=matrices(rh,cb,c0,cm,q,fs,dt);el,gl=matrices(rl,cb,c0,cm,q,fs,dt)
 fh,ghh=matrices(rh,cb,c0,cm,q,fs,1/fdrive/2);fl,gll=matrices(rl,cb,c0,cm,q,fs,1/fdrive/2)
 x=np.linalg.solve(np.eye(4)-fl@fh,fl@ghh*vdd)
 trace=[]
 lm=1/((2*math.pi*fs)**2*cm);rm=2*math.pi*fs*lm/q
 for high in [True,False]:
  u=vdd if high else 0.;r=rh if high else rl
  for _ in range(points):
   current=(u-x[0]-x[1])/r
   trace.append([len(trace)*dt,x[1],current,u,current*current*rseries,current*current*(r-rseries),x[2]*x[2]*rm+x[1]*x[1]*1e-6])
   x=(eh@x+gh*u) if high else (el@x)
 arr=np.array(trace);vpp=np.ptp(arr[:,1]);pnet=np.mean(arr[:,2]*arr[:,3]);pr=np.mean(arr[:,4]);pd=np.mean(arr[:,5])
 pm=np.mean(arr[:,6]);result=dict(vpp_v=float(vpp),vmin_v=float(arr[:,1].min()),vmax_v=float(arr[:,1].max()),r_series_w=float(pr),driver_ron_w=float(pd),net_load_supply_w=float(pnet),max_edge_a=float(np.max(np.abs(arr[:,2]))),motional_plus_bleed_w=float(pm),discrete_energy_residual_w=float(pnet-pr-pd-pm))
 # remaining positive power is motional Rm + bleed loss; negative error means numerical error.
 return (result,trace) if return_trace else result
