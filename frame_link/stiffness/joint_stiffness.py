"""Joint stiffness measurement and tracking."""

import numpy as np


class JointStiffness:
    """Connection stiffness measurement and degradation tracking."""
    
    def __init__(self):
        self.stiffness_history = []
    
    def measure_stiffness(self, force: float, displacement: float) -> float:
        """Measure joint stiffness K = F/δ."""
        if displacement <= 0:
            return float('inf')
        return force / displacement
    
    def compute_degradation(self, K_current: float, K_initial: float) -> float:
        """Compute stiffness degradation index."""
        if K_initial <= 0:
            return 1.0
        return 1.0 - K_current / K_initial
    
    def update_history(self, stiffness: float):
        """Update stiffness history."""
        self.stiffness_history.append(stiffness)
    
    def get_trend(self) -> float:
        """Get stiffness degradation trend."""
        if len(self.stiffness_history) < 2:
            return 0.0
        return (self.stiffness_history[-1] - self.stiffness_history[0]) / len(self.stiffness_history)
