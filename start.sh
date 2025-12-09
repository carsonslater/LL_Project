#!/bin/bash

# Run Migrations

python manage.py migrate

# Start gunicorn

gunicorn learning_log.wsgi:application
