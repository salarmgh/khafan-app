#!/bin/bash

docker run -p 8080:80 -v $PWD/nginx.conf:/etc/nginx/conf.d/default.conf:ro nginx:1.25-alpine3.18
