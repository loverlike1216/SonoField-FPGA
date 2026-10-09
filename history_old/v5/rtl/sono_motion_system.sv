`timescale 1ns/1ps
// Integrates the existing digital system unchanged in function. All new interfaces
// are internal PL/PS interfaces; no physical pin assignment is implied.
module sono_motion_system #(
 parameter integer CLOCK_HZ=132000000,POWER_WAIT_CYCLES=2*CLOCK_HZ+1,
 parameter integer INTERVAL_CYCLES=CLOCK_HZ/50,QUEUE_DEPTH=4
)(input wire clk,rst_n,hardware_enable,motion_arm,motion_stop,
 input wire frame_valid,input wire [2175:0] frame_data,input wire [31:0] frame_sequence,input wire frame_last,
 output wire frame_ready,output wire [31:0] buffered_count,acknowledged_sequence,
 output wire motion_running,motion_done,motion_underflow,motion_overflow,motion_invalid,motion_timeout,
 output wire motion_request_pulse,motion_ack_pulse,
 input wire bus_valid,bus_write,input wire [7:0] bus_address,input wire [31:0] bus_wdata,
 output wire [31:0] bus_rdata,output wire bus_ready,bus_error,
 input wire adc_busy,input wire [3:0] adc_dout,
 output wire adc_reset,adc_convst,adc_cs_n,adc_sclk,adc_sdi,
 output wire [1:0] rx_blank,output wire [31:0] serial_data,
 output wire shift_clock,latch_clock,output_disable,output wire [127:0] commanded_waveform,output wire irq);
 wire qvalid,qwrite,native_ready,native_error,map_ack,kill;
 wire [7:0] qaddress;wire [31:0] qdata;
 wire owned=motion_running||qvalid;
 assign bus_ready=bus_valid&&!owned;
 assign bus_error=native_error||(bus_valid&&owned);
 motion_queue #(.DEPTH(QUEUE_DEPTH),.INTERVAL_CYCLES(INTERVAL_CYCLES),.ACK_TIMEOUT_CYCLES(CLOCK_HZ/20000)) queue(
 .clk(clk),.rst_n(rst_n),.arm(motion_arm),.stop(motion_stop||!hardware_enable),
 .frame_valid(frame_valid),.frame_data(frame_data),.frame_sequence(frame_sequence),.frame_last(frame_last),
 .frame_ready(frame_ready),.count(buffered_count),.bus_valid(qvalid),.bus_write(qwrite),.bus_address(qaddress),
 .bus_wdata(qdata),.bus_ready(native_ready),.bus_error(native_error),.map_ack(map_ack),
 .running(motion_running),.done(motion_done),.underflow(motion_underflow),.overflow(motion_overflow),
 .invalid_frame(motion_invalid),.ack_timeout(motion_timeout),.disable_request(kill),
 .acknowledged_sequence(acknowledged_sequence),.request_pulse(motion_request_pulse),.ack_pulse(motion_ack_pulse));
 sono_digital_system #(.CLOCK_HZ(CLOCK_HZ),.POWER_WAIT_CYCLES(POWER_WAIT_CYCLES)) digital(
 .clk(clk),.rst_n(rst_n),.hardware_enable(hardware_enable&&!kill),
 .bus_valid(owned?qvalid:bus_valid),.bus_write(owned?qwrite:bus_write),
 .bus_address(owned?qaddress:bus_address),.bus_wdata(owned?qdata:bus_wdata),
 .bus_rdata(bus_rdata),.bus_ready(native_ready),.bus_error(native_error),
 .adc_busy(adc_busy),.adc_dout(adc_dout),.adc_reset(adc_reset),.adc_convst(adc_convst),
 .adc_cs_n(adc_cs_n),.adc_sclk(adc_sclk),.adc_sdi(adc_sdi),.rx_blank(rx_blank),
 .serial_data(serial_data),.shift_clock(shift_clock),.latch_clock(latch_clock),
 .output_disable(output_disable),.commanded_waveform(commanded_waveform),.irq(irq),.motion_map_ack(map_ack));
endmodule
