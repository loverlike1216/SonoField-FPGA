`timescale 1ns/1ps
module sono_core #(
    parameter integer CHANNELS=128, PHASE_BITS=8,
    parameter integer CLOCK_FREQ=33000000, ULTRASONIC_FREQ=40000,
    parameter integer ADDR_BITS=(CHANNELS<=1 ? 1 : $clog2(CHANNELS))
) (
    input wire clk, rst_n,
    input wire write_valid, commit, channel_enable,
    input wire [ADDR_BITS-1:0] write_channel,
    input wire [PHASE_BITS-1:0] requested_phase, calibration_phase,
    output wire write_ready, pending, commit_ack, command_error, active_valid,
    output wire [PHASE_BITS-1:0] master_phase,
    output wire [CHANNELS*PHASE_BITS-1:0] effective_phase,
    output wire [CHANNELS-1:0] waveform,
    output reg sample_valid,
    output wire period_boundary
);
    wire phase_tick;
    wire [CHANNELS-1:0] active_mask;
    initial if (CHANNELS<1 || CHANNELS>128) $fatal(1,"CHANNELS must be 1..128");
    ultrasonic_timebase #(.CLOCK_FREQ(CLOCK_FREQ),.ULTRASONIC_FREQ(ULTRASONIC_FREQ),.PHASE_BITS(PHASE_BITS))
        timebase(.clk(clk),.rst_n(rst_n),.master_phase(master_phase),.phase_tick(phase_tick),.period_boundary(period_boundary));
    phase_bank #(.CHANNELS(CHANNELS),.PHASE_BITS(PHASE_BITS)) bank(
        .clk(clk),.rst_n(rst_n),.period_boundary(period_boundary),.write_valid(write_valid),.channel_enable(channel_enable),
        .write_channel(write_channel),.requested_phase(requested_phase),.calibration_phase(calibration_phase),
        .commit(commit),.write_ready(write_ready),.pending(pending),.commit_ack(commit_ack),
        .command_error(command_error),.active_valid(active_valid),.effective_phase(effective_phase),.active_mask(active_mask));
    channel_waveform #(.CHANNELS(CHANNELS),.PHASE_BITS(PHASE_BITS)) waves(
        .master_phase(master_phase),.effective_phase(effective_phase),.active_mask(active_mask),.waveform(waveform));
    always @(posedge clk or negedge rst_n)
        if (!rst_n) sample_valid<=0; else sample_valid<=phase_tick;
endmodule
