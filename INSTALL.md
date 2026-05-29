# FRAME-LINK Installation Guide

## Quick Install

### Using pip (recommended)
```bash
pip install frame-link-engine
```

From source

```bash
git clone https://github.com/gitdeeper12/FRAME-LINK.git
cd FRAME-LINK
pip install -e .
```

Requirements

· Python >= 3.9
· Dependencies are automatically installed with pip

Verify Installation

```python
from frame_link import FrameLinkAssessor
print("FRAME-LINK ready!")
```

Platform Support

· Linux
· macOS
· Windows (WSL recommended)

Optional Dependencies

For sensor integration:

```bash
pip install pyserial paho-mqtt
```

For GPU acceleration:

```bash
pip install cupy-cuda11x
```

Troubleshooting

Import errors

Ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

Permission issues

Use virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Next Steps

See README.md for usage examples and documentation.
