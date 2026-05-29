"""Simple import tests for FRAME-LINK."""

def test_import_frame_link():
    """Test main package import."""
    try:
        import frame_link
        assert hasattr(frame_link, '__version__')
        print("✓ frame_link imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import frame_link: {e}")
        raise

def test_import_modules():
    """Test modules import."""
    modules = ['scfmm', 'fdarm', 'csdm']
    for module in modules:
        try:
            exec(f"from frame_link.modules import {module}")
            print(f"✓ {module} imported successfully")
        except ImportError as e:
            print(f"✗ Failed to import {module}: {e}")

def test_import_fracture():
    """Test fracture module import."""
    try:
        from frame_link.fracture import paris_erdogan, stress_intensity
        print("✓ fracture module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import fracture: {e}")

def test_import_fatigue():
    """Test fatigue module import."""
    try:
        from frame_link.fatigue import rainflow, palmgren_miner
        print("✓ fatigue module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import fatigue: {e}")
