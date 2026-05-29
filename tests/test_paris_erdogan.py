"""Tests for Paris-Erdogan crack propagation."""

import pytest
import numpy as np
from frame_link.fracture.paris_erdogan import ParisErdogan

class TestParisErdogan:
    """Test suite for Paris-Erdogan law."""
    
    def test_da_dn_positive(self):
        """Test crack growth rate is positive."""
        paris = ParisErdogan(C=3e-13, m=3.0)
        delta_K = 10.0
        rate = paris.da_dn(delta_K)
        assert rate > 0
    
    def test_power_law_scaling(self):
        """Test da/dN scales with (ΔK)^m."""
        paris = ParisErdogan(C=3e-13, m=3.0)
        rate1 = paris.da_dn(10.0)
        rate2 = paris.da_dn(20.0)
        # 20^3 / 10^3 = 8
        assert abs(rate2 / rate1 - 8.0) < 1e-6
    
    def test_integration(self):
        """Test crack growth integration."""
        paris = ParisErdogan(C=3e-13, m=3.0)
        result = paris.integrate(a_0=0.001, a_cr=0.025, delta_sigma=85e6, Y=1.12)
        assert result["cycles"] > 0
        assert result["final_crack"] >= 0.001
