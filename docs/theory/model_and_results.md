# Acoustic reference and geometry comparison

Classification of every numerical result: **SIMULATION_ESTIMATE**.
Configuration is explicit in `config/acoustic_baseline.json`: c=343 m/s, f=40 kHz, diameter 16 mm,
pitch 18 mm, center gap 160 mm, cap radius 180 mm, no fitted atmospheric absorption. These values
are exploration inputs; no mechanical design is frozen.

The solver adds each emitter's complex pressure with spherical spreading, signed circular-piston
directivity `2 J1(ka sin(theta))/(ka sin(theta))`, front-hemisphere restriction, relative amplitude,
intrinsic phase and independently stored electronic calibration. Source phase for a target is `-2*pi*r/lambda`.
Standing-wave mode adds 180 degrees to the lower array, creating a central pressure node by symmetry;
focus mode adds constructively at the center. **Pressure at a trap node is not a useful pressure-strength maximum.**

The model ignores mutual coupling, multiple reflections, streaming, finite-size particle scattering,
measured resonance transfer functions and driver distortion. TCT40 is not an ideal baffled piston; the
approximation establishes a directional baseline and must be replaced/fitted from measurements.
No arbitrary-unit result is labeled pascals or converted into supported milligrams.

## Results at the baseline gap (quantized 8-bit focus maps)

| Total emitters | Planar central pressure, a.u. | Concave central pressure, a.u. |
|---:|---:|---:|
| 2 | 25.00 | 25.00 |
| 8 | 88.65 | 96.05 |
| 16 | 144.15 | 178.32 |
| 32 | 234.74 | 331.68 |
| 72 | 308.45 | 607.02 |
| 128 | 302.91 | 854.27 |

At these inputs the planar 72→128 expansion produces no central gain because the added wide-angle
elements have low/signed directivity contributions. The concave model gives roughly 41% gain, not
128/72 ideal scaling. This supports investigating cap geometry before adding emitters; it does not
establish the purchased TCT40 directivity or a guaranteed trap improvement.

Seed 7020, 50 trials per case, independent 15-degree RMS phase error and 10% RMS amplitude mismatch
produce a 72-channel central-pressure 5–95% interval of approximately 289.95–305.76 a.u. planar and
574.77–598.19 a.u. concave. Errors are a scenario, not measured batch statistics. See CSV for all cases.

## Trap-region and spacing proxy

`geometry_comparison.csv` evaluates 120/160/200 mm gaps with both shapes. A normalized high-contrast
Rayleigh-particle potential proxy is `U'=|p|^2 - 3/(2*k^2)*|grad p|^2`, with contrast factors assumed 1.
A finite-difference Hessian evaluates local curvature; the reported volume is the central connected region
below the minimum boundary potential of a +/-10 mm cube sampled at 1 mm. It is a coarse geometric
comparison metric, not a measured capture volume or a gravity-loaded stable region.

At 160 mm, proxy basin volume is 69 mm^3 planar versus 21 mm^3 concave, while concave central
curvature is stronger. Stronger center pressure therefore does not imply a larger useful volume.
The grid is intentionally coarse; do not use these basin numbers to dimension final mechanics.
Re-run with finer grids, measured source patterns and finite-particle scattering before physical optimization.

The small-particle radiation-force treatment is discussed in
[Bruus, Acoustofluidics 7](https://orbit.dtu.dk/en/publications/acoustofluidics-7-the-acoustic-radiation-force-on-small-particles/).
The VN1 proxy omits gravity and absolute scale and cannot be applied to a large EPS sphere as a force prediction.

## Particle assessment

The example material density is 20 kg/m^3, explicitly illustrative. A 50 mg sphere then has diameter
16.84 mm and ka≈6.17 at 40 kHz. Its weight is 0.4903 mN. This is far outside ka<<1, so the proxy
does not predict its levitation. Even 1 mg at this density is outside the conservative ka<0.3 flag.
Measured mass **and** dimensions/density must determine later finite-size modeling. The staged target remains
initial stable particle → 5 → 10 → 25 → 50 mg; none has been physically tested here.

## Outputs

- `evidence/model/vn1/emitter_scaling.csv` and `.png`: counts, geometry and mismatch sensitivity.
- `geometry_comparison.csv`: spacing, node pressure, curvature and basin proxy.
- `standing_wave_comparison.png`: x-z field sections, separately labeled color scales.
- `particle_scenarios.csv`: assumed mass/diameter/density, weight, ka and invalidity flags.
- `reference_phase_map.csv`: complete 128-row requested/calibration/mask map.
- `channel_mapping.csv`: physical IDs → RTL bits → serializer lanes → 16-channel modules.
- `assumptions.json`: numerical inputs and approximation limits.
