# Calibration run report

SIMULATION_ESTIMATE. No physical calibration or levitation claim.

## System metadata

```json
{
  "board_revision": "SYNTHETIC",
  "classification": "SIMULATION_ESTIMATE",
  "git_commit": "4e5f0478e036cfefbadb2f6ceeb2ef1d180b6467",
  "lower_board_id": "SIM_LOWER",
  "project_version": "v2",
  "rx_batch": "SIM_SEED_7020",
  "timestamp": "2000-01-01T00:00:00Z",
  "tx_batch": "SIM_SEED_7020",
  "upper_board_id": "SIM_UPPER"
}
```

## Environment

```json
{
  "co2_ppm": 420,
  "humidity_percent": 55.0,
  "pressure_pa": 101325.0,
  "pressure_source": "ASSUMED_STANDARD_ATMOSPHERE",
  "temperature_c": 26.5
}
```

## Measured pose

```json
[
  0.0007073332692013412,
  -0.0005172320001195456,
  0.09880893128661596,
  0.34872553919096266,
  -0.21679653650869837,
  0.14929230017052433
]
```

## Quality and masks

```json
{
  "active_disabled_channels": [],
  "classification": "SIMULATION_ESTIMATE",
  "counts": {
    "GOOD": 127,
    "INVALID": 0,
    "OUTLIER": 0,
    "WEAK": 1
  },
  "invalid_tx_count": 0,
  "manual_gap_comparison_mm": null,
  "mean_circular_phase_agreement": 0.9999773767803003,
  "median_tof_peak_ratio": 1.0204401372745675,
  "paths": 512,
  "paths_with_clipping": 0,
  "recommended_disabled_channels": [
    7
  ],
  "valid_tx_count": 128,
  "weak_tx_count": 1
}
```

## Metrics

```json
{
  "f0_rmse_hz": 51.67872231431506,
  "f_work_hz": 40300.0,
  "lut_status": "GENERATED",
  "path_count": 512,
  "phase_rmse_deg": 0.6073452809588495,
  "pose_rms_mm": 0.0068031600074870404,
  "raw_sha256": "cc6e6b260cb82219ffd8bf2447fbfc4dc22ad52c8b2c750729bb8a92846bf1fa",
  "record_sha256": "1be42d3616a4b4aab100f03720fcfa5db17e254c68231cfccf1812c816150035",
  "rotation_error_deg": 0.01685967757967064,
  "snr_db": 35,
  "translation_error_mm": 0.020748169700379106,
  "valid_channels": 128
}
```

Per-path TOF/ADC/pose quality: path_quality.csv. Per-channel phase/f0/amplitude/health: channel_health.csv.
Phase references: SIMULATION_REFERENCE_ONLY; calibrated RX0 phase in each bank. Without real reference only per-bank relative phase is identifiable.
