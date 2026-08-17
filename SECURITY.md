# Security Policy

## Supported Versions

Currently supported versions of this project:
- Version 0.1.0 (Current)

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please follow these steps:

### 1. Do NOT use public issue tracker
**IMPORTANT**: Do NOT create a public GitHub issue for security vulnerabilities.

### 2. Send a private disclosure
Send an email to the maintainer:
- **Email**: yaowanxiang@qut.edu.cn
- **Subject**: [SECURITY] LLM API Calibration Tool - Security Vulnerability Report

Please include:
- A clear description of the vulnerability
- Steps to reproduce the issue
- Potential impact and affected versions
- Any suggested fixes or workarounds

### 3. What happens next
1. **Confirmation**: The maintainer will acknowledge receipt within 48 hours
2. **Analysis**: The vulnerability will be analyzed and confirmed
3. **Fix**: A fix will be developed
4. **Release**: A security patch will be released as soon as possible
5. **Credit**: You will be credited for the discovery (if desired)

### 4. Disclosure timeline
- **Critical vulnerabilities**: Patch released within 7 days
- **High severity**: Patch released within 14 days
- **Medium severity**: Patch released within 30 days
- **Low severity**: Patch released in next scheduled release

## Security Best Practices

### API Key Management
- Never commit API keys to version control
- Use environment variables or secret management services
- Rotate API keys regularly
- Use scoped API keys with minimal permissions

### Code Review
- All code changes go through pull request review
- Security-sensitive changes require at least 2 reviewers
- Automated security scanning (e.g., Bandit) is part of CI/CD

### Dependency Management
- Dependencies are regularly updated for security patches
- Use `pip-audit` to check for known vulnerabilities
- Review dependencies for security implications

### Logging
- Avoid logging sensitive information (API keys, personal data)
- Use appropriate log levels
- Implement log rotation and secure log storage

## Security Features

This project includes the following security features:

### Input Validation
- All user inputs are validated before processing
- Sanitization of user-provided content
- Protection against prompt injection attacks

### Error Handling
- Secure error messages (no sensitive data leakage)
- Graceful degradation on failures
- Comprehensive error logging

### API Security
- Support for scoped API keys
- Secure credential storage
- Automatic timeout handling

## Related Resources

- [GitHub Security Advisories](https://github.com/yaowanxiang/llm-api-calibration/security/advisories)
- [CISA Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [Python Security Best Practices](https://wiki.python.org/moin/SecurityBestPractices)