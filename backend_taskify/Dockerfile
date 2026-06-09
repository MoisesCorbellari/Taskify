# Build das dependências
FROM python:3.14-slim AS builder

WORKDIR /app

# Instala compilador
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instala dependências Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt


# Imagem final
FROM python:3.14-slim

# Configurações do Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copia dependências instaladas
COPY --from=builder /install /usr/local

# Cria usuário da aplicação
RUN useradd --create-home --shell /bin/bash appuser

# Copia o código da aplicação
COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 8000

# Inicia a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]