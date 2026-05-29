"""Palmgren-Miner linear damage accumulation."""

class PalmgrenMiner:
    """Palmgren-Miner damage accumulation.
    
    D(t) = Σ n_i / N_i(Δσ_i)
    """
    
    D_ALLOWABLE = 0.80
    D_CRITICAL = 1.00
    
    def __init__(self, sn_curve):
        self.sn_curve = sn_curve
    
    def accumulate(self, cycles: list) -> float:
        """Compute cumulative fatigue damage."""
        damage = 0.0
        for delta_sigma, n_i in cycles:
            n_f = self.sn_curve.get_cycles_to_failure(delta_sigma)
            if n_f > 0:
                damage += n_i / n_f
        return min(damage, 2.0)
    
    def remaining_life(self, current_damage: float) -> float:
        """Compute remaining life fraction."""
        if current_damage >= self.D_CRITICAL:
            return 0.0
        return (self.D_CRITICAL - current_damage) / self.D_CRITICAL
