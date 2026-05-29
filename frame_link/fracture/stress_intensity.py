"""Stress intensity factor computations for connection geometries."""

import numpy as np


class StressIntensityFactor:
    """Stress intensity factor calculator for various connection geometries."""
    
    def __init__(self, geometry: str = "weld_toe"):
        self.geometry = geometry
    
    def compute(self, delta_sigma: float, a: float) -> float:
        """Compute stress intensity factor range.
        
        ΔK = Y·Δσ·√(π·a)
        """
        Y = self.get_geometry_factor(a)
        return Y * delta_sigma * np.sqrt(np.pi * a)
    
    def get_geometry_factor(self, a: float) -> float:
        """Get geometry correction factor Y(a)."""
        geometries = {
            "weld_toe": 1.12,
            "edge_crack": 1.12,
            "through_crack": 1.0,
            "hole_edge": 2.24,
            "surface_crack": 1.25
        }
        return geometries.get(self.geometry, 1.12)
    
    def critical_crack_size(self, K_Ic: float, sigma_max: float, Y: float = 1.12) -> float:
        """Compute critical crack size from fracture toughness.
        
        a_cr = (1/π)·(K_Ic/(Y·σ_max))²
        """
        return (1.0 / np.pi) * (K_Ic / (Y * sigma_max)) ** 2
