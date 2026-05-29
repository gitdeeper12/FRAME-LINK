"""Model validation tests for FRAME-LINK."""

import sys
sys.path.insert(0, '.')

from frame_link.modules.scfmm import SCFMM
from frame_link.modules.fdarm import FDARM
from frame_link.modules.csdm import CSDM
from frame_link.csii import CSII

def test_scfmm_validation():
    """Test SCFMM module."""
    print("\n=== SCFMM Validation ===")
    scfmm = SCFMM()
    result = scfmm.compute()
    
    print(f"  Crack depth: {result['crack_depth']:.4f} m")
    print(f"  da/dN: {result['da_dn']:.3e} m/cycle")
    print(f"  Cycles to failure: {result['cycles_to_failure']:,}")
    
    assert result['crack_depth'] > 0
    assert result['da_dn'] > 0
    print("✓ SCFMM passed")

def test_fdarm_validation():
    """Test FDARM module."""
    print("\n=== FDARM Validation ===")
    fdarm = FDARM()
    result = fdarm.compute()
    
    print(f"  D_joint: {result['d_joint']:.4f}")
    print(f"  β index: {result['beta']:.3f}")
    print(f"  Cycles counted: {result['cycles_counted']}")
    
    assert result['d_joint'] >= 0
    assert result['beta'] > 0
    print("✓ FDARM passed")

def test_csdm_validation():
    """Test CSDM module."""
    print("\n=== CSDM Validation ===")
    csdm = CSDM()
    result = csdm.compute()
    
    print(f"  S_deg: {result['s_deg']:.3f}")
    print(f"  K_current: {result['k_current']:.3f}")
    print(f"  Degradation warning: {result['degradation_warning']}")
    
    assert 0.0 <= result['s_deg'] <= 1.0
    print("✓ CSDM passed")

def test_csii_validation():
    """Test CSII composite index."""
    print("\n=== CSII Validation ===")
    csii = CSII.compute(s_deg=0.05, d_joint=0.35, beta=3.8)
    print(f"  CSII: {csii:.3f}")
    assert csii >= 0.85
    print("✓ CSII passed")

def run_all():
    print("=" * 50)
    print("FRAME-LINK MODEL VALIDATION")
    print("=" * 50)
    
    tests = [test_scfmm_validation, test_fdarm_validation, 
             test_csdm_validation, test_csii_validation]
    
    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} failed: {e}")
    
    print("\n" + "=" * 50)
    print(f"RESULTS: {passed}/{len(tests)} passed")
    print("=" * 50)

if __name__ == "__main__":
    run_all()
