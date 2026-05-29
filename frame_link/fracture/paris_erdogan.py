"""Paris-Erdogan crack propagation law implementation."""

import numpy as np


class ParisErdogan:
    """Paris-Erdogan crack propagation law.
    
    da/dN = C·(ΔK)^m
    """
    
    def __init__(self, C: float = 3e-13, m: float = 3.0):
        self.C = C
        self.m = m
    
    def da_dn(self, delta_K: float) -> float:
        """Compute crack growth rate per cycle."""
        return self.C * (delta_K ** self.m)
    
    def integrate(self, a_0: float, a_cr: float, delta_sigma: float, Y: float = 1.12) -> dict:
        """Integrate Paris law to failure."""
        a = a_0
        cycles = 0
        history = []
        
        while a < a_cr and cycles < 1e7:
            delta_K = Y * delta_sigma * np.sqrt(np.pi * a)
            da = self.da_dn(delta_K)
            if da <= 0:
                break
            cycles += 1
            a += da
            history.append((cycles, a, da))
        
        return {"cycles": cycles, "final_crack": a, "history": history}


def integrate_crack_growth(a_0: float, a_cr: float, delta_sigma: float, C: float = 3e-13, m: float = 3.0, Y: float = 1.12) -> int:
    """Integrate Paris law to compute cycles to failure."""
    model = ParisErdogan(C, m)
    result = model.integrate(a_0, a_cr, delta_sigma, Y)
    return result["cycles"]
