`timescale 1ns/1ps
// F common-clock snapshot stage.264MHz must be generated from the same132MHz
// source; this is not an asynchronous CDC synchronizer for a128-bit bus.
module btx_f_top(input wire core_clk,tx_clk,rst_n,start,
 input wire[127:0]waveform,output wire[31:0]serial_data,
 output wire shift_clock,latch_clock,busy,frame_done,overrun);
 reg start_q;reg[127:0]snapshot;
 always@(posedge core_clk or negedge rst_n)
  if(!rst_n)begin start_q<=0;snapshot<=0;end
  else begin start_q<=start;snapshot<=waveform;end
 serializer_pipeline_44 candidate(tx_clk,rst_n,start_q,snapshot,serial_data,shift_clock,latch_clock,busy,frame_done,overrun);
endmodule
