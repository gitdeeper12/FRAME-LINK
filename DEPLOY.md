# FRAME-LINK Deployment Guide

## Prerequisites

- Python 3.9 or higher
- Git
- Docker (optional)

## Local Deployment

### 1. Clone the repository
```bash
git clone https://github.com/gitdeeper12/FRAME-LINK.git
cd FRAME-LINK
```

2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

4. Configure environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run the pipeline

```bash
python -m frame_link.pipeline --config configs/default.yaml
```

6. Launch dashboard

```bash
streamlit run frame_link/monitoring/app.py
```

Docker Deployment

Build image

```bash
docker build -t frame-link:latest .
```

Run container

```bash
docker run -p 8000:8000 -p 8501:8501 frame-link:latest
```

PyPI Package

Install from PyPI

```bash
pip install frame-link-engine
```

Build and publish

```bash
python -m build
twine upload dist/*
```

CI/CD Pipeline

The project uses GitLab CI/CD for automated testing and deployment.
See .gitlab-ci.yml for configuration.

Monitoring Dashboard

Access the dashboard at: https://frame-link.netlify.app/dashboard
