# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Instalar dependências do sistema operacional
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar Redis
RUN wget http://download.redis.io/redis-stable.tar.gz && \
    tar xvzf redis-stable.tar.gz && \
    cd redis-stable && \
    make && \
    make install

# Instalar Scrapy e Scrapy-Redis
RUN pip install scrapy scrapy-redis

# Copiar o projeto Scrapy para o contêiner
COPY myproject /app/myproject

# Definir o diretório de trabalho
WORKDIR /app/myproject

# Comando para iniciar o Redis e o Scrapy
CMD ["sh", "-c", "redis-server & scrapy runspider myproject/spiders/example_spider.py"]