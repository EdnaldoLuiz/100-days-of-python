FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openjdk-11-jdk \
    wget \
    gnupg

RUN wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.13-2.8.0.tgz && \
    tar -xzf kafka_2.13-2.8.0.tgz && \
    mv kafka_2.13-2.8.0 /usr/local/kafka

RUN pip3 install numpy matplotlib kafka-python

COPY day_086.py /app/day_086.py

WORKDIR /app

CMD ["/bin/bash", "-c", "/usr/local/kafka/bin/zookeeper-server-start.sh /usr/local/kafka/config/zookeeper.properties & \
                        sleep 10 && \
                        /usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server.properties & \
                        sleep 10 && \
                        python3 day_086.py"]