.PHONY: dev lint format typecheck test test-cov check ci-check fix int-to-hex hex-to-int clean clean-all

UV_DEV_RUN := uv run --extra dev

dev: ## Create .venv with Python 3.12 and install dev dependencies
	uv sync --python 3.12 --extra dev
	@if [ -f .pre-commit-config.yaml ] && [ -d .git ]; then uv run pre-commit install; fi

lint: ## Run ruff linter
	$(UV_DEV_RUN) ruff check src/starter tests

format: ## Format code with ruff
	$(UV_DEV_RUN) ruff format src/starter tests

typecheck: ## Run mypy
	$(UV_DEV_RUN) mypy src/starter

test: ## Run unit tests
	$(UV_DEV_RUN) pytest

test-cov: ## Run unit tests with coverage
	$(UV_DEV_RUN) pytest --cov --cov-report=term-missing

check: lint typecheck test ## Run all local checks

ci-check: lint typecheck test-cov ## Run CI checks

fix: ## Auto-fix lint and format
	$(UV_DEV_RUN) ruff check --fix src/starter tests
	$(UV_DEV_RUN) ruff format src/starter tests

int-to-hex: ## Prompt for an integer and print it as hex
	uv run int-to-hex

hex-to-int: ## Prompt for a hex number and print it as an integer
	uv run hex-to-int

clean: ## Remove local generated files
	rm -rf .pytest_cache .ruff_cache .mypy_cache .coverage htmlcov dist build

clean-all: clean ## Remove local generated files and the virtual environment
	rm -rf .venv
