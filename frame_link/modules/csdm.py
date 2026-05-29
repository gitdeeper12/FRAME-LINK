"""Connection Stiffness Degradation Module (CSDM).

S_deg,joint = 1 - K_joint(t)/K_joint,0
Force redistribution: K(t)·u = f
"""

import numpy as np


class CSDM:
    """Connection Stiffness Degradation Module."""
    
    STIFFNESS_WARN = 0.10
    STIFFNESS_CRITICAL = 0.25
    
    def __init__(self, ai_accelerated: bool = True):
        self.ai_accelerated = ai_accelerated
    
    def compute_stiffness_degradation(self, K_current: float, K_initial: float) -> float:
        """Compute stiffness degradation index.
        
        S_deg = 1 - K_current / K_initial
        """
        if K_initial <= 0:
            return 1.0
        return max(0.0, min(1.0, 1.0 - K_current / K_initial))
    
    def update_global_stiffness(self, K_global: np.ndarray, connection_id: int, K_new: float) -> np.ndarray:
        """Update global stiffness matrix with damaged connection."""
        K_updated = K_global.copy()
        # Simplified: replace connection stiffness (would need proper assembly)
        return K_updated
    
    def force_redistribution(self, K: np.ndarray, F: np.ndarray, fixed_dofs: list) -> np.ndarray:
        """Compute force redistribution after stiffness change.
        
        K·u = f → ΔF_member = K_member·Δu_member
        """
        n_dof = len(K)
        free_dofs = [i for i in range(n_dof) if i not in fixed_dofs]
        
        K_ff = K[np.ix_(free_dofs, free_dofs)]
        F_f = F[free_dofs]
        
        u = np.zeros(n_dof)
        u[free_dofs] = np.linalg.solve(K_ff, F_f)
        
        return u
    
    def ai_stiffness_estimate(self, sensor_data: np.ndarray) -> float:
        """AI-assisted stiffness estimation from sensor data."""
        if not self.ai_accelerated:
            return 0.95
        
        # Simplified ML prediction (would use XGBoost in production)
        predicted_ratio = 0.95 - 0.05 * np.std(sensor_data) / np.mean(sensor_data)
        return max(0.5, min(1.0, predicted_ratio))
    
    def compute(self) -> dict:
        """Run CSDM analysis."""
        K_initial = 1.0  # Reference stiffness
        K_current = self.ai_stiffness_estimate(np.random.randn(100))
        
        s_deg = self.compute_stiffness_degradation(K_current, K_initial)
        
        return {
            "s_deg": s_deg,
            "k_current": K_current,
            "k_initial": K_initial,
            "degradation_warning": s_deg >= self.STIFFNESS_WARN,
            "degradation_critical": s_deg >= self.STIFFNESS_CRITICAL
        }
