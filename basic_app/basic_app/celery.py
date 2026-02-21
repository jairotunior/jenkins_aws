"""
Celery application for pactum_backend.

Usage:
    celery -A basic_app worker -l info
    celery -A basic_app beat -l info
"""

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basic_app.settings")

app = Celery("basic_app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
