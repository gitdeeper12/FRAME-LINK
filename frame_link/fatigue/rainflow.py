"""ASTM E1049-85 rainflow cycle counting algorithm."""

import numpy as np


class RainflowCounter:
    """Rainflow cycle counting for variable amplitude fatigue."""
    
    def count(self, stress_history: np.ndarray) -> list:
        """Extract cycle spectrum from stress history."""
        if len(stress_history) < 3:
            return []
        
        # Extract turning points
        turning = self._extract_turning_points(stress_history)
        
        # Perform rainflow counting
        cycles = self._rainflow_algorithm(turning)
        
        # Bin by amplitude
        return self._bin_cycles(cycles)
    
    def _extract_turning_points(self, data: np.ndarray) -> np.ndarray:
        """Extract peaks and valleys."""
        turning = [data[0]]
        for i in range(1, len(data) - 1):
            if (data[i] > data[i-1] and data[i] > data[i+1]) or \
               (data[i] < data[i-1] and data[i] < data[i+1]):
                turning.append(data[i])
        turning.append(data[-1])
        return np.array(turning)
    
    def _rainflow_algorithm(self, points: np.ndarray) -> list:
        """Implement rainflow counting algorithm."""
        if len(points) < 3:
            return []
        
        cycles = []
        stack = list(points)
        idx = 0
        
        while len(stack) >= 3 and idx < len(stack) - 2:
            x, y, z = stack[idx], stack[idx + 1], stack[idx + 2]
            
            if abs(y - x) <= abs(z - y):
                amplitude = abs(y - x) / 2
                mean = (x + y) / 2
                cycles.append((amplitude, mean, 1))
                stack.pop(idx)
                stack.pop(idx)
                idx = max(0, idx - 1)
            else:
                idx += 1
        
        return cycles
    
    def _bin_cycles(self, cycles: list, n_bins: int = 20) -> list:
        """Bin cycles by amplitude."""
        if not cycles:
            return []
        
        amplitudes = [c[0] for c in cycles]
        max_amp = max(amplitudes)
        min_amp = min(amplitudes)
        
        if max_amp == min_amp:
            return [(max_amp, len(cycles))]
        
        bins = [[] for _ in range(n_bins)]
        for amp in amplitudes:
            idx = min(int((amp - min_amp) / (max_amp - min_amp) * n_bins), n_bins - 1)
            bins[idx].append(amp)
        
        return [(np.mean(b) if b else 0, len(b)) for b in bins if b]
