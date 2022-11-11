FROM python:3.10-slim
WORKDIR /code
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y build-essential libzbar-dev