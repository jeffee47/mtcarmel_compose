FROM python:3.10.9-slim-buster
RUN pip install --upgrade pip
RUN mkdir -p /usr/src/flask_app
WORKDIR /usr/src/flask_app

COPY requirements.txt /requirements.txt
COPY flaskapp.py /usr/src/flask_app/flaskapp.py
RUN pip install -r /requirements.txt
