#!/bin/bash
docker rmi $(docker images -f "dangling=true" -q) #remove all none images
docker rm $(docker ps -a -f status=exited -q) #remove all exited containers
docker-compose -f docker-compose.prod.yml up --remove-orphans --build -d
docker-compose -f docker-compose.prod.yml exec prod-django-community python manage.py migrate --noinput
