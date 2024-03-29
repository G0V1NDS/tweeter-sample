#!/bin/sh
set -e

# until psql $DATABASE_URL -c '\l'; do
#   >&2 echo "Postgres is unavailable - sleeping"
#   sleep 1
# done

# >&2 echo "Postgres is up - continuing"
if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    # /venv/bin/python manage.py makemigrations --noinput
    /venv/bin/python manage.py migrate --noinput
fi

if [ "x$DJANGO_MANAGEPY_COLLECTSTATIC" = 'xon' ]; then
    /venv/bin/python manage.py collectstatic --noinput
fi

exec "$@"

/venv/bin/gunicorn --bind :8000 --workers $(expr $(grep -c ^processor /proc/cpuinfo 2>/dev/null || sysctl -n hw.ncpu || echo '1') \* 2 \+ 1) main.wsgi:application --reload
