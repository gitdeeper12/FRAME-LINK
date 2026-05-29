#!/bin/bash
# FRAME-LINK Validation Script

echo "=========================================="
echo "🔬 FRAME-LINK Validation Suite"
echo "=========================================="

# Run unit tests
echo ""
echo "=== Unit Tests ==="
python -c "import sys; sys.path.insert(0, '.'); import pytest; pytest.main(['tests/', '-v'])"

# Run model validation
echo ""
echo "=== Model Validation ==="
python tests/test_model_validation.py

echo ""
echo "=========================================="
echo "✅ Validation complete!"
echo "=========================================="
