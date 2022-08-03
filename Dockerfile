FROM python:latest

WORKDIR /code
COPY . ./
RUN ls -a
RUN pip install -r requirements.txt