#!/bin/sh

set -e

echo "Running migrations..."

alembic upgrade head

echo "Starting FastAPI..."

exec python run.py