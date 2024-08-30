import socket
import threading

# Lista para armazenar os clientes conectados
clientes = []

def broadcast(mensagem, cliente_atual):
    """
    Envia a mensagem para todos os clientes, exceto o remetente.
    """
    for cliente in clientes:
        if cliente != cliente_atual:
            try:
                cliente.send(mensagem)
            except:
                cliente.close()
                clientes.remove(cliente)

def handle_cliente(cliente):
    """
    Lida com a comunicação com um cliente específico.
    """
    while True:
        try:
            mensagem = cliente.recv(1024)
            if mensagem:
                print(f"Mensagem recebida: {mensagem.decode()}")
                broadcast(mensagem, cliente)
            else:
                cliente.close()
                clientes.remove(cliente)
                break
        except:
            cliente.close()
            clientes.remove(cliente)
            break

def servidor():
    """
    Cria um servidor de chat que escuta em uma porta e retransmite mensagens.
    """
    host = 'localhost'
    porta = 12345

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(5)

    print(f"Servidor escutando em {host}:{porta}")

    while True:
        cliente, endereco = servidor.accept()
        print(f"Conexão de {endereco}")
        clientes.append(cliente)
        thread = threading.Thread(target=handle_cliente, args=(cliente,))
        thread.start()

if __name__ == '__main__':
    servidor()