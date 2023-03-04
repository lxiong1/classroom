#!/usr/bin/env bash

set -ex

pip install --upgrade pip &&
pip install pipenv &&
pipenv requirements > requirements.txt &&
pip install -r requirements.txt
