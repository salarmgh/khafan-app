#!/bin/bash

docker run -p 3380:3306 -e MYSQL_ROOT_PASSWORD="root" -e MYSQL_DATABASE="khafan_app" mysql:8.3.0
