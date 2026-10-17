`timescale 1ns/1ps
module tb_final_tx;
 parameter integer FREQ=40000;
 reg clk=0,tx_clk=0,rst_n=0,run=1;always #3.90625 clk=~clk;always #1.953125 tx_clk=~tx_clk;
 reg start=0;reg[127:0]waveform=0;
 wire[31:0]serial_data;wire shift_clock,latch_clock,busy,frame_done,overrun;
 tx_pipeline44 dut(.*);
 wire drive_enable;wire disabled=~drive_enable;
 safety_controller safety(.clk(clk),.rst_n(rst_n),.hardware_enable(1'b1),.software_enable(1'b1),.fault(overrun),.frame_valid(frame_done),.drive_enable(drive_enable));
 reg[127:0]expected[0:5000];reg[127:0]received=0;integer requests=0,latches=0,l,clocks=0;
 reg[31:0]acc=0;reg[7:0]phase=0;integer ch;
 always@(negedge clk)begin
  start=0;
  if(rst_n&&run&&requests<4096)begin
   if(acc+FREQ*256>=128000000)begin
    acc=acc+FREQ*256-128000000;phase=phase+1;start=1;
    for(ch=0;ch<128;ch=ch+1)waveform[ch]=((phase-ch)&255)<128;
   end else acc=acc+FREQ*256;
  end
 end
 always@(posedge clk)if(rst_n&&start)begin expected[requests]=waveform;requests=requests+1;end
 always@(posedge shift_clock)begin
  for(l=0;l<32;l=l+1)received[l*4+:4]={received[l*4+:3],serial_data[l]};clocks=clocks+1;
 end
 always@(posedge latch_clock)begin
  if(clocks!=(latches+1)*4)$fatal(1,"not four shifts per completed frame");
  if(latches>=requests||received!==expected[latches])$fatal(1,"128TX snapshot/bit order mismatch frame%0d got%h expected%h",latches,received,expected[latches]);
  latches=latches+1;
 end
 initial begin
  repeat(8)@(negedge clk);rst_n=1;
  wait(latches==4096);run=0;repeat(12)@(negedge clk);
  if(overrun||disabled)$fatal(1,"continuous256phase stream overran or disabled");
  repeat(70)@(negedge clk);if(!disabled)$fatal(1,"missingframe safety did not close");
  $display("PASS4096frames128TX256phase128/256MHz carrier%0dHz",FREQ); $finish;
 end
 initial begin #1000000;$fatal(1,"timeout");end
endmodule
