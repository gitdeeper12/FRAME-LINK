"""Main FRAME-LINK assessment pipeline."""

import numpy as np
from dataclasses import dataclass
from typing import Dict, Optional

from frame_link.csii import CSII
from frame_link.modules.scfmm import SCFMM
from frame_link.modules.fdarm import FDARM
from frame_link.modules.csdm import CSDM
from frame_link.ai_support.anomaly_detection import AnomalyDetector


@dataclass
class PipelineResult:
    """Pipeline assessment result."""
    csii: float
    signal: str
    beta: float
    d_joint: float
    s_deg: float
    crack_depth: float
    da_dn: float
    a_score: float


class FrameLinkAssessor:
    """FRAME-LINK main assessment pipeline."""
    
    def __init__(self, connection_config: Optional[Dict] = None, sensor_stream: str = "live"):
        self.connection_config = connection_config or {}
        self.sensor_stream = sensor_stream
        
        self.scfmm = SCFMM()
        self.fdarm = FDARM()
        self.csdm = CSDM()
        self.anomaly_detector = AnomalyDetector()
        self.csii = CSII()
    
    def evaluate(self) -> PipelineResult:
        """Run full FRAME-LINK assessment pipeline."""
        # SCFMM: Stress intensity factor and crack growth
        scfmm_result = self.scfmm.compute()
        
        # FDARM: Fatigue damage and reliability index
        fdarm_result = self.fdarm.compute()
        
        # CSDM: Connection stiffness degradation
        csdm_result = self.csdm.compute()
        
        # Anomaly detection
        anomaly_result = self.anomaly_detector.detect()
        
        # CSII composite index
        csii_value = self.csii.compute(
            s_deg=csdm_result["s_deg"],
            d_joint=fdarm_result["d_joint"],
            beta=fdarm_result["beta"]
        )
        
        signal = self._get_signal(csii_value)
        
        return PipelineResult(
            csii=csii_value,
            signal=signal,
            beta=fdarm_result["beta"],
            d_joint=fdarm_result["d_joint"],
            s_deg=csdm_result["s_deg"],
            crack_depth=scfmm_result["crack_depth"],
            da_dn=scfmm_result["da_dn"],
            a_score=anomaly_result["a_score"]
        )
    
    def _get_signal(self, csii: float) -> str:
        if csii >= 0.90:
            return "🟢 STEADY_ELASTIC_STATE"
        elif csii >= 0.75:
            return "🟠 ANOMALY_DETECTED_L1"
        elif csii >= 0.65:
            return "🟠 DEGRADATION_WARNING_L2"
        else:
            return "🔴 CRITICAL_CONNECTION_FAILURE"
