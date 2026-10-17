`timescale 1ns/1ps
//Common132/264MHz clocks; snapshot is held across the fast capture edge.
//Completion crosses back as a toggle, never as an undersampled3.8ns pulse.
module tx_pipeline44(input wire clk,tx_clk,rst_n,start,
 input wire[127:0]waveform,output wire[31:0]serial_data,
 output wire shift_clock,latch_clock,busy,frame_done,overrun);
 reg request_q;reg[127:0]snapshot;
 always@(posedge clk or negedge rst_n)
  if(!rst_n)begin request_q<=0;snapshot<=0;end
  else begin request_q<=start;if(start)snapshot<=waveform;end
 wire done_fast,overrun_fast,busy_fast;reg done_toggle;
 (* ASYNC_REG="TRUE" *)reg[1:0]fast_release;
 reg[2:0]request_pipe;
 reg[127:0]fast_hold;
 always@(posedge tx_clk or negedge rst_n)
  if(!rst_n)fast_release<=0;else fast_release<={fast_release[0],1'b1};
 always@(posedge tx_clk or negedge fast_release[1])
  if(!fast_release[1])begin request_pipe<=0;fast_hold<=0;end
  else begin
   request_pipe<={request_pipe[1:0],request_q};
   if(request_pipe[0])fast_hold<=snapshot;
  end
 serializer_pipeline_44 tx(tx_clk,fast_release[1],request_pipe[2],fast_hold,serial_data,shift_clock,latch_clock,busy_fast,done_fast,overrun_fast);
 always@(posedge tx_clk or negedge fast_release[1])
  if(!fast_release[1])done_toggle<=0;else if(done_fast)done_toggle<=!done_toggle;
 (* ASYNC_REG="TRUE" *) reg[1:0]done_sync,overrun_sync,busy_sync;
 reg previous_done;
 always@(posedge clk or negedge rst_n)
  if(!rst_n)begin done_sync<=0;overrun_sync<=0;busy_sync<=0;previous_done<=0;end
  else begin done_sync<={done_sync[0],done_toggle};previous_done<=done_sync[1];
   overrun_sync<={overrun_sync[0],overrun_fast};busy_sync<={busy_sync[0],busy_fast};end
 assign frame_done=done_sync[1]^previous_done;
 assign overrun=overrun_sync[1];assign busy=busy_sync[1];
endmodule
