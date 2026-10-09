`timescale 1ns/1ps
// Candidate module-reference top. All I/O are logical; never a production pinout.
module prepcb_pl(input wire clk,rst_n,
 input wire [31:0] S_AXI_awaddr,input wire S_AXI_awvalid,output wire S_AXI_awready,
 input wire [31:0] S_AXI_wdata,input wire [3:0] S_AXI_wstrb,input wire S_AXI_wvalid,output wire S_AXI_wready,
 output wire [1:0] S_AXI_bresp,output wire S_AXI_bvalid,input wire S_AXI_bready,
 input wire [31:0] S_AXI_araddr,input wire S_AXI_arvalid,output wire S_AXI_arready,
 output wire [31:0] S_AXI_rdata,output wire [1:0] S_AXI_rresp,output wire S_AXI_rvalid,input wire S_AXI_rready,
 input wire [15:0] control,input wire [7:0] health,output wire [31:0] status,
 output wire bram_clk,bram_rst,output wire [3:0] bram_we,output wire bram_en,
 output wire [31:0] bram_addr,bram_wrdata,input wire [31:0] bram_rddata,
 input wire adc_busy,input wire [3:0] adc_dout,
 output wire adc_reset,adc_convst,adc_cs_n,adc_sclk,adc_sdi,
 output wire [1:0] rx_blank,output wire [31:0] serial_data,
 output wire shift_clock,latch_clock,output_disable,heartbeat,efuse_up,efuse_dn,irq);
 wire emit_permit,supervisor_disable,core_disable;
 wire [3:0] state;
 wire [31:0] buffered_count,acknowledged_sequence;
 wire motion_running,motion_done,motion_underflow,motion_overflow,motion_invalid,motion_timeout,motion_request_pulse,motion_ack_pulse;
 wire core_fault=motion_underflow|motion_overflow|motion_invalid|motion_timeout;
 wire [127:0] commanded_waveform;
 wire frame_valid,frame_ready,frame_last,mailbox_busy,mailbox_invalid;
 wire core_frame_ready;
 wire task_allowed=(state==6)||(state==7)||(state==8);
 wire core_reset_n=rst_n && state!=9 && state!=10 && !control[7];
 wire [31:0] ps_ack_sequence=acknowledged_sequence+1;
 reg publish_armed;
 always @(posedge clk or negedge core_reset_n)begin
  if(!core_reset_n)publish_armed<=0;
  else if(!task_allowed)publish_armed<=0;
  else if(!control[9])publish_armed<=1;
 end
 assign frame_ready=core_frame_ready & task_allowed;
 wire [2175:0] frame_data;wire [31:0] frame_sequence;
 prepcb_frame_mailbox mailbox(.clk(clk),.rst_n(core_reset_n),.publish(control[9]&publish_armed),
  .bram_clk(bram_clk),.bram_rst(bram_rst),.bram_we(bram_we),.bram_en(bram_en),.bram_addr(bram_addr),.bram_wrdata(bram_wrdata),.bram_rddata(bram_rddata),
  .frame_valid(frame_valid),.frame_data(frame_data),.frame_sequence(frame_sequence),.frame_last(frame_last),.frame_ready(frame_ready),.busy(mailbox_busy),.invalid(mailbox_invalid));
 prepcb_supervisor supervisor(.clk(clk),.rst_n(rst_n),.estop_loop_ok(health[0]),
  .pgood_up(health[1]),.pgood_dn(health[2]),.thermal_ok(health[3]&health[6]&health[7]&~mailbox_invalid&~core_fault),.link_ok(health[4]),.watchdog_ok(health[5]),
  .ps_arm(control[0]),.pl_cal(control[1]),.clear_fault(control[2]),.cal_complete(control[3]),.cal_quality(control[4]),
  .trap_request(control[5]),.motion_request(control[6]),.motion_done(motion_done),.stop(control[7]),
  .state(state),.emit_permit(emit_permit),.output_disable(supervisor_disable),.heartbeat(heartbeat),.efuse_up(efuse_up),.efuse_dn(efuse_dn));
 assign output_disable=supervisor_disable|core_disable;
 assign status={ps_ack_sequence[15:0],buffered_count[5:0],mailbox_busy,mailbox_invalid,motion_timeout,motion_invalid,motion_overflow,motion_underflow,state};
 // The inherited queue latches STOP until reset. Keep its logical clock/enable
 // alive during SAFE for ADC setup and safe prefill; physical OE/eFuse stay
 // dominated by supervisor_disable above. Fault/STOP resets the whole core.
 // Mailbox uses task sequence1..N; original queue/ACK use0..N-1.
 sono_axi_system core(.clk(clk),.rst_n(core_reset_n),.hardware_enable(1'b1),.motion_arm(control[8]&emit_permit),.motion_stop(1'b0),
 .frame_valid(frame_valid&task_allowed),.frame_data(frame_data),.frame_sequence(frame_sequence-1),.frame_last(frame_last),.frame_ready(core_frame_ready),
 .buffered_count(buffered_count),.acknowledged_sequence(acknowledged_sequence),.motion_running(motion_running),.motion_done(motion_done),
 .motion_underflow(motion_underflow),.motion_overflow(motion_overflow),.motion_invalid(motion_invalid),.motion_timeout(motion_timeout),
 .motion_request_pulse(motion_request_pulse),.motion_ack_pulse(motion_ack_pulse),
 .s_awaddr(S_AXI_awaddr),.s_awvalid(S_AXI_awvalid),.s_awready(S_AXI_awready),.s_wdata(S_AXI_wdata),.s_wstrb(S_AXI_wstrb),.s_wvalid(S_AXI_wvalid),.s_wready(S_AXI_wready),
 .s_bresp(S_AXI_bresp),.s_bvalid(S_AXI_bvalid),.s_bready(S_AXI_bready),.s_araddr(S_AXI_araddr),.s_arvalid(S_AXI_arvalid),.s_arready(S_AXI_arready),
 .s_rdata(S_AXI_rdata),.s_rresp(S_AXI_rresp),.s_rvalid(S_AXI_rvalid),.s_rready(S_AXI_rready),
 .adc_busy(adc_busy),.adc_dout(adc_dout),.adc_reset(adc_reset),.adc_convst(adc_convst),.adc_cs_n(adc_cs_n),.adc_sclk(adc_sclk),.adc_sdi(adc_sdi),
 .rx_blank(rx_blank),.serial_data(serial_data),.shift_clock(shift_clock),.latch_clock(latch_clock),.output_disable(core_disable),.commanded_waveform(commanded_waveform),.irq(irq));
endmodule
