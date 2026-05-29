"""Hasofer-Lind exact invariant reliability index (FORM)."""

import numpy as np


class HasoferLindSolver:
    """Iterative Hasofer-Lind reliability index solver."""
    
    def __init__(self, target_beta: float = 3.8):
        self.target_beta = target_beta
    
    def solve(self, limit_state, means: np.ndarray, stds: np.ndarray, max_iter: int = 100) -> float:
        """Solve for reliability index."""
        n = len(means)
        x = np.zeros(n)
        
        for _ in range(max_iter):
            g, grad = self._evaluate(limit_state, x, means, stds)
            
            if abs(g) < 1e-6:
                break
            
            grad_norm = np.linalg.norm(grad)
            if grad_norm < 1e-10:
                break
            
            alpha = -grad / grad_norm
            beta = g / grad_norm
            x = -beta * alpha
        
        return np.linalg.norm(x)
    
    def _evaluate(self, limit_state, x: np.ndarray, means: np.ndarray, stds: np.ndarray):
        """Evaluate limit state and gradient."""
        original = means + x * stds
        g = limit_state(original)
        
        epsilon = 1e-6
        grad = np.zeros_like(x)
        for i in range(len(x)):
            x_pert = x.copy()
            x_pert[i] += epsilon
            original_pert = means + x_pert * stds
            g_pert = limit_state(original_pert)
            grad[i] = (g_pert - g) / epsilon
        
        return g, grad
