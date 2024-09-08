# Desafio 86

Analisando dados em tempo real com Apache Kafka

## Explicação

### Ferramentas Utilizadas

- `kafka-python`: Biblioteca para interagir com Apache Kafka em Python.
- `numpy`: Biblioteca para computação numérica eficiente.
- `matplotlib.pyplot`: Biblioteca para criação de gráficos em Python.

### Funções Principais

- `KafkaConsumer()`: Cria um consumidor Kafka.
- `consumer.poll()`: Recupera mensagens do Kafka.
- `plt.ion()`: Ativa o modo interativo do Matplotlib.
- `ax.plot()`: Cria um gráfico de linha.

## Resultado

```py
import numpy as np
import matplotlib.pyplot as plt
from kafka import KafkaConsumer

topic = 'sensor-data'
bootstrap_servers = ['localhost:9092']

consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, auto_offset_reset='latest')

data = []

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(data)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

while True:
    for message in consumer.poll(timeout_ms=1000).values():
        for record in message:
            value = float(record.value.decode('utf-8'))
            data.append(value)
            if len(data) > 100:
                data.pop(0)
            line.set_ydata(data)
            line.set_xdata(np.arange(len(data)))
            ax.draw_artist(ax.patch)
            ax.draw_artist(line)
            fig.canvas.flush_events()