`timescale 1ns/1ps
module ultrasonic_timebase #(
    parameter integer CLOCK_FREQ = 33000000,
    parameter integer ULTRASONIC_FREQ = 40000,
    parameter integer PHASE_BITS = 8
) (
    input wire clk, input wire rst_n,
    output reg [PHASE_BITS-1:0] master_phase,
    output wire phase_tick, output wire period_boundary
);
    localparam integer STEP_RATE = ULTRASONIC_FREQ * (2**PHASE_BITS);
    localparam integer WIDTH = $clog2(CLOCK_FREQ + STEP_RATE + 1);
    reg [WIDTH-1:0] remainder;
    wire [WIDTH:0] next_sum = {1'b0, remainder} + STEP_RATE;
    assign phase_tick = rst_n && (next_sum >= CLOCK_FREQ);
    assign period_boundary = phase_tick && (&master_phase);
    initial begin
        if (PHASE_BITS < 1 || PHASE_BITS > 12 || ULTRASONIC_FREQ <= 0 || CLOCK_FREQ < STEP_RATE)
            $fatal(1, "Invalid timebase parameters");
    end
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin remainder <= 0; master_phase <= 0; end
        else if (phase_tick) begin
            remainder <= next_sum - CLOCK_FREQ;
            master_phase <= master_phase + 1'b1;
        end else remainder <= next_sum;
    end
endmodule
