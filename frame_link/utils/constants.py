"""Material constants and fatigue limits."""

# Material constants for Paris-Erdogan law
MATERIAL_CONSTANTS = {
    'steel_S235': {'C': 3.5e-13, 'm': 3.0, 'K_Ic': 70.0, 'sigma_u': 360e6},
    'steel_S355': {'C': 3.0e-13, 'm': 3.0, 'K_Ic': 80.0, 'sigma_u': 490e6},
    'steel_S460': {'C': 2.8e-13, 'm': 3.0, 'K_Ic': 100.0, 'sigma_u': 540e6},
    'steel_high_strength': {'C': 2.0e-13, 'm': 3.1, 'K_Ic': 120.0, 'sigma_u': 700e6}
}

# Fatigue limits per Eurocode 3
FATIGUE_LIMITS = {
    'FAT36': 36e6,
    'FAT40': 40e6,
    'FAT45': 45e6,
    'FAT50': 50e6,
    'FAT56': 56e6,
    'FAT63': 63e6,
    'FAT71': 71e6,
    'FAT80': 80e6,
    'FAT90': 90e6,
    'FAT100': 100e6,
    'FAT112': 112e6,
    'FAT125': 125e6,
    'FAT140': 140e6,
    'FAT160': 160e6
}

# Safety thresholds
SAFETY_THRESHOLDS = {
    'csii_steady': 0.90,
    'csii_monitoring': 0.75,
    'csii_mitigation': 0.65,
    'beta_target': 3.8,
    'd_allowable': 0.80,
    'd_critical': 1.00,
    's_deg_warning': 0.10,
    's_deg_critical': 0.25
}
