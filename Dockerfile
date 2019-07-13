FROM python:3.7-alpine
MAINTAINER Ashraf

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /recurements.txt
RUN pip install -r /requirements.txt


RUN  mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
