<div align="center">

# FRAME-LINK

### Fatigue Reliability Assessment and Monitoring Extension for Structural Connection Integrity under Cyclic and Dynamic Loading

**Structural Connection Mechanics · Welded and Riveted Joint Fatigue · Crack Propagation Mechanics · AI-Assisted Reliability Support**

---

[![PyPI version](https://img.shields.io/pypi/v/frame-link-engine?color=2C1A2E&label=PyPI&logo=pypi&logoColor=white)](https://pypi.org/project/frame-link-engine)
[![PyPI downloads](https://img.shields.io/pypi/dm/frame-link-engine?color=4A235A&label=Downloads&logo=pypi&logoColor=white)](https://pypi.org/project/frame-link-engine/#files)
[![Python versions](https://img.shields.io/pypi/pyversions/frame-link-engine?color=306998&logo=python&logoColor=white)](https://pypi.org/project/frame-link-engine)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20440786-blue.svg)](https://doi.org/10.5281/zenodo.20440786)
[![OSF Preregistration](https://img.shields.io/badge/OSF-Preregistered-blue?logo=osf&logoColor=white)](https://doi.org/10.17605/OSF.IO/BP27A)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0003-8903-0029)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Domain](https://img.shields.io/badge/Domain-Structural%20Connection%20Integrity-2C1A2E)](https://doi.org/10.5281/zenodo.20440786)
[![Series](https://img.shields.io/badge/Series-CONN--SAFETY--01-7D3C98)](https://doi.org/10.5281/zenodo.20440786)
[![Version](https://img.shields.io/badge/Version-1.0.1-orange)](https://github.com/gitdeeper12/FRAME-LINK)

</div>

---

## 📌 Overview

**FRAME-LINK** is a structural engineering framework for the analysis, monitoring, and safety governance of welded and riveted connection systems — including welded T-joints, gusset plate attachments, bolted splices, pin-and-hanger assemblies, and cruciform connections — grounded in classical fracture mechanics, fatigue reliability engineering, and connection stiffness mechanics, with an AI-assisted computational support layer operating under strict physics-based constraints.

> *"A structural connection is not merely a component of a larger structural system — it is frequently the governing link in the reliability chain, the element whose failure most directly produces overall structural loss of function. FRAME-LINK treats each individual connection as the subject of its own specific fatigue assessment, combining classical fracture mechanics with direct measurement, sensor-based monitoring, and AI-assisted trend estimation to provide continuous, quantitative safety governance."*

Conventional periodic NDT inspection of structural connections cannot detect dynamic crack propagation patterns between inspections, assess fatigue damage accumulation under variable amplitude loading histories, or evaluate the connection reliability index under the specific loading conditions of the next extreme event. FRAME-LINK provides a continuous, quantitative, three-module analytical framework that classifies connection condition in real time as:

| Signal | Safety Status | Action |
|---|---|---|
| 🟢 **STEADY ELASTIC STATE** | `CSII ≥ 0.90` | Connection response within elastic design bounds — standard monitoring, no intervention |
| 🟠 **ANOMALY DETECTED L1** | `0.75 ≤ CSII < 0.90` | Onset of measurable stiffness change or fatigue growth — targeted NDT inspection |
| 🟠 **DEGRADATION WARNING L2** | `0.65 ≤ CSII < 0.75` | Critical stiffness reduction or accelerating damage — immediate load restriction |
| 🔴 **CRITICAL CONNECTION FAILURE** | `CSII < 0.65` | Safety threshold breached — operational shutdown; emergency structural assessment |

---

## 🗂️ Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [FRAME-LINK Pipeline](#-frame-link-pipeline)
- [Governing Equations](#-governing-equations)
- [Scoring & Safety Bounds](#-scoring--safety-bounds)
- [Platforms & Mirrors](#-platforms--mirrors)
- [Clone & Download](#-clone--download)
- [Citation](#-citation)
- [License](#-license)
- [Author](#-author)

---

## ✨ Key Features

- **Three-module coupled assessment pipeline** — SCFMM (Stress Concentration and Fracture Mechanics Module), FDARM (Fatigue Damage Accumulation and Reliability Module), CSDM (Connection Stiffness Degradation Module)
- **Connection Structural Integrity Index (CSII)** — weighted composite safety metric with four-level governance decision logic
- **Paris–Erdogan crack propagation law** — `da/dN = C · (ΔK)^m` with Wheeler retardation correction for overload effects
- **IIW hot-spot stress extrapolation** — sub-model FE approach with 0.4t and 1.0t reference points for weld toe stress resolution
- **ASTM E1049-85 rainflow cycle counting** — variable amplitude stress history decomposition + Goodman mean stress correction
- **Cornell–Hasofer–Lind reliability index (β)** — target β = 3.8 (P_f ≈ 10⁻⁴/year) with continuous D_joint monitoring
- **Connection stiffness model updating** — direct joint stiffness measurement + AI-accelerated global stiffness matrix updating
- **Three-time-scale monitoring architecture** — 1s anomaly detection, 1h damage update, 24h model update + 48h forecast
- **±2.9% CSII accuracy** — validated against controlled fatigue tests and field SHM campaign data
- **Full open-source distribution** — available across 11 platforms

---

## 📁 Project Structure

```
FRAME-LINK/
│
├── frame_link/                             # Core Python package
│   ├── __init__.py                         # Package entry point & public API
│   ├── pipeline.py                         # Main FRAME-LINK assessment pipeline
│   ├── csii.py                             # CSII composite index & governance logic
│   │
│   ├── modules/                            # Three analytical modules
│   │   ├── __init__.py
│   │   ├── scfmm.py                        # Module 1: Stress Concentration & Fracture Mechanics Module
│   │   ├── fdarm.py                        # Module 2: Fatigue Damage Accumulation & Reliability Module
│   │   └── csdm.py                         # Module 3: Connection Stiffness Degradation Module
│   │
│   ├── fracture/                           # Fracture mechanics subsystem
│   │   ├── __init__.py
│   │   ├── paris_erdogan.py                # Paris law: da/dN = C · (ΔK)^m
│   │   ├── stress_intensity.py             # SIF: ΔK = Y · Δσ · √(π·a)
│   │   ├── wheeler_retardation.py          # Wheeler overload retardation model
│   │   ├── kirsch_solution.py              # Kirsch stress field around holes
│   │   ├── scf_computation.py             # Stress concentration factor K_t
│   │   ├── sub_model_fe.py                 # IIW sub-model FE with mesh refinement
│   │   ├── hot_spot_stress.py              # 0.4t and 1.0t IIW reference extrapolation
│   │   └── fracture_toughness.py           # K_Ic brittle fracture limit assessment
│   │
│   ├── fatigue/                            # Fatigue accumulation subsystem
│   │   ├── __init__.py
│   │   ├── rainflow.py                     # ASTM E1049-85 rainflow cycle counting
│   │   ├── palmgren_miner.py               # D(t) = Σ n_i / N_i ≤ D_allowable
│   │   ├── sn_curves.py                    # Eurocode 3 / AISC / BS 7608 S-N database
│   │   ├── goodman.py                      # Goodman mean stress correction σ_a,eq
│   │   ├── detail_categories.py            # FAT class detail category registry
│   │   └── damage_map.py                   # Spatial damage distribution D(x,t)
│   │
│   ├── reliability/                        # Structural reliability analysis
│   │   ├── __init__.py
│   │   ├── cornell.py                      # Cornell reliability index β computation
│   │   ├── hasofer_lind.py                 # Hasofer–Lind FORM invariant β
│   │   ├── failure_probability.py          # P_f = Φ(−β) mapping
│   │   ├── limit_state.py                  # Limit state g(X) = R − S
│   │   └── monte_carlo.py                  # Monte Carlo P_f verification
│   │
│   ├── stiffness/                          # Connection stiffness degradation subsystem
│   │   ├── __init__.py
│   │   ├── joint_stiffness.py              # Direct joint stiffness measurement K_joint(t)
│   │   ├── model_updating.py               # FE model updating from measured response
│   │   ├── degradation_index.py            # S_deg,joint = 1 − K_joint(t)/K_joint,0
│   │   ├── force_redistribution.py         # Global stiffness matrix K(t) update
│   │   └── capacity_tracker.py             # Member force demand vs fatigue capacity
│   │
│   ├── connection_types/                   # Connection-type specific models
│   │   ├── __init__.py
│   │   ├── welded_joint.py                 # Weld toe stress concentration + residual stress
│   │   ├── bolted_splice.py                # Bolt preload relaxation + fretting fatigue
│   │   ├── gusset_plate.py                 # Re-entrant corner SCF + secondary bending
│   │   ├── pin_hanger.py                   # Pin-and-hanger stress corrosion + fretting
│   │   └── riveted_joint.py                # Rivet hole edge fatigue + bearing stress
│   │
│   ├── ai_support/                         # AI-assisted support layer (bounded)
│   │   ├── __init__.py
│   │   ├── anomaly_detection.py            # Strain field anomaly score A_score
│   │   ├── lstm_crack_growth.py            # LSTM crack propagation pattern recognition
│   │   ├── xgboost_fatigue.py              # XGBoost 24-48h fatigue trend estimation
│   │   ├── gaussian_process.py             # GP probabilistic reliability forecasting
│   │   ├── acoustic_emission.py            # AE b-value crack propagation detection
│   │   ├── physics_bounds.py               # Physics-based constraint enforcement
│   │   └── uncertainty.py                  # AI prediction uncertainty quantification
│   │
│   ├── sensors/                            # Sensor integration and data fusion
│   │   ├── __init__.py
│   │   ├── strain_gauge.py                 # IIW rosette strain gauge processing
│   │   ├── acoustic_emission.py            # AE transducer signal processing
│   │   ├── bolt_load_cell.py               # Bolt preload measurement and tracking
│   │   ├── clip_gauge.py                   # LVDT / clip gauge joint stiffness input
│   │   ├── accelerometer.py                # MEMS biaxial dynamic stress contribution
│   │   └── fusion.py                       # Multi-sensor data fusion and QC
│   │
│   ├── degradation/                        # Material and environmental degradation
│   │   ├── __init__.py
│   │   ├── corrosion.py                    # ISO 9224 corrosion rate at connection zone
│   │   ├── remaining_life.py               # T_rem = (a_cr − a_0) / (da/dN · f_cycles)
│   │   ├── capacity_reduction.py           # R(t) = R₀ · (1 − D_corr − D_fatigue)
│   │   └── chaboche.py                     # Chaboche continuum damage mechanics
│   │
│   └── utils/                              # Shared utilities
│       ├── __init__.py
│       ├── metrics.py                      # CSII, β, D_joint, S_deg computation
│       ├── validators.py                   # Input validation and safety bounds
│       └── constants.py                    # Material constants C, m, K_Ic, FAT classes
│
├── monitoring/                             # Real-time monitoring dashboard
│   ├── __init__.py
│   ├── app.py                              # Streamlit application entry point
│   ├── dashboard.py                        # CSII governance dashboard layout
│   ├── crack_growth_plot.py                # Paris law crack propagation display
│   ├── damage_map.py                       # Spatial fatigue damage map renderer
│   ├── stiffness_trend.py                  # Connection stiffness degradation trend
│   └── components/
│       ├── csii_gauge.py                   # CSII composite index gauge display
│       ├── signal_panel.py                 # 🔴🟠🟢 governance signal status
│       └── reliability_forecast.py         # 48h β index trajectory projection
│
├── archival/                               # Operational data archival
│   ├── __init__.py
│   ├── writer.py                           # Append-only JSON/CSV record writer
│   ├── checksum.py                         # SHA-256 tamper-evidence layer
│   └── partitioner.py                      # Per-module time-window CSV partitioner
│
├── simulation/                             # Validation and benchmark environment
│   ├── __init__.py
│   ├── connection_configs.py               # Connection geometry and material definitions
│   ├── loading_scenarios.py                # Variable amplitude fatigue spectra
│   ├── benchmarks.py                       # Three-case validation suite
│   ├── parameters.py                       # Canonical v1.0.1 parameter registry
│   └── results/                            # Pre-computed validation outputs
│       ├── V1_welded_T_joint_variable_amplitude.json
│       ├── V2_railway_bridge_shm_campaign.json
│       └── V3_bolted_splice_preload_loss.json
│
├── examples/                               # Usage examples and tutorials
│   ├── quickstart.py                       # Minimal working example
│   ├── basic_csii.ipynb                    # Jupyter: single-connection CSII assessment
│   ├── crack_propagation.ipynb             # Jupyter: Paris–Erdogan walkthrough
│   ├── rainflow_counting.ipynb             # Jupyter: ASTM E1049-85 cycle counting
│   ├── reliability_index.ipynb             # Jupyter: Cornell–Hasofer–Lind β computation
│   ├── streamlit_dashboard.py              # Launch real-time monitoring dashboard
│   └── remaining_life_prediction.py        # Remaining life forecast demo
│
├── tests/                                  # Unit and integration tests
│   ├── test_scfmm.py
│   ├── test_fdarm.py
│   ├── test_csdm.py
│   ├── test_csii.py
│   ├── test_rainflow.py
│   ├── test_paris_erdogan.py
│   ├── test_reliability.py
│   └── test_pipeline.py
│
├── docs/                                   # Documentation source
│   ├── architecture.md                     # Module architecture reference
│   ├── mathematics.md                      # Governing equations documentation
│   ├── monitoring.md                       # Sensor system and data fusion guide
│   ├── governance.md                       # CSII threshold calibration reference
│   └── api_reference.md                    # Full Python API reference
│
├── paper/                                  # Research paper artifacts
│   ├── FRAME-LINK_Research_Paper.pdf       # Published paper (PDF)
│   ├── FRAME-LINK_Research_Paper.docx      # Editable Word version
│   └── figures/
│       ├── csii_formulation.svg
│       ├── paris_law_crack_growth.svg
│       ├── fatigue_damage_map.svg
│       └── scf_hot_spot_stress.svg
│
├── .gitlab-ci.yml                          # GitLab CI/CD pipeline
├── .github/
│   └── workflows/
│       ├── tests.yml
│       └── publish.yml
├── pyproject.toml
├── setup.cfg
├── requirements.txt
├── requirements-dev.txt
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── AUTHORS.md
├── LICENSE
└── README.md                               # This file
```

---

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI
pip install frame-link-engine

# Install from source
git clone https://github.com/gitdeeper12/FRAME-LINK.git
cd FRAME-LINK
pip install -e .
```

### Minimal Example

```python
from frame_link import FrameLinkAssessor

# Initialize assessor with connection configuration
assessor = FrameLinkAssessor(
    connection_config="configs/welded_T_joint.yaml",
    sensor_stream="live"   # or path to historical CSV
)

# Run full FRAME-LINK assessment pipeline
result = assessor.evaluate()

print(result.csii)               # Connection Structural Integrity Index ∈ [0, 1]
print(result.signal)             # "STEADY_ELASTIC" | "ANOMALY_L1" | "DEGRADATION_L2" | "CRITICAL"
print(result.beta)               # Cornell–Hasofer–Lind reliability index β
print(result.d_joint)            # Current Palmgren–Miner damage D_joint
print(result.s_deg)              # Connection stiffness degradation index S_deg,joint
print(result.crack_depth)        # Current estimated crack depth a (mm)
print(result.da_dn)              # Paris law crack propagation rate da/dN
```

### With Full Three-Module Configuration

```python
from frame_link import FrameLinkAssessor
from frame_link.modules import SCFMM, FDARM, CSDM

assessor = FrameLinkAssessor(
    connection_config="configs/welded_T_joint.yaml",
    modules={
        "scfmm": SCFMM(fat_class="FAT71", K_t_method="FE", mesh_convergence=0.02),
        "fdarm": FDARM(d_allowable=0.80, beta_target=3.8, sn_code="EC3"),
        "csdm":  CSDM(stiffness_warn=0.10, ai_accelerated=True),
    }
)

result = assessor.evaluate()
print(result.breakdown)
# {"scfmm": 0.91, "fdarm": 0.87, "csdm": 0.94}
```

### Paris–Erdogan Crack Growth Assessment

```python
from frame_link.fracture import ParisErdogan, WheelerRetardation, StressIntensityFactor

# Define connection geometry and material constants
sif = StressIntensityFactor(Y=1.12, geometry="weld_toe")
paris = ParisErdogan(C=3e-13, m=3.0)
wheeler = WheelerRetardation(p=2.0)

# Compute crack propagation under variable amplitude loading
a_0 = 0.001          # Initial crack depth 1 mm
a_cr = 0.025         # Critical crack depth (fracture toughness limit)

result = paris.integrate(
    a_0=a_0, a_cr=a_cr,
    delta_sigma=85.0,   # MPa
    sif=sif,
    retardation=wheeler
)

print(f"Remaining cycles to failure: {result.N_remaining:,.0f}")
print(f"Estimated remaining life: {result.life_hours:.1f} h")
```

### Fatigue Damage Accumulation

```python
from frame_link.fatigue import RainflowCounter, PalmgrenMiner, SNcurve

# Load strain time series from instrumented connection detail
strain_ts = load_csv("sensors/weld_toe_strain.csv")

counter = RainflowCounter()
cycles = counter.count(strain_ts)           # ASTM E1049-85 rainflow

sn = SNcurve(fat_class=71, m=3, code="EC3")  # Eurocode 3 FAT71
miner = PalmgrenMiner(sn_curve=sn, goodman_correction=True)
D = miner.accumulate(cycles)               # D(t) = Σ n_i / N_i

print(f"Fatigue damage: {D:.4f} (warning: 0.80, failure: 1.00)")
```

### Launch Real-Time Monitoring Dashboard

```bash
# Start Streamlit CSII governance dashboard
streamlit run examples/streamlit_dashboard.py

# Dashboard at: http://localhost:8501
# Panels:
#   · CSII composite gauge with 4-level signal
#   · Paris law crack growth trend
#   · Fatigue damage map (spatial connection display)
#   · Connection stiffness degradation trend
#   · 48h β reliability index trajectory forecast
```

---

## 🧩 FRAME-LINK Pipeline

```
┌────────────────────────────────────────────────────────────────────────────┐
│  Sensor Input: Strain Gauges · AE Transducers · Bolt Load Cells · LVDT    │
└──────────────────────────┬─────────────────────────────────────────────────┘
                           │
           ┌───────────────┼──────────────────┐
           │               │                  │
           ▼               ▼                  ▼
        SCFMM           FDARM              CSDM
        IIW Sub-model   Rainflow           Direct stiffness
        FE hot-spot     ASTM E1049-85      K_joint(t) measurement
        Paris–Erdogan   Palmgren–Miner     Model updating
        ΔK = Y·Δσ·√πa  D(t) = Σn_i/N_i   S_deg = 1−K/K₀
        Wheeler retard. Cornell β index    Force redistribution
           │               │                  │
           └───────────────┼──────────────────┘
                           │
                AI-Assisted Support Layer
                Anomaly detection A_score (1s)
                LSTM crack pattern recognition
                XGBoost 24–48h fatigue trend
                GP probabilistic β forecast
                Physics-bounded outputs only
                           │
                           ▼
          Connection Structural Integrity Index
          CSII = 0.40·(1−S_deg) + 0.35·(1−D/D_allow)
                     + 0.25·(β_joint/β_target)
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
           Safety Signal       Archival
           🟢🟠🔴             JSON/CSV + SHA-256
           4-level CSII       Streamlit dashboard
```

### Module Summary

| # | Module | Governing Output | Core Method |
|---|--------|-----------------|-------------|
| 1 | **SCFMM** | `ΔK(t), da/dN(t), K_t` | Paris–Erdogan + IIW hot-spot FE sub-model |
| 2 | **FDARM** | `D_joint(t), β(t), P_f` | Rainflow + Palmgren–Miner + Cornell–Hasofer–Lind |
| 3 | **CSDM** | `S_deg,joint(t), K_joint(t)` | Direct stiffness measurement + FE model updating |
| — | **AISL** | `CSII_forecast(t+48h)` | LSTM + XGBoost + GP (physics-constrained) |
| — | **CSII** | `CSII(t) ∈ [0,1]` | Weighted composite of all three modules |

---

## ⚙️ Governing Equations

```
Eq. 1 — Stress Intensity Factor Range:
  ΔK = Y · Δσ · √(π · a)

Eq. 2 — Paris–Erdogan Crack Propagation Law:
  da/dN = C · (ΔK)^m   [C ≈ 3×10⁻¹³, m ≈ 3.0 for structural steel]

Eq. 3 — Wheeler Retardation Correction:
  (da/dN)_eff = φ_W · C · (ΔK)^m

Eq. 4 — Fatigue Damage Accumulation (Palmgren–Miner):
  D_joint(t) = Σᵢ [ nᵢ(t) / Nᵢ(Δσᵢ) ] ≤ D_allowable = 0.80

Eq. 5 — Cornell Reliability Index:
  β = (μ_R − μ_S) / √(σ_R² + σ_S² + σ_AI²)   →   P_f = Φ(−β)

Eq. 6 — Connection Structural Integrity Index:
  CSII = 0.40 · (1 − S_deg,joint) + 0.35 · (1 − D_joint / D_allowable)
             + 0.25 · (β_joint / β_target)
```

---

## 📊 Scoring & Safety Bounds

```
CSII governance certification thresholds:
  CSII ≥ 0.90   →   🟢 Steady Elastic State
  0.75 ≤ CSII < 0.90   →   🟠 Anomaly Detected Level 1
  0.65 ≤ CSII < 0.75   →   🟠 Degradation Warning Level 2
  CSII < 0.65   →   🔴 Critical Connection Failure

Additional safety bounds:
  β (reliability index)    ≥  3.80   (target P_f ≈ 10⁻⁴/year)
  D_joint (Miner damage)   <  0.80   (D_allowable warning threshold)
  S_deg,joint              <  0.10   (10% stiffness degradation warning)
  a_current (crack depth)  <  0.60 · a_cr   (60% of fracture toughness limit)
  A_score (anomaly)        <  3.0    (3σ strain anomaly threshold)
```

**Validation results (FRAME-LINK v1.0.1):**

| Case | Connection / Scenario | CSII Accuracy | Crack Rate Error | Fatigue MAE | β Accuracy |
|---|---|---|---|---|---|
| V1 | Welded T-joint — variable amplitude traffic | ±2.9% | 4.1% | 3.3% | ±4.7% |
| V2 | Railway bridge SHM — crack initiation detected | ±3.1% | 3.8% | 2.9% | ±3.2% |
| V3 | Bolted splice — progressive preload loss | ±2.8% | 4.4% | 3.7% | ±5.1% |
| **Mean** | — | **±2.93%** | **4.1%** | **3.3%** | **±4.3%** |

---

## 🌐 Platforms & Mirrors

| Platform | URL | Role |
|---|---|---|
| 🐙 **GitHub** (Primary) | [github.com/gitdeeper12/FRAME-LINK](https://github.com/gitdeeper12/FRAME-LINK) | Source code, issues, PRs |
| 🦊 **GitLab** (Mirror) | [gitlab.com/gitdeeper12/FRAME-LINK](https://gitlab.com/gitdeeper12/FRAME-LINK) | CI/CD mirror |
| 🪣 **Bitbucket** (Mirror) | [bitbucket.org/gitdeeper-12/FRAME-LINK](https://bitbucket.org/gitdeeper-12/FRAME-LINK) | Enterprise mirror |
| 🏔️ **Codeberg** (Mirror) | [codeberg.org/gitdeeper12/FRAME-LINK](https://codeberg.org/gitdeeper12/FRAME-LINK) | Open-source community |
| 📦 **PyPI** | [pypi.org/project/frame-link-engine](https://pypi.org/project/frame-link-engine) | Python package distribution |
| 🔬 **Zenodo** | [doi.org/10.5281/zenodo.20440786](https://doi.org/10.5281/zenodo.20440786) | Citable DOI, paper & data |
| 📋 **OSF Project** | [osf.io/framelink](https://osf.io/f8hgy) | Research project registry |
| 📝 **OSF Preregistration** | [doi.org/10.17605/OSF.IO/BP27A](https://doi.org/10.17605/OSF.IO/BP27A) | Pre-registered study protocol |
| 🌐 **Website** | [frame-link.netlify.app](https://frame-link-v1.netlify.app) | Live documentation & dashboard |
| 🧑‍🔬 **ORCID** | [orcid.org/0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029) | Researcher identity |
| 🗄️ **Internet Archive** | [archive.org/details/osf-registrations-bp27a-v1](https://archive.org/details/osf-registrations-bp27a-v1) | Permanent archival copy |

### 🌐 Official Website Pages

| Page | URL |
|---|---|
| Homepage | [frame-link.netlify.app](https://frame-link-v1.netlify.app) |
| Dashboard | [frame-link.netlify.app/dashboard](https://frame-link-v1.netlify.app/dashboard) |
| Results | [frame-link.netlify.app/results](https://frame-link-v1.netlify.app/results) |
| Documentation | [frame-link.netlify.app/documentation](https://frame-link-v1.netlify.app/documentation) |

---

## 🔄 Clone & Download

### Git Clone

```bash
# GitHub (Primary)
git clone https://github.com/gitdeeper12/FRAME-LINK.git

# GitLab (Mirror)
git clone https://gitlab.com/gitdeeper12/FRAME-LINK.git

# Bitbucket (Mirror)
git clone https://bitbucket.org/gitdeeper-12/FRAME-LINK.git

# Codeberg (Mirror)
git clone https://codeberg.org/gitdeeper12/FRAME-LINK.git
```

### Direct ZIP Download

| Source | Link |
|---|---|
| GitHub | [FRAME-LINK-main.zip](https://github.com/gitdeeper12/FRAME-LINK/archive/refs/heads/main.zip) |
| GitLab | [FRAME-LINK-main.zip](https://gitlab.com/gitdeeper12/FRAME-LINK/-/archive/main/FRAME-LINK-main.zip) |
| Bitbucket | [FRAME-LINK-main.zip](https://bitbucket.org/gitdeeper-12/FRAME-LINK/get/main.zip) |
| Codeberg | [FRAME-LINK-main.zip](https://codeberg.org/gitdeeper12/FRAME-LINK/archive/main.zip) |
| PyPI files | [pypi.org/project/frame-link-engine/#files](https://pypi.org/project/frame-link-engine/#files) |
| Zenodo record | [doi.org/10.5281/zenodo.20440786](https://doi.org/10.5281/zenodo.20440786) |

---

## 📖 Citation

If FRAME-LINK contributes to your research, please cite using one of the following formats.

### 📦 PyPI Package

```bibtex
@software{baladi2026framelink_pypi,
  author       = {Baladi, Samir},
  title        = {{FRAME-LINK}: Fatigue Reliability Assessment and Monitoring
                  Extension for Structural Connection Integrity under
                  Cyclic and Dynamic Loading},
  year         = {2026},
  version      = {1.0.1},
  publisher    = {Python Package Index},
  url          = {https://pypi.org/project/frame-link-engine},
  note         = {Python package, MIT License, Series CONN-SAFETY-01}
}
```

### 🔬 Zenodo Archive (Paper & Data)

```bibtex
@dataset{baladi2026framelink_zenodo,
  author       = {Baladi, Samir},
  title        = {{FRAME-LINK}: Fatigue Reliability Assessment and Monitoring
                  Extension for Structural Connection Integrity under
                  Cyclic and Dynamic Loading —
                  Research Paper and Simulation Data},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {1.0.1},
  doi          = {10.5281/zenodo.20440786},
  url          = {https://doi.org/10.5281/zenodo.20440786},
  note         = {Structural Connection Integrity · CONN-SAFETY-01}
}
```

### 📝 OSF Preregistration

```bibtex
@misc{baladi2026framelink_osf,
  author       = {Baladi, Samir},
  title        = {{FRAME-LINK} Framework: Pre-registered Study Protocol for
                  Fatigue Reliability Assessment and Monitoring of Structural
                  Connection Integrity under Cyclic and Dynamic Loading},
  year         = {2026},
  publisher    = {Open Science Framework},
  doi          = {10.17605/OSF.IO/BP27A},
  url          = {https://doi.org/10.17605/OSF.IO/BP27A},
  note         = {OSF Preregistration}
}
```

### 📄 Research Paper

```bibtex
@article{baladi2026framelink,
  author       = {Baladi, Samir},
  title        = {{FRAME-LINK}: Fatigue Reliability Assessment and Monitoring
                  Extension for Structural Connection Integrity under
                  Cyclic and Dynamic Loading},
  year         = {2026},
  month        = {May},
  version      = {1.0.1},
  doi          = {10.5281/zenodo.20440786},
  url          = {https://doi.org/10.5281/zenodo.20440786},
  note         = {Ronin Institute / Rite of Renaissance,
                  Series CONN-SAFETY-01}
}
```

### APA (inline)

> Baladi, S. (2026). *FRAME-LINK: Fatigue Reliability Assessment and Monitoring Extension for Structural Connection Integrity under Cyclic and Dynamic Loading* (Version 1.0.1, Series CONN-SAFETY-01). Zenodo. https://doi.org/10.5281/zenodo.20440786

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Samir Baladi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
```

---

## 👤 Author

**Samir Baladi**
Interdisciplinary Researcher — Structural Reliability Engineering, Fatigue Mechanics & Computational Safety Analysis
Ronin Institute / Rite of Renaissance

| Contact | Link |
|---|---|
| 📧 Email | [gitdeeper@gmail.com](mailto:gitdeeper@gmail.com) |
| 🧑‍🔬 ORCID | [0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029) |
| 🐙 GitHub | [github.com/gitdeeper12](https://github.com/gitdeeper12) |
| 🔬 Zenodo | [doi.org/10.5281/zenodo.20440786](https://doi.org/10.5281/zenodo.20440786) |

---

<div align="center">

**CONN-SAFETY-01 · Version 1.0.1 · May 2026**

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20440786-blue.svg)](https://doi.org/10.5281/zenodo.20440786)
[![PyPI](https://img.shields.io/pypi/v/frame-link-engine?color=2C1A2E)](https://pypi.org/project/frame-link-engine)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Domain](https://img.shields.io/badge/Domain-Structural%20Connection%20Integrity-2C1A2E)](https://doi.org/10.5281/zenodo.20440786)

*"A structural connection is not merely a component — it is the governing link in the reliability chain. FRAME-LINK treats each connection as the subject of its own specific fatigue assessment, providing continuous, quantitative safety governance at the detail level where structural failures originate."*

</div>
