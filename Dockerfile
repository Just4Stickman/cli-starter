FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src
COPY tests ./tests

RUN pip install --upgrade pip && pip install -e ".[dev]"

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

ENTRYPOINT ["forge"]
CMD ["info"]
