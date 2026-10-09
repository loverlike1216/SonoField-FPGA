# Sparse geometry calibration

16 unique diagonals per8×8 array; upperTX→fourlowerRX and lowerTX→fourupperRX,
128directedpaths. Optional supplemental TX IDs are explicit, not silently
invented measurements. Capture plan preserves oneTX and timestamps/temperature/
frequency/rawreference/quality/source metadata. Physical burst16cycles is a
candidate; actual onset/ring-up/AFE/CONVST alignment is NOT_VERIFIED.

Singlefrequency phase cannot determine carrier cycle by itself. `refine_tof`
requires independently supplied coarseuncertainty<.45/f and consistency, then
refines the nearest cycle. The C feature extractor supplies I/Q amplitude,
phase and an envelope-onset ESTIMATE; that estimate alone does not establish
the required physical coarsebound. Any production adapter must supply measured
frontend alignment and conservative independent uncertainty.

Fit6DoF plus6RXdelays; RX0/RX4 delays explicitly fixed0 as reference gauges,
not measuredzero. Translation±5mm, gap90–115mm and Euler±3° bounds are enforced.
SoftL1 multiple starts, residual rejection, scaledJacobian SVD rank12,
condition<1e5 and covariance are recorded. SNR≥35dB remains mandatory.
Missing RX coverage/duplicate paths/lowSNR/ambiguouscycle fail closed. Suggested
additional off-diagonalTX do not fix an unmeasured absolute timing gauge.

At least5randomseeds×uniform/gradienttemperature=10fits, each5initialguesses,
are compared to numerical groundtruth and384non-scanned holdoutpaths. Existing
translation<.1mm and angle<.1° remain; new holdout max<80ns. Independent repeat
must reproduce the same posehash. Explicit threeoutlier test and missingRX/
SNR34.9/20uscoarsebound rejection are recorded. Exact outputs, observations,
covariance and hashes are in current successful `system*/sparse/` evidence.
All references are SYNTHETIC_REFERENCE / ALTERNATIVE_VALIDATION.

Output grade is only GEOMETRY_SPARSITY_CALIBRATED. Every128TX channel remains
UNMEASURED with null individualgain/phaseoffset. Actual levitationbounds=null,
RXpositionprovenance=nominalmechanical. This does not complete fullchannel
amplitude/phase calibration, hardware self-calibration or particle support.

JSON schemas under `schemas/` describe directedobservations and resultpayload.
Runtime-generated observation/result files are examples with explicit source
and raw_ref=null. Never relabel them RAW_ADC. Existing calibration regression
and truth/error limits remain separate, unchanged and fully required.
