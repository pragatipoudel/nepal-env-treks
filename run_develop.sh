#!/bin/bash

sass --watch scss:static/css &
python manage.py migrate --no-input
python manage.py runserver 0.0.0.0:8000
