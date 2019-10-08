#!/bin/sh

echo "+++++++++++++++++ Start up virtualenvironment ++++++++++++++++++++++++"
source /root/.local/share/virtualenvs/teacher_app-api-*/bin/activate
echo "------------------- Virtualenv started ------------------------"

echo "+++++++++++++++++ Export Environmets vars ++++++++++++++++++++++++"
source .env
echo "------------------- Exportiing Done ------------------------"

sleep 10
echo "+++++++++++++++++ Initialize database migrations ++++++++++++++++++++++++"
python manage.py makemigrations
echo "------------------- Initialize database migrations Done!!! ------------------------"

echo "+++++++++++++++++ Make migrations ++++++++++++++++++++++++"
python manage.py migrate
echo "------------------- Make migrations Done !!! ------------------------"

echo "+++++++++++++++++ Start up the server ++++++++++++++++++++++++"
python manage.py runserver 0.0.0.0:8000
echo "------------------- Development server up and running ------------------------"