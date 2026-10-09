`timescale 1ns/1ps
module tb_bad_bandwidth;
    sono_top #(.CLOCK_FREQ(33000000)) dut(.clk(1'b0),.rst_n(1'b0),.hardware_enable(1'b0),
        .software_enable(1'b0),.write_valid(1'b0),.commit(1'b0),.channel_enable(1'b0),
        .write_channel(7'd0),.requested_phase(8'd0),.calibration_phase(8'd0));
    initial begin #100; $fatal(1,"MISSING_BANDWIDTH_GUARD"); end
endmodule
