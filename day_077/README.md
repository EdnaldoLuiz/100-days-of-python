# Desafio 77

Construindo um sistema básico de chat com sockets

## Explicação

### Ferramentas Utilizadas

- `socket`: Biblioteca padrão do Python para comunicação de rede.
- `threading`: Biblioteca padrão do Python para criação e gerenciamento de threads.

### Funções Principais

- `socket.socket()`: Cria um novo socket.
- `socket.bind()`: Associa o socket a um endereço e porta.
- `socket.listen()`: Coloca o socket em modo de escuta.
- `socket.accept()`: Aceita uma conexão.
- `socket.recv()`: Recebe dados do socket.
- `socket.send()`: Envia dados pelo socket.

## Resultado

### Servidor (DAY_077_SERVER.PY)

```python
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
```

## Cliente (DAY_077_CLIENT.PY)

```py
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
```