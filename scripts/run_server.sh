#!/usr/bin/env bash

set -ex

python site/manage.py migrate && \
    python site/manage.py runserver 0.0.0.0:8000
