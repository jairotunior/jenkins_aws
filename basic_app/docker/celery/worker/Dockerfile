# Dockerfile for pactum_backend: Django app, Celery worker, and Celery beat
# Same image is used for all three; the command is overridden in docker-compose.

FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install OS dependencies (optional, for packages that need build tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements/requirements.txt requirements/requirements.txt
RUN pip install --no-cache-dir -r requirements/requirements.txt

# Copy application code
COPY . .

ENV DJANGO_SETTINGS_MODULE="basic_app.settings"

CMD celery -A basic_app worker -B --autoscale 6,2 -Q default --loglevel=INFO