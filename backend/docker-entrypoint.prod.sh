#!/bin/sh
#exec python manage.py check --deploy
export DJANGO_SETTINGS_MODULE="backend.settings.production"

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done


python manage.py collectstatic --noinput

gunicorn backend.wsgi:application --bind 0.0.0.0:7999