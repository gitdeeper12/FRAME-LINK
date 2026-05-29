#!/bin/bash
# FRAME-LINK Test Runner

echo "=========================================="
echo "🧪 Running FRAME-LINK tests..."
echo "=========================================="

# Run pytest with coverage
pytest tests/ -v --cov=frame_link --cov-report=term --cov-report=html

echo ""
echo "=========================================="
echo "✅ Tests complete!"
echo "📊 Coverage report: htmlcov/index.html"
echo "=========================================="
