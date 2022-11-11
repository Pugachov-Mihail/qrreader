FROM tiangolo/uvicorn-gunicorn:python3.9-slim

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN apt-get update

RUN apt-get install -y build-essential libzbar-dev

COPY app /app/app

RUN cd app
RUN mkdir "application"
