# Forge

Production-grade CLI starter. Typed, tested, containerized, and CI-ready from the first commit.

## Features

- Typer-based CLI with Rich output
- Typed, validated configuration via pydantic-settings
- Full test suite with coverage
- Ruff for linting and formatting
- Mypy in strict mode
- GitHub Actions CI across Python 3.10 to 3.13
- Docker image with non-root user
- Pre-commit hooks
- Makefile for standard workflows
- MIT licensed

## Usage

    forge --version
    forge info
    forge inspect ./some-folder
    forge prepare

## Configuration

All settings are read from environment variables with the prefix FORGE_.

| Variable         | Default   | Purpose           |
|------------------|-----------|-------------------|
| FORGE_APP_NAME   | forge     | Application name  |
| FORGE_DEBUG      | false     | Debug mode        |
| FORGE_LOG_LEVEL  | INFO      | Logging level     |
| FORGE_OUTPUT_DIR | ./output  | Output directory  |

## License

MIT
