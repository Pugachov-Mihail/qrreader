FROM python:3.10-slim-buster
WORKDIR /code
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y build-essential libzbar-dev
CMD ["uvicorn", "work.main:app", "--host", "127.0.0.1", "--port", "8000"]