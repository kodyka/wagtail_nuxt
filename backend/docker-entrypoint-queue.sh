#!/bin/sh
# python manage.py migrate --no-input
# exec gunicorn backend.wsgi:application --bind 0.0.0.0:7999 --workers 3
until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done


# python manage.py collectstatic --noinput

python3 manage.py qcluster