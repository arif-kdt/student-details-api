#!/usr/bin/env bash
# build.sh — placed in project root (same folder as manage.py)
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
