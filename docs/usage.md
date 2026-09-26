# Usage

## Commands

### forge info

Prints version and current configuration as a table.

### forge inspect PATH

Inspects a file or directory.

For a file, prints size and SHA256.

For a directory, prints a table of all files with sizes and short hashes,
plus the total count and total size.

Exit code 1 if the path does not exist.

### forge prepare

Creates the output directory defined by FORGE_OUTPUT_DIR.

### forge --version

Prints the current version and exits.

## Configuration

All settings are read from environment variables with the prefix FORGE_.

| Variable         | Default   | Purpose           |
|------------------|-----------|-------------------|
| FORGE_APP_NAME   | forge     | Application name  |
| FORGE_DEBUG      | false     | Debug mode        |
| FORGE_LOG_LEVEL  | INFO      | Logging level     |
| FORGE_OUTPUT_DIR | ./output  | Output directory  |

A local .env file is read if present. Environment variables take precedence.

## Examples

    forge inspect ./pyproject.toml
    forge inspect ./src
    FORGE_OUTPUT_DIR=./build forge prepare
    FORGE_LOG_LEVEL=DEBUG forge info

## Exit codes

| Code | Meaning             |
|------|---------------------|
| 0    | Success             |
| 1    | Invalid input path  |
| 2    | Typer usage error   |
