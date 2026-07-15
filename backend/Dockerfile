# Build das dependências
FROM python:3.14-slim-trixie AS builder

WORKDIR /app

# Dependências necessárias para compilar extensões C, caso algum pacote 
# não possua wheel pré-compilada.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \ 
    gcc \ 
    python3-dev \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instala dependências Python
RUN python -m pip install --upgrade pip && \
    python -m pip install \
    --no-cache-dir \ 
    --prefix=/install \
    -r requirements.txt

# Imagem final
FROM python:3.14-slim-trixie

# Configurações do Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Biblioteca cliente do PostgreSQL necessária em tempo de execução.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq5 && \
    rm -rf /var/lib/apt/lists/*

# Copia dependências instaladas
COPY --from=builder /install /usr/local

COPY . .

EXPOSE 8000

# Inicia a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]