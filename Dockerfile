FROM python:3.12.1-alpine3.19

WORKDIR /app

RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev
COPY ["requirements.txt", "/app/"]

RUN ["pip", "install", "-r", "requirements.txt"]
RUN apk del .build-deps

COPY ["./", "/app/"]

CMD ["flask", "--app", "khafan_app_db", "--debug", "run", "--host", "0.0.0.0"]
