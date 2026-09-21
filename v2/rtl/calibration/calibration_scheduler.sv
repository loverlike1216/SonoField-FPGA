`timescale 1ns/1ps
// All acquisition windows overlap the burst/propagation interval. Host ACK owns reuse.
module calibration_scheduler #(parameter integer DEPTH=1024)(
 input wire clk,rst_n,start,abort,ack,adc_ready,adc_idle,adc_error,frame_valid,
 input wire [127:0] frame,input wire[63:0] frame_timestamp,time_now,
 input wire[31:0] sample_period,pre_samples,main_samples,tail_samples,settle_cycles,guard_cycles,
 input wire[6:0] first_tx,input wire[7:0] scan_count,
 input wire burst_active,burst_done,
 input wire[11:0] read_address,output wire[31:0] read_data,
 output reg sample_request,burst_start,capture_ready,done,error,
 output reg[6:0] selected_tx,output reg[7:0] capture_sequence,
 output reg[10:0] frame_count,output reg[63:0] first_timestamp,burst_timestamp,
 output wire[1:0] rx_blank,output wire active,output wire[3:0] state_debug);
 localparam IDLE=0,SETTLE=1,CAPTURE=2,DRAIN=3,WAIT_ACK=4,GUARD=5,FINISHED=6,FAULT=7;
 reg[3:0] state;reg[31:0] wait_count,period_count,issued,total;
 (* ram_style="block" *) reg[127:0] memory[0:DEPTH-1];
 reg[127:0] read_frame;reg[1:0] read_word;reg read_valid;
 assign active=state==SETTLE||state==CAPTURE||state==DRAIN||state==GUARD;
 assign state_debug=state;
 // 1 = receiver bank blanked. Opposite bank unblanked before settling starts.
 assign rx_blank=(state==SETTLE||state==CAPTURE||state==DRAIN)?(selected_tx[6]?2'b10:2'b01):2'b11;
 // Synchronous full-frame read enables block RAM inference; select the host word afterwards.
 always @(posedge clk)begin
  read_frame<=memory[read_address[11:2]];read_word<=read_address[1:0];
  read_valid<=read_address[11:2]<frame_count;
 end
 assign read_data=read_valid?read_frame[read_word*32+:32]:0;
 always @(posedge clk or negedge rst_n)begin
  if(!rst_n)begin
   state<=IDLE;sample_request<=0;burst_start<=0;capture_ready<=0;done<=0;error<=0;
   selected_tx<=0;capture_sequence<=0;frame_count<=0;first_timestamp<=0;burst_timestamp<=0;
   wait_count<=0;period_count<=0;issued<=0;total<=0;
  end else begin
   sample_request<=0;burst_start<=0;
   if(abort)begin state<=IDLE;capture_ready<=0;done<=0;end
   else if(adc_error)begin state<=FAULT;error<=1;capture_ready<=0;end
   else case(state)
    IDLE,FINISHED:if(start)begin
     if(!adc_ready||!adc_idle||scan_count==0||scan_count>128||pre_samples==0||
        pre_samples+main_samples+tail_samples>DEPTH||main_samples==0||sample_period<165)begin error<=1;state<=FAULT;end
     else begin selected_tx<=first_tx;capture_sequence<=0;total<=pre_samples+main_samples+tail_samples;
      wait_count<=0;frame_count<=0;issued<=0;capture_ready<=0;done<=0;state<=SETTLE;end
    end
    SETTLE:if(wait_count>=settle_cycles)begin period_count<=0;state<=CAPTURE;end else wait_count<=wait_count+1;
    CAPTURE,DRAIN:begin
     if(state==CAPTURE)begin
      if(period_count==0)begin
       sample_request<=1;issued<=issued+1;period_count<=sample_period-1;
       if(issued==pre_samples)begin burst_start<=1;burst_timestamp<=time_now+1;end
       if(issued+1==total)state<=DRAIN;
      end else period_count<=period_count-1;
     end
     if(frame_valid)begin
      if(frame_count>=DEPTH)begin error<=1;state<=FAULT;end
      else begin
       memory[frame_count]<=frame;frame_count<=frame_count+1;
       if(frame_count==0)first_timestamp<=frame_timestamp;
       if(frame_count+1==total)begin
        if(burst_active)begin error<=1;state<=FAULT;end
        else begin capture_ready<=1;state<=WAIT_ACK;end
       end
      end
     end
    end
    WAIT_ACK:if(ack)begin
     capture_ready<=0;
     if(capture_sequence+1==scan_count)begin done<=1;state<=FINISHED;end
     else begin wait_count<=0;state<=GUARD;end
    end
    GUARD:if(wait_count>=guard_cycles && adc_idle)begin
     selected_tx<=selected_tx+1;capture_sequence<=capture_sequence+1;
     frame_count<=0;issued<=0;wait_count<=0;state<=SETTLE;
    end else wait_count<=wait_count+1;
    FAULT:begin capture_ready<=0;done<=0;end
    default:begin error<=1;state<=FAULT;end
   endcase
  end
 end
endmodule
