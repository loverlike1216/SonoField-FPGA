`timescale 1ns/1ps
module safety_controller (
    input wire clk, rst_n, hardware_enable, software_enable,
    input wire frame_valid, fault,
    output wire drive_enable
);
    (* ASYNC_REG = "TRUE" *) reg [1:0] enable_sync;
    reg armed;
    wire permit = rst_n && hardware_enable;
    // Asynchronous kill; release passes through two synchronizer stages and a fresh frame.
    always @(posedge clk or negedge permit) begin
        if (!permit) begin enable_sync <= 0; armed <= 0; end
        else begin
            enable_sync <= {enable_sync[0], 1'b1};
            if (!software_enable || fault) armed <= 0;
            else if (enable_sync[1] && frame_valid) armed <= 1;
        end
    end
    assign drive_enable = permit && software_enable && !fault && armed;
endmodule
