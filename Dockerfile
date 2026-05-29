FROM python:3.11-slim-bookworm AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml setup.cfg VERSION ./
COPY requirements.txt requirements-dev.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim-bookworm

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY frame_link/ ./frame_link/
COPY simulation/ ./simulation/
COPY configs/ ./configs/
COPY README.md LICENSE VERSION ./

RUN mkdir -p /data /logs /models

ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=production

EXPOSE 8000 8501

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import frame_link; print('OK')" || exit 1

CMD ["python", "-m", "frame_link.pipeline", "--config", "configs/default.yaml"]
