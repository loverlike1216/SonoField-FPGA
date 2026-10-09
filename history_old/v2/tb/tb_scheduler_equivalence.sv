`timescale 1ns/1ps
module tb_scheduler_equivalence;
 reg clk=0;always #5 clk=~clk;
 reg rst_n=0,start=0,abort=0,ack=0,adc_ready=1,adc_idle=1,adc_error=0,frame_valid=0;
 reg[127:0]frame=0;reg[63:0]frame_timestamp=0,time_now=0;
 reg[31:0]sample_period=165,pre_samples=2,main_samples=3,tail_samples=2,settle_cycles=13,guard_cycles=17;
 reg[6:0]first_tx=63;reg[7:0]scan_count=3;reg burst_active=0,burst_done=0;
 reg[11:0]read_address=0;
 wire[31:0]rd1,rd2;wire sr1,sr2,bs1,bs2,cr1,cr2,d1,d2,e1,e2;
 wire[6:0]tx1,tx2;wire[7:0]sq1,sq2;wire[10:0]fc1,fc2;
 wire[63:0]ft1,ft2,bt1,bt2;wire[1:0]rb1,rb2;wire ac1,ac2;wire[3:0]st1,st2;
 calibration_scheduler dut(clk,rst_n,start,abort,ack,adc_ready,adc_idle,adc_error,frame_valid,
  frame,frame_timestamp,time_now,sample_period,pre_samples,main_samples,tail_samples,settle_cycles,guard_cycles,
  first_tx,scan_count,burst_active,burst_done,read_address,rd1,sr1,bs1,cr1,d1,e1,tx1,sq1,fc1,ft1,bt1,rb1,ac1,st1);
 calibration_scheduler_golden ref_dut(clk,rst_n,start,abort,ack,adc_ready,adc_idle,adc_error,frame_valid,
  frame,frame_timestamp,time_now,sample_period,pre_samples,main_samples,tail_samples,settle_cycles,guard_cycles,
  first_tx,scan_count,burst_active,burst_done,read_address,rd2,sr2,bs2,cr2,d2,e2,tx2,sq2,fc2,ft2,bt2,rb2,ac2,st2);
 wire[197:0]a={rd1,sr1,bs1,cr1,d1,e1,tx1,sq1,fc1,ft1,bt1,rb1,ac1,st1};
 wire[197:0]b={rd2,sr2,bs2,cr2,d2,e2,tx2,sq2,fc2,ft2,bt2,rb2,ac2,st2};
 integer cycles=0,samples=0,bursts=0,good=0,bad=0,delay_count=0,trial,j;
 always @(posedge clk)begin
  #1;cycles=cycles+1;
  if(a!==b)$fatal(1,"SCHED_EQ cycle%0d trial%0d actual=%h golden=%h",cycles,trial,a,b);
  if(sr1)samples=samples+1;if(bs1)bursts=bursts+1;
 end
 always @(negedge clk)begin
  time_now=time_now+1;frame_valid=0;ack=cr1;burst_active=bs1;burst_done=0;
  if(!rst_n)delay_count=0;
  else begin
   if(delay_count>0)begin delay_count=delay_count-1;
    if(delay_count==0)begin frame_valid=1;frame=frame+1;frame_timestamp=time_now-7;end
   end
   if(sr1)delay_count=7;
  end
  read_address=(read_address+1)%28;
 end
 initial begin
  for(trial=0;trial<16;trial=trial+1)begin
   @(negedge clk);#1;rst_n=0;start=0;abort=0;adc_error=0;
   pre_samples=2;main_samples=3;tail_samples=2;sample_period=165;scan_count=3;adc_ready=1;
   repeat(3)@(negedge clk);#1;rst_n=1;
   case(trial)
    2:pre_samples=0;3:main_samples=0;4:scan_count=0;5:sample_period=164;
    6:main_samples=2000;7:adc_ready=0;8:scan_count=129;
    9:begin pre_samples=32'hffffffff;main_samples=3;tail_samples=7;end
   endcase
   @(negedge clk);#1;start=1;@(negedge clk);#1;start=0;
   for(j=0;j<4000;j=j+1)begin
    @(negedge clk);#1;
    if(trial==10&&j==30)abort=1;if(trial==10&&j==32)abort=0;
    if(trial==11&&j==30)adc_error=1;
    if(trial==12&&j==1300)guard_cycles=19;
   end
   if(d1)good=good+1;if(e1)bad=bad+1;
  end
  if(samples<50||bursts<8||good<3||bad<6)$fatal(1,"Insufficient scheduler coverage");
  $display("PASS SCHEDULER_EQ cycles=%0d samples=%0d bursts=%0d completed=%0d rejected=%0d",cycles,samples,bursts,good,bad);$finish;
 end
endmodule
