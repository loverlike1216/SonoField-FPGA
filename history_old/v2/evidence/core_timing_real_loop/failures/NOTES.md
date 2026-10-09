# Testbench correction

The new independent phase oracle initially tested an uninitialized internal synchronized reset at simulation time zero. The real external reset was already asserted. The oracle now observes both external reset and internal reset, matching the DUT reset contract; no functional comparisons, thresholds or existing tests were removed. Raw initial failure retained.
