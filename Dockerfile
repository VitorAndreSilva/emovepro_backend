FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml pdm.lock* /app/
RUN pip install pdm && pdm install --prod

COPY . /app

CMD ["pdm", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]