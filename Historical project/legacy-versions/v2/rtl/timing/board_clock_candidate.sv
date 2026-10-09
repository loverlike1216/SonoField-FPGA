`timescale 1ns/1ps
// User-approved 33.333MHz document fallback, not a measured oscillator.
// Nominal design reference132MHz; resulting arithmetic clock131.998680MHz.
// Pin/voltage/PS clock-domain integration must be qualified before deployment.
module board_clock_candidate(input wire clk_in,rst_n,output wire core_clk,locked);
 wire feedback,feedback_buf,clock_unbuffered;
 BUFG feedback_clock(.I(feedback),.O(feedback_buf));
 BUFG core_clock(.I(clock_unbuffered),.O(core_clk));
 MMCME2_BASE #(.CLKIN1_PERIOD(30.000300003),.DIVCLK_DIVIDE(2),
  .CLKFBOUT_MULT_F(49.5),.CLKOUT0_DIVIDE_F(6.25)) mmcm(
  .CLKIN1(clk_in),.RST(!rst_n),.PWRDWN(1'b0),.CLKFBIN(feedback_buf),
  .CLKFBOUT(feedback),.CLKOUT0(clock_unbuffered),.LOCKED(locked));
endmodule
