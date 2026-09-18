`timescale 1ns/1ps
module phase_bank #(
    parameter integer CHANNELS = 128,
    parameter integer PHASE_BITS = 8,
    parameter integer ADDR_BITS = (CHANNELS <= 1 ? 1 : $clog2(CHANNELS))
) (
    input wire clk, rst_n, period_boundary,
    input wire write_valid, channel_enable,
    input wire [ADDR_BITS-1:0] write_channel,
    input wire [PHASE_BITS-1:0] requested_phase, calibration_phase,
    input wire commit,
    output wire write_ready,
    output reg pending, commit_ack, command_error, active_valid,
    output wire [CHANNELS*PHASE_BITS-1:0] effective_phase,
    output reg [CHANNELS-1:0] active_mask
);
    // Parallel register banks: no sequential copy can expose a mixed field.
    reg [PHASE_BITS-1:0] shadow_requested [0:CHANNELS-1];
    reg [PHASE_BITS-1:0] shadow_calibration [0:CHANNELS-1];
    reg [PHASE_BITS-1:0] active_requested [0:CHANNELS-1];
    reg [PHASE_BITS-1:0] active_calibration [0:CHANNELS-1];
    reg [CHANNELS-1:0] written;
    reg [CHANNELS-1:0] shadow_mask;
    integer i;
    assign write_ready = rst_n && !pending;
    genvar c;
    generate for (c=0; c<CHANNELS; c=c+1) begin: phases
        assign effective_phase[c*PHASE_BITS +: PHASE_BITS] = active_requested[c] + active_calibration[c];
    end endgenerate
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            written <= 0; pending <= 0; commit_ack <= 0; command_error <= 0; active_valid <= 0;
            shadow_mask <= 0; active_mask <= 0;
            for (i=0; i<CHANNELS; i=i+1) begin
                shadow_requested[i] <= 0; shadow_calibration[i] <= 0;
                active_requested[i] <= 0; active_calibration[i] <= 0;
            end
        end else begin
            commit_ack <= 0; command_error <= 0;
            if (pending && period_boundary) begin
                for (i=0; i<CHANNELS; i=i+1) begin
                    active_requested[i] <= shadow_requested[i];
                    active_calibration[i] <= shadow_calibration[i];
                end
                pending <= 0; written <= 0; commit_ack <= 1; active_valid <= 1;
                active_mask <= shadow_mask;
            end
            // Commit is a separate transaction after the last write. Simultaneous write+commit is rejected.
            if (commit) begin
                if (!pending && (&written) && !write_valid) pending <= 1;
                else command_error <= 1;
            end
            if (write_valid) begin
                if (!pending && !commit && write_channel < CHANNELS) begin
                    shadow_requested[write_channel] <= requested_phase;
                    shadow_calibration[write_channel] <= calibration_phase;
                    written[write_channel] <= 1;
                    shadow_mask[write_channel] <= channel_enable;
                end else command_error <= 1;
            end
        end
    end
endmodule
