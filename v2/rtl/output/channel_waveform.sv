`timescale 1ns/1ps
module channel_waveform #(
    parameter integer CHANNELS = 128, PHASE_BITS = 8
) (
    input wire [PHASE_BITS-1:0] master_phase,
    input wire [CHANNELS*PHASE_BITS-1:0] effective_phase,
    input wire [CHANNELS-1:0] active_mask,
    output wire [CHANNELS-1:0] waveform
);
    genvar c;
    generate for (c=0; c<CHANNELS; c=c+1) begin: channel
        // Positive phase is a delay, consistent with field phasors using exp(-j*omega*t).
        wire [PHASE_BITS-1:0] local_phase = master_phase - effective_phase[c*PHASE_BITS +: PHASE_BITS];
        assign waveform[c] = active_mask[c] && ~local_phase[PHASE_BITS-1];
    end endgenerate
endmodule
