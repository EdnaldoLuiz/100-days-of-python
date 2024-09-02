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