import socket

def servidor():
    """
    Cria um servidor simples que escuta em uma porta e exibe mensagens recebidas.
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

        mensagem = cliente.recv(1024).decode()
        print(f"Mensagem recebida: {mensagem}")

        resposta = f"Recebido: {mensagem}"
        cliente.send(resposta.encode())

        cliente.close()

if __name__ == '__main__':
    servidor()