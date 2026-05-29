"""FRAME-LINK: Fatigue Reliability Assessment and Monitoring Extension for Structural Connection Integrity."""

__version__ = "1.0.0"
__author__ = "Samir Baladi"
__email__ = "gitdeeper@gmail.com"
__license__ = "MIT"
__doi__ = "10.5281/zenodo.20440786"

from frame_link.pipeline import FrameLinkAssessor
from frame_link.csii import CSII

__all__ = ["FrameLinkAssessor", "CSII"]
