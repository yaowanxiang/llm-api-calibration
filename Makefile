"""
Makefile for LLM API Calibration Tool
"""

.PHONY: help install install-dev install-all test lint format clean docs build release

help:
	@echo "可用命令:"
	@echo "  make install       - 安装基础包"
	@echo "  make install-dev   - 安装开发依赖"
	@echo "  make install-all   - 安装所有依赖"
	@echo "  make test          - 运行测试"
	@echo "  make lint          - 代码检查"
	@echo "  make format        - 代码格式化"
	@echo "  make clean         - 清理构建文件"
	@echo "  make docs          - 构建文档"
	@echo "  make build         - 构建包"
	@echo "  make release       - 发布版本"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pre-commit install

install-all:
	pip install -e ".[all]"
	pre-commit install

test:
	pytest tests/ -v --cov=llm_api_calibration --cov-report=html

test-quick:
	pytest tests/ -v

lint:
	flake8 llm_api_calibration
	mypy llm_api_calibration

format:
	black llm_api_calibration examples tests
	isort llm_api_calibration examples tests

format-check:
	black --check llm_api_calibration examples tests
	isort --check-only llm_api_calibration examples tests

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docs:
	cd docs && make html

build:
	python -m build

release:
	$(MAKE) clean
	$(MAKE) build
	twine check dist/*
	@echo "准备发布: 记得在GitHub上创建Release并上传到PyPI"