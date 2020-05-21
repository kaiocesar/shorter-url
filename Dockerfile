FROM python:3.6-stretch

WORKDIR /usr/src/core

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev -y

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/core/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/core