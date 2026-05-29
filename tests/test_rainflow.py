"""Tests for rainflow cycle counting."""

import pytest
import numpy as np
from frame_link.fatigue.rainflow import RainflowCounter

class TestRainflow:
    """Test suite for rainflow cycle counting."""
    
    def setup_method(self):
        self.counter = RainflowCounter()
    
    def test_constant_amplitude(self):
        """Test constant amplitude sinusoid."""
        t = np.linspace(0, 10, 1000)
        stress = 100e6 * np.sin(2 * np.pi * t)
        cycles = self.counter.count(stress)
        assert len(cycles) > 0
    
    def test_empty_input(self):
        """Test empty input handling."""
        cycles = self.counter.count(np.array([]))
        assert cycles == []
    
    def test_single_point(self):
        """Test single point input."""
        cycles = self.counter.count(np.array([100]))
        assert cycles == []
