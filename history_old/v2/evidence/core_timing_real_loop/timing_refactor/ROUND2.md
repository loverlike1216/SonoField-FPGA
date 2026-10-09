# Round 2

Round 1 removed the main phase divider and exposed the equivalent burst divider as the new worst cone (synthesis WNS -7.911 ns, 24 levels, burst accumulator to serialized data). Apply the same exact rational phase representation to burst generation; preserve start/abort/completed/done timing and offsets. Compare every clock against the preserved baseline RTL over 256 offsets and 38500/40000/41500 Hz. No frequency profile change and no pipeline latency.
