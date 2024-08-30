import socket
import threading

def receber_mensagens(cliente):
    """
    Recebe mensagens do servidor e as exibe.
    """
    while True:
        try:
            mensagem = cliente.recv(1024).decode()
            if mensagem:
                print(mensagem)
            else:
                cliente.close()
                break
        except:
            cliente.close()
            break

def enviar_mensagens(cliente):
    """
    Envia mensagens do usuário para o servidor.
    """
    while True:
        mensagem = input()
        cliente.send(mensagem.encode())

def cliente():
    """
    Conecta-se ao servidor de chat e permite enviar e receber mensagens.
    """
    host = 'localhost'
    porta = 12345

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))

    thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,))
    thread_receber.start()

    thread_enviar = threading.Thread(target=enviar_mensagens, args=(cliente,))
    thread_enviar.start()

if __name__ == '__main__':
    cliente()