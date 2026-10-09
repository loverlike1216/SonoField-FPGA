`timescale 1ns/1ps
// CANDIDATE_ANALYSIS_ONLY. No board package pin or IO voltage is assigned.
// 33 MHz -> 792 MHz VCO (M=24,D=1) -> 132 MHz (/6), 66 MHz (/12).
module clock_candidate(input wire clk33,input wire reset,
 output wire clk132,clk66,locked,output wire reset132_n,reset66_n);
 wire feedback,feedback_buf,raw132,raw66;
 MMCME2_BASE #(.BANDWIDTH("OPTIMIZED"),.CLKIN1_PERIOD(30.303030),
 .CLKFBOUT_MULT_F(24.0),.DIVCLK_DIVIDE(1),.CLKOUT0_DIVIDE_F(6.0),.CLKOUT1_DIVIDE(12),
 .STARTUP_WAIT("FALSE"),.REF_JITTER1(0.010)) mmcm(
 .CLKIN1(clk33),.CLKFBIN(feedback_buf),.CLKFBOUT(feedback),.CLKOUT0(raw132),.CLKOUT1(raw66),
 .LOCKED(locked),.RST(reset),.PWRDWN(1'b0));
 BUFG fb(.I(feedback),.O(feedback_buf));
 BUFG core(.I(raw132),.O(clk132));BUFG half(.I(raw66),.O(clk66));
 (* ASYNC_REG="TRUE" *)reg[2:0]sync132=0,sync66=0;
 wire async_reset=reset||!locked;
 always @(posedge clk132 or posedge async_reset)if(async_reset)sync132<=0;else sync132<={sync132[1:0],1'b1};
 always @(posedge clk66 or posedge async_reset)if(async_reset)sync66<=0;else sync66<={sync66[1:0],1'b1};
 assign reset132_n=sync132[2];assign reset66_n=sync66[2];
endmodule
