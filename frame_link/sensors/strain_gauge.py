"""Strain gauge data processing."""

import numpy as np


class StrainGauge:
    """Strain gauge sensor data processor."""
    
    YOUNG_MODULUS = 200e9  # Pa for steel
    
    def __init__(self, gauge_factor: float = 2.0):
        self.gauge_factor = gauge_factor
    
    def voltage_to_strain(self, voltage: np.ndarray, excitation: float = 5.0) -> np.ndarray:
        """Convert voltage reading to strain."""
        return (voltage / excitation) / self.gauge_factor
    
    def strain_to_stress(self, strain: np.ndarray) -> np.ndarray:
        """Convert strain to stress (linear elastic)."""
        return strain * self.YOUNG_MODULUS
    
    def compute_hot_spot_stress(self, strain_04t: float, strain_10t: float) -> float:
        """Compute hot-spot stress using IIW extrapolation."""
        epsilon_hotspot = strain_04t + (strain_04t - strain_10t) * 0.4 / 0.6
        return epsilon_hotspot * self.YOUNG_MODULUS
    
    def process(self, raw_data: np.ndarray) -> dict:
        """Process raw strain gauge data."""
        strain = self.voltage_to_strain(raw_data)
        stress = self.strain_to_stress(strain)
        
        return {
            "strain": strain,
            "stress": stress,
            "mean_strain": float(np.mean(strain)),
            "max_strain": float(np.max(strain)),
            "min_strain": float(np.min(strain)),
            "strain_range": float(np.ptp(strain))
        }
