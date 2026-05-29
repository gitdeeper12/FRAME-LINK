#!/bin/bash
# FRAME-LINK Package Builder

echo "=========================================="
echo "📦 Building FRAME-LINK package..."
echo "=========================================="

# Clean old builds
rm -rf dist/ build/ *.egg-info

# Build package
python -m build

echo ""
echo "=========================================="
echo "✅ Package built successfully!"
echo "📁 dist/ directory contains:"
ls -la dist/
echo "=========================================="
