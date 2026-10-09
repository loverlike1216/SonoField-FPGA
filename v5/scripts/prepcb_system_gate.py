"""Bounded numerical references + actual GUI callbacks + C bytes + two RTL tools.

Nothing here represents a sensor reading, real UART, particle or board result.
"""
import argparse, copy, ctypes, hashlib, json, os, sys, time,shutil
from pathlib import Path
from types import SimpleNamespace
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import numpy as np
from software.prepcb.temperature import Environment,Reading
from software.prepcb.reference import synthetic_observations
from software.prepcb.sparse import solve,scan_plan
from software.prepcb.c_session import Session,build
from software.prepcb.field import TemperatureTrapSolver,nominal_reference
from software.prepcb.user_path import Document
from software.calibration.config import load
from software.calibration.geometry import positions
from software.motion.workspace import load_profile
from software.motion.transport import RegisterTranscriptTransport,SimulationTransport
from software.motion.trap_solver import digest

def env(values,gap=.1):
    return Environment([Reading('TMP117_'+k.upper(),k,0,v,provenance='SYNTHETIC_REFERENCE')
                        for k,v in zip(('center','upper','lower'),values)],0,gap_m=gap)

def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def rejected(callback):
    try:callback()
    except ValueError as exc:return str(exc)
    raise AssertionError('Unsafe calibration unexpectedly accepted')

def sparse_gate(out):
    expected=np.array([.0007,-.0005,.1008,.35,-.2,.15]);config=load();fits=[]
    for seed in range(7020,7025):
        for temperatures in ((25,25,25),(25,31,19)):
            e=env(temperatures);observations=synthetic_observations(seed,e)
            result=solve(config,observations,e);pose=np.array(result['pose'])
            error=abs(pose-expected)
            assert np.linalg.norm(error[:3])<.0001 and np.linalg.norm(error[3:])<.1
            assert result['rank']==12 and all(c['status']=='UNMEASURED' for c in result['channels'])
            true_tx,true_rx=positions(config,expected,centered=True)
            fitted_tx,fitted_rx=positions(config,pose,centered=True)
            # Independent holdout excludes every diagonal TX used in fitting.
            used={t for t,_ in scan_plan()};holdout=[]
            for tx in range(128):
                if tx in used:continue
                for rx in (range(4,8) if tx<64 else range(4)):
                    actual=e.reference_time(true_tx[tx],true_rx[rx])+[0,.2,-.15,.1,0,-.1,.15,-.2][rx]*1e-6
                    prediction=e.travel_time(fitted_tx[tx],fitted_rx[rx])+result['receiver_delay_us'][rx]*1e-6
                    holdout.append(prediction-actual)
            assert np.max(np.abs(holdout))<80e-9
            result.update(seed=seed,translation_error_mm=(error[:3]*1000).tolist(),rotation_error_deg=error[3:].tolist(),
                holdout_paths=len(holdout),holdout_max_error_ns=float(np.max(np.abs(holdout))*1e9),
                observation_sha256=digest(observations))
            label=f'{seed}_'+('_'.join(map(str,temperatures)))
            save(out/(label+'_observations.json'),observations);save(out/(label+'_result.json'),result)
            fits.append(result);print('SPARSE',label,'PASS',flush=True)
    e=env((25,25,25));obs=synthetic_observations(7020,e)
    repeat=solve(config,obs,e)
    assert digest(repeat['pose'])==digest(fits[0]['pose'])
    missing=rejected(lambda:solve(config,[o for o in obs if o['rx_id']!=7],e))
    ambiguous=copy.deepcopy(obs)
    for o in ambiguous:o['coarse_uncertainty_s']=20e-6
    ambiguous=rejected(lambda:solve(config,ambiguous,e))
    bad=copy.deepcopy(obs)
    for o in bad:o['SNR']=34.9
    low_snr=rejected(lambda:solve(config,bad,e))
    robust=copy.deepcopy(obs)
    for i in (5,23,80):
        robust[i]['phase']=(robust[i]['phase']+2*np.pi*40000*1e-6)%(2*np.pi)
        robust[i]['TOF_candidate']+=1e-6
    robust_result=solve(config,robust,e)
    assert len(robust_result['rejected'])>=3
    assert np.max(abs(np.array(robust_result['pose'])[:3]-expected[:3]))<.0001
    save(out/'robust_result.json',robust_result)
    return dict(status='PASS',fits=10,seeds=5,initial_guesses_per_fit=5,holdout_paths_per_fit=fits[0]['holdout_paths'],
                maximum_translation_error_mm=max(max(r['translation_error_mm']) for r in fits),
                maximum_rotation_error_deg=max(max(r['rotation_error_deg']) for r in fits),
                maximum_holdout_error_ns=max(r['holdout_max_error_ns'] for r in fits),
                rejection_cases=dict(missing_rx=missing,ambiguous_phase=ambiguous,low_snr=low_snr),
                robust_rejected=len(robust_result['rejected']),deterministic_repeat=True),fits[0]

def phase_gate(library,out,fit):
    lib=ctypes.CDLL(str(library));f=lib.fixture_phase_map
    f.argtypes=[ctypes.POINTER(ctypes.c_int32),ctypes.POINTER(ctypes.c_int16),ctypes.POINTER(ctypes.c_uint8),ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_uint32)]
    rng=np.random.default_rng(20261009);checks=[]
    for pose in ([0,0,.1,0,0,0],fit['pose']):
        tx,_=positions(load(),pose,centered=True)
        for temperatures in ((25,25,25),(25,31,19)):
            e=env(temperatures,pose[2]);worst=0
            for _ in range(40):
                nm=np.rint(rng.uniform([-.002,-.002,-.001],[.002,.002,.001])*1e9).astype(np.int32)
                target=nm*1e-9;cal=rng.integers(0,256,128,dtype=np.uint8)
                expected=[0x10000|(int(cal[c])<<8)|((int(np.rint(-40000*e.travel_time(tx[c],target)*256))+(128 if c>=64 else 0))%256) for c in range(128)]
                words=(ctypes.c_uint32*128)()
                f((ctypes.c_int32*3)(*nm),(ctypes.c_int16*3)(*[round(t*128) for t in temperatures]),
                  (ctypes.c_uint8*128)(*cal),(ctypes.c_double*6)(*pose),words)
                assert list(words)==expected,'Python/C phase or calibration word mismatch'
                for source in tx[::16]:worst=max(worst,abs(e.travel_time(source,target)-e.reference_time(source,target)))
            checks.append(dict(pose=pose,temperatures=temperatures,maps=40,channels=5120,
                               maximum_independent_integral_error_s=worst))
    # Independently generated signed ADC-like vector, not recorded ADC data.
    n=800;t=np.arange(n)/800000;raw=np.zeros((n,8),dtype=np.int16)
    raw[:,3]=np.rint(1200*np.cos(2*np.pi*40000*t+.42)).astype(np.int16)
    features=lib.fixture_features
    features.argtypes=[ctypes.POINTER(ctypes.c_int16),ctypes.c_uint,ctypes.c_uint,ctypes.c_double,ctypes.c_double,
                       ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_double)]
    amp,phase,coarse=ctypes.c_double(),ctypes.c_double(),ctypes.c_double()
    assert features(raw.ctypes.data_as(ctypes.POINTER(ctypes.c_int16)),n,3,800000,40000,ctypes.byref(amp),ctypes.byref(phase),ctypes.byref(coarse))==0
    expected=2*np.sum(raw[:,3]*np.exp(-2j*np.pi*40000*t))/n
    assert abs(amp.value-abs(expected))<1e-8 and abs(phase.value-np.angle(expected))<1e-10
    result=dict(status='PASS',maps=160,channel_words=20480,checks=checks,adc_features=dict(classification='SYNTHETIC_SIGNED_VECTOR',amplitude=amp.value,phase=phase.value,coarse_estimate_s=coarse.value))
    save(out/'summary.json',result);return result

def gui_gate(library,out):
    import tkinter as tk
    from software.ui.prepcb_app import Editor
    rng=np.random.default_rng(20261009);results=[]
    for case in range(5):
        folder=out/f'case_{case+1}';folder.mkdir(parents=True)
        root=tk.Tk();app=Editor(root,folder,automated=True);root.update()
        offset=rng.uniform(-.05,.05,3)
        points=[offset,offset+[.18,.04,.02]]
        if case>=2:points.append(offset+[.09,.18,-.03])
        # Actual entry variables and application callbacks, created at runtime.
        for point in points:
            for var,v in zip(app.xyz,point):var.set(format(v,'.9f'))
            app.add()
        app.document.undo();app.document.redo();app.refresh()
        if case==1:
            app.plane.set('XZ');x,y=app.project(app.document.data['vertices'][1]['xyz'])
            app.click(SimpleNamespace(x=x,y=y));app.drag_point(SimpleNamespace(x=x+1,y=y-1));app.release(None)
        if case==2:
            app.selected=0;app.controls.set(','.join(map(str,np.r_[offset+[.08,.11,.02],offset+[.12,-.02,0]])))
            app.bezier()
        if case==3:app.change(lambda:app.document.edit(lambda d:d.update(closed=True)))
        if case==4:
            app.selected=1;app.add(True);app.document.delete(1);app.document.reorder(1,2);app.document.reorder(2,1);app.refresh()
        frames=app.preview();app.document.save(folder/'runtime_user_input.json')
        assert digest(Document.load(folder/'runtime_user_input.json').data)==digest(app.document.data)
        assert len(frames)<=512
        if case==2:
            root.lift();root.attributes('-topmost',True);root.update();time.sleep(.2);root.update()
            from PIL import ImageGrab
            ImageGrab.grab(bbox=(root.winfo_rootx(),root.winfo_rooty(),root.winfo_rootx()+root.winfo_width(),root.winfo_rooty()+root.winfo_height())).save(folder/'gui.png')
        app.close()
        session=Session(library);session.client.upload(frames);session.client.command('MOTION_START')
        session.tick();session.client.command('MOTION_PAUSE');before=session.lib.fixture_cursor()
        for _ in range(3):session.tick()
        assert session.lib.fixture_cursor()==before
        session.client.command('MOTION_RESUME')
        for _ in range(len(frames)+2):session.tick()
        maps=session.maps();assert len(maps)==len(frames)
        solver=TemperatureTrapSolver(load(),nominal_reference(json.loads((ROOT/'simulation/fixtures/calibration_reference.json').read_text())),load_profile(),env((25,26,24)))
        for point,words in zip(frames,maps):
            target=[round(point[k]*1e6)/1e6 for k in ('x_mm','y_mm','z_mm')]
            rows,report=solver.solve(target);assert report['validity']=='TRAP_VALID'
            assert [0x10000|(r['calibration_phase']<<8)|r['requested_phase'] for r in rows]==words
        transcript=RegisterTranscriptTransport();transcript.frames=maps;transcript.write_count=len(maps)*385
        rtl=[SimulationTransport(folder/s,simulator=s).execute(transcript,40000) for s in ('icarus','xsim')]
        assert rtl[0]['ack_sha256']==rtl[1]['ack_sha256']
        result=dict(status='PASS',input='AUTOMATED_RUNTIME_GUI_ENTRY_AND_CALLBACKS',human_manual_test=False,
                    frames=len(frames),path_sha256=digest(frames),maps_sha256=digest(maps),protocol_trace=session.trace,
                    pause_holds_cursor=True,python_c_maps_bit_exact=True,rtl=rtl,actual_particle_position='NOT_MEASURED')
        save(folder/'summary.json',result);results.append(result);print('GUI_CASE',case+1,'PASS',len(frames),flush=True)
    return dict(status='PASS',runtime_inputs=5,total_frames=sum(r['frames'] for r in results),results=results)

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT/'evidence'):raise ValueError('Output outside v5 evidence')
    out.mkdir(parents=True,exist_ok=True)
    if (out/'summary.json').exists():raise ValueError('Fresh evidence label required')
    summary=dict(status='RUNNING',classification='ALTERNATIVE_VALIDATION_AND_SIMULATED_NO_PHYSICAL_HARDWARE',started_at=time.time())
    try:
        library=build(ROOT/'build/prepcb_system_gate'/out.name)
        shutil.copyfile(library.parent/'compile.log',out/'c_compile.log')
        summary['sparse'],fit=sparse_gate(out/'sparse')
        summary['phase']=phase_gate(library,out/'phase',fit)
        summary['gui']=gui_gate(library,out/'gui')
        summary['status']='PASS'
    except Exception as exc:summary.update(status='FAIL',error=str(exc));raise
    finally:save(out/'summary.json',summary)

if __name__=='__main__':main()
