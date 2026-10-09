`timescale 1ns/1ps
module tb_serializer_fault;
    reg clk=0; always #5 clk=~clk;
    reg rst_n=0,start=0;
    reg [4:0] waveform=5'b10101;
    wire [1:0] serial_data;
    wire shift_clock,latch_clock,busy,frame_done,overrun;
    wire drive_enable;
    serializer #(.CHANNELS(5),.LANES(2)) dut(.*);
    safety_controller guard(.clk(clk),.rst_n(rst_n),.hardware_enable(1'b1),.software_enable(1'b1),
        .frame_valid(frame_done),.fault(overrun),.drive_enable(drive_enable));
    reg [2:0] model0=0,model1=0;
    always @(posedge shift_clock) begin model0={model0[1:0],serial_data[0]}; model1={model1[1:0],serial_data[1]}; end
    always @(posedge latch_clock) if({model1,model0}!==6'b010101) $fatal(1,"padding/order");
    initial begin
        repeat(3) @(negedge clk); rst_n=1; start=1;
        @(negedge clk); start=0;
        wait(frame_done); repeat(3) @(negedge clk);
        if(!drive_enable) $fatal(1,"guard did not arm");
        start=1; repeat(2) @(negedge clk); start=0;
        if(!overrun || drive_enable) $fatal(1,"overrun did not fail closed");
        repeat(20) @(negedge clk);
        if(!overrun || drive_enable) $fatal(1,"fault not sticky");
        $display("PASS serializer padding, overrun and fault disable"); $finish;
    end
    initial begin #10000; $fatal(1,"timeout"); end
endmodule
