"""Tk v5 runtime path editor; the validated legacy App remains available intact."""
import argparse, copy, json, os, queue, threading, time, tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import numpy as np
from ..prepcb.user_path import Document, sample
from ..prepcb.protocol import discover_ports
from ..prepcb.c_session import Session, build
from ..prepcb.temperature import Environment, Reading, compensate
from ..calibration.geometry import positions
from ..calibration.config import load
from ..motion.transport import RegisterTranscriptTransport, SimulationTransport
from ..motion.trap_solver import digest, TrapSolver
from ..motion.workspace import load_profile
from ..prepcb.field import TemperatureTrapSolver,nominal_reference
from .app import App as LegacyApp
ROOT=Path(__file__).resolve().parents[2]


class Editor:
    def __init__(self,root,output,automated=False):
        self.root=root;self.output=Path(output).resolve();self.output.mkdir(parents=True,exist_ok=True)
        self.document=Document();self.frames=None;self.selected=None;self.drag=None
        self.events=queue.Queue();self.session=None;self.stop_event=threading.Event();self.paused=False
        self.worker=None;self.rtl=None;self.result=None;self.automated=automated
        self.array_tx,self.array_rx=positions(load(),[0,0,.1,0,0,0],centered=True)
        root.title('SonoField v5 用户轨迹与校准');root.geometry('1450x950')
        style=ttk.Style();style.theme_use('clam')
        ttk.Label(root,text='SIMULATION · 开环声场指令 · 实际粒子位置未测量',font=('Microsoft YaHei UI',15)).pack(anchor='w',padx=15,pady=10)
        self.status=tk.StringVar(value='HARDWARE_NOT_READY；预览/主机 C 服务与 RTL 仿真可用。')
        ttk.Label(root,textvariable=self.status).pack(fill='x',padx=15)
        tabs=ttk.Notebook(root);tabs.pack(fill='both',expand=True,padx=15,pady=10)
        edit=ttk.Frame(tabs,padding=8);diag=ttk.Frame(tabs,padding=12);cal=ttk.Frame(tabs,padding=12)
        tabs.add(edit,text='用户轨迹');tabs.add(diag,text='连接与运行');tabs.add(cal,text='温度与稀疏校准')
        left=ttk.Frame(edit);left.pack(side='left',fill='y',padx=(0,12));right=ttk.Frame(edit);right.pack(side='left',fill='both',expand=True)
        self.tree=ttk.Treeview(left,columns=('x','y','z','speed','dwell'),show='headings',height=8)
        for key,title in [('x','X mm'),('y','Y mm'),('z','Z mm'),('speed','mm/s'),('dwell','停留 s')]:
            self.tree.heading(key,text=title);self.tree.column(key,width=72)
        self.tree.pack(fill='x');self.tree.bind('<<TreeviewSelect>>',self.select)
        self.xyz=[tk.StringVar(value='0') for _ in range(3)];self.speed=tk.StringVar(value='3');self.dwell=tk.StringVar(value='0')
        for label,var in list(zip(('X mm','Y mm','Z mm'),self.xyz))+[('速度 mm/s',self.speed),('停留 s',self.dwell)]:
            row=ttk.Frame(left);row.pack(fill='x',pady=3);ttk.Label(row,text=label,width=12).pack(side='left');ttk.Entry(row,textvariable=var,width=25).pack(side='left')
        for label,callback in [('添加点',self.add),('更新选中点',self.update),('在选中点前插入',lambda:self.add(True)),('删除点',self.delete),('上移顺序',lambda:self.reorder(-1)),('下移顺序',lambda:self.reorder(1))]:
            ttk.Button(left,text=label,command=lambda f=callback:self.guarded(f)).pack(fill='x',pady=2)
        row=ttk.Frame(left);row.pack(fill='x');ttk.Button(row,text='撤销',command=lambda:self.change(self.document.undo)).pack(side='left');ttk.Button(row,text='重做',command=lambda:self.change(self.document.redo)).pack(side='left')
        self.closed=tk.BooleanVar();ttk.Checkbutton(left,text='闭合当前用户路径',variable=self.closed,command=lambda:self.change(lambda:self.document.edit(lambda d:d.update(closed=self.closed.get())))).pack(anchor='w')
        ttk.Label(left,text='选中段的两控制柄 XYZ（6 个数）').pack(anchor='w',pady=(8,2))
        self.controls=tk.StringVar(value='0,0,0,0,0,0');ttk.Entry(left,textvariable=self.controls,width=44).pack(fill='x')
        ttk.Button(left,text='设为三次 Bezier 段',command=lambda:self.guarded(self.bezier)).pack(fill='x',pady=3)
        row=ttk.Frame(left);row.pack(fill='x');ttk.Button(row,text='保存 JSON',command=lambda:self.guarded(self.save)).pack(side='left');ttk.Button(row,text='重载并编辑',command=lambda:self.guarded(self.open)).pack(side='left')
        self.plane=tk.StringVar(value='XY');ttk.Combobox(right,textvariable=self.plane,values=['XY','XZ','YZ','3D'],state='readonly',width=10).pack(anchor='w')
        self.zoom=tk.DoubleVar(value=28)
        zoomrow=ttk.Frame(right);zoomrow.pack(fill='x');ttk.Label(zoomrow,text='缩放 px/mm（6 查看双阵列，400 精调短路径）').pack(side='left')
        ttk.Scale(zoomrow,from_=6,to=400,variable=self.zoom,command=lambda _:self.draw()).pack(side='left',fill='x',expand=True)
        self.plane.trace_add('write',lambda *_:self.draw())
        self.canvas=tk.Canvas(right,bg='white',width=850,height=580,highlightthickness=1,highlightbackground='#c8d2df');self.canvas.pack(fill='both',expand=True)
        self.canvas.bind('<Configure>',lambda e:self.draw());self.canvas.bind('<Button-1>',self.click);self.canvas.bind('<B1-Motion>',self.drag_point);self.canvas.bind('<ButtonRelease-1>',self.release)
        ttk.Label(right,text='点击空白添加运行时点；拖动顶点或橙色控制柄。3D 拖动保持当前 Z，XYZ 文本可改深度。\n边界为模型检查范围，未证明全范围真实悬浮。').pack(anchor='w',pady=5)
        self.summary=tk.StringVar(value='尚未规划');ttk.Label(right,textvariable=self.summary).pack(anchor='w')
        limits_row=ttk.Frame(right);limits_row.pack(fill='x',pady=4)
        self.limit_vars={key:tk.StringVar(value=str(self.document.data['limits'][key])) for key in ('speed_mm_s','acceleration_mm_s2','jerk_mm_s3')}
        for key,label in [('speed_mm_s','速度上限 mm/s'),('acceleration_mm_s2','加速度 ≤8'),('jerk_mm_s3','jerk ≤40')]:
            ttk.Label(limits_row,text=label).pack(side='left');ttk.Entry(limits_row,textvariable=self.limit_vars[key],width=8).pack(side='left',padx=3)
        ttk.Button(limits_row,text='应用约束',command=lambda:self.guarded(self.apply_limits)).pack(side='left')
        row=ttk.Frame(right);row.pack(fill='x',pady=5)
        for label,callback in [('验证/预览',self.preview),('人工确认仿真 START',self.start),('暂停',self.pause),('继续',self.resume),('STOP/断开',self.stop)]:
            ttk.Button(row,text=label,command=lambda f=callback:self.guarded(f)).pack(side='left',padx=3)
        ttk.Button(diag,text='枚举串口（仅查询）',command=lambda:self.diagnostics.set(json.dumps(discover_ports(),ensure_ascii=False,indent=2))).pack(anchor='w')
        self.diagnostics=tk.StringVar(value='硬件连接门禁未闭合：Rev3/UART 所有权、平台和独立安全链待验证。\n115200 8N1：11520 byte/s；16384B raw 理想至少 1.422s。\n运动任务先完整上传，50Hz 主机 C 参考调度；40kHz PL 载波独立。')
        ttk.Label(diag,textvariable=self.diagnostics,wraplength=1200).pack(anchor='w',pady=8)
        ttk.Button(diag,text='打开既有已验证控制界面',command=self.legacy).pack(anchor='w')
        self.log=tk.Text(diag,height=25,font=('Consolas',10));self.log.pack(fill='both',expand=True)
        self.temps=[tk.StringVar(value=str(v)) for v in (25,26,24)]
        for label,var in zip(('中心 TMP117 °C','上板 TMP117 °C','下板 TMP117 °C'),self.temps):
            row=ttk.Frame(cal);row.pack(anchor='w',pady=4);ttk.Label(row,text=label,width=22).pack(side='left');ttk.Entry(row,textvariable=var).pack(side='left')
        ttk.Label(cal,text='此处为显式 SYNTHETIC_REFERENCE 输入；真实温度暂无。RH 修正未应用，pressure_assumed。').pack(anchor='w',pady=8)
        ttk.Button(cal,text='生成并拟合稀疏参考（非硬件校准）',command=lambda:self.guarded(self.calibrate)).pack(anchor='w')
        self.cal_info=tk.StringVar(value='16+16 个对角线 TX，单 TX → 对侧 4 RX，共128路径。RX 坐标名义 (±54,±54) mm；TX 正向相对参考两锚点。')
        ttk.Label(cal,textvariable=self.cal_info,wraplength=1250).pack(anchor='w',pady=15)
        root.protocol('WM_DELETE_WINDOW',self.close);self.poll_handle=root.after(100,self.poll)

    def guarded(self,callback):
        try:return callback()
        except Exception as exc:
            self.status.set(str(exc))
            if not self.automated:messagebox.showerror('操作未执行',str(exc),parent=self.root)
            else:raise

    def change(self,callback):
        if self.worker and self.worker.is_alive():raise RuntimeError('先停止当前任务再编辑')
        callback();self.frames=None;self.refresh()

    def apply_limits(self):
        limits={k:float(v.get()) for k,v in self.limit_vars.items()}
        if limits['acceleration_mm_s2']>8 or limits['jerk_mm_s3']>40:
            raise ValueError('当前 C 接收门禁：加速度≤8mm/s²，jerk≤40mm/s³')
        self.change(lambda:self.document.edit(lambda d:d['limits'].update(limits)))

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        for i,v in enumerate(self.document.data['vertices']):self.tree.insert('', 'end',iid=str(i),values=[*v['xyz'],v['speed_mm_s'],v['dwell_s']])
        self.closed.set(self.document.data['closed']);self.draw()
        for key,var in self.limit_vars.items():var.set(str(self.document.data['limits'][key]))

    def select(self,event=None):
        items=self.tree.selection()
        if not items:return
        self.selected=int(items[0]);v=self.document.data['vertices'][self.selected]
        for var,value in zip(self.xyz,v['xyz']):var.set(str(value))
        self.speed.set(str(v['speed_mm_s']));self.dwell.set(str(v['dwell_s']));self.draw()

    def add(self,insert=False):
        self.change(lambda:self.document.add([float(v.get()) for v in self.xyz],index=self.selected if insert else None,dwell=float(self.dwell.get()),speed=float(self.speed.get())))

    def update(self):
        if self.selected is None:raise ValueError('先选择顶点')
        def update(d):d['vertices'][self.selected].update(xyz=[float(v.get()) for v in self.xyz],speed_mm_s=float(self.speed.get()),dwell_s=float(self.dwell.get()))
        self.change(lambda:self.document.edit(update))

    def delete(self):
        if self.selected is not None:self.change(lambda:self.document.delete(self.selected));self.selected=None

    def reorder(self,step):
        if self.selected is None:return
        target=max(0,min(len(self.document.data['vertices'])-1,self.selected+step))
        self.change(lambda:self.document.reorder(self.selected,target));self.selected=target

    def bezier(self):
        if self.selected is None:raise ValueError('先选中段的起点')
        values=[float(x) for x in self.controls.get().split(',')]
        if len(values)!=6:raise ValueError('需要两个 XYZ 控制柄')
        self.change(lambda:self.document.bezier(self.selected,values[:3],values[3:]))

    def project(self,p):
        mode=self.plane.get();a,b={'XY':(0,1),'XZ':(0,2),'YZ':(1,2),'3D':(0,1)}[mode]
        scale=self.zoom.get()
        if mode=='3D':return self.canvas.winfo_width()/2+scale*(p[0]+.45*p[2]),self.canvas.winfo_height()/2-scale*(p[1]+.3*p[2])
        return self.canvas.winfo_width()/2+scale*p[a],self.canvas.winfo_height()/2-scale*p[b]

    def draw(self):
        c=self.canvas;c.delete('all');w,h=c.winfo_width(),c.winfo_height()
        c.create_line(w/2,0,w/2,h,fill='#dde3ed');c.create_line(0,h/2,w,h/2,fill='#dde3ed')
        c.create_text(12,12,anchor='nw',text='名义阵列：灰128TX / 紫8RX / 箭头发射法向；坐标 mm；非实测',fill='#526071')
        for point in self.array_tx*1000:
            x,y=self.project(point);c.create_oval(x-2,y-2,x+2,y+2,fill='#a5afba',outline='')
        for point in self.array_rx*1000:
            x,y=self.project(point);c.create_rectangle(x-3,y-3,x+3,y+3,fill='#875a9f',outline='')
        for z in (-50,50):
            x,y=self.project([0,0,z]);a,b=self.project([0,0,z-np.sign(z)*10]);c.create_line(x,y,a,b,arrow='last',fill='#875a9f')
        if self.frames and len(self.frames)>1:c.create_line(*[v for r in self.frames for v in self.project([r[k] for k in ('x_mm','y_mm','z_mm')])],fill='#167d85',width=2)
        for i,v in enumerate(self.document.data['vertices']):
            x,y=self.project(v['xyz']);c.create_oval(x-5,y-5,x+5,y+5,fill='#1f4e78' if i!=self.selected else '#bc3345');c.create_text(x+12,y-9,text=str(i))
        for s in self.document.data['segments']:
            for key in ('control1','control2'):
                x,y=self.project(s[key]);c.create_rectangle(x-4,y-4,x+4,y+4,fill='#d67b22')

    def click(self,event):
        if self.worker and self.worker.is_alive():return
        candidates=[]
        for s in self.document.data['segments']:
            for key in ('control1','control2'):
                x,y=self.project(s[key])
                candidates.append(((x-event.x)**2+(y-event.y)**2,('control',s['index'],key)))
        for i,v in enumerate(self.document.data['vertices']):
            x,y=self.project(v['xyz'])
            candidates.append(((x-event.x)**2+(y-event.y)**2,('vertex',i,None)))
        if candidates:
            distance,picked=min(candidates,key=lambda x:x[0])
            if distance<144:
                self.drag=picked
                if picked[0]=='vertex':self.selected=picked[1];self.tree.selection_set(str(self.selected))
                return
        p=[float(v.get()) for v in self.xyz];a,b={'XY':(0,1),'XZ':(0,2),'YZ':(1,2),'3D':(0,1)}[self.plane.get()]
        p[a]=(event.x-self.canvas.winfo_width()/2)/self.zoom.get();p[b]=-(event.y-self.canvas.winfo_height()/2)/self.zoom.get()
        if self.plane.get()=='3D':p[0]-=.45*p[2];p[1]-=.3*p[2]
        self.guarded(lambda:self.change(lambda:self.document.add(p,speed=float(self.speed.get()),dwell=float(self.dwell.get()))))

    def drag_point(self,event):
        if not self.drag:return
        kind,index,key=self.drag;a,b={'XY':(0,1),'XZ':(0,2),'YZ':(1,2),'3D':(0,1)}[self.plane.get()]
        p=(self.document.data['vertices'][index]['xyz'][:] if kind=='vertex' else next(s[key][:] for s in self.document.data['segments'] if s['index']==index))
        p[a]=(event.x-self.canvas.winfo_width()/2)/self.zoom.get();p[b]=-(event.y-self.canvas.winfo_height()/2)/self.zoom.get()
        if self.plane.get()=='3D':p[0]-=.45*p[2];p[1]-=.3*p[2]
        if kind=='vertex':self.guarded(lambda:self.change(lambda:self.document.move(index,p)))
        else:
            s=next(s for s in self.document.data['segments'] if s['index']==index)
            self.guarded(lambda:self.change(lambda:self.document.bezier(index,p if key=='control1' else s['control1'],p if key=='control2' else s['control2'])))

    def release(self,event):self.drag=None

    def preview(self):
        values=[float(t.get()) for t in self.temps]
        env=Environment([Reading('TMP117_'+k.upper(),k,0,v,provenance='SYNTHETIC_REFERENCE') for k,v in zip(('center','upper','lower'),values)],0)
        record=nominal_reference(json.loads((ROOT/'simulation/fixtures/calibration_reference.json').read_text()))
        solver=TemperatureTrapSolver(load(),record,load_profile(),env)
        reports={}
        def phases(point):
            rows,report=solver.solve(point)
            if report['validity']!='TRAP_VALID':raise ValueError('温度声场模型拒绝目标；不能发送')
            reports[tuple(point)]=report
            return [r['requested_phase'] for r in rows]
        self.frames=sample(self.document,phases)
        for f in self.frames:phases([f[k] for k in ('x_mm','y_mm','z_mm')])
        self.document.data['calibration_snapshot']=dict(classification='SYNTHETIC_REFERENCE',temperature=env.metadata(),phase_reference='NOMINAL_ZERO_ERROR_REFERENCE_NOT_HARDWARE')
        self.summary.set(f'{len(self.frames)} 帧，{self.frames[-1]["t_s"]:.2f}s，50Hz；温度积分/模型局部陷阱/相位步进已检查')
        (self.output/'preview_traps.json').write_text(json.dumps(list(reports.values()),indent=2),encoding='utf-8')
        self.draw();return self.frames

    def save(self):
        path=filedialog.asksaveasfilename(defaultextension='.json',parent=self.root)
        if path:self.document.save(path)

    def open(self):
        path=filedialog.askopenfilename(filetypes=[('User path','*.json')],parent=self.root)
        if path:self.document=Document.load(path);self.frames=None;self.refresh()

    def start(self):
        if self.worker and self.worker.is_alive():raise RuntimeError('当前任务正在运行')
        frames=copy.deepcopy(self.preview());values=tuple(float(t.get()) for t in self.temps)
        self.document.save(self.output/'user_input.json')
        self.stop_event.clear();self.paused=False
        def work():
            try:
                library=build(ROOT/'build/prepcb_gui_runtime');self.session=Session(library,values)
                self.session.client.upload(frames);self.session.client.command('MOTION_START')
                while self.session.lib.fixture_cursor()<len(frames):
                    if self.stop_event.is_set():raise RuntimeError('STOPPED_REARM_REQUIRED')
                    if self.paused:self.session.tick();time.sleep(.02);continue
                    self.session.tick();self.events.put(('cursor',self.session.lib.fixture_cursor()));time.sleep(.02)
                transcript=RegisterTranscriptTransport();transcript.frames=self.session.maps();transcript.write_count=len(transcript.frames)*385
                self.rtl=SimulationTransport(self.output/'rtl')
                result=self.rtl.execute(transcript,40000)
                self.result=dict(status='PASS',classification=self.session.classification,frames=len(frames),rtl=result,
                                 path_sha256=digest(frames),protocol_trace=self.session.trace,actual_particle_position='NOT_MEASURED')
                (self.output/'user_path_result.json').write_text(json.dumps(self.result,indent=2),encoding='utf-8');self.events.put(('done',self.result))
            except Exception as exc:self.events.put(('error',str(exc)))
        self.worker=threading.Thread(target=work,daemon=True);self.worker.start()

    def pause(self):
        if self.session:self.session.client.command('MOTION_PAUSE');self.paused=True;self.status.set('C 服务已暂停；当前位置保持为指令模型，非实测粒子位置')

    def resume(self):
        if self.session and self.paused:self.session.client.command('MOTION_RESUME');self.paused=False

    def stop(self):
        self.stop_event.set();self.paused=False
        if self.session:
            try:self.session.client.command('MOTION_STOP')
            except Exception:pass
            self.session=None
        if self.rtl:self.rtl.stop()
        self.status.set('SAFE/OFF；必须再次人工启动，不自动恢复')

    def calibrate(self):
        # Import the explicit numerical reference generator, never an ADC reading.
        from ..prepcb.reference import synthetic_observations
        from ..prepcb.sparse import solve
        values=[float(t.get()) for t in self.temps]
        env=Environment([Reading('TMP117_'+k.upper(),k,0,v,provenance='SYNTHETIC_REFERENCE') for k,v in zip(('center','upper','lower'),values)],0)
        observations=synthetic_observations(7020,env)
        result=solve(load(),observations,env)
        (self.output/'sparse_reference_result.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
        self.cal_info.set(f'{result["classification"]}；{result["grade"]}；rank {result["rank"]}；condition {result["condition"]:.1f}；128 TX 单体仍 UNMEASURED。')

    def legacy(self):LegacyApp(tk.Toplevel(self.root),self.output/'legacy')

    def poll(self):
        while not self.events.empty():
            kind,value=self.events.get()
            if kind=='cursor':self.status.set(f'HOST_FIXTURE 已提交 {value}/{len(self.frames or [])}；等待批次 RTL ACK 交叉验证')
            else:self.status.set(str(value)[:250]);self.log.insert('end',json.dumps(value,ensure_ascii=False)+'\n')
        self.poll_handle=self.root.after(100,self.poll)

    def close(self):
        self.stop();self.root.after_cancel(self.poll_handle);self.root.destroy()


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'evidence/pre_pcb_20261009/gui_manual');a=p.parse_args()
    root=tk.Tk();Editor(root,a.output);root.mainloop()

if __name__=='__main__':main()
