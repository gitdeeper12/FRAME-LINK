"""Tests for main FRAME-LINK pipeline."""

import pytest
from frame_link.pipeline import FrameLinkAssessor

class TestPipeline:
    """Test suite for FrameLinkAssessor."""
    
    def setup_method(self):
        self.assessor = FrameLinkAssessor()
    
    def test_evaluate_returns_result(self):
        """Test evaluate method returns result."""
        result = self.assessor.evaluate()
        
        assert hasattr(result, 'csii')
        assert hasattr(result, 'signal')
        assert hasattr(result, 'beta')
        assert hasattr(result, 'd_joint')
        assert hasattr(result, 's_deg')
        assert hasattr(result, 'crack_depth')
        assert hasattr(result, 'da_dn')
        assert hasattr(result, 'a_score')
    
    def test_csii_in_bounds(self):
        """Test CSII is within bounds."""
        result = self.assessor.evaluate()
        assert 0.0 <= result.csii <= 1.0
    
    def test_signal_is_valid(self):
        """Test signal is valid."""
        result = self.assessor.evaluate()
        valid_signals = ["🟢 STEADY_ELASTIC_STATE", "🟠 ANOMALY_DETECTED_L1", 
                        "🟠 DEGRADATION_WARNING_L2", "🔴 CRITICAL_CONNECTION_FAILURE"]
        assert result.signal in valid_signals
