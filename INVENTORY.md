# FRAME-LINK v1.0.0 - Project Inventory

## Project Metadata

| Field | Value |
|-------|-------|
| Project Name | FRAME-LINK |
| Version | 1.0.0 |
| Release Date | May 29, 2026 |
| Author | Samir Baladi |
| Email | gitdeeper@gmail.com |
| ORCID | 0009-0003-8903-0029 |
| License | MIT |
| DOI (Zenodo) | 10.5281/zenodo.20440786 |
| DOI (OSF) | 10.17605/OSF.IO/BP27A |

## Repository Links

| Platform | URL |
|----------|-----|
| GitHub | https://github.com/gitdeeper12/FRAME-LINK |
| GitLab | https://gitlab.com/gitdeeper12/FRAME-LINK |
| Bitbucket | https://bitbucket.org/gitdeeper-12/FRAME-LINK |
| Codeberg | https://codeberg.org/gitdeeper12/FRAME-LINK |
| PyPI | https://pypi.org/project/frame-link-engine |
| Zenodo | https://doi.org/10.5281/zenodo.20440786 |
| OSF Project | https://osf.io/f8hgy |
| OSF Registration | https://doi.org/10.17605/OSF.IO/BP27A |
| Internet Archive | https://archive.org/details/osf-registrations-bp27a-v1 |
| Website | https://frame-link-v1.netlify.app |

## File Statistics

| Type | Count |
|------|-------|
| Python Files | 25 |
| Configuration Files | 12 |
| Documentation Files | 8 |
| Test Files | 6 |
| HTML Files | 4 |
| Scripts | 6 |
| YAML Configs | 2 |

## Directory Structure

```

FRAME-LINK/
├── frame_link/           # Core package (25 .py files)
├── tests/                # Test files (6 .py files)
├── examples/             # Usage examples
├── docs/                 # Documentation source
├── configs/              # YAML configurations (2 files)
├── paper/                # Research paper (PDF/DOCX + figures)
├── data/                 # Data directories (raw, processed, archival)
├── logs/                 # Log files
├── scripts/              # Helper scripts (6 files)
├── Netlify/              # Web dashboard (4 HTML + assets)
└── [root files]          # README, LICENSE, CHANGELOG, etc.

```

## Python Modules Inventory

| Module | File | Lines | Description |
|--------|------|-------|-------------|
| Core | `__init__.py` | 15 | Package entry point |
| Core | `pipeline.py` | 95 | Main assessment pipeline |
| Core | `csii.py` | 45 | CSII composite index |
| SCFMM | `modules/scfmm.py` | 85 | Stress Concentration & Fracture Mechanics |
| FDARM | `modules/fdarm.py` | 105 | Fatigue Damage & Reliability |
| CSDM | `modules/csdm.py` | 70 | Connection Stiffness Degradation |
| Fracture | `fracture/paris_erdogan.py` | 45 | Paris law implementation |
| Fracture | `fracture/stress_intensity.py` | 40 | SIF computation |
| Fatigue | `fatigue/rainflow.py` | 75 | ASTM E1049-85 cycle counting |
| Fatigue | `fatigue/palmgren_miner.py` | 30 | Miner damage accumulation |
| Fatigue | `fatigue/sn_curves.py` | 40 | S-N curve database |
| Reliability | `reliability/cornell.py` | 30 | Cornell β index |
| Reliability | `reliability/hasofer_lind.py` | 50 | Hasofer-Lind FORM |
| Stiffness | `stiffness/joint_stiffness.py` | 35 | Joint stiffness measurement |
| AI Support | `ai_support/anomaly_detection.py` | 55 | Anomaly detection |
| Sensors | `sensors/strain_gauge.py` | 45 | Strain gauge processing |
| Utils | `utils/constants.py` | 40 | Material constants |

## Test Files Inventory

| File | Tests | Description |
|------|-------|-------------|
| `test_simple.py` | 6 | Basic functionality tests |
| `test_csii.py` | 6 | CSII composite index tests |
| `test_paris_erdogan.py` | 3 | Paris law tests |
| `test_rainflow.py` | 3 | Rainflow counting tests |
| `test_pipeline.py` | 3 | Pipeline integration tests |
| `test_model_validation.py` | 4 | Model validation suite |

## Configuration Files

| File | Purpose |
|------|---------|
| `pyproject.toml` | Python project configuration |
| `setup.cfg` | Setup configuration |
| `requirements.txt` | Production dependencies |
| `requirements-dev.txt` | Development dependencies |
| `.env.example` | Environment variables template |
| `.gitignore` | Git ignore rules |
| `.gitlab-ci.yml` | CI/CD pipeline |
| `.pre-commit-config.yaml` | Pre-commit hooks |
| `.readthedocs.yaml` | ReadTheDocs configuration |
| `CITATION.cff` | Citation metadata |
| `Dockerfile` | Docker container definition |
| `Makefile` | Make commands |

## Web Dashboard Files (Netlify/)

| File | Size | Description |
|------|------|-------------|
| `index.html` | 43KB | Homepage |
| `dashboard.html` | 45KB | Live dashboard |
| `results.html` | 19KB | Validation results |
| `documentation.html` | 26KB | Documentation |
| `_redirects` | 167B | Netlify redirects |

## Validation Results

| Case | Connection Type | CSII Accuracy | Crack Rate Error | Fatigue MAE |
|------|----------------|---------------|-----------------|-------------|
| V1 | Welded T-joint | ±2.9% | 4.1% | 3.3% |
| V2 | Railway bridge SHM | ±3.1% | 3.8% | 2.9% |
| V3 | Bolted splice | ±2.8% | 4.4% | 3.7% |
| **Mean** | — | **±2.93%** | **4.1%** | **3.3%** |

## Test Status

| Test Suite | Status |
|------------|--------|
| Unit Tests | ✅ 10/10 passed |
| Model Validation | ✅ 4/4 passed |
| Import Tests | ✅ All passed |

## Dependencies

### Production
- numpy >= 1.21.0
- scipy >= 1.7.0
- pandas >= 1.3.0
- matplotlib >= 3.4.0
- scikit-learn >= 1.0.0
- xgboost >= 1.5.0
- streamlit >= 1.12.0
- plotly >= 5.5.0
- pyyaml >= 5.4.0
- pydantic >= 1.9.0

### Development
- pytest >= 7.0.0
- pytest-cov >= 4.0.0
- black >= 22.0.0
- flake8 >= 5.0.0
- mypy >= 0.990
- sphinx >= 5.0.0

## Build & Deploy Commands

| Command | Purpose |
|---------|---------|
| `pip install frame-link-engine` | Install from PyPI |
| `python -m build` | Build package |
| `twine upload dist/*` | Upload to PyPI |
| `docker build -t frame-link .` | Build Docker image |
| `streamlit run frame_link/monitoring/app.py` | Run dashboard |
| `pytest tests/ -v` | Run tests |

---

*Last Updated: May 29, 2026*
*Version: 1.0.0*
*Series: CONN-SAFETY-01*
