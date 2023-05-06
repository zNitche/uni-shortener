python manage.py makemigrations --no-input
python manage.py migrate --no-input

gunicorn -c gunicorn.conf.py uni_shortener.wsgi:application --preload