#!/bin/sh

# echo y | docker container rm django
# echo y | docker container prune
# docker-compose run django python manage.py migrate
docker stop db
docker rm django db
docker rmi django-api-service-webdjango:latest
docker-compose up webdjango
