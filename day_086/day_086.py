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
ax.set_title('Analisando Dados em Tempo Real')
ax.set_xlabel('Tempo')
ax.set_ylabel('Valor')

for message in consumer:
    value = float(message.value.decode('utf-8'))
    data.append(value)
    line.set_ydata(data)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    fig.canvas.flush_events()

consumer.close()
print('Consumidor Kafka fechado com sucesso.')