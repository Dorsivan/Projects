FROM python:3.7

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /
WORKDIR /app