FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    rabbitmq-server

RUN pip3 install pika

COPY day_080.py /app/day_080.py
COPY producer.py /app/producer.py

WORKDIR /app

CMD ["sh", "-c", "rabbitmq-server start & sleep 10 && python3 day_080.py"]