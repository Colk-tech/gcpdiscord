FROM python:3.8.8-slim
USER root
MAINTAINER Colk-tech <iam@colk.dev>

ENV LC_ALL=en_US.UTF-8 \
    TZ=JST-9 \
    TERM=xtermdocker-attachingdocker-attaching

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    locales postgresql-client \
    && apt-get upgrade -y \
    && localedef -f UTF-8 -i en_US en_US.UTF-8

RUN mkdir -p /deploy/gcpdiscord
COPY ./Pipfile /deploy/gcpdiscord/Pipfile
COPY ./Pipfile.lock /deploy/gcpdiscord/Pipfile.lock

WORKDIR /deploy/gcpdiscord

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install pipenv \
    && pipenv sync --system --dev

RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
