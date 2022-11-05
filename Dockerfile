FROM python:3.10-slim-buster
WORKDIR /code
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "work.main:app", "--host", "0.0.0.0", "--port", "80"]