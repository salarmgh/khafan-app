FROM python:3.12.1-alpine3.19

WORKDIR /app

COPY ["requirements.txt", "/app/"]

RUN ["pip", "install", "-r", "requirements.txt"]

COPY ["./", "/app/"]

CMD ["flask", "--app", "khafan_app_db", "--debug", "run", "--host", "0.0.0.0"]
