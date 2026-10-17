`timescale 1ns/1ps
module safety_controller #(parameter integer FRAME_TIMEOUT_CYCLES=64) (
    input wire clk, rst_n, hardware_enable, software_enable,
    input wire frame_valid, fault,
    output wire drive_enable
);
    (* ASYNC_REG = "TRUE" *) reg [1:0] enable_sync;
    reg armed;
    localparam integer AGE_W=$clog2(FRAME_TIMEOUT_CYCLES+1);
    reg[AGE_W-1:0]frame_age;
    wire permit = rst_n && hardware_enable;
    // Asynchronous kill; release passes through two synchronizer stages and a fresh frame.
    always @(posedge clk or negedge permit) begin
        if (!permit) begin enable_sync <= 0; armed <= 0; frame_age<=0; end
        else begin
            enable_sync <= {enable_sync[0], 1'b1};
            if (!software_enable || fault) begin armed<=0;frame_age<=0;end
            else if(enable_sync[1]&&frame_valid)begin armed<=1;frame_age<=0;end
            else if(armed)begin
                if(frame_age>=FRAME_TIMEOUT_CYCLES-1)begin armed<=0;frame_age<=FRAME_TIMEOUT_CYCLES;end
                else frame_age<=frame_age+1;
            end
        end
    end
    assign drive_enable = permit && software_enable && !fault && armed;
endmodule
