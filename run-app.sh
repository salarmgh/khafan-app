#!/bin/bash

docker build -t khafan_app:v1 ./
docker run -p 5000:5000 -e MYSQL_DATABASE_HOST=172.17.0.2 khafan_app:v1
