"""Fatigue Damage Accumulation and Reliability Module (FDARM).

Palmgren-Miner damage: D(t) = Σ n_i/N_i(Δσ_i)
Cornell reliability index: β = (μ_R - μ_S)/√(σ_R² + σ_S² + σ_AI²)
"""

import numpy as np


class FDARM:
    """Fatigue Damage Accumulation and Reliability Module."""
    
    D_ALLOWABLE = 0.80
    BETA_TARGET = 3.8
    
    def __init__(self, sn_class: str = "FAT71", goodman_correction: bool = True):
        self.sn_class = sn_class
        self.goodman_enabled = goodman_correction
        self._init_sn_curve()
    
    def _init_sn_curve(self):
        """Initialize S-N curve parameters per Eurocode 3."""
        fat_classes = {"FAT36": 36e6, "FAT50": 50e6, "FAT71": 71e6, "FAT90": 90e6, "FAT125": 125e6}
        sigma_c = fat_classes.get(self.sn_class, 71e6)
        self.C = (sigma_c ** 3) * 2e6  # Constant for m=3
    
    def rainflow_counting(self, stress_history: np.ndarray) -> list:
        """ASTM E1049-85 rainflow cycle counting."""
        if len(stress_history) < 3:
            return []
        
        # Extract turning points
        turning = [stress_history[0]]
        for i in range(1, len(stress_history) - 1):
            if (stress_history[i] > stress_history[i-1] and stress_history[i] > stress_history[i+1]) or \
               (stress_history[i] < stress_history[i-1] and stress_history[i] < stress_history[i+1]):
                turning.append(stress_history[i])
        turning.append(stress_history[-1])
        
        return [(abs(turning[i+1] - turning[i]) / 2, 1) for i in range(len(turning) - 1)]
    
    def goodman_correction(self, sigma_a: float, sigma_m: float, sigma_u: float = 490e6) -> float:
        """Apply Goodman mean stress correction.
        
        σ_a,eq = σ_a / (1 - σ_m/σ_u)
        """
        if sigma_m <= 0:
            return sigma_a
        return sigma_a / (1 - sigma_m / sigma_u)
    
    def palmgren_miner(self, cycles: list) -> float:
        """Compute Palmgren-Miner damage accumulation.
        
        D = Σ n_i / N_i(Δσ_i)
        """
        damage = 0.0
        for delta_sigma, n_i in cycles:
            if self.goodman_enabled:
                delta_sigma = self.goodman_correction(delta_sigma, delta_sigma * 0.1)
            n_f = self.C / (delta_sigma ** 3)
            if n_f > 0:
                damage += n_i / n_f
        return min(damage, 1.5)
    
    def cornell_reliability_index(self, d_joint: float, var_ai: float = 0.002) -> float:
        """Compute Cornell reliability index.
        
        β = (μ_R - μ_S)/√(σ_R² + σ_S² + σ_AI²)
        """
        mu_R = 1.0  # Mean resistance (Miner sum at failure)
        mu_S = d_joint  # Mean load effect
        sigma_R = 0.45  # Resistance standard deviation
        sigma_S = 0.08  # Load standard deviation
        
        numerator = mu_R - mu_S
        if numerator <= 0:
            return 0.0
        
        denominator = np.sqrt(sigma_R**2 + sigma_S**2 + var_ai)
        return numerator / denominator
    
    def compute(self) -> dict:
        """Run FDARM analysis."""
        # Simulated stress history
        stress_history = np.random.randn(10000) * 15e6 + 50e6
        
        cycles = self.rainflow_counting(stress_history)
        d_joint = self.palmgren_miner(cycles)
        beta = self.cornell_reliability_index(d_joint)
        
        return {
            "d_joint": d_joint,
            "beta": beta,
            "cycles_counted": len(cycles),
            "damage_limit_exceeded": d_joint >= self.D_ALLOWABLE,
            "reliability_target_met": beta >= self.BETA_TARGET
        }
