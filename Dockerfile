# syntax=docker/dockerfile:1
FROM python:3.9-alpine

WORKDIR /app

COPY requirements.ini .
RUN pip install -r requirements.ini

COPY app/ .

CMD [ "python", "./service.py" ]