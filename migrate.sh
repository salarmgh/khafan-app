#!/bin/sh

flask --app khafan_app_db db init
flask --app khafan_app_db db migrate
flask --app khafan_app_db db upgrade
