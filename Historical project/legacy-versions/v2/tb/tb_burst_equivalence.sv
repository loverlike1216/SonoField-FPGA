`timescale 1ns/1ps
module tb_burst_equivalence;
 reg clk=0;always #3.787878788 clk=~clk;
 reg rst_n=0,start=0,abort=0;reg[31:0] frequency=40000,cycles=1;reg[7:0] start_phase=0;
 wire active,done,wave,old_active,old_done,old_wave;
 burst_generator dut(clk,rst_n,start,abort,frequency,cycles,start_phase,active,done,wave);
 burst_generator_golden reference(clk,rst_n,start,abort,frequency,cycles,start_phase,old_active,old_done,old_wave);
 integer checks=0,p,f;
 always @(posedge clk)begin #0.1;
  if({active,done,wave}!=={old_active,old_done,old_wave})$fatal(1,"burst equivalence check %0d phase=%0d f=%0d",checks,start_phase,frequency);
  checks=checks+1;
 end
 initial begin
  repeat(5)@(negedge clk);rst_n=1;
  for(f=0;f<3;f=f+1)for(p=0;p<256;p=p+1)begin
   @(negedge clk);frequency=(f==0)?38500:(f==1)?40000:41500;start_phase=p;cycles=1+p%3;start=1;
   @(negedge clk);start=0;
   wait(done);@(negedge clk);
  end
  start=1;cycles=9;@(negedge clk);start=0;repeat(777)@(negedge clk);abort=1;@(negedge clk);abort=0;
  repeat(3)@(negedge clk);rst_n=0;repeat(3)@(negedge clk);rst_n=1;repeat(10)@(negedge clk);
  $display("PASS BURST_EQUIVALENCE checked=%0d all_256_offsets min_nominal_max_frequency latency_change=0",checks);$finish;
 end
endmodule
