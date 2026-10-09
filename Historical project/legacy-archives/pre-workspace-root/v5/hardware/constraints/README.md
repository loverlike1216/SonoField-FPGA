# AX7020 constraints boundary

core_ooc.xdc constrains only internal sono_axi_system132MHz OOC analysis. It assigns no package pins and is not complete board timing. Manufacturer documents show PL clock U18/50MHz, but physical revision and application connector allocation/IO/loading must be reviewed before a production XDC is created. No old board pins or preset are inherited. PS/XSA/BSP and real UART/DDR are not deployed. No bitstream generation or hardware programming is included.
