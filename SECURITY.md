# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

**Please DO NOT report security vulnerabilities through public GitHub issues.**

Please report them via email to: **gitdeeper@gmail.com**

You should receive a response within 48 hours.

## Security Features

### Data Integrity
- SHA-256 checksums for all archival data
- Append-only record writing
- Tamper-evidence logging

### AI Output Safety
- Physics-constrained outputs
- Mandatory engineering verification
- Uncertainty quantification for AI predictions

### Access Control
- Environment-based configuration
- JWT authentication for API endpoints

## Best Practices

1. Never commit `.env` files to version control
2. Use strong, unique secrets in production
3. Validate all AI outputs against physics-based analysis
4. Maintain regular backups of archival data

## Contact

Security Coordinator: Samir Baladi (gitdeeper@gmail.com)
