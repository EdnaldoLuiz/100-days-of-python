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