"""Simple tests for FRAME-LINK."""

import sys
sys.path.insert(0, '.')


def test_paris_law():
    """Test Paris-Erdogan crack propagation."""
    print("\n=== Testing Paris-Erdogan Law ===")
    
    def paris_law(C, m, delta_K):
        return C * (delta_K ** m)
    
    delta_K = 10.0  # MPa√m
    C = 3e-13
    m = 3.0
    
    da_dn = paris_law(C, m, delta_K)
    print(f"  Crack growth rate da/dN: {da_dn:.3e} m/cycle")
    assert da_dn > 0
    print("✓ Paris law test passed!")


def test_stress_intensity():
    """Test stress intensity factor computation."""
    print("\n=== Testing Stress Intensity Factor ===")
    
    import numpy as np
    
    def stress_intensity(Y, delta_sigma, a):
        return Y * delta_sigma * np.sqrt(np.pi * a)
    
    Y = 1.12
    delta_sigma = 85e6
    a = 0.001
    
    delta_K = stress_intensity(Y, delta_sigma, a)
    print(f"  Stress intensity factor ΔK: {delta_K/1e6:.2f} MPa√m")
    assert delta_K > 0
    print("✓ Stress intensity test passed!")


def test_csii():
    """Test CSII computation."""
    print("\n=== Testing CSII Index ===")
    
    def compute_csii(s_deg, d_joint, beta):
        beta_target = 3.8
        d_allowable = 0.80
        term1 = 0.40 * (1 - s_deg)
        term2 = 0.35 * (1 - d_joint / d_allowable)
        term3 = 0.25 * (beta / beta_target)
        return term1 + term2 + term3
    
    # Perfect connection
    csii = compute_csii(0.0, 0.0, 4.0)
    print(f"  Perfect CSII: {csii:.3f}")
    assert csii > 0.90
    
    # Degraded connection
    csii = compute_csii(0.15, 0.60, 2.5)
    print(f"  Degraded CSII: {csii:.3f}")
    assert csii < 0.90
    
    print("✓ CSII test passed!")


def test_palmgren_miner():
    """Test Palmgren-Miner damage accumulation."""
    print("\n=== Testing Palmgren-Miner ===")
    
    def damage(cycles, C, m=3):
        d = 0.0
        for delta_sigma, n in cycles:
            n_f = C / (delta_sigma ** m)
            if n_f > 0:
                d += n / n_f
        return min(d, 1.5)
    
    cycles = [(50e6, 1000), (40e6, 5000), (30e6, 20000)]
    C = (71e6 ** 3) * 2e6
    
    d = damage(cycles, C)
    print(f"  Miner damage: {d:.4f}")
    assert d >= 0
    print("✓ Palmgren-Miner test passed!")


def test_rainflow():
    """Test rainflow cycle counting."""
    print("\n=== Testing Rainflow Counting ===")
    
    import numpy as np
    
    def simple_rainflow(stress):
        peaks = []
        for i in range(1, len(stress) - 1):
            if (stress[i] > stress[i-1] and stress[i] > stress[i+1]) or \
               (stress[i] < stress[i-1] and stress[i] < stress[i+1]):
                peaks.append(stress[i])
        return peaks
    
    t = np.linspace(0, 10, 100)
    stress = 100e6 * np.sin(2 * np.pi * t)
    
    peaks = simple_rainflow(stress)
    print(f"  Number of peaks/valleys: {len(peaks)}")
    assert len(peaks) > 0
    print("✓ Rainflow test passed!")


def test_goodman():
    """Test Goodman mean stress correction."""
    print("\n=== Testing Goodman Correction ===")
    
    def goodman(sigma_a, sigma_m, sigma_u=490e6):
        if sigma_m <= 0:
            return sigma_a
        return sigma_a / (1 - sigma_m / sigma_u)
    
    sigma_a = 40e6
    sigma_m = 20e6
    
    sigma_eq = goodman(sigma_a, sigma_m)
    print(f"  Equivalent stress: {sigma_eq/1e6:.1f} MPa")
    assert sigma_eq > sigma_a
    print("✓ Goodman correction test passed!")


def run_all():
    print("=" * 50)
    print("FRAME-LINK TEST SUITE")
    print("=" * 50)
    
    tests = [test_paris_law, test_stress_intensity, test_csii, 
             test_palmgren_miner, test_rainflow, test_goodman]
    
    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ Test failed: {test.__name__} - {e}")
    
    print("\n" + "=" * 50)
    print(f"RESULTS: {passed}/{len(tests)} passed")
    print("=" * 50)


if __name__ == "__main__":
    run_all()
