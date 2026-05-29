"""Tests for CSII composite index."""

import pytest
from frame_link.csii import CSII

class TestCSII:
    """Test suite for CSII."""
    
    def test_steady_state(self):
        """Test steady state classification."""
        csii = CSII.compute(s_deg=0.02, d_joint=0.25, beta=4.2)
        assert csii >= 0.90
    
    def test_monitoring_phase(self):
        """Test monitoring phase."""
        csii = CSII.compute(s_deg=0.08, d_joint=0.60, beta=3.5)
        assert 0.75 <= csii < 0.90
    
    def test_mitigation_phase(self):
        """Test mitigation phase."""
        csii = CSII.compute(s_deg=0.15, d_joint=0.75, beta=2.5)
        assert 0.65 <= csii < 0.75
    
    def test_critical_breach(self):
        """Test critical breach."""
        csii = CSII.compute(s_deg=0.30, d_joint=0.95, beta=1.2)
        assert csii < 0.65
    
    def test_csii_bounds(self):
        """Test CSII stays within [0, 1] bounds."""
        csii = CSII.compute(s_deg=-0.5, d_joint=-1.0, beta=10.0)
        assert 0.0 <= csii <= 1.0
    
    def test_governance_action(self):
        """Test governance action retrieval."""
        action = CSII.get_governance_action(0.95)
        assert "Continue standard monitoring" in action
        
        action = CSII.get_governance_action(0.50)
        assert "Immediate operational shutdown" in action
