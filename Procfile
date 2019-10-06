release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn teacher_app.wsgi --log-file -
