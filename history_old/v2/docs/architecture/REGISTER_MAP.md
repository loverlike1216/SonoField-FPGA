# Register map

synchronous 32-bit request/response, byte addresses, single cycle, no AXI wrapper claimed

| Name | Byte address |
|---|---|
| CONTROL | 0x00 |
| STATUS | 0x04 |
| MODE | 0x08 |
| FREQUENCY | 0x0c |
| BURST_CYCLES | 0x10 |
| START_PHASE | 0x14 |
| FIRST_TX | 0x18 |
| SCAN_COUNT | 0x1c |
| SAMPLE_PERIOD | 0x20 |
| PRE_SAMPLES | 0x24 |
| MAIN_SAMPLES | 0x28 |
| TAIL_SAMPLES | 0x2c |
| SETTLE_CYCLES | 0x30 |
| GUARD_CYCLES | 0x34 |
| BUFFER_ADDR | 0x38 |
| BUFFER_DATA | 0x3c |
| FRAME_COUNT | 0x40 |
| CAPTURE_TX | 0x44 |
| CAPTURE_SEQ | 0x48 |
| TIMESTAMP_LO | 0x4c |
| TIMESTAMP_HI | 0x50 |
| MAP_CHANNEL | 0x54 |
| MAP_DATA | 0x58 |
| MAP_WRITE | 0x5c |
| MAP_COMMIT | 0x60 |
| MAP_STATUS | 0x64 |
| ERROR | 0x68 |
| ACK_CAPTURE | 0x6c |
| BURST_TIMESTAMP_LO | 0x70 |
| BURST_TIMESTAMP_HI | 0x74 |
| TX_ENABLE_TIMESTAMP_LO | 0x78 |
| TX_ENABLE_TIMESTAMP_HI | 0x7c |
