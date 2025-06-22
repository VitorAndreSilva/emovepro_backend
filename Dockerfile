FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libmagic-dev \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml pdm.lock* /app/
RUN pip install pdm
RUN pdm config -l
RUN pdm install --no-dev

COPY . /app

CMD ["pdm", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]