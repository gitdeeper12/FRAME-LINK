#!/bin/bash
# FRAME-LINK Setup Script

echo "=========================================="
echo "📦 Setting up FRAME-LINK..."
echo "=========================================="

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install package in development mode
pip install -e .

# Create data directories
mkdir -p data/raw data/processed data/archival

# Copy example environment file
cp .env.example .env

echo ""
echo "=========================================="
echo "✅ Setup complete!"
echo "Run 'source venv/bin/activate' to activate environment"
echo "=========================================="
