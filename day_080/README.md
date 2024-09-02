# Desafio 80

Trabalhando com mensagens assíncronas usando RabbitMQ

## Explicação

### Ferramentas Utilizadas

- `pika`: Biblioteca para interagir com RabbitMQ em Python.

### Funções Principais

- `pika.BlockingConnection()`: Cria uma conexão com o servidor RabbitMQ.
- `channel.queue_declare()`: Declara uma fila.
- `channel.basic_publish()`: Publica uma mensagem na fila.
- `channel.basic_consume()`: Consome mensagens da fila.
- `channel.start_consuming()`: Inicia o consumo de mensagens.

## Resultado

### Producer (PRODUCER.PY)

```python
import pika

def enviar_mensagem(mensagem):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='fila', durable=True)

    channel.basic_publish(
        exchange='',
        routing_key='fila',
        body=mensagem,
        properties=pika.BasicProperties(
            delivery_mode=2,
        ))
    print(f" [x] Enviado: {mensagem}")
    connection.close()

if __name__ == '__main__':
    mensagem = input("Digite a mensagem a ser enviada: ")
    enviar_mensagem(mensagem)
```

### Consumer (DAY_080.PY)

```py
import pika
import time

def callback(ch, method, properties, body):
    print(f" [x] Recebido: {body}")
    time.sleep(body.count(b'.'))
    print(" [x] Feito")
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='fila', durable=True)
print(' [*] Aguardando mensagens. Para sair pressione CTRL+C')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='fila', on_message_callback=callback)

channel.start_consuming()
```