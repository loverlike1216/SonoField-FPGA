`timescale 1ns/1ps
//Theoretical physical profile:128/256MHz,8DOUT8MHz,TX42.666667MHz. GPIO upper
//bits are explicit PS qualification flags, default0 until real initialization.
module draw_ready_pl(input wire clk,tx_clk,rst_n,
 input wire[31:0]S_AXI_awaddr,input wire S_AXI_awvalid,output wire S_AXI_awready,
 input wire[31:0]S_AXI_wdata,input wire[3:0]S_AXI_wstrb,input wire S_AXI_wvalid,output wire S_AXI_wready,
 output wire[1:0]S_AXI_bresp,output wire S_AXI_bvalid,input wire S_AXI_bready,
 input wire[31:0]S_AXI_araddr,input wire S_AXI_arvalid,output wire S_AXI_arready,
 output wire[31:0]S_AXI_rdata,output wire[1:0]S_AXI_rresp,output wire S_AXI_rvalid,input wire S_AXI_rready,
 input wire[31:0]control,input wire[4:0]physical_health,output wire[31:0]status,
 (* X_INTERFACE_PARAMETER="FREQ_HZ 128000000" *)output wire bram_clk,
 output wire bram_rst,output wire[3:0]bram_we,output wire bram_en,
 output wire[31:0]bram_addr,bram_wrdata,input wire[31:0]bram_rddata,
 input wire adc_busy,input wire[7:0]adc_dout,
 output wire adc_reset,adc_convst,adc_cs_n,adc_sclk,adc_sdi,
 output wire[1:0]rx_blank,output wire[31:0]serial_data,
 (* X_INTERFACE_IGNORE="true" *)output wire shift_clock,latch_clock,
 output wire output_disable,heartbeat,efuse_up,efuse_dn,irq);
 wire link_safe=physical_health[0]&physical_health[3]&physical_health[4];
 wire service_fresh;
 service_freshness service_watch(.clk(clk),.rst_n(rst_n),.kick(control[19]),
  .qualified(control[16]&control[17]&control[18]),.fresh(service_fresh));
 wire[7:0]health={control[18]&service_fresh,control[16]&service_fresh,link_safe,link_safe,control[17],physical_health[2:0]};
 prepcb_pl #(.CLOCK_HZ(128000000),.ADC_C16(1),.ADC_DOUT_LANES(8),.ADC_SCLK_DIVIDER(16),.TX_PIPELINE44(1)) implementation
 (.clk(clk),.tx_clk(tx_clk),.rst_n(rst_n),.control(control[15:0]),.health(health),
 .S_AXI_awaddr(S_AXI_awaddr),.S_AXI_awvalid(S_AXI_awvalid),.S_AXI_awready(S_AXI_awready),
 .S_AXI_wdata(S_AXI_wdata),.S_AXI_wstrb(S_AXI_wstrb),.S_AXI_wvalid(S_AXI_wvalid),.S_AXI_wready(S_AXI_wready),
 .S_AXI_bresp(S_AXI_bresp),.S_AXI_bvalid(S_AXI_bvalid),.S_AXI_bready(S_AXI_bready),
 .S_AXI_araddr(S_AXI_araddr),.S_AXI_arvalid(S_AXI_arvalid),.S_AXI_arready(S_AXI_arready),
 .S_AXI_rdata(S_AXI_rdata),.S_AXI_rresp(S_AXI_rresp),.S_AXI_rvalid(S_AXI_rvalid),.S_AXI_rready(S_AXI_rready),
 .status(status),.bram_clk(bram_clk),.bram_rst(bram_rst),.bram_we(bram_we),.bram_en(bram_en),
 .bram_addr(bram_addr),.bram_wrdata(bram_wrdata),.bram_rddata(bram_rddata),.adc_busy(adc_busy),.adc_dout(adc_dout),
 .adc_reset(adc_reset),.adc_convst(adc_convst),.adc_cs_n(adc_cs_n),.adc_sclk(adc_sclk),.adc_sdi(adc_sdi),
 .rx_blank(rx_blank),.serial_data(serial_data),.shift_clock(shift_clock),.latch_clock(latch_clock),
 .output_disable(output_disable),.heartbeat(heartbeat),.efuse_up(efuse_up),.efuse_dn(efuse_dn),.irq(irq));
endmodule
