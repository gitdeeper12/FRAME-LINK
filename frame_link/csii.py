"""Connection Structural Integrity Index (CSII)."""

class CSII:
    """
    Connection Structural Integrity Index.
    
    CSII = 0.40·(1 - S_deg) + 0.35·(1 - D_joint/D_allow) + 0.25·(β_joint/β_target)
    """
    
    BETA_TARGET = 3.8
    D_ALLOWABLE = 0.80
    STEADY_THRESHOLD = 0.90
    MONITORING_THRESHOLD = 0.75
    MITIGATION_THRESHOLD = 0.65
    
    @staticmethod
    def compute(s_deg: float, d_joint: float, beta: float) -> float:
        """Compute CSII composite index."""
        term1 = 0.40 * (1 - s_deg)
        term2 = 0.35 * (1 - d_joint / CSII.D_ALLOWABLE)
        term3 = 0.25 * (beta / CSII.BETA_TARGET)
        
        csii = term1 + term2 + term3
        return max(0.0, min(csii, 1.0))
    
    @staticmethod
    def get_governance_action(csii: float) -> str:
        """Get governance action based on CSII value."""
        if csii >= 0.90:
            return "Continue standard monitoring; no intervention required"
        elif csii >= 0.75:
            return "Increase monitoring frequency; schedule targeted NDT inspection"
        elif csii >= 0.65:
            return "Immediate temporary load restriction; structural review within 48 hours"
        else:
            return "Immediate operational shutdown; site evacuation; emergency assessment"
