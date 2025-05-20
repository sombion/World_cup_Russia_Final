#!/bin/bash

export PYTHONPATH=/app

alembic upgrade head

python backend/default/init_data.py

gunicorn backend.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000