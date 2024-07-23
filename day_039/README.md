# Desafio 39

Criando um servidor simples com `socket` e trocando mensagens

## Explicação

### Ferramentas Utilizadas

- `socket`: Biblioteca padrão do Python para comunicação de rede.

### Funções Principais

- `socket.socket()`: Cria um novo socket.
- `socket.bind()`: Associa o socket a um endereço e porta.
- `socket.listen()`: Coloca o socket em modo de escuta.
- `socket.accept()`: Aceita uma conexão.
- `socket.recv()`: Recebe dados do socket.
- `socket.send()`: Envia dados pelo socket.

## Resultado

```py
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
        conexao, endereco = servidor.accept()
        print(f"Conectado por {endereco}")

        while True:
            dados = conexao.recv(1024)
            if not dados:
                break
            print(f"Recebido: {dados.decode()}")
            conexao.sendall(dados)

        conexao.close()

if __name__ == '__main__':
    servidor()