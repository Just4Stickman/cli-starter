FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src

RUN pip install --upgrade pip && pip install -e .

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

ENTRYPOINT ["forge"]
CMD ["info"]
