# ---- Stage 1: build (instala dependencias) ----
FROM python:3.12-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --prefix=/install .

# ---- Stage 2: runtime (imagem enxuta, sem ferramentas de build) ----
FROM python:3.12-slim AS runtime

RUN apt-get update && apt-get install -y --no-install-recommends \
    libjpeg62-turbo \
    zlib1g \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --uid 1000 appuser

WORKDIR /app

COPY --from=builder /install /usr/local
COPY bot ./bot
COPY alembic.ini ./

USER appuser

EXPOSE 8000

CMD ["uvicorn", "bot.main:app", "--host", "0.0.0.0", "--port", "8000"]
