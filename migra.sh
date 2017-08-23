#!/usr/bin/env bash

#Borrramos todas las migraciones
rm -r personas/migrations
rm -r localidades/migrations
rm -r actas/migrations
rm -r grados/migrations
rm -r salud/migrations
rm ./db.sqlite3

#Creamos todas las tablas
python manage.py makemigrations personas
python manage.py makemigrations localidades
python manage.py makemigrations actas
python manage.py makemigrations grados
python manage.py makemigrations salud
python manage.py migrate

#insertamos datos iniciales
python manage.py loaddata grados/dumps/rango.json
python manage.py loaddata grados/dumps/escalafon.json
python manage.py loaddata grados/dumps/grado.json
python manage.py loaddata localidades/dumps/pais.json
python manage.py loaddata localidades/dumps/provincia.json
python manage.py loaddata localidades/dumps/localidad.json
python manage.py loaddata personas/dumps/entidad.json
python manage.py loaddata personas/dumps/persona.json
python manage.py loaddata personas/dumps/user.json
python manage.py loaddata personas/dumps/bombero.json
python manage.py loaddata personas/dumps/parentesco.json

#creamos super usuario y corremos en desarrollo
python manage.py createsuperuser
python manage.py runserver
