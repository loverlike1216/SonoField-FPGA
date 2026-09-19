`timescale 1ns/1ps
module serializer #(
    parameter integer CHANNELS=128, LANES=32,
    parameter integer BITS_PER_LANE=(CHANNELS+LANES-1)/LANES
) (
    input wire clk, rst_n, start,
    input wire [CHANNELS-1:0] waveform,
    output reg [LANES-1:0] serial_data,
    output reg shift_clock, latch_clock, busy, frame_done, overrun
);
    localparam integer PADDED=LANES*BITS_PER_LANE;
    reg [PADDED-1:0] captured;
    integer bit_index;
    reg [1:0] state;
    integer l;
    localparam IDLE=0, SHIFT=1, LATCH=2, FINISH=3;
    initial if (LANES<1 || BITS_PER_LANE<1) $fatal(1,"Invalid serializer parameters");
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            captured<=0; serial_data<=0; shift_clock<=0; latch_clock<=0;
            busy<=0; frame_done<=0; overrun<=0; bit_index<=0; state<=IDLE;
        end else begin
            frame_done<=0;
            if (start && busy) overrun<=1;
            case (state)
                IDLE: if (start) begin
                    captured <= {{(PADDED-CHANNELS){1'b0}},waveform};
                    for (l=0;l<LANES;l=l+1)
                        if (l*BITS_PER_LANE+BITS_PER_LANE-1<CHANNELS)
                            serial_data[l]<=waveform[l*BITS_PER_LANE+BITS_PER_LANE-1];
                        else serial_data[l]<=0;
                    bit_index<=BITS_PER_LANE-1; busy<=1; state<=SHIFT;
                end
                SHIFT: begin
                    if (!shift_clock) shift_clock<=1;
                    else begin
                        shift_clock<=0;
                        if (bit_index==0) state<=LATCH;
                        else begin
                            bit_index<=bit_index-1;
                            for(l=0;l<LANES;l=l+1) serial_data[l]<=captured[l*BITS_PER_LANE+bit_index-1];
                        end
                    end
                end
                LATCH: begin latch_clock<=1; state<=FINISH; end
                FINISH: begin latch_clock<=0; frame_done<=1; busy<=0; state<=IDLE; end
            endcase
        end
    end
endmodule
