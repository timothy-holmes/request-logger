FROM python:latest

WORKDIR /code
COPY . ./
RUN ls -a -R
RUN pip install -r requirements.txt