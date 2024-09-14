FROM openjdk:11-slim

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz && \
    tar -xzf spark-3.1.2-bin-hadoop3.2.tgz && \
    mv spark-3.1.2-bin-hadoop3.2 /usr/local/spark && \
    rm spark-3.1.2-bin-hadoop3.2.tgz

ENV SPARK_HOME=/usr/local/spark
ENV PATH=$SPARK_HOME/bin:$PATH

RUN pip3 install pyspark

COPY day_092.py /app/day_092.py

WORKDIR /app

CMD ["python3", "day_092.py"]