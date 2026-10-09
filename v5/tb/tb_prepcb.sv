`timescale 1ns/1ps
module tb_prepcb;
 reg clk=0;always #5 clk=~clk;
 reg rst_n=0,estop_loop_ok=1,pgood_up=1,pgood_dn=1,thermal_ok=1,link_ok=1,watchdog_ok=1;
 reg ps_arm=0,pl_cal=0,clear_fault=0,cal_complete=0,cal_quality=1,trap_request=0,motion_request=0,motion_done=0,stop=0;
 wire[3:0]state;wire emit_permit,efuse_up,efuse_dn,output_disable,heartbeat;
 prepcb_supervisor #(.MS_CYCLES(4),.LONG_PRESS_MS(3),.DEBOUNCE_MS(2),.TIMEOUT_MS(200)) dut(.*);
 task ms(input integer n);begin repeat(n*4)@(negedge clk);end endtask
 task boot;begin rst_n=0;ms(2);rst_n=1;ps_arm=0;pl_cal=0;clear_fault=0;cal_complete=0;trap_request=0;motion_request=0;stop=0;ms(5);end endtask
 task armed;begin ps_arm=1;ms(10);ps_arm=0;ms(4);if(state!=3||emit_permit)$fatal(1,"ARM gate");end endtask
 task emitting;begin armed();pl_cal=1;ms(10);pl_cal=0;ms(4);if(state!=4||!emit_permit)$fatal(1,"CAL gate");end endtask
 task offcheck;begin #1;if(emit_permit||efuse_up||efuse_dn||!output_disable)$fatal(1,"not both OFF");end endtask
 reg publish=0;wire bram_clk,bram_rst;wire[3:0]bram_we;wire bram_en;wire[31:0]bram_addr,bram_wrdata;
 reg[31:0]bram_rddata=0;wire frame_valid;wire[2175:0]frame_data;wire[31:0]frame_sequence;wire frame_last;
 reg frame_ready=0;wire busy,invalid;reg[31:0]memory[0:129];integer i;
 prepcb_frame_mailbox mailbox(.*);
 always @(posedge clk)if(bram_en)bram_rddata<=memory[bram_addr/4];
 initial begin
  for(i=0;i<128;i=i+1)memory[i]=32'h10000+i;memory[128]=1;memory[129]=1;
  boot();ms(3);if(state!=2)$fatal(1,"not BOARD_CHECK");offcheck();
  // Held at power-on cannot authorize emission.
  rst_n=0;ps_arm=1;ms(2);rst_n=1;ms(20);if(state!=2)$fatal(1,"held ARM accepted");offcheck();
  boot();emitting();
  // Sub-clock pulse latches; restoring a source never resumes automatically.
  #1 pgood_up=0;offcheck();#1 pgood_up=1;ms(4);offcheck();
  clear_fault=1;ms(5);clear_fault=0;ms(5);if(state!=2)$fatal(1,"clear did not require new ARM");offcheck();
  boot();emitting();pgood_dn=0;offcheck();ms(2);pgood_dn=1;ms(3);offcheck();
  boot();emitting();thermal_ok=0;offcheck();ms(2);thermal_ok=1;ms(3);offcheck();
  boot();emitting();link_ok=0;offcheck();ms(2);link_ok=1;ms(3);offcheck();
  boot();emitting();watchdog_ok=0;offcheck();ms(2);watchdog_ok=1;ms(3);offcheck();
  boot();emitting();estop_loop_ok=0;offcheck();if(state!=10)$fatal(1,"ESTOP code");ms(2);estop_loop_ok=1;ms(3);offcheck();
  boot();emitting();cal_complete=1;ms(2);cal_complete=0;ms(2);if(state!=6)$fatal(1,"quality gate");offcheck();
  trap_request=1;ms(2);trap_request=0;if(state!=7||!emit_permit)$fatal(1,"trap gate");
  motion_request=1;ms(2);motion_request=0;if(state!=8)$fatal(1,"motion gate");motion_done=1;ms(2);motion_done=0;if(state!=7)$fatal(1,"done");
  stop=1;ms(2);stop=0;offcheck();
  boot();ps_arm=1;ms(1);ps_arm=0;ms(10);if(state!=2)$fatal(1,"short press");
  ms(210);if(state!=9)$fatal(1,"timeout");offcheck();
  boot();publish=1;wait(frame_valid);#1;
  if(frame_sequence!=1||!frame_last||frame_data[16:0]!=17'h10000||frame_data[127*17+:17]!=17'h1007f)$fatal(1,"mailbox frame");
  ms(3);if(!frame_valid)$fatal(1,"mailbox dropped pending frame");frame_ready=1;ms(1);frame_ready=0;
  memory[0]=32'h80000000;publish=0;wait(invalid);ms(3);if(frame_valid)$fatal(1,"invalid mailbox published");
  $display("PASS PREPCB supervisor startup/debounce/longpress/subclock/6faults/clear/quality/trap/motion/timeout/mailbox atomic+invalid");$finish;
 end
 initial begin #200000;$fatal(1,"TB timeout");end
endmodule
