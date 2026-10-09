`timescale 1ns/1ps
module tb_system;
    reg clk=0; always #3.787879 clk=~clk;
    reg rst_n=0, hardware_enable=0, software_enable=0, write_valid=0, commit=0;
    reg channel_enable=1;
    reg [6:0] write_channel=0;
    reg [7:0] requested_phase=0, calibration_phase=0;
    wire write_ready,pending,commit_ack,command_error,shift_clock,latch_clock,output_disable,serializer_fault;
    wire [31:0] serial_data;
    wire [127:0] safe_waveform;
    sono_top #(.CLOCK_FREQ(132000000)) dut(.*);
    reg [3:0] shift_model[0:31];
    reg [127:0] expected_capture;
    integer frames=0, bits=0;
    always @(posedge clk) begin
        if(dut.core_reset_n && dut.sample_valid && dut.active_valid) expected_capture=dut.waveform;
    end
    always @(posedge shift_clock) begin
        for(integer lane=0;lane<32;lane=lane+1) shift_model[lane]={shift_model[lane][2:0],serial_data[lane]};
        bits=bits+1;
    end
    always @(posedge latch_clock) begin
        if(bits!=4) $fatal(1,"TB12 bit count %0d",bits);
        for(integer lane=0;lane<32;lane=lane+1)
            if(shift_model[lane]!==expected_capture[lane*4+:4]) $fatal(1,"TB12/TB13 lane %0d",lane);
        bits=0; frames=frames+1;
    end
    task tick; begin @(negedge clk); end endtask
    initial begin
        for(integer l=0;l<32;l=l+1) shift_model[l]=0;
        repeat(4) tick;
        if(output_disable!==1 || safe_waveform!==0) $fatal(1,"TB09 reset not safe");
        rst_n=1; hardware_enable=1; software_enable=1;
        repeat(8) tick;
        if(!output_disable) $fatal(1,"TB10 enabled without map/frame");
        for(integer c=0;c<128;c=c+1) begin
            tick; write_valid=1; write_channel=c; requested_phase=c*7; calibration_phase=c*3;
        end
        tick; write_valid=0;
        tick; commit=1;
        tick; commit=0;
        wait(!output_disable);
        repeat(7000) tick;
        if(serializer_fault || frames<500) $fatal(1,"serializer throughput failure frames=%0d",frames);
        #1; hardware_enable=0; #0.1;
        if(output_disable!==1 || safe_waveform!==0) $fatal(1,"TB09 asynchronous kill failure");
        repeat(20) tick;
        hardware_enable=1;
        #0.1; if(!output_disable) $fatal(1,"TB10 unsafe immediate reenable");
        wait(!output_disable);
        tick; software_enable=0; #0.1;
        if(!output_disable || safe_waveform!==0) $fatal(1,"software disable failure");
        tick; software_enable=1;
        wait(!output_disable);
        #1; rst_n=0; #0.1;
        if(!output_disable || safe_waveform!==0) $fatal(1,"async reset failure");
        $display("PASS TB09 TB10 TB12 TB13 integrated frames=%0d",frames);
        $finish;
    end
    initial begin #200000; $fatal(1,"timeout"); end
endmodule
