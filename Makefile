.PHONY: help install install-dev test lint format clean build docs run dashboard

help:
	@echo "FRAME-LINK Makefile Commands:"
	@echo "  make install      - Install production dependencies"
	@echo "  make install-dev  - Install development dependencies"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linters"
	@echo "  make format       - Format code"
	@echo "  make clean        - Clean build artifacts"
	@echo "  make build        - Build distribution packages"
	@echo "  make docs         - Build documentation"
	@echo "  make run          - Run assessment pipeline"
	@echo "  make dashboard    - Launch monitoring dashboard"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
	pre-commit install

test:
	pytest tests/ -v --cov=frame_link --cov-report=term

lint:
	flake8 frame_link/ tests/
	mypy frame_link/ --ignore-missing-imports

format:
	black frame_link/ tests/ examples/
	isort frame_link/ tests/ examples/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build
	@echo "Build complete. Check dist/ directory"

docs:
	cd docs && make html
	@echo "Documentation built in docs/_build/html/"

run:
	python -m frame_link.pipeline --config configs/default.yaml

dashboard:
	streamlit run frame_link/monitoring/app.py
