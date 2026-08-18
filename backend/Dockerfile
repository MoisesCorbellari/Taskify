# Estágio de compilação (Builder)
FROM python:3.14-slim AS builder

WORKDIR /app

# Instala o uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Dependências necessárias para compilação
RUN apt-get update && \
    apt-get install -y --no-install-recommends \ 
    gcc \ 
    python3-dev \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copia os arquivos de dependência
COPY pyproject.toml uv.lock ./

# Instala as dependências de produção
# --no-dev: ignora pacotes de desenvolvimento
# --frozen: usa exatamente o uv.lock 
# --no-install-project: não instala a aplicação como pacote
RUN uv sync --no-dev --frozen --no-install-project

# Estágio final
FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Biblioteca necessária em runtime para PostgreSQL
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq5 && \
    rm -rf /var/lib/apt/lists/*

# Copia o ambiente virtual criado pelo uv
COPY --from=builder /app/.venv /app/.venv

# Copia código da aplicação
COPY . .

EXPOSE 8000

# Inicia a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
