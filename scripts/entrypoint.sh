#!/usr/bin/env bash

set -ex

# docker compose up

pip install --upgrade pip && \
    pip install pipenv && \
    pipenv sync --dev && \
    pipenv shell && \
    exit 0

python site/manage.py migrate && \
    python site/manage.py runserver
