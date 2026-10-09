"""Run with python -m software.ui.app from v5. Built-in Tk avoids a new GUI dependency."""
import argparse
import copy
import json
import queue
import threading
import tkinter as tk
from tkinter import ttk,messagebox,filedialog
from pathlib import Path
from ..calibration.config import load
from ..motion.workspace import load_profile
from ..motion.motion_controller import MotionController,demo_commands
from ..motion.transport import SimulationTransport
from ..motion.commands import encode
from ..motion.trap_solver import digest
from ..motion.trajectory import xyz

ROOT=Path(__file__).resolve().parents[2]
DEFAULT_CALIBRATION=ROOT/'simulation/fixtures/calibration_reference.json'
PRESETS={
 'LINE':{'start':[-5,0],'end':[5,0]},
 'CIRCLE':{'center':[0,0],'radius':5,'start_angle_deg':0,'sweep_deg':360},
 'SEMICIRCLE':{'center':[0,0],'radius':5,'start_angle_deg':0,'sweep_deg':180},
 'ELLIPSE':{'center':[0,0],'a':6,'b':3,'rotation_deg':0},
 'HYPERBOLA_SEGMENT':{'center':[0,0],'a':2,'b':2,'interval':[-1,1],'branch':1,'rotation_deg':0},
 'TRIANGLE':{'center':[0,0],'radius':5,'rotation_deg':0},
 'RECTANGLE':{'center':[0,0],'width':8,'height':6,'rotation_deg':0},
 'CUSTOM_WAYPOINTS':{'vertices':[[-4,-3],[4,-3],[4,3],[-4,3]],'closed':False}}


class App:
    def __init__(self,root,output,simulator='icarus',automated=False):
        self.root=root;self.output=Path(output).resolve();self.output.mkdir(parents=True,exist_ok=True)
        self.model=MotionController(load(),load_profile(),SimulationTransport(self.output/'rtl',simulator=simulator),self.output/'commands.jsonl')
        self.sequence=0;self.events=queue.Queue();self.preview_path=None;self.preview_command=None;self.automated=automated
        self.worker=None;self.results=[];self.completed_callback=None;self.error=None
        root.title('SonoField-FPGA v5 | 指令陷阱控制 · SIMULATION');root.geometry('1360x920');root.minsize(1200,820)
        root.configure(bg='#eef2f7');root.option_add('*Font',('Microsoft YaHei UI',10))
        style=ttk.Style();style.theme_use('clam');style.configure('TButton',padding=7);style.configure('TLabelframe.Label',font=('Microsoft YaHei UI',11,'bold'))
        top=tk.Frame(root,bg='#152b46',padx=22,pady=12);top.pack(fill='x')
        tk.Label(top,text='SonoField  /  v5',bg='#152b46',fg='white',font=('Segoe UI',22,'bold')).pack(side='left')
        tk.Label(top,text='SIMULATION  ·  开环指令控制\n实际粒子位置未测量',bg='#152b46',fg='#96e4dd',font=('Microsoft YaHei UI',11)).pack(side='right')
        self.state=tk.StringVar();ttk.Label(root,textvariable=self.state,padding=(18,10),font=('Microsoft YaHei UI',11)).pack(fill='x')
        body=ttk.Frame(root,padding=(15,0,15,10));body.pack(fill='both',expand=True)
        left=ttk.Frame(body,width=450);left.pack(side='left',fill='y',padx=(0,15));right=ttk.Frame(body);right.pack(side='left',fill='both',expand=True)
        safety=ttk.LabelFrame(left,text='1  连接 → 校准 → 中心陷阱 → 人工确认',padding=10);safety.pack(fill='x')
        row=ttk.Frame(safety);row.pack(fill='x')
        ttk.Button(row,text='连接仿真',command=lambda:self.action('CONNECT')).pack(side='left')
        ttk.Button(row,text='加载校准',command=self.load_record).pack(side='left',padx=5)
        ttk.Button(row,text='应用中心陷阱',command=lambda:self.action('APPLY_CENTER')).pack(side='left')
        self.confirm=ttk.Button(safety,text='已确认球位于中心 · 允许运动',command=lambda:self.action('BALL_AT_CENTER_CONFIRMED'));self.confirm.pack(fill='x',pady=(8,0))
        ttk.Label(safety,text='仿真确认仅用于数字验证；硬件接口保持关闭。').pack(anchor='w',pady=(5,0))
        point=ttk.LabelFrame(left,text='2  点移动 / 返回中心（mm）',padding=10);point.pack(fill='x',pady=10)
        self.fields={}
        for i,(name,value) in enumerate((('X',5),('Y',0),('Z',0),('速度 mm/s',3))):
            ttk.Label(point,text=name).grid(row=0,column=i,padx=4)
            v=tk.StringVar(value=str(value));self.fields[name]=v
            ttk.Entry(point,textvariable=v,width=9).grid(row=1,column=i,padx=4,pady=5)
        ttk.Button(point,text='预览点移动',command=self.preview_point).grid(row=2,column=0,columnspan=2,sticky='ew')
        ttk.Button(point,text='平滑返回中心',command=lambda:self.action('RETURN_CENTER')).grid(row=2,column=2,columnspan=2,sticky='ew')
        planar=ttk.LabelFrame(left,text='3  平面轨迹 · 固定 Z（mm / degrees）',padding=10);planar.pack(fill='x')
        self.kind=tk.StringVar(value='CIRCLE');combo=ttk.Combobox(planar,textvariable=self.kind,values=list(PRESETS),state='readonly',width=28);combo.pack(fill='x');combo.bind('<<ComboboxSelected>>',lambda _:self.preset())
        self.parameters=tk.Text(planar,height=6,width=42,font=('Consolas',10),wrap='word');self.parameters.pack(fill='x',pady=6);self.preset()
        row=ttk.Frame(planar);row.pack(fill='x');self.z=tk.StringVar(value='0');self.repeat=tk.StringVar(value='1');self.clockwise=tk.BooleanVar()
        ttk.Label(row,text='固定 Z').pack(side='left');ttk.Entry(row,textvariable=self.z,width=6).pack(side='left',padx=4)
        ttk.Label(row,text='重复').pack(side='left');ttk.Entry(row,textvariable=self.repeat,width=5).pack(side='left',padx=4)
        ttk.Checkbutton(row,text='顺时针 / 反向',variable=self.clockwise).pack(side='left')
        ttk.Button(planar,text='预览轨迹（不发送）',command=self.preview_shape).pack(fill='x',pady=(7,0))
        vertical=ttk.LabelFrame(left,text='4  垂直控制 · XY 保持不变',padding=10);vertical.pack(fill='x',pady=10)
        row=ttk.Frame(vertical);row.pack(fill='x');self.vspeed=tk.StringVar(value='2');self.step=tk.StringVar(value='1')
        for text,var in [('速度 mm/s',self.vspeed),('步长 mm',self.step)]:
            ttk.Label(row,text=text).pack(side='left');ttk.Entry(row,textvariable=var,width=6).pack(side='left',padx=5)
        row=ttk.Frame(vertical);row.pack(fill='x',pady=(6,0))
        for label,direction in [('↑ 上移',1),('↓ 下移',-1),('回到 Z=0',0)]:
            ttk.Button(row,text=label,command=lambda d=direction:self.vertical(d)).pack(side='left',expand=True,fill='x')
        ttk.Button(left,text='运行完整数字演示',command=self.demo).pack(fill='x')
        ttk.Label(right,text='Commanded trap position  /  指令陷阱位置',font=('Segoe UI',15,'bold')).pack(anchor='w')
        self.position=tk.StringVar(value='X 0.00   Y 0.00   Z 0.00 mm');ttk.Label(right,textvariable=self.position,font=('Consolas',21),foreground='#137d77').pack(anchor='w',pady=5)
        self.canvas=tk.Canvas(right,bg='white',height=470,highlightthickness=0);self.canvas.pack(fill='both',expand=True);self.canvas.bind('<Configure>',lambda _:self.draw())
        self.preview_info=tk.StringVar(value='先预览轨迹，再发送。坐标原点为辐射面几何中心。');ttk.Label(right,textvariable=self.preview_info,wraplength=760).pack(anchor='w',pady=8)
        row=ttk.Frame(right);row.pack(fill='x')
        self.send=ttk.Button(row,text='发送预览轨迹',command=self.send_preview);self.send.pack(side='left',fill='x',expand=True)
        ttk.Button(row,text='HOLD 保持',command=lambda:self.action('HOLD')).pack(side='left',padx=8)
        tk.Button(row,text='STOP  立即停用',bg='#be293a',fg='white',activebackground='#912033',font=('Segoe UI',14,'bold'),command=self.stop,padx=25,pady=6).pack(side='right')
        self.log=tk.Text(right,height=7,bg='#f7f9fc',font=('Consolas',10),state='disabled');self.log.pack(fill='x',pady=(10,0))
        ttk.Label(root,text='演示范围 X/Y ±10 mm · Z ±6 mm  |  水平 0.5–10 mm/s · 垂直 0.5–5 mm/s  |  50 Hz逻辑更新  |  未验证实际悬浮',padding=(18,7)).pack(fill='x')
        root.protocol('WM_DELETE_WINDOW',self.close);root.after(100,self.poll);self.refresh()

    def note(self,text):
        self.log.configure(state='normal');self.log.insert('end',text+'\n');self.log.see('end');self.log.configure(state='disabled')

    def packet(self,command,payload=None):
        packet=encode(self.sequence,command,payload);self.sequence+=1;return packet

    def action(self,command,payload=None,path=None,callback=None):
        if self.worker and self.worker.is_alive() and command not in ('STOP','GET_STATUS'):
            self.note('MOTION_BUSY');return
        packet=self.packet(command,payload)
        self.note(command+'  '+json.dumps(payload or {},ensure_ascii=False))
        def work():
            try:
                result=self.model.dispatch(packet,prepared_path=path)
                # A later preview may replace self.preview_path before the UI polls.
                # Persist the exact path handed to dispatch, after its evaluation.
                executed_path=copy.deepcopy(path) if path is not None else None
                execution=copy.deepcopy(self.model.last_result)
                self.events.put(('done',(command,result,callback,execution,executed_path)))
            except Exception as exc:self.events.put(('error',str(exc)))
        self.worker=threading.Thread(target=work,daemon=True);self.worker.start();self.refresh()

    def load_record(self,path=None):
        try:
            record=json.loads(Path(path or DEFAULT_CALIBRATION).read_text())
            key=digest(record);self.model.calibration_records[key]=record
            self.action('LOAD_CALIBRATION',{'calibration_id':key})
        except Exception as exc:self.note(str(exc))

    def preset(self):
        self.parameters.delete('1.0','end');self.parameters.insert('1.0',json.dumps(PRESETS[self.kind.get()],indent=2))

    def set_preview(self,command,payload):
        try:
            self.preview_path=self.model.preview(command,payload);self.preview_command=(command,payload)
            self.preview_info.set(f"{command}  |  {len(self.preview_path)} 点  |  {self.preview_path[-1]['timestamp_target']:.2f} s  |  起止点见图；发送完全相同的采样点")
            self.draw();self.refresh()
        except Exception as exc:self.preview_path=None;self.preview_command=None;self.note(str(exc));self.refresh()

    def preview_point(self):
        try:self.set_preview('SET_TARGET',{'target':[float(self.fields[x].get()) for x in 'XYZ'],'speed':float(self.fields['速度 mm/s'].get()),'vertical_speed':float(self.vspeed.get())})
        except ValueError as exc:self.note(str(exc))

    def preview_shape(self):
        try:self.set_preview('RUN_TRAJECTORY',{'kind':self.kind.get(),'parameters':json.loads(self.parameters.get('1.0','end')),'speed':float(self.fields['速度 mm/s'].get()),'z':float(self.z.get()),'repeat':int(self.repeat.get()),'clockwise':self.clockwise.get()})
        except ValueError as exc:self.note(str(exc))

    def send_preview(self):
        if self.preview_path and self.preview_command:
            self.action(*self.preview_command,path=self.preview_path)

    def vertical(self,direction):
        try:self.action('RUN_VERTICAL',{'z':self.model.position[2]+direction*float(self.step.get()) if direction else 0,'speed':float(self.vspeed.get())})
        except ValueError as exc:self.note(str(exc))

    def stop(self):
        # STOP bypasses the worker queue and invalidates its generation token.
        self.model.dispatch(self.packet('STOP'));self.note('SAFE_DISABLED · 队列取消 · 需要重新应用中心并确认');self.refresh()

    def demo(self):
        if not self.model.confirmed:self.note('请先应用中心陷阱并确认');return
        self.set_preview('RUN_DEMO',{'program':demo_commands()})
        if self.preview_path:self.action('RUN_DEMO',{'program':demo_commands()},path=self.preview_path,callback=self.completed_callback)

    def demo_next(self):
        if not self.demo_queue:
            if self.completed_callback:self.completed_callback()
            return
        command,payload=self.demo_queue.pop(0)
        self.set_preview(command,payload)
        self.action(command,payload,path=self.preview_path,callback=self.demo_next)

    def draw(self):
        c=self.canvas;c.delete('all');w=c.winfo_width();h=c.winfo_height();scale=min((w-90)/32,(h-65)/26);cx=w/2;cy=h/2
        def pt(x,y):return cx+x*scale,cy-y*scale
        for n in range(-15,16,5):
            c.create_line(*pt(n,-12),*pt(n,12),fill='#edf1f6');c.create_text(*pt(n,-12),text=str(n),fill='#8595aa',anchor='n')
        for n in range(-10,11,5):c.create_line(*pt(-15,n),*pt(15,n),fill='#edf1f6')
        c.create_rectangle(*pt(-10,10),*pt(10,-10),outline='#b0bccc',dash=(5,4),width=2)
        c.create_line(*pt(-14,0),*pt(14,0),fill='#8090a5',arrow='last');c.create_line(*pt(0,-11),*pt(0,11),fill='#8090a5',arrow='last')
        c.create_text(*pt(14,0),text='+X 右',anchor='s');c.create_text(*pt(0,11),text='+Y 平面上方',anchor='s')
        c.create_text(*pt(0,0),text='(0,0)',anchor='nw',fill='#687a91')
        c.create_text(15,15,text='XY 俯视图 / mm     +Z 指向上阵列',anchor='nw',fill='#37465a')
        if self.preview_path:
            points=[pt(r['x_mm'],r['y_mm']) for r in self.preview_path]
            if len(points)>1:c.create_line(*[x for p in points for x in p],fill='#198c86',width=2)
            for p,color,label in ((points[0],'#d89b23','起点'),(points[-1],'#1b65d8','终点')):
                x,y=p;c.create_oval(x-5,y-5,x+5,y+5,fill=color,outline='white');c.create_text(x+8,y-9,text=label,anchor='w',fill=color)

    def refresh(self):
        s=self.model.status();self.state.set(f"{s['state']}   |   {'已连接仿真' if s['connected'] else '未连接'}   |   f_work {s['f_work'] or '—'} Hz   |   实际位置：未测量   |   {'RTL 执行中…' if self.worker and self.worker.is_alive() else '就绪'}")
        self.position.set('X %+.2f   Y %+.2f   Z %+.2f mm'%tuple(s['commanded_trap_position_mm']))
        self.confirm.configure(state='normal' if s['state']=='WAIT_OPERATOR' else 'disabled')
        self.send.configure(state='normal' if self.model.confirmed and self.preview_path and not self.model.busy else 'disabled')

    def record_execution(self,command,execution,executed_path):
        if not execution or command in ('CONNECT','LOAD_CALIBRATION','GET_STATUS','BALL_AT_CENTER_CONFIRMED'):
            return
        if executed_path is not None and digest(executed_path)!=execution['trajectory_sha256']:
            raise RuntimeError('EXECUTED_TRAJECTORY_HASH_MISMATCH')
        index=len(self.results);self.results.append({'command':command,**execution})
        if executed_path is not None:
            (self.output/f'trajectory_{index:02d}.json').write_text(json.dumps(executed_path,separators=(',',':')))
        # Preserve actual per-command RTL ACKs before the next execution replaces them.
        import shutil
        for name in ('motion_ack.txt','run.log','xsim.log'):
            src=self.output/'rtl'/name
            if src.exists():shutil.copy2(src,self.output/f'{index:02d}_{name}')

    def poll(self):
        try:
            while True:
                kind,value=self.events.get_nowait()
                if kind=='error':
                    self.error=value;self.note('REJECTED: '+value)
                    if self.automated:
                        (self.output/'gui_failure.json').write_text(json.dumps({'error':value}));self.root.after(500,self.close)
                else:
                    command,result,callback,execution,executed_path=value;self.note(command+' PASS');self.refresh()
                    self.record_execution(command,execution,executed_path)
                    if callback:self.root.after(50,callback)
        except queue.Empty:pass
        self.refresh();self.root.after(150,self.poll)

    def close(self):
        self.model.stop();self.root.destroy()

    def capture(self):
        from PIL import ImageGrab
        import ctypes
        import sys
        import time
        self.root.attributes('-topmost',True);self.root.lift();self.root.update();time.sleep(.25)
        x=self.root.winfo_rootx();y=self.root.winfo_rooty();w=self.root.winfo_width();h=self.root.winfo_height()
        bbox=(x,y,x+w,y+h)
        if sys.platform=='win32':
            # Tk can report virtualized 96-DPI coordinates while ImageGrab returns
            # physical pixels. DWM bounds use physical pixels at any desktop scale.
            from ctypes import wintypes
            hwnd=ctypes.windll.user32.GetAncestor(self.root.winfo_id(),2)
            rect=wintypes.RECT()
            result=ctypes.windll.dwmapi.DwmGetWindowAttribute(hwnd,9,ctypes.byref(rect),ctypes.sizeof(rect))
            if result!=0:raise RuntimeError('Cannot obtain physical window bounds')
            bbox=(rect.left,rect.top,rect.right,rect.bottom)
        ImageGrab.grab(bbox=bbox).save(self.output/'gui_simulation.png')
        self.root.attributes('-topmost',False)

    def automate(self):
        # Explicit CLI automation is simulation-only; this is not a claim of operator observation.
        def finish():
            self.kind.set('CIRCLE');self.preset();self.preview_shape();self.capture()
            (self.output/'gui_result.json').write_text(json.dumps({'status':'PASS','mode':'SIMULATION',
                'confirmation':'SIMULATION_AUTOMATION_ONLY','results':self.results,'final_status':self.model.status()},indent=2))
            self.root.after(300,self.close)
        self.completed_callback=finish
        def confirm():self.action('BALL_AT_CENTER_CONFIRMED',{'source':'SIMULATION_AUTOMATION_ONLY'},callback=self.demo)
        def center():self.action('APPLY_CENTER',callback=confirm)
        def calibration():
            record=json.loads(DEFAULT_CALIBRATION.read_text());key=digest(record);self.model.calibration_records[key]=record
            self.action('LOAD_CALIBRATION',{'calibration_id':key},callback=center)
        self.action('CONNECT',callback=calibration)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',default=str(ROOT/'build/motion_gui'))
    parser.add_argument('--simulator',choices=['icarus','xsim'],default='icarus');parser.add_argument('--automated-demo',action='store_true')
    args=parser.parse_args();root=tk.Tk();app=App(root,args.output,args.simulator,args.automated_demo)
    if args.automated_demo:root.after(500,app.automate)
    root.mainloop()
    if args.automated_demo and (app.error or not (Path(args.output)/'gui_result.json').exists()):raise SystemExit(1)


if __name__=='__main__':main()
