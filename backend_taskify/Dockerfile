# Build: instala dependências Python
FROM python:3.14-slim AS builder

WORKDIR /app

# Compilador necessário para alguns pacotes
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt .

# Instala dependências em diretório temporário
RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt


# Imagem final para execução
FROM python:3.14-slim

# Configurações do Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copia apenas as dependências instaladas
COPY --from=builder /install /usr/local

# Copia o código da aplicação
COPY . .

# Usuário sem privilégios (segurança)
RUN useradd -m appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]