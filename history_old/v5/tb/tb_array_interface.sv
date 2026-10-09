`timescale 1ns/1ps
module tb_array_interface;
 reg clk=0;always #5 clk=~clk;
 reg rst_n=0,global_disable=1,upper_permit=0,lower_permit=0;
 reg[1:0]array_fault=0,rx_blank=2'b01;reg[31:0]serial_data=32'hA55AC33C;
 reg shift_clock=0,latch_clock=0;
 wire[15:0]upper_data,lower_data;
 wire upper_shift_clock,lower_shift_clock,upper_latch_clock,lower_latch_clock;
 wire upper_oe_n,lower_oe_n,upper_board_enable,lower_board_enable,upper_rx_blank,lower_rx_blank;
 sono_array_interface dut(.*);
 task frame;begin @(negedge clk);latch_clock=1;@(negedge clk);latch_clock=0;@(negedge clk);end endtask
 initial begin
  #1;if(!upper_oe_n||!lower_oe_n)$fatal(1,"reset unsafe");
  repeat(3)@(negedge clk);rst_n=1;global_disable=0;upper_permit=1;
  repeat(4)@(negedge clk);if(!upper_oe_n)$fatal(1,"enable without fresh frame");
  frame;if(upper_oe_n||!lower_oe_n)$fatal(1,"upper-only enable failed");
  lower_permit=1;repeat(4)@(negedge clk);if(!lower_oe_n)$fatal(1,"lower enabled prematurely");
  frame;if(upper_oe_n||lower_oe_n)$fatal(1,"both enabled failed");
  #1;upper_permit=0;#1;if(!upper_oe_n||lower_oe_n)$fatal(1,"independent asynchronous disable failed");
  upper_permit=1;repeat(4)@(negedge clk);if(!upper_oe_n)$fatal(1,"stale upper reenable");
  frame;
  #1;global_disable=1;#1;if(!upper_oe_n||!lower_oe_n)$fatal(1,"global kill failed");
  global_disable=0;repeat(4)@(negedge clk);if(!upper_oe_n||!lower_oe_n)$fatal(1,"stale global reenable");
  frame;
  #1;array_fault=2'b10;#1;if(upper_oe_n||!lower_oe_n)$fatal(1,"independent fault kill failed");
  array_fault=0;repeat(4)@(negedge clk);if(!lower_oe_n)$fatal(1,"fault released without frame");
  frame;
  shift_clock=1;#1;
  if(upper_data!==16'hC33C||lower_data!==16'hA55A||!upper_shift_clock||!lower_shift_clock||
     upper_rx_blank!==1'b1||lower_rx_blank!==1'b0)$fatal(1,"mapping/common clock failed");
  $display("PASS ARRAY_INTERFACE mapping common clocks independent kill fresh-frame restart");$finish;
 end
endmodule
