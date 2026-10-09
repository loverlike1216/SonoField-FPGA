"""Generate additive C-16 top/bench/platform from preserved reference contracts.

Does not edit the reference bench, goldens or original platform Tcl.
"""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
def main():
 source=(ROOT/'rtl/board/prepcb_pl.v').read_text(encoding='utf-8')
 header=source[:source.index(' wire emit_permit')].replace('module prepcb_pl #(parameter integer ADC_C16=0)','module nextstage_pl')
 # Parse ANSI comma-separated declarations, not a greedy identifier list:
 # continuation declarations (bram_addr,bram_wrdata) are legal Verilog2001.
 port_text=re.sub(r'//[^\n]*|\(\*.*?\*\)','',header,flags=re.S)
 port_text=port_text[port_text.index('(input')+1:port_text.rindex(');')]
 ports=[re.search(r'(\w+)\s*$',part).group(1) for part in port_text.split(',')]
 assert len(ports)==len(set(ports)) and not set(ports)&{'input','output','wire'}
 connections=','.join('.'+name+'('+name+')' for name in ports)
 (ROOT/'rtl/board/nextstage_pl.v').write_text(header+' prepcb_pl #(.ADC_C16(1)) implementation('+connections+');\nendmodule\n',encoding='utf-8',newline='\n')
 tb=(ROOT/'tb/tb_prepcb_system.sv').read_text(encoding='utf-8').replace('module tb_prepcb_system','module tb_nextstage_system').replace('prepcb_pl dut','nextstage_pl dut').replace('dut.','dut.implementation.').replace('ad7606b_model adc','ad7606c16_model adc').replace('.hold_busy(1\'b0),','.hold_busy(1\'b0),.inject(3\'b0),')
 (ROOT/'tb/tb_nextstage_system.sv').write_text('// Generated additive bench from tb_prepcb_system; original assertions unchanged.\n'+tb,encoding='utf-8',newline='\n')
 tcl=(ROOT/'scripts/build_prepcb_platform.tcl').read_text(encoding='utf-8').replace('evidence pre_pcb_20261009','evidence next_stage 20261010').replace('config ooc_source_list.txt','config nextstage_source_list.txt')
 # Source list already includes supervisor/mailbox and both module-reference tops.
 tcl=tcl.replace('read_verilog -sv [file join $root rtl control prepcb_supervisor.sv]\n','').replace('read_verilog -sv [file join $root rtl motion prepcb_frame_mailbox.sv]\n','').replace('read_verilog [file join $root rtl board prepcb_pl.v]\n','')
 tcl=tcl.replace('-reference prepcb_pl','-reference nextstage_pl').replace('-top prepcb_pl','-top nextstage_pl').replace('prepcb_pl_routed.dcp','nextstage_pl_routed.dcp')
 tcl=tcl.replace('foreach rel [split [string trim [read $f]] \\n] {read_verilog -sv [file join $root [string trim $rel]]}', 'foreach rel [split [string trim [read $f]] \\n] {set src [file join $root [string trim $rel]]; if {[file extension $src] eq ".v"} {read_verilog $src} else {read_verilog -sv $src}}')
 tcl+='\nreport_drc -ruledecks {default} -file [file join $out pl_drc_full.rpt]\nset f [open [file join $out drc_all_objects.txt] w]\nforeach v [get_drc_violations] {puts $f [report_property -return_string $v]}\nclose $f\n'
 (ROOT/'scripts/build_nextstage_platform.tcl').write_text(tcl,encoding='utf-8',newline='\n')
 files=(ROOT/'config/ooc_source_list.txt').read_text(encoding='utf-8').strip().splitlines()+['rtl/acquisition/ad7606c16_if.sv','rtl/control/prepcb_supervisor.sv','rtl/motion/prepcb_frame_mailbox.sv','rtl/board/prepcb_pl.v','rtl/board/nextstage_pl.v']
 (ROOT/'config/nextstage_source_list.txt').write_text('\n'.join(files)+'\n',encoding='utf-8')
 print('Generated current C16 top, additive bench, explicit list and offline platform')
if __name__=='__main__':main()
