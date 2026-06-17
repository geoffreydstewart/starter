# Starter

A minimal Python starter project using uv and Make. This project can be quite useful to quickly achieve a local Python development environment. 

You just need to install [uv](https://docs.astral.sh/uv/getting-started/installation/) and the usual dev tools like `make`.

Then add the dependencies you need in the [pyproject.toml](pyproject.toml)

## Requirements
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
make dev
```

To activate the virtual environment for manual tasks:

```bash
source .venv/bin/activate
```

To leave it:

```bash
deactivate
```

## Makefile Targets

- `make dev`: create `.venv` with Python 3.12 and install dev dependencies.
- `make lint`: run ruff lint checks.
- `make format`: format code with ruff.
- `make typecheck`: run mypy.
- `make test`: run unit tests.
- `make test-cov`: run unit tests with coverage.
- `make check`: run lint, typecheck, and tests.
- `make ci-check`: run lint, typecheck, and tests with coverage.
- `make fix`: auto-fix lint issues and format code.
- `make int-to-hex`: prompt for an integer and print it as hex.
- `make hex-to-int`: prompt for a hex number and print it as an integer.
- `make clean`: remove local generated files.
- `make clean-all`: remove local generated files and `.venv`.

## Examples

```bash
make int-to-hex
make hex-to-int
```
