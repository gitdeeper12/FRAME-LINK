"""S-N curves per Eurocode 3 EN 1993-1-9."""

class SNCurve:
    """S-N curve for fatigue design."""
    
    FAT_CLASSES = {
        'FAT36': 36e6, 'FAT40': 40e6, 'FAT45': 45e6, 'FAT50': 50e6,
        'FAT56': 56e6, 'FAT63': 63e6, 'FAT71': 71e6, 'FAT80': 80e6,
        'FAT90': 90e6, 'FAT100': 100e6, 'FAT112': 112e6, 'FAT125': 125e6,
        'FAT140': 140e6, 'FAT160': 160e6
    }
    
    def __init__(self, fat_class: str = 'FAT71', m: int = 3):
        if fat_class not in self.FAT_CLASSES:
            raise ValueError(f"Unknown FAT class: {fat_class}")
        
        self.fat_class = fat_class
        self.sigma_c = self.FAT_CLASSES[fat_class]
        self.m = m
        self.C = (self.sigma_c ** m) * 2e6
    
    def get_cycles_to_failure(self, delta_sigma: float) -> float:
        """Get cycles to failure N_f = C / (Δσ)^m."""
        if delta_sigma <= 0:
            return float('inf')
        return self.C / (delta_sigma ** self.m)
    
    def get_constant_amplitude_limit(self) -> float:
        """Get constant amplitude fatigue limit (CAFL = FAT/2)."""
        return self.sigma_c * 0.5
