FROM python:latest

WORKDIR /code
COPY . ./
RUN ls -R
# RUN pip3 install pipreqs
# RUN pipreqs --force
RUN pip3 install -r requirements.txt