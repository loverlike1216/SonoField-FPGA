`timescale 1ns/1ps
// Board-independent integration top; CLOCK_FREQ=0 deliberately requires a chosen interface clock.
// Proposed simulation profile: 132 MHz (4 x documented 33 MHz); no board PLL/pins are claimed.
module sono_top #(
    parameter integer CHANNELS=128, PHASE_BITS=8, LANES=32,
    parameter integer CLOCK_FREQ=0, ULTRASONIC_FREQ=40000,
    parameter integer ADDR_BITS=(CHANNELS<=1 ? 1 : $clog2(CHANNELS))
) (
    input wire clk, rst_n, hardware_enable, software_enable,
    input wire write_valid, commit, channel_enable,
    input wire [ADDR_BITS-1:0] write_channel,
    input wire [PHASE_BITS-1:0] requested_phase, calibration_phase,
    output wire write_ready, pending, commit_ack, command_error,
    output wire [LANES-1:0] serial_data,
    output wire shift_clock, latch_clock, output_disable, serializer_fault,
    output wire [CHANNELS-1:0] safe_waveform
);
    localparam integer FRAME_CYCLES=2*((CHANNELS+LANES-1)/LANES)+3;
    initial if (CLOCK_FREQ/(ULTRASONIC_FREQ*(2**PHASE_BITS)) < FRAME_CYCLES)
        $fatal(1,"Serializer bandwidth insufficient: increase lanes/clock, do not drop phase samples");
    (* ASYNC_REG = "TRUE" *) reg [1:0] reset_sync;
    always @(posedge clk or negedge rst_n)
        if (!rst_n) reset_sync<=0; else reset_sync<={reset_sync[0],1'b1};
    wire core_reset_n=reset_sync[1];
    wire [CHANNELS-1:0] waveform;
    wire active_valid, sample_valid, frame_done, busy, drive_enable;
    sono_core #(.CHANNELS(CHANNELS),.PHASE_BITS(PHASE_BITS),.CLOCK_FREQ(CLOCK_FREQ),.ULTRASONIC_FREQ(ULTRASONIC_FREQ)) core(
        .clk(clk),.rst_n(core_reset_n),.write_valid(write_valid),.write_channel(write_channel),.channel_enable(channel_enable),
        .requested_phase(requested_phase),.calibration_phase(calibration_phase),.commit(commit),
        .write_ready(write_ready),.pending(pending),.commit_ack(commit_ack),.command_error(command_error),
        .active_valid(active_valid),.waveform(waveform),.sample_valid(sample_valid),
        .master_phase(),.effective_phase(),.period_boundary());
    serializer #(.CHANNELS(CHANNELS),.LANES(LANES)) serial_out(
        .clk(clk),.rst_n(core_reset_n),.start(sample_valid && active_valid),.waveform(waveform),
        .serial_data(serial_data),.shift_clock(shift_clock),.latch_clock(latch_clock),
        .busy(busy),.frame_done(frame_done),.overrun(serializer_fault));
    safety_controller safety(.clk(clk),.rst_n(core_reset_n && rst_n),.hardware_enable(hardware_enable),
        .software_enable(software_enable),.frame_valid(frame_done && active_valid),
        .fault(serializer_fault),.drive_enable(drive_enable));
    assign output_disable=~drive_enable;
    assign safe_waveform=waveform & {CHANNELS{drive_enable}};
endmodule
