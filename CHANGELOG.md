# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-08-18

### Added
- ✨ Initial release of LLM API Calibration Tool
- 🎯 APICalibrator core module for API calibration
- 🧠 ClaudeWebSimulationStrategy for Web version simulation
- 🔧 Scene-based configuration (research_writing/code_review/data_analysis/daily_chat)
- 🛠️ Tool chain simulation (search, code execution, context management)
- 🔄 Version compatibility detection and automatic fallback
- 📚 Comprehensive documentation (API reference, best practices, technical details)
- ✅ Unit tests with pytest
- 📦 Python package structure with pyproject.toml
- 📄 MIT license

### Features
- Smart system prompt engineering based on leaked Claude official prompts
- Modular prompt architecture (identity → principles → scenario → tools → safety)
- Scenario-specific optimizations for different use cases
- Automatic detection of deprecated API parameters (temperature/top_p)
- Graceful degradation strategy for new API versions
- Configurable memory window for conversation context

### Documentation
- README.md with quick start guide
- docs/api_reference.md - Complete API reference
- docs/best_practices.md - Best practices guide
- docs/technical_details.md - Technical principles and implementation details
- CONTRIBUTING.md - Contribution guidelines
- PROJECT_SUMMARY.md - Project delivery report

### Python Package
- PyPI-ready package structure
- Support for Python 3.8+
- Development dependencies (pytest, pytest-cov)
- Optional dependencies for documentation (sphinx)

### Testing
- Unit tests for APICalibrator
- Tests for configuration generation
- Tests for scenario-specific modules
- Tests for language-specific configurations

### CI/CD
- GitHub Actions workflow for automated testing
- Multi-Python version testing (3.8, 3.9, 3.10, 3.11)
- Automated package building
- Code coverage reporting

---

## [Unreleased]

### Planned
- 🔍 Real web search integration (DuckDuckGo, Tavily)
- 📄 Document parsing (PDF, DOCX, TXT)
- 🧪 Integration tests with real API calls
- 📊 Performance benchmarks and comparison metrics
- 🌐 Multi-language support expansion
- 🎨 Visualization of calibration effects
- 📖 Tutorial notebooks
- 🚀 CLI tool for quick calibration