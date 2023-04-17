python manage.py migrate --no-input
#python manage.py collectstatic --no-input

gunicorn -c gunicorn.conf.py uni_shortener.wsgi:application --preload