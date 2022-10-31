# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster


ARG container_name
ENV CONTAINER_NAME $container_name

WORKDIR /$CONTAINER_NAME

COPY requierments.txt requierments.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requierments.txt

CMD [ "python3", "read.py"]
