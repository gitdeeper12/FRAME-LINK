"""Anomaly detection in strain fields."""

import numpy as np


class AnomalyDetector:
    """AI-assisted anomaly detection in sensor strain fields."""
    
    ANOMALY_THRESHOLD = 3.0
    
    def __init__(self):
        self.threshold = self.ANOMALY_THRESHOLD
    
    def compute_anomaly_score(self, measured: np.ndarray, predicted: np.ndarray) -> float:
        """Compute anomaly score A_score = |ε_meas - ε_pred|/σ."""
        if np.std(predicted) == 0:
            return 0.0
        return np.mean(np.abs(measured - predicted)) / np.std(predicted)
    
    def detect(self, measured: np.ndarray = None, predicted: np.ndarray = None) -> dict:
        """Detect anomalies in sensor data."""
        if measured is None:
            measured = np.random.randn(100) * 50
        if predicted is None:
            predicted = np.random.randn(100) * 48
        
        a_score = self.compute_anomaly_score(measured, predicted)
        is_anomaly = a_score > self.threshold
        
        return {
            "a_score": a_score,
            "is_anomaly": is_anomaly,
            "threshold": self.threshold,
            "confidence": min(0.95, 0.6 + a_score / 10)
        }
    
    def spatial_pattern_analysis(self, anomalies: list) -> dict:
        """Analyze spatial pattern of anomalies."""
        if not anomalies:
            return {"pattern": "NO_ANOMALIES", "risk": 0.0}
        
        n_anomalies = len(anomalies)
        if n_anomalies >= 3:
            return {"pattern": "CLUSTERED_ANOMALIES", "risk": 0.7}
        elif n_anomalies >= 1:
            return {"pattern": "ISOLATED_ANOMALY", "risk": 0.3}
        else:
            return {"pattern": "NO_ANOMALIES", "risk": 0.0}
