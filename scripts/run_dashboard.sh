#!/bin/bash
# FRAME-LINK Dashboard Launcher

echo "=========================================="
echo "🚀 Starting FRAME-LINK Dashboard..."
echo "=========================================="

streamlit run frame_link/monitoring/app.py --server.port 8501
