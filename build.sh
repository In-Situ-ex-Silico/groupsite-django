#!/usr/bin/env bash
# exit on error
set -o errexit
set -o pipefail
set -o xtrace

pip install -r requirements/deployment.txt

python manage.py collectstatic --no-input
python manage.py migrate
