#!/usr/bin/env bash

set -ex

python manage.py migrate && \
    DJANGO_SUPERUSER_PASSWORD=admin python manage.py createsuperuser \
    --no-input --username admin --email foobar@gmail.com && \
    python manage.py runserver 0.0.0.0:8000
