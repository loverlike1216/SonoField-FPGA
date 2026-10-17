module btx_d_top(input wire core_clk,phase_clk,rst_n,start,
 input wire[127:0]waveform,output wire[31:0]serial_data,
 output wire shift_clock,latch_clock,busy,frame_done,overrun);
 wire raw_s,raw_l;wire[31:0]raw_data;
 serializer source(core_clk,rst_n,start,waveform,raw_data,raw_s,raw_l,busy,frame_done,overrun);
 btx_phase_adapter candidate(phase_clk,rst_n,raw_s,raw_l,raw_data,shift_clock,latch_clock,serial_data);
endmodule
