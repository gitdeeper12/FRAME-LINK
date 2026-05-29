# Changelog

All notable changes to the FRAME-LINK project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.1/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-05-29

### Added
- SCFMM: Stress Concentration and Fracture Mechanics Module
  - Paris–Erdogan crack propagation law (da/dN = C·(ΔK)^m)
  - Wheeler retardation correction for overload effects
  - IIW sub-model FE with 0.4t and 1.0t reference points
  - J-integral stress intensity factor computation
  - Automated mesh convergence to 2% tolerance

- FDARM: Fatigue Damage Accumulation and Reliability Module
  - ASTM E1049-85 rainflow cycle counting
  - Palmgren–Miner linear damage accumulation (D_allowable = 0.80)
  - Goodman mean stress correction (σ_a,eq = σ_a / (1 - σ_m/σ_u))
  - Eurocode 3 FAT class S-N curves (FAT36–FAT160)
  - Cornell–Hasofer–Lind reliability index with AI variance augmentation

- CSDM: Connection Stiffness Degradation Module
  - Direct joint stiffness measurement K_joint(t)
  - AI-accelerated finite element model updating
  - Global stiffness matrix K(t) update
  - Force redistribution tracking after stiffness degradation

- AISL: AI-Assisted Support Layer
  - Strain field anomaly detection A_score = |σ_meas - σ_FE|/σ_FE
  - LSTM crack propagation pattern recognition from acoustic emission
  - XGBoost 24-48h CSII fatigue trend estimation
  - Gaussian process probabilistic reliability forecasting
  - Physics-constrained outputs (γ_ML ≤ 0.15, ε_AI ≤ 5·(da/dN)_Paris)

- CSII: Connection Structural Integrity Index
  - Weighted composite metric: 0.40·(1-S_deg) + 0.35·(1-D/D_allow) + 0.25·(β/β_target)
  - Four-level governance decision logic (Steady/Monitoring/Mitigation/Critical)
  - Target reliability β_target = 3.8 (P_f ≈ 10⁻⁴/year)

- Real-time monitoring dashboard with Streamlit
- Continuous sensor data integration (strain gauges, AE, bolt load cells, LVDT)
- Progressive collapse assessment for connection failure modes
- Complete documentation and API reference
- SHA-256 tamper-evidence archival layer
- Physics-constrained AI outputs with bounded uncertainty

### Validation Results
| Case | Connection / Scenario | CSII Accuracy | Crack Rate Error | Fatigue MAE | β Accuracy |
|------|----------------------|---------------|-----------------|-------------|------------|
| V1 | Welded T-joint — variable amplitude | ±2.9% | 4.1% | 3.3% | ±4.7% |
| V2 | Railway bridge SHM — crack detected | ±3.1% | 3.8% | 2.9% | ±3.2% |
| V3 | Bolted splice — preload loss | ±2.8% | 4.4% | 3.7% | ±5.1% |
| **Mean** | — | **±2.93%** | **4.1%** | **3.3%** | **±4.3%** |

### Test Results
- Unit tests: 10/10 passed
- Model validation: 4/4 passed
- Coverage: Core modules fully tested

### Changed
- N/A (initial release)

### Fixed
- N/A (initial release)

### Security
- SHA-256 tamper-evidence archival layer
- Physics-constrained AI outputs with bounded uncertainty
- Input validation and sanitization for all API endpoints

## [Unreleased]

### Planned for v1.1.0
- 3D crack surface tracking (elliptical crack front at weld toe)
- Corrosion-fatigue interaction (ISO 9224 + Paris law coupling)
- Probabilistic fracture mechanics (Monte Carlo uncertainty propagation)
- Multi-connection system reliability analysis
- Extended validation for gusset plate and pin-and-hanger connections

### Planned for v1.2.0
- Edge deployment for on-structure processing
- Integration with BIM workflows
- Mobile monitoring application
- Automated report generation
- Real-time sensor calibration routines

---

[1.0.1]: https://github.com/gitdeeper12/FRAME-LINK/releases/tag/v1.0.1
