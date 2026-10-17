`timescale 1ns/1ps
//AX7020V3 documented50MHzU18. MMCM1:800MHzVCO/12.5=64MHz.
//MMCM2:1024MHzVCO/8=128MHz,/4=256MHz. SharedsecondMMCMtimebase.
module draw_ready_clocks(
 (* X_INTERFACE_INFO="xilinx.com:signal:clock:1.0 ref_clk50 CLK", X_INTERFACE_PARAMETER="FREQ_HZ 50000000" *)input wire ref_clk50,
 (* X_INTERFACE_INFO="xilinx.com:signal:clock:1.0 core_clk CLK", X_INTERFACE_PARAMETER="FREQ_HZ 128000000" *)output wire core_clk,
 (* X_INTERFACE_INFO="xilinx.com:signal:clock:1.0 tx_clk CLK", X_INTERFACE_PARAMETER="FREQ_HZ 256000000" *)output wire tx_clk,
 output wire locked);
 wire ic,fb1,fb1b,c64u,c64,l1,fb2,fb2b,c128,c256,l2;
 IBUF input_clock(.I(ref_clk50),.O(ic));BUFG feedback1(.I(fb1),.O(fb1b));BUFG midbuf(.I(c64u),.O(c64));
 MMCME2_BASE #(.CLKIN1_PERIOD(20.0),.DIVCLK_DIVIDE(1),.CLKFBOUT_MULT_F(16.0),.CLKOUT0_DIVIDE_F(12.5)) mmcm1
 (.CLKIN1(ic),.CLKFBIN(fb1b),.CLKFBOUT(fb1),.CLKOUT0(c64u),.RST(1'b0),.PWRDWN(1'b0),.LOCKED(l1));
 BUFG feedback2(.I(fb2),.O(fb2b));BUFG corebuf(.I(c128),.O(core_clk));BUFG txbuf(.I(c256),.O(tx_clk));
 MMCME2_BASE #(.CLKIN1_PERIOD(15.625),.DIVCLK_DIVIDE(1),.CLKFBOUT_MULT_F(16.0),.CLKOUT0_DIVIDE_F(8.0),.CLKOUT1_DIVIDE(4)) mmcm2
 (.CLKIN1(c64),.CLKFBIN(fb2b),.CLKFBOUT(fb2),.CLKOUT0(c128),.CLKOUT1(c256),.RST(!l1),.PWRDWN(1'b0),.LOCKED(l2));
 assign locked=l1&l2;
endmodule
