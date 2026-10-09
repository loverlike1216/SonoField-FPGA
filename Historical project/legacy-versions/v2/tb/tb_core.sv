`timescale 1ns/1ps
module tb_core;
    parameter integer CHANNELS=128;
    localparam integer A=(CHANNELS<=1 ? 1 : $clog2(CHANNELS));
    reg clk=0; always #15.151515 clk=~clk;
    reg rst_n=0, write_valid=0, commit=0;
    reg channel_enable=1;
    reg [A-1:0] write_channel=0;
    reg [7:0] requested_phase=0, calibration_phase=0;
    wire write_ready,pending,commit_ack,command_error,active_valid,sample_valid,period_boundary;
    wire [7:0] master_phase;
    wire [CHANNELS*8-1:0] effective_phase;
    wire [CHANNELS-1:0] waveform;
    sono_core #(.CHANNELS(CHANNELS)) dut(.*);
    integer cycle=0, i, f, generation=0, ack_count=0, last_ack=-825, ticks=0;
    reg previous_ack=0;
    reg [7:0] expect_phase, expect_effective, delta;
    string trace_file;
    function automatic [7:0] req(input integer channel, input integer gen);
        if (gen==1) case(channel)
            0: req=0; 1: req=0; 2: req=64; 3: req=128; 4: req=255;
            default: req=(channel*37+11)%256;
        endcase
        else req=(channel*19+203)%256;
    endfunction
    function automatic [7:0] cal(input integer channel, input integer gen);
        if (gen==1 && channel<4) cal=0;
        else if(gen==1 && channel==4) cal=1;
        else cal=(channel*7+gen*13)%256;
    endfunction
    always @(posedge clk) begin
        if (!rst_n) cycle=0;
        else begin
            cycle=cycle+1;
            #1;
            expect_phase=((cycle*64'd10240000)/33000000)%256;
            if(master_phase!==expect_phase) $fatal(1,"TB01 phase cycle %0d got %0d expected %0d",cycle,master_phase,expect_phase);
            if(commit_ack) begin
                if(master_phase!==0 || previous_ack) $fatal(1,"TB08 commit not atomic boundary pulse");
                generation=generation+1; ack_count=ack_count+1; last_ack=cycle;
            end
            previous_ack=commit_ack;
            for(i=0;i<CHANNELS;i=i+1) begin
                expect_effective=(generation==0 ? 0 : req(i,generation)+cal(i,generation));
                if(effective_phase[i*8+:8]!==expect_effective) $fatal(1,"TB07/TB08 mixed phase map channel=%0d",i);
                delta=master_phase-expect_effective;
                if(waveform[i]!==((generation!=0 && (generation==1 || i%3!=0)) && ~delta[7]))
                    $fatal(1,"TB02-TB07 waveform channel=%0d cycle=%0d",i,cycle);
            end
            $fdisplay(f,"%0d,%0d,%0d,%0d,%h,%h",cycle,master_phase,generation,commit_ack,waveform,effective_phase);
        end
    end
    task tick; begin @(negedge clk); end endtask
    task write_one(input integer ch, input integer gen); begin
        tick; write_valid=1; write_channel=ch; requested_phase=req(ch,gen); calibration_phase=cal(ch,gen);
        channel_enable=(gen==1 || ch%3!=0);
        tick; write_valid=0;
        if(command_error) $fatal(1,"unexpected write error");
    end endtask
    task request_commit; begin tick; commit=1; tick; commit=0; end endtask
    initial begin
        if(!$value$plusargs("TRACE=%s",trace_file)) trace_file="trace.csv";
        f=$fopen(trace_file,"w"); if(!f) $fatal(1,"trace open failed");
        repeat(4) tick;
        if(active_valid!==0) $fatal(1,"reset active state");
        rst_n=1;
        request_commit;
        if(!command_error || pending) $fatal(1,"incomplete map accepted");
        if(CHANNELS>1 && (2**A)>CHANNELS) begin
            tick; write_valid=1; write_channel=CHANNELS;
            tick; write_valid=0;
            if(!command_error) $fatal(1,"out-of-range channel accepted");
        end
        write_one(0,1);
        if(CHANNELS>1) begin
            request_commit;
            if(!command_error || pending) $fatal(1,"partially written map accepted");
        end
        for(integer c=1;c<CHANNELS;c=c+1) write_one(c,1);
        request_commit;
        if(!pending) $fatal(1,"complete map rejected");
        request_commit;
        if(!command_error || !pending) $fatal(1,"duplicate pending commit not rejected");
        tick; write_valid=1; requested_phase=99; calibration_phase=99;
        tick; write_valid=0;
        if(!command_error) $fatal(1,"write during pending accepted");
        wait(commit_ack); tick;
        repeat(3300) tick;
        for(integer c=0;c<CHANNELS;c=c+1) write_one(c,2);
        // Simultaneous commit/write is explicitly rejected without modifying the map.
        tick; commit=1; write_valid=1;
        tick; commit=0; write_valid=0;
        if(!command_error || pending) $fatal(1,"simultaneous command not rejected");
        request_commit;
        wait(commit_ack); tick;
        repeat(3300) tick;
        if(ack_count!=2) $fatal(1,"commit count %0d",ack_count);
        $fclose(f);
        $display("PASS TB01 TB02 TB03 TB04 TB05 TB06 TB07 TB08 TB11 CHANNELS=%0d cycles=%0d",CHANNELS,cycle);
        $finish;
    end
    initial begin #1000000; $fatal(1,"timeout"); end
endmodule
