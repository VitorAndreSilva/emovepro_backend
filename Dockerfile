FROM python:3.11-slim

WORKDIR /app

# Instala dependências do sistema necessárias para o python-magic
RUN apt-get update && apt-get install -y \
    libmagic-dev \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instala dependências Python
COPY pyproject.toml pdm.lock ./
RUN pip install --no-cache-dir pdm
RUN pdm install --prod

COPY . .

CMD ["pdm", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]