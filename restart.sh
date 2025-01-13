#!/bin/sh

# echo y | docker container rm django
# echo y | docker container prune
# docker-compose run django python manage.py migrate
# docker stop db
# docker rm django db
# docker-compose rm django
# docker rmi django-api-service-webdjango:latest
# docker-compose up webdjango

docker compose down
docker rm -f django-api-service-webdjango
docker rmi django-api-service-webdjango
docker compose up --build -d