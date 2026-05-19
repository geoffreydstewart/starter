# Repository Guidelines

## Project Structure

- `src/starter/` contains the Python package.
- `tests/` contains unit tests.
- `pyproject.toml` defines packaging, console scripts, and tool config.
- `Makefile` is the primary development interface.

## Development

- Use Python 3.12.
- Use `uv` for dependency management and command execution.
- Run `make dev` to create `.venv` and install development dependencies.
- Activate the environment for manual work with `source .venv/bin/activate`.

## Common Commands

- `make lint`: run ruff lint checks.
- `make format`: format code with ruff.
- `make typecheck`: run mypy.
- `make test`: run unit tests.
- `make check`: run lint, typecheck, and tests.
- `make ci-check`: run lint, typecheck, and tests with coverage.
- `make fix`: apply ruff fixes and formatting.
- `make int-to-hex`: run the integer-to-hex CLI.
- `make hex-to-int`: run the hex-to-integer CLI.
- `make clean`: remove generated cache and build files.
- `make clean-all`: run `clean` and remove `.venv`.

## Coding Conventions

- Keep code typed and compatible with strict mypy.
- Keep public behavior covered by unit tests.
- Prefer small pure functions for logic and thin CLI wrappers for input/output.
- Let invalid conversion input raise the standard Python exception unless product requirements change.

## Verification

Before handing off changes, run:

```bash
make check
```

For changes that affect coverage expectations, run:

```bash
make ci-check
```
