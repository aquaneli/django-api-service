#!/bin/sh

# echo y | docker container rm django
echo y | docker container prune
docker rmi django-api-service-webdjango:latest
docker-compose up
