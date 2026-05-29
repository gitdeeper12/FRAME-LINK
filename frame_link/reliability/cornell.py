"""Cornell first-order second-moment reliability index."""

import numpy as np


def compute_cornell_index(mu_R: float, mu_S: float, sigma_R: float, sigma_S: float, sigma_AI: float = 0.0) -> float:
    """Compute Cornell reliability index.
    
    β = (μ_R - μ_S) / √(σ_R² + σ_S² + σ_AI²)
    """
    numerator = mu_R - mu_S
    if numerator <= 0:
        return 0.0
    
    denominator = np.sqrt(sigma_R**2 + sigma_S**2 + sigma_AI**2)
    return numerator / denominator


def failure_probability(beta: float) -> float:
    """Compute failure probability P_f = Φ(-β)."""
    from scipy.special import ndtr
    return ndtr(-beta)


def target_beta(target_pf: float = 1e-4) -> float:
    """Compute target reliability index from target failure probability."""
    from scipy.special import ndtri
    return -ndtri(target_pf)
