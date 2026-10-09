`timescale 1ns/1ps
// Logical safety supervisor. Independent physical watchdog/cutoff remains REQUIRED.
module prepcb_supervisor #(
 parameter integer MS_CYCLES=132000, LONG_PRESS_MS=1000, DEBOUNCE_MS=20, TIMEOUT_MS=30000
)(input wire clk,rst_n,estop_loop_ok,pgood_up,pgood_dn,thermal_ok,link_ok,watchdog_ok,
 input wire ps_arm,pl_cal,clear_fault,cal_complete,cal_quality,trap_request,motion_request,motion_done,stop,
 output wire [3:0] state,output wire emit_permit,efuse_up,efuse_dn,output_disable,
 output reg heartbeat);
 localparam RESET_SAFE=1,BOARD_CHECK=2,ARMED_SAFE=3,CAL_SPARSE=4,CAL_QUALITY_GATE=5,
 CAL_READY=6,IDLE_TRAP=7,MOTION_EXEC=8,FAULT_LATCHED=9,ESTOP=10;
 wire healthy=pgood_up & pgood_dn & thermal_ok & link_ok & watchdog_ok;
 wire kill_ok=estop_loop_ok & healthy;
 reg [31:0] ms_div,arm_count,cal_count,age,arm_stable,cal_stable;
 reg [1:0] arm_sync,cal_sync;
 reg arm_db,cal_db,arm_released,cal_released;
 reg [3:0] state_reg;
 reg fault_latched,cold;
 wire fault_reset_n=rst_n & kill_ok;
 assign state=!rst_n?RESET_SAFE:(!estop_loop_ok?ESTOP:(fault_latched?FAULT_LATCHED:state_reg));
 wire tick=ms_div==MS_CYCLES-1;
 assign emit_permit=kill_ok & rst_n & ~stop & ((state==CAL_SPARSE)||(state==IDLE_TRAP)||(state==MOTION_EXEC));
 assign efuse_up=emit_permit;
 assign efuse_dn=emit_permit;
 assign output_disable=~emit_permit;
 always @(posedge clk or negedge rst_n) begin
  if(!rst_n)begin ms_div<=0;arm_sync<=0;cal_sync<=0;heartbeat<=0;end
  else begin
   arm_sync<={arm_sync[0],ps_arm};cal_sync<={cal_sync[0],pl_cal};
   if(tick)begin ms_div<=0;heartbeat<=~heartbeat;end else ms_div<=ms_div+1;
  end
 end
 // A constant asynchronous SET records even sub-clock kill pulses. State and
 // counters are synchronously controlled; no data-dependent asynchronous load.
 always @(posedge clk or negedge fault_reset_n) begin
  if(!fault_reset_n)fault_latched<=1;
  else if(cold||(clear_fault&&!arm_db&&!cal_db))fault_latched<=0;
 end
 always @(posedge clk or negedge rst_n) begin
  if(!rst_n)begin
   state_reg<=RESET_SAFE;cold<=1;arm_count<=0;cal_count<=0;age<=0;arm_stable<=0;cal_stable<=0;
   arm_db<=0;cal_db<=0;arm_released<=0;cal_released<=0;
  end else if(!kill_ok||fault_latched)begin
   if(cold&&kill_ok)begin state_reg<=RESET_SAFE;cold<=0;end
   else state_reg<=FAULT_LATCHED;
   arm_count<=0;cal_count<=0;age<=0;arm_stable<=0;cal_stable<=0;
   arm_db<=0;cal_db<=0;arm_released<=0;cal_released<=0;
  end else if(tick)begin
   cold<=0;
   if(arm_sync[1]==arm_db)arm_stable<=0;
   else if(arm_stable>=DEBOUNCE_MS-1)begin arm_db<=arm_sync[1];arm_stable<=0;end
   else arm_stable<=arm_stable+1;
   if(cal_sync[1]==cal_db)cal_stable<=0;
   else if(cal_stable>=DEBOUNCE_MS-1)begin cal_db<=cal_sync[1];cal_stable<=0;end
   else cal_stable<=cal_stable+1;
   if(!arm_db&&!arm_sync[1]&&!ps_arm)arm_released<=1;
   if(!cal_db&&!cal_sync[1]&&!pl_cal)cal_released<=1;
   arm_count<=(arm_db&&arm_released)?((arm_count<LONG_PRESS_MS)?arm_count+1:arm_count):0;
   cal_count<=(cal_db&&cal_released)?((cal_count<LONG_PRESS_MS)?cal_count+1:cal_count):0;
   age<=((state>=BOARD_CHECK)&&(state<=CAL_QUALITY_GATE))?age+1:0;
   if((state_reg==FAULT_LATCHED)||(state_reg==ESTOP))begin
    if(clear_fault&&!arm_db&&!cal_db)begin state_reg<=RESET_SAFE;arm_released<=0;cal_released<=0;end
   end else if(stop)begin state_reg<=RESET_SAFE;arm_released<=0;cal_released<=0;end
   else if(age>=TIMEOUT_MS)state_reg<=FAULT_LATCHED;
   else case(state_reg)
    RESET_SAFE:state_reg<=BOARD_CHECK;
    BOARD_CHECK:if(arm_released&&arm_count>=LONG_PRESS_MS)state_reg<=ARMED_SAFE;
    ARMED_SAFE:if(cal_released&&cal_count>=LONG_PRESS_MS)state_reg<=CAL_SPARSE;
    CAL_SPARSE:if(cal_complete)state_reg<=CAL_QUALITY_GATE;
    CAL_QUALITY_GATE:state_reg<=cal_quality?CAL_READY:FAULT_LATCHED;
    CAL_READY:if(trap_request)state_reg<=IDLE_TRAP;
    IDLE_TRAP:if(motion_request)state_reg<=MOTION_EXEC;
    MOTION_EXEC:if(motion_done)state_reg<=IDLE_TRAP;
    default:state_reg<=RESET_SAFE;
   endcase
  end
 end
endmodule
