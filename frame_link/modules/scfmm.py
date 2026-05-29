"""Stress Concentration and Fracture Mechanics Module (SCFMM).

Paris-Erdogan crack propagation law: da/dN = C·(ΔK)^m
Stress intensity factor: ΔK = Y·Δσ·√(π·a)
"""

import numpy as np


class SCFMM:
    """Stress Concentration and Fracture Mechanics Module."""
    
    def __init__(self, C: float = 3e-13, m: float = 3.0, Y: float = 1.12):
        self.C = C  # Paris law constant
        self.m = m  # Paris law exponent
        self.Y = Y  # Geometry correction factor
    
    def compute_stress_intensity_factor(self, delta_sigma: float, a: float) -> float:
        """Compute stress intensity factor range.
        
        ΔK = Y · Δσ · √(π·a)
        """
        return self.Y * delta_sigma * np.sqrt(np.pi * a)
    
    def paris_law(self, delta_K: float) -> float:
        """Compute crack propagation rate.
        
        da/dN = C · (ΔK)^m
        """
        return self.C * (delta_K ** self.m)
    
    def integrate_crack_growth(self, a_0: float, a_cr: float, delta_sigma: float) -> dict:
        """Integrate Paris law to compute cycles to failure."""
        a = a_0
        cycles = 0
        da_history = []
        a_history = [a]
        
        while a < a_cr and cycles < 1e7:
            delta_K = self.compute_stress_intensity_factor(delta_sigma, a)
            da = self.paris_law(delta_K)
            if da <= 0:
                break
            cycles += 1
            a += da
            a_history.append(a)
            da_history.append(da)
        
        return {
            "crack_depth": a,
            "da_dn": da,
            "cycles_to_failure": cycles,
            "crack_history": a_history,
            "da_history": da_history
        }
    
    def compute_critical_crack_size(self, K_Ic: float, sigma_max: float) -> float:
        """Compute critical crack size from fracture toughness.
        
        a_cr = (1/π) · (K_Ic / (Y·σ_max))²
        """
        return (1.0 / np.pi) * (K_Ic / (self.Y * sigma_max)) ** 2
    
    def wheeler_retardation(self, da_dn: float, a: float, a_ol: float, r_p_ol: float, beta: float = 2.0) -> float:
        """Apply Wheeler retardation correction after overload."""
        phi_w = (r_p_ol / (a_ol + r_p_ol - a)) ** beta
        return da_dn * max(phi_w, 0.1)
    
    def compute(self) -> dict:
        """Run SCFMM analysis."""
        # Simulated values
        a_0 = 0.001  # Initial crack depth (m)
        a_cr = 0.025  # Critical crack depth (m)
        delta_sigma = 85e6  # Stress range (Pa)
        
        result = self.integrate_crack_growth(a_0, a_cr, delta_sigma)
        
        return {
            "crack_depth": result["crack_depth"],
            "da_dn": result["da_dn"],
            "cycles_to_failure": result["cycles_to_failure"],
            "stress_intensity_factor": self.compute_stress_intensity_factor(delta_sigma, a_0),
            "critical_crack_size": a_cr
        }
