FROM python:3.10-slim-buster
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY ./work /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]