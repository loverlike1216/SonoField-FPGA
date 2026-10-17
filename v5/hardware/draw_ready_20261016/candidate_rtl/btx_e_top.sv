`timescale 1ns/1ps
// E correctedD: add one common core-cycle latency on DATA; stage SRCLK/RCLK
// on falling core edge before the phase-clock ODDR. This removes the0.568ns
// same-edge launch->ODDR requirement while retaining the relative+0.568ns shift.
module btx_e_top(input wire core_clk,phase_clk,rst_n,start,
 input wire[127:0]waveform,output wire[31:0]serial_data,
 output wire shift_clock,latch_clock,busy,output reg frame_done,output wire overrun);
 wire[31:0]raw_data;wire raw_s,raw_l,raw_done;
 serializer source(core_clk,rst_n,start,waveform,raw_data,raw_s,raw_l,busy,raw_done,overrun);
 (* IOB="TRUE" *)reg[31:0]data_q;
 reg s_neg,l_neg;
 always@(posedge core_clk or negedge rst_n)
  if(!rst_n)begin data_q<=0;frame_done<=0;end
  else begin data_q<=raw_data;frame_done<=raw_done;end
 always@(negedge core_clk or negedge rst_n)
  if(!rst_n)begin s_neg<=0;l_neg<=0;end
  else begin s_neg<=raw_s;l_neg<=raw_l;end
 btx_phase_adapter io(phase_clk,rst_n,s_neg,l_neg,data_q,shift_clock,latch_clock,serial_data);
endmodule
