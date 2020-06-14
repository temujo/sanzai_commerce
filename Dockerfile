FROM python:3.8.3-slim-buster
MAINTAINER Temuujin Natsagnyam <temuujin.natsagnyam@gmail.com>

ENV INSTALL_PATH /sanzai
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "sanzai.app:create_app()"
