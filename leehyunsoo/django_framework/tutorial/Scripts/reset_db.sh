#!/usr/bin/env bash

rm -f tmp.db db.sqllite3
rm -r snippets/migrations
python manage.py makemigrations snippets
python manage.py migrate