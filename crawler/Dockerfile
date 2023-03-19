FROM python:3.8

RUN apt-get update && apt-get install -y build-essential

WORKDIR /crawler

COPY . .

RUN pip install -r requirements.txt

