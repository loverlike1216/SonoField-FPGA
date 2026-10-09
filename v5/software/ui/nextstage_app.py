"""Same runtime trajectory editor, with explicit transport qualification display."""
import argparse,json,tkinter as tk,sys
from pathlib import Path
from tkinter import ttk
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from software.ui.prepcb_app import Editor
from software.prepcb.protocol import discover_ports

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path('build/nextstage_gui'));p.add_argument('--mode',choices=['SIMULATION','HOST_FIXTURE','REAL_BOARD'],default='SIMULATION');a=p.parse_args()
 if a.mode=='REAL_BOARD':raise SystemExit('REAL_BOARD_LOCKED: matched platform, image ownership, isolated outputs and explicit volatile-write approval missing')
 root=tk.Tk();app=Editor(root,a.output)
 app.status.set(a.mode+' · AD7606C-16 approved; physical transport NOT_RUN; editor is an open-loop intent/model controller')
 # Discovery returns descriptions/VID/PID only and never opens a port.
 app.diagnostics.set(json.dumps(dict(mode=a.mode,ports=discover_ports(),adc='AD7606C-16BSTZ-RL',real_board='LOCKED_A2',raw_bytes=16384,uart_ideal_seconds=16384/11520,humidity_applied=False),ensure_ascii=False,indent=2))
 root.mainloop()
if __name__=='__main__':main()
