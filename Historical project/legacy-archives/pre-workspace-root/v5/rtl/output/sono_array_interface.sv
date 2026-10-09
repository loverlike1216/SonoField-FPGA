`timescale 1ns/1ps
// Pin-independent adapter. Board wrapper/XDC integration requires verified voltages.
module sono_array_interface (
 input wire clk,rst_n,global_disable,upper_permit,lower_permit,
 input wire [1:0] array_fault,
 input wire [31:0] serial_data,
 input wire shift_clock,latch_clock,
 input wire [1:0] rx_blank,
 output wire [15:0] upper_data,lower_data,
 output wire upper_shift_clock,lower_shift_clock,upper_latch_clock,lower_latch_clock,
 output wire upper_oe_n,lower_oe_n,upper_board_enable,lower_board_enable,
 output wire upper_rx_blank,lower_rx_blank
);
 reg previous_latch;
 always @(posedge clk or negedge rst_n)
  if(!rst_n)previous_latch<=0;else previous_latch<=latch_clock;
 wire fresh_frame=previous_latch&&!latch_clock;
 wire upper_drive,lower_drive;
 safety_controller upper_safe(.clk(clk),.rst_n(rst_n),
  .hardware_enable(upper_permit&&!global_disable&&!array_fault[0]),
  .software_enable(1'b1),.frame_valid(fresh_frame),.fault(1'b0),.drive_enable(upper_drive));
 safety_controller lower_safe(.clk(clk),.rst_n(rst_n),
  .hardware_enable(lower_permit&&!global_disable&&!array_fault[1]),
  .software_enable(1'b1),.frame_valid(fresh_frame),.fault(1'b0),.drive_enable(lower_drive));
 assign upper_data=serial_data[15:0];assign lower_data=serial_data[31:16];
 assign upper_shift_clock=shift_clock;assign lower_shift_clock=shift_clock;
 assign upper_latch_clock=latch_clock;assign lower_latch_clock=latch_clock;
 assign upper_oe_n=!upper_drive;assign lower_oe_n=!lower_drive;
 assign upper_board_enable=upper_drive;assign lower_board_enable=lower_drive;
 assign upper_rx_blank=rx_blank[0];assign lower_rx_blank=rx_blank[1];
endmodule
