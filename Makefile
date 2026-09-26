.PHONY: help install install-dev test lint typecheck format all clean run docker-build docker-run

PYTHON ?= python3
VENV   ?= .venv
BIN    := $(VENV)/bin

help:
	@echo "install      - Install production dependencies"
	@echo "install-dev  - Install development dependencies"
	@echo "test         - Run tests with coverage"
	@echo "lint         - Run Ruff linting"
	@echo "typecheck    - Run Mypy"
	@echo "format       - Run Ruff formatting"
	@echo "all          - Lint, typecheck, test"
	@echo "clean        - Remove build artifacts"
	@echo "run          - Start the CLI"
	@echo "docker-build - Build Docker image"
	@echo "docker-run   - Run Docker container"

$(VENV):
	$(PYTHON) -m venv $(VENV)

install: $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -e .

install-dev: $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -e ".[dev]"
	$(BIN)/pre-commit install || true

test: install-dev
	$(BIN)/pytest

lint: install-dev
	$(BIN)/ruff check src tests

typecheck: install-dev
	$(BIN)/mypy src

format: install-dev
	$(BIN)/ruff format src tests
	$(BIN)/ruff check --fix src tests

all: lint typecheck test

run: install
	$(BIN)/forge info

clean:
	rm -rf $(VENV) build dist *.egg-info .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov
	find . -type d -name __pycache__ -exec rm -rf {} +

docker-build:
	docker build -t forge-cli:latest .

docker-run:
	docker run --rm -it forge-cli:latest info
