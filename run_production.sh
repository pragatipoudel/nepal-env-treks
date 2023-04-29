#!/bin/bash

sass --update scss:static/css
python manage.py collectstatic --no-input
python manage.py migrate --no-input
uwsgi --socket /socket/nep_env_treks.sock --module nep_env_treks.wsgi --chmod-socket=666
