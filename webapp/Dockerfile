FROM python:3.9.0-slim-buster as builder

WORKDIR /usr/src/app

RUN mkdir -p /var/logs/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update --no-install-recommends && \
  pip install --upgrade pip && \
  pip install pipenv

FROM builder as package

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./Pipfile* ./

RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt
FROM package as webapp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .
