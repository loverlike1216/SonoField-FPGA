`timescale 1ns/1ps
// D/E candidate: same32data/2clock ports. phase_clk is same frequency and
// common-MMCM phase27deg (~0.568ns at132MHz). It is NOT an async free-running clock.
// No claim that the sub-cycle raw->ODDR path has closed STA.
module btx_phase_adapter(input wire phase_clk,rst_n,
 input wire shift_in,latch_in,input wire[31:0]data_in,
 output wire shift_out,latch_out,output wire[31:0]data_out);
 assign data_out=data_in;
`ifdef SIMULATION
 reg s=0,l=0;
 always@(posedge phase_clk or negedge rst_n)
  if(!rst_n)begin s<=0;l<=0;end else begin s<=shift_in;l<=latch_in;end
 assign shift_out=s;assign latch_out=l;
`else
 ODDR #(.DDR_CLK_EDGE("SAME_EDGE"),.INIT(1'b0),.SRTYPE("ASYNC"))
  sr(.Q(shift_out),.C(phase_clk),.CE(1'b1),.D1(shift_in),.D2(shift_in),.R(!rst_n),.S(1'b0));
 ODDR #(.DDR_CLK_EDGE("SAME_EDGE"),.INIT(1'b0),.SRTYPE("ASYNC"))
  rl(.Q(latch_out),.C(phase_clk),.CE(1'b1),.D1(latch_in),.D2(latch_in),.R(!rst_n),.S(1'b0));
`endif
endmodule
