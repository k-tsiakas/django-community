#!/bin/bash
docker rmi $(docker images -f "dangling=true" -q) #remove all none images
docker rm $(docker ps -a -f status=exited -q) #remove all exited containers
docker-compose up --remove-orphans --build 
